# GPT-6 Luna — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.96 | quality: 10.0
- latency_total: 13.011s | tokens_per_second: 98.1
- input_tokens: 186 | output_tokens: 1277

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**No aprobaría los $10.000 de golpe con estos números.** El cálculo del LTV usa dos supuestos que no cuadran:

- Con un churn mensual constante del 8%, la permanencia esperada es aproximadamente **1 / 0,08 = 12,5 meses**, no 24.
- Para compararlo con el CAC, conviene usar el LTV de **margen bruto**, no solo los ingresos.

| Métrica | Cálculo | Resultado |
|---|---:|---:|
| Ingreso mensual por cliente |  | $35 |
| Margen bruto mensual | $35 × 70% | $24,50 |
| LTV de ingresos estimado | $35 / 8% | $437,50 |
| **LTV de margen bruto estimado** | $24,50 / 8% | **$306,25** |
| **LTV de margen bruto / CAC** | $306,25 / $290 | **1,06** |
| Recuperación del CAC | $290 / $24,50 | **11,8 meses** |

Así que no estás cerca de un ratio de 2,9: el ratio relevante es aproximadamente **1,06**, antes de costes fijos, coste del dinero y cualquier coste variable que no esté incluido en ese 70%.

A ese CAC, gastar $10.000 te conseguiría unos **34 clientes** si el CAC se mantiene. Su margen bruto esperado durante toda su vida sería alrededor de **$10.560** en total: apenas unos $560 por encima de la publicidad, y ese margen se cobraría a lo largo del tiempo, no de inmediato. Además, al escalar, el CAC marginal podría subir.

**Mi recomendación:** no escales fuerte todavía. Haz una prueba limitada y revisa la retención por cohortes, el CAC marginal y el tiempo real de recuperación. Como referencia, para llegar a un LTV de margen bruto/CAC de 3 con estas cifras, el CAC tendría que bajar a unos **$102**, o tendrías que mejorar sustancialmente el margen o la retención.