# Claude Fable 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 27.552s | tokens_per_second: 74.3
- input_tokens: 393 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para optimizar las campañas de marketing.

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.0% | 4.0% | **6.0%** |
| **CPC** | $1.40 | **$0.38** | $3.56 |
| **Conversion Rate** | 3.0% | 0.5% | **4.0%** |
| **CPA** | **$46.67** | $75.00 | $88.89 |

**Cálculos:**
- CTR = Clicks / Impresiones
- CPC = Costo / Clicks
- CPA = Costo / Signups
- Conv. Rate = Signups / Clicks

⚠️ **Nota importante:** Tu gasto actual es **$7,100**, no $5,000. Estás 42% sobre presupuesto, lo que hace la redistribución aún más urgente.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escalar: Campaña A
- **Mejor CPA ($46.67)** — 37% más barato que B y 47% más barato que C
- Conversion rate saludable (3%) con keywords de intención comercial directa
- Con solo 50K impresiones, probablemente hay volumen sin explotar (revisar Impression Share)

### ⏸️ Pausar (o transformar): Campaña B
- Genera muchos clicks baratos pero **conversion rate de 0.5%** — 6-8x peor que las otras
- Las keywords ("cómo gestionar inventario") son **intención informacional**, no de compra
- El problema no es la campaña en sí, es esperar signups directos de tráfico top-of-funnel

### ⚠️ Optimizar (no pausar): Campaña C
- Peor CPA ($88.89), **pero** tiene el mejor CTR (6%) y conversion rate (4%)
- Los usuarios que buscan "alternativa a [competidor]" son **alta intención** — probablemente convierten mejor a cliente pago
- El problema es el CPC de $3.56, no la calidad del tráfico

**Punto clave:** Si tienes datos de LTV, revisa qué campaña genera clientes que *pagan y se quedan*. Un signup de C podría valer 2x uno de A.

---

## 3. Redistribución de $5,000

| Campaña | Antes | Propuesta | Signups esperados* |
|---|---|---|---|
| A (Landing) | $2,100 | **$3,000** (60%) | ~64 |
| C (Competidor) | $3,200 | **$1,500** (30%) | ~17-22 |
| B (Blog → Retargeting) | $1,800 | **$500** (10%) | ~5-10 |

*Asumiendo CPAs estables; con optimización de C, esperaría más.

**Racional:**
- **A recibe +43%**: es tu motor de crecimiento comprobado. Escala gradualmente (20-30% semanal) para no degradar el Quality Score
- **C se recorta pero se mantiene**: reduce pujas, enfócate solo en las keywords "[competidor] vs" y "alternativa a" con mejor historial, y agrega negativas
- **B se convierte en retargeting**: usa el tráfico del blog (4,800 clicks = audiencia enorme) para remarketing en Display/YouTube. Ese tráfico ya te costó $1,800 — exprímelo

**Proyección:** de ~105 signups/mes con $7,100 (CPA blend $67.62) a **~85-95 signups con $5,000** (CPA blend ~$55).

---

## 4. A/B Tests para el próximo mes

### Campaña A (prioridad alta — es donde escalas)
1. **Headline de landing:** beneficio ("Reduce pérdidas de inventario 30%") vs. funcional ("Software de inventario para PyMEs")
2. **Largo del formulario de signup:** 3 campos vs. solo email (podría subir conv. rate de 3% a 4-5%)

### Campaña C (prioridad alta — mejorar el CPA)
3. **Landing de comparación dedicada** ("[T