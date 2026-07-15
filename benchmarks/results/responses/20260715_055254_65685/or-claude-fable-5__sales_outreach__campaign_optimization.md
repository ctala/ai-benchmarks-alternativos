# Claude Fable 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 31.939s | tokens_per_second: 73.7
- input_tokens: 393 | output_tokens: 2353
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para optimizar la campaña de marketing.

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

⚠️ **Nota importante:** Gastaste **$7,100** con un presupuesto de $5,000. Hay un sobregasto del 42% que hay que corregir.

---

## 2. ¿Cuál escalar y cuál pausar?

### 🚀 Escalar: Campaña A
- **CPA más bajo ($46.67)** — 38% más barato que B y 47% más barato que C
- Keywords de **alta intención comercial** ("software gestión inventario" = alguien buscando comprar)
- Conversion rate sólido (3%) con volumen razonable de impresiones (50K), lo que sugiere que hay espacio para crecer

### ⏸️ Pausar (o reestructurar): Campaña B
- Conversion rate de **0.5%** — 6-8x peor que A y C
- Aunque el CPC es baratísimo ($0.38), el tráfico es informacional ("cómo gestionar inventario" = alguien buscando aprender, no comprar)
- Su CPA de $75 es engañoso: estás pagando por volumen de tráfico que no convierte
- **No la mates del todo**: ese tráfico tiene valor para remarketing (ver punto 3)

### 🔧 Optimizar: Campaña C
- Tiene el **mejor CTR (6%) y mejor conversion rate (4%)** — la intención es excelente
- El problema es el **CPC de $3.56** (2.5x el de A), que infla el CPA a $88.89
- No la pauses: las keywords de competidor capturan usuarios en decisión de compra. Necesita optimización de pujas, no eliminación

---

## 3. Redistribución del Presupuesto ($5,000)

| Campaña | Presupuesto | % | Racional |
|---|---|---|---|
| **A (Landing)** | $2,750 | 55% | Escalar el mejor CPA. Con CPA constante → ~59 signups |
| **C (Competidor)** | $1,500 | 30% | Reducir gasto pero mantener presencia. Bajar pujas y ser más selectivo con keywords → ~17-20 signups |
| **B → Remarketing** | $500 | 10% | Pausar search, usar el presupuesto para **remarketing display/YouTube** al tráfico del blog (audiencia ya construida) |
| **Reserva/testing** | $250 | 5% | Buffer para A/B tests y nuevas keywords |

**Proyección conservadora: ~80-85 signups vs. 105 actuales, pero con $2,100 menos de gasto.** El CPA blended bajaría de ~$67.60 a ~$60, y si el remarketing funciona, podrías superar los signups actuales dentro del presupuesto.

---

## 4. A/B Tests para el Próximo Mes

### Campaña A (prioridad alta — es tu motor de crecimiento)
1. **Landing page: headline orientado a beneficio vs. feature** — "Reduce pérdidas de inventario 30%" vs. "Software de gestión de inventario"
2. **Formulario de signup: corto (email) vs. actual** — con 3% de conversión, reducir fricción puede ser la palanca más rápida
3. **Ad copy: precio/prueba gratis en el anuncio vs. sin mencionarlo** — pre-calificar clicks

### Campaña C
4. **Landing dedicada de comparación** ("[Tu producto] vs [Competidor]" con tabla comparativa) vs. landing genérica — con 4% de conversión y tráfico tan calificado, una página específica podría llevarlo a 6-8% y justificar el CPC alto
5. **Estrategia de puja: CPA objetivo ($60) vs. maximizar clicks** — controlar el CPC inflado

### Campaña B / Remarketing
6. **Lead magnet en el blog** (plantilla de inventario descargable vs. CTA directo a signup) — capturar emails del tráfico informacional y nutrirlo, en vez de esperar conversión directa

### Regla para los tests
Con tu volumen actual (~45 signups/mes en A), prueba **un cambio a la vez** y espera significancia estadística (mínimo ~2-3 semanas o 100+ conversiones por variante en tests de landing). Prioriza los tests de la Campaña A porque es donde más volumen tienes.

---

**Resumen ejecutivo:** Escala A, convierte B en remarketing, optimiza el costo de C, y enfoca los tests en mejorar la conversión de tu landing principal. El objetivo del próximo mes: CPA blended < $55.