# Claude Opus 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 32.523s | tokens_per_second: 63.0
- input_tokens: 262 | output_tokens: 2048

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

## Respuesta corta

El 31% no mide lo que crees que mide. Es, en la práctica, una métrica del plan gratuito disfrazada de métrica de salud del negocio.

**Desglose:**

| Población | Inicio | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Mezclado ("31%") | 200 | 62 | 31,0% |

El 89% de tu base es gratuita y aporta el 97% de las bajas. El número agregado es básicamente el churn del free tier con un poco de ruido encima.

## Pero no te vayas tranquilo con el 9,1%

Ese número tampoco es confiable, por una razón distinta: **n=22**.

- 1 baja → 4,5%
- 2 bajas → 9,1%
- 3 bajas → 13,6%

Un solo usuario mueve la métrica 4,5 puntos. Con esa base no puedes distinguir estadísticamente un churn del 5% de uno del 15%. No tienes un problema de retención confirmado; tienes una métrica sin resolución suficiente para decir nada.

Y falta un dato crítico: **¿qué facturaban esos 2 usuarios?** Si uno era tu cuenta más grande, tu churn de ingresos puede ser 25% aunque el churn de usuarios sea 9%. Con 22 clientes, la distribución de ingresos casi nunca es plana.

## Preguntas que hay que cerrar antes de actuar

1. **¿Cómo define "baja" el panel para cada plan?** Si un usuario gratuito se marca como churned por 30 días de inactividad, eso es una métrica de engagement, no de churn. Si un usuario de pago se cuenta al cancelar (y no al terminar el periodo pagado), las fechas no son comparables.
2. **¿De dónde salió el 5% esperado?** Si era un benchmark de SaaS B2B, se refiere a churn mensual de pago, no mezclado. Comparaste peras con canastas.
3. **¿Hay altas dentro del mes?** El denominador usa la foto del día 1. Quien entró y salió el día 15 no aparece en ninguna parte.
4. **De las 2 bajas de pago, ¿alguna fue involuntaria** (tarjeta rechazada)? Suele ser 20-40% del churn de pago y se arregla con dunning, no con producto.

## Plan

**Hoy**
- Deja de reportar el número mezclado. No es accionable y se moverá solo con el mix de planes: si mañana crece el free tier, tu "churn" subirá sin que nada haya empeorado.
- Separa el panel en tres métricas: churn de pago (usuarios), churn de ingresos (GRR/NRR en dinero), y retención del free tier.
- Revisa las facturas de los 2 usuarios que