# Claude Sonnet 5 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-sonnet-5`
- success: True  | final: 6.77 | quality: 8.0
- latency_total: 55.348s | tokens_per_second: 65.2
- input_tokens: 2 | output_tokens: 3611

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

No estás en pánico por lo que crees. El 31% no está mal calculado, está **mal segmentado** — mezcla dos poblaciones que no tienen nada que ver entre sí.

## El desglose que realmente importa

| Población | Usuarios | Bajas | Churn real |
|---|---|---|---|
| Free | 178 (89% de la base) | 60 | **33,7%** |
| Paid | 22 (11% de la base) | 2 | **9,1%** |
| Blended (lo que ves en el panel) | 200 | 62 | 31% |

El 31% no es "el churn de tu negocio". Es un promedio ponderado donde el free —que es 9 de cada 10 usuarios— arrastra el número. Tu plan de pago, que es el que paga las cuentas, está en 9,1%, no en 31%.

## Qué tan grave es

**Menos grave de lo que pensabas, pero no descartado:**

- El churn free al 33,7% mensual no es alarmante por sí solo. Es normal (a veces esperado) que usuarios gratuitos prueben y se vayan sin fricción de pago de por medio. Eso mide activación/producto, no salud del negocio.
- El churn paid al 9,1% sí está por encima del 5% que esperabas. Pero con **n=22 y solo 2 bajas**, el margen de error es enorme: una baja más o menos te mueve el número de 4,5% a 13,6%. No podés tratar esto como una tendencia todavía — es una muestra demasiado chica para sacar conclusiones duras.

## Antes de actuar, 3 preguntas que te faltan responder

1. **El 5% que esperabas, ¿era mensual o anual, y era de todos los usuarios o solo de pago?** Si esperabas 5% anual y estás viendo 9,1% mensual, ahí sí hay una alarma real (compuesto seria ~70% anual). Si esperabas 5% mensual blended, en realidad ya estás mejor de lo que creías en paid.
2. **¿Qué cuenta como "baja" en el free?** Cancelación explícita de cuenta ≠ expiración de trial ≠ inactividad ≠ downgrade. Si el panel cuenta "usuario dejó de loguearse 30 días" como baja free, ese 33,7% es ruido de definición, no señal.
3. **¿Es logo churn o revenue/MRR churn?** Con 2 bajas de pago, importa si eran tu plan más caro o el más barato. El impacto en logos y el impacto en MRR pueden contar historias distintas.

## Plan

1. **De ahora en adelante, reportá churn SIEMPRE segmentado por plan.** Nunca vuelvas a mirar el número blended como KPI de negocio — solo sirve como agregado contable, no para decidir nada.
2. **Fijá el paid churn (o mejor, MRR churn) como tu métrica norte.** El free churn lo trackeás aparte como métrica de producto/activación.
3. **Confirmá la definición exacta de "baja"** en el panel esta semana — con tu proveedor de plataforma o en la doc del panel. Sin esto, cualquier número que reportes puede estar midiendo otra cosa sin que lo sepas.
4. **No reacciones todavía sobre el 9,1% paid.** Con n=22 andá a ventana móvil de 3 meses antes de tomar una decisión (subir precio, cambiar onboarding, etc.). Un mes de 2 bajas no es tendencia.
5. **Habla con esos 2 usuarios de pago que se fueron.** Con una base tan chica, una entrevista de salida te dice más que cualquier porcentaje.

En resumen: no tenés un incendio del 31%. Tenés un free churn normal-alto que no debería estar en el mismo número que tu churn de pago, y un paid churn levemente por encima de tu meta pero con una muestra demasiado chica para confirmar si es problema real o ruido.