# yaml_frontmatter:
#   id: 'templates'
#   script_path: 'scripts/templates.py'
#   metadata_path: 'metadata/scripts/templates.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Plantillas de estilo para graficos matplotlib'
#   key_functions:
#     - 'get_colors'
#     - 'setup_style'
#     - 'get_output_dir_for_topic'
#     - 'save_figure'
#   tags:
#     - 'templates'
#     - 'graficos'
#     - 'matplotlib'

from pathlib import Path

import matplotlib.pyplot as plt


def get_colors():
    """Retorna la paleta de colores oficial del sitio."""
    return {
        # Claves legacy usadas por los scripts existentes.
        'primary': '#2563EB',    # Azul
        'secondary': '#DC2626',  # Rojo
        'accent': '#16A34A',     # Verde
        'tertiary': '#7C3AED',   # Morado

        # Paleta didactica extendida para figuras con muchos elementos.
        'blue': '#2563EB',
        'green': '#16A34A',
        'yellow': '#EAB308',
        'red': '#DC2626',
        'purple': '#7C3AED',
        'pink': '#EC4899',

        # Variantes para resaltes y contrastes.
        'blue_light': '#60A5FA',
        'green_light': '#4ADE80',
        'yellow_light': '#FDE047',
        'red_light': '#F87171',
        'purple_light': '#A78BFA',
        'pink_light': '#F472B6',
        'blue_dark': '#1D4ED8',
        'green_dark': '#15803D',
        'yellow_dark': '#CA8A04',
        'red_dark': '#B91C1C',
        'purple_dark': '#6D28D9',
        'pink_dark': '#DB2777',

        'background': '#ffffff',
        'text': '#1F2937'
    }

def setup_style():
    """Configura el estilo base de Matplotlib para coincidir con el sitio."""
    colors = get_colors()
    plt.rcParams.update({
        'figure.facecolor': colors['background'],
        'axes.facecolor': colors['background'],
        'axes.prop_cycle': plt.cycler(color=[
            colors['blue'],
            colors['green'],
            colors['yellow'],
            colors['red'],
            colors['purple'],
            colors['pink'],
        ]),
        'axes.edgecolor': colors['tertiary'],
        'axes.labelcolor': colors['text'],
        'xtick.color': colors['text'],
        'ytick.color': colors['text'],
        'text.color': colors['text'],
        'grid.color': colors['blue_light'],
        'grid.alpha': 0.25,
        'font.family': 'sans-serif',
        'font.sans-serif': ['Segoe UI', 'Roboto', 'Arial'],
        'axes.spines.top': False,
        'axes.spines.right': False,
    })


def get_output_dir_for_topic(topic_id):
    """Construye la ruta de salida de un tema y garantiza su existencia."""
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "assets" / "images" / "grafics" / str(topic_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def save_figure(fig, output_dir, base_name):
    """Guarda una figura en SVG y retorna las rutas generadas."""
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    svg_path = target_dir / f"{base_name}.svg"
    fig.savefig(str(svg_path), format="svg", bbox_inches="tight")
    return {"svg": str(svg_path)}
