<!--
::METADATA::
type: theory
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría: Transformada de Laplace

---

## 4.1 Definición y Transformadas Básicas

### Definición

La **[transformada de Laplace](../../../glossary.md#transformada-de-laplace)** de una [función](../../../glossary.md#funcion) $f(t)$ definida para $t \geq 0$ es:

$$\boxed{\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} e^{-st}f(t)\,dt}$$

siempre que la [integral impropia](../../../glossary.md#integral-impropia) converja.

### Notación

- $\mathcal{L}\{f(t)\} = F(s)$ ([función](../../../glossary.md#funcion) transformada)
- $\mathcal{L}^{-1}\{F(s)\} = f(t)$ (transformada inversa)
- Minúscula para [dominio](../../../glossary.md#dominio) del tiempo, mayúscula para dominio de $s$

### Condiciones de Existencia

La transformada existe si $f$ es:
1. **Continua a trozos** en $[0, \infty)$
2. **De orden exponencial**: $|f(t)| \leq Me^{ct}$ para constantes $M, c > 0$

### Transformadas Fundamentales

**1. Función constante:**
$$\mathcal{L}\{1\} = \int_0^{\infty} e^{-st}\,dt = \left[-\frac{e^{-st}}{s}\right]_0^{\infty} = \frac{1}{s}, \quad s > 0$$

**2. Potencias:**
$$\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}, \quad n = 0, 1, 2, ...$$

**3. Exponencial:**
$$\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \quad s > a$$

**4. [Seno](../../../glossary.md#seno):**
$$\mathcal{L}\{\sin bt\} = \frac{b}{s^2 + b^2}$$

**5. [Coseno](../../../glossary.md#coseno):**
$$\mathcal{L}\{\cos bt\} = \frac{s}{s^2 + b^2}$$

**6. [Seno](../../../glossary.md#seno) hiperbólico:**
$$\mathcal{L}\{\sinh bt\} = \frac{b}{s^2 - b^2}$$

**7. [Coseno](../../../glossary.md#coseno) hiperbólico:**
$$\mathcal{L}\{\cosh bt\} = \frac{s}{s^2 - b^2}$$

---

## 4.2 Propiedades de la Transformada

### Linealidad

$$\boxed{\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)}$$

> **Ejemplo:** $\mathcal{L}\{5e^{2t} + 3\sin 4t\} = \frac{5}{s-2} + \frac{12}{s^2+16}$

### Primera Traslación (Traslación en $s$)

Si $\mathcal{L}\{f(t)\} = F(s)$, entonces:

$$\boxed{\mathcal{L}\{e^{at}f(t)\} = F(s-a)}$$

> **Ejemplo:** $\mathcal{L}\{e^{3t}\cos 2t\} = \frac{s-3}{(s-3)^2 + 4}$
> 
> (Se reemplaza $s$ por $s-3$ en $\frac{s}{s^2+4}$)

### Segunda Traslación (Traslación en $t$)

Si $\mathcal{L}\{f(t)\} = F(s)$, entonces:

$$\boxed{\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)}$$

donde $u(t-a)$ es la función escalón unitario.

### Transformada de Derivadas

$$\boxed{\mathcal{L}\{f'(t)\} = sF(s) - f(0)}$$

$$\boxed{\mathcal{L}\{f''(t)\} = s^2F(s) - sf(0) - f'(0)}$$

En general:

$$\mathcal{L}\{f^{(n)}(t)\} = s^nF(s) - s^{n-1}f(0) - s^{n-2}f'(0) - \cdots - f^{(n-1)}(0)$$

### Transformada de Integrales

$$\boxed{\mathcal{L}\left\{\int_0^t f(\tau)\,d\tau\right\} = \frac{F(s)}{s}}$$

### Multiplicación por $t$

$$\boxed{\mathcal{L}\{tf(t)\} = -F'(s)}$$

$$\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n F}{ds^n}$$

### División por $t$

$$\boxed{\mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^{\infty} F(u)\,du}$$

(si el [límite](../../../glossary.md#limite) $\lim_{t\to 0^+} \frac{f(t)}{t}$ existe)

### Convolución

La **[convolución](../../../glossary.md#convolucion)** de $f$ y $g$ es:

$$(f * g)(t) = \int_0^t f(\tau)g(t-\tau)\,d\tau$$

**Teorema:**
$$\boxed{\mathcal{L}\{f * g\} = F(s) \cdot G(s)}$$

---

## 4.3 Transformada Inversa

### Definición

$$\mathcal{L}^{-1}\{F(s)\} = f(t)$$

### Linealidad Inversa

$$\mathcal{L}^{-1}\{aF(s) + bG(s)\} = af(t) + bg(t)$$

### Método de Fracciones Parciales

Para invertir funciones racionales $\frac{P(s)}{Q(s)}$:

**Caso 1: Factores lineales distintos**
$$\frac{P(s)}{(s-a)(s-b)} = \frac{A}{s-a} + \frac{B}{s-b}$$

**Caso 2: Factores lineales repetidos**
$$\frac{P(s)}{(s-a)^n} = \frac{A_1}{s-a} + \frac{A_2}{(s-a)^2} + \cdots + \frac{A_n}{(s-a)^n}$$

**Caso 3: Factores cuadráticos irreducibles**
$$\frac{P(s)}{s^2 + bs + c} = \frac{As + B}{s^2 + bs + c}$$

> **Ejemplo:** Encontrar $\mathcal{L}^{-1}\left\{\frac{5s+3}{(s-1)(s+2)}\right\}$
> 
> $\frac{5s+3}{(s-1)(s+2)} = \frac{A}{s-1} + \frac{B}{s+2}$
> 
> $5s + 3 = A(s+2) + B(s-1)$
> 
> $s = 1$: $8 = 3A \Rightarrow A = \frac{8}{3}$
> 
> $s = -2$: $-7 = -3B \Rightarrow B = \frac{7}{3}$
> 
> $\mathcal{L}^{-1} = \frac{8}{3}e^t + \frac{7}{3}e^{-2t}$

### Tabla de Transformadas Inversas Comunes

| $F(s)$ | $f(t) = \mathcal{L}^{-1}\{F\}$ |
|--------|-------------------------------|
| $\frac{1}{s-a}$ | $e^{at}$ |
| $\frac{1}{(s-a)^n}$ | $\frac{t^{n-1}}{(n-1)!}e^{at}$ |
| $\frac{b}{(s-a)^2+b^2}$ | $e^{at}\sin bt$ |
| $\frac{s-a}{(s-a)^2+b^2}$ | $e^{at}\cos bt$ |
| $\frac{1}{s^2+b^2}$ | $\frac{\sin bt}{b}$ |
| $\frac{s}{(s^2+b^2)^2}$ | $\frac{t\sin bt}{2b}$ |

---

## 4.4 Aplicación a Problemas de Valor Inicial

### Método General

Para resolver $ay'' + by' + cy = f(t)$ con $y(0) = y_0$, $y'(0) = y_0'$:

**Paso 1:** Aplicar $\mathcal{L}$ a ambos lados

**Paso 2:** Usar propiedades de [derivadas](../../../glossary.md#derivadas):
$$a[s^2Y - sy_0 - y_0'] + b[sY - y_0] + cY = F(s)$$

**Paso 3:** Despejar $Y(s)$:
$$Y(s) = \frac{F(s) + \text{términos de condiciones iniciales}}{as^2 + bs + c}$$

**Paso 4:** Aplicar $\mathcal{L}^{-1}$ para obtener $y(t)$

> **Ejemplo:** Resolver $y'' + 4y = 0$, $y(0) = 1$, $y'(0) = 2$
> 
> $\mathcal{L}\{y''\} + 4\mathcal{L}\{y\} = 0$
> 
> $s^2Y - s(1) - 2 + 4Y = 0$
> 
> $Y(s^2 + 4) = s + 2$
> 
> $Y = \frac{s}{s^2+4} + \frac{2}{s^2+4}$
> 
> $y(t) = \cos 2t + \sin 2t$

### Función de Transferencia

Para un sistema lineal con entrada $f(t)$ y salida $y(t)$:

$$H(s) = \frac{Y(s)}{F(s)}$$

es la **[función de transferencia](../../../glossary.md#funcion-de-transferencia)** (suponiendo condiciones iniciales nulas).

---

## 4.5 Funciones Especiales

### Función Escalón Unitario (Heaviside)

$$u(t-a) = \begin{cases} 0, & t < a \\ 1, & t \geq a \end{cases}$$

**Transformada:**
$$\mathcal{L}\{u(t-a)\} = \frac{e^{-as}}{s}$$

**Uso:** Representar funciones que "se encienden" en $t = a$

> **Ejemplo:** $f(t) = \begin{cases} 0, & t < 2 \\ t-2, & t \geq 2 \end{cases}$
> 
> $f(t) = (t-2)u(t-2)$
> 
> $\mathcal{L}\{f\} = e^{-2s} \cdot \frac{1}{s^2}$

### Función Delta de Dirac

La "función" delta $\delta(t-a)$ representa un impulso unitario en $t = a$:

$$\int_{-\infty}^{\infty} \delta(t-a)g(t)\,dt = g(a)$$

**Transformada:**
$$\mathcal{L}\{\delta(t-a)\} = e^{-as}$$

$$\mathcal{L}\{\delta(t)\} = 1$$

**Aplicación:** Fuerzas impulsivas, corrientes instantáneas

### Funciones Periódicas

Si $f(t)$ es periódica con período $T$:

$$\mathcal{L}\{f(t)\} = \frac{1}{1 - e^{-sT}}\int_0^T e^{-st}f(t)\,dt$$

> **Ejemplo:** Onda cuadrada con período $2a$:
> $$f(t) = \begin{cases} 1, & 0 < t < a \\ 0, & a < t < 2a \end{cases}$$
> 
> $$\mathcal{L}\{f\} = \frac{1}{s(1+e^{-as})}$$

### Función Rampa

$$r(t) = t \cdot u(t) = \begin{cases} 0, & t < 0 \\ t, & t \geq 0 \end{cases}$$

$$\mathcal{L}\{r(t)\} = \frac{1}{s^2}$$

### Representación de Funciones a Trozos

Cualquier función a trozos puede escribirse usando escalones:

$$f(t) = f_1(t)[u(t-a) - u(t-b)] + f_2(t)[u(t-b) - u(t-c)] + \cdots$$

> **Ejemplo:**
> $$f(t) = \begin{cases} 2, & 0 \leq t < 1 \\ t, & 1 \leq t < 3 \\ 0, & t \geq 3 \end{cases}$$
> 
> $f(t) = 2[1 - u(t-1)] + t[u(t-1) - u(t-3)]$
> 
> $= 2 - 2u(t-1) + tu(t-1) - tu(t-3)$
> 
> $= 2 + (t-2)u(t-1) - tu(t-3)$
