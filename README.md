# MathKernel

Repositorio educativo de matemáticas orientado a dos tipos de consumo:

- **Humano:** contenido en Markdown con fórmulas LaTeX legibles en navegador.
- **IA:** metadatos estructurados en JSON para indexación, análisis y automatización.

Sitio operativo actual:
https://nerudev.github.io/MathKernel/

## Objetivo del proyecto

Construir una base de conocimiento matemática en español que pueda:
- ser leída como material de estudio,
- renderizar notación matemática en web,
- y exponer estructura semántica para sistemas de IA.

## Arquitectura del repositorio

Estructura principal:

- `content/`: Teoría matemática pura en Markdown.
- `metadata/`: Capa semántica y de validación para consumo IA.
- `assets/`: Recursos gráficos (SVG). **Gestionado con Git LFS**.
- `scripts/`: Orquestadores de generación, enlazado inteligente y validación.
- `site_src/`: Código fuente de la interfaz web.
- `site/`: Artefacto final generado con **estructura aplanada** para despliegue optimizado.

## Gestión de activos (Git LFS)

Este repositorio utiliza **Git LFS (Large File Storage)** para los archivos gráficos. Esto es fundamental para mantener el repositorio ligero. El flujo de CI/CD está configurado para descargar estos activos automáticamente antes de generar el sitio.

Para clonar este repositorio correctamente, asegúrate de tener Git LFS instalado:
```powershell
git lfs install
git clone <url-del-repo>
```

## Enfoque dual: humano + IA

La **capa humana** se apoya en archivos Markdown limpios en `content/`, renderizados con MathJax en un sitio estático.

La **capa IA** se apoya en una arquitectura de **Metadatos Espejo**:
- **Consistencia:** Cada archivo de contenido o imagen tiene un archivo JSON homólogo en la misma ruta relativa dentro de `metadata/`.
- **Validación:** Todos los metadatos deben cumplir estrictamente con los esquemas definidos en `metadata/schemas/`.
- **Campos de Teoría:** `id`, `title`, `module`, `order`, `concepts`.
- **Campos de Activos:** `id`, `topic_id`, `description`, `section`, `image_path`.

Referencia rapida en contenido Markdown:
- Cada archivo en `content/` incluye un bloque `yaml_frontmatter` en comentario HTML (`<!-- ... -->`) para consulta rapida por IA.
- Ese bloque no reemplaza metadata JSON: la fuente de verdad sigue siendo `metadata/content/*.json`.
- El bloque comentado no se renderiza en la salida HTML del sitio.

## Flujo local con entorno virtual

Requisitos: Python 3.11+

### 1. Preparar el entorno
```powershell
python -m venv .venv
& ".venv/Scripts/Activate.ps1"
pip install -r requirements.txt
```

### 2. Build unificado
```powershell
# Pipeline completo: Validar -> Linkear Assets -> Generar Sitio
python scripts/build.py --verbose

# Incluye regeneracion de assets graficos al inicio (opcional)
python scripts/build.py --with-assets --verbose
```

Flags disponibles en el CLI unico:
- `--verbose`: muestra logs detallados.
- `--continue-on-error`: continua en errores no criticos.
- `--skip-validation`: salta validacion estructural.
- `--with-assets`: ejecuta `generate_assets.py` antes del pipeline principal.

Scripts auxiliares:
- `python scripts/migrate_content_yaml_frontmatter.py`: inserta/actualiza `yaml_frontmatter` comentado en `content/*.md` y agrega seccion `Glosario de variables` cuando el tema usa variables/constantes.
- `python scripts/validate_encoding.py`: valida codificacion UTF-8 en rutas criticas (`content/`, `metadata/`, `scripts/`, `utils/`, `site_src/`, `docs/`).
- `python scripts/validate_markdown_format.py`: valida de forma informativa formulas/tablas Markdown y reporta posibles casos de formato inconsistente.

### 3. Calidad y mantenibilidad Python

Se adopta una capa ligera de tooling sin cambiar la arquitectura del repositorio:

- `ruff` para chequeo rapido de calidad en `scripts/`, `utils/` y `tests/`.
- `mypy` en modo **informativo** para mostrar estado de tipado actual (sin bloquear deploy).
- `pyproject.toml` como configuracion central de tooling (no reemplaza `requirements.txt`).

Comandos recomendados:

```powershell
ruff check scripts utils tests
mypy scripts utils --config-file pyproject.toml --no-error-summary
python -m pytest -q
```

### 4. Higiene de contribucion

- `.editorconfig` fija convenciones base (UTF-8, newline final, fin de linea LF).
- `.pre-commit-config.yaml` habilita hooks locales no destructivos.

Flujo sugerido:

```powershell
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Publicación en GitHub Pages

El despliegue es automático mediante GitHub Actions (`.github/workflows/pages.yml`) al realizar un push a la rama **main**.

El workflow separa dos etapas:
- **quality**: ruff + mypy (informativo) + validaciones de encoding/markdown + tests.
- **deploy**: build con assets y publicación en GitHub Pages (solo si quality finaliza correctamente).

## Estado actual del repositorio

- **Módulos:** 7 módulos principales (Fundamentos, Álgebra Lineal, Cálculo Diferencial, Integral, Vectorial, EDO, Métodos Numéricos).
- **Contenido:** 34 temas con teoría matemática completa.
- **Metadatos:** 34 archivos JSON sincronizados con el contenido.
- **Rama principal:** `main`.

## Novedades recientes (2026-04-13)

- Se estandarizó el render de imágenes en el sitio para que queden centradas y no excedan el ancho del contenido de texto.
- Se añadió un límite de ancho para medios en la capa web fuente (`site_src/styles.css`), con comportamiento responsive en móvil.
- Se actualizó la paleta de generación SVG a colores didácticos vivos (azul, verde, amarillo, rojo, morado, rosa y variantes).
- Se regeneraron assets SVG y se validó build/tests sin rotura de enlaces de imágenes.

- Se agrego `yaml_frontmatter` comentado en `content/` para identificacion rapida de archivo, encabezados y conceptos clave sin afectar render web.
- Se incorporo seccion estandar `Glosario de variables` en Markdown para temas con variables/constantes, incluyendo precision de 12 digitos para constantes cuando aplica.
- Se incorporo validacion UTF-8 estricta en el pipeline de build y en un script dedicado (`scripts/validate_encoding.py`).

## Incidentes operativos y diagnostico (2026-04-13)

Durante la ejecucion local se observaron bloqueos intermitentes de terminal (PowerShell) al correr checks y pruebas en una sola pasada.

Incidentes registrados:
- Bloqueo de terminal con popup de VS Code (detener proceso / reabrir VS Code) en ejecuciones largas sin checkpoints.
- Proceso persistente de Pylance mostrando notificacion activa de analisis (`14 files and 0 cells to analyze`).
- Warning de Pylance `missingDefaultExcludes` por configuracion personalizada de `python.analysis.exclude` sin incluir patrones por defecto (faltaba `**/.*`).
- Ejecucion de mypy sobre `scripts` completo con `MYPY_EXIT=2`, errores de tipado en scripts de graficos Matplotlib 3D y mensaje `INTERNAL ERROR` de mypy.

Comando exacto reportado con `MYPY_EXIT=2`:

```powershell
$ErrorActionPreference='Continue'; & .\.venv\Scripts\python.exe -m mypy scripts utils --config-file pyproject.toml --no-error-summary > .mypy-report-local.txt 2>&1; $code=$LASTEXITCODE; Write-Host ('MYPY_EXIT=' + $code); Get-Content .mypy-report-local.txt | Select-Object -Last 40
```

Causas raiz consolidadas:
- Entorno virtual previo inconsistente (metadata de `pyvenv.cfg` de otra ruta/proyecto).
- Ejecucion de tareas pesadas sin segmentacion (tests/build/mypy completo) en una sola corrida.
- `subprocess.run` sin timeout en rutas criticas (`tests/conftest.py` y `scripts/build.py` para `--with-assets`).
- Configuracion de analisis de Pylance incompleta para exclusiones por defecto.

Mitigaciones aplicadas:
- Recreacion completa de `.venv` en la ruta actual del repo y reinstalacion de dependencias.
- Instalacion de tooling local para checkpoints (`ruff`, `mypy`, `pre-commit`, `pytest-timeout`).
- Ajuste de workspace para ejecucion estable:
	- `python.terminal.activateEnvironment = false`
	- `python.analysis.diagnosticMode = openFilesOnly`
	- `python.analysis.exclude` con `**/.*` y exclusiones de carpetas pesadas.
- Ejecucion por checkpoints cortos con python explicito del venv (`.venv\Scripts\python.exe`), evitando corridas monoliticas.

Protocolo recomendado de ejecucion segura local:

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

Estado de verificacion posterior a mitigaciones (misma fecha):
- `pytest tests -q -x --timeout=120`: 32 passed.
- `scripts/build.py --verbose`: exitoso (con alertas informativas de tablas).
- `scripts/build.py --with-assets --verbose`: exitoso (71 assets generados).

## Documentación técnica complementaria

Ver detalle técnico de arquitectura y flujo en:
- [docs/MATHKERNEL.md](docs/MATHKERNEL.md)
