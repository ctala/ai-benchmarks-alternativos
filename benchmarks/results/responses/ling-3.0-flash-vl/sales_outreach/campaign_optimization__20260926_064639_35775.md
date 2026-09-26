# Ling 3.0 Flash VL — sales_outreach/campaign_optimization

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 7.9 | quality: 8.0
- latency_total: 26.47s | tokens_per_second: 146.7
- input_tokens: 339 | output_tokens: 3883

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

# 📊 Análisis Completo de Campañas Google Ads

---

## 1. Métricas Calculadas por Campaña

| Métrica | Campana A (Landing) | Campana B (Blog) | Campana C (Competidor) |
|---|---|---|---|
| **CTR** | 1,500 / 50,000 = **3.00%** | 4,800 / 120,000 = **4.00%** | 900 / 15,000 = **6.00%** |
| **CPC** | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.375** | $3,200 / 900 = **$3.56** |
| **CPA** | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |
| **Conv. Rate** | 45 / 1,500 = **3.00%** | 24 / 4,800 = **0.50%** | 36 / 900 = **4.00%** |
| **Costo por 100 impresiones** | $0.42 | $0.15 | $2.13 |

### Observaciones clave:
- **Campana A** tiene el **CPA más bajo** ($46.67) y una conversión sólida (3%).
- **Campana B** tiene el **CPC más barato** ($0.375) y buen CTR (4%), pero la conversión es **muy baja** (0.5%).
- **Campana C** tiene el **mejor CTR** (6%) y **mejor tasa de conversión** (4%), pero el **CPC** ($3.56) y **CPA** ($88.89) son los más altos.

> ⚠️ **Nota:** Tu gasto actual total es **$7,100**, superando tu presupuesto de $5,000. Hay que optimizar urgentemente.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ **ESCALAR → Campana A (Landing Principal)**

**Justificación:**
- Tiene el **CPA más bajo** de todas las campañas: **$46.67** (41% más barato que B y 48% más barato que C).
- Conversion rate de **3.00%** es excelente para una landing de captación directa.
- El CPC de $1.40 es razonable y sostenible.
- Las keywords de **intención transaccional** ("software gestion inventario", "inventario pymes") captan usuarios que ya buscan tu solución.
- **Es la campaña que más eficientemente convierte dinero en signups.**

### ⚠️ **MANTENER (reducida) → Campana B (Blog Content)**

**Justificación:**
- El CPC de $0.375 es **excelente** y el CTR de 4% demuestra que los anuncios son atractivos.
- **El problema es la conversión** (0.5%). Esto indica un **funnel desalineado**: el blog atrae tráfico informacional que no está listo para registrarse.
- No pausarla porque tiene potencial: si mejoras la conversión del landing del blog, el CPA podría caer drásticamente.
- Funciona como **top-of-funnel** para generar awareness y autoridad.

### ❌ **PAUSAR (o reducir al mínimo) → Campana C (Competidor)**

**Justificación:**
- Aunque tiene la **mejor tasa de conversión** (4%) y el **mejor CTR** (6%), el **CPA de $88.89 es insostenible** — casi el doble que Campana A.
- Las keywords de competidor tienen **intención alta pero volumen bajo** (solo 15,000 impresiones).
- Con un presupuesto limitado a $5,000, no puedes permitirte un CPA de ~$89.
- **Excepción:** Si los signups de Campana C tienen un LTV (valor de vida del cliente) significativamente mayor, podrías mantenerla con un presupuesto mínimo de prueba ($500-$1,000).

---

## 3. Redistribución del Presupuesto de $5,000

| Campaña | Presupuesto Actual | Propuesto | Cambio | Justificación |
|---|---|---|---|---|
| **A (Landing)** | $2,100 | **$2,800** | +$700 (+33%) | Escalar la campaña más eficiente |
| **B (Blog)** | $1,800 | **$1,200** | -$600 (-33%) | Reducir pero mantener para testing |
| **C (Competidor)** | $3,200 | **$1,000** | -$2,200 (-69%) | Reducir drásticamente o pausar |
| **Total** | $7,100 | **$5,000** | -$2,100 | Dentro del presupuesto |

### Resultados proyectados con el nuevo presupuesto:

| Campaña | Clics Estimados | Signups Estimados | CPA Esperado |
|---|---|---|---|
| **A** | ~2,000 | ~60 | ~$46.67 |
| **B** | ~3,200 | ~16 | ~$75.00 (mejorando con tests) |
| **C** | ~280 | ~11 | ~$88.89 |
| **Total** | **~5,480** | **~87** | **~$57.47 promedio** |

### 📈 Comparación vs. situación actual:
- **Ahora:** 87 signups por $7,100 → CPA promedio: **$81.61**
- **Propuesto:** 87 signups por $5,000 → CPA promedio: **$57.47**
- **Ahorro:** $2,100 con los mismos signups → **26% más eficiente**

### Estrategia adicional:
- Destinar los **$2,100 ahorrados** a un fondo de experimentación para el próximo mes.
- Si Campana C con $1,000 no rinde bien en 2 semanas → **pausarla completamente** y redistribuir sus $1,000 a Campana A.

---

## 4. A/B Tests Sugeridos para el Próximo Mes

### 🔵 Campana A — Landing Principal ($2,800)

| Test | Variante A (Control) | Variante B | Métrica a optimizar |
|---|---|---|---|
| **Headline** | Actual | Incluir nombre del competidor ("La mejor alternativa a [X]") | CTR del anuncio |
| **CTA** | Botón "Registrarse" | Botón "Probar gratis 14 días" | Tasa de conversión |
| **Social Proof** | Sin testimonios | 3 testimonios de clientes | Tasa de conversión |
| **Formulario** | Formulario largo (5 campos) | Formulario corto (3 campos: email, empresa, teléfono) | Tasa de conversión |
| **Página de destino** | Landing genérica | Landing específica para "inventario pymes" vs "software gestion inventario" | CPA por segmento |

### 🟢 Campana B — Blog Content ($1,200)

| Test | Variante A (Control) | Variante B | Métrica a optimizar |
|---|---|---|---|
| **Landing del blog** | Blog sin CTA prominente | Blog con popup/CTA "Descarga guía gratuita" (lead magnet) | Conversión |
| **Tipo de contenido** | Artículos de blog | Videos cortos + infografías + blog | CTR y tiempo en página |
| **CTA en anuncio** | "Leer más" | "Descarga gratis: Guía de gestión de inventario" | CPC efectivo y conversión |
| **Retargeting** | Sin retargeting | Segmentar visitantes del blog que no se registraron → anuncios de remarketing | Conversión en 30 días |
| **Keywords** | "cómo gestionar inventario" | Añadir "inventario para restaurantes [tu ciudad]" | Intención de compra |

### 🔴 Campana C — Competidor ($1,000)

| Test | Variante A (Control) | Variante B | Métrica a optimizar |
|---|---|---|---|
| **Anuncios** | "[Competidor] vs [Tu marca]" | Anuncios con beneficio específico ("Más barato que [X], mismas funciones") | CTR y CPC |
| **Landing** | Landing genérica comparativa | Landing con tabla de comparación interactiva | Conversión |
| **Keywords** | "alternativa a [competidor]" | Añuir "mejor software inventario 2025" (búsqueda de intención) | Calidad del tráfico |

---

## 📋 Resumen Ejecutivo de Recomendaciones

1. **Escala Campana A** → Es tu motor de conversiones. Atribuye el 56% del presupuesto.
2. **Mantén Campana B** pero reducida → Tiene potencial oculto. El problema es conversión, no tráfico. Invierte en retargeting y lead magnets.
3. **Corta Campana C** drásticamente → Solo $1,000 para validar si el LTV justifica el CPA alto.
4. **Prioriza los tests de conversión** en Campana B — si logras pasar del 0.5% al 1.5% de conversión, su CPA caería de $75 a ~$25, convirtiéndola en la campaña más rentable.
5. **Mide el LTV** de signups por campaña — si los de Campana C valen 3x más que los de A, el CPA de $88 puede justificarse.