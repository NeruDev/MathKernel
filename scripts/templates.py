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
