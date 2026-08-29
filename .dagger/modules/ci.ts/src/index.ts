import { dag, Directory, object, func, check, argument } from "@dagger.io/dagger"

const PYTHON_VERSIONS = ["3.14", "3.13", "3.12", "3.11", "3.10"];

@object()
export class CiTs {
  private base(src: Directory, pythonVersion: string) {
    const pipCache = dag.cacheVolume("dbdp-pip")
    const poetryCache = dag.cacheVolume("dbdp-poetry")
    return dag
      .container()
      .from(`python:${pythonVersion}-slim`)
      .withMountedCache("/root/.cache/pip", pipCache)
      .withMountedCache("/root/.cache/pypoetry", poetryCache)
      .withExec(["pip", "install", "--quiet", "poetry"])
      // Mount lock files first — poetry install layer cached until poetry.lock changes.
      .withFile("/app/pyproject.toml", src.file("pyproject.toml"))
      .withFile("/app/poetry.lock", src.file("poetry.lock"))
      .withWorkdir("/app")
      .withExec(["poetry", "install", "--no-root", "--only", "build", "--no-ansi"])
      // Mount only the installable package — pip install layer cached until src/ changes.
      .withDirectory("/app/src", src.directory("src"))
      .withFile("/app/README.rst", src.file("README.rst"))
      .withFile("/app/tests/pip-constraints.txt", src.file("tests/pip-constraints.txt"))
      .withExec(["poetry", "run", "pip", "install", "--quiet", "-c", "tests/pip-constraints.txt", "."])
      // Mount test/dev files last — only busts the pytest layer.
      .withDirectory("/app/tests", src.directory("tests"))
      .withDirectory("/app/dev", src.directory("dev"))
      .withFile("/app/.env.defaults", src.file(".env.defaults"))
  }

  /** Run pytest against a single Python version. */
  @func()
  async test(
    @argument({ defaultPath: "../../..", ignore: [".git", ".venv", "worktrees", ".dagger", ".tox", "htmlcov", "coverage", "pages", "tmp"] }) src: Directory,
    pythonVersion = "3.14",
  ): Promise<string> {
    return this.base(src, pythonVersion).withExec(["poetry", "run", "pytest", "-v"]).stdout()
  }

  /** Run pytest against all supported Python versions in parallel. */
  @func()
  @check()
  async testAll(
    @argument({ defaultPath: "../../..", ignore: [".git", ".venv", "worktrees", ".dagger", ".tox", "htmlcov", "coverage", "pages", "tmp"] }) src: Directory,
  ): Promise<string> {
    const results = await Promise.all(
      PYTHON_VERSIONS.map(async (version) => {
        const out = await this.base(src, version).withExec(["poetry", "run", "pytest", "-v"]).stdout()
        return `--- Python ${version} ---\n${out}`
      }),
    )
    return results.join("\n\n")
  }

  /** Run poe lint (black, isort, pyright, pydocstyle, rstcheck) once. */
  @func()
  async lint(
    @argument({ defaultPath: "../../..", ignore: [".git", ".venv", "worktrees", ".dagger", ".tox", "htmlcov", "coverage", "pages", "tmp"] }) src: Directory,
  ): Promise<string> {
    const pipCache = dag.cacheVolume("dbdp-pip")
    const poetryCache = dag.cacheVolume("dbdp-poetry")
    return dag
      .container()
      .from("python:3.14-slim")
      .withMountedCache("/root/.cache/pip", pipCache)
      .withMountedCache("/root/.cache/pypoetry", poetryCache)
      .withExec(["pip", "install", "--quiet", "poetry"])
      .withFile("/app/pyproject.toml", src.file("pyproject.toml"))
      .withFile("/app/poetry.lock", src.file("poetry.lock"))
      .withWorkdir("/app")
      .withExec(["poetry", "install", "--no-root", "--only", "build", "--no-ansi"])
      .withDirectory("/app", src)
      .withExec(["poe", "lint"])
      .stdout()
  }
}
