<!--
yaml_frontmatter:
  id: 'aplicaciones_integral'
  content_path: 'content/03_calculo_integral/04_aplicaciones_integral/aplicaciones_integral.md'
  metadata_path: 'metadata/content/03_calculo_integral/04_aplicaciones_integral/aplicaciones_integral.json'
  source_of_truth: 'metadata/content/*.json'
  title: 'Teoría de Aplicaciones de la Integral'
  key_headings:
    - 'Aplicaciones de la Integral'
    - '4.1 Área entre Curvas'
    - 'Área con Integración Vertical'
    - 'Área con Integración Horizontal'
    - 'Criterio de Elección'
    - '4.2 Volúmenes por Discos y Arandelas'
    - 'Método del Disco'
    - 'Método de la Arandela'
  key_concepts:
    - 'Área entre curvas'
    - 'Volúmenes por discos'
    - 'Capas cilíndricas'
    - 'Longitud de arco'
    - 'Trabajo'
-->
# Aplicaciones de la Integral
## 4.1 Área entre Curvas

### Área con Integración Vertical

Si $f(x) \geq g(x)$ en $[a,b]$:
$$A = \int_a^b [f(x) - g(x)] \, dx$$

**Caso general:** Si no se sabe cuál está arriba:
$$A = \int_a^b |f(x) - g(x)| \, dx$$

### Área con Integración Horizontal

Cuando las curvas se expresan mejor como $x = f(y)$:
$$A = \int_c^d [f(y) - g(y)] \, dy$$

donde $f(y) \geq g(y)$ (derecha menos izquierda).

### Criterio de Elección

| Situación | Método |
|-----------|--------|
| Curvas $y = f(x)$ | Integración vertical |
| Curvas $x = g(y)$ | Integración horizontal |
| Se cruzan múltiples veces | Dividir en subintervalos |

---

## 4.2 Volúmenes por Discos y Arandelas

### Método del Disco

Al rotar $y = f(x)$ alrededor del eje $x$, cada sección transversal es un círculo de radio $f(x)$:

$$V = \int_a^b A(x)\,dx = \int_a^b \pi[f(x)]^2\,dx$$

**Rotación alrededor del eje $y$:**
$$V = \pi\int_c^d [g(y)]^2 \, dy$$

### Método de la Arandela

Cuando hay un hueco (región entre dos curvas):

$$V = \pi\int_a^b \left([R(x)]^2 - [r(x)]^2\right) dx$$

donde:
- $R(x)$ = radio exterior
- $r(x)$ = radio interior

### Rotación alrededor de Rectas Paralelas a los Ejes

**Alrededor de $y = k$:**
$$V = \pi\int_a^b [f(x) - k]^2\,dx$$

**Alrededor de $x = h$:**
$$V = \pi\int_c^d [g(y) - h]^2\,dy$$

---

## 4.3 Volúmenes por Capas Cilíndricas

### Concepto

Se "desenrolla" un tubo cilíndrico de:
- Radio: $x$
- Altura: $f(x)$
- Espesor: $dx$

**Área lateral del cilindro:** $2\pi x \cdot f(x)$

### Fórmula General

**Rotación alrededor del eje $y$:**
$$V = 2\pi\int_a^b x \cdot f(x) \, dx$$

**Rotación alrededor del eje $x$:**
$$V = 2\pi\int_c^d y \cdot g(y) \, dy$$

### Rotación alrededor de $x = h$

$$V = 2\pi\int_a^b |x - h| \cdot f(x) \, dx$$

### Cuándo Usar Cada Método

| Método | Usar cuando |
|--------|-------------|
| Discos/Arandelas | Los cortes ⊥ al eje dan círculos fáciles |
| Capas cilíndricas | Los cortes ∥ al eje son más simples |

---

## 4.4 Longitud de Arco

### Derivación

Un elemento de arco $ds$ satisface:
$$ds = \sqrt{dx^2 + dy^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

### Fórmula Cartesiana

$$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$

### Fórmula Paramétrica

Si $x = x(t)$, $y = y(t)$ para $t \in [\alpha, \beta]$:
$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

### Coordenadas Polares

Si $r = f(\theta)$:
$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta$$

---

## 4.5 Área de Superficie de Revolución

### Derivación

Un elemento de superficie es un tronco de cono:
$$dS = 2\pi r \cdot ds$$

donde $r$ es el radio de rotación.

### Rotación alrededor del eje $x$

$$S = 2\pi\int_a^b f(x)\sqrt{1 + [f'(x)]^2} \, dx$$

### Rotación alrededor del eje $y$

$$S = 2\pi\int_a^b x\sqrt{1 + [f'(x)]^2} \, dx$$

### Forma Paramétrica (rotación alrededor de $x$)

$$S = 2\pi\int_\alpha^\beta y(t)\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

---

## 4.6 Trabajo

### Trabajo por Fuerza Variable

$$W = \int_a^b F(x) \, dx$$

**Unidades:**
- SI: Joules (J) = Newton × metro
- CGS: ergios = dina × cm

### Aplicaciones Comunes

#### Resortes (Ley de Hooke)

$$F(x) = kx$$

$$W = \int_{x_1}^{x_2} kx \, dx = \frac{1}{2}k(x_2^2 - x_1^2)$$

#### Bombeo de Fluidos

Para bombear líquido de un tanque:
$$W = \int_a^b \rho g A(y) \cdot d(y) \, dy$$

donde:
- $\rho$ = densidad del fluido
- $g$ = aceleración gravitacional
- $A(y)$ = área de sección transversal
- $d(y)$ = distancia que se eleva el elemento

#### Trabajo por Gravedad

Para elevar un objeto de masa $m$:
$$W = \int_a^b mg \, dy = mg(b - a)$$

#### Cables y Cadenas

Para levantar un cable de densidad lineal $\lambda$:
$$W = \int_0^L \lambda g (L - y) \, dy$$

---

## 4.7 Valor Promedio de una Función

### Definición

El valor promedio de $f$ en $[a,b]$:
$$f_{\text{prom}} = \frac{1}{b-a}\int_a^b f(x) \, dx$$

### Teorema del Valor Medio para Integrales

Si $f$ es continua en $[a,b]$, existe $c \in (a,b)$ tal que:
$$f(c) = \frac{1}{b-a}\int_a^b f(x)\,dx$$

**Interpretación:** La integral es igual al área de un rectángulo de base $(b-a)$ y altura $f(c)$.

### Aplicaciones

- **Velocidad promedio:** $v_{\text{prom}} = \frac{1}{t_2-t_1}\int_{t_1}^{t_2} v(t)\,dt$
- **Temperatura promedio**
- **Concentración promedio**

## Glosario de variables

| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |
| --- | --- | --- | --- | --- | --- |
| π | Constante pi | constante | rad | 3.14159265359 | 12 |
| x | Variable x | variable | N/A | N/A | N/A |
| y | Variable y | variable | N/A | N/A | N/A |
| t | Variable t | variable | N/A | N/A | N/A |
| m | Variable m | variable | N/A | N/A | N/A |
| k | Variable k | variable | N/A | N/A | N/A |
| r | Variable r | variable | N/A | N/A | N/A |
