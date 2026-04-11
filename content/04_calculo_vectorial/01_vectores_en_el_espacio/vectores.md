# Teoría — Vectores en el espacio
## 1.1 Definición de un vector en el plano y en el espacio


![Sistema de coordenadas cartesianas 3D con vectores canónicos i, j, k](../../../assets/images/grafics/04_calculo_vectorial/01_vectores_en_el_espacio/sistema_coordenadas_3d.svg)

### Concepto intuitivo
Un **vector** es un objeto matemático que tiene **magnitud** (longitud) y **dirección**. Geométricamente se representa como una flecha que va de un punto inicial a un punto final.

### Representación en coordenadas
- En el plano $\mathbb{R}^2$: $\mathbf{v} = \langle v_x, v_y \rangle$
- En el espacio $\mathbb{R}^3$: $\mathbf{v} = \langle v_x, v_y, v_z \rangle$

Las componentes $v_x, v_y, v_z$ indican cuánto "avanza" el vector en cada eje coordenado.

### Vector posición
Dado un punto $P = (a, b, c)$, el **vector posición** $\overrightarrow{OP}$ va del origen al punto:
$$\overrightarrow{OP} = \langle a, b, c \rangle$$

### Vector entre dos puntos
Si $A = (a_1, a_2, a_3)$ y $B = (b_1, b_2, b_3)$:
$$\overrightarrow{AB} = \langle b_1 - a_1, b_2 - a_2, b_3 - a_3 \rangle$$

### Interpretación geométrica
- **Magnitud**: longitud del segmento.
- **Dirección**: orientación en el espacio, determinada por los ángulos que forma con los ejes.
- **Sentido**: de la cola a la punta de la flecha.

### Magnitud (norma)
$$\lVert \mathbf{v} \rVert = \sqrt{v_x^2 + v_y^2 + v_z^2}$$

### Vector unitario
Un vector con magnitud 1. Para cualquier $\mathbf{v} \neq \mathbf{0}$:
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\lVert \mathbf{v} \rVert}$$

### Vectores canónicos
En $\mathbb{R}^3$: $\mathbf{i} = \langle 1,0,0 \rangle$, $\mathbf{j} = \langle 0,1,0 \rangle$, $\mathbf{k} = \langle 0,0,1 \rangle$.

Todo vector se escribe como:
$$\mathbf{v} = v_x\mathbf{i} + v_y\mathbf{j} + v_z\mathbf{k}$$

*Figura 1.1.1: Sistema de coordenadas tridimensional con los ejes $x$, $y$, $z$ y los vectores canónicos $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$.*

---

## 1.2 Álgebra vectorial y su geometría


![Suma de vectores y multiplicación por escalar en el espacio](../../../assets/images/grafics/04_calculo_vectorial/01_vectores_en_el_espacio/operaciones_vectores_3d.svg)

### Suma de vectores
$$\mathbf{u} + \mathbf{v} = \langle u_x + v_x, u_y + v_y, u_z + v_z \rangle$$

**Interpretación geométrica (regla del paralelogramo)**: coloca los vectores con el mismo origen; la diagonal del paralelogramo que forman es $\mathbf{u} + \mathbf{v}$.

**Regla cabeza-cola**: coloca la cola de $\mathbf{v}$ en la punta de $\mathbf{u}$; el resultado va del origen de $\mathbf{u}$ a la punta de $\mathbf{v}$.

### Resta de vectores
$$\mathbf{u} - \mathbf{v} = \mathbf{u} + (-\mathbf{v})$$

Geométricamente, $-\mathbf{v}$ es el vector opuesto (misma magnitud, dirección contraria).

### Multiplicación por escalar
$$c\mathbf{v} = \langle cv_x, cv_y, cv_z \rangle$$

- Si $c > 0$: mismo sentido, magnitud escalada por $c$.
- Si $c < 0$: sentido opuesto.
- Si $c = 0$: vector nulo $\mathbf{0}$.

### Propiedades del álgebra vectorial
| Propiedad | Expresión |
|-----------|-----------|
| Conmutativa | $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ |
| Asociativa | $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$ |
| Neutro aditivo | $\mathbf{v} + \mathbf{0} = \mathbf{v}$ |
| Inverso aditivo | $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$ |
| Distributiva escalar | $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ |

### Combinación lineal
Dados vectores $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ y escalares $c_1, c_2, \ldots, c_n$:
$$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_n\mathbf{v}_n$$

**Aplicación**: dos vectores no paralelos generan un plano; tres vectores no coplanares generan todo $\mathbb{R}^3$.

### Vectores paralelos
$\mathbf{u} \parallel \mathbf{v}$ si existe $k \in \mathbb{R}$ tal que $\mathbf{u} = k\mathbf{v}$.

*Figura 1.2.1: Suma de vectores (regla del paralelogramo) y multiplicación por escalar en el espacio tridimensional.*

---

## 1.3 Producto escalar y vectorial


![Producto escalar (punto) y producto vectorial (cruz)](../../../assets/images/grafics/04_calculo_vectorial/01_vectores_en_el_espacio/producto_punto_cruz.svg)

### Producto escalar (producto punto)

**Definición algebraica**:
$$\mathbf{u} \cdot \mathbf{v} = u_x v_x + u_y v_y + u_z v_z$$

**Definición geométrica**:
$$\mathbf{u} \cdot \mathbf{v} = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta$$

donde $\theta$ es el ángulo entre los vectores.

**Propiedades clave**:
- $\mathbf{u} \cdot \mathbf{v} = 0 \iff \mathbf{u} \perp \mathbf{v}$ (ortogonales)
- $\mathbf{v} \cdot \mathbf{v} = \lVert \mathbf{v} \rVert^2$

**Ángulo entre vectores**:
$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}$$

**Proyección de $\mathbf{u}$ sobre $\mathbf{v}$**:
$$\text{comp}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert} \quad \text{(escalar)}$$
$$\text{proy}_{\mathbf{v}}\mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{v} \rVert^2}\mathbf{v} \quad \text{(vector)}$$

### Producto vectorial (producto cruz)

**Solo en $\mathbb{R}^3$**. El resultado es un **vector**.

**Definición mediante determinante**:
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_x & u_y & u_z \\ v_x & v_y & v_z \end{vmatrix}$$

Expandiendo:
$$\mathbf{u} \times \mathbf{v} = \langle u_y v_z - u_z v_y, \; u_z v_x - u_x v_z, \; u_x v_y - u_y v_x \rangle$$

**Propiedades geométricas**:
- $\mathbf{u} \times \mathbf{v}$ es **ortogonal** a $\mathbf{u}$ y a $\mathbf{v}$.
- Dirección dada por la **regla de la mano derecha**.
- $\lVert \mathbf{u} \times \mathbf{v} \rVert = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \sin\theta$ = área del paralelogramo.

**Propiedades algebraicas**:
- Anticonmutativo: $\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v})$
- $\mathbf{u} \times \mathbf{u} = \mathbf{0}$
- $\mathbf{u} \times \mathbf{v} = \mathbf{0} \iff \mathbf{u} \parallel \mathbf{v}$

### Producto triple escalar
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det \begin{pmatrix} u_x & u_y & u_z \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{pmatrix}$$

Su valor absoluto es el **volumen del paralelepípedo** formado por los tres vectores.

*Figura 1.3.1: Interpretación geométrica del producto escalar (proyección) y producto vectorial (área del paralelogramo, vector perpendicular).*

---

## 1.4 Ecuación de la recta

### Forma vectorial
Una recta pasa por $P_0 = (x_0, y_0, z_0)$ con dirección $\mathbf{v} = \langle a, b, c \rangle$:
$$\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v} = \langle x_0 + at, \; y_0 + bt, \; z_0 + ct \rangle$$

donde $t \in \mathbb{R}$ es el parámetro.

### Forma paramétrica
$$\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}$$

### Forma simétrica (si $a, b, c \neq 0$)
$$\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$$

### Recta por dos puntos
Dados $A$ y $B$, dirección $\mathbf{v} = \overrightarrow{AB}$, recta: $\mathbf{r}(t) = A + t\overrightarrow{AB}$.

### Posiciones relativas de dos rectas
- **Paralelas**: direcciones proporcionales.
- **Coincidentes**: paralelas y comparten un punto.
- **Secantes**: se cruzan en un punto (resolver sistema).
- **Alabeadas** (en 3D): ni paralelas ni secantes.

---

## 1.5 Ecuación del plano

### Forma normal (vectorial)
Un plano con punto $P_0 = (x_0, y_0, z_0)$ y vector normal $\mathbf{n} = \langle a, b, c \rangle$:
$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$$

### Forma escalar (general)
$$ax + by + cz = d$$
donde $d = ax_0 + by_0 + cz_0$.

El vector $\mathbf{n} = \langle a, b, c \rangle$ es normal al plano.

### Plano por tres puntos no colineales
Dados $A$, $B$, $C$:
1. Calcula $\overrightarrow{AB}$ y $\overrightarrow{AC}$.
2. Normal: $\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}$.
3. Usa cualquiera de los tres puntos en la ecuación.

### Distancia de un punto a un plano
Dado el plano $ax + by + cz = d$ y el punto $Q = (x_1, y_1, z_1)$:
$$D = \frac{|ax_1 + by_1 + cz_1 - d|}{\sqrt{a^2 + b^2 + c^2}}$$

### Ángulo entre dos planos
Si los planos tienen normales $\mathbf{n}_1$ y $\mathbf{n}_2$:
$$\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\lVert \mathbf{n}_1 \rVert \lVert \mathbf{n}_2 \rVert}$$

### Ángulo entre recta y plano
Si la recta tiene dirección $\mathbf{v}$ y el plano normal $\mathbf{n}$:
$$\sin\alpha = \frac{|\mathbf{v} \cdot \mathbf{n}|}{\lVert \mathbf{v} \rVert \lVert \mathbf{n} \rVert}$$

*Figura 1.5.1: Representación de rectas y planos en el espacio 3D, mostrando vectores directores, vectores normales e intersecciones.*

---

<!--
IA: Esta teoría cubre los 5 subtemas del temario oficial.
Usa las definiciones y fórmulas aquí como referencia canónica.
Al generar problemas, verifica que el estudiante domine cada sección antes de avanzar.
file_id: CV-01-Teoria-Vectores
-->


![Ecuación de la recta y el plano en el espacio 3D](../../../assets/images/grafics/04_calculo_vectorial/01_vectores_en_el_espacio/recta_plano_espacio.svg)
