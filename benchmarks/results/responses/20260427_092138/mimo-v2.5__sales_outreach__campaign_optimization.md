# MiMo V2.5 (Xiaomi) — sales_outreach/campaign_optimization

- model_id: `mimo-v2.5`
- success: True  | final: 7.98 | quality: 9.36
- latency_total: 17.73s | tokens_per_second: 115.5
- input_tokens: 546 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas Calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Conv. Rate** | 3.0% | 0.5% | 4.0% |

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ ESCALAR: Campaña A (Landing principal)

**Justificación numérica:**
- **Mejor CPA ($46.67)** — es 37% más barato que B y 48% más barato que C
- **3.0% de conversión** — cada 33 clics genera un signup
- Keywords de **alta intención comercial** ("software gestión inventario")
- ROI más eficiente: por cada $1 invertido, consigues 0.021 signups

### ⚠️ MANTENER CON OPTIMIZACIÓN: Campaña C (Competidor)

**Justificación:**
- **Mejor tasa de conversión (4.0%)** — el público está listo para decidir
- **CTR más alto (6.0%)** — el anuncio resuena con la audiencia
- **Problema:** CPA de $88.89 es el más caro
- **Oportunidad:** Si reduces el CPC de $3.56 a ~$2.50, el CPA bajaría a ~$62

### ❌ PAUSAR: Campaña B (Blog content)

**Justificación numérica:**
- **Peor CPA ($75.00)** — 61% más caro que Campaña A
- **0.5% de conversión** — necesitas 200 clics para 1 signup
- Aunque tiene el CPC más bajo ($0.38), el tráfico es de **baja intención**
- Los keywords ("cómo gestionar inventario") atraen personas que **buscan información**, no que **quieren comprar**

> 💡 **Dato clave:** Campaña B genera el 68% de tus clics pero solo el 25% de tus signups. Es tráfico "vanidad".

---

## 3. Redistribución del Presupuesto ($5,000)

```
┌─────────────────────────────────────────────────────────┐
│  ACTUAL vs PROPUESTO                                    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Campaña A:  $2,100 (42%)  →  $2,800 (56%)  ⬆️ +$700  │
│  Campaña B:  $1,800 (36%)  →  $400  (8%)   ⬇️ -$1,400 │
│  Campaña C:  $1,100 (22%)  →  $1,800 (36%)  ⬆️ +$700  │
│                                                         │
│  Total:      $5,000         $5,000                      │
└─────────────────────────────────────────────────────────┘
```

### Proyección con nueva distribución:

| Campaña | Presupuesto | Signups estimados | CPA estimado |
|---------|-------------|-------------------|--------------|
| A | $2,800 | ~60 | $46.67 |
| B | $400 | ~5 | $80.00 |
| C | $1,800 | ~27 | $66.67 |
| **TOTAL** | **$5,000** | **~92** | **$54.35** |

> 📈 **Resultado:** Pasarías de ~105 signups (con $7,100) a ~92 signups (con $5,000), pero con un **CPA 35% más eficiente**.

---

## 4. A/B Tests para el Próximo Mes

### Para Campaña A (escalar):
| Test | Variable A | Variable B | Métrica a medir |
|------|-----------|-----------|-----------------|
| **Landing page** | Formulario largo (5 campos) | Formulario corto (3 campos) | Tasa de conversión |
| **Copy del anuncio** | "Software para inventario" | "Controla tu inventario desde hoy" | CTR |
| **Social proof** | Sin