def test_md_json_mirror_integrity(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/validate_structure.py")

    assert result.returncode == 0, (
        f"La validacion debio pasar.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )


def test_metadata_schema_compliance(sandbox_project, run_script):
    (sandbox_project / "metadata" / "content" / "tema.json").write_text(
        '{"id": "tema", "module": "00_fundamentos", "order": "1", "concepts": ["base"]}',
        encoding="utf-8",
    )

    result = run_script(sandbox_project, "scripts/validate_structure.py")

    assert result.returncode == 1
    assert "Falta campo requerido 'title'" in result.stdout
