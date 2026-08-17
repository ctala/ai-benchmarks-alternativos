# Claude Sonnet 4.6 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-sonnet-4-6`
- success: True  | final: 7.27 | quality: 9.92
- latency_total: 58.893s | tokens_per_second: 55.4
- input_tokens: 3 | output_tokens: 3263
- judge_score: 5.0 | justificación: 

## Respuesta completa

## Análisis Completo Google Ads — Último Mes

---

### 1. 📊 Métricas calculadas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.0% | 4.0% | **6.0%** ✅ |
| **CPC** | $1.40 | **$0.38** ✅ | $3.56 |
| **CPA** | **$46.67** ✅ | $75.00 | $88.89 |
| **Conv. Rate** | 3.0% | 0.5% | **4.0%** ✅ |
| **Signups** | 45 | 24 | 36 |
| **Gasto actual** | $2,100 | $1,800 | $3,200 |

> ⚠️ **Nota crítica**: estás gastando **$7,100** con presupuesto de $5,000 — hay $2,100 de sobre-gasto que ya no tiene sentido discutir en retrospectiva, pero el mes que viene es evitable.

---

### 2. 🔍 Diagnóstico y decisión por campaña

#### ✅ Campaña A — **ESCALAR**
- **CPA $46.67** — la más eficiente por lejos
- Keywords transaccionales ("software gestión inventario") → usuario en modo compra
- Conversión del 3% sobre 1,500 clicks demuestra que el funnel funciona
- **Señal de escala**: si subes budget, la demanda de estas keywords aguanta más volumen

#### 🚫 Campaña B — **PAUSAR o transformar radicalmente**
- CTR de 4% con CPC de $0.38 suena bien **hasta que ves el 0.5% de conversión**
- De 4,800 clicks, solo 24 convierten → estas personas buscan información, no comprar
- Keywords TOFU ("cómo gestionar inventario") = audiencia educacional, no compradora
- Estás pagando $1,800 para "educar" a gente que no va a convertir ese mes
- **Excepción**: puede tener valor como fuente de audiencia para remarketing

#### ⚠️ Campaña C — **OPTIMIZAR antes de escalar (ni pausar ni escalar)**
- Conversión del **4%** = mejor de las tres, usuario con intención clara de cambiar
- Pero CPC de $3.56 infla el CPA a $88.89 — casi el doble que Campaña A
- El problema no es la audiencia, es el **costo por clic y probablemente el Quality Score**
- Tiene potencial real si bajas el CPA

---

### 3. 💰 Redistribución de $5,000

| Campaña | Presupuesto actual | Presupuesto propuesto | Lógica |
|---|---|---|---|
| **A (Landing)** | $2,100 | **$3,000** (+43%) | Mejor CPA, escalar directo |
| **B (Blog)** | $1,800 | **$400** (−78%) | Solo para alimentar audiencias de remarketing |
| **C (Competidor)** | $3,200 | **$1,600** (−50%) | Optimizar primero, escalar cuando CPA < $60 |
| **Total** | $7,100 | **$5,000** | |

**Proyección con nuevo presupuesto** (asumiendo mismos ratios iniciales):
- Campaña A: $3,000 / $46.67 = **~64 signups**
- Campaña B: $400 / $75 = **~5 signups** (más retargeting downstream)
- Campaña C: $1,600 / $88.89 = **~18 signups** (objetivo: bajar CPA a $60 → 27 signups)
- **Total proyectado: ~87 signups** vs 105 actuales, pero con $2,100 menos de gasto

> La reducción de signups es temporal y aceptable — estás eliminando los más caros ($75–$89) y reforzando los más baratos ($47).

---

### 4. 🧪 A/B Tests recomendados para el próximo mes

#### Campaña A (prioridad alta — es tu motor)
| Test | Variante A | Variante B | Métrica objetivo |
|---|---|---|---|
| **CTA landing page** | "Prueba gratis 14 días" | "Ver demo en vivo" | Conv. Rate > 3% |
| **Headline del anuncio** | Beneficio funcional: "Controla tu inventario en tiempo real" | Prueba social: "Más de 500 PYMEs ya gestionan con nosotros" | CTR + Conv. Rate |
| **Match type** | Broad Match (actual probablemente) | Exact Match "software gestión inventario" | CPA — puede bajar con más precisión |

#### Campaña B (si la mantienes reducida)
| Test | Descripción | Objetivo |
|---|---|---|
| **Oferta de conversión** | Cambiar CTA de "signup" → "Descarga guía gratis: Cómo reducir pérdidas en inventario" | Subir conversión de 0.5% a 3-5% con un lead magnet |
| **Audiencia remarketing** | Crear audiencia de los 4,800 clicks → retargetear en Display/YouTube | Recuperar intención latente con menor CPC |

#### Campaña C (prioridad alta — arreglar CPA)
| Test | Variante A | Variante B | Objetivo |
|---|---|---|---|
| **Landing page específica** | Landing genérica (actual) | Landing "¿Cansado de [Competidor]? Mira qué diferente es [Tu producto]" con comparativa feature vs feature | Conv. Rate > 5% |
| **Ángulo del anuncio** | Precio: "50% más barato que [Competidor]" | Experiencia: "Sin las limitaciones de [Competidor]" | CTR |
| **Bid strategy** | CPC manual | Target CPA $55 | CPA — dejar que el algoritmo optimice |

---

### 📌 Resumen ejecutivo

```
ESCALAR HOY  → Campaña A ($3,000) — CPA $46.67, motor principal
PAUSAR HOY   → Campaña B a $400 — 0.5% conv. rate es dinero quemado
CIRUGÍA      → Campaña C: nueva landing, target CPA $55, reducir a $1,600

Meta del mes próximo: 87+ signups con $5,000 (~$57 CPA promedio)
Meta de optimización: si Campaña C baja a CPA $60 → escalar a $2,000 en mes 3
```