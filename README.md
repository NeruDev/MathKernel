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

- `content/`: Teoría matemática pura en Markdown (sin metadatos internos ni enlaces rotos).
- `metadata/`: Descriptores JSON para consumo IA (conceptos, módulo, orden).
- `scripts/`: Generación de sitio y utilidades Python.
- `site_src/`: Plantilla base del sitio (HTML, CSS, JS).
- `site/`: Salida generada para publicación estática.
- `assets/`: Recursos gráficos referenciados por la teoría.
- `tests/`: Pruebas automatizadas de estructura y generación.

## Enfoque dual: humano + IA

La **capa humana** se apoya en archivos Markdown limpios en `content/`, renderizados con MathJax en un sitio estático.

La **capa IA** se apoya en archivos JSON en `metadata/` que siguen un esquema estricto:
- `id`: Identificador único (nombre del archivo).
- `title`: Título formal del tema.
- `module`: Módulo de pertenencia.
- `order`: Orden jerárquico.
- `concepts`: Lista de términos matemáticos clave.

## Flujo local con entorno virtual

Requisitos: Python 3.11+

### 1. Preparar el entorno
```powershell
python -m venv .venv
& ".venv/Scripts/Activate.ps1"
pip install -r requirements.txt
```

### 2. Generar el sitio
```powershell
python scripts/generate_site.py
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
