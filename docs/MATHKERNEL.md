# Arquitectura técnica del repositorio: MathKernel

## 1. Propósito técnico

Este proyecto implementa una arquitectura de contenido desacoplada:

- **Capa de lectura humana:** Archivos Markdown en `content/` que contienen exclusivamente teoría matemática y fórmulas LaTeX. Se han eliminado metadatos internos y elementos de navegación para maximizar la legibilidad y portabilidad.
- **Capa de lectura por IA:** Archivos JSON en `metadata/` que proporcionan la estructura semántica, facilitando el procesamiento por agentes y sistemas automatizados.

## 2. Componentes

### 2.1 Capa de contenido (`content/`)
- **Formato:** Markdown puro.
- **Organización:** Estructura jerárquica por módulos.
- **Integridad:** Las imágenes se inyectan automáticamente mediante scripts basados en metadatos, evitando el hardcoding manual.

### 2.2 Capa de metadatos (`metadata/`)
- **Estructura Espejo (Homóloga):**
    - `metadata/content/`: Réplica exacta de `content/`. Cada `.md` tiene un `.json`.
    - `metadata/assets/images/grafics/`: Réplica de los activos visuales. Cada `.svg` tiene un `.json`.
- **Esquemas de Validación (`metadata/schemas/`):**
    - `content.schema.json`: Rige la teoría (id, title, concepts, etc.).
    - `assets.schema.json`: Rige los gráficos (id, topic_id, description, section, etc.).

### 2.3 Capa de generación y herramientas (`scripts/`)
- **`generate_site.py`:** Convierte Markdown a HTML y orquestando el glosario/índice mediante búsqueda recursiva en `metadata/content/`.
- **`validate_structure.py`:** Validador integral que asegura la correspondencia espejo entre archivos y valida cada JSON contra su respectivo esquema.
- **`generate_assets.py`:** Genera gráficos SVG desde scripts de Matplotlib y crea automáticamente sus archivos de metadatos espejo.
- **`link_assets_to_content.py`:** Escanea los metadatos de activos y los inyecta en el contenido Markdown basándose en `topic_id` y `section`.

### 2.4 Gestión de Activos
- **Git LFS:** Utilizado para rastrear archivos en `assets/images/grafics/`, manteniendo el repositorio ligero.
- **Formato Vectorial:** Se prioriza SVG para garantizar calidad matemática infinita y bajo peso.

## 3. Flujo de trabajo y Despliegue

1. **Creación:** Escribir teoría en `content/` o scripts de gráficos en `scripts/grafics/`.
2. **Sincronización:** Ejecutar `generate_assets.py` y `link_assets_to_content.py`.
3. **Verificación:** `validate_structure.py` confirma que todo el sistema de metadatos es coherente.
4. **Build:** `generate_site.py` construye el artefacto final en `site/`.
5. **CI/CD:** GitHub Actions despliega el contenido de `site/` automáticamente.

## 4. Configuración del Repositorio
- **Nombre:** MathKernel
- **Rama principal:** `main`
- **Sitio:** https://nerudev.github.io/MathKernel/

## 5. Recomendaciones de Evolución
- Mantener el desacoplamiento: no incluir información de formato o metadatos dentro de los archivos de teoría.
- Expandir el catálogo de conceptos en los archivos JSON para mejorar la indexación por parte de IAs.
- Asegurar que cualquier nuevo módulo siga la convención de nombrado `XX_nombre_modulo`.
