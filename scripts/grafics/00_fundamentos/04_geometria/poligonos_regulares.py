"""
Gráfico: Polígonos Regulares
============================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (sección 4.5)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "poligonos_regulares",
    "description": "Polígonos regulares: triángulo, cuadrado, pentágono, hexágono, octágono",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.5",
}

def draw_regular_polygon(ax, n, center, radius, color, name, angle_interior):
    """Dibuja un polígono regular de n lados."""
    angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, n+1)[:-1]  # Empezar desde arriba
    
    vertices = [(center[0] + radius*np.cos(a), center[1] + radius*np.sin(a)) for a in angles]
    
    # Polígono
    polygon = plt.Polygon(vertices, fill=True, facecolor=color,
                         alpha=0.2, edgecolor=color, linewidth=2)
    ax.add_patch(polygon)
    
    # Centro
    ax.plot(center[0], center[1], 'o', color='#374151', markersize=4)
    
    # Radio (línea punteada al centro)
    ax.plot([center[0], vertices[0][0]], [center[1], vertices[0][1]], 
           '--', color='#6b7280', lw=1, alpha=0.7)
    
    # Apotema
    mid_side = ((vertices[0][0] + vertices[1][0])/2, (vertices[0][1] + vertices[1][1])/2)
    ax.plot([center[0], mid_side[0]], [center[1], mid_side[1]], 
           ':', color='#9ca3af', lw=1.5)
    
    # Etiquetas
    ax.text(center[0], center[1] - radius - 0.3, name, ha='center', 
            fontsize=11, fontweight='bold', color='#1f2937')
    ax.text(center[0], center[1] - radius - 0.55, f'n = {n}', ha='center', 
            fontsize=9, color='#6b7280')
    ax.text(center[0], center[1] - radius - 0.8, f'∠ = {angle_interior}°', ha='center', 
            fontsize=9, color=color)

def generate() -> plt.Figure:
    """Genera el gráfico de polígonos regulares."""
    setup_style()
    colors = get_colors()
    
    fig, ax = plt.subplots(figsize=(14, 8), layout='constrained')
    
    polygons = [
        (3, 'Triángulo', 60, colors['primary']),
        (4, 'Cuadrado', 90, colors['secondary']),
        (5, 'Pentágono', 108, colors['accent']),
        (6, 'Hexágono', 120, colors['tertiary']),
        (8, 'Octágono', 135, '#f59e0b'),
    ]
    
    # Posiciones en fila
    x_positions = [1.5, 4, 6.5, 9, 11.5]
    y_center = 2.5
    
    for (n, name, angle, color), x in zip(polygons, x_positions):
        draw_regular_polygon(ax, n, (x, y_center), 1.0, color, name, angle)
    
    # Fórmulas en la parte inferior
    formulas = [
        ('Ángulo interior:', r'$\frac{(n-2) \cdot 180°}{n}$'),
        ('Suma ángulos int.:', r'$(n-2) \cdot 180°$'),
        ('Nº diagonales:', r'$\frac{n(n-3)}{2}$'),
    ]
    
    for i, (label, formula) in enumerate(formulas):
        ax.text(1.5 + i*4.5, 0.3, label, fontsize=10, color='#374151', fontweight='bold')
        ax.text(1.5 + i*4.5, 0, formula, fontsize=11, color='#1f2937')
    
    ax.set_xlim(0, 13)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    ax.set_title('Polígonos Regulares', fontsize=14, fontweight='bold', pad=15)
    
    # Leyenda
    ax.plot([0.5, 0.8], [4.2, 4.2], '--', color='#6b7280', lw=1)
    ax.text(1, 4.2, 'Radio', va='center', fontsize=9, color='#6b7280')
    ax.plot([2.5, 2.8], [4.2, 4.2], ':', color='#9ca3af', lw=1.5)
    ax.text(3, 4.2, 'Apotema', va='center', fontsize=9, color='#9ca3af')
    
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
