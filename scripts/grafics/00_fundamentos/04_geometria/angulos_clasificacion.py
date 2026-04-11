"""
Gráfico: Clasificación de Ángulos
=================================

Topic: FUN-04 Geometría
Usado en: theory/FUN-04-Teoria-Geometria.md (sección 4.2)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "angulos_clasificacion",
    "description": "Clasificación de ángulos: agudo, recto, obtuso, llano, cóncavo",
    "used_in": ["theory/FUN-04-Teoria-Geometria.md"],
    "section": "4.2",
}

def draw_angle(ax, center, angle_deg, label, color, y_offset=0):
    """Dibuja un ángulo con su arco y etiqueta."""
    # Rayos del ángulo
    length = 1.0
    x0, y0 = center
    
    # Rayo horizontal (lado inicial)
    ax.annotate('', xy=(x0 + length, y0), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    
    # Rayo rotado (lado terminal)
    angle_rad = np.radians(angle_deg)
    x_end = x0 + length * np.cos(angle_rad)
    y_end = y0 + length * np.sin(angle_rad)
    ax.annotate('', xy=(x_end, y_end), xytext=(x0, y0),
                arrowprops=dict(arrowstyle='->', color=color, lw=2))
    
    # Arco del ángulo
    arc_angles = np.linspace(0, angle_rad, 50)
    arc_r = 0.3
    arc_x = x0 + arc_r * np.cos(arc_angles)
    arc_y = y0 + arc_r * np.sin(arc_angles)
    ax.plot(arc_x, arc_y, color=color, lw=2)
    
    # Etiqueta del ángulo (grados) - con bbox para legibilidad
    label_angle = angle_rad / 2
    label_r = 0.5
    label_x = x0 + label_r * np.cos(label_angle)
    label_y = y0 + label_r * np.sin(label_angle)
    ax.text(label_x, label_y, f'{angle_deg}°', ha='center', va='center', 
            fontsize=10, color=color, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.2'))
    
    # Nombre del tipo de ángulo - debajo de la figura
    ax.text(x0 + 0.5, y0 - 0.6, label, ha='center', va='top',
            fontsize=11, fontweight='bold', color='#1f2937')

def generate() -> plt.Figure:
    """Genera el gráfico de clasificación de ángulos."""
    setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(1, 5, figsize=(16, 5), layout='constrained')
    
    angle_types = [
        (45, "Agudo", colors['primary']),
        (90, "Recto", colors['secondary']),
        (120, "Obtuso", colors['accent']),
        (180, "Llano", colors['tertiary']),
        (270, "Cóncavo", '#f59e0b'),
    ]
    
    for ax, (angle, name, color) in zip(axes, angle_types):
        ax.set_xlim(-0.3, 1.8)
        ax.set_ylim(-1.0, 1.6)
        ax.set_aspect('equal')
        ax.axis('off')
        
        draw_angle(ax, (0.3, 0.1), angle, name, color)
        
        # Condición - más abajo para evitar superposición
        if angle < 90:
            cond = "0° < α < 90°"
        elif angle == 90:
            cond = "α = 90°"
        elif angle < 180:
            cond = "90° < α < 180°"
        elif angle == 180:
            cond = "α = 180°"
        else:
            cond = "180° < α < 360°"
        ax.text(0.8, -0.85, cond, ha='center', va='top', fontsize=9, 
                color='#6b7280', style='italic')
    
    fig.suptitle('Clasificación de Ángulos por Medida', fontsize=14, 
                 fontweight='bold')
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
