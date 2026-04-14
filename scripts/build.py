import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import BuildConfig, Paths
from scripts.core import generators, processors, validators
from scripts.core.error_handling import ErrorCollector, FileOperationError, ProcessingError
from scripts.core.formula_validator import validate_markdown_math_tables
from scripts.io.file_manager import FileManager
from utils.links import detect_broken_internal_links
from utils.logging import log_error, log_info, log_warn
from utils.markdown import convert_md_to_html
from utils.pathing import compute_depth, get_relative_html_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build unificado de MathKernel")
    parser.add_argument("--verbose", action="store_true", help="Muestra logs detallados")
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continua la ejecucion en errores no criticos",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Salta el paso de validacion",
    )
    parser.add_argument(
        "--with-assets",
        action="store_true",
        help="Ejecuta generate_assets.py al inicio",
    )
    return parser.parse_args()


def _load_schema(path: Path, file_manager: FileManager) -> dict:
    return file_manager.read_json(path)


def _utf8_validation_targets(paths: Paths) -> list[Path]:
    return [
        paths.content_dir,
        paths.metadata_dir,
        paths.scripts_dir,
        paths.project_root / "utils",
        paths.site_src_dir,
        paths.project_root / "docs",
        paths.project_root / "README.md",
        paths.project_root / "requirements.txt",
    ]


def validate_project(config: BuildConfig, file_manager: FileManager) -> list[str]:
    paths = config.paths
    errors: list[str] = []

    if not paths.content_dir.exists():
        return [f"No existe la carpeta content/: {paths.content_dir}"]

    errors.extend(validators.validate_utf8_targets(_utf8_validation_targets(paths)))

    md_files = sorted(paths.content_dir.rglob("*.md"))

    content_json_files = [
        path
        for path in sorted(paths.metadata_content_dir.rglob("*.json"))
        if path.name != "schema.json"
    ]

    content_errors, md_rel, content_json_rel = validators.validate_content_mirror(
        md_files,
        content_json_files,
        paths.content_dir,
        paths.metadata_content_dir,
    )
    errors.extend(content_errors)

    assets_svg_files = sorted(paths.assets_graphics_dir.rglob("*.svg")) if paths.assets_graphics_dir.exists() else []
    assets_json_files = [
        path
        for path in sorted(paths.metadata_assets_dir.rglob("*.json"))
        if path.name != "schema.json"
    ]

    assets_errors, svg_rel, assets_json_rel = validators.validate_assets_mirror(
        assets_svg_files,
        assets_json_files,
        paths.assets_graphics_dir,
        paths.metadata_assets_dir,
    )
    errors.extend(assets_errors)

    content_schema = _load_schema(paths.schemas_dir / "content.schema.json", file_manager)
    assets_schema = _load_schema(paths.schemas_dir / "assets.schema.json", file_manager)

    for rel_base in sorted(set(md_rel).intersection(content_json_rel)):
        data = file_manager.read_json(content_json_rel[rel_base])
        errors.extend(
            validators.validate_against_schema(
                data,
                content_schema,
                content_json_rel[rel_base],
            )
        )

    for rel_base in sorted(set(svg_rel).intersection(assets_json_rel)):
        data = file_manager.read_json(assets_json_rel[rel_base])
        errors.extend(
            validators.validate_against_schema(
                data,
                assets_schema,
                assets_json_rel[rel_base],
            )
        )

    return errors


def run_assets_generation(config: BuildConfig, collector: ErrorCollector) -> None:
    script_path = config.paths.scripts_dir / "generate_assets.py"
    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=False,
        cwd=str(config.paths.project_root),
    )

    if result.returncode != 0:
        collector.add_message(
            "generate_assets",
            f"generate_assets.py termino con codigo {result.returncode}",
            critical=True,
        )


def run_assets_linking(config: BuildConfig, file_manager: FileManager, collector: ErrorCollector) -> dict[str, int]:
    paths = config.paths
    linked_count = 0
    skipped_count = 0

    if not paths.metadata_assets_dir.exists():
        log_warn(f"No existe metadata de activos en {paths.metadata_assets_dir}")
        return {"linked": 0, "skipped": 0}

    content_records: list[tuple[str, dict]] = []
    for meta_path in generators.metadata_json_paths(paths.metadata_content_dir):
        try:
            data = file_manager.read_json(meta_path)
            rel_path = meta_path.relative_to(paths.metadata_content_dir).as_posix()
            content_records.append((rel_path, data))
        except FileOperationError as exc:
            collector.add("link_assets", exc)

    md_rel_paths = [
        path.relative_to(paths.content_dir).as_posix()
        for path in sorted(paths.content_dir.rglob("*.md"))
    ]
    script_to_md = processors.build_script_to_md_map(content_records, md_rel_paths)

    asset_meta_files = [
        path
        for path in sorted(paths.metadata_assets_dir.rglob("*.json"))
        if path.name != "schema.json"
    ]

    for json_path in asset_meta_files:
        try:
            asset = file_manager.read_json(json_path)
        except FileOperationError as exc:
            collector.add("link_assets", exc)
            skipped_count += 1
            continue

        asset_id = asset.get("id")
        if not asset_id or asset_id not in script_to_md:
            skipped_count += 1
            continue

        md_rel_path = script_to_md[asset_id]
        md_full_path = paths.content_dir / md_rel_path
        if not md_full_path.exists():
            collector.add_message(
                "link_assets",
                f"Archivo de contenido no encontrado: {md_full_path}",
            )
            skipped_count += 1
            continue

        image_path = asset.get("image_path")
        if not image_path:
            collector.add_message(
                "link_assets",
                f"Asset sin image_path: {json_path}",
            )
            skipped_count += 1
            continue

        description = asset.get("description", "Sin descripcion")
        section = asset.get("section", "")

        try:
            raw_content = file_manager.read_text(md_full_path)
            rel_img_path = processors.get_relative_image_path(md_rel_path, image_path)
            if rel_img_path in raw_content:
                continue

            image_markdown = f"![{description}]({rel_img_path})"
            new_content, inserted, _ = processors.inject_image_markdown(
                raw_content,
                image_markdown,
                section,
            )

            if inserted:
                file_manager.write_text(md_full_path, new_content)
                linked_count += 1
                if config.verbose:
                    log_info(f"Vinculado: {asset_id} -> {md_rel_path}")
            else:
                skipped_count += 1
        except FileOperationError as exc:
            collector.add("link_assets", exc)
            skipped_count += 1

    log_info(f"Vinculacion completada: {linked_count} vinculados, {skipped_count} omitidos")
    return {"linked": linked_count, "skipped": skipped_count}


def run_site_generation(config: BuildConfig, file_manager: FileManager, collector: ErrorCollector) -> list[str]:
    paths = config.paths

    if not paths.site_src_dir.exists():
        raise ProcessingError(f"No existe la carpeta fuente del sitio: {paths.site_src_dir}")

    if paths.site_dir.exists():
        file_manager.remove_dir(paths.site_dir)

    file_manager.copy_dir(paths.site_src_dir, paths.site_dir, merge=False)

    if paths.assets_dir.exists():
        file_manager.copy_dir(paths.assets_dir, paths.site_dir / "assets", merge=True)

    template_html = file_manager.read_text(paths.template_path)

    generated_pages: list[str] = []
    id_to_path: dict[str, str] = {}
    markdown_warning_count = 0

    for md_path in sorted(paths.content_dir.rglob("*.md")):
        rel_path_html = get_relative_html_path(md_path, paths.content_dir)
        out_path = paths.site_dir / rel_path_html
        file_manager.ensure_dir(out_path.parent)

        depth = compute_depth(rel_path_html)
        md_text = file_manager.read_text(md_path)

        markdown_warnings = validate_markdown_math_tables(md_text, md_path)
        markdown_warning_count += len(markdown_warnings)
        if config.verbose and markdown_warnings:
            for warning in markdown_warnings:
                log_warn(warning)

        html_content, conversion_count = convert_md_to_html(
            md_text,
            asset_prefix="../" * depth,
        )
        page_title = generators.format_display_title(md_path.stem)
        page_html = generators.wrap_html(page_title, html_content, template_html, depth)
        file_manager.write_text(out_path, page_html)

        generated_pages.append(str(out_path))
        id_to_path[md_path.stem] = Path(rel_path_html).as_posix()

        if config.verbose:
            log_info(f"Procesado: {md_path} -> {out_path} ({conversion_count} enlaces .md)")

    metadata_records: list[dict] = []
    for meta_path in generators.metadata_json_paths(paths.metadata_content_dir):
        try:
            metadata_records.append(file_manager.read_json(meta_path))
        except FileOperationError as exc:
            collector.add("generate_site", exc)

    index_items, warnings = generators.build_index_items(metadata_records, id_to_path)
    for warning in warnings:
        collector.add_message("generate_site", warning)

    index_body = generators.build_index_body(index_items)
    index_html = generators.wrap_html("Índice de Contenidos", index_body, template_html, depth=0)
    index_path = paths.site_dir / "index.html"
    file_manager.write_text(index_path, index_html)
    generated_pages.append(str(index_path))

    glossary_body = generators.build_glossary_body(metadata_records)
    glossary_html = generators.wrap_html("Glosario", glossary_body, template_html, depth=0)
    glossary_path = paths.site_dir / "glossary.html"
    file_manager.write_text(glossary_path, glossary_html)
    generated_pages.append(str(glossary_path))

    broken_links = detect_broken_internal_links(generated_pages)
    for html_path, link in broken_links:
        collector.add_message("generate_site", f"Enlace interno roto: {link} en {html_path}")

    if markdown_warning_count:
        log_warn(
            "Validacion Markdown informativa: "
            f"{markdown_warning_count} alertas detectadas (no bloqueantes)"
        )

    log_info("Generacion de sitio finalizada")
    return generated_pages


def print_error_summary(collector: ErrorCollector) -> None:
    if not collector.has_errors:
        return

    log_warn("Resumen de incidencias:")
    for line in collector.format_summary():
        if "[CRITICAL]" in line:
            log_error(line)
        else:
            log_warn(line)


def run_build(config: BuildConfig) -> int:
    collector = ErrorCollector()
    file_manager = FileManager()

    log_info("Iniciando build unificado...")

    if config.with_assets:
        run_assets_generation(config, collector)
        if collector.has_critical_errors and not config.continue_on_error:
            print_error_summary(collector)
            return 1

    if not config.skip_validation:
        try:
            validation_errors = validate_project(config, file_manager)
        except FileOperationError as exc:
            collector.add("validation", exc, critical=True)
            print_error_summary(collector)
            return 1

        if validation_errors:
            for error in validation_errors:
                log_error(error)
                collector.add_message("validation", error, critical=True)

            if not config.continue_on_error:
                print_error_summary(collector)
                return 2
        else:
            log_info("Validacion completada correctamente")

    try:
        run_assets_linking(config, file_manager, collector)
    except (FileOperationError, ProcessingError) as exc:
        collector.add("link_assets", exc, critical=True)
        if not config.continue_on_error:
            print_error_summary(collector)
            return 1

    try:
        run_site_generation(config, file_manager, collector)
    except (FileOperationError, ProcessingError) as exc:
        collector.add("generate_site", exc, critical=True)
        if not config.continue_on_error:
            print_error_summary(collector)
            return 1

    print_error_summary(collector)

    if collector.has_errors:
        return 1

    log_info("Build finalizado correctamente")
    return 0


def main() -> int:
    args = parse_args()
    config = BuildConfig(
        paths=Paths.from_project_root(PROJECT_ROOT),
        verbose=args.verbose,
        continue_on_error=args.continue_on_error,
        skip_validation=args.skip_validation,
        with_assets=args.with_assets,
    )

    return run_build(config)


if __name__ == "__main__":
    sys.exit(main())
