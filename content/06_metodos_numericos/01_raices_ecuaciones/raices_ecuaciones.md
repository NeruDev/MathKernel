# Teoría: Raíces de Ecuaciones
## 1. Introducción

El problema de encontrar raíces consiste en hallar valores $x^*$ tales que $f(x^*) = 0$.

**Ejemplos de ecuaciones sin solución analítica:**
- $x - e^{-x} = 0$
- $x^3 - 2x - 5 = 0$
- $\cos(x) = x$

---

## 2. Fundamentos Teóricos

### 2.1 Teorema del Valor Intermedio

> Si $f$ es continua en $[a, b]$ y $f(a) \cdot f(b) < 0$, entonces existe al menos un $c \in (a, b)$ tal que $f(c) = 0$.

Este teorema fundamenta los **métodos cerrados**.

### 2.2 Teorema del Punto Fijo

> Sea $g: [a, b] \to [a, b]$ continua. Si $|g'(x)| \leq L < 1$ para todo $x \in (a, b)$, entonces:
> 1. Existe un único punto fijo $p$ tal que $g(p) = p$
> 2. La sucesión $x_{n+1} = g(x_n)$ converge a $p$ para cualquier $x_0 \in [a, b]$

### 2.3 Series de Taylor

Base teórica del método de Newton-Raphson:

$$f(x) = f(x_n) + f'(x_n)(x - x_n) + \frac{f''(\xi)}{2}(x - x_n)^2$$

Si $x^*$ es raíz, aproximamos:
$$0 \approx f(x_n) + f'(x_n)(x^* - x_n)$$
$$x^* \approx x_n - \frac{f(x_n)}{f'(x_n)}$$

---

## 3. Métodos Cerrados

### 3.1 Método de Bisección

**Idea:** Dividir el intervalo $[a, b]$ repetidamente por la mitad.

**Algoritmo:**
1. Verificar $f(a) \cdot f(b) < 0$
2. Calcular $c = \frac{a + b}{2}$
3. Si $f(c) = 0$ → terminar
4. Si $f(a) \cdot f(c) < 0$ → $b = c$
5. Si no → $a = c$
6. Repetir hasta convergencia

**Análisis de error:**
Después de $n$ iteraciones:
$$|x_n - x^*| \leq \frac{b - a}{2^n}$$

**Número de iteraciones requeridas:**
$$n \geq \frac{\ln(b - a) - \ln(\varepsilon)}{\ln(2)}$$

### 3.2 Método de la Falsa Posición (Regula Falsi)

**Idea:** En lugar del punto medio, usar la intersección de la secante con el eje $x$.

$$c = b - f(b)\frac{b - a}{f(b) - f(a)}$$

**Ventaja:** Generalmente más rápido que bisección.
**Desventaja:** Puede tener convergencia lenta si un extremo queda fijo.

---

## 4. Métodos Abiertos

### 4.1 Método de Newton-Raphson

**Derivación geométrica:** La tangente a $f$ en $x_n$ corta al eje $x$ en $x_{n+1}$.

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**Convergencia cuadrática:**
$$e_{n+1} \approx \frac{f''(x^*)}{2f'(x^*)} e_n^2$$

**Condiciones de convergencia:**
- $f'(x^*) \neq 0$ (raíz simple)
- $x_0$ suficientemente cerca de $x^*$
- $f'' continua$

**Raíces múltiples:** Si $x^*$ tiene multiplicidad $m$:
$$x_{n+1} = x_n - m\frac{f(x_n)}{f'(x_n)}$$

### 4.2 Método de la Secante

**Idea:** Aproximar $f'(x_n)$ usando diferencias finitas:
$$f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$

**Fórmula:**
$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

**Orden de convergencia:** $p = \frac{1 + \sqrt{5}}{2} \approx 1.618$ (número áureo)

**Ventaja:** No requiere calcular $f'(x)$.

### 4.3 Método de Punto Fijo

**Idea:** Reescribir $f(x) = 0$ como $x = g(x)$ e iterar.

$$x_{n+1} = g(x_n)$$

**Ejemplo:** Para $x^3 - 2x - 5 = 0$:
- $g_1(x) = \frac{x^3 - 5}{2}$
- $g_2(x) = \sqrt[3]{2x + 5}$
- $g_3(x) = \sqrt{\frac{5}{x-2}}$

**Convergencia:** Depende de $|g'(x^*)|$:
- $|g'(x^*)| < 1$: Converge
- $|g'(x^*)| > 1$: Diverge

---

## 5. Análisis de Convergencia

### 5.1 Error y Orden de Convergencia

**Definición:** Un método tiene orden de convergencia $p$ si:
$$\lim_{n \to \infty} \frac{|e_{n+1}|}{|e_n|^p} = C \neq 0$$

donde $e_n = x_n - x^*$.

| Método | Orden $p$ | Convergencia |
|--------|--------|--------------|
| Bisección | 1 | Lineal |
| Newton-Raphson | 2 | Cuadrática |
| Secante | 1.618 | Supralineal |
| Punto Fijo | 1 | Lineal |
| Regula Falsi | 1 | Lineal |

### 5.2 Eficiencia Computacional

El **índice de eficiencia** mide el costo por iteración:
$$EI = p^{1/k}$$

donde $k$ es el número de evaluaciones de función por iteración.

| Método | $k$ | $EI$ |
|--------|-----|------|
| Bisección | 1 | 1.0 |
| Newton | 2 | 1.414 |
| Secante | 1 | 1.618 |

---

## 6. Problemas Comunes

### 6.1 Raíces Múltiples

Si $f(x) = (x - x^*)^m h(x)$ con $h(x^*) \neq 0$:
- Newton-Raphson tiene convergencia lineal
- Solución: Usar $u(x) = \frac{f(x)}{f'(x)}$ (Newton modificado)

### 6.2 Divergencia

**Causas comunes:**
1. $x_0$ muy lejos de $x^*$
2. $f'(x) \approx 0$ cerca de la raíz
3. Oscilación alrededor de puntos de inflexión

### 6.3 Criterios de Paro

1. **Tolerancia en $x$:** $|x_{n+1} - x_n| < \varepsilon$
2. **Tolerancia en $f$:** $|f(x_n)| < \delta$
3. **Número máximo de iteraciones:** $n > N_{max}$

---

## 7. Aplicaciones

1. **Ingeniería:** Encontrar puntos de equilibrio
2. **Física:** Resolver ecuaciones trascendentes
3. **Economía:** Calcular tasas de interés (TIR)
4. **Química:** Equilibrio de reacciones

**Ejemplo (TIR):** Resolver para $r$:
$$\sum_{t=1}^{n} \frac{C_t}{(1+r)^t} - I_0 = 0$$
