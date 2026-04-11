# MathKernel

Repositorio educativo de matematicas orientado a dos tipos de consumo:

- Humano: contenido en Markdown con formulas LaTeX legibles en navegador.
- IA: metadatos estructurados en JSON para indexacion, analisis y automatizacion.

Sitio operativo actual:
https://nerudev.github.io/MathKernel/

## Objetivo del proyecto

Construir una base de conocimiento matematica en espanol que pueda:

- ser leida como material de estudio,
- renderizar notacion matematica en web,
- y exponer estructura semantica para sistemas de IA.

## Arquitectura del repositorio

Estructura principal:

- content/: teoria y desarrollo por modulos en Markdown.
- metadata/: descriptores JSON para consumo IA (conceptos, scripts, assets, orden, modulo).
- scripts/: generacion de sitio y utilidades Python.
- site_src/: plantilla base del sitio (HTML, CSS, JS).
- site/: salida generada para publicacion estatica.
- assets/: recursos graficos generados o referenciados por metadata.
- tests/: pruebas automatizadas.
- utils/: herramientas auxiliares.

## Enfoque dual: humano + IA

La capa humana se apoya en:

- archivos Markdown en content/,
- render LaTeX en cliente con MathJax,
- navegacion web en el sitio estatico generado.

La capa IA se apoya en:

- JSON por tema en metadata/,
- campos como id, title, lang, concepts, scripts, assets, module y order,
- posibilidad de enlazar contenido teorico con artefactos y automatizaciones.

Ejemplo actual de metadata:
- metadata/simbologia_matematica.json

## Flujo local con entorno virtual (Python venv)

Requisitos:

- Python 3.11+ (local actual: venv con Python 3.12)

### 1. Crear y activar entorno virtual

PowerShell (Windows):

```powershell
python -m venv .venv
& ".venv/Scripts/Activate.ps1"
```

### 2. Instalar dependencias

```powershell
pip install -r requirements.txt
```

Dependencias actuales:

- markdown
- pymdown-extensions

### 3. Generar el sitio estatico

```powershell
python scripts/generate_site.py
```

Este proceso:

- limpia y reconstruye site/ desde site_src/,
- convierte Markdown a HTML dentro de site/pages/,
- corrige enlaces .md -> .html,
- ajusta rutas relativas de assets,
- genera glossary.html desde metadata/.

## Render de LaTeX con MathJax

La configuracion vive en dos puntos:

- site_src/index.html para la portada.
- scripts/generate_site.py (funcion wrap_html) para paginas generadas.

Delimitadores soportados:

- Inline: $...$ y \(...\)
- Display: $$...$$ y \[...\]

## Publicacion en GitHub Pages

Pipeline en:

- .github/workflows/pages.yml

Resumen del workflow:

1. Checkout del repo.
2. Setup de Python.
3. Setup de GitHub Pages.
4. Instalacion de dependencias.
5. Generacion de sitio con scripts/generate_site.py.
6. Creacion de site/.nojekyll.
7. Upload de artifact (./site).
8. Deploy con actions/deploy-pages.

Rama de disparo actual: main.

## Estado actual del repositorio

Snapshot verificado:

- Modulos en content/: 2 carpetas de primer nivel.
- Contenido activo en 00_fundamentos/: 5 archivos Markdown.
- Carpeta 01_algebra_lineal/: creada, aun sin contenido.
- Metadata disponible: 1 archivo JSON.
- scripts/: generate_site.py y simbologia_matematica.py.
- assets/: vacio actualmente.
- tests/: vacio actualmente.
- utils/: vacio actualmente.

## Recomendaciones inmediatas

1. Completar metadata para cada archivo Markdown existente.
2. Agregar assets referenciados desde metadata para evitar enlaces rotos.
3. Crear pruebas basicas del generador en tests/.
4. Mantener sincronia entre contenido humano (content/) y capa IA (metadata/).

## Documentacion tecnica complementaria

Ver detalle tecnico de arquitectura y flujo en:

- docs/MATHKERNEL.md
