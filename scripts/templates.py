import os
import matplotlib.pyplot as plt

def get_colors():
    """Retorna la paleta de colores oficial del sitio."""
    return {
        'primary': '#39C5BB',    # Miku Cyan
        'secondary': '#E12885',  # Miku Fuchsia
        'accent': '#1f2937',     # Dark Gray
        'tertiary': '#4B5563',   # Gray
        'background': '#ffffff',
        'text': '#2c2f33'
    }

def setup_style():
    """Configura el estilo base de Matplotlib para coincidir con el sitio."""
    colors = get_colors()
    plt.rcParams.update({
        'figure.facecolor': colors['background'],
        'axes.facecolor': colors['background'],
        'axes.edgecolor': colors['tertiary'],
        'axes.labelcolor': colors['text'],
        'xtick.color': colors['text'],
        'ytick.color': colors['text'],
        'text.color': colors['text'],
        'font.family': 'sans-serif',
        'font.sans-serif': ['Segoe UI', 'Roboto', 'Arial'],
        'axes.spines.top': False,
        'axes.spines.right': False,
    })

def get_output_dir_for_topic(topic_id):
    """
    Calcula la ruta de salida para los assets basada en el ID del tópico.
    Ejemplo: 'FUN-04' -> 'assets/00_fundamentos/04_geometria'
    """
    # Mapeo simple basado en la estructura conocida
    mapping = {
        "FUN-04": "assets/00_fundamentos/04_geometria",
        "FUN-05": "assets/00_fundamentos/05_trigonometria",
        "FUN-06": "assets/00_fundamentos/06_geometria_analitica",
        "CV-01": "assets/04_calculo_vectorial/01_vectores_en_el_espacio",
        "CV-03": "assets/04_calculo_vectorial/03_funciones_vectoriales",
        "CV-04": "assets/04_calculo_vectorial/04_funciones_de_varias_variables",
        "CV-05": "assets/04_calculo_vectorial/05_integracion_multiple",
        "ED-01": "assets/05_ecuaciones_diferenciales/ED-01",
        "ED-02": "assets/05_ecuaciones_diferenciales/ED-02",
        "ED-03": "assets/05_ecuaciones_diferenciales/ED-03",
        "ED-04": "assets/05_ecuaciones_diferenciales/ED-04",
        "ED-05": "assets/05_ecuaciones_diferenciales/ED-05",
    }
    
    path = mapping.get(topic_id, f"assets/unknown/{topic_id}")
    os.makedirs(path, exist_ok=True)
    return path

def save_figure(fig, output_dir, name):
    """Guarda la figura en formatos PNG y SVG."""
    png_path = os.path.join(output_dir, f"{name}.png")
    svg_path = os.path.join(output_dir, f"{name}.svg")
    
    fig.savefig(png_path, dpi=300, bbox_inches='tight')
    fig.savefig(svg_path, bbox_inches='tight')
    
    plt.close(fig)
    return [png_path, svg_path]
