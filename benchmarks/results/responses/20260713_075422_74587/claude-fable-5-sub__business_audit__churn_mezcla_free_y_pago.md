# Claude Fable 5 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-fable-5`
- success: True  | final: 4.22 | quality: 4.8
- latency_total: 39.214s | tokens_per_second: 42.9
- input_tokens: 2 | output_tokens: 1681

## Respuesta completa

Respira. El panel te está mezclando dos poblaciones distintas en una sola métrica, y eso hace que el 31% no signifique nada. Separemos:

## Lo que la métrica realmente mide

| Segmento | Inicio de mes | Bajas | Churn real |
|---|---|---|---|
| **Pago** | 22 | 2 | **9.1%** |
| **Gratuito** | 178 | 60 | 33.7% |
| Mezclado (lo que reporta el panel) | 200 | 62 | 31% ← engañoso |

El 31% es un "blended churn" dominado por usuarios gratuitos, que no pagan nada. Tu churn de **clientes de pago es 9.1%**, no 31%.

## Qué tan grave es (en serio)

1. **No es 31%, pero tampoco es tu 5% asumido.** 9.1% mensual en pago es alto para SaaS (benchmark SMB: 3-7% mensual). PERO...

2. **Con n=22, todavía no puedes concluir nada.** Cada cliente de pago mueve la métrica 4.5 puntos porcentuales. 2 bajas puede ser tendencia o puede ser ruido puro. Un mes con esta muestra no es data, es una anécdota.

3. **Los 60 gratuitos que se fueron NO son churn en el sentido de negocio.** Son abandono de top-of-funnel. Puede indicar un problema de onboarding/activación, o simplemente curiosos que nunca iban a pagar. Distinto problema, distinto plan.

## Plan concreto

**Esta semana:**
1. **Habla con los 2 clientes de pago que se fueron.** Son literalmente 2 personas — mándales un email o llámalos hoy. Con muestra tan chica, la entrevista de salida vale más que cualquier dashboard.
2. **Calcula el churn de revenue (MRR), no solo de logos.** Si los 2 que se fueron eran tu plan más barato, la foto cambia; si eran los más caros, se agrava.
3. **Arregla el dashboard:** churn de pago y "abandono de free" como métricas separadas, siempre. Nunca más una métrica mezclada.

**Este mes:**
4. **Mide activación de gratuitos:** ¿qué % de los 178 llegó al momento de valor del producto antes de irse? 60/178 abandonando sugiere revisar onboarding, pero primero confirma si alguna vez se activaron.
5. **Arma cohortes:** churn de pago por mes de alta, últimos 6 meses. Necesitas ver si el 9.1% es tendencia o punto atípico.

**Regla para adelante:** antes de reaccionar a cualquier métrica, pregunta *qué población está midiendo*. Hoy te salvó de tomar decisiones de pánico sobre un número que no existe.