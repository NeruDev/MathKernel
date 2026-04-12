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

## Flujo local con entorno virtual

Requisitos: Python 3.11+

### 1. Preparar el entorno
```powershell
python -m venv .venv
& ".venv/Scripts/Activate.ps1"
pip install -r requirements.txt
```

### 2. Validar y Generar
```powershell
# Enlaza inteligentemente imágenes en el contenido Markdown mediante metadatos
python scripts/link_assets_to_content.py

# Valida estructura y genera el sitio web estático (estructura aplanada)
python scripts/generate_site.py

# Genera nuevos activos y sus metadatos espejo (opcional si ya existen)
python scripts/generate_assets.py
```

## Publicación en GitHub Pages

El despliegue es automático mediante GitHub Actions (`.github/workflows/pages.yml`) al realizar un push a la rama **main**.

## Estado actual del repositorio

- **Módulos:** 7 módulos principales (Fundamentos, Álgebra Lineal, Cálculo Diferencial, Integral, Vectorial, EDO, Métodos Numéricos).
- **Contenido:** 34 temas con teoría matemática completa.
- **Metadatos:** 34 archivos JSON sincronizados con el contenido.
- **Rama principal:** `main`.

## Documentación técnica complementaria

Ver detalle técnico de arquitectura y flujo en:
- [docs/MATHKERNEL.md](docs/MATHKERNEL.md)
