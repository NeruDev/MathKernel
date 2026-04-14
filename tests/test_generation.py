def test_site_generation_execution(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/build.py")

    assert result.returncode == 0, (
        f"La generacion del sitio fallo.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
    assert (sandbox_project / "site" / "tema.html").exists()
    assert (sandbox_project / "site" / "index.html").exists()
    assert (sandbox_project / "site" / "glossary.html").exists()

    html = (sandbox_project / "site" / "tema.html").read_text(encoding="utf-8")
    assert 'href="tema.html"' in html


def test_site_generation_ignores_commented_yaml_frontmatter(sandbox_project, run_script):
        content_file = sandbox_project / "content" / "tema.md"
        content_file.write_text(
                """<!--
yaml_frontmatter:
    id: 'tema'
    content_path: 'content/tema.md'
    metadata_path: 'metadata/content/tema.json'
-->

# Tema

Contenido con enlace [interno](tema.md).
""",
                encoding="utf-8",
        )

        result = run_script(sandbox_project, "scripts/build.py")
        assert result.returncode == 0

        html = (sandbox_project / "site" / "tema.html").read_text(encoding="utf-8")
        assert "yaml_frontmatter" not in html
        assert '<a href="tema.html">interno</a>' in html
