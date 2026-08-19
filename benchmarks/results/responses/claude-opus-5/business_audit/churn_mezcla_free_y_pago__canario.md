# Claude Opus 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 32.839s | tokens_per_second: 62.4
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

## Primero: respira. El 31% no es tu churn de negocio

Tu panel está promediando dos poblaciones que no tienen nada que ver entre sí.

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Mezclado | 200 | 62 | 31% |

El 31% es esencialmente el churn del plan gratuito con un poco de ruido de pago encima. El 97% de tus bajas fueron usuarios que no te pagaban nada. Tu churn relevante para ingresos es 9,1%.

Y esto tiene una consecuencia incómoda: **el 31% subirá o bajará según cuántos usuarios gratuitos captes**, sin que tu retención de pago cambie en absoluto. Es una métrica que no puedes gestionar porque mide sobre todo tu volumen de registros gratuitos.

## Segundo: tu churn de pago tampoco es 9,1% de forma confiable

Aquí está el punto que realmente importa. Con 22 usuarios de pago:

- 1 baja = 4,5%
- 2 bajas = 9,1%
- 3 bajas = 13,6%

Tu "5% esperado" y tu "9,1% real" están separados por **un solo cliente**. No tienes un problema de retención confirmado; tienes una base demasiado pequeña para medir retención mensualmente. Cualquier número que calcules a este tamaño va a rebotar entre 0% y 15% por azar puro.

Esto no significa que estés bien. Significa que **todavía no sabes cuál es tu retención de pago**, y ese es el hallazgo real de hoy.

## Lo que hay que verificar antes de actuar

Tres preguntas que cambian por completo el diagnóstico:

**1. ¿Quiénes fueron esos 2 clientes de pago?** Si eran tus dos cuentas más grandes, tu churn de *ingresos* puede ser del 30-40% aunque el churn de clientes sea 9%. Con n=2 puedes revisarlo en cinco minutos.

**2. ¿Fue voluntario o fallo de cobro?** Una tarjeta rechazada se ve idéntica a una cancelación en la mayoría de paneles. El churn involuntario suele ser 20-40% del total en etapas tempranas y se arregla con reintentos y avisos, no con producto.

**3. ¿Qué cuenta como "baja" en el plan gratuito?** ¿Borraron la cuenta o simplemente dejaron de entrar? ¿Y cuántos de esos 60 llegaron a usar el producto alguna vez? Si se registraron y nunca activaron, eso es calidad de adquisición, no churn. Un 34% de abandono en freemium sin activación es normal; un 34% de abandono *después* de activar es un problema de producto.

## Plan

**Esta semana**

1. Separa los paneles. Churn de pago y comportamiento de gratuitos son dos mét