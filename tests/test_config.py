from pathlib import Path

from scripts.config import BuildConfig, Paths


def test_paths_from_project_root(tmp_path):
    paths = Paths.from_project_root(tmp_path)

    assert paths.project_root == Path(tmp_path)
    assert paths.content_dir == Path(tmp_path) / "content"
    assert paths.metadata_content_dir == Path(tmp_path) / "metadata" / "content"
    assert paths.metadata_scripts_dir == Path(tmp_path) / "metadata" / "scripts"
    assert paths.site_dir == Path(tmp_path) / "site"


def test_build_config_flags_defaults(tmp_path):
    config = BuildConfig(paths=Paths.from_project_root(tmp_path))

    assert config.verbose is False
    assert config.continue_on_error is False
    assert config.skip_validation is False
    assert config.with_assets is False
