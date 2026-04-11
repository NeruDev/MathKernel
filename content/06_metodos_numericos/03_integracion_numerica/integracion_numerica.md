# Teoría: Integración Numérica
## 1. Introducción

### 1.1 Motivación

Muchas integrales no tienen antiderivada elemental:
- $\int e^{-x^2} dx$ (función de error)
- $\int \frac{\sin(x)}{x} dx$ (seno integral)
- $\int \sqrt{1 + \cos^2(x)} dx$ (longitud de elipse)

También: datos experimentales solo disponibles en puntos discretos.

### 1.2 Idea General

Aproximar la integral mediante una suma ponderada:
$$\int_a^b f(x)\,dx \approx \sum_{i=0}^{n} w_i f(x_i)$$

donde $x_i$ son los **nodos** y $w_i$ los **pesos**.

---

## 2. Fórmulas de Newton-Cotes

### 2.1 Derivación

Se interpola $f$ con un polinomio en nodos equiespaciados y se integra el polinomio.

Con $h = \frac{b-a}{n}$ y $x_i = a + ih$:
$$\int_a^b f(x)\,dx \approx \int_a^b P_n(x)\,dx$$

### 2.2 Regla del Trapecio (n = 1)

Interpolación lineal entre $(a, f(a))$ y $(b, f(b))$:

$$\int_a^b f(x)\,dx \approx \frac{h}{2}[f(a) + f(b)]$$

**Error:**
$$E = -\frac{h^3}{12}f''(\xi), \quad \xi \in (a, b)$$

**Interpretación geométrica:** Área del trapecio bajo la recta.

### 2.3 Regla de Simpson 1/3 (n = 2)

Interpolación cuadrática por 3 puntos: $a$, $\frac{a+b}{2}$, $b$

$$\int_a^b f(x)\,dx \approx \frac{h}{3}[f(a) + 4f(\frac{a+b}{2}) + f(b)]$$

**Error:**
$$E = -\frac{h^5}{90}f^{(4)}(\xi)$$

**Nota:** Es exacta para polinomios de grado $\leq 3$ (no solo $\leq 2$).

### 2.4 Regla de Simpson 3/8 (n = 3)

Interpolación cúbica por 4 puntos equiespaciados:

$$\int_a^b f(x)\,dx \approx \frac{3h}{8}[f_0 + 3f_1 + 3f_2 + f_3]$$

**Error:** $E = -\frac{3h^5}{80}f^{(4)}(\xi)$

### 2.5 Tabla de Fórmulas Cerradas

| $n$ | Nombre | Coeficientes | Error |
|-----|--------|--------------|-------|
| 1 | Trapecio | $\frac{1}{2}, \frac{1}{2}$ | $O(h^3)$ |
| 2 | Simpson 1/3 | $\frac{1}{3}, \frac{4}{3}, \frac{1}{3}$ | $O(h^5)$ |
| 3 | Simpson 3/8 | $\frac{3}{8}, \frac{9}{8}, \frac{9}{8}, \frac{3}{8}$ | $O(h^5)$ |
| 4 | Boole | $\frac{7}{90}, \frac{32}{90}, \frac{12}{90}, \frac{32}{90}, \frac{7}{90}$ | $O(h^7)$ |

---

## 3. Fórmulas Compuestas

### 3.1 Motivación

Un solo intervalo con $n$ grande puede dar oscilaciones (Runge). Mejor: subdividir $[a,b]$ en muchos subintervalos y aplicar fórmulas simples.

### 3.2 Trapecio Compuesto

Dividir $[a,b]$ en $n$ subintervalos de longitud $h = \frac{b-a}{n}$:

$$\int_a^b f(x)\,dx \approx \frac{h}{2}\left[f(a) + 2\sum_{i=1}^{n-1} f(x_i) + f(b)\right]$$

**Error global:**
$$E_T = -\frac{(b-a)h^2}{12}f''(\xi) = O(h^2)$$

### 3.3 Simpson Compuesto

Requiere $n$ par. Aplicar Simpson 1/3 en cada par de subintervalos:

$$\int_a^b f(x)\,dx \approx \frac{h}{3}\left[f(a) + 4\sum_{i \text{ impar}} f(x_i) + 2\sum_{i \text{ par}} f(x_i) + f(b)\right]$$

**Error global:**
$$E_S = -\frac{(b-a)h^4}{180}f^{(4)}(\xi) = O(h^4)$$

---

## 4. Integración de Romberg

### 4.1 Idea

Usar extrapolación de Richardson para mejorar la precisión del trapecio compuesto.

### 4.2 Desarrollo

Sea $T(h)$ el resultado del trapecio compuesto con paso $h$. Se puede demostrar:
$$I = T(h) + c_1 h^2 + c_2 h^4 + c_3 h^6 + ...$$

Eliminando términos de bajo orden:
$$I = \frac{4T(h/2) - T(h)}{3} + O(h^4)$$

### 4.3 Esquema de Romberg

$$R_{k,0} = T(h_k), \quad h_k = \frac{b-a}{2^k}$$

$$R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}$$

| $k$ | $R_{k,0}$ (Trapecio) | $R_{k,1}$ (Simpson) | $R_{k,2}$ (Boole) | ... |
|-----|----------------------|---------------------|-------------------|-----|
| 0 | $R_{0,0}$ | | | |
| 1 | $R_{1,0}$ | $R_{1,1}$ | | |
| 2 | $R_{2,0}$ | $R_{2,1}$ | $R_{2,2}$ | |
| ... | ... | ... | ... | |

---

## 5. Cuadratura Gaussiana

### 5.1 Idea Principal

En Newton-Cotes los nodos son equiespaciados (fijos). ¿Qué pasa si también optimizamos las posiciones de los nodos?

Con $n$ nodos y $n$ pesos, tenemos $2n$ parámetros → podemos hacer la fórmula exacta para polinomios de grado $\leq 2n-1$.

### 5.2 Gauss-Legendre

Para $\int_{-1}^{1} f(x)\,dx$:

$$\int_{-1}^{1} f(x)\,dx \approx \sum_{i=1}^{n} w_i f(x_i)$$

Los nodos $x_i$ son las raíces del polinomio de Legendre $P_n(x)$.

**Tabla de nodos y pesos:**

| $n$ | Nodos | Pesos |
|-----|-------|-------|
| 1 | $x_1 = 0$ | $w_1 = 2$ |
| 2 | $x_{1,2} = \pm\frac{1}{\sqrt{3}} \approx \pm 0.5774$ | $w_1 = w_2 = 1$ |
| 3 | $x_1 = 0$, $x_{2,3} = \pm\sqrt{\frac{3}{5}} \approx \pm 0.7746$ | $w_1 = \frac{8}{9}$, $w_{2,3} = \frac{5}{9}$ |

### 5.3 Cambio de Variable

Para $\int_a^b f(x)\,dx$, usar $x = \frac{b-a}{2}t + \frac{a+b}{2}$:

$$\int_a^b f(x)\,dx = \frac{b-a}{2}\int_{-1}^{1} f\left(\frac{b-a}{2}t + \frac{a+b}{2}\right)dt$$

### 5.4 Error

$$E = \frac{2^{2n+1}(n!)^4}{(2n+1)[(2n)!]^3}f^{(2n)}(\xi)$$

---

## 6. Análisis del Error

### 6.1 Comparación de Órdenes

| Método | Orden del Error | Fórmula |
|--------|----------------|----------|
| Rectángulos | $O(h)$ | $E = \frac{h}{2}(b-a)f'(\xi)$ |
| Trapecios | $O(h^2)$ | $E = -\frac{h^2}{12}(b-a)f''(\xi)$ |
| Simpson | $O(h^4)$ | $E = -\frac{h^4}{180}(b-a)f^{(4)}(\xi)$ |
| Gauss-Legendre ($n$) | $O(h^{2n})$ | Ver fórmula específica |

---

## 7. Integrales Oscilatorias

### 7.1 Problema
Para $\int_a^b f(x)\sin(\omega x)\,dx$ con $\omega$ grande, los métodos clásicos necesitan muchos puntos.

### 7.2 Solución
- Cuadratura de Filon
- O integrar por partes y aplicar métodos estándar

---

## 8. Aplicaciones

1. **Física:** Trabajo, centro de masa, momentos de inercia
2. **Probabilidad:** Funciones de distribución
3. **Ingeniería:** Análisis de señales, procesamiento de datos
4. **Economía:** Valor presente, excedente del consumidor
