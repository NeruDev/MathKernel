from pathlib import Path

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
    """Builds an output path for a topic and ensures it exists."""
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "assets" / "images" / "grafics" / str(topic_id)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def save_figure(fig, output_dir, base_name):
    """Saves a figure to SVG and returns generated paths."""
    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    svg_path = target_dir / f"{base_name}.svg"
    fig.savefig(str(svg_path), format="svg", bbox_inches="tight")
    return {"svg": str(svg_path)}
