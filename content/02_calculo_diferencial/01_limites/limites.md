<!--
::METADATA::
type: theory
topic_id: cd-01-limites
file_id: CD-01-Teoria-Limites
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría de Límites

## 1.1 Concepto de Límite

### Definición Intuitiva

El **[límite](../../../glossary.md#limite)** de $f(x)$ cuando $x$ tiende a $a$ es $L$ si los valores de $f(x)$ se aproximan arbitrariamente a $L$ cuando $x$ se aproxima a $a$ (sin ser igual a $a$).

$$\lim_{x \to a} f(x) = L$$

**Interpretación:** "Cuando $x$ está muy cerca de $a$, $f(x)$ está muy cerca de $L$."

### Definición Formal (Épsilon-Delta)

$$\lim_{x \to a} f(x) = L$$

si y solo si: para todo $\varepsilon > 0$, existe un $\delta > 0$ [tal que](../../../glossary.md#tal-que):

$$0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon$$

**Significado:**
- $\varepsilon$ representa qué tan cerca queremos que esté $f(x)$ de $L$
- $\delta$ representa qué tan cerca debe estar $x$ de $a$ para lograrlo
- La condición $0 < \lvert x - a \rvert$ excluye el punto $x = a$

---

## 1.2 Límites Laterales

### Límite por la Derecha
$$\lim_{x \to a^+} f(x) = L$$

$x$ se aproxima a $a$ desde valores **mayores** que $a$.

### Límite por la Izquierda
$$\lim_{x \to a^-} f(x) = L$$

$x$ se aproxima a $a$ desde valores **menores** que $a$.

### Teorema de Existencia
$$\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$$

El [límite](../../../glossary.md#limite) existe si y solo si ambos [límites](../../../glossary.md#limites) laterales existen y son iguales.

---

## 1.3 Propiedades de los Límites

Sean $\lim_{x \to a} f(x) = L$ y $\lim_{x \to a} g(x) = M$ donde $L, M \in \mathbb{R}$.

### Álgebra de Límites

| Propiedad | Fórmula |
|-----------|---------|
| Constante | $\lim_{x \to a} c = c$ |
| Identidad | $\lim_{x \to a} x = a$ |
| Suma | $\lim_{x \to a} [f(x) + g(x)] = L + M$ |
| Resta | $\lim_{x \to a} [f(x) - g(x)] = L - M$ |
| Producto | $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$ |
| Constante por [función](../../../glossary.md#funcion) | $\lim_{x \to a} [c \cdot f(x)] = c \cdot L$ |
| Cociente | $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M}$ si $M \neq 0$ |
| Potencia | $\lim_{x \to a} [f(x)]^n = L^n$ |
| Raíz | $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L}$ si $L \geq 0$ para $n$ par |

### Teorema del Emparedado (Sándwich)

Si $g(x) \leq f(x) \leq h(x)$ para todo $x$ cerca de $a$ (excepto posiblemente en $a$), y:
$$\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$$

Entonces: $\lim_{x \to a} f(x) = L$

---

## 1.4 Técnicas de Evaluación

### Sustitución Directa
Si $f$ es continua en $a$:
$$\lim_{x \to a} f(x) = f(a)$$

Funciona para: polinomios, racionales (cuando el denominador ≠ 0), exponenciales, logarítmicas, trigonométricas.

### Formas Indeterminadas
Cuando la [sustitución](../../../glossary.md#sustitucion) directa produce:
- $\frac{0}{0}$ - Requiere técnica algebraica
- $\frac{\infty}{\infty}$ - Requiere simplificación o L'Hôpital
- $0 \cdot \infty$, $\infty - \infty$, $0^0$, $1^\infty$, $\infty^0$ - Requieren manipulación

### Factorización
Para $\frac{0}{0}$, [factorizar](../../../glossary.md#factorizar) y cancelar:

$$\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2} (x+2) = 4$$

### Racionalización
Multiplicar por el conjugado:

$$\lim_{x \to 0} \frac{\sqrt{x+1} - 1}{x} = \lim_{x \to 0} \frac{(\sqrt{x+1}-1)(\sqrt{x+1}+1)}{x(\sqrt{x+1}+1)} = \lim_{x \to 0} \frac{x}{x(\sqrt{x+1}+1)} = \frac{1}{2}$$

### Simplificación de Fracciones Complejas
Multiplicar por el común denominador.

---

## 1.5 Límites Trigonométricos Fundamentales

### Límites Básicos

$$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

$$\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$

$$\lim_{x \to 0} \frac{\tan x}{x} = 1$$

### Consecuencias

$$\lim_{x \to 0} \frac{\sin(ax)}{x} = a$$

$$\lim_{x \to 0} \frac{\sin(ax)}{\sin(bx)} = \frac{a}{b}$$

$$\lim_{x \to 0} \frac{\tan(ax)}{x} = a$$

---

## 1.6 Límites al Infinito

### Definición
$$\lim_{x \to \infty} f(x) = L$$

significa que $f(x)$ se aproxima a $L$ cuando $x$ crece sin límite.

### Límites Básicos

$$\lim_{x \to \infty} \frac{1}{x^n} = 0 \quad (n > 0)$$

$$\lim_{x \to \infty} \frac{1}{x} = 0$$

$$\lim_{x \to \infty} e^{-x} = 0$$

$$\lim_{x \to \infty} \frac{\ln x}{x} = 0$$

### Funciones Racionales
Para $\lim_{x \to \infty} \frac{P(x)}{Q(x)}$ donde $P$ tiene grado $n$ y $Q$ tiene grado $m$:

| Condición | Resultado |
|-----------|-----------|
| $n < m$ | 0 |
| $n = m$ | Cociente de coeficientes principales |
| $n > m$ | $\pm\infty$ (según signos) |

**Técnica:** Dividir numerador y denominador entre la mayor potencia de $x$ en el denominador.

### Asíntotas Horizontales
Si $\lim_{x \to \infty} f(x) = L$ o $\lim_{x \to -\infty} f(x) = L$, entonces $y = L$ es una **[asíntota](../../../glossary.md#asintota) horizontal**.

---

## 1.7 Límites Infinitos

### Definición
$$\lim_{x \to a} f(x) = \infty$$

significa que $f(x)$ crece sin límite cuando $x$ se aproxima a $a$.

$$\lim_{x \to a} f(x) = -\infty$$

significa que $f(x)$ decrece sin límite cuando $x$ se aproxima a $a$.

### Asíntotas Verticales
Si $\lim_{x \to a^+} f(x) = \pm\infty$ o $\lim_{x \to a^-} f(x) = \pm\infty$, entonces $x = a$ es una **[asíntota](../../../glossary.md#asintota) vertical**.

### Reglas de Operación con Infinitos

| Operación | Resultado |
|-----------|-----------|
| $L + \infty$ | $\infty$ |
| $L - \infty$ | $-\infty$ |
| $L \cdot \infty$ | $\pm\infty$ (según signo de $L \neq 0$) |
| $\frac{L}{\infty}$ | $0$ |
| $\frac{L}{0^+}$ | $+\infty$ si $L > 0$, $-\infty$ si $L < 0$ |

**Cuidado:** $\infty - \infty$, $\frac{\infty}{\infty}$, $0 \cdot \infty$ son **indeterminadas**.

---

## 1.8 Continuidad

### Definición
Una [función](../../../glossary.md#funcion) $f$ es **continua en $a$** si:
1. $f(a)$ está definida
2. $\lim_{x \to a} f(x)$ existe
3. $\lim_{x \to a} f(x) = f(a)$

### Tipos de Discontinuidad

| Tipo | Descripción | Remediable |
|------|-------------|------------|
| **Removible** | El límite existe pero $f(a)$ no existe o $f(a) \neq \lim$ | Sí |
| **Salto** | Los límites laterales existen pero son diferentes | No |
| **Infinita** | Al menos un límite lateral es $\pm\infty$ | No |
| **Oscilante** | El límite no existe por oscilación | No |

### Teoremas de Continuidad

1. **Suma, resta, producto de funciones continuas son continuas**
2. **Cociente de continuas es continuo donde el denominador ≠ 0**
3. **[Composición](../../../glossary.md#composicion) de funciones continuas es continua**

### Funciones Continuas en Todo su Dominio
- Polinomios
- Funciones racionales (donde denominador ≠ 0)
- $e^x$, $\ln x$ (en su [dominio](../../../glossary.md#dominio))
- Funciones trigonométricas (en su [dominio](../../../glossary.md#dominio))

---

## 1.9 Teorema del Valor Intermedio

### Enunciado
Si $f$ es continua en $[a, b]$ y $k$ es cualquier valor entre $f(a)$ y $f(b)$, entonces existe al menos un $c \in (a, b)$ [tal que](../../../glossary.md#tal-que) $f(c) = k$.

### Corolario (Existencia de Raíces)
Si $f$ es continua en $[a, b]$ y $f(a)$ y $f(b)$ tienen signos opuestos, entonces existe al menos un $c \in (a, b)$ tal que $f(c) = 0$.

### Aplicación
Para demostrar que una ecuación tiene solución en un intervalo:
1. Definir $f(x) = $ lado izquierdo − lado derecho
2. Verificar que $f$ es continua
3. Encontrar $a, b$ donde $f(a)$ y $f(b)$ tienen signos opuestos
4. Concluir por TVI que existe raíz en $(a, b)$
