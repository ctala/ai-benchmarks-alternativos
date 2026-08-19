# Claude Fable 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 22.414s | tokens_per_second: 59.4
- input_tokens: 262 | output_tokens: 1332
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y un plan de acción práctico para abordar el problema del churn.

## Respuesta completa

Respira. Antes de actuar, revisemos qué está midiendo realmente ese 31%, porque el panel está mezclando dos poblaciones muy distintas.

## Recalculando con la población correcta

**El 31% (62/200) mezcla usuarios gratuitos y de pago.** Eso no es churn de negocio, es un promedio que no representa a nadie. Separemos:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Pago | 22 | 2 | **9.1%** |
| Gratuito | 178 | 60 | 33.7% |
| Mezclado (lo que ves) | 200 | 62 | 31% |

El 31% está dominado por los usuarios gratuitos porque son el 89% de tu base. Tu churn de *ingresos* —el que amenaza tu negocio— es 9.1%.

## ¿Qué tan grave es?

**No estás en crisis, pero tampoco en el 5% que creías:**

1. **Churn de pago: 9.1% vs. tu 5% esperado.** Es más alto, pero cuidado con la muestra: con solo 22 usuarios de pago, **cada baja mueve la métrica 4.5 puntos**. La diferencia entre 5% y 9% es literalmente un usuario. No puedes concluir una tendencia con un mes y n=22.

2. **Churn gratuito: 33.7%.** Esto no es churn de ingresos, es un problema de **activación/retención de producto**. Importa para tu embudo de conversión, pero no está quemando dinero hoy.

## Plan de acción

**Esta semana:**
1. **Habla con los 2 usuarios de pago que se fueron.** Con solo 2, puedes contactarlos personalmente. Su razón de baja vale más que cualquier dashboard ahora mismo.
2. **Arregla el panel:** separa churn de pago, churn gratuito y (si tienes planes de distinto precio) churn de MRR. Nunca vuelvas a mirar la métrica mezclada.

**Este mes:**
3. **Verifica si los 2 de pago eran clientes nuevos o antiguos.** Churn en el primer mes = problema de onboarding/expectativas. Churn de clientes veteranos = problema de valor sostenido, más serio.
4. **Analiza los 60 gratuitos que se fueron:** ¿llegaron a usar el producto? ¿cuántos días estuvieron activos? Probablemente descubras que la mayoría nunca se activó — eso es un problema de onboarding, no de retención.

**Continuo:**
5. **Sigue el churn de pago por cohortes durante 3 meses** antes de sacar conclusiones. Con base pequeña necesitas tendencia, no fotos mensuales.
6. **Define una alerta correcta:** churn de pago >X% durante 2 meses seguidos, no la métrica mezclada.

## Resumen

Pasaste de "31% de churn, catástrofe" a "9% de churn de pago con n=22, que puede ser ruido, más un problema de activación en el plan gratuito". Lo primero se resuelve con dos llamadas telefónicas; lo segundo con trabajo de onboarding. Ninguno es pánico.