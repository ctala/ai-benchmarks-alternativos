# Qwen 3.8 27B — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 104.198s | tokens_per_second: 93.3
- input_tokens: 256 | output_tokens: 9722

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa



**No. No lo apruebo como plan para llegar a $6.000 USD/mes.**

El plan no muere en los porcentajes, muere en la multiplicación.

## Cálculo con sus propios números

1. **200.000 visitas/mes**
2. Conversión a suscriptor: **1,5%**
   - 200.000 × 1,5% = **3.000 suscriptores/mes**
3. Conversión de suscriptor a compra: **2%**
   - 3.000 × 2% = **60 compradores/mes**
4. Curso de **$30**
   - 60 × $30 = **$1.800 USD/mes**

**Resultado real: $1.800 USD/mes, no $6.000.**

Te faltan **$4.200 USD/mes**, es decir, el plan alcanza solo **30% del objetivo**.

---

## Para llegar a $6.000 USD/mes con un curso de $30

Necesitas:

**$6.000 / $30 = 200 ventas/mes**

Con las conversiones que puso tu socio:

- 1,5% de captura
- 2% de compra

El flujo sería:

> 200.000 visitas × 1,5% × 2% × $30 = $1.800

Para llegar a $6.000 con esos mismos porcentajes, necesitarías:

> **666.667 visitas/mes**

No 200.000.

---

## Otras formas de llegar a $6.000

### Opción 1: Subir la captura a suscriptor

Si mantienes:

- 200.000 visitas
- 2% de compra
- Precio $30

Necesitas:

- 10.000 suscriptores/mes
- 200 ventas/mes

Eso implica:

> 10.000 / 200.000 = **5% de conversión a suscriptor**

Eso es bastante más alto que 1,5%.

---

### Opción 2: Subir la conversión a compra

Si mantienes:

- 200.000 visitas
- 1,5% de captura
- Precio $30

Tienes 3.000 suscriptores/mes.

Para vender 200 cursos, necesitas:

> 200 / 3.000 = **6,7% de conversión de suscriptor a compra**

Eso también es mucho más alto que 2%.

---

### Opción 3: Subir el precio

Con las ventas actuales del plan:

- 60 compradores/mes

Para llegar a $6.000:

> $6.000 / 60 = **$100 por curso**

Es decir, con los mismos 60 compradores, el curso tendría que costar **$100**, no $30.

O combinaciones intermedias:

| Escenario | Ventas necesarias | Precio | Ingreso |
|---|---:|---:|---:|
| Actual | 60 | $30 | $1.800 |
| Subir precio a $50 | 120 | $50 | $6.000 |
| Subir precio a $75 | 80 | $75 | $6.000 |
| Subir precio a $100 | 60 | $100 | $6.000 |

---

## Segundo problema: “recurrentes”

Aquí hay una ambigüedad importante.

### Si el curso es de pago único

Entonces **no es ingreso recurrente**.

Con los números del plan:

- $1.800/mes de ventas nuevas
- No MRR
- No recurrencia

Eso no es un negocio de $6.000/mes recurrentes.

---

### Si es una suscripción de $30/mes

Entonces sí podría acumular MRR, pero el plan tampoco lo modela.

Con 60 nuevos suscriptores/mes y sin churn:

| Mes | Suscriptores activos | MRR |
|---:|---:|---:|
| 1 | 60 | $1.800 |
| 2 | 120 | $3.600 |
| 3 | 180 | $5.400 |
| 4 | 240 | $7.200 |

Ahí sí llegarías a $6.000 MRR alrededor del mes 4.

Pero si hay churn, por ejemplo 5% mensual:

| Mes | Suscriptores activos aproximados | MRR aproximado |
|---:|---:|---:|
| 1 | 60 | $1.800 |
| 2 | 117 | $3.510 |
| 3 | 171 | $5.135 |
| 4 | 223 | $6.678 |

También llegaría alrededor del mes 4, pero **no está en el plan**.

El plan no incluye:

- Churn
- Cancelaciones
- Pagos fallidos
- Soporte
- Onboarding
- Retención
- Base de suscriptores existente
- Crecimiento acumulado

Así que decir “llegamos cómodos a $6.000/mes recurrentes” con 60 ventas nuevas de $30 no está respaldado.

---

## Veredicto

**No le damos tal cual.**

Los porcentajes pueden ser razonables, pero el objetivo está mal dimensionado.

El plan actual dice:

> 200.000 visitas × 1,5% × 2% × $30 = **$1.800/mes**

No $6.000.

---

## Lo que sí apruebo

Aprobaría ejecutarlo como **test de 30 días**, pero con objetivo realista:

### Objetivo del test

- Validar si realmente logran:
  - 1,5% de captura
  - 2% de compra
- Generar **$1.800 USD/mes**
- Medir métricas reales:
  - Visitas → suscriptor
  - Suscriptor → comprador
  - Precio aceptado
  - Churn, si aplica
  - LTV
  - CAC, si el tráfico es pagado

---

## Para aprobar el objetivo de $6.000, el plan necesita cambiar al menos una de estas variables

### 1. Más tráfico

Manteniendo 1,5% captura, 2% compra y $30 precio:

> Necesitan **666.667 visitas/mes**

---

### 2. Mejor captura

Manteniendo 200.000 visitas, 2% compra y $30 precio:

> Necesitan **5% de conversión a suscriptor**

Eso implica un lead magnet muy fuerte, landing optimizada y tráfico calificado.

---

### 3. Mejor conversión de venta

Manteniendo 200.000 visitas, 1,5% captura y $30 precio:

> Necesitan **6,7% de conversión de suscriptor a compra**

Eso requiere una oferta muy fuerte, secuencia de email agresiva, urgencia, prueba social y página de venta bien optimizada.

---

### 4. Mayor precio

Manteniendo 60 ventas/mes:

> Necesitan vender a **$100**

O una combinación:

- 120 ventas × $50 = $6.000
- 80 ventas × $75 = $6.000
- 60 ventas × $100 = $6.000

---

### 5. Combinación más realista

Una combinación que sí cierra la cuenta sería:

- 200.000 visitas
- 3% de captura = 6.000 suscriptores
- 2% de compra = 120 ventas
- Precio $50

> 120 × $50 = **$6.000/mes**

Eso es más alcanzable que 5% de captura o 6,7% de compra, pero sigue siendo un salto importante.

---

## Decisión final

**No aprobamos el plan para $6.000 USD/mes.**

Sí aprobamos una versión corregida:

> Ejecutar el formulario y la oferta durante 30 días con objetivo de $1.800 USD/mes, validar las tasas reales y definir el plan de escalado solo con datos.

Si tu socio quiere $6.000/mes, el plan debe cambiar. No con más esfuerzo, sino con otra matemática.