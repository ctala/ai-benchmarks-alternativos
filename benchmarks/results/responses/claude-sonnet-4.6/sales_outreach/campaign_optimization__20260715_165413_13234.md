# Claude Sonnet 4.6 (ultimo Anthropic) — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 6.8 | quality: 8.0
- latency_total: 36.93s | tokens_per_second: 55.5
- input_tokens: 316 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Análisis Google Ads - Diagnóstico Completo

## 1. Métricas Calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.375 | $3.56 |
| **Conv. Rate** | 3.0% | 0.5% | 4.0% |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Costo total** | $2,100 | $1,800 | $3,200 |
| **Signups totales** | 45 | 24 | 36 |

**Cálculos verificables:**
- CTR = Clicks/Impresiones → Ej. Campaña A: 1,500/50,000 = 3.0%
- CPC = Costo/Clicks → Ej. Campaña A: $2,100/1,500 = $1.40
- Conv. Rate = Signups/Clicks → Ej. Campaña A: 45/1,500 = 3.0%
- CPA = Costo/Signups → Ej. Campaña A: $2,100/45 = $46.67

---

## 2. Decisiones: Escalar vs Pausar

### ✅ ESCALAR → Campaña A (Landing Principal)

**Por qué con números:**
- CPA de **$46.67** → el más bajo del portfolio (37% más barato que B, 47% más barato que C)
- Conv. Rate de **3.0%** → sólido para software B2B
- CPC de **$1.40** → eficiencia excelente
- **Problema real:** Solo gasta $2,100 de $5,000 disponibles → capital mal asignado

> Si escalas a $3,500 manteniendo CPA constante → proyección: **~75 signups** (+67%)

---

### ⚠️ REDUCIR DRÁSTICAMENTE → Campaña C (Competidor)

**Por qué con números:**
- CPA de **$88.89** → casi el doble que Campaña A
- Gasta **$3,200** (64% del presupuesto total) generando solo 36 signups
- Con ese mismo presupuesto en Campaña A → proyectarías **~68 signups** al CPA de $46.67
- **El CTR alto (6%) engaña:** la gente hace click por curiosidad comparativa, pero convierte peor

> **Salvaje pero real:** Campaña C está "quemando" ~$1,900 extra versus redirigir ese dinero a Campaña A para los mismos resultados

---

### 🔄 OPTIMIZAR ANTES DE DECIDIR → Campaña B (Blog)

**El problema no es el tráfico, es el destino:**
- CTR de 4.0% → la gente SÍ hace click (keywords informacionales funcionan)
- Conv. Rate de **0.5%** → la landing/CTA está fallando completamente
- Genera 4,800 clicks pero solo 24 signups → **4,776 clicks desperdiciados**
- CPC barato ($0.375) pero CPA caro ($75) → problema de conversión, no de tráfico

> Antes de pausar: test de 30 días con landing específica para intención informacional

---

## 3. Redistribución de Presupuesto ($5,000)

```
ACTUAL (problemático):
├── Campaña A: $2,100 (42%) → genera 45 signups
├── Campaña B: $1,800 (36%) → genera 24 signups  
└── Campaña C: $3,200 (64%) → genera 36 signups
                              TOTAL: 105 signups | CPA promedio: $67.62
```

```
PROPUESTO:
├── Campaña A: $3,000 (60%) → proyección: ~64 signups
├── Campaña B: $1,200 (24%) → proyección: ~16 signups (con nueva landing)
└── Campaña C:   $800 (16%) → proyección: ~9 signups
                              TOTAL: ~89 signups | CPA promedio: $56.18
```

**Espera... ¿menos signups totales?** Sí, en el escenario conservador. Pero:

| | Actual | Propuesto |
|---|---|---|
| Signups | 105 | ~89-105 |
| CPA promedio | $67.62 | $47-56 |
| **Ahorro por signup** | - | **~$11-20 menos** |
| **Margen para escalar** | - | Reinvertir ahorro |

> La lógica real: bajar CPA primero → luego escalar con presupuesto liberado

**Si tu LTV lo justifica**, la versión agresiva sería:

```
VERSIÓN AGRESIVA (si CPA < LTV/3):
├── Campaña A: $4,000 (80%) → proyección: ~85 signups
├── Campaña B:   $600 (12%) → solo retención/test
└── Campaña C:   $400 (8%)  → keywords de mayor intención únicamente
```

---

## 4. A/B Tests Recomendados

### 🧪 Test 1 → Campaña B: Landing por intención (PRIORIDAD MÁXIMA)

**Hipótesis:** El 0.5% de conversión se debe a un mismatch entre intención informacional y landing transaccional

| Variante | Descripción |
|---|---|
| **Control** | Landing actual (venta directa) |
| **Variante A** | Landing educacional → CTA "Descarga guía gratis" → nurture sequence |
| **Variante B** | Landing híbrida → Artículo + demo embebida al 50% del scroll |

**Métrica de éxito:** Conv. Rate > 1.5% (3x actual)
**Duración:** 21 días mínimo / 500 clicks por variante

---

### 🧪 Test 2 → Campaña A: Headline del anuncio

**Hipótesis:** Puedes mejorar CTR de 3% → 4%+ con messaging más específico

| Variante | Headline |
|---|---|
| **Control** | "Software Gestión Inventario" |
| **Variante A** | "Gestiona tu Inventario en 15 min/día" *(beneficio específico)* |
| **Variante B** | "Inventario para PyMEs · Prueba 14 días gratis" *(oferta explícita)* |

**Métrica de éxito:** CTR > 4% manteniendo Conv. Rate ≥ 2.5%

---

### 🧪 Test 3 → Campaña C: Segmentación de keywords

**Hipótesis:** No todas las keywords de competidor tienen igual intención de compra

| Grupo | Keywords | Acción |
|---|---|---|
| **Alta intención** | "[competidor] precio", "[competidor] alternativa barata" | Mantener |
| **Media intención** | "[competidor] vs [tu marca]" | Reducir bid 30% |
| **Baja intención** | "[competidor] tutorial", "[competidor] soporte" | Pausar |

**Métrica de éxito:** Reducir CPA de $88 → $65 manteniendo volumen

---

### 🧪 Test 4 → Global: Match types

**Hipótesis:** Broad match está generando tráfico irrelevante en Campaña B

```
Actual (probable): Broad match → mucho volumen, baja conversión
Test: