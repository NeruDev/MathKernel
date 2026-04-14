<!--
yaml_frontmatter:
  id: 'series_de_potencias'
  content_path: 'content/05_ecuaciones_diferenciales/05_series_de_potencias/series_de_potencias.md'
  metadata_path: 'metadata/content/05_ecuaciones_diferenciales/05_series_de_potencias/series_de_potencias.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de Series de Potencias'
  key_headings:
    - 'Teoría: Series de Potencias para EDO'
    - '5.1 Repaso de Series de Potencias'
    - 'Definición'
    - 'Radio de Convergencia'
    - 'Operaciones con Series'
    - 'Función Analítica'
    - '5.2 Soluciones en Puntos Ordinarios'
    - 'Clasificación de Puntos'
  key_concepts:
    - 'Puntos ordinarios'
    - 'Método de Frobenius'
    - 'Ecuación de Bessel'
    - 'Polinomios de Legendre'
    - 'Relación de recurrencia'
-->
# Teoría: Series de Potencias para EDO
## 5.1 Repaso de Series de Potencias

### Definición

Una **serie de potencias** centrada en $x_0$ es:

$$\sum_{n=0}^{\infty} c_n (x-x_0)^n = c_0 + c_1(x-x_0) + c_2(x-x_0)^2 + \cdots$$

### Radio de Convergencia

El **radio de convergencia** $R$ se determina por:

$$\frac{1}{R} = \lim_{n\to\infty} \left|\frac{c_{n+1}}{c_n}\right| \quad \text{o} \quad \frac{1}{R} = \lim_{n\to\infty} |c_n|^{1/n}$$

La serie converge para $|x - x_0| < R$ y diverge para $|x - x_0| > R$.

### Operaciones con Series

**Suma:**
$$\sum c_n x^n + \sum d_n x^n = \sum (c_n + d_n) x^n$$

**Multiplicación por $x^k$:**
$$x^k \sum_{n=0}^{\infty} c_n x^n = \sum_{n=0}^{\infty} c_n x^{n+k} = \sum_{m=k}^{\infty} c_{m-k} x^m$$

**Derivación término a término:**
$$\frac{d}{dx}\sum_{n=0}^{\infty} c_n x^n = \sum_{n=1}^{\infty} n c_n x^{n-1}$$

**Integración término a término:**
$$\int \sum_{n=0}^{\infty} c_n x^n \, dx = \sum_{n=0}^{\infty} \frac{c_n}{n+1} x^{n+1} + C$$

### Función Analítica

Una función es **analítica** en $x_0$ si tiene desarrollo en serie de potencias convergente en un entorno de $x_0$.

---

## 5.2 Soluciones en Puntos Ordinarios

### Clasificación de Puntos

Para la ecuación en forma estándar:

$$y'' + P(x)y' + Q(x)y = 0$$

**Punto ordinario:** $P(x)$ y $Q(x)$ son analíticas en $x_0$

**Punto singular:** $P(x)$ o $Q(x)$ no son analíticas en $x_0$

### Teorema de Existencia

Si $x_0$ es un **punto ordinario** de $y'' + P(x)y' + Q(x)y = 0$, entonces existen dos soluciones linealmente independientes de la forma:

$$y = \sum_{n=0}^{\infty} c_n (x-x_0)^n$$

que convergen en un intervalo $|x - x_0| < R$, donde $R$ es al menos la distancia al punto singular más cercano.

### Método de Solución

1. Suponer $y = \sum_{n=0}^{\infty} c_n x^n$ (para $x_0 = 0$)

2. Calcular:
   - $y' = \sum_{n=1}^{\infty} n c_n x^{n-1}$
   - $y'' = \sum_{n=2}^{\infty} n(n-1) c_n x^{n-2}$

3. Sustituir en la EDO

4. Igualar coeficientes de cada potencia a cero

5. Obtener **relación de recurrencia** para los $c_n$

6. Escribir la solución general

> **Ejemplo:** Resolver $y'' + y = 0$
> 
> $y = \sum c_n x^n$, $y'' = \sum_{n=2}^{\infty} n(n-1)c_n x^{n-2}$
> 
> Cambiando índice en $y''$: sea $m = n-2$, entonces $n = m+2$
> 
> $y'' = \sum_{m=0}^{\infty} (m+2)(m+1)c_{m+2} x^m$
> 
> Sustituyendo: $\sum_{n=0}^{\infty} [(n+2)(n+1)c_{n+2} + c_n] x^n = 0$
> 
> **Recurrencia:** $c_{n+2} = -\frac{c_n}{(n+2)(n+1)}$
> 
> Para $n$ par: $c_0, c_2 = -\frac{c_0}{2}, c_4 = \frac{c_0}{24}, ...$
> 
> Para $n$ impar: $c_1, c_3 = -\frac{c_1}{6}, c_5 = \frac{c_1}{120}, ...$
> 
> $$y = c_0\left(1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots\right) + c_1\left(x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots\right)$$
> 
> $$y = c_0 \cos x + c_1 \sin x$$

---

## 5.3 Método de Frobenius

### Puntos Singulares Regulares

Un punto singular $x_0$ de:

$$P(x)y'' + Q(x)y' + R(x)y = 0$$

es **regular** si los límites:

$$p_0 = \lim_{x \to x_0} (x-x_0)\frac{Q(x)}{P(x)}, \quad q_0 = \lim_{x \to x_0} (x-x_0)^2\frac{R(x)}{P(x)}$$

existen y son finitos. De lo contrario, es **irregular**.

### Forma de Frobenius

Para un punto singular regular en $x_0 = 0$, buscamos solución:

$$\boxed{y = x^r \sum_{n=0}^{\infty} c_n x^n = \sum_{n=0}^{\infty} c_n x^{n+r}, \quad c_0 \neq 0}$$

### Ecuación Indicial

Al sustituir en la EDO, el coeficiente de la potencia más baja da la **ecuación indicial**:

$$\boxed{r(r-1) + p_0 r + q_0 = 0}$$

Las raíces $r_1, r_2$ (con $r_1 \geq r_2$ si son reales) determinan los exponentes de la solución.

### Casos según las Raíces

**Caso 1:** $r_1 - r_2 \notin \mathbb{Z}$ (no difieren por entero)

Dos soluciones independientes tipo Frobenius:
$$y_1 = x^{r_1}\sum_{n=0}^{\infty} a_n x^n, \quad y_2 = x^{r_2}\sum_{n=0}^{\infty} b_n x^n$$

**Caso 2:** $r_1 = r_2 = r$ (raíces iguales)

$$y_1 = x^r\sum_{n=0}^{\infty} a_n x^n$$
$$y_2 = y_1 \ln x + x^r \sum_{n=1}^{\infty} b_n x^n$$

**Caso 3:** $r_1 - r_2 = N$ (entero positivo)

$$y_1 = x^{r_1}\sum_{n=0}^{\infty} a_n x^n$$
$$y_2 = C y_1 \ln x + x^{r_2}\sum_{n=0}^{\infty} b_n x^n$$

donde $C$ puede ser 0 (en cuyo caso $y_2$ no tiene logaritmo).

> **Ejemplo:** $2xy'' + y' + y = 0$ (punto singular regular en $x = 0$)
> 
> Forma estándar: $y'' + \frac{1}{2x}y' + \frac{1}{2x}y = 0$
> 
> $p_0 = \lim_{x\to 0} x \cdot \frac{1}{2x} = \frac{1}{2}$
> 
> $q_0 = \lim_{x\to 0} x^2 \cdot \frac{1}{2x} = 0$
> 
> **Ecuación indicial:** $r(r-1) + \frac{1}{2}r + 0 = 0$
> 
> $r^2 - \frac{1}{2}r = 0 \Rightarrow r(r - \frac{1}{2}) = 0$
> 
> $r_1 = \frac{1}{2}$, $r_2 = 0$
> 
> $r_1 - r_2 = \frac{1}{2} \notin \mathbb{Z}$ → Caso 1, dos series de Frobenius

---

## 5.4 Ecuaciones Especiales

### Ecuación de Bessel

$$x^2y'' + xy' + (x^2 - \nu^2)y = 0$$

donde $\nu \geq 0$ es el **orden**.

**Solución general:**
$$y = C_1 J_\nu(x) + C_2 Y_\nu(x)$$

**Función de Bessel de primera especie:**
$$J_\nu(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{n!\,\Gamma(n+\nu+1)}\left(\frac{x}{2}\right)^{2n+\nu}$$

Para $\nu = 0$:
$$J_0(x) = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \frac{x^6}{2304} + \cdots$$

**Aplicaciones:** Vibraciones de membranas circulares, conducción de calor en cilindros.

### Ecuación de Legendre

$$(1-x^2)y'' - 2xy' + n(n+1)y = 0$$

donde $n$ es un entero no negativo.

**Solución:** Los **polinomios de Legendre** $P_n(x)$

$$P_0(x) = 1$$
$$P_1(x) = x$$
$$P_2(x) = \frac{1}{2}(3x^2 - 1)$$
$$P_3(x) = \frac{1}{2}(5x^3 - 3x)$$

**Fórmula de Rodrigues:**
$$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2-1)^n$$

**Aplicaciones:** Potenciales electrostáticos, armónicos esféricos.

### Ecuación de Hermite

$$y'' - 2xy' + 2ny = 0$$

**Polinomios de Hermite:**
$$H_0(x) = 1, \quad H_1(x) = 2x, \quad H_2(x) = 4x^2 - 2$$

**Aplicación:** Oscilador armónico cuántico.

### Ecuación de Laguerre

$$xy'' + (1-x)y' + ny = 0$$

**Polinomios de Laguerre:**
$$L_0(x) = 1, \quad L_1(x) = 1-x, \quad L_2(x) = \frac{1}{2}(x^2 - 4x + 2)$$

**Aplicación:** Átomo de hidrógeno en mecánica cuántica.

---

## Tabla: Ecuaciones Especiales

| Ecuación | Forma | Soluciones |
|----------|-------|------------|
| Bessel | $x^2y'' + xy' + (x^2-\nu^2)y = 0$ | $J_\nu(x), Y_\nu(x)$ |
| Legendre | $(1-x^2)y'' - 2xy' + n(n+1)y = 0$ | $P_n(x), Q_n(x)$ |
| Hermite | $y'' - 2xy' + 2ny = 0$ | $H_n(x)$ |
| Laguerre | $xy'' + (1-x)y' + ny = 0$ | $L_n(x)$ |
| Chebyshev | $(1-x^2)y'' - xy' + n^2y = 0$ | $T_n(x), U_n(x)$ |


![Diagrama de flujo para método de series de potencias](../../../assets/images/grafics/05_ecuaciones_diferenciales/ED-05/diagrama_decision_series_potencias.svg)


## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| m | Variable m | variable | N/A | N/A | N/A |
| k | Variable k | variable | N/A | N/A | N/A |
| r | Variable r | variable | N/A | N/A | N/A |
