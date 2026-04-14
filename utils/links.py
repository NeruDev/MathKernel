import os
import re

from .io import read_text

HREF_PATTERN = re.compile(r'href="([^"]+)"')


def detect_broken_internal_links(generated_pages):
    broken_links = []

    for html_path in generated_pages:
        html_content = read_text(html_path)
        links = HREF_PATTERN.findall(html_content)

        for link in links:
            if (
                link.startswith("http://")
                or link.startswith("https://")
                or link.startswith("#")
                or link.startswith("mailto:")
            ):
                continue

            target = link.split("#", 1)[0]
            if not target or target.endswith(".css") or target.endswith(".js"):
                continue

            target_path = os.path.normpath(os.path.join(os.path.dirname(str(html_path)), target))
            if not os.path.exists(target_path):
                broken_links.append((str(html_path), link))

    return broken_links
