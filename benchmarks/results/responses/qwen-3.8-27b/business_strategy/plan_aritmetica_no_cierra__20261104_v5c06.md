# Qwen 3.8 27B — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 104.338s | tokens_per_second: 65.6
- input_tokens: 256 | output_tokens: 6845

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



**No. Tal como está, no lo apruebo para $6.000 USD/mes.**

El problema no son tanto los porcentajes, sino lo que produce la multiplicación completa.

## Cálculo real del plan

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Visitas/mes | — | 200.000 |
| Captura de suscriptores | 200.000 × 1,5% | 3.000 suscriptores/mes |
| Compradores del curso | 3.000 × 2% | 60 compradores/mes |
| Ingreso por curso | 60 × $30 | **$1.800/mes** |

El objetivo es **$6.000/mes**, así que el plan tal cual queda en:

> **$1.800 / $6.000 = 30% del objetivo**  
> Falta: **$4.200/mes**

O sea, no llega “cómodamente”. Llega **muy corto**.

---

## El multiplicador real es pequeño

La conversión total de visita a comprador es:

> 1,5% × 2% = **0,03%**

Eso significa que por cada 10.000 visitas, te quedan **3 compradores**.

Con un ticket de $30:

> 3 × $30 = **$90 por cada 10.000 visitas**

Por lo tanto, con 200.000 visitas:

> 20 × $90 = **$1.800/mes**

Esa es la realidad del modelo actual.

---

## ¿Qué haría falta para llegar a $6.000/mes?

Con un curso de $30, necesitas:

> $6.000 / $30 = **200 ventas/mes**

El plan actual produce 60 ventas/mes. Necesitas **3,33 veces más ventas**.

Puedes lograrlo cambiando una o varias variables:

### Opción 1: más tráfico

Con las mismas conversiones y mismo precio:

> 666.667 visitas/mes × 1,5% × 2% × $30 = $6.000

Es decir, necesitarías cerca de **667.000 visitas/mes**, no 200.000.

### Opción 2: mejor captura de suscriptores

Manteniendo 200.000 visitas, 2% de compra y $30:

> 200.000 × 5% × 2% × $30 = $6.000

Necesitarías subir la captura de **1,5% a 5%**.

Eso puede ser difícil de conseguir si 1,5% era tu línea base.

### Opción 3: mejor conversión de venta

Manteniendo 200.000 visitas, 1,5% de captura y $30:

> 200.000 × 1,5% × 6,67% × $30 = $6.000

Necesitarías que del listado de suscriptores compren **6,67%**, no 2%.

También es un salto grande.

### Opción 4: subir el precio

Manteniendo 60 ventas/mes:

> 60 × $100 = $6.000

El ticket tendría que pasar de **$30 a $100**.

No es imposible, pero requiere validar si el mercado paga eso.

### Opción 5: combinar mejoras más modestas

Por ejemplo:

- 200.000 visitas
- 3% de captura
- 3% de conversión de venta
- Precio de $50

> 200.000 × 3% = 6.000 suscriptores  
> 6.000 × 3% = 180 compradores  
> 180 × $50 = **$9.000/mes**

Eso ya superaría el objetivo.

Otra combinación:

- 200.000 visitas
- 2,5% de captura
- 4% de conversión de venta
- Precio de $50

> 200.000 × 2,5% = 5.000 suscriptores  
> 5.000 × 4% = 200 compradores  
> 200 × $50 = **$10.000/mes**

Pero eso no es “conservador”. Es un plan de optimización serio.

---

## El tema de “recurrentes”

Aquí hay una ambigüedad importante.

### Si el curso es de pago único

Entonces no son ingresos recurrentes. Esos $1.800/mes serían ventas nuevas cada mes.

En 6 meses tendrías, como máximo si se mantiene estable:

> $1.800 × 6 = **$10.800 totales**

No $36.000.

Y tu objetivo implícito de $6.000/mes durante 6 meses sería:

> $6.000 × 6 = **$36.000**

Así que con el plan actual estarías muy lejos.

### Si el curso es una suscripción mensual de $30

Entonces sí podría acumularse, pero el plan no menciona retención, churn ni cancelaciones.

Con churn cero, que es poco realista:

| Mes | Nuevos compradores | Total clientes | MRR |
|---:|---:|---:|---:|
| 1 | 60 | 60 | $1.800 |
| 2 | 60 | 120 | $3.600 |
| 3 | 60 | 180 | $5.400 |
| 4 | 60 | 240 | $7.200 |

En teoría, cruzarías $6.000 MRR en el mes 4 si nadie cancela.

Pero en la práctica, con churn mensual, cancelaciones, fallas de pago, fatiga de marketing o mal posicionamiento, no puedes prometer eso “cómodamente”.

Además, el plan tal cual dice “2% de los suscriptores compra”, no “2% se convierte en cliente recurrente y no churnea”. Eso cambia completamente el modelo.

---

## Mi veredicto

**No lo apruebo como plan para $6.000/mes.**

Los porcentajes pueden ser sanos, pero el multiplicador final no llega al objetivo.

Apruebo el plan solo en una de estas tres condiciones:

1. **Como plan de validación**, con objetivo realista de **$1.800/mes** o menos.
2. **Como plan de optimización**, si además se comprometen a mejorar tráfico, captura, conversión o ticket.
3. **Como plan escalable**, solo si se demuestra que pueden subir a **200 ventas/mes** sin depender de 667.000 visitas.

Si tu socio cree que con 200.000 visitas, 1,5% de captura, 2% de venta y $30 de ticket llegan a $6.000/mes, está equivocándose en la multiplicación.

**Decisión: no se ejecuta con expectativa de $6.000/mes. Se ajusta o se aprueba como experimento de $1.800/mes.**