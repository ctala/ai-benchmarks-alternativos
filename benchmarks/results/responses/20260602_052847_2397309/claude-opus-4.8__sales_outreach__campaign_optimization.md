# Claude Opus 4.8 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.29 | quality: 10.0
- latency_total: 28.593s | tokens_per_second: 71.6
- input_tokens: 393 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** (clicks/impr) | **3.00%** | **4.00%** | **6.00%** |
| **CPC** (costo/clicks) | **$1.40** | **$0.375** | **$3.56** |
| **CPA** (costo/signups) | **$46.67** | **$75.00** | **$88.89** |
| **Conv. Rate** (signups/clicks) | **3.00%** | **0.50%** | **4.00%** |

### Lectura rápida
- **Campaña A**: el **CPA más bajo** ($46.67) y buena conversión. Es tu ganadora en eficiencia.
- **Campaña B**: excelente CTR/CPC barato, pero **conversión pésima** (0.5%). Mucho tráfico, poco resultado.
- **Campaña C**: **mejor CTR (6%) y conversión (4%)**, pero el **CPA más caro** por el alto CPC ($3.56).

---

## 2. Qué escalar y qué pausar

### ✅ ESCALAR: Campaña A
- CPA de $46.67 (el mejor) + conversión sólida de 3%.
- Intención de búsqueda alta ("software gestión inventario" = ya buscan tu producto).
- **Margen para crecer**: solo 50K impresiones, baja saturación. Puedes ganar más volumen sin disparar el CPA.

### ⚠️ OPTIMIZAR (no pausar todavía): Campaña C
- CPA alto ($88.89) **pero** la mejor calidad de tráfico (CTR 6%, conv 4%).
- El leads de competidor suelen tener **mayor LTV** (ya conocen la categoría, buscan alternativa).
- **Antes de juzgar**: necesitas saber si esos $88.89 se justifican con el valor del cliente. Si tu LTV > $300, sigue siendo rentable.

### 🛑 PAUSAR / REDUCIR: Campaña B
- **Esta es la clara perdedora.** Genera mucho tráfico barato pero NO convierte (0.5%).
- Consumió $1,800 para solo 24 signups → CPA $75.
- **El problema**: keywords informacionales ("cómo gestionar", "problemas inventario") = gente investigando, no comprando.

**Dato clave de oportunidad-costo:**
> Con los $1,800 de Campaña B, al CPA de Campaña A obtendrías ~38 signups extra en lugar de 24.

---

## 3. Redistribución de $5,000

| Campaña | Presupuesto Actual | Propuesto | Cambio |
|---------|--------------------|-----------| -------|
| **A (Landing)** | $2,100 | **$2,600** | +$500 |
| **C (Competidor)** | $3,200 | $1,900 | −$1,300 |
| **B (Blog)** | $1,800 → (fuera de los $5K? eran $7,100 total) | **$500** | reducir |

⚠️ **Nota importante**: tu gasto actual suma **$7,100**, no $5,000. Asumo que ya venías sobre-presupuesto. Aquí lo ajusto a tu límite real:

### Distribución recomendada ($5,000)
- **Campaña A: $2,800 (56%)** → escalar la ganadora gradualmente (+33%).
- **Campaña C: $1,700 (34%)** → reducir y enfocar solo en keywords con mejor conversión; bajar pujas.
- **Campaña B: $500 (10%)** → modo prueba/remarketing, NO captación directa.

**Proyección estimada** (manteniendo CPAs):
- A: ~60 signups | C: ~19 signups | B: ~7 signups → **~86 signups** vs. 105 actuales

> Ojo: bajas volumen total pero subes eficiencia. Si A escala sin degradar CPA, podrías superar los 105 con menos gasto. **Recomendación: escala A de forma incremental (+20% semanal) vigilando que el CPA no suba.**

---

## 4. A/B Tests sugeridos para el próximo mes

### Campaña A (la que vas a escalar)
1. **Landing page**: variante con CTA arriba vs. después de beneficios.
2. **Headline del anuncio**: enfoque en precio vs. enfoque en ahorro de tiempo.
3. **Form de signup**: campos reducidos (email solo) vs. form completo → mide impacto en conv. rate.

### Campaña B (rescate de tráfico)
4. **Cambiar el objetivo**: en vez de signup directo, ofrecer **lead magnet** (guía PDF "Cómo gestionar inventario") para capturar emails y nutrir después. El tráfico informacional convierte mejor con oferta de bajo compromiso.
5. **Remarketing**: re-impactar a quienes leyeron el blog con anuncios de Campaña A.

### Campaña C (la cara pero valiosa)
6. **Segmentar keywords**: separar "alternativa a X" vs. "X vs" → probablemente una convierte mejor; pausa la peor.
7. **Landing comparativa dedicada**: página "Nosotros vs [Competidor]" con tabla → suele subir conversión vs. landing genérica.

---

## ⚡ Recomendación final priorizada
1. **Hoy**: redirige presupuesto de B → A.
2. **Esta sem