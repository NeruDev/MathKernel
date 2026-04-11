<!--
HUMANO:
Teoría de teoremas fundamentales del [cálculo diferencial](../../../glossary.md#calculo-diferencial).

IA:
Teoremas, demostraciones y aplicaciones.

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoremas Fundamentales del Cálculo Diferencial

## 4.1 Teorema de Rolle

### Enunciado
Si $f$ es:
1. Continua en $[a, b]$
2. Diferenciable en $(a, b)$
3. $f(a) = f(b)$

Entonces existe al menos un $c \in (a, b)$ [tal que](../../../glossary.md#tal-que) $f'(c) = 0$.

### Interpretación Geométrica
Si una curva suave comienza y termina a la misma altura, en algún punto intermedio la [tangente](../../../glossary.md#tangente) debe ser horizontal.

### Aplicaciones
- Garantizar existencia de puntos críticos
- [Base](../../../glossary.md#base) para el teorema del valor medio

---

## 4.2 Teorema del Valor Medio (TVM)

### Enunciado
Si $f$ es:
1. Continua en $[a, b]$
2. Diferenciable en $(a, b)$

Entonces existe al menos un $c \in (a, b)$ [tal que](../../../glossary.md#tal-que):
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### Interpretación Geométrica
La pendiente de alguna [tangente](../../../glossary.md#tangente) iguala la pendiente de la recta secante entre los extremos.

### Interpretación Física
Si $f(t)$ es posición, la velocidad instantánea en algún momento iguala la velocidad promedio.

### Consecuencias
- Si $f'(x) = 0$ en $(a,b)$, entonces $f$ es constante
- Si $f'(x) = g'(x)$ en $(a,b)$, entonces $f = g + C$
- Si $f'(x) > 0$ en $(a,b)$, entonces $f$ es estrictamente creciente

---

## 4.3 Teorema del Valor Medio Generalizado (Cauchy)

### Enunciado
Si $f$ y $g$ son:
1. Continuas en $[a, b]$
2. Diferenciables en $(a, b)$
3. $g'(x) \neq 0$ en $(a, b)$

Entonces existe $c \in (a, b)$ tal que:
$$\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$$

### Aplicación Principal
Es la [base](../../../glossary.md#base) de la demostración de la Regla de L'Hôpital.

---

## 4.4 Regla de L'Hôpital

### Forma $\frac{0}{0}$
Si $\lim_{x \to a} f(x) = 0$ y $\lim_{x \to a} g(x) = 0$, y existe $\lim_{x \to a} \frac{f'(x)}{g'(x)}$, entonces:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

### Forma $\frac{\infty}{\infty}$
Si $\lim_{x \to a} f(x) = \pm\infty$ y $\lim_{x \to a} g(x) = \pm\infty$, aplica la misma regla.

### Casos Válidos
- $x \to a$ (finito)
- $x \to a^+$ o $x \to a^-$
- $x \to \infty$ o $x \to -\infty$

### Advertencias
1. Verificar que sea [forma indeterminada](../../../glossary.md#forma-indeterminada) antes de aplicar
2. Se puede aplicar repetidamente si es [necesario](../../../glossary.md#necesario)
3. No siempre funciona; el [límite](../../../glossary.md#limite) del cociente de [derivadas](../../../glossary.md#derivadas) puede no existir

---

## 4.5 Otras Formas Indeterminadas

### Forma $0 \cdot \infty$
Reescribir como $\frac{0}{1/\infty}$ o $\frac{\infty}{1/0}$ y aplicar L'Hôpital.

**Ejemplo:** $\lim_{x \to 0^+} x \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x}$

### Forma $\infty - \infty$
Combinar fracciones o racionalizar.

**Ejemplo:** $\lim_{x \to 0} \left(\frac{1}{\sin x} - \frac{1}{x}\right)$

### Formas Exponenciales: $0^0$, $1^\infty$, $\infty^0$

Para $\lim f(x)^{g(x)}$:
1. Sea $y = f(x)^{g(x)}$
2. $\ln y = g(x) \ln f(x)$
3. Calcular $\lim \ln y$
4. Si $\lim \ln y = L$, entonces $\lim y = e^L$

**Ejemplo:** $\lim_{x \to 0^+} x^x$ (forma $0^0$)
$\ln y = x \ln x \to 0$, por lo tanto $y \to e^0 = 1$

---

## 4.6 Teorema de Taylor

### Polinomio de Taylor de Grado $n$
$$P_n(x) = \sum_{k=0}^{n} \frac{f^{(k)}(a)}{k!}(x-a)^k$$

### Teorema de Taylor con Resto de Lagrange
$$f(x) = P_n(x) + R_n(x)$$

donde el resto es:
$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$

para algún $c$ entre $a$ y $x$.

### Aplicaciones
- Aproximación de funciones
- Estimación de errores
- Análisis de comportamiento local

---

## 4.7 Series de Maclaurin

### Definición
Serie de Taylor centrada en $a = 0$:
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

### Series Importantes

**Exponencial:**
$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

**[Seno](../../../glossary.md#seno):**
$$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

**[Coseno](../../../glossary.md#coseno):**
$$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$

**Logaritmo Natural:**
$$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots \quad (-1 < x \leq 1)$$

**Serie Geométrica:**
$$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \cdots \quad (\lvert x \rvert < 1)$$

**Binomial:**
$$(1+x)^k = \sum_{n=0}^{\infty} \binom{k}{n} x^n \quad (\lvert x \rvert < 1)$$
