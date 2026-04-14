# yaml_frontmatter:
#   id: 'config'
#   script_path: 'scripts/config.py'
#   metadata_path: 'metadata/scripts/config.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Configuracion central de rutas y flags de build'
#   key_functions:
#     - 'Paths.from_project_root'
#   tags:
#     - 'configuracion'
#     - 'rutas'
#     - 'build'

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    """Agrupa rutas canonicas del proyecto para scripts y build."""

    project_root: Path
    content_dir: Path
    metadata_dir: Path
    metadata_content_dir: Path
    metadata_assets_dir: Path
    metadata_scripts_dir: Path
    schemas_dir: Path
    assets_dir: Path
    assets_graphics_dir: Path
    site_src_dir: Path
    site_dir: Path
    template_path: Path
    scripts_dir: Path

    @classmethod
    def from_project_root(cls, project_root: Path | None = None) -> "Paths":
        """Construye un conjunto de rutas absoluto a partir de la raiz del repo."""

        root = Path(project_root) if project_root else Path(__file__).resolve().parents[1]
        metadata_dir = root / "metadata"
        assets_dir = root / "assets"
        site_src_dir = root / "site_src"

        return cls(
            project_root=root,
            content_dir=root / "content",
            metadata_dir=metadata_dir,
            metadata_content_dir=metadata_dir / "content",
            metadata_assets_dir=metadata_dir / "assets" / "images" / "grafics",
            metadata_scripts_dir=metadata_dir / "scripts",
            schemas_dir=metadata_dir / "schemas",
            assets_dir=assets_dir,
            assets_graphics_dir=assets_dir / "images" / "grafics",
            site_src_dir=site_src_dir,
            site_dir=root / "site",
            template_path=site_src_dir / "template_page.html",
            scripts_dir=root / "scripts",
        )


@dataclass(frozen=True)
class BuildConfig:
    """Flags de ejecucion para el pipeline principal de build."""

    paths: Paths
    verbose: bool = False
    continue_on_error: bool = False
    skip_validation: bool = False
    with_assets: bool = False
