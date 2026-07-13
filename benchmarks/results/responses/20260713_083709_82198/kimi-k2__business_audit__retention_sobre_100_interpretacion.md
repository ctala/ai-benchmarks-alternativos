# Kimi K2 — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 5.93 | quality: 6.0
- latency_total: 17.677s | tokens_per_second: 29.1
- input_tokens: 162 | output_tokens: 514

## Respuesta completa

No. Esa lectura es incorrecta y peligrosa. Te explico por qué.

## El problema con el 114%

**Retención de ingresos > 100% ≠ retención de clientes > 100%**

Tu panel está midiendo **Net Revenue Retention (NRR)**, no retención de clientes. Son métricas distintas:

| Métrica | Qué mide | Tu caso |
|---------|----------|---------|
| **NRR (114%)** | Ingresos de cohorte inicial, incluyendo expansiones/contracciones | Los upgrades compensaron pérdidas |
| **Retención de clientes** | Cuántos logos se quedan | **90%** (36/40) |

## Tu situación real

- **Perdiste 4 clientes** (10% de churn mensual → ~70% anualizado, catastrófico)
- Los upgrades de los 36 restantes generaron 14% más ingreso que el mes anterior
- Pero **no puedes expandir a clientes que se fueron**

## Por qué no puedes ignorar el churn

| Escenario | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|-----------|-------|-------|-------|-------|
| Clientes | 40 | 36 | 32 | 29 |
| NRR | 114% | 112% | 110% | 108% |
| Ingresos | $100 | $114 | $128 | $138 |

Sí, los ingresos suben... hasta que la base es tan pequeña que ni las expansiones lo compensan. Además, **adquirir clientes cuesta 5-7x más que retenerlos**.

## Qué hacer ahora

1. **Segmentar el churn**: ¿Se fueron clientes pequeños, grandes, de cierto plan, cierta antigüedad?
2. **Calcular GRR (Gross Revenue Retention)**: sin expansiones, probablemente ~85-90%
3. **Mantener esfuerzo de retención**: el 10% mensual es insostenible

El 114% es una señal de que tu **expansión funciona**, no de que tu **retención está resuelta**.