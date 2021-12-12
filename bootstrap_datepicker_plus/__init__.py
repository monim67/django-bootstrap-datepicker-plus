def _make_version(major, minor, micro, releaselevel, serial):
    """Create a readable version string from version_info tuple components."""
    assert releaselevel in ["alpha", "beta", "candidate", "final"]
    version = "%d.%d.%d" % (major, minor, micro)
    if releaselevel != "final":
        short = {"alpha": "a", "beta": "b", "candidate": "rc"}[releaselevel]
        version += "%s%d" % (short, serial)
    return version


version_info = (4, 0, 0, "final", 0)
__version__ = _make_version(*version_info)
