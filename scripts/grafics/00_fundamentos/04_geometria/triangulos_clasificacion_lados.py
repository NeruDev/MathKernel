"""
Gráfico: Clasificación de Triángulos por Lados
==============================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (sección 4.3)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "triangulos_clasificacion_lados",
    "description": "Clasificación de triángulos: equilátero, isósceles, escaleno",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.3",
}

def draw_triangle_with_marks(ax, vertices, side_marks, title, colors_dict):
    """Dibuja un triángulo con marcas en los lados iguales."""
    A, B, C = vertices
    
    # Dibujar el triángulo
    triangle = plt.Polygon([A, B, C], fill=False, edgecolor=colors_dict['primary'], 
                           linewidth=2.5)
    ax.add_patch(triangle)
    
    # Rellenar con color suave
    triangle_fill = plt.Polygon([A, B, C], fill=True, facecolor=colors_dict['primary'],
                                 alpha=0.1, edgecolor='none')
    ax.add_patch(triangle_fill)
    
    # Vértices
    for point, label in zip([A, B, C], ['A', 'B', 'C']):
        ax.plot(point[0], point[1], 'o', color=colors_dict['secondary'], markersize=6)
    
    # Marcas en los lados
    def add_tick_marks(p1, p2, num_marks, color):
        """Añade marcas perpendiculares al lado."""
        mid = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = np.sqrt(dx**2 + dy**2)
        # Vector perpendicular normalizado
        perp = (-dy/length, dx/length)
        
        mark_len = 0.1
        spacing = 0.08
        
        for i in range(num_marks):
            offset = (i - (num_marks-1)/2) * spacing
            mx = mid[0] + offset * dx/length
            my = mid[1] + offset * dy/length
            ax.plot([mx - mark_len*perp[0], mx + mark_len*perp[0]],
                   [my - mark_len*perp[1], my + mark_len*perp[1]],
                   color=color, lw=2)
    
    # Aplicar marcas según el tipo
    sides = [(A, B), (B, C), (C, A)]
    for (p1, p2), marks in zip(sides, side_marks):
        if marks > 0:
            add_tick_marks(p1, p2, marks, colors_dict['accent'])
    
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)

def generate() -> plt.Figure:
    """Genera el gráfico de clasificación de triángulos por lados."""
    setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 5), layout='constrained')
    
    # Triángulo Equilátero (3 lados iguales)
    h = np.sqrt(3)/2 * 2  # altura para lado 2
    equi = [(0, 0), (2, 0), (1, h)]
    draw_triangle_with_marks(axes[0], equi, [1, 1, 1], 
                            'EQUILÁTERO\n(3 lados iguales)', colors)
    axes[0].text(1, -0.4, 'a = b = c', ha='center', fontsize=11, color='#6b7280')
    
    # Triángulo Isósceles (2 lados iguales)
    iso = [(0, 0), (2.5, 0), (1.25, 2)]
    draw_triangle_with_marks(axes[1], iso, [0, 2, 2], 
                            'ISÓSCELES\n(2 lados iguales)', colors)
    axes[1].text(1.25, -0.4, 'a = b ≠ c', ha='center', fontsize=11, color='#6b7280')
    
    # Triángulo Escaleno (todos diferentes)
    esc = [(0, 0), (3, 0), (1, 1.8)]
    draw_triangle_with_marks(axes[2], esc, [0, 0, 0], 
                            'ESCALENO\n(3 lados diferentes)', colors)
    axes[2].text(1.5, -0.4, 'a ≠ b ≠ c', ha='center', fontsize=11, color='#6b7280')
    
    for ax in axes:
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-0.5, 3.5)
        ax.set_ylim(-0.8, 2.5)
    
    fig.suptitle('Clasificación de Triángulos por Lados', fontsize=14, 
                 fontweight='bold')
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
