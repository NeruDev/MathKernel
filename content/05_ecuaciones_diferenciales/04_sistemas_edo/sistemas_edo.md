<!--
::METADATA::
type: theory
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría: Sistemas de Ecuaciones Diferenciales Ordinarias

---

## 3.1 Forma Matricial

### Sistema de EDO Lineales

Un sistema de $n$ [ecuaciones diferenciales](../../../glossary.md#ecuaciones-diferenciales) lineales de primer [orden](../../../glossary.md#orden):

$$\begin{cases}
x_1' = a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n + f_1(t) \\
x_2' = a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n + f_2(t) \\
\vdots \\
x_n' = a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n + f_n(t)
\end{cases}$$

### Notación Matricial

$$\boxed{\mathbf{X}' = A\mathbf{X} + \mathbf{F}(t)}$$

donde:
- $\mathbf{X} = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix}$ es el [vector](../../../glossary.md#vector) de incógnitas
- $A = (a_{ij})$ es la [matriz](../../../glossary.md#matriz) de coeficientes $n \times n$
- $\mathbf{F}(t) = \begin{pmatrix} f_1(t) \\ f_2(t) \\ \vdots \\ f_n(t) \end{pmatrix}$ es el [vector](../../../glossary.md#vector) de términos forzantes

### Sistema Homogéneo

Cuando $\mathbf{F}(t) = \mathbf{0}$:

$$\mathbf{X}' = A\mathbf{X}$$

### Conversión de EDO de Orden Superior

Una [EDO](../../../glossary.md#edo) de [orden](../../../glossary.md#orden) $n$:
$$y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_1y' + a_0y = f(t)$$

Se convierte en sistema con: $x_1 = y$, $x_2 = y'$, ..., $x_n = y^{(n-1)}$

> **Ejemplo:** $y'' + 3y' + 2y = 0$
> 
> Sea $x_1 = y$, $x_2 = y'$
> 
> $x_1' = x_2$
> 
> $x_2' = y'' = -3y' - 2y = -2x_1 - 3x_2$
> 
> $$\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -2 & -3 \end{pmatrix}\mathbf{X}$$

---

## 3.2 Método de Valores Propios (Eigenvalores Reales Distintos)

### Idea Central

Buscamos soluciones de la forma:

$$\mathbf{X} = e^{\lambda t}\mathbf{v}$$

donde $\lambda$ es un escalar y $\mathbf{v}$ un vector constante.

### Condición

Sustituyendo en $\mathbf{X}' = A\mathbf{X}$:

$$\lambda e^{\lambda t}\mathbf{v} = Ae^{\lambda t}\mathbf{v}$$

$$A\mathbf{v} = \lambda\mathbf{v}$$

Es decir, $\lambda$ debe ser **valor propio** y $\mathbf{v}$ **vector propio** de $A$.

### Solución General (Caso Reales Distintos)

Si $A$ tiene eigenvalores $\lambda_1, \lambda_2, ..., \lambda_n$ distintos con eigenvectores $\mathbf{v}_1, \mathbf{v}_2, ..., \mathbf{v}_n$:

$$\boxed{\mathbf{X} = C_1 e^{\lambda_1 t}\mathbf{v}_1 + C_2 e^{\lambda_2 t}\mathbf{v}_2 + \cdots + C_n e^{\lambda_n t}\mathbf{v}_n}$$

> **Ejemplo:** Resolver $\mathbf{X}' = \begin{pmatrix} 1 & 1 \\ 4 & 1 \end{pmatrix}\mathbf{X}$
> 
> **Ecuación característica:**
> $$\det(A - \lambda I) = \begin{vmatrix} 1-\lambda & 1 \\ 4 & 1-\lambda \end{vmatrix} = (1-\lambda)^2 - 4 = 0$$
> 
> $\lambda^2 - 2\lambda - 3 = 0 \Rightarrow \lambda_1 = 3, \lambda_2 = -1$
> 
> **Eigenvector para $\lambda_1 = 3$:**
> $(A - 3I)\mathbf{v} = 0$: $\begin{pmatrix} -2 & 1 \\ 4 & -2 \end{pmatrix}\mathbf{v} = 0$
> 
> $-2v_1 + v_2 = 0 \Rightarrow \mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$
> 
> **Eigenvector para $\lambda_2 = -1$:**
> $(A + I)\mathbf{v} = 0$: $\begin{pmatrix} 2 & 1 \\ 4 & 2 \end{pmatrix}\mathbf{v} = 0$
> 
> $2v_1 + v_2 = 0 \Rightarrow \mathbf{v}_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$
> 
> **Solución:**
> $$\mathbf{X} = C_1 e^{3t}\begin{pmatrix} 1 \\ 2 \end{pmatrix} + C_2 e^{-t}\begin{pmatrix} 1 \\ -2 \end{pmatrix}$$

---

## 3.3 Valores Propios Complejos

### Eigenvalores Complejos Conjugados

Si $\lambda = \alpha + \beta i$ es eigenvalor con eigenvector $\mathbf{v} = \mathbf{a} + i\mathbf{b}$, entonces $\bar{\lambda} = \alpha - \beta i$ también es eigenvalor.

### Solución Compleja

$$\mathbf{X} = e^{(\alpha + \beta i)t}(\mathbf{a} + i\mathbf{b})$$

### Soluciones Reales

Usando la fórmula de Euler $e^{i\theta} = \cos\theta + i\sin\theta$:

$$\boxed{\mathbf{X}_1 = e^{\alpha t}(\mathbf{a}\cos\beta t - \mathbf{b}\sin\beta t)}$$

$$\boxed{\mathbf{X}_2 = e^{\alpha t}(\mathbf{a}\sin\beta t + \mathbf{b}\cos\beta t)}$$

[Solución general](../../../glossary.md#solucion-general):

$$\mathbf{X} = C_1\mathbf{X}_1 + C_2\mathbf{X}_2$$

> **Ejemplo:** $\mathbf{X}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}\mathbf{X}$
> 
> $\det(A - \lambda I) = \lambda^2 + 1 = 0 \Rightarrow \lambda = \pm i$
> 
> Para $\lambda = i$: $(A - iI)\mathbf{v} = 0$
> 
> $\begin{pmatrix} -i & 1 \\ -1 & -i \end{pmatrix}\mathbf{v} = 0$
> 
> $-iv_1 + v_2 = 0 \Rightarrow v_2 = iv_1$
> 
> $\mathbf{v} = \begin{pmatrix} 1 \\ i \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} + i\begin{pmatrix} 0 \\ 1 \end{pmatrix}$
> 
> $\mathbf{a} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$
> 
> $\alpha = 0$, $\beta = 1$
> 
> **Solución:**
> $$\mathbf{X} = C_1\begin{pmatrix} \cos t \\ -\sin t \end{pmatrix} + C_2\begin{pmatrix} \sin t \\ \cos t \end{pmatrix}$$

---

## 3.4 Valores Propios Repetidos

### Eigenvalor Doble con Un Solo Eigenvector

Si $\lambda$ es eigenvalor de multiplicidad 2 pero solo hay un eigenvector linealmente independiente $\mathbf{v}$, necesitamos un **vector generalizado** $\mathbf{w}$ que satisface:

$$(A - \lambda I)\mathbf{w} = \mathbf{v}$$

### Solución General

$$\boxed{\mathbf{X} = C_1 e^{\lambda t}\mathbf{v} + C_2 e^{\lambda t}(t\mathbf{v} + \mathbf{w})}$$

> **Ejemplo:** $\mathbf{X}' = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}\mathbf{X}$
> 
> $\det(A - \lambda I) = (3-\lambda)(1-\lambda) + 1 = \lambda^2 - 4\lambda + 4 = 0$
> 
> $(\lambda - 2)^2 = 0 \Rightarrow \lambda = 2$ (doble)
> 
> **Eigenvector:**
> $(A - 2I)\mathbf{v} = 0$: $\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\mathbf{v} = 0$
> 
> $v_1 + v_2 = 0 \Rightarrow \mathbf{v} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
> 
> **Vector generalizado:**
> $(A - 2I)\mathbf{w} = \mathbf{v}$: $\begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}\mathbf{w} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$
> 
> $w_1 + w_2 = 1 \Rightarrow \mathbf{w} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$
> 
> **Solución:**
> $$\mathbf{X} = C_1 e^{2t}\begin{pmatrix} 1 \\ -1 \end{pmatrix} + C_2 e^{2t}\left[t\begin{pmatrix} 1 \\ -1 \end{pmatrix} + \begin{pmatrix} 1 \\ 0 \end{pmatrix}\right]$$

---

## 3.5 Retratos de Fase

### Punto de Equilibrio

El **punto de equilibrio** del sistema $\mathbf{X}' = A\mathbf{X}$ es $\mathbf{X} = \mathbf{0}$ (cuando $\det A \neq 0$).

### Clasificación (Sistema 2×2)

Para [matriz](../../../glossary.md#matriz) $A$ con eigenvalores $\lambda_1, \lambda_2$:

| Eigenvalores | Tipo | Descripción |
|--------------|------|-------------|
| $\lambda_1 < \lambda_2 < 0$ | **Nodo estable** | Trayectorias convergen al origen |
| $0 < \lambda_1 < \lambda_2$ | **Nodo inestable** | Trayectorias divergen del origen |
| $\lambda_1 < 0 < \lambda_2$ | **Punto silla** | Hiperbólico, inestable |
| $\alpha \pm \beta i$, $\alpha < 0$ | **Espiral estable** | Espiral hacia el origen |
| $\alpha \pm \beta i$, $\alpha > 0$ | **Espiral inestable** | Espiral alejándose |
| $\pm \beta i$ | **Centro** | Órbitas cerradas (elipses) |
| $\lambda_1 = \lambda_2 < 0$, 2 eigenvect. | **Nodo estrella estable** | Líneas rectas al origen |
| $\lambda_1 = \lambda_2 < 0$, 1 eigenvect. | **Nodo degenerado estable** | Tangente a una dirección |

### Estabilidad

- **Asintóticamente estable:** $\mathbf{X}(t) \to \mathbf{0}$ cuando $t \to \infty$ (todos $\text{Re}(\lambda) < 0$)
- **Estable:** Trayectorias permanecen cerca ($\text{Re}(\lambda) \leq 0$)
- **Inestable:** Algún $\text{Re}(\lambda) > 0$

### Traza y Determinante

Para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:

- $\tau = \text{tr}(A) = a + d = \lambda_1 + \lambda_2$
- $\Delta = \det(A) = ad - bc = \lambda_1 \lambda_2$
- Discriminante: $\tau^2 - 4\Delta$

| Región | Tipo |
|--------|------|
| $\Delta < 0$ | Silla |
| $\Delta > 0$, $\tau^2 > 4\Delta$, $\tau < 0$ | Nodo estable |
| $\Delta > 0$, $\tau^2 > 4\Delta$, $\tau > 0$ | Nodo inestable |
| $\Delta > 0$, $\tau^2 < 4\Delta$, $\tau < 0$ | Espiral estable |
| $\Delta > 0$, $\tau^2 < 4\Delta$, $\tau > 0$ | Espiral inestable |
| $\Delta > 0$, $\tau = 0$ | Centro |

---

## 3.6 Matriz Exponencial

### Definición

$$e^{At} = I + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \cdots = \sum_{k=0}^{\infty} \frac{(At)^k}{k!}$$

### Solución del PVI

Para $\mathbf{X}' = A\mathbf{X}$ con $\mathbf{X}(0) = \mathbf{X}_0$:

$$\boxed{\mathbf{X}(t) = e^{At}\mathbf{X}_0}$$

### Cálculo mediante Diagonalización

Si $A = PDP^{-1}$ donde $D = \text{diag}(\lambda_1, ..., \lambda_n)$:

$$e^{At} = Pe^{Dt}P^{-1}$$

donde $e^{Dt} = \text{diag}(e^{\lambda_1 t}, ..., e^{\lambda_n t})$

### Propiedades

1. $e^{0} = I$
2. $\frac{d}{dt}e^{At} = Ae^{At}$
3. $e^{A(t+s)} = e^{At}e^{As}$
4. $(e^{At})^{-1} = e^{-At}$

> **Ejemplo:** Calcular $e^{At}$ para $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$
> 
> Eigenvalores: $\lambda_1 = 1$, $\lambda_2 = 2$
> 
> Eigenvectores: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
> 
> $P = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, $P^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$
> 
> $$e^{At} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} e^t & 0 \\ 0 & e^{2t} \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$$
> 
> $$e^{At} = \begin{pmatrix} e^t & e^{2t} - e^t \\ 0 & e^{2t} \end{pmatrix}$$
