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
- **Campos de Scripts:** `file_name`, `script_path`, `description`, `repo_role`, `inputs`, `outputs`, `dependencies`, `status` y contexto de uso.

Referencia rapida en contenido Markdown:
- Cada archivo en `content/` incluye un bloque `yaml_frontmatter` en comentario HTML (`<!-- ... -->`) para consulta rapida por IA.
- Ese bloque no reemplaza metadata JSON: la fuente de verdad sigue siendo `metadata/content/*.json`.
- El bloque comentado no se renderiza en la salida HTML del sitio.

Referencia rapida en scripts Python:
- Cada script objetivo en `scripts/`, `scripts/core/` y `scripts/io/` incluye un bloque `yaml_frontmatter` comentado con `#` al inicio del archivo.
- El bloque de scripts apunta a su metadata homologa en `metadata/scripts/**/*.meta.json`.
- `scripts/build.py` valida de forma estricta el espejo `scripts <-> metadata/scripts` y el esquema `metadata/schemas/scripts.schema.json`.

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

## Historial de incidentes operativos

El detalle completo de errores grandes, diagnostico y mitigaciones se mantiene en:
- [docs/historial_errores.md](docs/historial_errores.md)

Entrada vigente:
- 2026-04-13: bloqueos de terminal, warning de excludes de Pylance y mypy con `MYPY_EXIT=2`.
- 2026-04-13 (continuidad): corte reportado en CP1 Ruff; diagnostico multi-host sin cuelgue reproducible del comando.

Nota de estado para Pylance:
- Con `python.analysis.diagnosticMode = openFilesOnly`, la notificacion `14 files and 0 cells to analyze` puede aparecer como actividad informativa de analisis de archivos abiertos.

## Documentación técnica complementaria

Ver detalle técnico de arquitectura y flujo en:
- [docs/MATHKERNEL.md](docs/MATHKERNEL.md)
