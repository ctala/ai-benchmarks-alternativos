# MiMo V2.5-Pro (Xiaomi) — sales_outreach/campaign_optimization

- model_id: `mimo-v2.5-pro`
- success: True  | final: 8.07 | quality: 9.92
- latency_total: 37.268s | tokens_per_second: 55.0
- input_tokens: 550 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis de Campañas Google Ads — Mes Completo

## 1. Métricas Calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 1,500 / 50,000 = **3.00%** | 4,800 / 120,000 = **4.00%** | 900 / 15,000 = **6.00%** |
| **CPC** | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.38** | $3,200 / 900 = **$3.56** |
| **CPA** | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |
| **Conv. Rate** | 45 / 1,500 = **3.00%** | 24 / 4,800 = **0.50%** | 36 / 900 = **4.00%** |

---

## 2. ¿Escalar, Mantener o Pausar?

### 🟢 ESCALAR — Campaña A (Landing principal)

**La razón es clara:** es la campaña con el **CPA más bajo ($46.67)** y una tasa de conversión sólida (3%). Cada dólar adicional aquí rinde más que en cualquier otra campaña.

- El CPC de $1.40 es razonable para keywords transaccionales
- Las keywords ("software gestión inventario", "inventario pymes") tienen **intención de compra directa**
- Si la escalas, el CPA podría subir un poco (ley de rendimientos decrecientes), pero tiene el mayor margen de maniobra

### 🟡 MANTENER CON AJUSTES — Campaña B (Blog content)

No la pausaría, pero **no la escalaría tal cual**:

- Tiene el CTR más alto en volumen absoluto (4,800 clicks) y el CPC más bajo ($0.38), lo cual es excelente para awareness
- **PERO** el conversion rate de 0.50% es alarmantemente bajo — 6x peor que la Campaña A
- Esto indica que el tráfico es informativo, no transaccional. La gente busca "cómo gestionar inventario" pero no está lista para comprar

**Acción:** Mantener como canal de captación top-of-funnel, pero trabajar en el puente de conversión (ver A/B tests abajo).

### 🔴 PAUSAR O REESTRUCTURAR FONDO — Campaña C (Competidor)

Los números no mienten:

- **CPA de $88.89** — casi el doble que la Campaña A
- **CPC de $3.56** — 2.5x más caro que la Campaña A
- Sí, tiene el mejor conversion rate (4%), pero eso no compensa el costo brutal por click
- Las keywords de competidores son **caras por naturaleza** (subasta muy competida)
- Con solo 900 clicks y $3,200 de gasto, está consumiendo **el 64% de tu presupuesto** para generar solo 36 signups

**La pregunta clave:** ¿Cuánto vale cada signup para tu negocio? Si tu LTV por cliente es alto ($500+), la Campaña C podría justificarse. Si es un SaaS de $20-50/mes, es insostenible.

---

## 3. Redistribución del Presupuesto ($5,000/mes)

Mi propuesta basada en los datos:

```
┌─────────────────────────────────────────────────┐
│           PRESUPUESTO RECOMENDADO               │
├──────────────────┬──────────┬───────────────────┤
│ Campaña          │ Monto    │ % del total       │
├──────────────────┼──────────┼───────────────────┤
│ A (Landing)      │ $2,800   │ 56%  (+$700)      │
│ B (Blog)         │ $1,500   │ 30%  (-$300)      │
│ C (Competidor)   │ $700     │ 14%  (-$2,500)    │
└──────────────────┴──────────┴───────────────────┘
```

### Proyección de resultados (asumiendo eficiencia constante):

| Campaña | Inversión | Clicks estimados | Signups estimados | CPA |
|---|---|---|---|---|
| **A** | $2,800 | ~2,000 | ~60 | $46.67 |
| **B** | $1,500 | ~4,000 | ~20 | $75.00 |
| **C** | $700 | ~197 | ~8 | $87.50 |
| **TOTAL** | **$5,000** | **~6,197** | **~88** | **$56.82** |

**Comparación con el mes actual:**

| | Mes actual | Proyección | Cambio |
|---|---|---|---|
| Signups totales | 105 | ~88 | -17 |
| CPA promedio | $47.62 | $56.82 | +$9.20 |

> ⚠️ **Nota honesta:** Con $5,000 vs. los $7,100 que gastaste este mes, vas a perder volumen. La redistribución optimiza el *costo por signup*, pero si quieres mantener los 105 signups necesitas o bien aumentar presupuesto o bien mejorar la conversión de la Campaña B.

---

## 4. A/B Tests para el Próximo Mes

### Test 1 — Landing Page de Campaña A (ALTA PRIORIDAD)
```
Versión actual: Landing principal genérica
vs.
Versión B: Landing específica por keyword
```
- Una landing para "software gestión inventario" con copy enfocado en features
- Otra para "inventario pymes" con copy enfocado en