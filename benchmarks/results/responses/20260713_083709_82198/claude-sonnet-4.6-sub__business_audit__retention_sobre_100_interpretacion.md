# Claude Sonnet 4.6 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-sonnet-4-6`
- success: True  | final: 5.94 | quality: 6.94
- latency_total: 46.398s | tokens_per_second: 38.3
- input_tokens: 3 | output_tokens: 1777

## Respuesta completa

## Las dos lecturas que estás mezclando

**114% es retención de *ingresos*, no de *clientes*.**

Son métricas distintas y en tu caso apuntan en direcciones opuestas:

| Métrica | Tu número | Qué significa |
|---|---|---|
| Net Revenue Retention (NRR) | **114%** ✅ | El revenue de tu base existente *creció* 14%, porque las expansiones superaron las pérdidas |
| Logo/Customer Retention | **90%** ⚠️ | Perdiste 4 de 40 clientes = 10% de churn mensual |

---

## Por qué el 114% no significa "nadie se va"

Lo que ocurrió matemáticamente:

- Perdiste 4 clientes → perdiste su revenue
- Varios otros subieron de plan → ganaste revenue extra
- El revenue extra > revenue perdido → NRR > 100%

**El NRR mayor a 100% no implica churn cero. Implica que la expansión compensó el churn.** Son cosas distintas.

---

## Por qué sí deberías preocuparte por el churn

**10% de churn mensual de clientes es alto.** Anualizado, si el patrón se mantiene, podrías perder la mitad de tu base en el año aunque el revenue aguante por ahora.

El problema estructural: **la expansión tiene techo físico**. Solo puedes hacer upsell de los clientes que conservas. Si el pool de clientes sigue encogiendo, eventualmente la expansión no alcanza a compensar, y el NRR cae por debajo de 100%.

Además, cada cliente perdido es:
- Un caso de estudio menos
- Un referido que no va a llegar
- Señal de un problema que todavía no entiendes

---

## Conclusión práctica

**Celebra el 114%** — la expansión funciona, el pricing escalonado hace su trabajo.

**No abandones el análisis de churn.** Investiga esos 4: ¿por qué se fueron? ¿Precio, resultados, alternativa, inactividad? Esa respuesta vale más que cualquier campaña de adquisición.

La métrica correcta para monitorear ambas cosas juntas es la **Gross Revenue Retention (GRR)**: ingresos retenidos sin contar expansión. Si tu GRR está por debajo del 85-90%, tienes un problema de base aunque el NRR se vea bien.