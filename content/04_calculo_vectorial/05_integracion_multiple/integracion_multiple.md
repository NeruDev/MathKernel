<!--
yaml_frontmatter:
  id: 'integracion_multiple'
  content_path: 'content/04_calculo_vectorial/05_integracion_multiple/integracion_multiple.md'
  metadata_path: 'metadata/content/04_calculo_vectorial/05_integracion_multiple/integracion_multiple.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de Integración Múltiple'
  key_headings:
    - 'Teoría — Integración múltiple'
    - '5.1 Integrales dobles sobre rectángulos'
    - 'Definición mediante sumas de Riemann'
    - 'Teorema de Fubini (rectángulos)'
    - 'Interpretación geométrica'
    - 'Propiedades'
    - '5.2 Integrales dobles sobre regiones generales'
    - 'Región tipo I (simple en $y$)'
  key_concepts:
    - 'Integrales dobles'
    - 'Coordenadas polares'
    - 'Integrales triples'
    - 'Teorema de Green'
    - 'Teorema de Stokes'
-->
# Teoría — Integración múltiple
## 5.1 Integrales dobles sobre rectángulos


![Regiones Tipo I y Tipo II](../../../assets/images/grafics/04_calculo_vectorial/05_integracion_multiple/regiones_integracion_doble.svg)



### Definición mediante sumas de Riemann

Para $f(x, y)$ definida en el rectángulo $R = [a, b] \times [c, d]$:

$$\iint_R f(x, y)\, dA = \lim_{m,n \to \infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(x_i^*, y_j^*) \Delta A$$

donde $\Delta A = \Delta x \cdot \Delta y$.

### Teorema de Fubini (rectángulos)

Si $f$ es continua en $R = [a, b] \times [c, d]$:

$$\iint_R f(x, y)\, dA = \int_a^b \int_c^d f(x, y)\, dy\, dx = \int_c^d \int_a^b f(x, y)\, dx\, dy$$

El orden de integración puede intercambiarse.

### Interpretación geométrica

- Si $f(x, y) \geq 0$: $\iint_R f\, dA$ = volumen bajo la superficie $z = f(x,y)$ sobre $R$
- $\iint_R 1\, dA$ = área de $R$

### Propiedades

| Propiedad | Fórmula |
|-----------|---------|
| Linealidad | $\iint_R [af + bg]\, dA = a\iint_R f\, dA + b\iint_R g\, dA$ |
| Aditividad | Si $R = R_1 \cup R_2$ disjuntas: $\iint_R f\, dA = \iint_{R_1} f\, dA + \iint_{R_2} f\, dA$ |
| Comparación | Si $f \leq g$ en $R$: $\iint_R f\, dA \leq \iint_R g\, dA$ |

---

## 5.2 Integrales dobles sobre regiones generales

### Región tipo I (simple en $y$)

$$D = \{(x, y) : a \leq x \leq b, \; g_1(x) \leq y \leq g_2(x)\}$$

$$\iint_D f(x, y)\, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\, dy\, dx$$

### Región tipo II (simple en $x$)

$$D = \{(x, y) : c \leq y \leq d, \; h_1(y) \leq x \leq h_2(y)\}$$

$$\iint_D f(x, y)\, dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\, dx\, dy$$

### Selección del orden de integración

- Elegir el orden que simplifique los límites
- A veces un orden es imposible o muy difícil; el otro puede ser factible
- Para cambiar el orden: dibujar la región e identificar los nuevos límites

*Figura 5.2.1: Regiones tipo I (simple en $y$) y tipo II (simple en $x$) para integrales dobles.*

### Valor medio

$$f_{\text{prom}} = \frac{1}{\text{Área}(D)} \iint_D f(x, y)\, dA$$

---

## 5.3 Coordenadas polares en integrales dobles

### Cambio a polares

$$x = r\cos\theta, \quad y = r\sin\theta$$
$$dA = r\, dr\, d\theta$$

**El factor $r$ es el Jacobiano** y es esencial.

### Transformación de la integral

$$\iint_D f(x, y)\, dA = \int_\alpha^\beta \int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\, r\, dr\, d\theta$$

### Cuándo usar polares

- Regiones circulares o sectores
- Funciones con $x^2 + y^2$
- Simetría radial

### Regiones comunes en polares

| Región | Límites |
|--------|---------|
| Disco $x^2 + y^2 \leq R^2$ | $0 \leq r \leq R$, $0 \leq \theta \leq 2\pi$ |
| Semidisco superior | $0 \leq r \leq R$, $0 \leq \theta \leq \pi$ |
| Cuarto de disco (primer cuadrante) | $0 \leq r \leq R$, $0 \leq \theta \leq \pi/2$ |
| Corona $a \leq r \leq b$ | $a \leq r \leq b$, $0 \leq \theta \leq 2\pi$ |
| Sector | $0 \leq r \leq R$, $\alpha \leq \theta \leq \beta$ |

---

## 5.4 Aplicaciones de integrales dobles


![Sistema de coordenadas cilíndricas](../../../assets/images/grafics/04_calculo_vectorial/05_integracion_multiple/coordenadas_cilindricas.svg)



### Área

$$A = \iint_D dA$$

### Volumen

$$V = \iint_D f(x, y)\, dA$$

(si $f \geq 0$ representa la altura).

### Masa

Si $\rho(x, y)$ es la densidad superficial:
$$m = \iint_D \rho(x, y)\, dA$$

### Centro de masa

$$\bar{x} = \frac{1}{m} \iint_D x\rho(x, y)\, dA, \quad \bar{y} = \frac{1}{m} \iint_D y\rho(x, y)\, dA$$

### Momentos de inercia

| Eje | Fórmula |
|-----|---------|
| Respecto al eje $x$ | $I_x = \iint_D y^2 \rho(x, y)\, dA$ |
| Respecto al eje $y$ | $I_y = \iint_D x^2 \rho(x, y)\, dA$ |
| Respecto al origen (polar) | $I_0 = \iint_D (x^2 + y^2)\rho(x, y)\, dA = I_x + I_y$ |

### Radio de giro

$$\bar{x}_g = \sqrt{\frac{I_y}{m}}, \quad \bar{y}_g = \sqrt{\frac{I_x}{m}}$$

---

## 5.5 Integrales triples


![Sistema de coordenadas esféricas](../../../assets/images/grafics/04_calculo_vectorial/05_integracion_multiple/coordenadas_esfericas.svg)



### Definición

Para $f(x, y, z)$ en una región $E \subseteq \mathbb{R}^3$:
$$\iiint_E f(x, y, z)\, dV = \lim \sum f(x_i^*, y_j^*, z_k^*) \Delta V$$

### Teorema de Fubini (cajas)

Para $B = [a,b] \times [c,d] \times [e,f]$:
$$\iiint_B f\, dV = \int_a^b \int_c^d \int_e^f f(x,y,z)\, dz\, dy\, dx$$

(cualquier orden si $f$ es continua).

### Regiones generales

**Tipo 1** (proyección en $xy$):
$$E = \{(x,y,z) : (x,y) \in D, \; u_1(x,y) \leq z \leq u_2(x,y)\}$$

$$\iiint_E f\, dV = \iint_D \left[ \int_{u_1(x,y)}^{u_2(x,y)} f(x,y,z)\, dz \right] dA$$

### Aplicaciones

| Cantidad | Fórmula |
|----------|---------|
| **Volumen** | $V = \iiint_E dV$ |
| **Masa** | $m = \iiint_E \rho(x,y,z)\, dV$ |
| **Centro de masa** | $\bar{x} = \frac{1}{m}\iiint_E x\rho\, dV$, etc. |

---

## 5.6 Coordenadas cilíndricas

### Definición

$$x = r\cos\theta, \quad y = r\sin\theta, \quad z = z$$

- $r \geq 0$: distancia al eje $z$
- $\theta$: ángulo en el plano $xy$
- $z$: altura

### Elemento de volumen

$$dV = r\, dr\, d\theta\, dz$$

### Integral triple

$$\iiint_E f(x,y,z)\, dV = \iiint f(r\cos\theta, r\sin\theta, z)\, r\, dr\, d\theta\, dz$$

### Cuándo usar cilíndricas

- Simetría respecto al eje $z$
- Cilindros, conos, paraboloides
- Funciones con $x^2 + y^2$

### Regiones comunes

| Región | Descripción |
|--------|-------------|
| Cilindro | $r \leq R$, $0 \leq z \leq h$ |
| Cono | $0 \leq z \leq h$, $0 \leq r \leq az$ |
| Paraboloide | $0 \leq z \leq c - r^2$ |

*Figura 5.6.1: Sistema de coordenadas cilíndricas $(r, \theta, z)$ y elemento de volumen $dV = r\,dr\,d\theta\,dz$.*

---

## 5.7 Coordenadas esféricas


![Teoremas de Green, Stokes y Divergencia](../../../assets/images/grafics/04_calculo_vectorial/05_integracion_multiple/teoremas_integrales.svg)



### Definición

$$x = \rho\sin\phi\cos\theta$$
$$y = \rho\sin\phi\sin\theta$$
$$z = \rho\cos\phi$$

- $\rho \geq 0$: distancia al origen
- $\phi \in [0, \pi]$: ángulo desde el eje $z$ positivo (colatitud)
- $\theta \in 0, 2\pi)$: ángulo en el plano $xy$ (azimut)

### Relaciones útiles

$$\rho = \sqrt{x^2 + y^2 + z^2}$$
$$x^2 + y^2 = \rho^2\sin^2\phi$$
$$\cos\phi = \frac{z}{\rho}$$

### Elemento de volumen

$$dV = \rho^2 \sin\phi\, d\rho\, d\phi\, d\theta$$

### Integral triple

$$\iiint_E f(x,y,z)\, dV = \iiint f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi)\, \rho^2\sin\phi\, d\rho\, d\phi\, d\theta$$

### Cuándo usar esféricas

- Simetría respecto al origen
- Esferas, conos, hemisferios
- Funciones con $x^2 + y^2 + z^2$

### Regiones comunes

| Región | Límites |
|--------|---------|
| Esfera $\rho \leq R$ | $0 \leq \rho \leq R$, $0 \leq \phi \leq \pi$, $0 \leq \theta \leq 2\pi$ |
| Hemisferio superior | $0 \leq \rho \leq R$, $0 \leq \phi \leq \pi/2$, $0 \leq \theta \leq 2\pi$ |
| Octante | $0 \leq \rho \leq R$, $0 \leq \phi \leq \pi/2$, $0 \leq \theta \leq \pi/2$ |
| Cono $\phi = \phi_0$ | $0 \leq \phi \leq \phi_0$ |
| Capa esférica | $a \leq \rho \leq b$ |

*Figura 5.7.1: Sistema de coordenadas esféricas $(\rho, \phi, \theta)$ y elemento de volumen $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.*

---

## 5.8 Cambio de variables general

### Transformación

Sea $T: (u, v) \mapsto (x, y)$ con $x = x(u, v)$, $y = y(u, v)$.

### Jacobiano

$$\frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$

### Fórmula de cambio de variables

$$\iint_R f(x, y)\, dx\, dy = \iint_S f(x(u,v), y(u,v)) \left| \frac{\partial(x,y)}{\partial(u,v)} \right| du\, dv$$

### Jacobianos comunes

| Transformación | Jacobiano |
|----------------|-----------|
| Polar: $x = r\cos\theta$, $y = r\sin\theta$ | $r$ |
| Cilíndrica | $r$ |
| Esférica | $\rho^2 \sin\phi$ |

### En tres dimensiones

$$\iiint_E f(x,y,z)\, dV = \iiint_{E'} f(x(u,v,w), y(u,v,w), z(u,v,w)) \left| \frac{\partial(x,y,z)}{\partial(u,v,w)} \right| du\, dv\, dw$$

---

## 5.9 Integrales de línea

### Integral de línea de una función escalar

Para $f(x, y, z)$ a lo largo de la curva $C$ parametrizada por $\mathbf{r}(t)$, $a \leq t \leq b$:

$$\int_C f\, ds = \int_a^b f(\mathbf{r}(t)) \lVert \mathbf{r}'(t) \rVert\, dt$$

### Integral de línea de un campo vectorial

Para $\mathbf{F} = \langle P, Q, R \rangle$:

$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\, dt = \int_C P\,dx + Q\,dy + R\,dz$$

### Trabajo

El trabajo realizado por una fuerza $\mathbf{F}$ a lo largo de $C$:
$$W = \int_C \mathbf{F} \cdot d\mathbf{r}$$

### Independencia del camino

$\int_C \mathbf{F} \cdot d\mathbf{r}$ es independiente del camino si y solo si $\mathbf{F}$ es conservativo.

### Campo conservativo

$\mathbf{F}$ es **conservativo** si existe $f$ [tal que $\mathbf{F} = \nabla f$.

**Criterio** (en región simplemente conexa): $\mathbf{F} = \langle P, Q \rangle$ es conservativo si y solo si:
$$\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}$$

### Teorema fundamental para integrales de línea

Si $\mathbf{F} = \nabla f$:
$$\int_C \nabla f \cdot d\mathbf{r} = f(\mathbf{r}(b)) - f(\mathbf{r}(a))$$

---

## 5.10 Teorema de Green

### Enunciado

Sea $D$ una región simplemente conexa con frontera $C$ recorrida en sentido positivo (antihorario). Si $P$ y $Q$ tienen derivadas parciales continuas:

$$\oint_C P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$$

### Formas alternativas

**Forma de circulación**:
$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_D (\nabla \times \mathbf{F}) \cdot \mathbf{k}\, dA$$

**Forma de flujo**:
$$\oint_C \mathbf{F} \cdot \mathbf{n}\, ds = \iint_D \nabla \cdot \mathbf{F}\, dA$$

### Área mediante Green

$$A = \frac{1}{2} \oint_C x\,dy - y\,dx = \oint_C x\,dy = -\oint_C y\,dx$$

---

## 5.11 Integrales de superficie

### Área de una superficie

Para $z = g(x, y)$ sobre región $D$:
$$A = \iint_D \sqrt{1 + (g_x)^2 + (g_y)^2}\, dA$$

### Integral de superficie de función escalar

$$\iint_S f\, dS = \iint_D f(x, y, g(x,y)) \sqrt{1 + (g_x)^2 + (g_y)^2}\, dA$$

### Superficie parametrizada

Para $\mathbf{r}(u, v) = \langle x(u,v), y(u,v), z(u,v) \rangle$:

$$dS = \lVert \mathbf{r}_u \times \mathbf{r}_v \rVert\, du\, dv$$

### Integral de superficie de campo vectorial (flujo)

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_D \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v)\, du\, dv$$

---

## 5.12 Teoremas fundamentales del cálculo vectorial

### Teorema de Stokes

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

Relaciona la circulación de $\mathbf{F}$ alrededor de $C$ con el flujo del rotacional a través de $S$.

### Teorema de la divergencia (Gauss)

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E \nabla \cdot \mathbf{F}\, dV$$

Relaciona el flujo de $\mathbf{F}$ a través de $S$ con la integral de la divergencia sobre $E$.

### Operadores diferenciales

| Operador | Definición |
|----------|------------|
| **Gradiente** | $\nabla f = \langle f_x, f_y, f_z \rangle$ |
| **Divergencia** | $\nabla \cdot \mathbf{F} = P_x + Q_y + R_z$ |
| **Rotacional** | $\nabla \times \mathbf{F} = \langle R_y - Q_z, P_z - R_x, Q_x - P_y \rangle$ |
| **Laplaciano** | $\nabla^2 f = f_{xx} + f_{yy} + f_{zz}$ |

*Figura 5.12.1: Ilustración de los teoremas de Green, Stokes y Divergencia que relacionan integrales de línea, superficie y volumen.*

---

<!--
IA: Esta teoría cubre integración múltiple, cambio de coordenadas y teoremas vectoriales.
Usa las definiciones y fórmulas aquí como referencia canónica.
Al generar problemas, asegura dominio progresivo de cada sección.
file_id: CV-05-Teoria-Integracion
-->

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| π | Constante pi | constante | rad | 3.14159265359 | 12 |
| e | Numero de Euler | constante | N/A | 2.71828182846 | 12 |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| z | Variable z | variable | N/A | N/A | N/A |
| t | Variable t | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| m | Variable m | variable | N/A | N/A | N/A |
