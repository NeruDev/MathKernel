<!--
::METADATA::
type: theory
status: active
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría: Solución Numérica de EDO

---

## 1. Introducción

### 1.1 Problema de Valor Inicial (PVI)

Dado el problema:
$$\frac{dy}{dx} = f(x, y), \quad y(x_0) = y_0$$

Buscamos aproximar $y(x)$ en puntos discretos $x_1, x_2, ..., x_n$.

### 1.2 Existencia y Unicidad

**Teorema de Picard:** Si $f(x,y)$ es continua y Lipschitz en $y$ en una región $R$, entonces existe solución única.

### 1.3 Notación

- $h = x_{n+1} - x_n$: tamaño de paso
- $y_n$: aproximación de $y(x_n)$
- $f_n = f(x_n, y_n)$

---

## 2. Método de Euler

### 2.1 Derivación Geométrica

La pendiente de la recta [tangente](../../../glossary.md#tangente) en $(x_n, y_n)$ es $f(x_n, y_n)$.

Avanzando un paso $h$:
$$y_{n+1} = y_n + h \cdot f(x_n, y_n)$$

### 2.2 Derivación por Serie de Taylor

$$y(x_{n+1}) = y(x_n) + h y'(x_n) + \frac{h^2}{2}y''(\xi)$$

Truncando en primer [orden](../../../glossary.md#orden):
$$y_{n+1} = y_n + h f(x_n, y_n) + O(h^2)$$

### 2.3 Error

- **Error de truncamiento local:** $O(h^2)$
- **Error global acumulado:** $O(h)$

### 2.4 Euler Implícito

$$y_{n+1} = y_n + h \cdot f(x_{n+1}, y_{n+1})$$

Requiere resolver ecuación (posiblemente no lineal) en cada paso.

**Ventaja:** Mayor estabilidad.

---

## 3. Método de Heun (Euler Mejorado)

### 3.1 Idea

Usar promedio de pendientes al inicio y fin del intervalo.

### 3.2 Fórmulas

**Predictor (Euler):**
$$\tilde{y}_{n+1} = y_n + h \cdot f(x_n, y_n)$$

**Corrector (promedio):**
$$y_{n+1} = y_n + \frac{h}{2}\left[f(x_n, y_n) + f(x_{n+1}, \tilde{y}_{n+1})\right]$$

### 3.3 Error

- **Error de truncamiento local:** $O(h^3)$
- **Error global:** $O(h^2)$

---

## 4. Métodos Runge-Kutta

### 4.1 Forma General

$$y_{n+1} = y_n + h \sum_{i=1}^{s} b_i k_i$$

donde cada $k_i$ es una evaluación de $f$ en puntos intermedios.

### 4.2 Runge-Kutta de Orden 2 (RK2)

**Punto medio:**
$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
$$y_{n+1} = y_n + h \cdot k_2$$

**Heun (forma RK2):**
$$k_1 = f(x_n, y_n)$$
$$k_2 = f(x_n + h, y_n + hk_1)$$
$$y_{n+1} = y_n + \frac{h}{2}(k_1 + k_2)$$

### 4.3 Runge-Kutta de Orden 4 (RK4)

El método más utilizado:

$$k_1 = f(x_n, y_n)$$
$$k_2 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_1\right)$$
$$k_3 = f\left(x_n + \frac{h}{2}, y_n + \frac{h}{2}k_2\right)$$
$$k_4 = f(x_n + h, y_n + hk_3)$$
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

### 4.4 Tabla de Butcher

Representación compacta de métodos RK:

**RK4:**
```
0   |
1/2 | 1/2
1/2 | 0   1/2
1   | 0   0   1
----|-------------
    | 1/6 1/3 1/3 1/6
```

### 4.5 Error de RK4

- **Error de truncamiento local:** $O(h^5)$
- **Error global:** $O(h^4)$

---

## 5. Métodos Multipaso

### 5.1 Idea

Usar información de varios pasos anteriores para mayor eficiencia.

### 5.2 Adams-Bashforth (Explícito)

**2 pasos:**
$$y_{n+1} = y_n + \frac{h}{2}(3f_n - f_{n-1})$$

**4 pasos:**
$$y_{n+1} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$

### 5.3 Adams-Moulton (Implícito)

**2 pasos:**
$$y_{n+1} = y_n + \frac{h}{12}(5f_{n+1} + 8f_n - f_{n-1})$$

**4 pasos:**
$$y_{n+1} = y_n + \frac{h}{24}(9f_{n+1} + 19f_n - 5f_{n-1} + f_{n-2})$$

### 5.4 Predictor-Corrector

Combinar Adams-Bashforth (predictor) con Adams-Moulton (corrector):

1. **Predecir:** $\tilde{y}_{n+1}$ con Adams-Bashforth
2. **Evaluar:** $\tilde{f}_{n+1} = f(x_{n+1}, \tilde{y}_{n+1})$
3. **Corregir:** $y_{n+1}$ con Adams-Moulton

### 5.5 Arranque

Los [métodos multipaso](../../../glossary.md#metodos-multipaso) necesitan valores iniciales $y_1, y_2, ...$

**Solución:** Usar RK4 para los primeros pasos.

---

## 6. Sistemas de EDO

### 6.1 Forma Vectorial

Sistema de $m$ ecuaciones:
$$\frac{d\mathbf{y}}{dx} = \mathbf{f}(x, \mathbf{y}), \quad \mathbf{y}(x_0) = \mathbf{y}_0$$

donde $\mathbf{y} = (y_1, y_2, ..., y_m)^T$

### 6.2 Euler para Sistemas

$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \cdot \mathbf{f}(x_n, \mathbf{y}_n)$$

Componente a componente:
$$y_{i,n+1} = y_{i,n} + h \cdot f_i(x_n, y_{1,n}, ..., y_{m,n})$$

### 6.3 Reducción de Orden

[EDO](../../../glossary.md#edo) de [orden](../../../glossary.md#orden) $m$:
$$y^{(m)} = g(x, y, y', ..., y^{(m-1)})$$

Se convierte en sistema introduciendo:
$$z_1 = y, \quad z_2 = y', \quad ..., \quad z_m = y^{(m-1)}$$

**Ejemplo:** $y'' + 3y' + 2y = 0$

Sistema:
$$z_1' = z_2$$
$$z_2' = -3z_2 - 2z_1$$

---

## 7. Análisis de Error

### 7.1 Error de Truncamiento Local

Error en un solo paso, asumiendo datos exactos.

| Método | Error local |
|--------|-------------|
| Euler | $O(h^2)$ |
| Heun/RK2 | $O(h^3)$ |
| RK4 | $O(h^5)$ |

### 7.2 Error Global

Error acumulado después de $N = \frac{x_f - x_0}{h}$ pasos.

$$E_{global} \approx N \cdot E_{local} = \frac{x_f - x_0}{h} \cdot O(h^{p+1}) = O(h^p)$$

### 7.3 Estimación del Error

**Comparación de pasos:**

Si $y_h$ es la solución con paso $h$ y $y_{h/2}$ con paso $h/2$:
$$E \approx \frac{y_{h/2} - y_h}{2^p - 1}$$

donde $p$ es el orden del método.

---

## 8. Estabilidad

### 8.1 Ecuación de Prueba

$$y' = \lambda y, \quad \lambda < 0$$

Solución exacta: $y(x) = y_0 e^{\lambda x} \to 0$

### 8.2 Análisis para Euler Explícito

$$y_{n+1} = y_n + h\lambda y_n = (1 + h\lambda)y_n$$

Para [convergencia](../../../glossary.md#convergencia) a cero: $|1 + h\lambda| < 1$

**Región de estabilidad:** $-2 < h\lambda < 0$

**Restricción:** $h < \frac{2}{|\lambda|}$

### 8.3 Euler Implícito

$$y_{n+1} = y_n + h\lambda y_{n+1}$$
$$y_{n+1} = \frac{y_n}{1 - h\lambda}$$

Para $\lambda < 0$: $\left|\frac{1}{1-h\lambda}\right| < 1$ siempre.

**Incondicionalmente estable.**

### 8.4 EDO Rígidas (Stiff)

Sistema con componentes de escalas temporales muy diferentes.

**Ejemplo:** $\lambda_1 = -1$, $\lambda_2 = -1000$

Métodos explícitos: $h$ limitado por componente rápida.

**Solución:** Usar métodos implícitos.

---

## 9. Control Adaptativo del Paso

### 9.1 Idea

Ajustar $h$ para mantener error dentro de tolerancia.

### 9.2 Runge-Kutta-Fehlberg (RKF45)

Calcula simultáneamente aproximaciones de orden 4 y 5:
$$\text{Error} \approx |y_5 - y_4|$$

**Ajuste:**
$$h_{nuevo} = h \cdot \left(\frac{\text{tol}}{\text{Error}}\right)^{1/5}$$

### 9.3 Criterio

- Si Error > tol: rechazar paso, reducir $h$
- Si Error < tol: aceptar paso, posiblemente aumentar $h$
