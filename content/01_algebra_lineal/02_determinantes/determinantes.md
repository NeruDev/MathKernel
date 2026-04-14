<!--
yaml_frontmatter:
  id: 'determinantes'
  content_path: 'content/01_algebra_lineal/02_determinantes/determinantes.md'
  metadata_path: 'metadata/content/01_algebra_lineal/02_determinantes/determinantes.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de Determinantes'
  key_headings:
    - 'Teoría de Determinantes'
    - '2.1 Determinante de Matrices 2×2 y 3×3'
    - 'Determinante $2 \times 2$'
    - 'Determinante $3 \times 3$ (Regla de Sarrus)'
    - 'Interpretación Geométrica'
    - '2.2 Propiedades de Determinantes'
    - 'Propiedades Fundamentales'
    - 'Efecto de Operaciones Elementales de Fila'
  key_concepts:
    - 'Regla de Sarrus'
    - 'Propiedades de determinantes'
    - 'Cofactores'
    - 'Método de Laplace'
    - 'Regla de Cramer'
-->
# Teoría de Determinantes
## 2.1 Determinante de Matrices 2×2 y 3×3

### Determinante $2 \times 2$

$$\det(A) = \det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

**Notación alternativa:** $|A|$ o $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$

### Determinante $3 \times 3$ (Regla de Sarrus)

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$

**Fórmula:**
$$= a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}$$
$$- a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}$$

**Nemotécnica:** Diagonales principales (+) menos diagonales secundarias (−).

### Interpretación Geométrica

- **$2 \times 2$:** Área del paralelogramo formado por los vectores fila/columna
- **$3 \times 3$:** Volumen del paralelepípedo formado por los vectores

---

## 2.2 Propiedades de Determinantes

### Propiedades Fundamentales

1. $\det(I_n) = 1$

2. $\det(A^T) = \det(A)$

3. $\det(AB) = \det(A) \cdot \det(B)$

4. Si $A$ es invertible: $\det(A^{-1}) = \frac{1}{\det(A)}$

5. $\det(cA) = c^n \det(A)$ para matriz $n \times n$

### Efecto de Operaciones Elementales de Fila

| Operación | Efecto en $\det$ |
|-----------|-----------------|
| Intercambiar dos filas | Cambia de signo |
| Multiplicar fila por $k$ | Multiplica det por $k$ |
| Sumar múltiplo de fila a otra | No cambia |

### Propiedades Especiales

- Fila o columna de ceros $\Rightarrow \det = 0$
- Dos filas o columnas iguales $\Rightarrow \det = 0$
- Dos filas o columnas proporcionales $\Rightarrow \det = 0$
- Matriz triangular $\Rightarrow \det =$ producto de diagonal

$$\det\begin{pmatrix} a_{11} & * & * \\ 0 & a_{22} & * \\ 0 & 0 & a_{33} \end{pmatrix} = a_{11} \cdot a_{22} \cdot a_{33}$$

---

## 2.3 Cofactores y Menores

### Menor

El **menor** $M_{ij}$ es el determinante de la submatriz obtenida al eliminar la fila $i$ y columna $j$.

**Ejemplo:** Para $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$

$$M_{11} = \det\begin{pmatrix} 5 & 6 \\ 8 & 9 \end{pmatrix} = 45 - 48 = -3$$

### Cofactor

El **cofactor** $C_{ij}$ incluye el signo:
$$C_{ij} = (-1)^{i+j} M_{ij}$$

**Patrón de signos:**
$$\begin{pmatrix} + & - & + & \cdots \\ - & + & - & \cdots \\ + & - & + & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

---

## 2.4 Expansión por Cofactores (Método de Laplace)

### Expansión por Fila

$$\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij} = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in}$$

### Expansión por Columna

$$\det(A) = \sum_{i=1}^{n} a_{ij} C_{ij} = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj}$$

### Estrategia

Elegir la fila o columna con más ceros para minimizar cálculos.

**Ejemplo:** $A = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \\ 0 & 4 & 5 \end{pmatrix}$

Expandiendo por primera fila:
$$\det(A) = 1 \cdot C_{11} + 0 \cdot C_{12} + 2 \cdot C_{13}$$

$$= 1 \cdot \begin{vmatrix} 1 & 0 \\ 4 & 5 \end{vmatrix} + 2 \cdot (-1)^{1+3}\begin{vmatrix} 3 & 1 \\ 0 & 4 \end{vmatrix}$$

$$= 1(5) + 2(12) = 29$$

---

## 2.5 Matriz Adjunta

### Definición

La **matriz de cofactores** es $C = (C_{ij})$.

La **matriz adjunta** (o adjugada) es la transpuesta de la matriz de cofactores:
$$\text{adj}(A) = C^T$$

### Fórmula para la Inversa

$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

**Ejemplo:** Para $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$

Cofactores:
- $C_{11} = 4$, $C_{12} = -3$
- $C_{21} = -2$, $C_{22} = 1$

$$\text{adj}(A) = \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix}$$

$$A^{-1} = \frac{1}{-2}\begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ 3/2 & -1/2 \end{pmatrix}$$

---

## 2.6 Regla de Cramer

### Teorema

Para el sistema $Ax = b$ donde $A$ es $n \times n$ con $\det(A) \neq 0$:

$$x_i = \frac{\det(A_i)}{\det(A)}$$

donde $A_i$ es la matriz $A$ con la columna $i$ reemplazada por el vector $b$.

### Ejemplo

Resolver:
$$\begin{cases} 2x + y = 5 \\ 3x + 4y = 6 \end{cases}$$

$$A = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 5 \\ 6 \end{pmatrix}$$

$$\det(A) = 8 - 3 = 5$$

$$x = \frac{\begin{vmatrix} 5 & 1 \\ 6 & 4 \end{vmatrix}}{5} = \frac{20 - 6}{5} = \frac{14}{5}$$

$$y = \frac{\begin{vmatrix} 2 & 5 \\ 3 & 6 \end{vmatrix}}{5} = \frac{12 - 15}{5} = -\frac{3}{5}$$

### Limitaciones

- Solo para sistemas con $\det(A) \neq 0$
- Ineficiente para sistemas grandes (preferir eliminación gaussiana)
- Útil para sistemas pequeños y demostrar existencia/unicidad

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| k | Variable k | variable | N/A | N/A | N/A |
