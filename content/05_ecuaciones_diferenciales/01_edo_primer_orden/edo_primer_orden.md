<!--
yaml_frontmatter:
  id: 'edo_primer_orden'
  content_path: 'content/05_ecuaciones_diferenciales/01_edo_primer_orden/edo_primer_orden.md'
  metadata_path: 'metadata/content/05_ecuaciones_diferenciales/01_edo_primer_orden/edo_primer_orden.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de EDO de Primer Orden'
  key_headings:
    - 'Teoría de EDO de Primer Orden'
    - '1.1 Conceptos Fundamentales'
    - 'Definición de Ecuación Diferencial'
    - 'Orden y Grado'
    - 'Tipos de Soluciones'
    - 'Problema de Valor Inicial (PVI)'
    - 'Teorema de Existencia y Unicidad (Picard-Lindelöf)'
    - '1.2 Ecuaciones Separables'
  key_concepts:
    - 'Ecuaciones separables'
    - 'Ecuaciones lineales'
    - 'Ecuaciones exactas'
    - 'Ecuaciones de Bernoulli'
    - 'Problema de Valor Inicial'
-->
# Teoría de EDO de Primer Orden
## 1.1 Conceptos Fundamentales

### Definición de Ecuación Diferencial

Una **ecuación diferencial** es una ecuación que relaciona una función desconocida con sus derivadas.

**Ecuación Diferencial Ordinaria (EDO):** Involucra una función de una sola variable independiente.

$$F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, ..., \frac{d^ny}{dx^n}\right) = 0$$

### Orden y Grado

- **Orden:** El orden de la derivada más alta que aparece
- **Grado:** El exponente de la derivada de mayor orden (cuando es polinomial)

| Ejemplo | Orden | Grado |
|---------|-------|-------|
| $\frac{dy}{dx} + y = x$ | 1 | 1 |
| $\left(\frac{dy}{dx}\right)^2 + y = 0$ | 1 | 2 |
| $\frac{d^2y}{dx^2} + 3\frac{dy}{dx} = 0$ | 2 | 1 |

### Tipos de Soluciones

**Solución general:** Contiene constantes arbitrarias (una por cada orden).

**Solución particular:** Se obtiene asignando valores a las constantes.

**Solución singular:** No se obtiene de la general (tangente a la familia de curvas).

### Problema de Valor Inicial (PVI)

Un PVI consiste en una EDO junto con condiciones iniciales:
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

### Teorema de Existencia y Unicidad (Picard-Lindelöf)

> **Teorema:** Si $f(x,y)$ y $\frac{\partial f}{\partial y}$ son continuas en una región rectangular $R$ que contiene $(x_0, y_0)$, entonces existe un intervalo $I$ conteniendo a $x_0$ en el cual el PVI tiene **solución única**.

---

## 1.2 Ecuaciones Separables

### Definición

Una EDO es **separable** si puede escribirse como:
$$\frac{dy}{dx} = g(x)h(y)$$

o equivalentemente:
$$M(x)dx + N(y)dy = 0$$

### Método de Solución


![Diagrama de flujo para identificar tipo de EDO de primer orden](../../../assets/images/grafics/05_ecuaciones_diferenciales/ED-01/diagrama_decision_edo_primer_orden.svg)



1. Separar variables: $\frac{dy}{h(y)} = g(x)dx$
2. Integrar ambos lados: $\int \frac{dy}{h(y)} = \int g(x)dx + C$

### Ejemplo

$$\frac{dy}{dx} = xy^2$$

Separando: $\frac{dy}{y^2} = x\,dx$

Integrando: $-\frac{1}{y} = \frac{x^2}{2} + C$

Solución: $y = -\frac{2}{x^2 + C_1}$

---

## 1.3 Ecuaciones Lineales de Primer Orden

### Forma Estándar

$$\frac{dy}{dx} + P(x)y = Q(x)$$

### Factor Integrante

El **factor integrante** es:
$$\mu(x) = e^{\int P(x)dx}$$

### Derivación de la Solución

Multiplicando por $\mu$:
$$\mu\frac{dy}{dx} + \mu P y = \mu Q$$

El lado izquierdo es $\frac{d}{dx}(\mu y)$:
$$\frac{d}{dx}(\mu y) = \mu Q$$

Integrando:
$$\mu y = \int \mu Q\,dx + C$$

### Fórmula de Solución General

$$\boxed{y = \frac{1}{\mu(x)}\left[\int \mu(x)Q(x)dx + C\right]}$$

donde $\mu(x) = e^{\int P(x)dx}$

### Ejemplo

$$\frac{dy}{dx} + \frac{2}{x}y = x^2$$

$P(x) = \frac{2}{x}$, $Q(x) = x^2$

$\mu = e^{\int \frac{2}{x}dx} = e^{2\ln|x|} = x^2$

$y = \frac{1}{x^2}\left[\int x^2 \cdot x^2\,dx + C\right] = \frac{1}{x^2}\left[\frac{x^5}{5} + C\right]$

$$y = \frac{x^3}{5} + \frac{C}{x^2}$$

---

## 1.4 Ecuaciones Exactas

### Definición

La ecuación $M(x,y)dx + N(x,y)dy = 0$ es **exacta** si existe $F(x,y)$ tal que:
$$dF = \frac{\partial F}{\partial x}dx + \frac{\partial F}{\partial y}dy = Mdx + Ndy$$

### Criterio de Exactitud

> **Teorema:** $Mdx + Ndy = 0$ es exacta si y solo si:
> $$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$

### Método de Solución

1. Verificar exactitud: $M_y = N_x$
2. Integrar $M$ respecto a $x$: $F = \int M\,dx + g(y)$
3. Derivar $F$ respecto a $y$ e igualar a $N$: $\frac{\partial F}{\partial y} = N$
4. Resolver para $g(y)$
5. La solución es $F(x,y) = C$

### Ejemplo

$(2xy + 3)dx + (x^2 + 4y)dy = 0$

$M = 2xy + 3$, $N = x^2 + 4y$

Verificar: $M_y = 2x$, $N_x = 2x$ ✓ (Es exacta)

$F = \int (2xy + 3)dx = x^2y + 3x + g(y)$

$\frac{\partial F}{\partial y} = x^2 + g'(y) = x^2 + 4y$

$g'(y) = 4y \Rightarrow g(y) = 2y^2$

**Solución:** $x^2y + 3x + 2y^2 = C$

---

## 1.5 Factor Integrante para Ecuaciones No Exactas

### Cuando No es Exacta

Si $M_y \neq N_x$, buscamos un factor integrante $\mu$ tal que:
$$\mu M\,dx + \mu N\,dy = 0$$
sea exacta.

### Fórmulas para el Factor Integrante

**Caso 1:** Si $\frac{M_y - N_x}{N}$ depende solo de $x$:
$$\mu(x) = e^{\int \frac{M_y - N_x}{N}dx}$$

**Caso 2:** Si $\frac{N_x - M_y}{M}$ depende solo de $y$:
$$\mu(y) = e^{\int \frac{N_x - M_y}{M}dy}$$

---

## 1.6 Ecuaciones de Bernoulli

### Forma

$$\frac{dy}{dx} + P(x)y = Q(x)y^n \quad (n \neq 0, 1)$$

### Método de Solución

**Sustitución:** $v = y^{1-n}$

Entonces: $\frac{dv}{dx} = (1-n)y^{-n}\frac{dy}{dx}$

La ecuación se transforma en **lineal**:
$$\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$$

### Ejemplo

$$\frac{dy}{dx} + y = xy^3$$

Aquí $n = 3$, $v = y^{-2}$

$\frac{dv}{dx} = -2y^{-3}\frac{dy}{dx}$

Dividiendo la original por $y^3$:
$y^{-3}\frac{dy}{dx} + y^{-2} = x$

$-\frac{1}{2}\frac{dv}{dx} + v = x$

$\frac{dv}{dx} - 2v = -2x$ (ecuación lineal)

---

## 1.7 Ecuaciones Homogéneas

### Definición

Una función $f(x,y)$ es **homogénea de grado $n$** si:
$$f(tx, ty) = t^n f(x, y)$$

Una EDO es **homogénea** si puede escribirse como:
$$\frac{dy}{dx} = F\left(\frac{y}{x}\right)$$

### Método de Solución

**Sustitución:** $y = vx$ donde $v = \frac{y}{x}$

Entonces: $\frac{dy}{dx} = v + x\frac{dv}{dx}$

La ecuación se vuelve **separable** en $v$ y $x$:
$$v + x\frac{dv}{dx} = F(v)$$
$$x\frac{dv}{dx} = F(v) - v$$

### Ejemplo

$$\frac{dy}{dx} = \frac{x^2 + y^2}{xy}$$

Reescribiendo: $\frac{dy}{dx} = \frac{x}{y} + \frac{y}{x} = \frac{1}{v} + v$

Con $y = vx$: $v + x\frac{dv}{dx} = \frac{1}{v} + v$

$x\frac{dv}{dx} = \frac{1}{v}$

$v\,dv = \frac{dx}{x}$

$\frac{v^2}{2} = \ln|x| + C$

$\frac{y^2}{2x^2} = \ln|x| + C$

---

## Aplicaciones

### Crecimiento y Decaimiento Exponencial

$$\frac{dP}{dt} = kP \quad \Rightarrow \quad P(t) = P_0 e^{kt}$$

### Enfriamiento de Newton

$$\frac{dT}{dt} = -k(T - T_a)$$

Solución: $T(t) = T_a + (T_0 - T_a)e^{-kt}$

### Circuitos RC

$$\frac{dq}{dt} + \frac{1}{RC}q = \frac{E(t)}{R}$$

### Mezclas

$$\frac{dx}{dt} = \text{(tasa entrada)} - \text{(tasa salida)}$$

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| e | Numero de Euler | constante | N/A | 2.71828182846 | 12 |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| t | Variable t | variable | N/A | N/A | N/A |
| n | Variable n | variable | N/A | N/A | N/A |
| k | Variable k | variable | N/A | N/A | N/A |
| v | Variable v | variable | N/A | N/A | N/A |
