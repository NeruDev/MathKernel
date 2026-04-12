def test_site_generation_execution(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/generate_site.py")

    assert result.returncode == 0, (
        f"La generacion del sitio fallo.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
    assert (sandbox_project / "site" / "pages" / "tema.html").exists()
    assert (sandbox_project / "site" / "index.html").exists()
    assert (sandbox_project / "site" / "pages" / "index.html").exists()
    assert (sandbox_project / "site" / "glossary.html").exists()

    html = (sandbox_project / "site" / "pages" / "tema.html").read_text(encoding="utf-8")
    assert 'href="tema.html"' in html
