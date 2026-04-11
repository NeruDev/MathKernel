<!--
::METADATA::
type: theory
topic_id: 01-integral-indefinida
file_id: CI-01-Teoria-Integral-Indefinida
status: stable
audience: student
-->


> 🏠 **Navegación:** [← Volver al Índice Principal](../../../glossary.md)

---

# Teoría de la Integral Indefinida

---

## 1.1 Concepto de Antiderivada

### Definición

Una [función](../../../glossary.md#funcion) $F(x)$ es una **[antiderivada](../../../glossary.md#antiderivada)** (o [primitiva](../../../glossary.md#primitiva)) de $f(x)$ en un intervalo $I$ si:

$$F'(x) = f(x) \quad \text{para todo } x \in I$$

### Ejemplo
Si $F(x) = x^3$, entonces $F'(x) = 3x^2$, por lo que $F(x) = x^3$ es una [antiderivada](../../../glossary.md#antiderivada) de $f(x) = 3x^2$.

### Observación Importante
Si $F(x)$ es una antiderivada de $f(x)$, entonces $F(x) + C$ también lo es para cualquier constante $C$, porque:
$$(F(x) + C)' = F'(x) + 0 = f(x)$$

---

## 1.2 Notación y Constante de Integración

### Notación
La **[integral indefinida](../../../glossary.md#integral-indefinida)** de $f(x)$ se denota:

$$\int f(x) \, dx = F(x) + C$$

donde:
- $\int$ es el símbolo de integración
- $f(x)$ es el **integrando**
- $dx$ indica la variable de integración
- $F(x)$ es una antiderivada de $f(x)$
- $C$ es la **[constante de integración](../../../glossary.md#constante-de-integracion)**

### La Constante de Integración
La constante $C$ representa que hay infinitas antiderivadas que difieren por una constante.

**Teorema:** Si $F(x)$ y $G(x)$ son antiderivadas de $f(x)$ en un intervalo, entonces $F(x) - G(x) = C$ para alguna constante $C$.

---

## 1.3 Integrales de Funciones Algebraicas

### Regla de la Potencia

$$\boxed{\int x^n \, dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1}$$

**Verificación:** $\frac{d}{dx}\left(\frac{x^{n+1}}{n+1}\right) = \frac{(n+1)x^n}{n+1} = x^n$ ✓

### Casos Especiales

| Integral | Resultado |
|----------|-----------|
| $\int dx$ | $x + C$ |
| $\int x \, dx$ | $\frac{x^2}{2} + C$ |
| $\int x^2 \, dx$ | $\frac{x^3}{3} + C$ |
| $\int \sqrt{x} \, dx$ | $\frac{2x^{3/2}}{3} + C$ |
| $\int \frac{1}{x^2} \, dx$ | $-\frac{1}{x} + C$ |
| $\int \frac{1}{\sqrt{x}} \, dx$ | $2\sqrt{x} + C$ |

### Integral de $1/x$

$$\boxed{\int \frac{1}{x} \, dx = \ln\lvert x \rvert + C}$$

El valor absoluto es [necesario](../../../glossary.md#necesario) porque $\ln x$ solo está definido para $x > 0$.

---

## 1.4 Integrales de Funciones Exponenciales

### Exponencial Natural

$$\boxed{\int e^x \, dx = e^x + C}$$

### Exponencial General

$$\boxed{\int a^x \, dx = \frac{a^x}{\ln a} + C, \quad a > 0, a \neq 1}$$

**Verificación:** $\frac{d}{dx}\left(\frac{a^x}{\ln a}\right) = \frac{a^x \ln a}{\ln a} = a^x$ ✓

### Forma Generalizada

$$\int e^{kx} \, dx = \frac{e^{kx}}{k} + C$$

---

## 1.5 Integrales de Funciones Logarítmicas

La integral de $\ln x$ requiere [integración por partes](../../../glossary.md#integracion-por-partes) (ver [Técnicas de Integración](../../../glossary.md#tecnicas-de-integracion)):

$$\int \ln x \, dx = x \ln x - x + C$$

**Verificación:** 
$$\frac{d}{dx}(x \ln x - x) = \ln x + x \cdot \frac{1}{x} - 1 = \ln x + 1 - 1 = \ln x \quad ✓$$

---

## 1.6 Integrales de Funciones Trigonométricas

### Funciones Básicas

| Integral | Resultado | Verificación |
|----------|-----------|--------------|
| $\int \sin x \, dx$ | $-\cos x + C$ | $(-\cos x)' = \sin x$ |
| $\int \cos x \, dx$ | $\sin x + C$ | $(\sin x)' = \cos x$ |
| $\int \tan x \, dx$ | $-\ln\lvert\cos x\rvert + C$ | o $\ln\lvert\sec x\rvert + C$ |
| $\int \cot x \, dx$ | $\ln\lvert\sin x\rvert + C$ | |
| $\int \sec x \, dx$ | $\ln\lvert\sec x + \tan x\rvert + C$ | |
| $\int \csc x \, dx$ | $-\ln\lvert\csc x + \cot x\rvert + C$ | o $\ln\lvert\csc x - \cot x\rvert + C$ |

### Funciones Trigonométricas al Cuadrado

| Integral | Resultado |
|----------|-----------|
| $\int \sec^2 x \, dx$ | $\tan x + C$ |
| $\int \csc^2 x \, dx$ | $-\cot x + C$ |
| $\int \sec x \tan x \, dx$ | $\sec x + C$ |
| $\int \csc x \cot x \, dx$ | $-\csc x + C$ |

---

## 1.7 Integrales que Producen Funciones Inversas

### Funciones Trigonométricas Inversas

$$\boxed{\int \frac{1}{\sqrt{1-x^2}} \, dx = \arcsin x + C}$$

$$\boxed{\int \frac{1}{1+x^2} \, dx = \arctan x + C}$$

$$\boxed{\int \frac{1}{\lvert x \rvert\sqrt{x^2-1}} \, dx = \text{arcsec}\, \lvert x \rvert + C}$$

### Formas Generalizadas

$$\int \frac{1}{\sqrt{a^2-x^2}} \, dx = \arcsin\frac{x}{a} + C$$

$$\int \frac{1}{a^2+x^2} \, dx = \frac{1}{a}\arctan\frac{x}{a} + C$$

$$\int \frac{1}{x\sqrt{x^2-a^2}} \, dx = \frac{1}{a}\text{arcsec}\frac{\lvert x \rvert}{a} + C$$

---

## 1.8 Propiedades de la Integral Indefinida

### Linealidad

**Propiedad 1: Constante multiplicativa**
$$\int k \cdot f(x) \, dx = k \int f(x) \, dx$$

**Propiedad 2: Suma y diferencia**
$$\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx$$

**Combinación ([Linealidad](../../../glossary.md#linealidad) completa):**
$$\int [af(x) + bg(x)] \, dx = a\int f(x) \, dx + b\int g(x) \, dx$$

### Tabla Resumen de Integrales Básicas

| [Función](../../../glossary.md#funcion) | Integral |
|---------|----------|
| $x^n$ $(n \neq -1)$ | $\frac{x^{n+1}}{n+1} + C$ |
| $\frac{1}{x}$ | $\ln\lvert x \rvert + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\frac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x \tan x$ | $\sec x + C$ |
| $\csc x \cot x$ | $-\csc x + C$ |
| $\frac{1}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |
| $\frac{1}{1+x^2}$ | $\arctan x + C$ |
