# Ling 3.0 Flash — sales_outreach/campaign_optimization

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 8.762s | tokens_per_second: 384.3
- input_tokens: 339 | output_tokens: 3367
- judge_score: 5.0 | justificación: 

## Respuesta completa

# 📊 Análisis Completo de Campañas Google Ads

---

## 1. Métricas Calculadas

| Métrica | 🎯 Campaña A (Landing) | 📝 Campaña B (Blog) | ⚔️ Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.375 | $3.56 |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Conversion Rate** | 3.00% | 0.50% | 4.00% |
| **Costo por signup** | $46.67 | $75.00 | $88.89 |

### Fórmulas usadas:
- **CTR** = Clicks ÷ Impresiones × 100
- **CPC** = Costo ÷ Clicks
- **CPA** = Costo ÷ Signups
- **Conversion Rate** = Signups ÷ Clicks × 100

---

## 2. ¿ Escalar o Pausar? — Justificación con números

### 🟢 Campaña A → **ESCALAR**
- **CPA de $46.67** — es la más eficiente, un **37% más barata** que B y un **47% más barata** que C.
- **Conversion rate del 3.00%** — sólida y consistente.
- Cada signup cuesta lo mínimo entre las tres. Es la campaña que **genera valor real** al menor costo.
- Tiene **intención transaccional** directa ("software gestión inventario", "inventario pymes").

### 🔴 Campaña B → **PAUSAR (o reducir drásticamente)**
- **CPA de $75.00** — la más cara de las tres, **61% más cara que A**.
- **Conversion rate del 0.50%** — es 6x peor que A y 8x peor que C.
- Aunque el CTR (4%) y CPC ($0.375) parecen atractivos, el tráfico es **informativo/top de funnel**. La gente busca "cómo gestionar inventario" — está investigando, no comprando.
- **$1,800 gastados → solo 24 signups**. El retorno es pésimo si el objetivo es conversión.
- **Veredicto:** El tráfico es barato pero no convierte. No justifica el presupuesto con el objetivo actual de signups.

### 🟡 Campaña C → **MANTENER CON OPTIMIZACIÓN**
- **CPA de $88.89** — la más alta, pero tiene la **mejor conversion rate (4.00%)** de todas.
- El tráfico de competidor tiene **alta intención**: quien busca "alternativa a X" ya tiene un problema y está comparando soluciones.
- El CPC alto ($3.56) infla el CPA, pero la **calidad del signup es superior** (menor tasa de churn probable).
- No hay suficientes impresiones (15,000) para juzgar su potencial real. **Podría escalar si se baja el CPC.**

---

## 3. Redistribución del Presupuesto de $5,000/mes

| Campaña | Presupuesto Anterior | **Nuevo Presupuesto** | % del Total | Justificación |
|---|---|---|---|---|
| 🎯 **A (Landing)** | $2,100 | **$2,800** | 56% | Escalar la más eficiente. Con el CPC actual ($1.40), obtendrías ~2,000 clicks y ~60 signups estimados. |
| ⚔️ **C (Competidor)** | $3,200 | **$1,800** | 36% | Reducir pero no eliminar. Bajar bidding manualmente para reducir CPC de $3.56 a ~$2.50. Esto baja el CPA a ~$63 y mantiene tráfico cualificado. |
| 📝 **B (Blog)** | $1,800 | **$400** | 8% | Reducir a mínimo para mantener presencia de marca y recolectar datos de keyword. O pausar completamente si no hay margen. |

### Proyección estimada con nueva distribución:

| Campaña | Clicks estimados | Signups estimados | CPA proyectado |
|---|---|---|---|
| A | ~2,000 | ~60 | $46.67 |
| C | ~500 | ~20 | $90.00* |
| B | ~1,067 | ~5 | $80.00* |
| **Total** | **~3,567** | **~85** | **$58.82** |

*\*Proyecciones conservadoras asumiendo que las métricas se mantienen. Si optimizas la Campaña C (bajar CPC), el CPA mejora significativamente.*

> 💡 **Con $2,800 en Campaña A sola**, proyectas ~60 signups a $46.67 CPA. Eso es **~16% más signups** que el total actual combinado ($7,100 gastados → 105 signups).

---

## 4. A/B Tests Sugeridos para el Próximo Mes

### 🔬 Test 1 — Landing Page de Campaña A (Prioridad Alta)
- **Variable:** Headline y propuesta de valor
- **Versión A (control):** Landing actual
- **Versión B:** Headline centrado en resultado + CTA específico (ej: "Gestiona tu inventario en 5 minutos" vs. "El mejor software de inventario")
- **Métrica a monitorear:** Conversion rate y CPA
- **Por qué:** La Campaña A ya convierte bien; un pequeño lift en la tasa de conversión tiene impacto directo en CPA.

### 🔬 Test 2 — Anuncios de Campaña C (Competidor)
- **Variable:** Copy de anuncio (mensaje de dolor vs. mensaje de beneficio)
- **Versión A:** "¿Problemas con [competidor]? Prueba [tu producto]" (dolor)
- **Versión B:** "La alternativa que [número] pymes eligen para gestionar inventario" (beneficio + prueba social)
- **Métrica a monitorear:** CTR y CPA
- **Por qué:** El CPC es alto ($3.56). Un CTR más alto con el mismo presupuesto reduce el CPA y permite más impressions.

### 🔬 Test 3 — Rediseño de Campaña B (o reactivación inteligente)
- **Variable:** Tipo de campaña y mensaje
- **Versión A (actual):** Campaña de blog con keywords informational
- **Versión B:** Campaña de **remarketing** dirigida a visitantes de Campaña A que no convirtieron, con contenido de blog como herramienta de nurturing
- **Métrica a monitorear:** CPA y tasa de conversión
- **Por qué:** El tráfico de blog no convierte en primera instancia, pero podría funcionar como segundo toque para usuarios que ya conocen la marca.

### 🔬 Test 4 — Extensiónes de anuncio (todas las campañas)
- **Variable:** Sin extensiones vs. con extensiones (sitelinks, callouts, structured snippets)
- **Métrica a monitorear:** CTR y CPA
- **Por qué:** Las extensiones suelen mejorar CTR entre 10-30% sin aumentar el CPC, lo que baja el CPA automáticamente.

### 🔬 Test 5 — Segmentación horaria (Campaña A y C)
- **Variable:** Horarios de exposición
- **Hipótesis:** Los clics en horario laboral (9am-2pm) convierten mejor que los de fin de semana
- **Métrica a monitorear:** CPA por franja horaria
- **Por qué:** Permite concentrar el presupuesto en los horarios de mayor conversión y reducir desperdicio.

---

## 📌 Resumen Ejecutivo

| Acción | Campaña | Razón principal |
|---|---|---|
| **ESCALAR** | A | Mejor CPA ($46.67), mejor balance eficiencia/ volumen |
| **PAUSAR** | B | CPA excesivo ($75), conversión baja (0.5%), tráfico no intencional |
| **OPTIMIZAR** | C | Alta calidad (4% conversión) pero CPC caro; reducir bidding para mejorar CPA |

> **Regla de oro:** Con $5,000/mes, tu mayor apalancamiento está en la Campaña A. Cada dollar invertido ahí genera ~2.14x más signups que la Campaña B y ~1.88x más que la Campaña C.