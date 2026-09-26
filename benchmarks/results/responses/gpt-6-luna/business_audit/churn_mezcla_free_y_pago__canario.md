# GPT-6 Luna — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.22 | quality: 10.0
- latency_total: 9.105s | tokens_per_second: 113.1
- input_tokens: 165 | output_tokens: 1030

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

Respira: **el 31% no parece ser el churn de pago**, sino una mezcla de usuarios gratuitos y de pago.

| Segmento | Bajas | Usuarios al inicio | Churn |
|---|---:|---:|---:|
| Total | 62 | 200 | **31%** |
| Gratuito | 60 | 178 | **33,7%** |
| De pago | 2 | 22 | **9,1%** |

**Qué tan grave es:** si lo que te preocupa es la pérdida de clientes que generan ingresos, la cifra relevante es **2 de 22: 9,1%**, no 31%. Aun así, está por encima del 5% que esperabas. Pero son solo 22 cuentas: una baja equivale a 4,5 puntos porcentuales, así que dos bajas bastan para que la tasa casi se duplique respecto a una. Es una señal para investigar, no una conclusión definitiva sobre una tendencia.

Las 60 bajas gratuitas pueden ser importantes para la adquisición o la conversión futura, pero no deberían mezclarse con el churn de pago para evaluar retención de ingresos. Y confirma que “baja” significa realmente que la cuenta dejó de ser cliente: no una cancelación de prueba, una cuenta inactiva o un cambio de plan.

### Plan

1. **Verifica la definición y los datos.** Confirma qué cuenta como baja, que el denominador sean usuarios activos al inicio del mes y cómo se trataron cambios entre planes.
2. **Separa las métricas desde ahora.** Reporta churn de pago por separado; añade pérdida de ingresos (MRR) y, si las bajas gratuitas alimentan el embudo, mide también su conversión a pago.
3. **Investiga las dos bajas de pago.** Revisa motivo declarado, antigüedad, plan, uso reciente, incidencias de soporte y si hubo problemas de facturación. Con dos casos, leer cada historia es más útil que buscar patrones estadísticos.
4. **Compara con meses anteriores usando la misma definición.** Mira varios meses y el número absoluto de bajas junto con la tasa; no compares el 31% combinado con una meta de churn de pago.
5. **Actúa según lo que encuentres.** Si ambas bajas comparten una causa corregible, priorízala. Si no, sigue de cerca las próximas cohortes antes de cambiar la estrategia por un solo mes.

En resumen: **el 31% es engañoso para medir la retención de pago; el 9,1% merece atención, pero el volumen pequeño hace que el resultado sea muy sensible a solo una baja adicional o menos.**