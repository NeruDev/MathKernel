import os
from pathlib import Path


def get_relative_html_path(md_path, base_dir):
    rel_path = os.path.relpath(str(md_path), str(base_dir))
    return rel_path.replace(".md", ".html")


def compute_depth(rel_path):
    parts = Path(rel_path).parts
    return max(len(parts) - 1, 0)


def build_relative_prefix(depth):
    return "../" * max(int(depth), 0)
