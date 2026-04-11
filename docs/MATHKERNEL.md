# Arquitectura tecnica del repositorio

## 1. Proposito tecnico

Este proyecto implementa una arquitectura de contenido dual:

- Capa de lectura humana: Markdown + render web con MathJax.
- Capa de lectura por IA: metadatos JSON vinculados a conceptos, scripts y assets.

El objetivo es que una misma base de conocimiento sirva para:

- estudio directo en web,
- procesamiento estructurado por agentes, pipelines o motores semanticos.

## 2. Componentes

### 2.1 Capa de contenido

- content/
- Formato: Markdown en espanol.
- Organizacion: modulos y submodulos en carpetas snake_case.

Rol:

- contiene la teoria y explicaciones matematicas,
- incluye expresiones LaTeX para render en cliente.

### 2.2 Capa de metadatos para IA

- metadata/
- Formato: JSON por unidad o tema.

Campos observados en el estado actual:

- id
- title
- lang
- concepts
- scripts
- assets
- module
- order

Rol:

- describir semanticamente cada unidad,
- enlazar contenido con scripts y recursos,
- facilitar recuperacion y automatizacion por IA.

### 2.3 Capa de generacion

- scripts/generate_site.py

Responsabilidades:

- limpiar salida previa site/,
- copiar base estatica desde site_src/,
- convertir Markdown a HTML,
- corregir enlaces internos .md a .html,
- ajustar rutas relativas de assets segun profundidad,
- envolver cada pagina con plantilla comun,
- construir glossary.html a partir de metadata/.

### 2.4 Capa de presentacion web

- site_src/index.html
- site_src/styles.css
- site_src/scripts.js

Rol:

- experiencia visual base del sitio,
- cambio de tema light/dark con localStorage,
- carga de MathJax para render LaTeX.

### 2.5 Capa de salida publica

- site/

Rol:

- artefacto estatico listo para publicacion,
- contiene index, glossary y pages/ generadas.

## 3. Flujo de datos

1. Autor edita o agrega contenido en content/.
2. Autor mantiene metadata correspondiente en metadata/.
3. Ejecuta scripts/generate_site.py en venv Python.
4. Se reconstruye site/ con HTML final.
5. GitHub Actions repite build y despliega en GitHub Pages.

## 4. Render de formulas (MathJax)

La estrategia de render es 100% en cliente.

Puntos de configuracion:

- site_src/index.html
- plantilla wrap_html en scripts/generate_site.py

Delimitadores configurados:

- inline: $...$ y \(...\)
- display: $$...$$ y \[...\]

## 5. CI/CD de publicacion

Workflow:

- .github/workflows/pages.yml

Secuencia actual:

1. Trigger en push sobre main.
2. Setup Python 3.11.
3. Setup de Pages.
4. pip install -r requirements.txt.
5. python scripts/generate_site.py.
6. Crear .nojekyll.
7. Subir artifact desde ./site.
8. Deploy con actions/deploy-pages.

Sitio activo:

- https://nerudev.github.io/MathKernel/

## 6. Estado actual (tecnico)

- content/00_fundamentos contiene 5 unidades Markdown.
- content/01_algebra_lineal existe pero aun esta vacio.
- metadata/ contiene solo simbologia_matematica.json.
- scripts/ contiene generate_site.py y simbologia_matematica.py.
- assets/, tests/ y utils/ estan vacios.

## 7. Limites y riesgos actuales

1. Cobertura parcial de metadatos respecto al contenido existente.
2. assets declarados en metadata aun no presentes fisicamente.
3. Sin pruebas automatizadas del generador ni validacion de schema JSON.
4. El indice de portada es estatico y no lista todo el contenido automaticamente.

## 8. Recomendaciones de evolucion

1. Definir plantilla minima de metadata por cada nuevo Markdown.
2. Implementar validacion de metadata en CI (campos requeridos y rutas existentes).
3. Agregar pruebas unitarias para funciones clave de generate_site.py.
4. Incorporar generacion automatica de indice desde content/.
5. Completar modulo 01_algebra_lineal con contenido y metadata asociada.
