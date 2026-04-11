# Teoría de Álgebra
## 3.1 Expresiones algebraicas

### Lenguaje algebraico

Una **expresión algebraica** es una combinación de números, variables y operaciones. Los componentes fundamentales son:

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Variable** | Símbolo que representa una cantidad desconocida | $x$, $y$, $n$ |
| **Constante** | Valor numérico fijo | $3$, $\pi$, $-7$ |
| **Coeficiente** | Número que multiplica a la variable | En $5x$, el 5 |
| **Término** | Producto de un coeficiente y variables | $3x^2y$, $-7ab$ |
| **Exponente** | Potencia a la que está elevada la variable | En $x^3$, el 3 |

### Términos semejantes

Dos términos son **semejantes** si tienen las mismas variables con los mismos exponentes.

**Ejemplos:**
- $3x^2$ y $-5x^2$ son semejantes ✓
- $2xy$ y $7xy$ son semejantes ✓
- $4x^2$ y $4x^3$ **no** son semejantes ✗
- $3xy$ y $3x^2y$ **no** son semejantes ✗

### Evaluación de expresiones

Para evaluar una expresión, sustituimos las variables por valores específicos.

**Ejemplo:** Evaluar $2x^2 - 3x + 1$ para $x = -2$:
$$2(-2)^2 - 3(-2) + 1 = 2(4) + 6 + 1 = 8 + 6 + 1 = 15$$

### Grado de un término y polinomio

- **Grado de un término**: Suma de los exponentes de sus variables.
- **Grado de un polinomio**: El mayor grado de sus términos.

**Ejemplo:** En $5x^3y^2 - 2x^2y + 7x$:
- Grado de $5x^3y^2$: $3 + 2 = 5$
- Grado de $-2x^2y$: $2 + 1 = 3$
- Grado de $7x$: $1$
- **Grado del polinomio: 5**

---

## 3.2 Operaciones con polinomios

### Suma y resta de polinomios

Se combinan únicamente los términos semejantes.

**Ejemplo:** $(3x^2 - 2x + 5) + (x^2 + 4x - 3)$
$$= (3x^2 + x^2) + (-2x + 4x) + (5 - 3) = 4x^2 + 2x + 2$$

**Ejemplo:** $(5x^3 - 2x + 1) - (2x^3 + x^2 - 3x + 4)$
$$= 5x^3 - 2x + 1 - 2x^3 - x^2 + 3x - 4 = 3x^3 - x^2 + x - 3$$

### Multiplicación de polinomios

Cada término del primer polinomio multiplica a cada término del segundo (propiedad distributiva).

**Ejemplo:** $(2x + 3)(x^2 - 2x + 1)$
$$= 2x(x^2 - 2x + 1) + 3(x^2 - 2x + 1)$$
$$= 2x^3 - 4x^2 + 2x + 3x^2 - 6x + 3$$
$$= 2x^3 - x^2 - 4x + 3$$

### División de polinomios

#### División larga

Para dividir $P(x) \div D(x)$:
1. Dividir el primer término de $P$ entre el primer término de $D$
2. Multiplicar el cociente por $D$ y restar de $P$
3. Repetir hasta que el grado del residuo sea menor que el de $D$

**Ejemplo:** $(x^3 - 2x^2 + x - 3) \div (x - 1)$

```
        x² - x + 0
       ___________
x - 1 | x³ - 2x² + x - 3
        x³ -  x²
        _________
             -x² + x
             -x² + x
             _______
                  0 - 3
```
Cociente: $x^2 - x$, Residuo: $-3$

#### Teorema del residuo

Si $P(x)$ se divide entre $(x - a)$, el residuo es $P(a)$.

**Ejemplo:** El residuo de $P(x) = x^3 - 2x + 1$ entre $(x - 2)$ es:
$$P(2) = 8 - 4 + 1 = 5$$

### División sintética (Ruffini)

Método abreviado para dividir por $(x - a)$:

**Ejemplo:** $(2x^3 - 3x^2 + 4x - 5) \div (x - 2)$

| $a = 2$ | 2 | -3 | 4 | -5 |
|---------|---|----|----|-----|
| | | 4 | 2 | 12 |
| | 2 | 1 | 6 | **7** |

Cociente: $2x^2 + x + 6$, Residuo: $7$

---

## 3.3 Productos notables

### Fórmulas fundamentales

| Nombre | Fórmula |
|--------|---------|
| Binomio al cuadrado | $(a + b)^2 = a^2 + 2ab + b^2$ |
| | $(a - b)^2 = a^2 - 2ab + b^2$ |
| Diferencia de cuadrados | $(a + b)(a - b) = a^2 - b^2$ |
| Binomio al cubo | $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$ |
| | $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$ |
| Suma de cubos | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ |
| Diferencia de cubos | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ |

### Binomio de Newton

Para $(a + b)^n$:
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

Los coeficientes se obtienen del **Triángulo de Pascal**:
```
n=0:          1
n=1:        1   1
n=2:      1   2   1
n=3:    1   3   3   1
n=4:  1   4   6   4   1
```

**Ejemplo:** $(x + 2)^4 = x^4 + 4(x^3)(2) + 6(x^2)(4) + 4(x)(8) + 16$
$$= x^4 + 8x^3 + 24x^2 + 32x + 16$$

---

## 3.4 Factorización

### Tipos de factorización

#### 1. Factor común

Extraer el máximo factor común de todos los términos.

$$6x^3 - 9x^2 + 3x = 3x(2x^2 - 3x + 1)$$

#### 2. Agrupación

Agrupar términos que compartan factores comunes.

$$xy + 2x + 3y + 6 = x(y + 2) + 3(y + 2) = (y + 2)(x + 3)$$

#### 3. Trinomio cuadrado perfecto

$$a^2 + 2ab + b^2 = (a + b)^2$$
$$a^2 - 2ab + b^2 = (a - b)^2$$

**Ejemplo:** $x^2 - 6x + 9 = (x - 3)^2$

#### 4. Diferencia de cuadrados

$$a^2 - b^2 = (a + b)(a - b)$$

**Ejemplo:** $4x^2 - 25 = (2x + 5)(2x - 5)$

#### 5. Trinomio de la forma $x^2 + bx + c$

Buscar dos números que sumen $b$ y multipliquen $c$.

**Ejemplo:** $x^2 + 5x + 6$
- Buscamos $m + n = 5$ y $m \cdot n = 6$
- $m = 2$, $n = 3$
- $x^2 + 5x + 6 = (x + 2)(x + 3)$

#### 6. Trinomio de la forma $ax^2 + bx + c$ (con $a \neq 1$)

**Método AC:**
1. Multiplicar $a \cdot c$
2. Buscar dos números que sumen $b$ y multipliquen $ac$
3. Reescribir y factorizar por agrupación

**Ejemplo:** $6x^2 + 7x - 3$
- $ac = 6 \times (-3) = -18$
- Números: $9$ y $-2$ (suman 7, multiplican -18)
- $6x^2 + 9x - 2x - 3 = 3x(2x + 3) - 1(2x + 3) = (2x + 3)(3x - 1)$

#### 7. Suma y diferencia de cubos

$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

**Ejemplo:** $8x^3 - 27 = (2x)^3 - 3^3 = (2x - 3)(4x^2 + 6x + 9)$

---

## 3.5 Fracciones algebraicas

### Simplificación

Para simplificar, factorizamos numerador y denominador, luego cancelamos factores comunes.

**Ejemplo:**
$$\frac{x^2 - 9}{x^2 + 6x + 9} = \frac{(x+3)(x-3)}{(x+3)^2} = \frac{x-3}{x+3}, \quad x \neq -3$$

### Operaciones con fracciones algebraicas

#### Suma y resta
$$\frac{A}{B} \pm \frac{C}{D} = \frac{AD \pm BC}{BD}$$

**Ejemplo:**
$$\frac{2}{x+1} + \frac{3}{x-1} = \frac{2(x-1) + 3(x+1)}{(x+1)(x-1)} = \frac{5x + 1}{x^2 - 1}$$

#### Multiplicación
$$\frac{A}{B} \cdot \frac{C}{D} = \frac{AC}{BD}$$

#### División
$$\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C} = \frac{AD}{BC}$$

### Fracciones complejas

Una fracción compleja tiene fracciones en el numerador y/o denominador.

**Ejemplo:**
$$\frac{\frac{1}{x} + \frac{1}{y}}{\frac{1}{x} - \frac{1}{y}} = \frac{\frac{y + x}{xy}}{\frac{y - x}{xy}} = \frac{y + x}{y - x}$$

---

## 3.6 Ecuaciones lineales

### Ecuación de primer grado

Una ecuación lineal tiene la forma $ax + b = 0$ con $a \neq 0$.

**Método de solución:**
1. Eliminar paréntesis (distribuir)
2. Eliminar denominadores (multiplicar por MCM)
3. Agrupar términos con variable a un lado
4. Agrupar constantes al otro lado
5. Despejar la variable

**Ejemplo:** $\frac{2x + 1}{3} - \frac{x - 2}{4} = 2$

Multiplicamos por MCM(3, 4) = 12:
$$4(2x + 1) - 3(x - 2) = 24$$
$$8x + 4 - 3x + 6 = 24$$
$$5x + 10 = 24$$
$$5x = 14$$
$$x = \frac{14}{5}$$

### Ecuaciones literales

Despejar una variable específica de una fórmula.

**Ejemplo:** Despejar $r$ de $A = \pi r^2$:
$$r^2 = \frac{A}{\pi}$$
$$r = \sqrt{\frac{A}{\pi}}$$

---

## 3.7 Ecuaciones cuadráticas

### Forma general

$$ax^2 + bx + c = 0, \quad a \neq 0$$

### Métodos de solución

#### 1. Por factorización

Si $ax^2 + bx + c = a(x - r_1)(x - r_2)$, entonces $x = r_1$ o $x = r_2$.

**Ejemplo:** $x^2 - 5x + 6 = 0$
$$(x - 2)(x - 3) = 0$$
$$x = 2 \quad \text{o} \quad x = 3$$

#### 2. Completar el cuadrado

**Ejemplo:** $x^2 + 6x - 7 = 0$
$$x^2 + 6x = 7$$
$$x^2 + 6x + 9 = 7 + 9$$
$$(x + 3)^2 = 16$$
$$x + 3 = \pm 4$$
$$x = 1 \quad \text{o} \quad x = -7$$

#### 3. Fórmula general (cuadrática)

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Ejemplo:** $2x^2 - 3x - 2 = 0$
$$x = \frac{3 \pm \sqrt{9 + 16}}{4} = \frac{3 \pm 5}{4}$$
$$x = 2 \quad \text{o} \quad x = -\frac{1}{2}$$

### Discriminante

El discriminante $\Delta = b^2 - 4ac$ determina la naturaleza de las raíces:

| Discriminante | Naturaleza de las raíces |
|---------------|--------------------------|
| $\Delta > 0$ | Dos raíces reales distintas |
| $\Delta = 0$ | Una raíz real doble |
| $\Delta < 0$ | Dos raíces complejas conjugadas |

---

## 3.8 Sistemas de ecuaciones

### Sistema de dos ecuaciones con dos incógnitas

#### Método de sustitución

1. Despejar una variable de una ecuación
2. Sustituir en la otra ecuación
3. Resolver la ecuación resultante
4. Sustituir para encontrar la otra variable

**Ejemplo:**
$$\begin{cases} 2x + y = 7 \\ x - y = 2 \end{cases}$$

De la segunda: $x = y + 2$

Sustituyendo: $2(y + 2) + y = 7 \Rightarrow 3y + 4 = 7 \Rightarrow y = 1$

Entonces: $x = 1 + 2 = 3$

**Solución:** $(3, 1)$

#### Método de eliminación (reducción)

1. Multiplicar ecuaciones para que los coeficientes de una variable sean opuestos
2. Sumar las ecuaciones para eliminar esa variable
3. Resolver y sustituir

**Ejemplo:**
$$\begin{cases} 3x + 2y = 12 \\ 5x - 2y = 4 \end{cases}$$

Sumando: $8x = 16 \Rightarrow x = 2$

Sustituyendo: $6 + 2y = 12 \Rightarrow y = 3$

#### Método de determinantes (Regla de Cramer)

Para $\begin{cases} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{cases}$

$$\Delta = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1b_2 - a_2b_1$$

$$x = \frac{\Delta_x}{\Delta} = \frac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\Delta}$$

$$y = \frac{\Delta_y}{\Delta} = \frac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\Delta}$$

### Clasificación de sistemas

| Condición | Tipo | Soluciones |
|-----------|------|------------|
| $\Delta \neq 0$ | Determinado | Única solución |
| $\Delta = 0$, $\Delta_x = \Delta_y = 0$ | Indeterminado | Infinitas soluciones |
| $\Delta = 0$, $\Delta_x \neq 0$ o $\Delta_y \neq 0$ | Incompatible | Sin solución |

### Sistemas 3×3

Se resuelven por:
- Eliminación sucesiva
- Regla de Cramer (determinantes 3×3)
- Método de Gauss

---

## 3.9 Desigualdades

### Propiedades de las desigualdades

| Propiedad | Ejemplo |
|-----------|---------|
| Sumar/restar igual en ambos lados | Si $a < b$, entonces $a + c < b + c$ |
| Multiplicar/dividir por positivo | Si $a < b$ y $c > 0$, entonces $ac < bc$ |
| Multiplicar/dividir por negativo | Si $a < b$ y $c < 0$, entonces $ac > bc$ (**se invierte**) |

### Inecuaciones lineales

**Ejemplo:** $3x - 7 < 2x + 5$
$$x < 12$$
**Solución:** $(-\infty, 12)$

### Inecuaciones cuadráticas

**Método:**
1. Llevar a la forma $ax^2 + bx + c \lessgtr 0$
2. Factorizar y encontrar raíces
3. Usar tabla de signos o gráfica

**Ejemplo:** $x^2 - x - 6 > 0$
$$(x - 3)(x + 2) > 0$$

| Intervalo | $(x-3)$ | $(x+2)$ | Producto |
|-----------|---------|---------|----------|
| $x < -2$ | $-$ | $-$ | $+$ |
| $-2 < x < 3$ | $-$ | $+$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ |

**Solución:** $(-\infty, -2) \cup (3, +\infty)$

### Inecuaciones con valor absoluto

| Forma | Equivalencia |
|-------|--------------|
| $\lvert x \rvert < a$ | $-a < x < a$ |
| $\lvert x \rvert > a$ | $x < -a$ o $x > a$ |
| $\lvert x - c \rvert < a$ | $c - a < x < c + a$ |

**Ejemplo:** $|2x - 3| \leq 5$
$$-5 \leq 2x - 3 \leq 5$$
$$-2 \leq 2x \leq 8$$
$$-1 \leq x \leq 4$$

---

## 3.10 Exponentes y radicales algebraicos

### Leyes de exponentes (extensión)

| Ley | Fórmula |
|-----|---------|
| Exponente cero | $a^0 = 1$ ($a \neq 0$) |
| Exponente negativo | $a^{-n} = \frac{1}{a^n}$ |
| Exponente fraccionario | $a^{m/n} = \sqrt[n]{a^m}$ |
| Producto de potencias | $a^m \cdot a^n = a^{m+n}$ |
| Cociente de potencias | $\frac{a^m}{a^n} = a^{m-n}$ |
| Potencia de potencia | $(a^m)^n = a^{mn}$ |

### Simplificación de expresiones con radicales

#### Propiedades de radicales

$$\sqrt[n]{ab} = \sqrt[n]{a} \cdot \sqrt[n]{b}$$
$$\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$$
$$\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$$
$$\sqrt[n]{a^m} = a^{m/n}$$

#### Racionalización

**Monomio:**
$$\frac{a}{\sqrt{b}} = \frac{a\sqrt{b}}{b}$$

**Binomio con raíz:**
$$\frac{a}{b + \sqrt{c}} = \frac{a(b - \sqrt{c})}{b^2 - c}$$

**Ejemplo:**
$$\frac{6}{2 + \sqrt{3}} = \frac{6(2 - \sqrt{3})}{4 - 3} = 6(2 - \sqrt{3}) = 12 - 6\sqrt{3}$$

### Ecuaciones con radicales

**Método:**
1. Aislar el radical
2. Elevar ambos lados a la potencia adecuada
3. Resolver la ecuación resultante
4. **Verificar soluciones** (pueden aparecer soluciones extrañas)

**Ejemplo:** $\sqrt{x + 3} = x - 3$

Elevando al cuadrado:
$$x + 3 = x^2 - 6x + 9$$
$$x^2 - 7x + 6 = 0$$
$$(x - 1)(x - 6) = 0$$
$$x = 1 \text{ o } x = 6$$

**Verificación:**
- $x = 1$: $\sqrt{4} = -2$ ✗ (falso)
- $x = 6$: $\sqrt{9} = 3$ ✓

**Solución:** $x = 6$
