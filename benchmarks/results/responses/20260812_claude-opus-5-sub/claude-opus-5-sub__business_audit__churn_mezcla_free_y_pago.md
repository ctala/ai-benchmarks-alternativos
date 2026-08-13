# Claude Opus 5 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-opus-5`
- success: True  | final: 7.99 | quality: 10.0
- latency_total: 66.549s | tokens_per_second: 54.3
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

## Primero: respira. La cifra de 31% no mide lo que crees

Tu panel está promediando dos poblaciones que no tienen nada que ver entre sí.

| Población | Base | Bajas | Churn real |
|---|---|---|---|
| Gratuitos | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Mezclado (lo que ves) | 200 | 62 | 31% |

El 89% de tu base es gratuita. Eso significa que tu "churn del 31%" es, en la práctica, **el churn del plan gratis con un poco de ruido de pago encima**. No es una métrica de negocio: es una métrica de gente que nunca te dio dinero y decidió no seguir usando algo que no le costaba nada.

## Segundo: el 9,1% tampoco es un dato todavía

Aquí viene la parte incómoda, y es la que importa.

Con 22 pagadores, **2 bajas no distinguen un churn del 5% de uno del 15%**. Míralo así:

- Si se hubiera ido 1 pagador → 4,5% (tu supuesto original)
- Se fueron 2 → 9,1%
- Si se hubieran ido 3 → 13,6%

Una sola persona mueve la métrica 4,5 puntos. El intervalo de confianza con esa muestra va aproximadamente de 2% a 28%. Es decir: **no tienes suficientes pagadores para leer churn mensual.** Ningún cálculo lo va a arreglar; es un límite de la muestra.

Lo que sí es cierto: si el 9% se sostuviera, tu vida media de cliente pasa de ~20 meses (a 5%) a ~11 meses. Eso es la mitad de tu LTV. Vale la pena vigilarlo — pero vigilarlo, no reaccionar hoy.

## Tercero: dos preguntas que cambian el diagnóstico entero

**1. ¿Qué cuenta tu panel como "baja"?** Cancelación activa o inactividad. Si es inactividad (no entró en 30 días), el 33,7% del plan gratis es casi decorativo. Muchísimas plataformas marcan como churn a alguien que se registró, miró una vez y nunca volvió. Eso no es retención rota: es **activación que nunca ocurrió**.

**2. ¿Cuánto MRR se fue, no cuántos logos?** 2 de 22 pagadores puede ser el 9% de tus clientes y el 3% o el 25% de tus ingresos. Churn de logos y churn de revenue son métricas distintas y solo una paga las cuentas.

---

## Plan

**Hoy (1 hora)**
1. Separa el panel en dos números que nunca vuelvan a promediarse: churn de pago y churn de gratis. Ponles nombres distintos — al gratis llámalo "caída de activación", no churn.
2. Calcula cuánto MRR se fue con esos 2 pagadores y qué % de tu MRR total representa.
3. Revisa la definición de "baja" en el panel. Anótala por escrito.

**Esta semana**
4. Con n=2, lo cuantitativo no sirve: **habla con los 2 que se fueron.** Escríbeles hoy. Dos conversaciones te dan más señal que cualquier dashboard con esta muestra.
5. Corta las 60 bajas gratuitas por canal de adquisición y por cohorte de registro. Busca específicamente: ¿hubo una campaña o pico de registros que trajo gente de baja intención? Un lote de registros fríos que rebota infla el churn sin que nada haya cambiado para tus usuarios reales.
6. Mira cuántos de esos 60 llegaron alguna vez a usar el producto de verdad. Si la mayoría nunca activó, tu problema es onboarding, no retención.

**Los próximos 90 días**
7. Deja de leer churn de pago mensualmente. Léelo como promedio móvil de 3 meses, o en cohortes trimestrales. Con 22 pagadores el ruido mensual te va a dar un infarto cada dos meses sin motivo.
8. La métrica que sí deberías estar mirando con una base 89% gratuita: **conversión de gratis a pago**. Ahí está tu cuello, no en el churn.

**Qué NO hacer**
- No lances una campaña de retención de emergencia esta semana.
- No cambies el precio.
- No rediseñes el onboarding basándote en 2 cancelaciones.

Toda reacción fuerte a esta cifra sería una reacción a un artefacto de medición. Primero arregla el instrumento, después decide.

---

Si me pasas el desglose de las 60 bajas gratuitas por fecha de registro y canal, te ayudo a ver si hay un lote contaminado ahí — es la hipótesis más probable.