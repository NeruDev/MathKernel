# Teoría de Aplicaciones de la Derivada

## 3.1 Recta Tangente y Normal

### Recta Tangente
La recta tangente a $y = f(x)$ en $(a, f(a))$:
$$y - f(a) = f'(a)(x - a)$$

### Recta Normal
La recta normal es perpendicular a la tangente:
$$y - f(a) = -\frac{1}{f'(a)}(x - a) \quad (f'(a) \neq 0)$$

---

## 3.2 Razones de Cambio Relacionadas

### Concepto
Cuando varias cantidades varían con el tiempo y están relacionadas por una ecuación, sus tasas de cambio también están relacionadas.

### Procedimiento
1. Dibujar un diagrama e identificar variables
2. Escribir la ecuación que relaciona las variables
3. Derivar implícitamente respecto al tiempo $t$
4. Sustituir valores conocidos y resolver

---

## 3.3 Valores Extremos

### Definiciones
- **Máximo absoluto:** $f(c) \geq f(x)$ para todo $x$ en el dominio
- **Mínimo absoluto:** $f(c) \leq f(x)$ para todo $x$ en el dominio
- **Máximo relativo:** $f(c) \geq f(x)$ para $x$ cerca de $c$
- **Mínimo relativo:** $f(c) \leq f(x)$ para $x$ cerca de $c$

### Teorema de Weierstrass
Si $f$ es continua en $[a, b]$, entonces $f$ alcanza un máximo y un mínimo absolutos en $[a, b]$.

### Puntos Críticos
$c$ es punto crítico si $f'(c) = 0$ o $f'(c)$ no existe.

### Método del Intervalo Cerrado
Para encontrar extremos absolutos de $f$ continua en $[a, b]$:
1. Encontrar puntos críticos en $(a, b)$
2. Evaluar $f$ en puntos críticos y extremos $a$, $b$
3. El mayor valor es el máximo, el menor es el mínimo

---

## 3.4 Criterio de la Primera Derivada

### Crecimiento y Decrecimiento
- $f'(x) > 0$ en $(a, b)$ → $f$ es **creciente** en $(a, b)$
- $f'(x) < 0$ en $(a, b)$ → $f$ es **decreciente** en $(a, b)$

### Prueba de Extremos
Si $c$ es punto crítico:
- Si $f'$ cambia de $+$ a $-$ en $c$ → **máximo relativo**
- Si $f'$ cambia de $-$ a $+$ en $c$ → **mínimo relativo**
- Si $f'$ no cambia de signo → **no es extremo**

---

## 3.5 Criterio de la Segunda Derivada

### Concavidad
- $f''(x) > 0$ → **cóncava hacia arriba** (∪)
- $f''(x) < 0$ → **cóncava hacia abajo** (∩)

### Puntos de Inflexión
Un punto donde la concavidad cambia de signo.
Candidatos: donde $f''(x) = 0$ o $f''(x)$ no existe.

### Prueba del Extremo
Si $f'(c) = 0$:
- $f''(c) > 0$ → **mínimo relativo** en $c$
- $f''(c) < 0$ → **máximo relativo** en $c$
- $f''(c) = 0$ → prueba no concluyente

---

## 3.6 Problemas de Optimización

### Procedimiento
1. **Entender:** Leer el problema, identificar qué maximizar/minimizar
2. **Diagrama:** Dibujar y etiquetar variables
3. **Objetivo:** Escribir la función a optimizar
4. **Restricción:** Usar la restricción para eliminar variables
5. **Derivar:** Encontrar puntos críticos
6. **Verificar:** Confirmar que es máximo o mínimo
7. **Responder:** Dar la respuesta en contexto

---

## 3.7 Aproximaciones y Diferenciales

### Aproximación Lineal
$$f(x) \approx f(a) + f'(a)(x - a)$$

para $x$ cerca de $a$.

### Diferencial
$$dy = f'(x) \, dx$$

### Propagación de Errores
Si $y = f(x)$ y $\Delta x$ es el error en $x$:
$$\Delta y \approx f'(x) \Delta x$$

Error relativo: $\frac{\Delta y}{y} \approx \frac{f'(x)}{f(x)} \Delta x$

---

## 3.8 Análisis Completo de Funciones

### Pasos
1. **Dominio**
2. **Intersecciones:** con ejes $x$ e $y$
3. **Simetría:** par, impar, periódica
4. **Asíntotas:** verticales, horizontales, oblicuas
5. **Intervalos de crecimiento/decrecimiento**
6. **Máximos y mínimos relativos**
7. **Concavidad y puntos de inflexión**
8. **Graficar**

### Asíntota Oblicua
Si $\lim_{x \to \pm\infty} [f(x) - (mx + b)] = 0$, entonces $y = mx + b$ es asíntota oblicua.

---

## 3.9 Método de Newton-Raphson

### Fórmula
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### Procedimiento
1. Elegir $x_0$ (aproximación inicial)
2. Iterar hasta convergencia
3. El límite es una raíz de $f$

### Convergencia
- Funciona bien si $x_0$ está cerca de la raíz
- Puede fallar si $f'(x_n) \approx 0$
