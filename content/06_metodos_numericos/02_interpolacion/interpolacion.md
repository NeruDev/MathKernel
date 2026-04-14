<!--
yaml_frontmatter:
  id: 'interpolacion'
  content_path: 'content/06_metodos_numericos/02_interpolacion/interpolacion.md'
  metadata_path: 'metadata/content/06_metodos_numericos/02_interpolacion/interpolacion.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de Interpolación'
  key_headings:
    - 'Teoría: Interpolación'
    - '1. Introducción'
    - '1.1 El Problema de Interpolación'
    - '1.2 Teorema de Existencia y Unicidad'
    - '2. Interpolación de Lagrange'
    - '2.1 Polinomios Base de Lagrange'
    - '2.2 Polinomio Interpolante de Lagrange'
    - '2.3 Ejemplo: 3 Puntos'
  key_concepts:
    - 'Interpolación de Lagrange'
    - 'Diferencias divididas'
    - 'Splines cúbicos'
    - 'Error de interpolación'
    - 'Nodos de Chebyshev'
-->
# Teoría: Interpolación
## 1. Introducción

### 1.1 El Problema de Interpolación

Dados $n+1$ puntos $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$ con $x_i$ distintos, encontrar una función $P(x)$ tal que:
$$P(x_i) = y_i \quad \text{para } i = 0, 1, ..., n$$

### 1.2 Teorema de Existencia y Unicidad

> **Teorema:** Dados $n+1$ puntos con abscisas distintas, existe un único polinomio de grado menor o igual a $n$ que los interpola.

**Demostración de unicidad:** Si $P$ y $Q$ son dos polinomios de grado $\leq n$ que interpolan los mismos puntos, entonces $P - Q$ tiene grado $\leq n$ y se anula en $n+1$ puntos, por lo que $P - Q = 0$.

---

## 2. Interpolación de Lagrange

### 2.1 Polinomios Base de Lagrange

$$L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

**Propiedad fundamental:**
$$L_i(x_j) = \delta_{ij} = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}$$

### 2.2 Polinomio Interpolante de Lagrange

$$P_n(x) = \sum_{i=0}^{n} y_i L_i(x)$$

**Verificación:** $P_n(x_k) = \sum_{i=0}^{n} y_i L_i(x_k) = y_k \cdot 1 = y_k$ ✓

### 2.3 Ejemplo: 3 Puntos

Dados $(0, 1)$, $(1, 3)$, $(2, 2)$:

$$L_0(x) = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{(x-1)(x-2)}{2}$$

$$L_1(x) = \frac{(x-0)(x-2)}{(1-0)(1-2)} = \frac{x(x-2)}{-1}$$

$$L_2(x) = \frac{(x-0)(x-1)}{(2-0)(2-1)} = \frac{x(x-1)}{2}$$

$$P_2(x) = 1 \cdot L_0 + 3 \cdot L_1 + 2 \cdot L_2 = -\frac{3}{2}x^2 + \frac{7}{2}x + 1$$

---

## 3. Diferencias Divididas

### 3.1 Definición Recursiva

**Diferencia dividida de orden 0:**
$$f[x_i] = f(x_i) = y_i$$

**Diferencia dividida de orden 1:**
$$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$$

**Diferencia dividida de orden $k$:**
$$f[x_i, x_{i+1}, ..., x_{i+k}] = \frac{f[x_{i+1}, ..., x_{i+k}] - f[x_i, ..., x_{i+k-1}]}{x_{i+k} - x_i}$$

### 3.2 Tabla de Diferencias Divididas

| $x_i$ | $f[x_i]$ | $f[x_i, x_{i+1}]$ | $f[x_i, x_{i+1}, x_{i+2}]$ | ... |
|-------|----------|-------------------|----------------------------|-----|
| $x_0$ | $f[x_0]$ | | | |
| $x_1$ | $f[x_1]$ | $f[x_0, x_1]$ | | |
| $x_2$ | $f[x_2]$ | $f[x_1, x_2]$ | $f[x_0, x_1, x_2]$ | |
| ... | ... | ... | ... | |

### 3.3 Propiedades

1. **Simetría:** $f[x_0, x_1, ..., x_n]$ es invariante ante permutaciones de los argumentos.

2. **Relación con derivadas:** Si $f \in C^n$, entonces:
$$f[x_0, x_1, ..., x_n] = \frac{f^{(n)}(\xi)}{n!}$$ para algún $\xi$ en el intervalo.

---

## 4. Forma de Newton del Polinomio Interpolante

### 4.1 Fórmula General

$$P_n(x) = f[x_0] + fx_0, x_1(x - x_1) + ...$$

$$= \sum_{k=0}^{n} f[x_0, ..., x_k] \prod_{j=0}^{k-1}(x - x_j)$$

### 4.2 Ventaja Principal

Agregar un nuevo punto $(x_{n+1}, y_{n+1})$ solo requiere calcular $f[x_0, ..., x_{n+1}]$ y agregar un término:
$$P_{n+1}(x) = P_n(x) + f[x_0, ..., x_{n+1}]\prod_{j=0}^{n}(x - x_j)$$

---

## 5. Datos Equiespaciados

### 5.1 Diferencias Finitas

Si $x_i = x_0 + ih$ (equiespaciado):

**Diferencia progresiva:**
$$\Delta f_i = f_{i+1} - f_i$$
$$\Delta^k f_i = \Delta^{k-1} f_{i+1} - \Delta^{k-1} f_i$$

**Diferencia regresiva:**
$$\nabla f_i = f_i - f_{i-1}$$

### 5.2 Fórmula de Newton Progresiva

Con $s = \frac{x - x_0}{h}$:

$$P_n(x) = \sum_{k=0}^{n} \binom{s}{k} \Delta^k f_0$$

donde $\binom{s}{k} = \frac{s(s-1)(s-2)...(s-k+1)}{k!}$

### 5.3 Fórmula de Newton Regresiva

Con $s = \frac{x - x_n}{h}$:

$$P_n(x) = \sum_{k=0}^{n} \binom{-s}{k}(-1)^k \nabla^k f_n$$

---

## 6. Error de Interpolación

### 6.1 Teorema del Error

Si $f \in C^{n+1}[a, b]$ y $P_n$ es el polinomio interpolante en $x_0, ..., x_n \in [a, b]$, entonces:

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)$$

para algún $\xi_x$ entre $\min\{x, x_0, ..., x_n\}$ y $\max\{x, x_0, ..., x_n\}$.

### 6.2 Cota del Error

$$|f(x) - P_n(x)| \leq \frac{M_{n+1}}{(n+1)!}\left|\prod_{i=0}^{n}(x - x_i)\right|$$

donde $M_{n+1} = \max_{a \leq x \leq b} |f^{(n+1)}(x)|$

### 6.3 Fenómeno de Runge

La función $f(x) = \frac{1}{1+25x^2}$ interpolada con puntos equiespaciados en $[-1, 1]$ muestra oscilaciones crecientes cerca de los extremos cuando $n$ aumenta.

**Solución:** Usar nodos de Chebyshev:
$$x_k = \cos\left(\frac{2k+1}{2(n+1)}\pi\right), \quad k = 0, 1, ..., n$$

---

## 7. Splines Cúbicos

### 7.1 Definición

Un spline cúbico $S(x)$ en $[a, b]$ con nodos $a = x_0 < x_1 < ... < x_n = b$ es una función que:

1. En cada subintervalo $[x_i, x_{i+1}]$, $S(x)$ es un polinomio de grado $\leq 3$
2. $S$, $S'$ y $S''$ son continuas en $[a, b]$
3. $S(x_i) = y_i$ para todo $i$

### 7.2 Construcción

En cada intervalo: $S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$

**Condiciones:**
- Interpolación: $4n$ incógnitas (coeficientes), $n$ condiciones
- Continuidad de $S$: $n-1$ condiciones
- Continuidad de $S'$: $n-1$ condiciones
- Continuidad de $S''$: $n-1$ condiciones

Total: $n + 3(n-1) = 4n - 3$ condiciones → Faltan 2

### 7.3 Condiciones de Frontera

**Spline natural:** $S''(x_0) = S''(x_n) = 0$

**Spline sujeto:** $S'(x_0) = f'_0$, $S'(x_n) = f'_n$

**Spline periódico:** $S'(x_0) = S'(x_n)$, $S''(x_0) = S''(x_n)$

### 7.4 Sistema de Ecuaciones

El cálculo de los $c_i = \frac{S''(x_i)}{2}$ lleva a un sistema tridiagonal.

---

## 8. Interpolación de Hermite

### 8.1 Planteamiento

Dados los puntos y sus derivadas $(x_i, y_i, y'_i)$ para $i = 0, ..., n$, encontrar un polinomio $H(x)$ de grado $\leq 2n+1$ tal que:
$$H(x_i) = y_i, \quad H'(x_i) = y'_i$$

### 8.2 Forma de Newton para Hermite

Usar diferencias divididas "ampliadas" donde puntos repetidos implican derivadas:
$$f[x_i, x_i] = f'(x_i)$$

---

## 9. Aplicaciones

1. **Gráficos por computadora:** Curvas suaves (Bézier, B-splines)
2. **Procesamiento de señales:** Reconstrucción de señales
3. **Tablas numéricas:** Estimación entre valores tabulados
4. **Integración y diferenciación numérica:** Base para otros métodos

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| π | Constante pi | constante | rad | 3.14159265359 | 12 |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| k | Variable k | variable | N/A | N/A | N/A |
