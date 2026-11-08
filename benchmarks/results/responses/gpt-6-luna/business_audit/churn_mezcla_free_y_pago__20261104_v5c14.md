# GPT-6 Luna — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 8.678s | tokens_per_second: 97.4
- input_tokens: 165 | output_tokens: 845

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

Respira: **el 31% no significa que hayas perdido el 31% de tus clientes de pago ni de tus ingresos**. Es el churn de todos los usuarios mezclados, y casi todos son gratuitos.

Con los datos que das:

- **Total:** 62 / 200 = **31%**
- **Plan gratuito:** 60 / 178 = **33,7%**
- **Plan de pago:** 2 / 22 = **9,1%**

Así que, si tu referencia del 5% es para clientes de pago, el dato relevante es aproximadamente **9,1%**, no 31%. Aun así, está por encima del 5% y merece revisión. Con solo 22 usuarios de pago, cada baja equivale a unos **4,5 puntos porcentuales**, así que dos bajas hacen que la tasa parezca muy alta; no saques conclusiones de tendencia con un solo mes.

### Plan

1. **Comprueba la definición del panel.** Confirma que el denominador son usuarios activos al inicio del mes y que las bajas corresponden a usuarios que estaban activos entonces. Revisa también cómo trata cambios de plan, pausas, reactivaciones y cuentas duplicadas.
2. **Separa las métricas.** Reporta por separado churn de pago y churn gratuito. Si la meta es conservar ingresos, calcula además el *churn de ingresos recurrentes* (MRR): dos cuentas pueden representar cantidades muy distintas.
3. **Investiga las dos bajas de pago.** Revisa motivo, antigüedad, plan, uso del producto, tickets de soporte y si hubo fallos de cobro. Contacta a esos clientes si es apropiado.
4. **Mira la tendencia, no solo este mes.** Compara varios meses y cohortes, manteniendo la misma definición. Con una base de pago pequeña, muestra también el número de bajas junto al porcentaje.
5. **Decide según el resultado.** Si hubo un problema concreto, corrígelo primero. Si las bajas se repiten, prioriza entrevistas y señales de riesgo entre los clientes de pago.

El 31% parece alarmante porque mezcla poblaciones distintas. Para evaluar el negocio de pago, empieza por el **9,1%** y por el impacto real en ingresos; no asumas que ese porcentaje representa una pérdida equivalente de MRR.