<!--
HUMANO:
Teoría de [integrales impropias](../../../glossary.md#integrales-impropias).

IA:
Desarrollo formal con todos los tipos y criterios.

---
content_type: theory
format: formal_exposition
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Integrales Impropias

---

## Introducción

Una **[integral impropia](../../../glossary.md#integral-impropia)** es una [integral definida](../../../glossary.md#integral-definida) donde:
1. Uno o ambos [límites](../../../glossary.md#limites) de integración son infinitos (Tipo I)
2. El integrando tiene una discontinuidad en el intervalo (Tipo II)

---

## 5.1 Tipo I: Límites Infinitos

### Definición

**[Límite](../../../glossary.md#limite) superior infinito:**
$$\int_a^{\infty} f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$$

**[Límite](../../../glossary.md#limite) inferior infinito:**
$$\int_{-\infty}^{b} f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$$

**Ambos [límites](../../../glossary.md#limites) infinitos:**
$$\int_{-\infty}^{\infty} f(x)\,dx = \int_{-\infty}^{c} f(x)\,dx + \int_c^{\infty} f(x)\,dx$$

donde $c$ es cualquier número real (si ambas integrales convergen).

### Convergencia

La integral **converge** si el límite existe y es finito.
La integral **diverge** si el límite no existe o es $\pm\infty$.

### Ejemplos Fundamentales

**Ejemplo 1:** $\displaystyle\int_1^{\infty} \frac{1}{x^2}\,dx$

$$= \lim_{t \to \infty} \int_1^t x^{-2}\,dx = \lim_{t \to \infty} \left[-\frac{1}{x}\right]_1^t = \lim_{t \to \infty} \left(-\frac{1}{t} + 1\right) = 1$$

**Converge** a 1.

**Ejemplo 2:** $\displaystyle\int_1^{\infty} \frac{1}{x}\,dx$

$$= \lim_{t \to \infty} [\ln x]_1^t = \lim_{t \to \infty} \ln t = \infty$$

**Diverge.**

---

## 5.2 Tipo II: Discontinuidades

### Discontinuidad en un Extremo

**En el extremo izquierdo $a$:**
$$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$

**En el extremo derecho $b$:**
$$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$

### Discontinuidad Interior

Si $f$ tiene discontinuidad en $c \in (a,b)$:
$$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$

Ambas deben converger para que la integral original converja.

### Ejemplos

**Ejemplo 1:** $\displaystyle\int_0^1 \frac{1}{\sqrt{x}}\,dx$

Discontinuidad en $x = 0$:
$$= \lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx = \lim_{t \to 0^+} [2\sqrt{x}]_t^1 = 2 - 0 = 2$$

**Converge** a 2.

**Ejemplo 2:** $\displaystyle\int_0^1 \frac{1}{x}\,dx$

$$= \lim_{t \to 0^+} [\ln x]_t^1 = \lim_{t \to 0^+} (0 - \ln t) = \infty$$

**Diverge.**

---

## 5.3 Convergencia y Divergencia

### Condiciones Necesarias

Para que $\int_a^{\infty} f(x)\,dx$ tenga posibilidad de converger:
$$\lim_{x \to \infty} f(x) = 0$$

⚠️ **Nota:** Esta condición es necesaria pero NO [suficiente](../../../glossary.md#suficiente) (ver $1/x$).

### Convergencia Absoluta

$\int_a^{\infty} f(x)\,dx$ **converge absolutamente** si:
$$\int_a^{\infty} |f(x)|\,dx < \infty$$

La [convergencia](../../../glossary.md#convergencia) absoluta implica convergencia.

### Convergencia Condicional

Una integral converge **condicionalmente** si converge pero no absolutamente.

**Ejemplo:** $\int_0^{\infty} \frac{\sin x}{x}\,dx$ converge condicionalmente.

---

## 5.4 Criterios de Comparación

### Comparación Directa

Si $0 \leq f(x) \leq g(x)$ para todo $x \geq a$:

1. Si $\int_a^{\infty} g(x)\,dx$ converge, entonces $\int_a^{\infty} f(x)\,dx$ converge.
2. Si $\int_a^{\infty} f(x)\,dx$ diverge, entonces $\int_a^{\infty} g(x)\,dx$ diverge.

### Comparación por Límite

Si $f(x), g(x) > 0$ para $x$ grande y:
$$\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$$

- Si $0 < L < \infty$: ambas convergen o ambas divergen.
- Si $L = 0$ y $\int g$ converge: $\int f$ converge.
- Si $L = \infty$ y $\int g$ diverge: $\int f$ diverge.

### Aplicación

Para $\int_1^{\infty} \frac{x}{x^3 + 1}\,dx$:

Comparamos con $\frac{1}{x^2}$:
$$\lim_{x \to \infty} \frac{x/(x^3+1)}{1/x^2} = \lim_{x \to \infty} \frac{x^3}{x^3+1} = 1$$

Como $\int_1^{\infty} \frac{1}{x^2}\,dx$ converge, la integral original **converge**.

---

## 5.5 Integrales p

### En el Infinito

$$\int_1^{\infty} \frac{dx}{x^p} = \begin{cases} \dfrac{1}{p-1} & \text{si } p > 1 \\ \infty & \text{si } p \leq 1 \end{cases}$$

### En Cero

$$\int_0^{1} \frac{dx}{x^p} = \begin{cases} \dfrac{1}{1-p} & \text{si } p < 1 \\ \infty & \text{si } p \geq 1 \end{cases}$$

### Regla Práctica

| Comportamiento de $f(x)$ | [Convergencia](../../../glossary.md#convergencia) |
|--------------------------|--------------|
| $f(x) \sim \frac{1}{x^p}$ cuando $x \to \infty$ | Converge si $p > 1$ |
| $f(x) \sim \frac{1}{(x-a)^p}$ cuando $x \to a$ | Converge si $p < 1$ |

---

## Integrales Clásicas

| Integral | Convergencia | Valor |
|----------|--------------|-------|
| $\int_0^{\infty} e^{-x}\,dx$ | Sí | $1$ |
| $\int_0^{\infty} x e^{-x}\,dx$ | Sí | $1$ |
| $\int_0^{\infty} e^{-x^2}\,dx$ | Sí | $\frac{\sqrt{\pi}}{2}$ |
| $\int_0^{\infty} \frac{1}{1+x^2}\,dx$ | Sí | $\frac{\pi}{2}$ |
| $\int_1^{\infty} \frac{\ln x}{x^2}\,dx$ | Sí | $1$ |
| $\int_0^{\infty} \frac{\sin x}{x}\,dx$ | Sí (condicional) | $\frac{\pi}{2}$ |

---

## Advertencias Comunes

### Error del Valor Principal

**Incorrecto:**
$$\int_{-1}^{1} \frac{1}{x}\,dx \neq \lim_{\varepsilon \to 0} \left(\int_{-1}^{-\varepsilon} + \int_{\varepsilon}^{1}\right) = 0$$

El **valor principal de Cauchy** (VP) no es lo mismo que convergencia.

La integral $\int_{-1}^{1} \frac{1}{x}\,dx$ **diverge** porque las dos partes deben converger independientemente.

### Funciones que Oscilan

Para funciones oscilantes como $\sin x$ o $\cos x$:
- $\int_0^{\infty} \sin x\,dx$ **diverge** (oscila)
- $\int_0^{\infty} \frac{\sin x}{x}\,dx$ **converge** (amortiguada)
