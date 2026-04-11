# Arquitectura técnica del repositorio: MathKernel

## 1. Propósito técnico

Este proyecto implementa una arquitectura de contenido desacoplada:

- **Capa de lectura humana:** Archivos Markdown en `content/` que contienen exclusivamente teoría matemática y fórmulas LaTeX. Se han eliminado metadatos internos y elementos de navegación para maximizar la legibilidad y portabilidad.
- **Capa de lectura por IA:** Archivos JSON en `metadata/` que proporcionan la estructura semántica, facilitando el procesamiento por agentes y sistemas automatizados.

## 2. Componentes

### 2.1 Capa de contenido (`content/`)
- **Formato:** Markdown puro.
- **Organización:** Estructura jerárquica por módulos (ej. `00_fundamentos`, `01_algebra_lineal`).
- **Estado:** Limpio de enlaces rotos, imágenes inexistentes y bloques de metadatos internos.

### 2.2 Capa de metadatos (`metadata/`)
- **Esquema:** Definido en `metadata/schema.json`.
- **Campos:** `id`, `title`, `module`, `order`, `concepts`.
- **Sincronización:** Existe una correspondencia 1:1 entre cada archivo `.md` de teoría y su descriptor `.json`.

### 2.3 Capa de generación (`scripts/`)
- **`generate_site.py`:** Orquestador del build. Convierte la teoría a HTML, genera el glosario desde los metadatos y construye el índice de contenidos.
- **`validate_structure.py`:** Asegura que la jerarquía de archivos y los metadatos cumplan con las reglas del repositorio.

### 2.4 Presentación y Salida
- **`site_src/`:** Plantillas y activos base (CSS/JS).
- **`site/`:** Artefacto final listo para GitHub Pages.

## 3. Flujo de trabajo y Despliegue

1. **Desarrollo:** Edición de teoría en `content/` y actualización de metadatos en `metadata/`.
2. **Validación:** Los scripts de build verifican la integridad de la estructura.
3. **CI/CD:** GitHub Actions procesa la rama `main` y despliega automáticamente el sitio.

## 4. Configuración del Repositorio
- **Nombre:** MathKernel
- **Rama principal:** `main`
- **Sitio:** https://nerudev.github.io/MathKernel/

## 5. Recomendaciones de Evolución
- Mantener el desacoplamiento: no incluir información de formato o metadatos dentro de los archivos de teoría.
- Expandir el catálogo de conceptos en los archivos JSON para mejorar la indexación por parte de IAs.
- Asegurar que cualquier nuevo módulo siga la convención de nombrado `XX_nombre_modulo`.
