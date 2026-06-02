# MiniMax M3 — sales_outreach/campaign_optimization

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.65 | quality: 9.92
- latency_total: 105.015s | tokens_per_second: 27.7
- input_tokens: 426 | output_tokens: 2904
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **CTR** | 3.00% | 4.00% | **6.00%** ✅ |
| **CPC** | $1.40 | **$0.38** ✅ | $3.56 |
| **CPA** | **$46.67** ✅ | $75.00 | $88.89 |
| **Conv. Rate** | 3.00% | 0.50% | **4.00%** ✅ |

**Fórmulas usadas:**
- CTR = Clicks / Impresiones
- CPC = Costo / Clicks
- CPA = Costo / Signups
- Conv. Rate = Signups / Clicks

> ⚠️ **Alerta importante:** El costo total ($7,100) supera tu presupuesto de $5,000. Estás sobre-gastando un 42%.

---

## 2. ¿Escalar o Pausar?

### 🟢 ESCALAR: Campaña A (Landing principal)
- **Mejor CPA del portafolio** ($46.67)
- Cada dólar invertido genera más signups que las demás
- **Proyección:** si escalas 50%, podrías pasar de 45 → ~67 signups con el mismo CPA
- Keywords de alta intención transaccional ("software gestion inventario")

### 🔴 PAUSAR (o reducir drásticamente): Campaña B (Blog)
- Conversion rate de **0.50%** = 1 de cada 200 clicks se registra
- $1,800 quemados en tráfico que no convierte
- **Diagnóstico probable:** el blog atrae lectores top-of-funnel que no están listos para comprar. No es culpa del anuncio, es un mismatch de expectativa.
- **Excepción:** pausar solo si el signup no es la métrica correcta. Si buscas awareness/MQLs para nutrir después, mantenla con presupuesto mínimo.

### 🟡 MANTENER CON CAUTELA: Campaña C (Competidor)
- CPA más alto ($88.89) pero **mejor CR (4%)** y CTR (6%)
- Estos usuarios ya están en modo compra, solo comparan opciones
- **Decisión depende del LTV:** si tu LTV > $89, es rentable. Si no, reduce.

---

## 3. Redistribución de Presupuesto ($5,000)

| Campaña | Actual | Propuesto | Cambio | Razón |
|---------|--------|-----------|--------|-------|
| **A** | $2,100 (30%) | **$2,800** (56%) | +$700 | Mejor CPA, escalar agresivamente |
| **B** | $1,800 (25%) | **$300** (6%) | -$1,500 | Pausar ads, mantener SEO orgánico |
| **C** | $3,200 (45%) | **$1,500** (30%) | -$1,700 | Mantener presencia, reducir volumen |
| **Testing** | $0 | **$400** (8%) | +$400 | Reservar para A/B tests |

**Proyección conservadora con presupuesto eficiente:**

| Campaña | Inversión | Signups estimados | CPA resultante |
|---------|-----------|-------------------|----------------|
| A | $2,800 | ~60 | $46.67 |
| B | $300 | ~4 | $75.00 |
| C | $1,500 | ~17 | $88.89 |
| **Total** | **$5,000** | **~81** | **$61.73** |

📉 Pasas de $67.62 CPA global a **$61.73**, con un volumen similar pero sin sobre-gasto.

---

## 4. A/B Tests Sugeridos para el Próximo Mes

### 🎯 Test #1: Landing page Campaña A (alto impacto)
- **Variante A:** Formulario corto (email + empresa)
- **Variante B:** Formulario con campo de "tamaño de inventario" (qualifica lead)
- **Hipótesis:** Menos fricción = más signups, aunque la calidad baje marginalmente

### 🎯 Test #2: Ad Copy Campaña C (alta intención)
- **Variante A:** Enfoque en precio ("Más económico que [competidor]")
- **Variante B:** Enfoque en features ("Migración en 24h desde [competidor]")
- **Hipótesis:** Resuelve objeción principal del usuario que viene de competidor

### 🎯 Test #3: Bid Strategy Campaña A
- **Actual:** Manual CPC
- **Test:** Target CPA ($50) con Smart Bidding
- **Hipótesis:** El algoritmo de Google puede encontrar conversiones más baratas que la gestión manual

### 🎯 Test #4: Match Types Campaña B (antes de pausar)
- **Variante A:** Broad match
- **Variante B:** Exact match en long-tails específicos
- **Razón:** Reducir impresiones irrelevantes que disparan CTR falso

### 🎯 Test #5: Negativas keywords
- Agregar términos como: "gratis", "gratuito", "código", "tutorial", "definición" en Campaña B
- **Impacto esperado:** filtrar el tráfico top-of-funnel no comprador

---

## Resumen Ejecutivo

> **Tu gema escondida es la Campaña A.** Está entregando el mejor CPA y probablemente tiene techo para crecer. La B es un drenaje, y la C vale la pena solo si el LTV del cliente lo justifica. **Deja de medir las tres con la misma vara** — B debería tener otra métrica objetivo (engagement, branded search lift) o pausarse.