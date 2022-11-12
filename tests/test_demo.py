import shutil
from pathlib import Path
from typing import List

import urllib3
from pytest_django.live_server_helper import LiveServer


def test_build(live_server: LiveServer) -> None:
    pages = Path.cwd() / "pages"
    if pages.exists():
        shutil.rmtree(pages)
    demo = pages / "demo"
    demo.mkdir(parents=True)
    http = urllib3.PoolManager()
    for path in paths:
        r = http.request("GET", f"{live_server.url}/{path}")
        file_text = r.data.decode("utf-8")
        for search_text, replace_text in replacements:
            file_text = file_text.replace(search_text, replace_text)
        file_path = demo.joinpath(f"{path}/index.html" if path.endswith("/") else path)
        if not file_path.parent.exists():
            file_path.parent.mkdir(parents=True)
        file_path.write_text(file_text)
    pages.joinpath("index.html").write_text(
        '<META http-equiv="refresh" content="0;URL=demo/">'
    )
    pages.joinpath("Bootstrap4.html").write_text(
        '<META http-equiv="refresh" content="0;URL=demo/">'
    )


replacements = [
    (
        '"/bootstrap',
        '"/django-bootstrap-datepicker-plus/demo/bootstrap',
    ),
    (
        "/static/bootstrap_datepicker_plus/",
        "/django-bootstrap-datepicker-plus/demo/static/bootstrap_datepicker_plus/",
    ),
]
paths: List[str] = [
    "bootstrap3/crispy-form.html",
    "bootstrap3/custom-form.html",
    "bootstrap3/django-filter.html",
    "bootstrap3/dynamic-formset.html",
    "bootstrap3/generic-view.html",
    "bootstrap3/model-form.html",
    "bootstrap3/",
    "bootstrap4/crispy-form.html",
    "bootstrap4/custom-form.html",
    "bootstrap4/django-filter.html",
    "bootstrap4/dynamic-formset.html",
    "bootstrap4/generic-view.html",
    "bootstrap4/model-form.html",
    "bootstrap4/",
    "bootstrap5/crispy-form.html",
    "bootstrap5/custom-form.html",
    "bootstrap5/django-filter.html",
    "bootstrap5/dynamic-formset.html",
    "bootstrap5/generic-view.html",
    "bootstrap5/model-form.html",
    "bootstrap5/",
    "./",
    "static/bootstrap_datepicker_plus/css/datepicker-widget.css",
    "static/bootstrap_datepicker_plus/js/datepicker-widget.js",
]
