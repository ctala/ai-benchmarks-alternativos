# Claude Opus 4.7 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-opus-4-7`
- success: True  | final: 7.01 | quality: 9.64
- latency_total: 48.046s | tokens_per_second: 65.8
- input_tokens: 6 | output_tokens: 3162
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.00% | 4.00% | **6.00%** |
| **CPC** | $1.40 | **$0.38** | $3.56 |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Conv. Rate** | 3.00% | 0.50% | **4.00%** |
| Signups | 45 | 24 | 36 |
| Costo total | $2,100 | $1,800 | $3,200 |

**Totales actuales:** $7,100 gastados (sobre presupuesto en $2,100) → 105 signups → **CPA blended: $67.62**

---

## 2. Decisión por campaña (justificada con números)

### 🟢 ESCALAR: Campaña A
- **CPA $46.67** = el más bajo de las 3 (38% mejor que B, 47% mejor que C)
- Conv rate de 3% es saludable para B2B
- Keywords transaccionales ("software gestión inventario") = intent de compra alto
- **Headroom**: solo 50k impresiones → hay volumen para crecer sin saturar el keyword

### 🔴 PAUSAR (o reestructurar): Campaña B
- **Conv rate 0.5%** = 6x peor que A, 8x peor que C
- A pesar del CPC barato ($0.38), el CPA termina en $75 porque las keywords son **informacionales** ("cómo gestionar", "problemas") = gente investigando, no comprando
- **No está mal el contenido — está mal el funnel**. Estos clicks deberían ir a blog post + email capture, no a signup directo
- Costo de oportunidad: $1,800 ahí = 38 signups extra en Campaña A

### 🟡 OPTIMIZAR antes de escalar: Campaña C
- **CTR 6%** + **conv rate 4%** = la audiencia de mayor intent de las 3
- Pero **CPC $3.56** está dragueando el CPA a $88.89 (subasta cara contra competidor)
- Vale la pena bajar CPC mejorando **Quality Score**: landing dedicada de comparación, ad copy más relevante, sitelinks específicos

---

## 3. Redistribución de $5,000

| Campaña | Presupuesto | % | Signups esperados (mismo CPA) | Acción |
|---|---|---|---|---|
| **A (escalar)** | **$3,000** | 60% | ~64 signups | +43% budget vs actual |
| **C (optimizar)** | **$1,700** | 34% | ~19 signups (asumiendo mismo CPA) | -47% pero con foco en bajar CPA a ~$60 → ~28 signups |
| **B (retargeting only)** | **$300** | 6% | ~4-8 signups | Solo retargeting de visitantes del blog hacia landing A |

**Proyección conservadora:** ~91-100 signups con $5,000 vs 105 actuales con $7,100 → **CPA blended cae de $67.62 a ~$53** (-22%).

**Alternativa más agresiva:** pausar B completamente, $3,200 a A + $1,800 a C → ~69 + ~20 = ~89 signups, CPA $56.

> **Por qué no todo a A**: diversificación de riesgo. Si Google cambia algo en la subasta de "software gestión inventario" o entra un competidor agresivo, no querés depender 100% de un solo keyword cluster.

---

## 4. A/B tests sugeridos próximo mes

### Campaña A (escalando — testear para subir conv rate de 3% a 4%+)
1. **Landing headline**: "Software de inventario para pymes" vs "Controla tu inventario en 5 minutos" (benefit vs feature)
2. **CTA del form**: "Crear cuenta gratis" vs "Probar 14 días sin tarjeta"
3. **Form length**: 3 campos (email + empresa + tamaño) vs 1 campo (solo email, resto en onboarding)
4. **Social proof above-the-fold**: testimonios vs logos de clientes vs número de pymes usando

### Campaña B (rescatar tráfico informacional)
5. **Funnel intermedio**: enviar tráfico a blog post con email capture (lead magnet: "Plantilla Excel control de inventario") en vez de signup directo. Hipótesis: conv rate de email capture 8-12% vs 0.5% actual → CPA de lead $5-8, después nurture por email
6. **Retargeting**: audiencia "visitó blog + no convirtió" → ads de Campaña A con descuento o caso de éxito

### Campaña C (bajar CPA de $89 a ~$60)
7. **Landing dedicada de comparación**: tabla "[Tu producto] vs [Competidor]" con feature matrix, pricing, testimonios de switchers. Hipótesis: conv rate sube de 4% a 6-7% por relevancia
8. **Ad copy con ángulo de switch**: "¿Cansado de [pain del competidor]?" vs genérico "Alternativa a X"

### Cross-campaña
9. **Lookalike audiences**: subir los 45 signups de A a Google Ads como customer match → generar audiencia similar para Display/YouTube de bajo CPC
10. **Dayparting**: revisar a qué horas convierten los 105 signups actuales. Probable que 8am-8pm L-V concentre 80%+ → recortar gasto fines de semana/madrugada

---

## TL;DR ejecutivo
- **Tu plata está mal asignada**: B gasta $1,800 en tráfico que no compra; C gasta $3,200 en tráfico caro pero buena calidad; A es la joya subfondeada.
- **Mueve $3,000 a A, $1,700 a C (optimizando QS), $300 a retargeting de B**.
- **Primer test prioritario**: lead magnet en Campaña B (cambia el funnel, no la creatividad). Es el cambio con mayor upside.