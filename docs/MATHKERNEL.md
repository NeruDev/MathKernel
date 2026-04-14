# Arquitectura técnica del repositorio: MathKernel

## 1. Propósito técnico

Este proyecto implementa una arquitectura de contenido desacoplada:

- **Capa de lectura humana:** Archivos Markdown en `content/` que contienen teoría matemática y fórmulas LaTeX. Para apoyar flujos IA sin romper previews, los metadatos rapidos se incluyen como YAML comentado al inicio (`<!-- yaml_frontmatter: ... -->`).
- **Capa de lectura por IA:** Archivos JSON en `metadata/` que proporcionan la estructura semántica, facilitando el procesamiento por agentes y sistemas automatizados.

## 2. Componentes

### 2.1 Capa de contenido (`content/`)
- **Formato:** Markdown puro.
- **Organización:** Estructura jerárquica por módulos.
- **Integridad:** Las imágenes se inyectan automáticamente mediante scripts basados en metadatos, evitando el hardcoding manual.
- **Frontmatter comentado:** Cada archivo incluye `yaml_frontmatter` dentro de comentario HTML para evitar renderizado en preview/web.
- **Glosario local:** Cuando el tema usa variables/constantes, se agrega sección `## Glosario de variables` con tabla estándar.

### 2.2 Capa de metadatos (`metadata/`)
- **Estructura Espejo (Homóloga):**
    - `metadata/content/`: Réplica exacta de `content/`. Cada `.md` tiene un `.json`.
    - `metadata/assets/images/grafics/`: Réplica de los activos visuales. Cada `.svg` tiene un `.json`.
- **Esquemas de Validación (`metadata/schemas/`):**
    - `content.schema.json`: Rige la teoría (id, title, concepts, etc.).
    - `assets.schema.json`: Rige los gráficos (id, topic_id, description, section, etc.).

### 2.3 Capa de generación y herramientas (`scripts/`)
- **`build.py`**: CLI único del proyecto. Orquesta el pipeline `Validar -> Linkear Assets -> Generar Sitio` y centraliza flags operativos (`--verbose`, `--continue-on-error`, `--skip-validation`, `--with-assets`).
- **`core/`**: Lógica de negocio pura desacoplada del filesystem (`validators.py`, `processors.py`, `generators.py`, `error_handling.py`).
- **`io/file_manager.py`**: Abstracción de entrada/salida para texto, JSON y operaciones de directorios.
- **`generate_assets.py`**: Generador de gráficos SVG invocado de forma opcional mediante el flag `--with-assets`.
- **`migrate_content_yaml_frontmatter.py`**: Script de migración para insertar/actualizar YAML comentado y glosario de variables en `content/`.
- **`validate_encoding.py`**: Validación UTF-8 estricta para carpetas críticas y archivos fuente.
- **`validate_markdown_format.py`**: Validación informativa de fórmulas/tablas Markdown para detectar posibles problemas de formato sin bloquear el build.

### 2.3.1 Calidad y mantenibilidad Python (incremental)
- **`pyproject.toml`** centraliza configuración de `ruff` y `mypy`.
- **`ruff`** se usa para checks rápidos de calidad en `scripts/`, `utils/`, `tests/`.
- **`mypy`** se ejecuta en modo informativo para exponer el estado de tipado a IA y revisiones humanas, sin convertirlo aún en gate estricto.
- **`.pre-commit-config.yaml`** y **`.editorconfig`** agregan higiene de contribución no destructiva.


### 2.4 Gestión de Activos
- **Git LFS:** Utilizado para rastrear archivos en `assets/images/grafics/`. Es crítico que el entorno de CI/CD (GitHub Actions) realice un `git lfs pull` para que los archivos reales estén disponibles durante la generación del sitio.
- **Formato Vectorial:** Se prioriza SVG. Las rutas en el sitio generado se ajustan dinámicamente de `../../../assets/` a `../../assets/` (o el nivel correspondiente) para mantener la compatibilidad entre el repositorio y la web.

### 2.5 Cambios recientes en presentación y gráficos (2026-04-13)
- En `site_src/styles.css` se incorporaron reglas para `main img`/`main figure` con `max-width` relativo al contenido, centrado y ajuste responsive.
- En `scripts/templates.py` se amplió `get_colors` con paleta didáctica y variantes, manteniendo compatibilidad de claves legacy (`primary`, `secondary`, `accent`, `tertiary`).
- `setup_style` define un `axes.prop_cycle` que prioriza azul, verde, amarillo, rojo, morado y rosa.
- La regeneración de SVG se realiza con `scripts/generate_assets.py` y se integra al flujo con `scripts/build.py --with-assets`.
- La verificación de integridad debe incluir pruebas de `tests/test_links.py`, `tests/test_assets.py` y `tests/test_structure.py`.

## 3. Flujo de trabajo y Despliegue

1. **Creación:** Escribir teoría en `content/` o scripts de gráficos en `scripts/grafics/`.
2. **Build local:** Ejecutar `python scripts/build.py --verbose` para validar, vincular activos y generar el sitio.
3. **Build con assets:** Ejecutar `python scripts/build.py --with-assets --verbose` cuando se requiera regenerar gráficos SVG.
4. **CI/CD:** GitHub Actions descarga objetos LFS y ejecuta el build unificado antes de desplegar `site/`.

El workflow de Pages está separado en dos jobs:
- **quality**: linting, tipado informativo, validación UTF-8/Markdown y tests.
- **deploy**: build con assets y publicación, dependiente del job quality.

## 4. Estructura del Proyecto

Esta sección describe la organización física del repositorio, segmentada por tipo de consumo.

### 4.1 Árbol de directorios (IA-Ready)
Para un análisis exhaustivo por agentes de IA, se mantiene un registro completo de la estructura en formato JSON siguiendo la arquitectura homóloga de metadatos:
- **Referencia:** [metadata/docs/project_structure.json](../metadata/docs/project_structure.json)

### 4.2 Arquitectura simplificada (Lectura Humana)
A continuación se presenta la jerarquía principal del repositorio para facilitar la navegación rápida:

```mermaid
graph TD
    Root[MathKernel/] --> Content[content/ - Teoría MD]
    Root --> Metadata[metadata/ - Metadatos Espejo]
    Root --> Assets[assets/ - Gráficos SVG LFS]
    Root --> Scripts[scripts/ - Automatización]
    Root --> SiteSrc[site_src/ - Plantillas Web]
    Root --> Docs[docs/ - Documentación]

    Metadata --> MContent[content/ - JSON de Teoría]
    Metadata --> MAssets[assets/images/grafics/ - JSON de Activos]
    Metadata --> MSchemas[schemas/ - Validadores JSON Schema]
    Metadata --> MDocs[docs/ - Estructura de Proyecto JSON]

    Scripts --> Grafics[grafics/ - Generadores Matplotlib]
```

## 5. Configuración del Repositorio
- **Nombre:** MathKernel
- **Rama principal:** `main`
- **Sitio:** https://nerudev.github.io/MathKernel/

## 6. Recomendaciones de Evolución
- Mantener el desacoplamiento: conservar `metadata/content/*.json` como fuente de verdad y usar solo YAML comentado como referencia breve.
- Expandir el catálogo de conceptos en los archivos JSON para mejorar la indexación por parte de IAs.
- Asegurar que cualquier nuevo módulo siga la convención de nombrado `XX_nombre_modulo`.
- Mantener validación UTF-8 estricta en CI para prevenir roturas por codificación en web.
- Mantener `mypy` como señal informativa en el corto plazo y elevar gradualmente el nivel de exigencia por módulos estables.
