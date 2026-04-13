from pathlib import Path

from utils.pathing import build_relative_prefix, compute_depth


def get_relative_image_path(md_file_rel_path: str, image_path: str) -> str:
    depth = compute_depth(md_file_rel_path)
    prefix = build_relative_prefix(depth)
    return f"{prefix}{image_path}"


def extract_section_id(section_text: str) -> str:
    if not section_text:
        return ""
    return section_text.split(" ")[0].strip()


def build_script_to_md_map(
    content_metadata_records: list[tuple[str, dict]],
    md_rel_paths: list[str],
) -> dict[str, str]:
    script_to_md: dict[str, str] = {}

    md_by_dir: dict[str, str] = {}
    for md_rel in sorted(md_rel_paths):
        directory = Path(md_rel).parent.as_posix()
        md_by_dir.setdefault(directory, md_rel)

    for rel_json_path, data in content_metadata_records:
        scripts = data.get("scripts", [])
        rel_dir = Path(rel_json_path).parent.as_posix()
        target_md = md_by_dir.get(rel_dir)
        if not target_md:
            continue

        for script_name in scripts:
            script_to_md[Path(script_name).stem] = target_md

    return script_to_md


def inject_image_markdown(
    raw_content: str,
    image_markdown: str,
    section_text: str,
) -> tuple[str, bool, str]:
    if image_markdown in raw_content:
        return raw_content, False, "duplicate"

    section_id = extract_section_id(section_text)
    lines = raw_content.splitlines(keepends=True)
    if not lines:
        return f"{image_markdown}\n", True, "appended"

    section_found = False
    new_lines: list[str] = []

    for line in lines:
        new_lines.append(line)
        if section_found:
            continue

        if section_id and section_id != "N/A" and line.startswith("#"):
            stripped = line.strip()
            if (
                f" {section_id} " in line
                or f" {section_id}\n" in line
                or stripped.endswith(f" {section_id}")
            ):
                new_lines.append(f"\n{image_markdown}\n")
                section_found = True

    if section_found:
        return "".join(new_lines), True, "section"

    if new_lines and not new_lines[-1].endswith("\n"):
        new_lines[-1] += "\n"
    new_lines.append(f"\n{image_markdown}\n")
    return "".join(new_lines), True, "appended"
