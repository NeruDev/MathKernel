def test_validate_encoding_script_ok(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/validate_encoding.py")

    assert result.returncode == 0, (
        f"La validacion UTF-8 debio pasar.\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )


def test_validate_encoding_script_detects_invalid_utf8(sandbox_project, run_script):
    bad_file = sandbox_project / "utils" / "bad_encoding.py"
    bad_file.write_bytes(b"\xff\xfe\xfa")

    result = run_script(sandbox_project, "scripts/validate_encoding.py")

    assert result.returncode == 1
    assert "Codificacion no UTF-8" in result.stdout


def test_build_fails_on_invalid_utf8_content(sandbox_project, run_script):
    bad_content = sandbox_project / "content" / "tema.md"
    bad_content.write_bytes(b"\xff\xfe\xfa")

    result = run_script(sandbox_project, "scripts/build.py")

    assert result.returncode == 2
    assert "Codificacion no UTF-8" in result.stdout
