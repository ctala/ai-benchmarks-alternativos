# Claude Opus 4.7 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 29.992s | tokens_per_second: 61.4
- input_tokens: 398 | output_tokens: 1840
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para optimizar las campañas de marketing.

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.375 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Conv. Rate** | 3.00% | 0.50% | 4.00% |
| **Signups** | 45 | 24 | 36 |

**Fórmulas:**
- CTR = Clicks / Impresiones
- CPC = Costo / Clicks
- CPA = Costo / Signups
- Conv. Rate = Signups / Clicks

---

## 2. Qué escalar y qué pausar

### ✅ ESCALAR: Campaña A (Landing principal)
- **Mejor CPA ($46.67)** — 47% más barato que B, 48% más barato que C
- Alta intención de compra ("software gestión inventario" = usuario buscando solución)
- Conv. Rate de 3% es sólido para B2B SaaS
- **Es tu campaña más eficiente en dólares gastados por cliente.**

### ⚠️ OPTIMIZAR (no pausar aún): Campaña C (Competidor)
- CPA alto ($88.89) pero **Conv. Rate del 4% (el mejor)** — indica que quien llega está muy calificado
- El problema es el **CPC de $3.56** (guerra de pujas contra competidor)
- Estos leads suelen tener mayor LTV (ya conocen la categoría)
- **Acción:** Reducir presupuesto pero mantenerla activa; optimizar Quality Score

### 🛑 PAUSAR o REESTRUCTURAR: Campaña B (Blog content)
- **Conv. Rate de 0.5%** es alarmantemente bajo (6x peor que A)
- Aunque el CPC es barato ($0.375), el CPA final es peor
- Traduce: atrae tráfico pero **no compradores** — son investigadores en fase de aprendizaje
- **Acción:** Pausarla en Google Ads y mover ese contenido a estrategia SEO orgánica (donde el ROI es mucho mejor a largo plazo)

---

## 3. Redistribución del presupuesto ($5,000)

| Campaña | Actual | Propuesto | Cambio | Signups esperados |
|---------|--------|-----------|--------|-------------------|
| A (Landing) | $2,100 | **$3,300** | +57% | ~70 |
| B (Blog) | $1,800 | **$200** (test) | -89% | ~3 |
| C (Competidor) | $3,200 | **$1,500** | -53% | ~17 |
| **Total** | $7,100 | **$5,000** | | **~90 signups** |

**Nota:** Actualmente gastas $7,100 (excedes presupuesto). Con esta redistribución:
- Bajas costo total a $5,000
- Signups estimados: **~90 vs 105 actuales** (solo -14% signups con -30% presupuesto)
- **CPA promedio baja de $67 a ~$56**

Los $200 en Campaña B son para mantenerla viva y seguir testeando después de optimizar landing.

---

## 4. A/B Tests sugeridos para el próximo mes

### En Campaña A (tu ganadora — protege y expande)
1. **Landing page:** Testa headline enfocado en dolor ("Deja de perder inventario") vs. beneficio ("Controla tu inventario en 5 min")
2. **CTA:** "Prueba gratis 14 días" vs. "Ver demo en vivo"
3. **Ad copy:** Incluir precio en el anuncio vs. no incluirlo (filtra leads no calificados)

### En Campaña C (mejorar eficiencia)
4. **Landing dedicada de comparación:** "TuProducto vs [Competidor]" con tabla comparativa vs. landing genérica
5. **Ángulo del ad:** "Migra desde [Competidor] gratis" vs. "Por qué [Competidor] no es para pymes"

### En Campaña B (antes de pausar del todo)
6. **Lead magnet en vez de signup directo:** "Descarga: Guía de gestión de inventario" → nurture por email → signup. Esto puede rescatar ese 4,800 clicks/mes desperdiciados.

### Cross-campaña
7. **Segmentación por dispositivo:** Revisa si mobile vs desktop tienen conv. rates distintos (probablemente desktop convierte mejor en B2B)
8. **Dayparting:** ¿Los signups vienen en horario laboral? Concentra budget ahí.

---

## 💡 Insight clave
Tu **Campaña B tiene un problema de intención de búsqueda**, no de ejecución. Alguien buscando "cómo gestionar inventario" está aprendiendo, no comprando. Ese tráfico es oro para **contenido orgánico + email nurture**, no para conversión directa en Ads.

¿Quieres que profundice en la estructura de un funnel de nurture para recuperar ese tráfico del blog?