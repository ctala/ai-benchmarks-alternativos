# GLM 5.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 94.589s | tokens_per_second: 71.7
- input_tokens: 177 | output_tokens: 6786

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

Respira. El 31% es aritméticamente correcto, pero no mide lo que crees que mide: es un **churn mezclado sobre una población donde el 89% son usuarios gratuitos**. Parte el número primero:

| Plan | Base | Bajas | Churn mensual |
|---|---|---|---|
| Gratuito | 178 | 60 | 33,7% |
| Pago | 22 | 2 | 9,1% |
| Mezclado | 200 | 62 | **31%** |

El 97% de tus bajas (60 de 62) vienen del plan gratuito. El 31% es, en la práctica, el churn de tu capa gratuita disfrazado de métrica general.

**Qué tan grave es**

- **Para tu ingreso: poco.** Perdiste 2 clientes de pago. Eso se investiga en una tarde, no es un incendio. Y con 22 usuarios de pago, 2 bajas no bastan para concluir que algo empeoró: si tu churn real fuera 5%, esperarías ~1 baja al mes, y hay ~30% de probabilidad de ver 2 o más por puro azar. A esta escala, 5% y 9,1% son indistinguibles. De hecho, cada baja mueve tu métrica 4,5 puntos: el churn de pago mensual va a oscilar entre 5% y 14% sin que nada cambie de verdad.
- **Para tu funnel: es la pregunta real.** 33,7% mensual en gratuito implica una vida media de ~3 meses por usuario gratuito. Si eso es lo normal en tu producto y el gratuito convierte a pago, es un embudo funcional. Si no convierte, es un costo. Con estos datos aún no lo sabemos.

**Antes de interpretar más, verifica** (el salto 5% → 31% huele más a cambio de medición que de comportamiento):

1. **¿De dónde salía tu 5%?** ¿Misma definición, mismo denominador, mismo periodo? 5% de 200 son 10 bajas; 5% de 22 son 1,1. Reconstruye el número histórico. Sospecha principal: antes mirabas solo pago y el panel ahora mezcla planes.
2. **¿Las 62 bajas existían a inicio de mes?** Si el numerador incluye altas del mismo mes que rebotaron, el 31% está inflado. Revisa fecha de alta de las 62.
3. **¿Las 60 bajas gratuitas están concentradas en un día/hora?** Busca purga automática de cuentas inactivas — eso no es churn con intención.
4. **¿Cambió algo este mes?** Tracking, panel, o que el plan gratuito ahora permita darse de baja fácilmente.
5. Reactivaciones y duplicados.

**Plan**

*Hoy:*
- Parte el tablero: churn de pago y churn gratuito por separado, siempre. El mezclado no es una métrica de salud del negocio.
- Audita las 62 bajas: fecha de alta, fecha de baja, plan, canal, antigüedad.
- Revisa uno por uno a los 2 clientes de pago que se fueron: plan, tenure, motivo, últimas acciones. Son 2, se puede.

*Esta semana:*
- Serie histórica de 6 meses de churn de pago; con n=22 usa ventana móvil de 90 días para que un evento no te mueva el número.
- Baseline de churn gratuito: ¿33,7% es nuevo o siempre fue así? Por cohorte de antigüedad y por canal.
- Tasa de conversión gratuito→pago. Con eso decides si la capa gratuita es motor o lastre.
- Churn en MRR además de logos: 2 bajas de planes baratos no pesan como 2 de planes caros.
- Altas vs. bajas del mes: churn bruto alto con altas fuertes es recambio de funnel, no fuga.

*Mediano plazo:*
- Define churn distinto por población: pago = cancelación/no renovación; gratuito = inactividad de X días, con umbral explícito.
- Alertas sobre churn de pago en MRR, no sobre el mezclado.
- Encuesta de cancelación para capturar motivo.

**Veredicto:** no es una emergencia. Es primero un problema de medición (población mezclada, y probablemente definición que cambió) y segundo una pregunta de funnel. Si mañana el panel te muestra 9% en pago y 34% en gratuito, ya sabrás qué mirar y qué ignorar.