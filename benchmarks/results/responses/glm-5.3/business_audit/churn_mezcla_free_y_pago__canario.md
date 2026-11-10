# GLM 5.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 58.407s | tokens_per_second: 86.6
- input_tokens: 177 | output_tokens: 5060

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

# Respira: el 31% es real pero mide otra población que la que tú crees

Antes de interpretar el número, separamos la población. El panel está calculando el churn **de todos los usuarios mezclados**, y el 89% de tu base es plan gratuito:

| Segmento | Usuarios | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Total | 200 | 62 | 31% |

Verificación de consistencia: 0.89 × 33.7% + 0.11 × 9.1% = 31%. El panel no está roto; simplemente mezcla dos poblaciones con economías distintas. **El 97% de tus bajas (60 de 62) son usuarios que no generan ingreso directo.**

## Qué tan grave es

Depende de de dónde salió tu "5%", y eso es lo primero que hay que verificar:

**Escenario A — el 5% era churn de pago (o una métrica solo-de-pagos).** Entonces el salto a 31% es definicional, no un evento. Y tu churn de pago actual (9.1%) es estadísticamente indistinguible de 5%: con 22 usuarios de pago, si la tasa real fuera 5%, verías 2 o más bajas ~30% de las veces. Un usuario más o menos mueve la métrica 4.5 puntos.

**Escenario B — el 5% era el churn combinado de la misma población.** Entonces pasaste de ~10 a 62 bajas en un mes: algo real pasó, concentrado en usuarios gratuitos. No es una crisis de ingresos, pero sí una señal del funnel.

En cualquier caso, el impacto directo en ingresos este mes son 2 usuarios de pago. Ese es el número que debe dictar la urgidad.

La verdadera bandera amarilla es el **33.7% de churn gratuito**: no te cuesta MRR, pero es tu pipeline hacia pago. Si un tercio se va cada mes, tu adquisición llena un balde agujereado.

## El plan

**Paso 0 — Verifica la definición (hoy)**
- Recalcula los últimos 3–6 meses con esta misma fórmula (bajas / usuarios a inicio de mes, todos). ¿El 5% existió alguna vez bajo esta definición?
- Confirma qué cuenta como "baja": ¿incluye borrado automático de cuentas gratuitas inactivas o limpiezas batch? Una purga de inactivos puede explicar 60 bajas de golpe.

**Paso 1 — Descompón las 60 bajas gratuitas (esta semana)**
- Por antigüedad: ¿son signups recientes? Churn de cohortes nuevas (problema de activación o calidad de adquisición) ≠ usuarios consolidados que se van (problema de producto).
- Por activación: ¿llegaron alguna vez a la acción central del producto? Si la mayoría nunca activó, no tienes un problema de retención, tienes uno de onboarding.
- Por canal: una campaña de adquisición de baja calidad dispara churn 30 días después.

**Paso 2 — Los 2 que pagaban (esta semana, prioridad)**
- n=2 es malo para estadística pero perfecto para entrevistas. Escríbeles hoy. Lo que digen vale más que cualquier panel.
- Revisa su MRR: si eran del plan alto, ese 9.1% pesa más de lo que parece.

**Paso 3 — Arregla el panel**
- Métrica principal: **churn de MRR** (pago, ponderado por ingreso), no churn de usuarios.
- Muestra churn segmentado por plan y retención por cohorte (día 30/60/90).
- Etiqueta cada métrica con su población y fórmula. Tu pánico de hoy nació de una métrica sin etiqueta.

**Paso 4 — Benchmarks para orientarte**
- Churn de MRR mensual: 1–3% (B2B), 4–7% (consumidor/PYMES). Estás en ~9% con incertidumbre enorme (n=2): obsérvalo 2–3 meses más antes de sacar conclusiones.
- Churn gratuito de 30%+ es común en freemium con activación débil. La palanca ahí es activación, no campañas de retención.

## En resumen

No tienes un problema de 31%; tienes un problema de medición (métrica combinada dominada por usuarios gratuitos) más una señal manejable (34% gratuito, 9.1% pago con n=2). Antes de tocar producto o precios, corre el Paso 0 y el 1: verificar la historia y descomponer esas 60 bajas.