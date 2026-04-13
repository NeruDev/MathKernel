def test_link_assets_to_content(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/build.py")
    assert result.returncode == 0

    md_file = sandbox_project / "content" / "tema.md"
    updated_content = md_file.read_text(encoding="utf-8")

    assert "![Circulo unitario](assets/images/grafics/00_fundamentos/tema/circulo.svg)" in updated_content
    assert "## 1.1 Seccion" in updated_content


def test_link_assets_no_duplicates(sandbox_project, run_script):
    first = run_script(sandbox_project, "scripts/build.py")
    second = run_script(sandbox_project, "scripts/build.py")

    assert first.returncode == 0
    assert second.returncode == 0

    content = (sandbox_project / "content" / "tema.md").read_text(encoding="utf-8")
    img_link = "![Circulo unitario](assets/images/grafics/00_fundamentos/tema/circulo.svg)"
    assert content.count(img_link) == 1
