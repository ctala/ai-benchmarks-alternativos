# Seed 2.1 Turbo — business_strategy/plan_aritmetica_no_cierra

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 133.971s | tokens_per_second: 61.1
- input_tokens: 252 | output_tokens: 8192

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

**No lo apruebes tal cual. La multiplicación básica ya falla por un 70%, y hay supuestos no validados que lo alejan aún más del objetivo.** Vamos a desglosarlo paso a paso, como hacemos con cualquier plan antes de dar el visto bueno:

---

### 1. Primero: la cuenta cruda del plan que presentó tu socio (sin trucos)
Hagamos la multiplicación línea por línea, tal cual lo escribiste:
- 200.000 visitas/mes × 1,5% de conversión a suscriptor = **3.000 suscriptores nuevos por mes**
- 3.000 suscriptores nuevos × 2% de compra = **60 ventas por mes**
- 60 ventas × $30 por curso = **$1.800 USD de ingreso bruto por mes**

Eso es **$4.200 USD menos que el objetivo de $6.000**. Ni de cerca. Tu socio cometió un error de cálculo muy común: casi seguro confundió la base sobre la que aplica el porcentaje de compra, o asumió que los ingresos crecen solos por acumulación de lista (lo que no es real, como veremos).

---

### 2. Los errores de supuesto que hacen que el número sea aún peor
Tú dices que los porcentajes te parecen sanos, pero son promedios del sector, no números conservadores. Y dependen de condiciones que el plan no menciona, así que en la práctica pueden ser mucho menores:
#### ❌ El 1,5% de conversión a suscriptor no es conservador por defecto
Es un número promedio solo si cumples dos condiciones:
  - Tienes un **lead magnet de alta calidad** (no un "suscríbete a mi boletín" genérico) alineado con el contenido que trae el tráfico.
  - El formulario está en ubicaciones estratégicas (pop up de intención de salida, contenido encerrado, banners en artículos relacionados).
Si el formulario es genérico o está en el pie de página, la conversión cae a 0,2-0,5% de media.

#### ❌ El 2% de conversión a compra es promedio, no conservador
Solo se cumple si:
  - El lead magnet está perfectamente alineado con el curso (ej: lead magnet = "5 trucos para editar reels" → curso = "Edición de reels para negocios"). Si el lead magnet no tiene relación, la conversión cae a 0,5% o menos.
  -