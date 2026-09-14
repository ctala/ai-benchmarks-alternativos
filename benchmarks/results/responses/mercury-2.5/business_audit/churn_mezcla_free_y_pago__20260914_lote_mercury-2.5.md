# Mercury 2.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.52 | quality: 10.0
- latency_total: 3.855s | tokens_per_second: 420.3
- input_tokens: 197 | output_tokens: 1620

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



Respira profundo. El pánico surge de mezclar poblaciones distintas. Tu panel mide a todos los usuarios, pero tu expectativa (5%) casi seguro se refería solo a los de pago.

**Diagnóstico:**
*   **Usuarios de pago:** Solo 2 de 22 se fueron (~9%). Esto es señal de alerta, pero no es una catástrofe.
*   **Usuarios gratuitos:** 60 de 178 se fueron (~34%). En modelos freemium, esto es normal y esperado.
*   **El 31% total:** Es una distorsión matemática por incluir a los gratuitos en el denominador principal.

**¿Qué tan grave es?**
La salud de tu negocio depende de los pagos. El 9% de churn en pagos es lo que debes corregir, no el 31% general.

**Plan de Acción:**
1.  **Separa tus métricas:** Configura un dashboard exclusivo para usuarios activos de pago. No uses el total para decisiones críticas.
2.  **Investiga las 2 pérdidas:** Contacta a quienes dejaron el plan. ¿Fue precio, falta de valor o problemas técnicos?
3.  **Revisa el onboarding:** Si el churn gratuito es tan alto, asegúrate de que vean el valor antes de decidir si quedarse o irse.
4.  **Define tus KPIs:** Establece una línea base real para churn de pago basada en tu industria, no en un número genérico.

Enfócate en retener a los 22 pagadores, no en los 178 gratuitos.