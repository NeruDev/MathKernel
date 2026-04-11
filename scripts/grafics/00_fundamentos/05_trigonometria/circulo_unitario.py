"""
Gráfico: Círculo Unitario con Funciones Trigonométricas
=======================================================

Topic: FUN-05 Trigonometría
Usado en: theory/FUN-05-Teoria-Trigonometria.md (Sección 5.3)

Muestra el círculo unitario con las funciones trigonométricas.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from templates import (
    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

METADATA = {
    "topic_id": "FUN-05",
    "name": "circulo_unitario",
    "description": "Círculo unitario con definición de seno y coseno",
    "used_in": ["theory/FUN-05-Teoria-Trigonometria.md"],
    "section": "5.3 Funciones trigonométricas en el círculo unitario",
}

def generate() -> plt.Figure:
    """Genera el diagrama del círculo unitario."""
    setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(12, 10), layout='constrained')
    gs = fig.add_gridspec(2, 2, height_ratios=[3, 1], hspace=0.15)
    
    ax_main = fig.add_subplot(gs[0, :])
    ax_info = fig.add_subplot(gs[1, :])
    
    # =========================================
    # PANEL PRINCIPAL: Círculo unitario
    # =========================================
    
    # Ejes
    ax_main.axhline(y=0, color='#9ca3af', linewidth=1.5, zorder=1)
    ax_main.axvline(x=0, color='#9ca3af', linewidth=1.5, zorder=1)
    
    # Círculo unitario
    theta_circle = np.linspace(0, 2*np.pi, 100)
    ax_main.plot(np.cos(theta_circle), np.sin(theta_circle), 
                color=colors['primary'], linewidth=2.5, zorder=2)
    
    # Ángulo de ejemplo: 60°
    theta = np.radians(50)
    P = np.array([np.cos(theta), np.sin(theta)])
    
    # Radio al punto P
    ax_main.plot([0, P[0]], [0, P[1]], color='#f59e0b', linewidth=2.5, zorder=3)
    
    # Punto P en el círculo
    ax_main.plot(P[0], P[1], 'o', color='#f59e0b', markersize=10, zorder=5)
    ax_main.text(P[0] + 0.08, P[1] + 0.08, f'P(cos θ, sin θ)', fontsize=11, 
                fontweight='bold', color='#f59e0b')
    
    # Proyección sobre eje X (coseno)
    ax_main.plot([P[0], P[0]], [0, P[1]], '--', color=colors['accent'], linewidth=2, zorder=3)
    ax_main.plot([0, P[0]], [0, 0], color=colors['tertiary'], linewidth=3, zorder=4)
    ax_main.text(P[0]/2, -0.12, 'cos θ', fontsize=12, ha='center', 
                fontweight='bold', color=colors['tertiary'])
    
    # Proyección sobre eje Y (seno)
    ax_main.plot([0, P[0]], [P[1], P[1]], '--', color=colors['accent'], linewidth=2, zorder=3)
    ax_main.plot([0, 0], [0, P[1]], color=colors['secondary'], linewidth=3, zorder=4)
    ax_main.text(-0.15, P[1]/2, 'sin θ', fontsize=12, ha='center', rotation=90,
                fontweight='bold', color=colors['secondary'])
    
    # Arco del ángulo
    arc_angles = np.linspace(0, theta, 30)
    arc_r = 0.25
    ax_main.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 
                color='#f59e0b', linewidth=2)
    ax_main.text(0.35, 0.12, 'θ', fontsize=14, fontweight='bold', color='#f59e0b')
    
    # Punto origen
    ax_main.plot(0, 0, 'o', color=colors['text'], markersize=6, zorder=5)
    ax_main.text(-0.08, -0.12, 'O', fontsize=12, fontweight='bold')
    
    # Puntos cardinales
    cardinal_points = [
        (1, 0, '(1, 0)', 'left', -0.08),
        (-1, 0, '(-1, 0)', 'right', -0.08),
        (0, 1, '(0, 1)', 'center', 0.08),
        (0, -1, '(0, -1)', 'center', -0.15),
    ]
    for x, y, label, ha, y_off in cardinal_points:
        ax_main.plot(x, y, 'o', color=colors['primary'], markersize=6)
        ax_main.text(x, y + y_off, label, fontsize=10, ha=ha, color='#6b7280')
    
    # Ángulos notables
    notable_angles = [
        (30, 'π/6'),
        (45, 'π/4'),
        (60, 'π/3'),
        (90, 'π/2'),
        (120, '2π/3'),
        (135, '3π/4'),
        (150, '5π/6'),
        (180, 'π'),
        (210, '7π/6'),
        (225, '5π/4'),
        (240, '4π/3'),
        (270, '3π/2'),
        (300, '5π/3'),
        (315, '7π/4'),
        (330, '11π/6'),
    ]
    
    for deg, label in notable_angles:
        rad = np.radians(deg)
        x, y = 1.15 * np.cos(rad), 1.15 * np.sin(rad)
        ax_main.text(x, y, label, fontsize=8, ha='center', va='center', color='#9ca3af')
        # Pequeña marca en el círculo
        ax_main.plot(np.cos(rad), np.sin(rad), '.', color='#d1d5db', markersize=4)
    
    # Etiquetas de cuadrantes
    ax_main.text(0.6, 0.7, 'I', fontsize=16, fontweight='bold', color='#d1d5db')
    ax_main.text(-0.7, 0.7, 'II', fontsize=16, fontweight='bold', color='#d1d5db')
    ax_main.text(-0.7, -0.7, 'III', fontsize=16, fontweight='bold', color='#d1d5db')
    ax_main.text(0.6, -0.7, 'IV', fontsize=16, fontweight='bold', color='#d1d5db')
    
    # Radio = 1
    ax_main.text(0.35, 0.5, 'r = 1', fontsize=11, color='#f59e0b', rotation=50,
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    
    ax_main.set_xlim(-1.4, 1.6)
    ax_main.set_ylim(-1.4, 1.4)
    ax_main.set_aspect('equal')
    ax_main.set_xlabel('x', fontsize=12)
    ax_main.set_ylabel('y', fontsize=12)
    ax_main.spines['top'].set_visible(False)
    ax_main.spines['right'].set_visible(False)
    ax_main.spines['bottom'].set_visible(False)
    ax_main.spines['left'].set_visible(False)
    ax_main.set_xticks([])
    ax_main.set_yticks([])
    
    # =========================================
    # PANEL INFERIOR: Información
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Definiciones
    ax_info.add_patch(plt.Rectangle((0.02, 0.15), 0.45, 0.75, 
                                    facecolor='#f0fdf4', edgecolor=colors['accent'],
                                    linewidth=1.5, transform=ax_info.transAxes))
    
    ax_info.text(0.25, 0.82, 'Definición', fontsize=11, fontweight='bold',
                ha='center', color=colors['accent'])
    
    defs = [
        r'$\cos\theta = x$ (coordenada x)',
        r'$\sin\theta = y$ (coordenada y)',
        r'$\tan\theta = \frac{y}{x} = \frac{\sin\theta}{\cos\theta}$',
    ]
    y_pos = 0.68
    for d in defs:
        ax_info.text(0.25, y_pos, d, fontsize=10, ha='center', color='#374151')
        y_pos -= 0.15
    
    # Signos por cuadrante
    ax_info.add_patch(plt.Rectangle((0.53, 0.15), 0.45, 0.75, 
                                    facecolor='#fef3c7', edgecolor='#f59e0b',
                                    linewidth=1.5, transform=ax_info.transAxes))
    
    ax_info.text(0.75, 0.82, 'Signos por Cuadrante', fontsize=11, fontweight='bold',
                ha='center', color='#f59e0b')
    
    signos = [
        ('I (0°-90°):', 'sin+, cos+, tan+'),
        ('II (90°-180°):', 'sin+, cos−, tan−'),
        ('III (180°-270°):', 'sin−, cos−, tan+'),
        ('IV (270°-360°):', 'sin−, cos+, tan−'),
    ]
    y_pos = 0.68
    for quad, signs in signos:
        ax_info.text(0.58, y_pos, quad, fontsize=9, color='#374151', fontweight='bold')
        ax_info.text(0.92, y_pos, signs, fontsize=9, color='#6b7280', ha='right')
        y_pos -= 0.13
    
    fig.suptitle('El Círculo Unitario', fontsize=14, fontweight='bold')
    
    return fig


def get_output_dir():
    return get_output_dir_for_topic(METADATA["topic_id"])


if __name__ == "__main__":
    print(f"Generando: {METADATA['name']}")
    fig = generate()
    output_dir = get_output_dir()
    paths = save_figure(fig, output_dir, METADATA["name"])
    print(f"✅ Guardado en: {output_dir}")
    for fmt, path in paths.items():
        print(f"   • {fmt}: {path.name}")
