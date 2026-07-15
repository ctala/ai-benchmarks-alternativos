# Claude Fable 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.66 | quality: 8.0
- latency_total: 22.16s | tokens_per_second: 57.3
- input_tokens: 262 | output_tokens: 1269
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y un plan de acción práctico.

## Respuesta completa

# Respira: el 31% no es tu churn real

## El diagnóstico en 30 segundos

Tu panel está mezclando dos poblaciones que se comportan de forma completamente distinta:

| Segmento | Bajas | Base | Churn |
|---|---|---|---|
| Gratuito | 60 | 178 | **33.7%** |
| **De pago** | **2** | **22** | **9.1%** |
| Mezclado (lo que ves) | 62 | 200 | 31% |

El 31% es un promedio contaminado: como el 89% de tu base es gratuita, su comportamiento domina la métrica. **El churn que importa para tu negocio —el de pago— es 9.1%.**

## Matices importantes antes de actuar

**1. El churn gratuito del 33.7% es probablemente normal.** Los usuarios free abandonan a tasas altísimas en casi cualquier producto. No es señal de crisis; es señal de que tu métrica no debería mezclarlos.

**2. El 9.1% de pago sí merece atención, pero cuidado con la muestra.** Con solo 22 usuarios de pago, **cada usuario mueve la métrica 4.5 puntos porcentuales**. La diferencia entre 2 bajas (9.1%) y 1 baja (4.5%, tu 5% esperado) es literalmente una persona. No puedes concluir todavía que tu churn de pago empeoró.

## Plan de acción

**Esta semana:**
1. **Separa las métricas en el panel**: churn de pago, churn gratuito y conversión free→pago como tres números distintos. Nunca vuelvas a mirar el mezclado.
2. **Habla con los 2 clientes de pago que se fueron.** Con números tan pequeños, la investigación cualitativa vale más que cualquier estadística. Un email o llamada te dice más que el dashboard.

**Este mes:**
3. **Revisa los meses anteriores con la misma segmentación.** ¿Ese "5%" histórico era de pago, mezclado, o de dónde salía? Necesitas comparar peras con peras.
4. **Define qué cuenta como baja gratuita**: ¿cancelación explícita o inactividad? Muchos "churns" free son cuentas dormidas, no abandonos.

**En adelante:**
5. **Sigue el churn de pago por cohortes** (mes de alta), no solo el agregado mensual. Con base pequeña, la tendencia de 3-6 meses es lo único confiable.
6. **Vigila la conversión free→pago**: si los free se van al 33% mensual, tu prioridad no es retenerlos, es convertirlos antes de que se vayan.

## Resumen

No estás en 31%. Estás en ~9% de pago con una muestra de 2 personas, lo cual es estadísticamente indistinguible de tu 5% esperado. La única acción urgente es hablar con esos 2 clientes y arreglar el panel para que esto no vuelva a asustarte.