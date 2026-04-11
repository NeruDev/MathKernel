"""
Gráfico: Funciones Trigonométricas Inversas
===========================================

Topic: FUN-05 Trigonometría
Usado en: theory/FUN-05-Teoria-Trigonometria.md (Sección 5.10)

Gráficas de arcoseno, arcocoseno y arcotangente.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import matplotlib.pyplot as plt
import numpy as np

from templates import (
    setup_style,
    get_colors,
    get_output_dir_for_topic,
    save_figure,
)

METADATA = {
    "topic_id": "FUN-05",
    "name": "funciones_inversas",
    "description": "Funciones trigonométricas inversas: arcsen, arccos, arctan",
    "used_in": ["theory/FUN-05-Teoria-Trigonometria.md"],
    "section": "5.10 Funciones trigonométricas inversas",
}

def generate() -> plt.Figure:
    """Genera las gráficas de funciones inversas."""
    setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 9), layout='constrained')
    gs = fig.add_gridspec(2, 3, height_ratios=[1.3, 0.7], hspace=0.25, wspace=0.2)
    
    ax_arcsin = fig.add_subplot(gs[0, 0])
    ax_arccos = fig.add_subplot(gs[0, 1])
    ax_arctan = fig.add_subplot(gs[0, 2])
    ax_info = fig.add_subplot(gs[1, :])
    
    # =========================================
    # ARCOSENO
    # =========================================
    x_arcsin = np.linspace(-1, 1, 200)
    y_arcsin = np.arcsin(x_arcsin)
    
    ax_arcsin.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_arcsin.axvline(x=0, color='#d1d5db', linewidth=1)
    
    # Líneas de rango
    ax_arcsin.axhline(y=np.pi/2, color='#e5e7eb', linewidth=1, linestyle='--')
    ax_arcsin.axhline(y=-np.pi/2, color='#e5e7eb', linewidth=1, linestyle='--')
    
    ax_arcsin.plot(x_arcsin, y_arcsin, color=colors['secondary'], linewidth=2.5)
    
    # Puntos notables
    points = [(-1, -np.pi/2), (0, 0), (1, np.pi/2)]
    for x, y in points:
        ax_arcsin.plot(x, y, 'o', color=colors['secondary'], markersize=6)
    
    ax_arcsin.set_xlim(-1.3, 1.3)
    ax_arcsin.set_ylim(-2, 2)
    ax_arcsin.set_xlabel('x', fontsize=10)
    ax_arcsin.set_ylabel('y', fontsize=10)
    ax_arcsin.set_title(r'$y = \arcsin(x) = \sin^{-1}(x)$', fontsize=11, fontweight='bold',
                       color=colors['secondary'])
    ax_arcsin.set_xticks([-1, 0, 1])
    ax_arcsin.set_yticks([-np.pi/2, 0, np.pi/2])
    ax_arcsin.set_yticklabels(['-π/2', '0', 'π/2'], fontsize=9)
    ax_arcsin.spines['top'].set_visible(False)
    ax_arcsin.spines['right'].set_visible(False)
    
    # Anotaciones
    ax_arcsin.text(0.65, 1.2, 'D: [-1, 1]', fontsize=9, color='#6b7280')
    ax_arcsin.text(0.65, 0.95, 'R: [-π/2, π/2]', fontsize=9, color='#6b7280')
    
    # =========================================
    # ARCOCOSENO
    # =========================================
    x_arccos = np.linspace(-1, 1, 200)
    y_arccos = np.arccos(x_arccos)
    
    ax_arccos.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_arccos.axvline(x=0, color='#d1d5db', linewidth=1)
    
    # Líneas de rango
    ax_arccos.axhline(y=np.pi, color='#e5e7eb', linewidth=1, linestyle='--')
    
    ax_arccos.plot(x_arccos, y_arccos, color=colors['tertiary'], linewidth=2.5)
    
    # Puntos notables
    points = [(-1, np.pi), (0, np.pi/2), (1, 0)]
    for x, y in points:
        ax_arccos.plot(x, y, 'o', color=colors['tertiary'], markersize=6)
    
    ax_arccos.set_xlim(-1.3, 1.3)
    ax_arccos.set_ylim(-0.3, 3.5)
    ax_arccos.set_xlabel('x', fontsize=10)
    ax_arccos.set_ylabel('y', fontsize=10)
    ax_arccos.set_title(r'$y = \arccos(x) = \cos^{-1}(x)$', fontsize=11, fontweight='bold',
                       color=colors['tertiary'])
    ax_arccos.set_xticks([-1, 0, 1])
    ax_arccos.set_yticks([0, np.pi/2, np.pi])
    ax_arccos.set_yticklabels(['0', 'π/2', 'π'], fontsize=9)
    ax_arccos.spines['top'].set_visible(False)
    ax_arccos.spines['right'].set_visible(False)
    
    # Anotaciones
    ax_arccos.text(0.65, 2.8, 'D: [-1, 1]', fontsize=9, color='#6b7280')
    ax_arccos.text(0.65, 2.5, 'R: [0, π]', fontsize=9, color='#6b7280')
    
    # =========================================
    # ARCOTANGENTE
    # =========================================
    x_arctan = np.linspace(-5, 5, 500)
    y_arctan = np.arctan(x_arctan)
    
    ax_arctan.axhline(y=0, color='#d1d5db', linewidth=1)
    ax_arctan.axvline(x=0, color='#d1d5db', linewidth=1)
    
    # Asíntotas horizontales
    ax_arctan.axhline(y=np.pi/2, color='#e5e7eb', linewidth=1, linestyle='--')
    ax_arctan.axhline(y=-np.pi/2, color='#e5e7eb', linewidth=1, linestyle='--')
    
    ax_arctan.plot(x_arctan, y_arctan, color='#f59e0b', linewidth=2.5)
    
    # Puntos notables
    points = [(-1, -np.pi/4), (0, 0), (1, np.pi/4)]
    for x, y in points:
        ax_arctan.plot(x, y, 'o', color='#f59e0b', markersize=6)
    
    ax_arctan.set_xlim(-5, 5)
    ax_arctan.set_ylim(-2, 2)
    ax_arctan.set_xlabel('x', fontsize=10)
    ax_arctan.set_ylabel('y', fontsize=10)
    ax_arctan.set_title(r'$y = \arctan(x) = \tan^{-1}(x)$', fontsize=11, fontweight='bold',
                       color='#f59e0b')
    ax_arctan.set_yticks([-np.pi/2, 0, np.pi/2])
    ax_arctan.set_yticklabels(['-π/2', '0', 'π/2'], fontsize=9)
    ax_arctan.spines['top'].set_visible(False)
    ax_arctan.spines['right'].set_visible(False)
    
    # Anotaciones
    ax_arctan.text(2.5, 1.2, 'D: ℝ', fontsize=9, color='#6b7280')
    ax_arctan.text(2.5, 0.95, 'R: (-π/2, π/2)', fontsize=9, color='#6b7280')
    ax_arctan.text(-4.5, np.pi/2 + 0.15, 'asíntota', fontsize=8, color='#9ca3af')
    ax_arctan.text(-4.5, -np.pi/2 - 0.15, 'asíntota', fontsize=8, color='#9ca3af')
    
    # =========================================
    # INFORMACIÓN
    # =========================================
    ax_info.axis('off')
    ax_info.set_xlim(0, 1)
    ax_info.set_ylim(0, 1)
    
    # Tabla de resumen
    ax_info.add_patch(plt.Rectangle((0.02, 0.05), 0.96, 0.9,
                                    facecolor='#f9fafb', edgecolor='#d1d5db',
                                    linewidth=1.5))
    
    ax_info.text(0.5, 0.88, 'Resumen de Funciones Trigonométricas Inversas', 
                fontsize=11, fontweight='bold', ha='center', color=colors['text'])
    
    # Headers
    headers = ['Función', 'Dominio', 'Rango', 'Notación']
    x_positions = [0.15, 0.35, 0.55, 0.8]
    for x, h in zip(x_positions, headers):
        ax_info.text(x, 0.75, h, fontsize=10, fontweight='bold', ha='center',
                    color=colors['primary'])
    
    # Línea separadora
    ax_info.axhline(y=0.7, xmin=0.05, xmax=0.95, color='#d1d5db', linewidth=1)
    
    # Datos
    data = [
        ('Arcoseno', '[-1, 1]', '[-π/2, π/2]', 'arcsin, sin⁻¹', colors['secondary']),
        ('Arcocoseno', '[-1, 1]', '[0, π]', 'arccos, cos⁻¹', colors['tertiary']),
        ('Arcotangente', 'ℝ', '(-π/2, π/2)', 'arctan, tan⁻¹', '#f59e0b'),
    ]
    
    y_pos = 0.58
    for func, dom, ran, nota, color in data:
        ax_info.text(0.15, y_pos, func, fontsize=9, ha='center', color=color, fontweight='bold')
        ax_info.text(0.35, y_pos, dom, fontsize=9, ha='center', color='#374151')
        ax_info.text(0.55, y_pos, ran, fontsize=9, ha='center', color='#374151')
        ax_info.text(0.8, y_pos, nota, fontsize=9, ha='center', color='#6b7280')
        y_pos -= 0.15
    
    # Nota importante
    ax_info.text(0.5, 0.1, '⚠️ Nota: sin⁻¹(x) ≠ 1/sin(x). La notación "⁻¹" indica función inversa.',
                fontsize=9, ha='center', color='#dc2626', style='italic')
    
    fig.suptitle('Funciones Trigonométricas Inversas', fontsize=14, fontweight='bold')
    
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
