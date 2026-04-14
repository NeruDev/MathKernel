<!--
yaml_frontmatter:
  id: 'derivadas'
  content_path: 'content/02_calculo_diferencial/02_derivadas/derivadas.md'
  metadata_path: 'metadata/content/02_calculo_diferencial/02_derivadas/derivadas.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de la Derivada'
  key_headings:
    - 'Teoría de la Derivada'
    - '2.1 Definición de Derivada'
    - 'Definición por Límite'
    - 'Notaciones'
    - 'Interpretación Geométrica'
    - 'Interpretación Física'
    - '2.2 Derivadas de Funciones Elementales'
    - 'Funciones Algebraicas'
  key_concepts:
    - 'Definición por límite'
    - 'Regla de la cadena'
    - 'Derivación implícita'
    - 'Derivación logarítmica'
    - 'Diferenciabilidad'
-->
# Teoría de la Derivada

## 2.1 Definición de Derivada

### Definición por Límite

La **derivada** de $f(x)$ en $x = a$ es:

$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

Equivalentemente:
$$f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$

### Notaciones
| Notación | Se lee |
|----------|--------|
| $f'(x)$ | "f prima de x" |
| $\frac{df}{dx}$ | "derivada de f respecto a x" |
| $\frac{d}{dx}f(x)$ | "derivada de f de x" |
| $Df(x)$ | "D de f de x" |

### Interpretación Geométrica
$f'(a)$ es la **pendiente** de la recta tangente a la gráfica de $f$ en el punto $(a, f(a))$.

### Interpretación Física
Si $s(t)$ es posición, entonces $s'(t)$ es **velocidad instantánea**.
Si $v(t)$ es velocidad, entonces $v'(t) = s''(t)$ es **aceleración**.

---

## 2.2 Derivadas de Funciones Elementales

### Funciones Algebraicas

| Función | Derivada |
|---------|----------|
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\log_a x$ | $\frac{1}{x \ln a}$ |

### Funciones Trigonométricas

| Función | Derivada |
|---------|----------|
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\cot x$ | $-\csc^2 x$ |
| $\sec x$ | $\sec x \tan x$ |
| $\csc x$ | $-\csc x \cot x$ |

### Funciones Trigonométricas Inversas

| Función | Derivada |
|---------|----------|
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ |
| $\text{arccot}\, x$ | $-\frac{1}{1+x^2}$ |
| $\text{arcsec}\, x$ | $\frac{1}{\lvert x \rvert\sqrt{x^2-1}}$ |
| $\text{arccsc}\, x$ | $-\frac{1}{\lvert x \rvert\sqrt{x^2-1}}$ |

---

## 2.3 Reglas de Diferenciación

Sean $f$ y $g$ funciones diferenciables y $c$ constante.

### Regla de la Constante
$$\frac{d}{dx}[c] = 0$$

### Regla del Múltiplo Constante
$$\frac{d}{dx}[cf(x)] = c \cdot f'(x)$$

### Regla de la Suma/Resta
$$\frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$$

### Regla del Producto
$$\frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)$$

### Regla del Cociente
$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$

---

## 2.4 Regla de la Cadena

Si $y = f(g(x))$, entonces:
$$\frac{dy}{dx} = f'(g(x)) \cdot g'(x)$$

### Notación de Leibniz
Si $y = f(u)$ y $u = g(x)$:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### Regla de la Cadena Generalizada
$$\frac{d}{dx}[f(g(x))]^n = n[f(g(x))]^{n-1} \cdot f'(g(x)) \cdot g'(x)$$

### Ejemplos Importantes
- $\frac{d}{dx}[\sin(3x)] = 3\cos(3x)$
- $\frac{d}{dx}[e^{x^2}] = 2xe^{x^2}$
- $\frac{d}{dx}[\ln(x^2+1)] = \frac{2x}{x^2+1}$

---

## 2.5 Derivación Implícita

Cuando $y$ está definida implícitamente por $F(x,y) = 0$:

### Procedimiento
1. Derivar ambos lados respecto a $x$
2. Aplicar regla de la cadena: $\frac{d}{dx}[y^n] = ny^{n-1}\frac{dy}{dx}$
3. Despejar $\frac{dy}{dx}$

### Ejemplo
Para $x^2 + y^2 = 25$:
$$2x + 2y\frac{dy}{dx} = 0$$
$$\frac{dy}{dx} = -\frac{x}{y}$$

---

## 2.6 Derivadas de Orden Superior

### Segunda Derivada
$$f''(x) = \frac{d^2f}{dx^2} = \frac{d}{dx}\left[\frac{df}{dx}\right]$$

### n-ésima Derivada
$$f^{(n)}(x) = \frac{d^nf}{dx^n}$$

### Interpretación
- $f'(x)$: velocidad (tasa de cambio)
- $f''(x)$: aceleración (tasa de cambio de la tasa de cambio)
- $f''(x) > 0$: concavidad hacia arriba
- $f''(x) < 0$: concavidad hacia abajo

---

## 2.7 Derivadas de Funciones Inversas

Si $f$ es invertible y diferenciable:
$$\left(f^{-1}\right)'(y) = \frac{1}{f'(f^{-1}(y))}$$

O equivalentemente, si $y = f^{-1}(x)$:
$$\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}$$

---

## 2.8 Derivación Logarítmica

### Cuándo Usar
- Productos de muchos factores
- Cocientes complicados
- Funciones de la forma $[f(x)]^{g(x)}$

### Procedimiento
1. Tomar logaritmo natural de ambos lados: $\ln y = \ln f(x)$
2. Derivar implícitamente
3. Despejar $\frac{dy}{dx}$

### Ejemplo
Para $y = x^x$:
$$\ln y = x \ln x$$
$$\frac{1}{y}\frac{dy}{dx} = \ln x + x \cdot \frac{1}{x} = \ln x + 1$$
$$\frac{dy}{dx} = x^x(\ln x + 1)$$

---

## Diferenciabilidad y Continuidad

### Teorema
Si $f$ es diferenciable en $a$, entonces $f$ es continua en $a$.

**Contrapositivo:** Si $f$ no es continua en $a$, entonces $f$ no es diferenciable en $a$.

### Cuidado
El recíproco NO es cierto: $f(x) = \lvert x \rvert$ es continua en $x = 0$ pero no diferenciable ahí.

### Puntos de No Diferenciabilidad
- Esquinas (picos)
- Cúspides
- Discontinuidades
- Tangentes verticales

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| e | Numero de Euler | constante | N/A | 2.71828182846 | 12 |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| t | Variable t | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| u | Variable u | variable | N/A | N/A | N/A |
| v | Variable v | variable | N/A | N/A | N/A |
