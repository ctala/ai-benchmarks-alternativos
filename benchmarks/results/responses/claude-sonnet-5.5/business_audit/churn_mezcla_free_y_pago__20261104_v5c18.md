# Claude Sonnet 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.04 | quality: 8.0
- latency_total: 15.576s | tokens_per_second: 122.8
- input_tokens: 264 | output_tokens: 1912

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

# Qué tan grave es

**No es un 31% de churn "real" en el sentido que te preocupa.** El panel mezcla dos poblaciones muy distintas.

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | 31% |

- El 31% está dominado por el plan gratuito (89% de la base y 97% de las bajas).
- El churn de pago es 9,1%, no 5%, pero con 22 usuarios **cada baja mueve el indicador 4,5 puntos**. Una baja menos serían 4,5% (tu cifra esperada) y tres serían 13,6%. El intervalo de confianza al 95% para 2/22 va aproximadamente del 3% al 28%, así que no puedes concluir que empeoró.
- Lo que sí es anómalo es el **33,7% en gratuito**, si tu histórico es mucho menor. Pero eso es un problema de activación o de embudo, no de ingresos.

# Plan

**Hoy (verificar antes de actuar)**
1. **Define de dónde sale tu 5%.** ¿Era churn de pago? ¿De ingresos? ¿Un promedio de varios meses? Si comparas churn total contra churn de pago, la comparación no es válida.
2. **Revisa qué significa "baja" para el plan gratuito.** ¿Cancelación explícita, eliminación de cuenta o inactividad de X días? Un cambio en esa regla puede inflar la cifra.
3. **Busca causas mecánicas en los 60 gratuitos:** limpieza de cuentas inactivas, cuentas spam o de prueba, un cambio reciente en los límites del plan, migración de datos, o una cohorte de registro de una campaña de baja calidad.

**Esta semana**
4. **Mira las 2 bajas de pago una por una.** Con tan pocos casos, el análisis cualitativo (motivo, antigüedad, uso previo, ticket de soporte) vale más que el porcentaje. Calcula también el MRR perdido.
5. **Segmenta las 60 bajas gratuitas** por fecha de registro, canal de adquisición y si llegaron a usar el producto. Si la mayoría se fue en los primeros días sin activarse, es un problema de onboarding.
6. **Compara con meses anteriores por segmento**, no solo el total. Si el gratuito ya estaba en 30%, esto no es novedad, solo que antes no lo veías.

**Cambios al reporting**
7. Reporta **churn de pago y churn de ingresos** como métricas principales, y el churn gratuito por separado (o como tasa de conversión/retención de activación).
8. Con una base de pago tan pequeña, usa **media móvil de 3 meses** o muestra el conteo absoluto junto al porcentaje.

# Cuándo sí preocuparse

- Si el churn gratuito subió fuertemente frente a tus meses previos y no hay causa mecánica: el embudo de activación se está rompiendo, lo que reduce la conversión a pago futura.
- Si las 2 bajas de pago comparten un motivo (precio, bug, competidor) o eran cuentas de alto valor.
- Si el churn de pago se mantiene en torno al 9% durante 2-3 meses.

Dime cuál era la base de tu 5% y qué definición de baja usa el plan gratuito, y te ayudo a afinar el diagnóstico.