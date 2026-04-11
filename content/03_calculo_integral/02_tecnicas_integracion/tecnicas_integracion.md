<!--
HUMANO:
Teoría de [técnicas de integración](../../../glossary.md#tecnicas-de-integracion).

IA:
Desarrolla cada técnica con ejemplos.

---
content_type: theory
expected_output:
  default: markdown
audience: self-study
---
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría de Técnicas de Integración

---

## 2.1 Sustitución (Cambio de Variable)

### Teorema Fundamental
Si $u = g(x)$ es una [función](../../../glossary.md#funcion) diferenciable y $f$ es continua en el rango de $g$, entonces:

$$\boxed{\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du}$$

### Procedimiento
1. Identificar $u = g(x)$
2. Calcular $du = g'(x) \, dx$
3. Sustituir todo en términos de $u$
4. Integrar
5. Regresar a variable original

### Ejemplo
$$\int 2x \cos(x^2) \, dx$$

Sea $u = x^2$, entonces $du = 2x \, dx$

$$= \int \cos u \, du = \sin u + C = \sin(x^2) + C$$

---

## 2.2 Integración por Partes

### Fórmula
Si $u$ y $v$ son funciones diferenciables:

$$\boxed{\int u \, dv = uv - \int v \, du}$$

### Regla LIATE
Para elegir $u$ (en [orden](../../../glossary.md#orden) de preferencia):
1. **L**ogarítmicas: $\ln x$, $\log x$
2. **I**nversas trigonométricas: $\arctan x$, $\arcsin x$
3. **A**lgebraicas: $x^n$, polinomios
4. **T**rigonométricas: $\sin x$, $\cos x$
5. **E**xponenciales: $e^x$, $a^x$

### Ejemplo
$$\int x e^x \, dx$$

Sea $u = x$ (algebraica), $dv = e^x dx$
Entonces $du = dx$, $v = e^x$

$$= xe^x - \int e^x \, dx = xe^x - e^x + C = e^x(x-1) + C$$

### Casos Especiales

#### Partes cíclicas
$$\int e^x \sin x \, dx$$

Aplicando partes dos veces y resolviendo algebraicamente:
$$\int e^x \sin x \, dx = \frac{e^x(\sin x - \cos x)}{2} + C$$

#### Fórmula tabular
Para $\int x^n e^x \, dx$: derivar $x^n$ repetidamente, integrar $e^x$ repetidamente.

---

## 2.3 Integrales Trigonométricas

### Tipo 1: $\int \sin^m x \cos^n x \, dx$

**Caso A: $m$ impar**
Separar un factor $\sin x$, convertir resto a $\cos x$ usando $\sin^2 x = 1 - \cos^2 x$, sustituir $u = \cos x$.

**Caso B: $n$ impar**
Separar un factor $\cos x$, convertir resto a $\sin x$, sustituir $u = \sin x$.

**Caso C: Ambos pares**
Usar identidades de reducción:
$$\sin^2 x = \frac{1 - \cos 2x}{2}, \quad \cos^2 x = \frac{1 + \cos 2x}{2}$$

### Tipo 2: $\int \tan^m x \sec^n x \, dx$

**Caso A: $n$ par**
Separar $\sec^2 x$, convertir resto a $\tan x$ usando $\sec^2 x = 1 + \tan^2 x$, sustituir $u = \tan x$.

**Caso B: $m$ impar**
Separar $\sec x \tan x$, convertir resto a $\sec x$, sustituir $u = \sec x$.

### Integrales de Referencia
$$\int \tan x \, dx = -\ln\lvert\cos x\rvert + C = \ln\lvert\sec x\rvert + C$$
$$\int \sec x \, dx = \ln\lvert\sec x + \tan x\rvert + C$$

---

## 2.4 Sustitución Trigonométrica

### Tabla de Sustituciones

| Expresión | [Sustitución](../../../glossary.md#sustitucion-trigonometrica) | Identidad usada |
|-----------|---------------|-----------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

---

## 2.5 Fracciones Parciales

### Requisito
El grado del numerador debe ser [menor](../../../glossary.md#menor) que el grado del denominador. Si no, hacer división de polinomios primero.

### Tipos de Descomposición

#### Factor lineal no repetido: $(ax + b)$
$$\frac{P(x)}{(ax+b)Q(x)} = \frac{A}{ax+b} + \frac{\text{resto}}{Q(x)}$$

#### Factor lineal repetido: $(ax + b)^n$
$$\frac{P(x)}{(ax+b)^n} = \frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \cdots + \frac{A_n}{(ax+b)^n}$$

#### Factor cuadrático irreducible: $(ax^2 + bx + c)$
$$\frac{P(x)}{ax^2+bx+c} = \frac{Ax + B}{ax^2+bx+c}$$

#### Factor cuadrático repetido: $(ax^2 + bx + c)^n$
$$\frac{A_1x + B_1}{ax^2+bx+c} + \frac{A_2x + B_2}{(ax^2+bx+c)^2} + \cdots$$

### Ejemplo
$$\int \frac{x+5}{(x-1)(x+2)} \, dx$$

Descomposición:
$$\frac{x+5}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$$

$x + 5 = A(x+2) + B(x-1)$

$x = 1$: $6 = 3A \Rightarrow A = 2$
$x = -2$: $3 = -3B \Rightarrow B = -1$

$$= \int \left(\frac{2}{x-1} - \frac{1}{x+2}\right) dx = 2\ln\lvert x-1\rvert - \ln\lvert x+2\rvert + C$$

---

## 2.6 Completar el Cuadrado

### Uso
Para integrales con expresiones cuadráticas $ax^2 + bx + c$.

### Fórmula
$$ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

### Ejemplo
$$\int \frac{dx}{x^2 + 4x + 5}$$

Completamos: $x^2 + 4x + 5 = (x+2)^2 + 1$

$$= \int \frac{dx}{(x+2)^2 + 1} = \arctan(x+2) + C$$

---

## 2.7 Integrales con Radicales

### Sustitución racional
Para $\sqrt[n]{ax+b}$, usar $u = \sqrt[n]{ax+b}$, entonces $u^n = ax+b$

### Ejemplo
$$\int \frac{dx}{\sqrt{x} + 1}$$

Sea $u = \sqrt{x}$, entonces $x = u^2$, $dx = 2u \, du$

$$= \int \frac{2u \, du}{u + 1} = 2\int \frac{u}{u+1} du = 2\int \left(1 - \frac{1}{u+1}\right) du$$

$$= 2(u - \ln\lvert u+1\rvert) + C = 2\sqrt{x} - 2\ln(\sqrt{x}+1) + C$$

---

## 2.8 Estrategias de Integración

### Árbol de Decisión

1. **¿Es integral básica?** → Usar tabla de fórmulas

2. **¿Hay [composición](../../../glossary.md#composicion) de funciones?** → Intentar [sustitución](../../../glossary.md#sustitucion)

3. **¿Es producto de funciones diferentes?** → Intentar partes

4. **¿Hay funciones trigonométricas?**
   - Potencias → Identidades trigonométricas
   - $\sqrt{a^2 \pm x^2}$ → [Sustitución trigonométrica](../../../glossary.md#sustitucion-trigonometrica)

5. **¿Es fracción racional?** → [Fracciones parciales](../../../glossary.md#fracciones-parciales)

6. **¿Hay radicales?** → Sustitución racional o trigonométrica

7. **¿Ninguna funciona?** → Probar manipulación algebraica
