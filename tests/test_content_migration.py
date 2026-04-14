def test_migrate_content_inserts_yaml_comment_frontmatter(sandbox_project, run_script):
    md_file = sandbox_project / "content" / "tema.md"
    md_file.write_text("# Tema\n\nLa funcion es $f(x)=x^2$.\n", encoding="utf-8")

    result = run_script(sandbox_project, "scripts/migrate_content_yaml_frontmatter.py")

    assert result.returncode == 0, (
        f"La migracion debio pasar.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    updated = md_file.read_text(encoding="utf-8")
    assert updated.startswith("<!--\nyaml_frontmatter:")
    assert "metadata_path:" in updated
    assert "## Glosario de variables" in updated


def test_migrate_content_is_idempotent(sandbox_project, run_script):
    md_file = sandbox_project / "content" / "tema.md"
    md_file.write_text("# Tema\n\nLa funcion es $f(x)=x^2$.\n", encoding="utf-8")

    first = run_script(sandbox_project, "scripts/migrate_content_yaml_frontmatter.py")
    second = run_script(sandbox_project, "scripts/migrate_content_yaml_frontmatter.py")

    assert first.returncode == 0
    assert second.returncode == 0

    updated = md_file.read_text(encoding="utf-8")
    assert updated.count("yaml_frontmatter:") == 1
    assert updated.count("## Glosario de variables") == 1
