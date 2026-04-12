import os
from pathlib import Path


def get_relative_html_path(md_path, base_dir):
    rel_path = os.path.relpath(str(md_path), str(base_dir))
    return rel_path.replace(".md", ".html")


def compute_depth(rel_path):
    return len(Path(rel_path).parts)


def build_relative_prefix(depth):
    return "../" * max(int(depth), 0)
