# Claude Fable 5 — strategy/pricing_strategy

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.21 | quality: 7.5
- latency_total: 28.807s | tokens_per_second: 71.1
- input_tokens: 288 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y escenarios bien estructurados que un emprendedor podría aplicar directamente.

## Respuesta completa

# Análisis de Aumento de Precio: $60 → $89/mes

## 1. LTV/CAC Ratio: Actual vs. Proyectado

**Situación actual:**
- LTV (ingresos): $840 | LTV/CAC = **7.0x**
- LTV ajustado por margen: ($60 - $8) × 14.3 meses = $743 | LTV/CAC = **6.2x**

Ambos están muy por encima del benchmark saludable (3x). Esto sugiere que **estás cobrando de menos o invirtiendo poco en adquisición**.

**Con precio de $89 (si el churn no cambiara):**
- LTV: $89 × 14.3 = $1,272 | LTV/CAC = **10.6x**
- LTV ajustado: $81 × 14.3 = $1,158 | LTV/CAC = **9.6x**

Pero el churn SÍ va a cambiar, así que modelemos eso.

---

## 2. Impacto Estimado en Churn (Benchmarks SaaS)

Datos relevantes de la industria:

- Un aumento del **48%** (tu caso) es agresivo; los aumentos "seguros" suelen ser del 10-20% anuales
- Estudios de Price Intelligently/ProfitWell muestran que aumentos comunicados con valor agregado generan churn adicional de **1-3 puntos porcentuales** en los primeros 60-90 días
- **Dato importante:** tu churn actual de 7% mensual ya es alto (benchmark SMB SaaS: 3-5%). Esto indica sensibilidad al precio o problemas de retención que el aumento podría amplificar

Estimación: churn incremental de +1 a +5 puntos según ejecución, más una ola de cancelaciones inmediatas del 5-25%.

---

## 3. Tres Escenarios (base: 200 clientes, MRR actual $12,000)

| Métrica | Optimista | Realista | Pesimista |
|---|---|---|---|
| Cancelaciones inmediatas | 5% (10 clientes) | 12% (24 clientes) | 22% (44 clientes) |
| Clientes restantes | 190 | 176 | 156 |
| Churn mensual nuevo | 8% | 9.5% | 12% |
| **MRR nuevo** | **$16,910 (+41%)** | **$15,664 (+31%)** | **$13,884 (+16%)** |
| LTV nuevo (ingresos) | $1,113 | $937 | $742 |
| LTV/CAC nuevo | 9.3x | 7.8x | 6.2x |
| Margen bruto/cliente | $81 (91%) | $81 (91%) | $81 (91%) |

**El hallazgo clave:** tu punto de equilibrio en MRR es perder **65 clientes (32.5%)**. Incluso en el escenario pesimista ganas más dinero con menos clientes que soportar. El riesgo de downside es bajo.

---

## 