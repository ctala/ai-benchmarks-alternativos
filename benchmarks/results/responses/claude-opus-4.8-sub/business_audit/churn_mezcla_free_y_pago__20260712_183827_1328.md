# Claude Opus 4.8 (suscripción) — business_audit/churn_mezcla_free_y_pago

- model_id: `claude-opus-4-8`
- success: True  | final: 5.22 | quality: 6.0
- latency_total: 58.334s | tokens_per_second: 53.2
- input_tokens: 4 | output_tokens: 3106

## Respuesta completa

## Primero: el 31% no es tu churn

Es un promedio ponderado que está midiendo tres poblaciones distintas como si fueran una. Separadas:

| Segmento | Base inicio | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Blended (el del panel) | 200 | 62 | 31% |

El 97% de tus bajas (60 de 62) son de usuarios que nunca te pagaron un peso. El número del panel está dominado por el plan gratis y no te dice nada accionable sobre el negocio.

## Segundo: con 22 clientes de pago, el porcentaje es ruido

Cada cliente de pago vale **4.5 puntos porcentuales**. Mirá la escala completa:

- 1 baja → 4.5%
- 2 bajas → 9.1%
- 3 bajas → 13.6%

Tu "5% esperado" equivale a **1 baja**. Este mes tuviste **2**. Estás en pánico por una persona. Con esta muestra no podés distinguir 5% de 9%: no hay resolución estadística. Reportar porcentajes con n=22 es inventar precisión que no existe.

## Tercero: todavía no sabés qué tan grave es, y ese es el problema real

Nada de lo que me diste responde la pregunta que importa: **cuánto MRR se fue.** Logo churn de 9% con 2 cuentas chicas es un mal mes. Con tus 2 cuentas más grandes, puede ser 25-30% de revenue churn y ahí sí hay incendio.

---

## Plan

**Hoy (30 minutos, sin tocar código)**

1. **Revenue churn:** MRR perdido ÷ MRR al inicio del mes. Y NRR (incluyendo upgrades de los que se quedaron). Esa es la métrica del negocio, no el conteo de cabezas.
2. **Reconciliá el 5%:** ¿de dónde salía? ¿Era paid-only? ¿Otro período? ¿Otra definición de baja? Si no sabés qué medía, no sabés si mejoraste o empeoraste.
3. **Definí "baja" en el plan gratis.** ¿Borró la cuenta o "no entró en 30 días"? Si es lo segundo, 34% probablemente es normal y ni siquiera es churn.

**Esta semana**

4. **Hablá con los 2 que cancelaron.** Son dos. Literalmente podés llamarlos. Con n=2 no hacés estadística, hacés entrevistas — y vale más.
5. **Segmentá el churn gratuito por cohorte de signup y por activación.** Si los 60 son gente que se registró hace poco y nunca llegó al momento "ajá", no tenés un problema de retención: tenés un problema de **activación/onboarding**. Es otro problema, con otra solución.

**Estructural (arreglar el panel)**

6. Matá el número blended. Reemplazalo por tres métricas separadas: **churn de pago (logo)**, **NRR**, **activación del free tier**.
7. Con menos de ~50 clientes de pago, reportá **absolutos**: "2 bajas de 22", no "9.1%".
8. Ojo con la trampa a futuro: si tu plan gratis crece, el churn blended va a *empeorar* aunque el negocio mejore. Es una métrica que te va a mentir cada vez más.

---

**Resumen:** lo que tenés es un problema de medición disfrazado de crisis. La evidencia disponible no muestra un colapso de retención — muestra un dashboard que mezcla poblaciones. Bajá el pulso, calculá el revenue churn, y llamá a esos dos clientes.