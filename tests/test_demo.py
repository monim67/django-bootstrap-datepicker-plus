import shutil
from pathlib import Path

from pytest_django.live_server_helper import LiveServer
from website_downloader.crawler import CrawlOptions, crawl_site


def test_build(live_server: LiveServer) -> None:
    pages = Path.cwd() / "pages"
    if pages.exists():
        shutil.rmtree(pages)
    demo = pages / "demo"
    demo.mkdir(parents=True)
    crawl_options = CrawlOptions(start_url=live_server.url, root=demo, max_pages=500)
    stats = crawl_site(crawl_options)
    assert stats.errors == 0
    pages.joinpath("index.html").write_text(
        '<META http-equiv="refresh" content="0;URL=demo/">'
    )
    pages.joinpath("Bootstrap4.html").write_text(
        '<META http-equiv="refresh" content="0;URL=demo/">'
    )
    pages.joinpath("configure").mkdir(parents=True, exist_ok=True)
    pages.joinpath("configure/index.html").write_text(
        '<META http-equiv="refresh" content="0;URL=https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Getting_Started.html">'
    )
