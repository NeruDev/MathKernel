<!--
::METADATA::
type: theory
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría: Ecuaciones Diferenciales de Segundo Orden

---

## 2.1 Ecuaciones Homogéneas con Coeficientes Constantes

### Forma General
$$ay'' + by' + cy = 0$$

donde $a, b, c$ son constantes con $a \neq 0$.

### Ecuación Característica

Suponiendo solución de la forma $y = e^{rx}$:

$$ar^2 + br + c = 0$$

Las raíces determinan la forma de la solución.

### Caso 1: Raíces Reales Distintas ($\Delta > 0$)

Si $r_1 \neq r_2$ son las raíces:

$$\boxed{y_h = C_1 e^{r_1 x} + C_2 e^{r_2 x}}$$

> **Ejemplo:** $y'' - 5y' + 6y = 0$
> 
> Ecuación característica: $r^2 - 5r + 6 = 0$
> 
> $(r-2)(r-3) = 0 \Rightarrow r_1 = 2, r_2 = 3$
> 
> **Solución:** $y = C_1 e^{2x} + C_2 e^{3x}$

### Caso 2: Raíces Reales Repetidas ($\Delta = 0$)

Si $r_1 = r_2 = r$:

$$\boxed{y_h = (C_1 + C_2 x)e^{rx} = C_1 e^{rx} + C_2 x e^{rx}}$$

> **Ejemplo:** $y'' - 4y' + 4y = 0$
> 
> Ecuación característica: $r^2 - 4r + 4 = 0$
> 
> $(r-2)^2 = 0 \Rightarrow r = 2$ (doble)
> 
> **Solución:** $y = (C_1 + C_2 x)e^{2x}$

### Caso 3: Raíces Complejas Conjugadas ($\Delta < 0$)

Si $r = \alpha \pm \beta i$:

$$\boxed{y_h = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)}$$

Forma alternativa con amplitud y fase:

$$y_h = Ae^{\alpha x}\cos(\beta x - \phi)$$

> **Ejemplo:** $y'' + 2y' + 5y = 0$
> 
> Ecuación característica: $r^2 + 2r + 5 = 0$
> 
> $r = \frac{-2 \pm \sqrt{4-20}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$
> 
> $\alpha = -1$, $\beta = 2$
> 
> **Solución:** $y = e^{-x}(C_1 \cos 2x + C_2 \sin 2x)$

---

## 2.2 Ecuaciones No Homogéneas

### Forma General
$$ay'' + by' + cy = f(x)$$

donde $f(x) \neq 0$ es el **término forzante**.

### Teorema de la Solución General

La [solución general](../../../glossary.md#solucion-general) de la ecuación no homogénea es:

$$\boxed{y = y_h + y_p}$$

donde:
- $y_h$ = [solución general](../../../glossary.md#solucion-general) de la [ecuación homogénea](../../../glossary.md#ecuacion-homogenea) asociada
- $y_p$ = una [solución particular](../../../glossary.md#solucion-particular) de la ecuación no homogénea

### Principio de Superposición

Si $y_{p1}$ es [solución particular](../../../glossary.md#solucion-particular) para $f_1(x)$ y $y_{p2}$ para $f_2(x)$, entonces:

$$y_p = y_{p1} + y_{p2}$$

es solución particular para $f_1(x) + f_2(x)$.

---

## 2.3 Método de Coeficientes Indeterminados

### Aplicabilidad

El método funciona cuando $f(x)$ es combinación de:
- Polinomios: $x^n$
- Exponenciales: $e^{ax}$
- Senos y cosenos: $\sin bx$, $\cos bx$
- Productos de los anteriores

### Tabla de Soluciones Particulares

| Término forzante $f(x)$ | Forma de $y_p$ |
|------------------------|----------------|
| $k$ (constante) | $A$ |
| $kx^n$ | $A_n x^n + A_{n-1}x^{n-1} + \cdots + A_1 x + A_0$ |
| $ke^{ax}$ | $Ae^{ax}$ |
| $k\cos bx$ o $k\sin bx$ | $A\cos bx + B\sin bx$ |
| $ke^{ax}\cos bx$ o $ke^{ax}\sin bx$ | $e^{ax}(A\cos bx + B\sin bx)$ |
| $kx^n e^{ax}$ | $(A_n x^n + \cdots + A_0)e^{ax}$ |

### Regla de Modificación

**Si algún término de $y_p$ duplica una solución de $y_h$:**

Multiplicar $y_p$ por $x$ (o por $x^2$ si ya hay multiplicación por $x$).

> **Ejemplo 1:** $y'' - 3y' + 2y = e^x$
> 
> Homogénea: $r^2 - 3r + 2 = 0 \Rightarrow r = 1, 2$
> 
> $y_h = C_1 e^x + C_2 e^{2x}$
> 
> Como $e^x$ está en $y_h$, usamos $y_p = Axe^x$
> 
> $y_p' = Ae^x + Axe^x = Ae^x(1+x)$
> 
> $y_p'' = Ae^x(2+x)$
> 
> Sustituyendo: $Ae^x(2+x) - 3Ae^x(1+x) + 2Axe^x = e^x$
> 
> $Ae^x[(2+x) - 3(1+x) + 2x] = e^x$
> 
> $Ae^x[-1] = e^x \Rightarrow A = -1$
> 
> **$y_p = -xe^x$**

> **Ejemplo 2:** $y'' + 4y = \cos 2x$
> 
> Homogénea: $r^2 + 4 = 0 \Rightarrow r = \pm 2i$
> 
> $y_h = C_1\cos 2x + C_2\sin 2x$
> 
> Como $\cos 2x$ está en $y_h$, usamos $y_p = x(A\cos 2x + B\sin 2x)$
> 
> Derivando y sustituyendo... $A = 0, B = \frac{1}{4}$
> 
> **$y_p = \frac{x}{4}\sin 2x$**

---

## 2.4 Variación de Parámetros

### Ventaja del Método

Funciona para **cualquier** $f(x)$, no solo para las formas especiales del método de coeficientes indeterminados.

### Procedimiento

Dada $y'' + P(x)y' + Q(x)y = f(x)$ con solución homogénea:

$$y_h = C_1 y_1(x) + C_2 y_2(x)$$

Buscamos $y_p = u_1(x)y_1(x) + u_2(x)y_2(x)$

### Wronskiano

$$W(y_1, y_2) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1 y_2' - y_2 y_1'$$

### Fórmulas para $u_1'$ y $u_2'$

$$\boxed{u_1' = -\frac{y_2 f(x)}{W}, \quad u_2' = \frac{y_1 f(x)}{W}}$$

Integrando:

$$u_1 = -\int \frac{y_2 f(x)}{W}\,dx, \quad u_2 = \int \frac{y_1 f(x)}{W}\,dx$$

### Fórmula Compacta

$$\boxed{y_p = -y_1 \int \frac{y_2 f}{W}\,dx + y_2 \int \frac{y_1 f}{W}\,dx}$$

> **Ejemplo:** $y'' + y = \sec x$
> 
> Homogénea: $y_h = C_1\cos x + C_2\sin x$
> 
> $y_1 = \cos x$, $y_2 = \sin x$
> 
> $W = \cos x \cdot \cos x - \sin x \cdot (-\sin x) = \cos^2 x + \sin^2 x = 1$
> 
> $u_1' = -\sin x \cdot \sec x = -\tan x$
> 
> $u_1 = \int -\tan x\,dx = \ln|\cos x|$
> 
> $u_2' = \cos x \cdot \sec x = 1$
> 
> $u_2 = x$
> 
> **$y_p = \cos x \ln|\cos x| + x\sin x$**

---

## 2.5 Ecuación de Cauchy-Euler

### Forma Estándar

$$ax^2y'' + bxy' + cy = 0$$

Los coeficientes son **potencias de $x$** que coinciden con el [orden](../../../glossary.md#orden) de la [derivada](../../../glossary.md#derivada).

### Método de Solución

Suponemos $y = x^m$ para $x > 0$:

$$y' = mx^{m-1}, \quad y'' = m(m-1)x^{m-2}$$

Sustituyendo:

$$ax^2 \cdot m(m-1)x^{m-2} + bx \cdot mx^{m-1} + cx^m = 0$$

$$x^m[am(m-1) + bm + c] = 0$$

### Ecuación Auxiliar

$$\boxed{am(m-1) + bm + c = 0}$$

o equivalentemente: $am^2 + (b-a)m + c = 0$

### Casos de Solución

**Caso 1:** Raíces reales distintas $m_1 \neq m_2$

$$y = C_1 x^{m_1} + C_2 x^{m_2}$$

**Caso 2:** Raíces repetidas $m_1 = m_2 = m$

$$y = (C_1 + C_2 \ln x)x^m$$

**Caso 3:** Raíces complejas $m = \alpha \pm \beta i$

$$y = x^\alpha[C_1 \cos(\beta \ln x) + C_2 \sin(\beta \ln x)]$$

> **Ejemplo:** $x^2y'' - 2xy' - 4y = 0$
> 
> Ecuación auxiliar: $m(m-1) - 2m - 4 = 0$
> 
> $m^2 - 3m - 4 = 0$
> 
> $(m-4)(m+1) = 0 \Rightarrow m = 4, -1$
> 
> **Solución:** $y = C_1 x^4 + C_2 x^{-1}$

### Método Alternativo: Cambio de Variable

La [sustitución](../../../glossary.md#sustitucion) $x = e^t$ (o $t = \ln x$) transforma la ecuación de Cauchy-Euler en una ecuación con coeficientes constantes.

---

## 2.6 Aplicaciones

### Oscilador Armónico Amortiguado

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

donde:
- $m$ = masa
- $c$ = coeficiente de amortiguamiento
- $k$ = constante del resorte
- $F(t)$ = fuerza externa

**Ecuación característica:** $mr^2 + cr + k = 0$

$r = \frac{-c \pm \sqrt{c^2 - 4mk}}{2m}$

### Tipos de Amortiguamiento

**Subamortiguado** ($c^2 < 4mk$): Oscilaciones decrecientes

$$x(t) = e^{-\gamma t}(A\cos\omega_d t + B\sin\omega_d t)$$

donde $\gamma = \frac{c}{2m}$ y $\omega_d = \frac{\sqrt{4mk - c^2}}{2m}$

**Críticamente amortiguado** ($c^2 = 4mk$): Sin oscilaciones, regreso más rápido

$$x(t) = (A + Bt)e^{-\gamma t}$$

**Sobreamortiguado** ($c^2 > 4mk$): Sin oscilaciones, regreso lento

$$x(t) = Ae^{r_1 t} + Be^{r_2 t}$$

### Frecuencias Importantes

- **Frecuencia natural:** $\omega_0 = \sqrt{k/m}$
- **Frecuencia amortiguada:** $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$
- **Factor de amortiguamiento:** $\zeta = \frac{c}{2\sqrt{mk}}$

### Circuito RLC en Serie

$$L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = E(t)$$

donde:
- $L$ = inductancia (H)
- $R$ = resistencia (Ω)
- $C$ = capacitancia (F)
- $q$ = carga (C)
- $E(t)$ = fem aplicada (V)

**Analogía mecánica-eléctrica:**

| Mecánico | Eléctrico |
|----------|-----------|
| $m$ (masa) | $L$ (inductancia) |
| $c$ (amortiguamiento) | $R$ (resistencia) |
| $k$ (rigidez) | $1/C$ (elastancia) |
| $x$ (desplazamiento) | $q$ (carga) |
| $F$ (fuerza) | $E$ (fem) |

### Resonancia

Cuando la frecuencia de la fuerza externa $\omega$ iguala la frecuencia natural $\omega_0$:

**Sin amortiguamiento:** La amplitud crece sin [límite](../../../glossary.md#limite) ([resonancia](../../../glossary.md#resonancia) pura)

**Con amortiguamiento:** La amplitud alcanza un máximo finito en:

$$\omega_r = \sqrt{\omega_0^2 - 2\gamma^2}$$
