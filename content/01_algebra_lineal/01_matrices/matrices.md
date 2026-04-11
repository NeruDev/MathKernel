> 🏠 **Navegación:** ← Volver al Índice Principal

---

# Teoría de Matrices

---

## 1.1 Definición y Notación

### Definición
Una **matriz** es un arreglo rectangular de números organizados en filas y columnas.

$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$

### Notación
- $A_{m \times n}$ o $A \in \mathbb{R}^{m \times n}$: matriz con $m$ filas y $n$ columnas
- $a_{ij}$ o $(A)_{ij}$: elemento en la fila $i$, columna $j$
- Forma compacta: $A = (a_{ij})$

### Igualdad de Matrices
$A = B$ si y solo si tienen las mismas dimensiones y $a_{ij} = b_{ij}$ para todo $i, j$.

---

## 1.2 Tipos de Matrices

### Por su forma

| Tipo | Descripción |
|------|-------------|
| **Fila** | $1 \times n$ |
| **Columna** | $m \times 1$ |
| **Cuadrada** | $n \times n$ |
| **Rectangular** | $m \neq n$ |

### Matrices Cuadradas Especiales

**Matriz diagonal:**
$$D = \begin{pmatrix} d_1 & 0 & \cdots & 0 \\ 0 & d_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & d_n \end{pmatrix} = \text{diag}(d_1, d_2, \ldots, d_n)$$

**Matriz identidad:**
$$I_n = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix}$$

**Matriz triangular superior:**
$$U = \begin{pmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{pmatrix}$$

**Matriz triangular inferior:**
$$L = \begin{pmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0 \\ l_{31} & l_{32} & l_{33} \end{pmatrix}$$

**Matriz nula:** $O$ donde todos los elementos son cero.

---

## 1.3 Operaciones Básicas

### Suma de Matrices

Si $A$ y $B$ son de la misma dimensión $m \times n$:
$$(A + B)_{ij} = a_{ij} + b_{ij}$$

**Propiedades:**
1. **Conmutativa:** $A + B = B + A$
2. **Asociativa:** $(A + B) + C = A + (B + C)$
3. **Elemento neutro:** $A + O = A$
4. **Inverso aditivo:** $A + (-A) = O$

### Multiplicación por Escalar

Si $c \in \mathbb{R}$ y $A$ es una matriz:
$$(cA)_{ij} = c \cdot a_{ij}$$

**Propiedades:**
1. $c(A + B) = cA + cB$
2. $(c + d)A = cA + dA$
3. $c(dA) = (cd)A$
4. $1 \cdot A = A$

---

## 1.4 Multiplicación de Matrices

### Definición

Si $A$ es $m \times n$ y $B$ es $n \times p$, entonces $AB$ es $m \times p$ donde:
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj}$$

**Regla de dimensiones:**
$$(m \times n) \cdot (n \times p) = (m \times p)$$

### Interpretación: Fila por Columna

El elemento $(i,j)$ del producto es el producto punto de la fila $i$ de $A$ con la columna $j$ de $B$.

### Propiedades

1. **Asociativa:** $(AB)C = A(BC)$
2. **Distributiva:** $A(B + C) = AB + AC$ y $(A + B)C = AC + BC$
3. **Escalar:** $c(AB) = (cA)B = A(cB)$
4. **Identidad:** $AI = IA = A$

**⚠️ NO conmutativa:** En general $AB \neq BA$

### Potencias

Para matriz cuadrada $A$:
- $A^0 = I$
- $A^n = A \cdot A \cdots A$ ($n$ veces)
- $A^m A^n = A^{m+n}$
- $(A^m)^n = A^{mn}$

---

## 1.5 Transpuesta

### Definición

La transpuesta de $A_{m \times n}$ es $A^T_{n \times m}$ where:
$$(A^T)_{ij} = a_{ji}$$

Las filas se convierten en columnas y viceversa.

### Ejemplo

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \Rightarrow A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

### Propiedades

1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(cA)^T = cA^T$
4. $(AB)^T = B^T A^T$ (**nota el orden**)

### Matrices Simétricas y Antisimétricas

**Simétrica:** $A = A^T$ (solo matrices cuadradas)

**Antisimétrica:** $A = -A^T$ (diagonal principal es cero)

**Teorema:** Toda matriz cuadrada se puede escribir como:
$$A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T)$$
(parte simétrica + parte antisimétrica)

---

## 1.6 Matriz Inversa

### Definición

Una matriz cuadrada $A$ es **invertible** (o no singular) si existe una matriz $A^{-1}$ tal que:
$$AA^{-1} = A^{-1}A = I$$

### Existencia

$A$ es invertible si y solo si $\det(A) \neq 0$.

### Fórmula para $2 \times 2$

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \Rightarrow A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

### Método General: Gauss-Jordan

Para encontrar $A^{-1}$:
1. Formar la matriz aumentada $(A | I)$
2. Aplicar operaciones elementales de fila
3. Reducir a $(I | A^{-1})$

### Propiedades

1. $(A^{-1})^{-1} = A$
2. $(AB)^{-1} = B^{-1}A^{-1}$ (**nota el orden**)
3. $(A^T)^{-1} = (A^{-1})^T$
4. $(cA)^{-1} = \frac{1}{c}A^{-1}$ para $c \neq 0$
5. $\det(A^{-1}) = \frac{1}{\det(A)}$

### Matriz Ortogonal

$A$ es **ortogonal** si $A^T = A^{-1}$, es decir, $AA^T = A^T A = I$.

Las columnas (y filas) forman un conjunto ortonormal.
