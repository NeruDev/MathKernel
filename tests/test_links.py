
from utils.links import detect_broken_internal_links


def test_detect_broken_internal_links_reports_missing(tmp_path):
    ok_page = tmp_path / "ok.html"
    ok_page.write_text("<html><body>ok</body></html>", encoding="utf-8")

    page = tmp_path / "index.html"
    page.write_text(
        """
        <html><body>
            <a href=\"ok.html\">ok</a>
            <a href=\"missing.html\">missing</a>
            <a href=\"https://example.com\">external</a>
            <a href=\"#top\">anchor</a>
            <a href=\"styles.css\">css</a>
        </body></html>
        """,
        encoding="utf-8",
    )

    broken = detect_broken_internal_links([str(page)])

    assert (str(page), "missing.html") in broken
    assert (str(page), "ok.html") not in broken
    assert all(link != "https://example.com" for _, link in broken)
