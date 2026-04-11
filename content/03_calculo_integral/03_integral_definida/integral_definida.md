<!--
HUMANO:
Teoría de [integral definida](../../../glossary.md#integral-definida).

IA:
Desarrolla definición, teoremas y propiedades.

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría de la Integral Definida

---

## 3.1 Sumas de Riemann

### Partición del Intervalo
Dado un intervalo $[a, b]$, una **partición** $P$ divide el intervalo en $n$ subintervalos:
$$a = x_0 < x_1 < x_2 < \cdots < x_n = b$$

El ancho de cada subintervalo es:
$$\Delta x_i = x_i - x_{i-1}$$

Para partición **regular**: $\Delta x = \frac{b-a}{n}$

### Suma de Riemann
Elegimos un punto de muestra $x_i^*$ en cada subintervalo $[x_{i-1}, x_i]$:

$$S_n = \sum_{i=1}^{n} f(x_i^*) \Delta x_i$$

### Tipos de Sumas
- **Suma izquierda**: $x_i^* = x_{i-1}$ (extremo izquierdo)
- **Suma derecha**: $x_i^* = x_i$ (extremo derecho)
- **Suma del punto medio**: $x_i^* = \frac{x_{i-1} + x_i}{2}$

---

## 3.2 Definición de Integral Definida

### Definición
Si $f$ es una [función](../../../glossary.md#funcion) continua en $[a, b]$, la **[integral definida](../../../glossary.md#integral-definida)** de $f$ de $a$ a $b$ es:

$$\boxed{\int_a^b f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x}$$

donde:
- $\Delta x = \frac{b-a}{n}$
- $x_i^* \in [x_{i-1}, x_i]$

### Interpretación Geométrica
- Si $f(x) \geq 0$: La integral representa el **área** bajo la curva $y = f(x)$, sobre el eje $x$, de $x = a$ a $x = b$.
- Si $f(x) < 0$: El área se considera **negativa**.
- En general: **Área neta** (áreas arriba menos áreas abajo del eje).

### Notación
$$\int_a^b f(x) \, dx = \Big[ F(x) \Big]_a^b = F(b) - F(a)$$

---

## 3.3 Propiedades de la Integral Definida

### Propiedades Básicas

**1. Integral sobre intervalo de longitud cero:**
$$\int_a^a f(x) \, dx = 0$$

**2. Inversión de [límites](../../../glossary.md#limites):**
$$\int_a^b f(x) \, dx = -\int_b^a f(x) \, dx$$

**3. Constante multiplicativa:**
$$\int_a^b cf(x) \, dx = c\int_a^b f(x) \, dx$$

**4. Suma y diferencia:**
$$\int_a^b [f(x) \pm g(x)] \, dx = \int_a^b f(x) \, dx \pm \int_a^b g(x) \, dx$$

**5. Aditividad respecto al intervalo:**
$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$$

### Propiedades de Comparación

**6.** Si $f(x) \geq 0$ en $[a, b]$, entonces:
$$\int_a^b f(x) \, dx \geq 0$$

**7.** Si $f(x) \geq g(x)$ en $[a, b]$, entonces:
$$\int_a^b f(x) \, dx \geq \int_a^b g(x) \, dx$$

**8. Acotamiento:**
Si $m \leq f(x) \leq M$ en $[a, b]$, entonces:
$$m(b-a) \leq \int_a^b f(x) \, dx \leq M(b-a)$$

---

## 3.4 Teorema Fundamental del Cálculo (Parte 1)

### Enunciado
Si $f$ es continua en $[a, b]$, entonces la [función](../../../glossary.md#funcion) $g$ definida por:

$$g(x) = \int_a^x f(t) \, dt, \quad a \leq x \leq b$$

es continua en $[a, b]$ y diferenciable en $(a, b)$, y su [derivada](../../../glossary.md#derivada) es:

$$\boxed{g'(x) = f(x)}$$

### Interpretación
La [derivada](../../../glossary.md#derivada) de una integral con [límite](../../../glossary.md#limite) variable es el integrando evaluado en ese límite.

### Generalización (Regla de Leibniz)
Si los [límites](../../../glossary.md#limites) son funciones:

$$\frac{d}{dx}\int_{u(x)}^{v(x)} f(t) \, dt = f(v(x)) \cdot v'(x) - f(u(x)) \cdot u'(x)$$

### Ejemplo
$$\frac{d}{dx}\int_1^{x^2} \cos t \, dt = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

---

## 3.5 Teorema Fundamental del Cálculo (Parte 2)

### Enunciado
Si $f$ es continua en $[a, b]$, y $F$ es cualquier [antiderivada](../../../glossary.md#antiderivada) de $f$ (es decir, $F' = f$), entonces:

$$\boxed{\int_a^b f(x) \, dx = F(b) - F(a)}$$

### Notación
$$F(x) \Big|_a^b = F(b) - F(a)$$

### Significado
Este teorema conecta las dos operaciones fundamentales del cálculo:
- La **derivación** (encontrar tasas de cambio)
- La **integración** (encontrar acumulaciones)

### Ejemplo
$$\int_0^{\pi} \sin x \, dx = [-\cos x]_0^{\pi} = -\cos\pi - (-\cos 0) = -(-1) + 1 = 2$$

---

## 3.6 Sustitución en Integrales Definidas

### Método
Al hacer [sustitución](../../../glossary.md#sustitucion) $u = g(x)$ en una integral definida, los límites deben **cambiarse**:

$$\int_a^b f(g(x)) g'(x) \, dx = \int_{g(a)}^{g(b)} f(u) \, du$$

### Ejemplo
$$\int_0^1 x e^{x^2} dx$$

$u = x^2$, $du = 2x \, dx$

Cuando $x = 0$: $u = 0$
Cuando $x = 1$: $u = 1$

$$= \frac{1}{2}\int_0^1 e^u \, du = \frac{1}{2}[e^u]_0^1 = \frac{1}{2}(e - 1)$$

---

## 3.7 Integrales de Funciones Pares e Impares

### Función Par
$f(-x) = f(x)$ (simétrica respecto al eje $y$)

$$\boxed{\int_{-a}^{a} f(x) \, dx = 2\int_0^a f(x) \, dx}$$

**Ejemplos:** $x^2$, $\cos x$, $\lvert x \rvert$

### Función Impar
$f(-x) = -f(x)$ (simétrica respecto al origen)

$$\boxed{\int_{-a}^{a} f(x) \, dx = 0}$$

**Ejemplos:** $x$, $x^3$, $\sin x$

### Ejemplos de Aplicación

$$\int_{-\pi}^{\pi} \sin x \, dx = 0 \quad \text{(impar)}$$

$$\int_{-2}^{2} x^4 \, dx = 2\int_0^2 x^4 \, dx = 2 \cdot \frac{32}{5} = \frac{64}{5}$$
