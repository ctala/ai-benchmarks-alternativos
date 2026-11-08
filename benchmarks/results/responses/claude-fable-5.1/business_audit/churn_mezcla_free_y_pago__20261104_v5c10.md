# Claude Fable 5.1 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 24.238s | tokens_per_second: 68.6
- input_tokens: 264 | output_tokens: 1663

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

Respira. El 31% es real como número, pero está midiendo la población equivocada para lo que te preocupa.

## Lo que el panel está mezclando

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Combinado (lo que reporta el panel) | 200 | 62 | 31% |

El 31% está dominado por el plan gratuito, que es el 89% de tu base. El churn de los usuarios que te pagan es 9,1%.

## ¿Qué tan grave es?

**El churn de pago (9,1%) no es tu 5%, pero tampoco puedes concluir que empeoró.** Con 22 usuarios, cada baja mueve la métrica 4,5 puntos. Una baja = 4,5%, dos bajas = 9,1%. Eso es ruido estadístico, no tendencia. Necesitas varios meses para saber si estás en 5% o en 9%.

**El churn gratuito (34%) probablemente no es "churn".** Usuarios gratuitos que prueban y se van es comportamiento normal de un funnel. Antes de alarmarte, hay dos preguntas:
- ¿Qué cuenta el panel como "baja" en un usuario gratuito? ¿Borró la cuenta, o simplemente dejó de entrar? Si es inactividad, el 34% puede ser lo esperado.
- ¿El plan gratuito es un producto en sí mismo o es la puerta de entrada al pago? Si es la puerta, la métrica que importa es conversión y activación, no retención.

**Lo que sí tienes que verificar:** de dónde salió el 5% que tenías en la cabeza. Si era churn de pago de meses anteriores, compáralo con el 9,1% de hoy. Si era el número combinado de otro mes, entonces nunca tuviste 5% de nada y la comparación no sirve.

## Plan

1. **Hoy:** Mira las 2 bajas de pago una por una. Con n=2 no haces estadística, haces investigación: ¿quiénes eran, cuánto tiempo llevaban, hubo algún ticket o señal previa? Si puedes escribirles, hazlo. Eso te dice más que cualquier porcentaje.

2. **Esta semana:** Separa el reporte. Churn de pago y churn gratuito como dos métricas distintas, nunca combinadas. Si el panel no lo permite, calcúlalo a mano desde el export.

3. **Esta semana:** Define "baja" para usuarios gratuitos. Si es inactividad, decide cuántos días son el umbral y mídelo como *abandono de prueba* o *no activación*, no como churn.

4. **Próximos 3 meses:** Registra churn de pago mensual con el denominador y el numerador, no solo el porcentaje. Con 22 usuarios, el porcentaje te va a mentir cada mes; los números absolutos no.

5. **Como referencia:** Para un SaaS pequeño, churn mensual de pago entre 3% y 8% es un rango habitual. 9,1% con 2 bajas está en el borde, pero no es una emergencia. Sería una emergencia si ves 2 bajas al mes durante tres meses seguidos.

El pánico venía de leer 31% como si fueran clientes. No lo son. Tienes 2 clientes perdidos y 60 usuarios gratuitos que no se quedaron, y esos son problemas distintos con soluciones distintas.