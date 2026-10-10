# Claude Haiku 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 14.172s | tokens_per_second: 183.4
- input_tokens: 320 | output_tokens: 2599

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

**No lo aprobaría tal como está.** Los porcentajes pueden ser razonables, pero el plan no llega a $6.000/mes, y además confunde ventas únicas con ingresos recurrentes.

## 1. Cuentas con sus propios supuestos

- **Visitas:** 200.000/mes
- **Suscriptores nuevos:** 200.000 × 1,5% = **3.000/mes**
- **Compradores:** 3.000 × 2% = **60 cursos/mes**
- **Ingreso:** 60 × $30 = **$1.800/mes**

Esto es **30% del objetivo**. La brecha no es un detalle de redondeo.

## 2. Qué tendría que ser cierto para llegar a $6.000

Son $6.000 / $30 = **200 ventas por mes**. Con sus porcentajes, eso exige una de estas opciones:

| Palanca | Valor necesario | Comparación con el plan |
|---|---|---|
| Visitas | ~667.000/mes | 3,3× el tráfico actual |
| Precio del curso | ~$100 | 3,3× el precio actual |
| Conversión a suscriptor | ~5% | Más del triple de 1,5% |
| Conversión a compra | ~6,7% de la lista | Muy por encima de 2% |

Ninguna palanca sola es probablemente realista. Para llegar hay que combinar varias, y eso hay que demostrarlo, no suponerlo.

## 3. Problemas de fondo

- **"Recurrentes" es incorrecto.** Un curso de $30 es una venta única. Si cada mes solo sumás compras nuevas, el ingreso depende de conseguir ventas nuevas cada mes. No es recurrente.
- **Acumulado vs. mensual.** Con 18.000 suscriptores a los 6 meses (sin bajas, lo cual es optimista), el 2% compra unas 360 veces en total, es decir ~$10.800 acumulados. Eso puede sonar bien, pero no equivale a $6.000 por mes.
- **Visitas no son personas.** Si las 200.000 son sesiones, los visitantes únicos son menos, y los recurrentes no vuelven a suscribirse. Los suscriptores nuevos reales pueden ser bastante menores que 3.000.
- **"Conservador" no es un dato.** Los porcentajes son supuestos. Si no los medieron, no sabemos si son conservadores, optimistas o inventados.

## 4. Qué haría antes de decidir

1. **Medir los números reales de las últimas semanas:** visitas únicas, tasa de suscripción actual (si hay formulario) y ventas por email, si ya existen.
2. **Hacer un test de 2 a 4 semanas** con el formulario y una oferta del curso a la lista existente. Eso da una tasa de compra medida, no estimada.
3. **Modelar tres escenarios** (pesimista, base, optimista) con esos datos, y mostrar cuánto ingreso da cada uno a 6 meses.
4. **Si el objetivo es recurrente de verdad**, evaluar un modelo que lo sea: membresía mensual, suscripción a contenido, comunidad paga, o cursos de renovación. Con $30 por única vez, $6.000/mes es un volumen de ventas difícil de sostener sin escalar mucho el tráfico.

**Veredicto:** no ejecutarlo como está. Primero validar la tasa de compra con un test barato, y reformular el objetivo si lo que se busca es ingreso recurrente. Si quieren, les armo el modelo con escenarios y el test concreto.