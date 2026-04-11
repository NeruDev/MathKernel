<!--
::METADATA::
type: theory
topic_id: cv-02-curvas-parametricas-polares
file_id: CV-02-Teoria-Curvas
status: stable
audience: student
requires: [CD-02-[Derivadas](../../../glossary.md#derivadas), FUN-05-Trigonometria]
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría — Curvas planas, ecuaciones paramétricas y coordenadas polares

---

## 2.1 Ecuaciones paramétricas

### Concepto intuitivo
Una **curva paramétrica** describe la posición de un punto en el plano como [función](../../../glossary.md#funcion) de un parámetro $t$ (que frecuentemente representa el tiempo). En lugar de expresar $y$ directamente en función de $x$, ambas coordenadas dependen de $t$.

### Definición formal
Una **curva paramétrica plana** es el conjunto de puntos $(x, y)$ donde:
$$x = x(t), \quad y = y(t), \quad t \in I$$

siendo $I$ un intervalo (abierto, cerrado o infinito).

### Orientación
La **orientación** de la curva es el sentido en que se recorre al aumentar $t$. Se indica con flechas sobre la curva.

### Eliminación del parámetro
Para obtener la ecuación cartesiana:
1. Despeja $t$ de una de las ecuaciones
2. Sustituye en la otra
3. Simplifica

**Ejemplo**: Si $x = \cos t$, $y = \sin t$, entonces $x^2 + y^2 = 1$ (círculo unitario).

### Curvas paramétricas clásicas

| Curva | Parametrización | Rango |
|-------|-----------------|-------|
| Circunferencia | $x = a\cos t$, $y = a\sin t$ | $t \in [0, 2\pi]$ |
| Elipse | $x = a\cos t$, $y = b\sin t$ | $t \in [0, 2\pi]$ |
| Cicloide | $x = a(t - \sin t)$, $y = a(1 - \cos t)$ | $t \in \mathbb{R}$ |
| Astroide | $x = a\cos^3 t$, $y = a\sin^3 t$ | $t \in [0, 2\pi]$ |

---

## 2.2 Cálculo con curvas paramétricas

### Tangentes a curvas paramétricas

La **pendiente de la recta [tangente](../../../glossary.md#tangente)** en un punto de la curva es:
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{y'(t)}{x'(t)}$$

siempre que $x'(t) \neq 0$.

**Segunda [derivada](../../../glossary.md#derivada)** (para [concavidad](../../../glossary.md#concavidad)):
$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$$

### Clasificación de tangentes

| Condición | Tipo de [tangente](../../../glossary.md#tangente) |
|-----------|------------------|
| $y'(t) = 0$, $x'(t) \neq 0$ | Horizontal |
| $x'(t) = 0$, $y'(t) \neq 0$ | Vertical |
| $x'(t) = 0$, $y'(t) = 0$ | Punto singular (análisis adicional) |

### Longitud de arco

La longitud de una curva paramétrica de $t = a$ a $t = b$ es:
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\, dt = \int_a^b \sqrt{[x'(t)]^2 + [y'(t)]^2}\, dt$$

**Interpretación**: Se integra la "rapidez" con que se recorre la curva.

### Función longitud de arco

$$s(t) = \int_a^t \sqrt{[x'(u)]^2 + [y'(u)]^2}\, du$$

Cumple: $\frac{ds}{dt} = \sqrt{[x'(t)]^2 + [y'(t)]^2}$

### Área bajo una curva paramétrica

Si la curva no se auto-intersecta y $y(t) \geq 0$ en el intervalo:
$$A = \int_a^b y(t) \cdot x'(t)\, dt$$

o equivalentemente:
$$A = -\int_a^b x(t) \cdot y'(t)\, dt$$

**Nota**: El signo depende de la orientación; tomar valor absoluto si es [necesario](../../../glossary.md#necesario).

### Área encerrada por una curva cerrada

Para una curva cerrada recorrida en sentido antihorario:
$$A = \frac{1}{2} \int_a^b \left[ x(t)y'(t) - y(t)x'(t) \right] dt$$

---

## 2.3 Coordenadas polares

### Sistema de coordenadas polares

Un punto en el plano se describe por:
- $r$: distancia al origen (polo)
- $\theta$: ángulo medido desde el eje polar (eje $x$ positivo)

### Conversión entre sistemas

| Polar → Cartesianas | Cartesianas → Polares |
|---------------------|----------------------|
| $x = r\cos\theta$ | $r = \sqrt{x^2 + y^2}$ |
| $y = r\sin\theta$ | $\theta = \arctan\left(\frac{y}{x}\right)$ |

**Nota**: Para $\theta$, considerar el cuadrante correcto.

### Representación de puntos

Un mismo punto puede tener múltiples representaciones:
- $(r, \theta)$ y $(r, \theta + 2\pi n)$ representan el mismo punto
- $(-r, \theta)$ y $(r, \theta + \pi)$ representan el mismo punto

### Curvas en coordenadas polares

Una **curva polar** se define como $r = f(\theta)$ o implícitamente $F(r, \theta) = 0$.

### Curvas polares clásicas

| Nombre | Ecuación | Características |
|--------|----------|-----------------|
| Círculo (centro en origen) | $r = a$ | Radio $a$ |
| Círculo (pasa por origen) | $r = a\cos\theta$ o $r = a\sin\theta$ | Diámetro $a$ |
| Cardioide | $r = a(1 \pm \cos\theta)$ o $r = a(1 \pm \sin\theta)$ | Forma de corazón |
| Limaçon | $r = a + b\cos\theta$ | Con/sin lazo según $\lvert a/b \rvert$ |
| Rosa de $n$ pétalos | $r = a\cos(n\theta)$ o $r = a\sin(n\theta)$ | $n$ pétalos si $n$ impar, $2n$ si par |
| Lemniscata | $r^2 = a^2\cos(2\theta)$ | Forma de $\infty$ |
| Espiral de Arquímedes | $r = a\theta$ | Espiral uniforme |
| Espiral logarítmica | $r = ae^{b\theta}$ | Espiral equiangular |

### Simetrías en polares

| Prueba | Simetría |
|--------|----------|
| $r(\theta) = r(-\theta)$ | Eje polar (eje $x$) |
| $r(\theta) = r(\pi - \theta)$ | Recta $\theta = \pi/2$ (eje $y$) |
| $r(\theta) = r(\theta + \pi)$ | Respecto al polo (origen) |

---

## 2.4 Cálculo con coordenadas polares

### Tangentes a curvas polares

Expresando $x = r\cos\theta$ y $y = r\sin\theta$:

$$\frac{dy}{dx} = \frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}$$

### Tangentes en el polo

En el polo ($r = 0$), si $r = f(\theta)$ y $f(\theta_0) = 0$ pero $f'(\theta_0) \neq 0$, la recta $\theta = \theta_0$ es tangente.

### Longitud de arco en polares

$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\, d\theta$$

**Derivación**: Se obtiene de la fórmula paramétrica con $x = r\cos\theta$, $y = r\sin\theta$.

### Área en coordenadas polares

El área encerrada por la curva $r = f(\theta)$ entre $\theta = \alpha$ y $\theta = \beta$ es:
$$A = \frac{1}{2}\int_\alpha^\beta r^2\, d\theta = \frac{1}{2}\int_\alpha^\beta [f(\theta)]^2\, d\theta$$

**Interpretación geométrica**: Se suman sectores circulares infinitesimales de área $\frac{1}{2}r^2 d\theta$.

### Área entre dos curvas polares

Si $r_{\text{int}} \leq r_{\text{ext}}$ para $\theta \in [\alpha, \beta]$:
$$A = \frac{1}{2}\int_\alpha^\beta \left[ r_{\text{ext}}^2 - r_{\text{int}}^2 \right] d\theta$$

**Importante**: Identificar correctamente los [límites](../../../glossary.md#limites) de integración encontrando los puntos de intersección.

### Intersección de curvas polares

Para encontrar intersecciones de $r = f(\theta)$ y $r = g(\theta)$:
1. Resolver $f(\theta) = g(\theta)$
2. Verificar intersecciones en el polo: ¿existen $\theta_1, \theta_2$ tales que $f(\theta_1) = 0$ y $g(\theta_2) = 0$?

---

## 2.5 Secciones cónicas en polares

### Forma general

Una cónica con foco en el origen y directriz perpendicular al eje polar:
$$r = \frac{ed}{1 \pm e\cos\theta} \quad \text{o} \quad r = \frac{ed}{1 \pm e\sin\theta}$$

donde:
- $e$ = excentricidad
- $d$ = distancia del foco a la directriz

### Clasificación por excentricidad

| Excentricidad | Cónica |
|---------------|--------|
| $e < 1$ | Elipse |
| $e = 1$ | Parábola |
| $e > 1$ | Hipérbola |

### Orientación según el signo

| Ecuación | Directriz | Apertura |
|----------|-----------|----------|
| $r = \frac{ed}{1 + e\cos\theta}$ | A la derecha | Hacia la izquierda |
| $r = \frac{ed}{1 - e\cos\theta}$ | A la izquierda | Hacia la derecha |
| $r = \frac{ed}{1 + e\sin\theta}$ | Arriba | Hacia abajo |
| $r = \frac{ed}{1 - e\sin\theta}$ | Abajo | Hacia arriba |

---

## 2.6 Aplicaciones

### Cinemática en el plano

Si la posición de una partícula es $(x(t), y(t))$:

| Cantidad | Fórmula |
|----------|---------|
| **Vector posición** | $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ |
| **Velocidad** | $\mathbf{v}(t) = \langle x'(t), y'(t) \rangle$ |
| **Rapidez** | $v = \sqrt{[x'(t)]^2 + [y'(t)]^2}$ |
| **Aceleración** | $\mathbf{a}(t) = \langle x''(t), y''(t) \rangle$ |

### Distancia recorrida

$$s = \int_{t_1}^{t_2} \sqrt{[x'(t)]^2 + [y'(t)]^2}\, dt$$

### Área de superficies de revolución

Para una curva paramétrica rotada alrededor del eje $x$:
$$S = 2\pi \int_a^b y(t) \sqrt{[x'(t)]^2 + [y'(t)]^2}\, dt$$

Alrededor del eje $y$:
$$S = 2\pi \int_a^b x(t) \sqrt{[x'(t)]^2 + [y'(t)]^2}\, dt$$

---

<!--
IA: Esta teoría cubre los subtemas principales de curvas paramétricas y polares.
Usa las definiciones y fórmulas aquí como referencia canónica.
Al generar problemas, asegura [dominio](../../../glossary.md#dominio) de cada sección antes de avanzar.
file_id: CV-02-Teoria-Curvas
-->
