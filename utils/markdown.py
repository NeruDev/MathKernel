import re

import markdown


DEFAULT_EXTENSIONS = ["tables", "fenced_code", "toc"]


def convert_md_to_html(md_text, extensions=None):
    active_extensions = extensions or DEFAULT_EXTENSIONS
    html = markdown.markdown(md_text, extensions=active_extensions)

    replacements = len(re.findall(r'href="[^"]+\.md(?:#[^"]*)?"', html))
    html = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', html)

    return html, replacements
