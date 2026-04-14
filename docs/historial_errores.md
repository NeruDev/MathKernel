# Historial de errores operativos

Este archivo centraliza incidentes grandes, su diagnostico y las mitigaciones aplicadas.

## 2026-04-13 | Bloqueos de terminal, Pylance persistente y mypy MYPY_EXIT=2

### Contexto

Durante la ejecucion local se observaron bloqueos intermitentes de terminal (PowerShell) al correr checks y pruebas en una sola pasada.

### Incidentes registrados

- Bloqueo de terminal con popup de VS Code (detener proceso / reabrir VS Code) en ejecuciones largas sin checkpoints.
- Proceso persistente de Pylance mostrando notificacion activa de analisis (`14 files and 0 cells to analyze`).
- Warning de Pylance `missingDefaultExcludes` por configuracion personalizada de `python.analysis.exclude` sin incluir patrones por defecto (faltaba `**/.*`).
- Ejecucion de mypy sobre `scripts` completo con `MYPY_EXIT=2`, errores de tipado en scripts de graficos Matplotlib 3D y mensaje `INTERNAL ERROR` de mypy.

### Comando exacto reportado con MYPY_EXIT=2

```powershell
$ErrorActionPreference='Continue'; & .\.venv\Scripts\python.exe -m mypy scripts utils --config-file pyproject.toml --no-error-summary > .mypy-report-local.txt 2>&1; $code=$LASTEXITCODE; Write-Host ('MYPY_EXIT=' + $code); Get-Content .mypy-report-local.txt | Select-Object -Last 40
```

### Causas raiz consolidadas

- Entorno virtual previo inconsistente (metadata de `pyvenv.cfg` de otra ruta/proyecto).
- Ejecucion de tareas pesadas sin segmentacion (tests/build/mypy completo) en una sola corrida.
- `subprocess.run` sin timeout en rutas criticas (`tests/conftest.py` y `scripts/build.py` para `--with-assets`).
- Configuracion de analisis de Pylance incompleta para exclusiones por defecto.

### Mitigaciones aplicadas

- Recreacion completa de `.venv` en la ruta actual del repo y reinstalacion de dependencias.
- Instalacion de tooling local para checkpoints (`ruff`, `mypy`, `pre-commit`, `pytest-timeout`).
- Ajuste de workspace para ejecucion estable:
  - `python.terminal.activateEnvironment = false`
  - `python.analysis.diagnosticMode = openFilesOnly`
  - `python.analysis.exclude` con `**/.*` y exclusiones de carpetas pesadas.
- Ejecucion por checkpoints cortos con python explicito del venv (`.venv\Scripts\python.exe`), evitando corridas monoliticas.

### Protocolo recomendado de ejecucion segura local

```powershell
# CP0: entorno
.\.venv\Scripts\python.exe -m pip check

# CP1: lint
.\.venv\Scripts\python.exe -m ruff check scripts utils tests

# CP2: mypy informativo (alcance estable)
.\.venv\Scripts\python.exe -m mypy scripts/core scripts/io scripts/config.py scripts/validate_encoding.py scripts/validate_markdown_format.py utils --config-file pyproject.toml --no-error-summary

# CP3: validadores
.\.venv\Scripts\python.exe scripts/validate_encoding.py
.\.venv\Scripts\python.exe scripts/validate_markdown_format.py

# CP4: tests por lotes (recomendado)
.\.venv\Scripts\python.exe -m pytest tests/test_config.py tests/test_core_modules.py tests/test_metadata.py tests/test_links.py -q -x --timeout=90
.\.venv\Scripts\python.exe -m pytest tests/test_file_manager.py tests/test_error_handling.py tests/test_markdown_validation.py tests/test_encoding_validation.py -q -x --timeout=90
.\.venv\Scripts\python.exe -m pytest tests/test_content_migration.py tests/test_generation.py tests/test_assets.py tests/test_structure.py -q -x --timeout=120

# CP5/CP6: build
.\.venv\Scripts\python.exe scripts/build.py --verbose
.\.venv\Scripts\python.exe scripts/build.py --with-assets --verbose
```

### Estado de verificacion posterior a mitigaciones

- `pytest tests -q -x --timeout=120`: 32 passed.
- `scripts/build.py --verbose`: exitoso (con alertas informativas de tablas).
- `scripts/build.py --with-assets --verbose`: exitoso (71 assets generados).

### Nota operativa sobre Pylance

Con `python.analysis.diagnosticMode = openFilesOnly`, la notificacion `14 files and 0 cells to analyze` puede mostrarse como actividad informativa de analisis de archivos abiertos. Si queda activa de forma indefinida con consumo anomalo, reiniciar Pylance y recargar la ventana de VS Code antes de continuar con tareas pesadas.

## 2026-04-13 | Continuidad: corte reportado en comando Ruff (CP1)

### Contexto de continuidad

En la continuidad del plan de higiene se reporto detencion de flujo al ejecutar:

```powershell
Set-Location "g:\REPOSITORIOS GITHUB\MathKernel"
.\.venv\Scripts\python.exe -m ruff check scripts utils tests
```

### Diagnostico ejecutado (hosts alternos)

- Host `pwsh` con salida redirigida a `%TEMP%`: comando finalizo en `~200 ms`, `exit code = 1` (hallazgos de Ruff, sin cuelgue).
- Host `cmd.exe` via `Start-Process` con salida redirigida a `%TEMP%`: comando finalizo en `~185 ms`, `exit code = 1` (mismos hallazgos, sin cuelgue).

Conclusión operativa:
- No se reprodujo cuelgue del proceso Ruff.
- El corte previo se clasifica como degradacion puntual del host de terminal integrado (buffer/estado de sesion), no como bloqueo del comando Ruff.

### Mitigacion de contingencia para CP1

1. Ejecutar Ruff con salida redirigida para evitar saturacion de la terminal integrada.
2. Si la terminal integrada se degrada, ejecutar la misma orden en `cmd.exe` o shell externa del sistema.
3. Cuando el arbol sea grande, dividir CP1 por rutas:
  - `scripts/core scripts/io`
  - `utils`
  - `tests`
  - `scripts/grafics` por subcarpetas.

### Comandos de contingencia recomendados

```powershell
# Ruff con salida redirigida (pwsh)
.\.venv\Scripts\python.exe -m ruff check scripts utils tests *> "$env:TEMP\mk_ruff_pwsh.out"

# Ruff en host alterno cmd.exe
Start-Process -FilePath cmd.exe -ArgumentList '/c', '.\\.venv\\Scripts\\python.exe -m ruff check scripts utils tests > "%TEMP%\\mk_ruff_cmd.out" 2>&1' -PassThru -Wait -NoNewWindow
```
