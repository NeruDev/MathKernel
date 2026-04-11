"""
Gráfico: Ángulos Notables y sus Valores Exactos
===============================================

Topic: FUN-05 Trigonometría
Usado en: theory/FUN-05-Teoria-Trigonometria.md (Sección 5.3)

Tabla visual con los valores exactos de ángulos notables.
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
    "name": "angulos_notables_valores",
    "description": "Tabla de valores exactos de funciones trigonométricas para ángulos notables",
    "used_in": ["theory/FUN-05-Teoria-Trigonometria.md"],
    "section": "5.3 Valores de las funciones en ángulos notables",
}

def generate() -> plt.Figure:
    """Genera la tabla de valores de ángulos notables."""
    setup_style()
    colors = get_colors()
    
    fig = plt.figure(figsize=(14, 8), layout='constrained')
    gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.08)
    
    ax_table = fig.add_subplot(gs[0])
    ax_visual = fig.add_subplot(gs[1])
    
    # =========================================
    # PANEL IZQUIERDO: Tabla de valores
    # =========================================
    ax_table.axis('off')
    ax_table.set_xlim(0, 1)
    ax_table.set_ylim(0, 1)
    
    # Datos de la tabla
    headers = ['θ (grados)', 'θ (rad)', 'sin θ', 'cos θ', 'tan θ']
    data = [
        ['0°', '0', '0', '1', '0'],
        ['30°', 'π/6', '1/2', '√3/2', '√3/3'],
        ['45°', 'π/4', '√2/2', '√2/2', '1'],
        ['60°', 'π/3', '√3/2', '1/2', '√3'],
        ['90°', 'π/2', '1', '0', '∞'],
        ['120°', '2π/3', '√3/2', '−1/2', '−√3'],
        ['135°', '3π/4', '√2/2', '−√2/2', '−1'],
        ['150°', '5π/6', '1/2', '−√3/2', '−√3/3'],
        ['180°', 'π', '0', '−1', '0'],
        ['270°', '3π/2', '−1', '0', '∞'],
        ['360°', '2π', '0', '1', '0'],
    ]
    
    n_cols = len(headers)
    n_rows = len(data) + 1  # +1 para headers
    
    col_widths = [0.16, 0.14, 0.22, 0.22, 0.22]  # Proporciones de columna
    col_x = [0.02]
    for w in col_widths[:-1]:
        col_x.append(col_x[-1] + w)
    
    row_height = 0.075
    y_start = 0.92
    
    # Dibujar headers
    for i, (header, x) in enumerate(zip(headers, col_x)):
        rect = plt.Rectangle((x, y_start - row_height), col_widths[i], row_height,
                             facecolor=colors['primary'], edgecolor='white', linewidth=2)
        ax_table.add_patch(rect)
        ax_table.text(x + col_widths[i]/2, y_start - row_height/2, header,
                     fontsize=10, fontweight='bold', ha='center', va='center', color='white')
    
    # Dibujar filas de datos
    for row_idx, row in enumerate(data):
        y = y_start - (row_idx + 2) * row_height
        # Color alternado para filas
        row_color = '#f3f4f6' if row_idx % 2 == 0 else 'white'
        
        # Resaltar ángulos notables principales (30, 45, 60)
        if row[0] in ['30°', '45°', '60°']:
            row_color = '#fef3c7'
        
        for col_idx, (value, x) in enumerate(zip(row, col_x)):
            rect = plt.Rectangle((x, y), col_widths[col_idx], row_height,
                                 facecolor=row_color, edgecolor='#d1d5db', linewidth=1)
            ax_table.add_patch(rect)
            
            # Color especial para valores negativos o indefinidos
            text_color = '#374151'
            if '−' in value or value == '∞':
                text_color = '#dc2626'
            
            ax_table.text(x + col_widths[col_idx]/2, y + row_height/2, value,
                         fontsize=9, ha='center', va='center', color=text_color)
    
    ax_table.text(0.5, 0.03, '* Valores resaltados: ángulos más frecuentes',
                 fontsize=9, ha='center', color='#9ca3af', style='italic')
    
    # =========================================
    # PANEL DERECHO: Visualización triángulos
    # =========================================
    ax_visual.axis('off')
    ax_visual.set_xlim(0, 1)
    ax_visual.set_ylim(0, 1)
    
    # Título
    ax_visual.text(0.5, 0.95, 'Triángulos de Referencia', fontsize=11, fontweight='bold',
                  ha='center', color=colors['text'])
    
    # Triángulo 45-45-90
    ax_visual.add_patch(plt.Rectangle((0.05, 0.55), 0.9, 0.35,
                                      facecolor='#eff6ff', edgecolor=colors['primary'],
                                      linewidth=1.5))
    ax_visual.text(0.5, 0.86, 'Triángulo 45°-45°-90°', fontsize=10, fontweight='bold',
                  ha='center', color=colors['primary'])
    
    # Dibujar triángulo 45-45-90
    tri_45 = np.array([[0.2, 0.6], [0.45, 0.6], [0.45, 0.83]])
    ax_visual.fill(tri_45[:, 0], tri_45[:, 1], facecolor='#dbeafe', edgecolor=colors['primary'],
                  linewidth=2)
    # Etiquetas
    ax_visual.text(0.32, 0.57, '1', fontsize=10, ha='center', color='#374151')
    ax_visual.text(0.48, 0.71, '1', fontsize=10, ha='left', color='#374151')
    ax_visual.text(0.29, 0.73, '√2', fontsize=10, ha='center', color=colors['primary'],
                  fontweight='bold', rotation=45)
    ax_visual.text(0.23, 0.62, '45°', fontsize=9, color='#f59e0b')
    ax_visual.text(0.42, 0.81, '45°', fontsize=9, color='#f59e0b')
    # Ángulo recto
    rect_mark = plt.Rectangle((0.42, 0.6), 0.03, 0.03, fill=False, edgecolor='#374151')
    ax_visual.add_patch(rect_mark)
    
    # Proporciones
    ax_visual.text(0.75, 0.74, 'Proporciones:', fontsize=9, fontweight='bold', color='#374151')
    ax_visual.text(0.75, 0.68, '1 : 1 : √2', fontsize=10, color=colors['primary'])
    
    # Triángulo 30-60-90
    ax_visual.add_patch(plt.Rectangle((0.05, 0.1), 0.9, 0.4,
                                      facecolor='#f0fdf4', edgecolor=colors['secondary'],
                                      linewidth=1.5))
    ax_visual.text(0.5, 0.46, 'Triángulo 30°-60°-90°', fontsize=10, fontweight='bold',
                  ha='center', color=colors['secondary'])
    
    # Dibujar triángulo 30-60-90
    tri_30_60 = np.array([[0.15, 0.15], [0.5, 0.15], [0.5, 0.42]])
    ax_visual.fill(tri_30_60[:, 0], tri_30_60[:, 1], facecolor='#dcfce7', 
                  edgecolor=colors['secondary'], linewidth=2)
    # Etiquetas
    ax_visual.text(0.32, 0.12, '√3', fontsize=10, ha='center', color='#374151')
    ax_visual.text(0.53, 0.28, '1', fontsize=10, ha='left', color='#374151')
    ax_visual.text(0.28, 0.31, '2', fontsize=10, ha='center', color=colors['secondary'],
                  fontweight='bold', rotation=38)
    ax_visual.text(0.19, 0.17, '30°', fontsize=9, color='#f59e0b')
    ax_visual.text(0.46, 0.39, '60°', fontsize=9, color='#f59e0b')
    # Ángulo recto
    rect_mark2 = plt.Rectangle((0.47, 0.15), 0.03, 0.03, fill=False, edgecolor='#374151')
    ax_visual.add_patch(rect_mark2)
    
    # Proporciones
    ax_visual.text(0.65, 0.34, 'Proporciones:', fontsize=9, fontweight='bold', color='#374151')
    ax_visual.text(0.65, 0.28, '1 : √3 : 2', fontsize=10, color=colors['secondary'])
    ax_visual.text(0.65, 0.2, '(opuesto 30° : opuesto 60°', fontsize=8, color='#6b7280')
    ax_visual.text(0.65, 0.15, ' : hipotenusa)', fontsize=8, color='#6b7280')
    
    fig.suptitle('Valores Exactos de las Funciones Trigonométricas', fontsize=14, fontweight='bold')
    
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
