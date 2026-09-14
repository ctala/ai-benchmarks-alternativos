# GLM 5.3 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 33.207s | tokens_per_second: 67.6
- input_tokens: 177 | output_tokens: 2246

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

# Respira: el 31% mezcla dos poblaciones que no se parecen en nada

Antes de interpretar cualquier métrica, la pregunta correcta es: **¿qué población está midiendo realmente ese número?** Aquí la respuesta es "un promedio de cosas muy distintas".

## Desglose real

| Segmento | Inicio de mes | Bajas | Churn real |
|---|---|---|---|
| **Total** | 200 | 62 | **31%** |
| Plan gratuito | 178 (89% de la base) | 60 | **33.7%** |
| Plan de pago | 22 (11% de la base) | 2 | **9.1%** |

**Lectura:** el 31% está casi enteramente explicado por usuarios gratuitos, que son el 89% de tu denominador. El 97% de tus bajas (60 de 62) son usuarios que no pagaban. El churn de pago es 9.1% mensual —no es excelente, pero es un problema completamente distinto al que el panel te hizo creer.

## Qué significa cada número

- **Churn gratuito (33.7%):** no es pérdida de ingresos. Es pérdida de usuarios en la parte superior del embudo. Materia para diagnóstico, no para pánico.
- **Churn de pago (9.1%):** esto sí es dinero que se va. Son 2 clientes, con denominador de 22. Mensualizado y anualizado, ronda ~68% de churn anual —si esto se sostiene, sí es grave—. Pero con n=22, un mes puede ser ruido.

## Plan

**Hoy — verificar que el número sea real (30 min):**
1. **¿Cambió la definición del panel?** Un salto de 5% a 31% en un mes casi nunca es comportamiento orgánico. Pregúntate: ¿el panel empezó a contar inactivos como "baja"? ¿Hubo una limpieza de cuentas inactivas o un cambio técnico que disparó cancelaciones automáticas?
2. **Identifica los 2 clientes de pago que se fueron:** MRR que pierdes, antigüedad, motivo de cancelación, si estaban cerca de su renovación. Llámalos o escríbeles hoy.
3. **Trae el histórico:** ¿cómo se veían los últimos 6 meses de churn segmentado? Con 22 usuarios de pago, un solo mes no establece tendencia.

**Esta semana — redefinir cómo reportas:**
4. **Separa la métrica para siempre:** churn de pago (logo y MRR) como métrica principal; churn gratuito como métrica de embudo, con su propia línea. Un promedio de poblaciones distintas solo sirve para generar pánico como el de hoy.
5. **Define operativamente "baja":** ¿es cancelar suscripción? ¿eliminar cuenta? ¿30 días sin sesión? Cada definición da números diferentes, y deben estar documentadas.
6. **Investiga el pico gratuito por separado:** ¿hubo cambio de onboarding, un bug, cambio en notificaciones, o simplemente llegaron muchos usuarios de baja calidad hace 1-2 meses y ahora se caen? El churn gratuito de este mes suele ser el eco de adquisiciones de meses anteriores.

**En curso:**
7. Con 22 clientes de pago, analiza churn por cohorte de entrada, no por mes calendario. Y cuando tengas más volumen, evalúa MRR churn además de churn por número de clientes: perder 2 clientes grandes no pesa igual que perder 2 pequeños.

## Resumen ejecutivo

No perdiste el 31% de tu negocio; perdiste 2 clientes de pago (9.1% mensual, a vigilar de cerca) y muchos usuarios que no generaban ingresos. La gravedad real la defines los datos de los puntos 1-3: si el churn de pago se repite varios meses, ahí sí tienes un incendio —pero hoy no es eso.