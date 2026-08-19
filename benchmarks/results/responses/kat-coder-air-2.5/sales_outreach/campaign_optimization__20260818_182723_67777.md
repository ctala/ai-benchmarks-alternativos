# KAT Coder Air v2.5 — sales_outreach/campaign_optimization

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 21.598s | tokens_per_second: 201.0
- input_tokens: 309 | output_tokens: 4342

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa



Aquí tienes el análisis completo, paso a paso y con datos concretos:

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|--------|---------------------|------------------|------------------------|
| **CTR** | `(1.500 / 50.000) × 100 = **3.0%**` | `(4.800 / 120.000) × 100 = **4.0%**` | `(900 / 15.000) × 100 = **6.0%**` |
| **CPC** | `$2.100 / 1.500 = **$1.40**` | `$1.800 / 4.800 = **$0.38**` | `$3.200 / 900 = **$3.56**` |
| **Conversion Rate (CVR)** | `(45 / 1.500) × 100 = **3.0%**` | `(24 / 4.800) × 100 = **0.5%**` | `(36 / 900) × 100 = **4.0%**` |
| **CPA** | `$2.100 / 45 = **$46.67**` | `$1.800 / 24 = **$75.00**` | `$3.200 / 36 = **$88.89**` |

> ⚠️ Nota: El gasto reportado suma **$7.100**, superando tu presupuesto de $5.000. El análisis asume que buscas optimizar dentro del límite real.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escalar: **Campaña A**
- **CPA más bajo**: $46.67 (40% menos que B y 47% menos que C)
- **CVR sólido**: 3% (6× mayor que B, 75% de C)
- **CPC razonable**: $1.40 con intención comercial clara (`software`, `pymes`)
- **Proyección**: Con $3.200 generaría ~68 signups vs. los 45 actuales.

### 🛑 Pausar/Reducir: **Campaña B**
- **CPA más alto en eficiencia relativa**: $75.00
- **CVR crítico**: 0.5% → el tráfico es mayoritariamente **informacional**, no comercial.
- **CTR alto pero engañoso**: 4% refleja curiosidad, no intención de compra.
- **Conclusión**: Gasta $1.800 para solo 24 signups. No es escalable sin cambios estructurales.

### ⚠️ Mantener pero optimizar: **Campaña C**
- **CVR más alto** (4%) y **CTR más alto** (6%) → intención de cambio muy clara.
- **CPA alto** ($88.89) por CPC elevado ($3.56). No es pausable, pero requiere ajuste de pujas o landing específica antes de escalar.

---

## 3. Redistribución del presupuesto ($5.000)

| Campaña | Presupuesto | % | Signups esperados* | CPA estimado |
|---------|-------------|---|---------------------|--------------|
| **A** | $3.200 | 64% | ~68 | $46.67 |
| **C** | $1.500 | 30% | ~17 | $88.89 |
| **B** | $300 | 6% | ~4 | $75.00 |
| **Total** | $5.000 | 100% | **~89 signups** | **$56.18** |

*\*Proyección basada en CPA histórico. En la práctica, el CPA puede mejorar con optimización.*

**Por qué esta distribución:**
- **A recibe la mayor parte** porque es el motor de conversión más eficiente.
- **C se mantiene** por su alta intención de compra, pero con presupuesto reducido para no inflar el CPA promedio.
- **B se reduce a mínimo** (solo para no perder datos de aprendizaje o probar ajustes) o puedes **pausarla completamente** y reasignar sus $300 a A → lo que elevaría los signups esperados a **~92** y bajaría el CPA global a **$54.35**.

---

## 4. A/B Tests sugeridos para el próximo mes

| Prioridad | Qué testear | Hipótesis | Métrica de éxito |
|-----------|-------------|-----------|------------------|
| 🔴 Alta | **Landing de A**: Headline/CTA vs. formulario corto (3 campos) vs. formulario largo (5+ campos) | Reducir fricción aumentará el CVR de 3% a >4% | CVR, CPA, tasa de abandono |
| 🔴 Alta | **Campaña C**: Landing específica para "vs competidor" (comparativa + prueba social) vs. landing principal | Los usuarios que buscan alternativas ya están en fase de decisión; una página dedicada mejorará el CVR de 4% a >6% | CVR, CPA, tasa de scroll al CTA |
| 🟡 Media | **Campaña B**: Redirigir tráfico a un *lead magnet* (checklist/guía "5 errores de inventario") vs. artículo de blog directo | El contenido informativo no convierte; un recurso de valor capturará emails y nutrirá en el funnel | CVR, costo por lead, tasa de apertura posterior |
| 🟡 Media | **Match types**: Exact match vs. Phrase match en A y C | Restringir a exact/phrase reducirá impresiones irrelevantes y bajará el CPC sin matar volumen | CPC, CTR, CPA |
| 🟢 Baja | **Estrategia de puja**: Manual CPC vs. tCPA (objetivo $50) en A | Automatizar hacia conversiones estabilizará el CPA y liberará tiempo de optimización | CPA, volumen de signups, costo por click |

### Recomendación de ejecución:
1. **Lanza 2 tests simultáneos** (no más de 3) para no diluir el aprendizaje.
2. **Mantén cada test activo al menos 14 días** o hasta alcanzar ~100 conversiones por variante.
3. **Revisa antes de decidir**: Si un test no muestra diferencia estadística (p < 0.05), no lo implementes aunque la tendencia sea favorable.

---

¿Quieres que te arme un **calendario de tests** o un **dashboard simple en Sheets** para monitorear estas métricas semanales?