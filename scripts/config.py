from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    project_root: Path
    content_dir: Path
    metadata_dir: Path
    metadata_content_dir: Path
    metadata_assets_dir: Path
    schemas_dir: Path
    assets_dir: Path
    assets_graphics_dir: Path
    site_src_dir: Path
    site_dir: Path
    template_path: Path
    scripts_dir: Path

    @classmethod
    def from_project_root(cls, project_root: Path | None = None) -> "Paths":
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
    paths: Paths
    verbose: bool = False
    continue_on_error: bool = False
    skip_validation: bool = False
    with_assets: bool = False
