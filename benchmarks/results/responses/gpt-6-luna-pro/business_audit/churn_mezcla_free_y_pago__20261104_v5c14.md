# GPT-6 Luna Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 37.499s | tokens_per_second: 109.0
- input_tokens: 4921 | output_tokens: 4089

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

Respira: **el 31% no significa que haya perdido el 31% de sus clientes de pago**. Es el resultado de mezclar usuarios gratuitos y de pago.

Con los datos que compartes:

| Población | Bajas | Usuarios al inicio | Churn |
|---|---:|---:|---:|
| Todos | 62 | 200 | **31%** |
| Gratis | 60 | 178 | **33,7%** |
| De pago | 2 | 22 | **9,1%** |

Así que el 31% es correcto **para todos los usuarios**, pero puede ser una métrica poco útil para evaluar la retención del negocio si tu preocupación es conservar clientes de pago. El churn de pago observado sería 9,1%, **si esos 22 eran los clientes de pago activos al inicio del mes**.

Eso sí: no concluyas todavía que tu churn habitual haya pasado del 5% al 9,1%. Solo son dos bajas: con una base de 22, cada cliente representa unos **4,5 puntos porcentuales**. Además, hay que confirmar que ambos meses usan la misma definición. Si el 5% era de clientes de pago, compáralo con el 9,1%, no con el 31%.

### Plan

1. **Audita la métrica.** Confirma que el denominador incluya clientes activos al inicio del mes y que las bajas sean efectivas dentro del mismo periodo. Revisa también si alguien pasó de pago a gratis: puede contar como baja de pago, aunque no como abandono total.
2. **Separa las métricas en el panel.** Como mínimo, muestra churn de clientes de pago, churn de usuarios gratuitos y bajas de ingresos recurrentes. Para el negocio, perder dos clientes pequeños no equivale necesariamente a perder dos clientes grandes.
3. **Investiga las dos bajas de pago.** Comprueba motivo, antigüedad, uso del producto y si fue una cancelación voluntaria, un fallo de cobro o una degradación a gratis. Si puedes, contacta a esas personas.
4. **No hagas cambios drásticos por este único mes.** Compara varios meses con la misma definición y observa también conversiones de gratis a pago. Las bajas gratuitas pueden ser normales o revelar un problema de activación; por sí solas no indican cuánto ingreso has perdido.
5. **Revisa la meta del 5%.** Asegúrate de que se refería al churn mensual de clientes de pago y calcula cuánto ingreso representa cada baja.

**Conclusión:** el 31% está muy influido por los usuarios gratuitos. La cifra que conviene investigar primero es el 9,1% de pago; es mayor que el 5% que esperabas, pero con solo dos bajas no basta para diagnosticar una tendencia.