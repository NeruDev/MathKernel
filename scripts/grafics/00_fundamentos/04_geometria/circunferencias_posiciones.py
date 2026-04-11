"""
Gráfico: Posiciones Relativas de Dos Circunferencias
====================================================

Topic: FUN-04 Geometría
Usado en: problems/FUN-04-Problemas.md (Prob-56)
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np
from templates import setup_style, get_colors, get_output_dir_for_topic, save_figure

METADATA = {
    "topic_id": "FUN-04",
    "name": "circunferencias_posiciones",
    "description": "Posiciones relativas: exteriores, tangentes ext/int, secantes, interiores",
    "used_in": ["problems/FUN-04-Problemas.md"],
    "section": "4.6",
}

def draw_two_circles(ax, r1, r2, d, title, condition, colors_dict):
    """Dibuja dos circunferencias con distancia d entre centros."""
    theta = np.linspace(0, 2*np.pi, 100)
    
    # Primera circunferencia (centrada en origen)
    ax.plot(r1*np.cos(theta), r1*np.sin(theta), color=colors_dict['primary'], lw=2)
    ax.fill(r1*np.cos(theta), r1*np.sin(theta), color=colors_dict['primary'], alpha=0.15)
    ax.plot(0, 0, 'o', color=colors_dict['primary'], markersize=5)
    ax.text(-0.15, -0.35, 'O₁', fontsize=9)
    
    # Segunda circunferencia (centrada en d, 0)
    ax.plot(d + r2*np.cos(theta), r2*np.sin(theta), color=colors_dict['secondary'], lw=2)
    ax.fill(d + r2*np.cos(theta), r2*np.sin(theta), color=colors_dict['secondary'], alpha=0.15)
    ax.plot(d, 0, 'o', color=colors_dict['secondary'], markersize=5)
    ax.text(d-0.15, -0.35, 'O₂', fontsize=9)
    
    # Línea entre centros
    ax.plot([0, d], [0, 0], '--', color='#9ca3af', lw=1)
    
    # Radios
    ax.plot([0, r1], [0, 0], color=colors_dict['primary'], lw=1.5, alpha=0.7)
    ax.text(r1/2, 0.15, 'R', fontsize=9, color=colors_dict['primary'])
    ax.plot([d, d-r2], [0, 0], color=colors_dict['secondary'], lw=1.5, alpha=0.7)
    ax.text(d-r2/2, 0.15, 'r', fontsize=9, color=colors_dict['secondary'])
    
    ax.set_title(title, fontsize=10, fontweight='bold', pad=5)
    ax.text((r1+d-r2)/2, -1.8, condition, fontsize=9, ha='center', 
            color='#4b5563', style='italic')

def generate() -> plt.Figure:
    """Genera el gráfico de posiciones relativas de circunferencias."""
    setup_style()
    colors = get_colors()
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 9), layout='constrained')
    axes = axes.flatten()
    
    R, r = 1.0, 0.6  # Radios
    
    # 1. Exteriores (d > R + r)
    draw_two_circles(axes[0], R, r, 2.5, 'EXTERIORES', 'd > R + r', colors)
    
    # 2. Tangentes exteriores (d = R + r)
    draw_two_circles(axes[1], R, r, R + r, 'TANGENTES\nEXTERIORES', 'd = R + r', colors)
    # Punto de tangencia
    axes[1].plot(R, 0, 'o', color=colors['accent'], markersize=8)
    axes[1].text(R+0.1, 0.2, 'T', fontsize=9, color=colors['accent'], fontweight='bold')
    
    # 3. Secantes (|R - r| < d < R + r)
    draw_two_circles(axes[2], R, r, 1.0, 'SECANTES', '|R - r| < d < R + r', colors)
    
    # 4. Tangentes interiores (d = R - r, r dentro de R)
    draw_two_circles(axes[3], R, r, R - r, 'TANGENTES\nINTERIORES', 'd = |R - r|', colors)
    # Punto de tangencia
    axes[3].plot(R, 0, 'o', color=colors['accent'], markersize=8)
    axes[3].text(R+0.1, 0.2, 'T', fontsize=9, color=colors['accent'], fontweight='bold')
    
    # 5. Interiores (d < |R - r|)
    draw_two_circles(axes[4], R, r, 0.2, 'INTERIORES', 'd < |R - r|', colors)
    
    # 6. Concéntricas (d = 0)
    ax6 = axes[5]
    theta = np.linspace(0, 2*np.pi, 100)
    ax6.plot(R*np.cos(theta), R*np.sin(theta), color=colors['primary'], lw=2)
    ax6.fill(R*np.cos(theta), R*np.sin(theta), color=colors['primary'], alpha=0.15)
    ax6.plot(r*np.cos(theta), r*np.sin(theta), color=colors['secondary'], lw=2)
    ax6.fill(r*np.cos(theta), r*np.sin(theta), color=colors['secondary'], alpha=0.15)
    ax6.plot(0, 0, 'o', color='#374151', markersize=5)
    ax6.text(0.1, 0.1, 'O', fontsize=9)
    ax6.set_title('CONCÉNTRICAS', fontsize=10, fontweight='bold', pad=5)
    ax6.text(0, -1.8, 'd = 0', fontsize=9, ha='center', color='#4b5563', style='italic')
    
    for ax in axes:
        ax.set_xlim(-1.5, 3)
        ax.set_ylim(-2.2, 1.8)
        ax.set_aspect('equal')
        ax.axis('off')
    
    # Leyenda general
    fig.text(0.5, 0.02, 'd = distancia entre centros | R = radio mayor | r = radio menor', 
             ha='center', fontsize=10, color='#6b7280')
    
    fig.suptitle('Posiciones Relativas de Dos Circunferencias', fontsize=14, 
                 fontweight='bold')
    return fig

def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])

if __name__ == "__main__":
    fig = generate()
    paths = save_figure(fig, get_output_dir(), METADATA["name"])
    print(f"✅ Generado: {paths}")
