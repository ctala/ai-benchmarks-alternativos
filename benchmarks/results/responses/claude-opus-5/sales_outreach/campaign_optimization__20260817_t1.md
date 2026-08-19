# Claude Opus 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 99.627s | tokens_per_second: 68.6
- input_tokens: 393 | output_tokens: 6833

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

# Análisis de tus 3 campañas

## 1. Métricas calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) | **Blended** |
|---|---|---|---|---|
| Impresiones | 50,000 | 120,000 | 15,000 | 185,000 |
| Clicks | 1,500 | 4,800 | 900 | 7,200 |
| **CTR** | 3.00% | **4.00%** | **6.00%** | 3.89% |
| **CPC** | $1.40 | **$0.38** | $3.56 | $0.99 |
| Signups | 45 | 24 | 36 | 105 |
| **Conv. rate** | 3.00% | **0.50%** | **4.00%** | 1.46% |
| Costo | $2,100 | $1,800 | $3,200 | $7,100 |
| **CPA** | **$46.67** | $75.00 | **$88.89** | $67.62 |

### 🚨 Hallazgo #1 (el más importante): estás gastando $7,100, no $5,000

Tu presupuesto es $5,000/mes y gastaste **$7,100 = 42% de sobregiro**. Antes de optimizar nada, esto significa que cualquier redistribución implica **recortar $2,100 reales**, no solo mover dinero. Revisa si estás usando presupuestos a nivel campaña sin presupuesto compartido — Google puede gastar hasta 2x el presupuesto diario en un día individual.

### Índice de eficiencia (% de signups ÷ % de costo)

| Campaña | % del gasto | % de signups | Índice | Lectura |
|---|---|---|---|---|
| A | 29.6% | 42.9% | **1.45** | Subfinanciada |
| B | 25.4% | 22.9% | 0.90 | Ligeramente ineficiente |
| C | 45.1% | 34.3% | **0.76** | Sobrefinanciada |

---

## 2. Qué escalar y qué pausar

### ✅ ESCALAR: Campaña A
- CPA de **$46.67 = 31% mejor** que el blended y **47% mejor** que C.
- Conversion rate de 3% con intención comercial clara ("software gestión inventario" = alguien buscando comprar).
- CTR de 3% es el más bajo de las tres → **hay upside en creativos**, no está saturada.
- **Pregunta crítica que necesito responder antes de escalar duro:** ¿cuál es tu *Search Impression Share*? Si está en 40-60%, puedes duplicar volumen casi al mismo CPA. Si está en 85%+, el dinero extra se irá a keywords peores y el CPA subirá 30-50%. Esta métrica define si el escalado es de +50% o de +150%.

### ⚠️ REESTRUCTURAR (no pausar): Campaña C
Es la que más plata consume (45%) con el peor CPA. Pero **ojo**: tiene el mejor conversion rate (4%) y el mejor CTR (6%). El problema no es la audiencia, es el **CPC de $3.56** (2.5x el de A).

Por qué el CPC está tan alto y qué hacer:
- Keywords de marca ajena = Quality Score bajo estructural (no puedes poner la marca del competidor en el anuncio por política de trademark → ad relevance baja).
- `"[competidor] vs"` probablemente está en broad/phrase y captura búsquedas **inversas** (gente que ya usa tu producto o compara con un tercero irrelevante).
- **Acción:** segmenta por keyword. Casi seguro `alternativa a [competidor]` tiene CPA de ~$50-60 y `[competidor] vs` de ~$130+. Mata la segunda, quédate con la primera.
- Solo 15,000 impresiones → **este canal tiene techo de volumen**. Aunque le pongas $10,000, el mercado no existe. Nunca será tu motor principal.

### ❌ PAUSAR (casi todo): Campaña B
- Conversion rate de **0.50% = 6x peor que A y 8x peor que C**.
- Estás pagando $1,800 por 4,800 clicks de gente que busca **información, no software**. "Cómo gestionar inventario" = intención informacional. Ese tráfico se compra con SEO, no con CPC.
- CPA $75 con la intención más débil = el peor ROI real de las tres.

**Pero antes de matarla, dos verificaciones:**
1. **Modelo de atribución.** Si estás en last-click, B puede estar asistiendo conversiones de A y C (alguien lee el blog, después busca tu marca). Revisa el reporte de *Rutas de conversión* y las conversiones *view-through*. Si B asiste en >20% de las conversiones de A, no la mates: bájala a $300 y mídela.
2. **Búsquedas de marca.** Si tus impresiones de marca crecieron durante el mes de B, hay efecto halo.

---

## 3. Redistribución de los $5,000

### Escenario base (presupuesto duro de $5,000)

| Campaña | Actual | Propuesto | Δ | Signups esperados |
|---|---|---|---|---|
| A | $2,100 | **$3,200** | +52% | ~58 (CPA ~$55, asumiendo degradación) |
| C (reestructurada) | $3,200 | **$1,500** | −53% | ~21 (CPA ~$70 tras limpiar keywords) |
| B (solo remarketing + 1 keyword) | $1,800 | **$300** | −83% | ~4 |
| **Total** | **$7,100** | **$5,000** | **−30%** | **~83** |

**Resultado honesto:** ~83 signups vs 105 actuales (−21%), pero con **30% menos gasto**. Blended CPA baja de $67.62 → **~$60**. No te voy a vender que vas a conseguir más signups con menos plata: no es realista. Lo que ganas es eficiencia y espacio para reinvertir.

Asumí que el CPA de A se degrada de $46.67 → $55 (+18%) al subir el presupuesto. Es un supuesto conservador; si tu impression share es bajo, podría mantenerse cerca de $48 y darte ~66 signups.

### Escenario alternativo: ¿deberías pedir más presupuesto?

Esta es la pregunta que realmente importa y **no puedo responderla con los datos que me diste**. Necesito:
- **Signup → cliente pagado (%)** — en SaaS B2B con free trial suele ser 10-25%
- **ACV o LTV**

Ejemplo: si convierte 20% y tu ACV es $1,200/año:
- CAC real de A = $46.67 ÷ 0.20 = **$233** → LTV/CAC = 5.1x → **excelente, no recortes: pide más presupuesto**
- CAC real de C = $88.89 ÷ 0.20 = **$444** → LTV/CAC = 2.7x → aceptable pero ajustado

Si los números dan así, recortar A de $7,100 a $5,000 es destruir valor. La conversación correcta con finanzas sería: "cada $1,000 en Campaña A genera ~4 clientes a $233 de CAC con LTV de $1,200". **Optimizar dentro de un presupuesto equivocado es el error más caro aquí.**

### Prerrequisito de tracking

Antes de decisiones más finas, importa **conversiones offline** a Google Ads (signup → trial activado → pagado) y pásate a Target CPA o Maximize Conversion Value con valores diferenciados. Optimizar por "signup" te lleva a optimizar por el evento más barato, no por el más valioso. Es perfectamente posible que B genere signups basura y C genere signups que convierten al doble.

---

## 4. A/B tests para el próximo mes

### ⚠️ Primero, la mala noticia sobre el poder estadístico

Con 45 conversiones/mes en A, para detectar un lift de 3% → 4% en conversion rate (95% confianza, 80% poder) necesitas **~5,400 clicks por variante**. Campaña A genera ~1,500-2,300 clicks/mes en total.

**Implicación práctica:** olvídate de testear colores de botón o microcopy. Solo tienes budget estadístico para **2-3 tests grandes por trimestre**, con cambios lo suficientemente radicales para producir lifts de 30%+. Y mide también micro-conversiones (scroll depth, inicio de formulario) que tienen más volumen para leer señales tempranas.

### Test #1 — Fricción del formulario (Campaña A) · **prioridad máxima**
- **A:** formulario actual
- **B:** solo email + password (todo lo demás se pide dentro del producto)
- **Hipótesis:** cada campo eliminado sube conversión 5-10%; pasar de 5 a 2 campos puede dar +30-50%
- **Por qué primero:** cambio de una hora, afecta el 100% del tráfico pagado, y es el punto de fuga más común en SaaS

### Test #2 — Landing dedicada de comparación (Campaña C) · **prioridad alta**
- **A:** landing genérica actual
- **B:** página `/alternativa-a-[competidor]` con tabla comparativa, + oferta de migración: *"Importamos tus datos gratis en 48h"*
- **Hipótesis:** este tráfico tiene la intención más alta (4% CVR) pero llega a una página que no habla su idioma. Objetivo: 4% → 7-8%, lo que baja el CPA de $88.89 a ~$50 y convierte C en escalable
- Bonus: esa página posiciona en orgánico para el mismo término, y ahí el clic es gratis

### Test #3 — Rescate del contenido informacional (Campaña B) · presupuesto pequeño, upside alto
- **A:** CTA actual "Prueba gratis" (0.5% CVR)
- **B:** lead magnet alineado a la intención — *"Plantilla de control de inventario para restaurantes (Excel gratis)"* o una calculadora de merma
- **Hipótesis:** el problema es el mismatch de intención, no el tráfico. A $0.38 de CPC, si logras 1.5% de CVR el CPA cae a **$25 = mejor que A**. Esto justifica el test aunque sea con $300
- Mide el lead → signup, no solo el download

### Test #4 — Estrategia de puja (Campaña A)
- **A:** estrategia actual
- **B:** Target CPA a $45
- Corre 3-4 semanas mínimo (el algoritmo necesita ~30 conversiones para calibrar). Con 45 conv/mes estás justo en el límite, así que no interrumpas el test antes de tiempo

### Test #5 — Housekeeping (no es A/B, pero hazlo el día 1)
- **Negativas en B:** `gratis`, `excel`, `plantilla`, `qué es`, `curso`, `pdf`, `ejemplos`
- **Segmentación por keyword en C:** aísla `[competidor] vs` en su propio grupo para poder matarlo con datos
- **Revisa el término de búsqueda real** de las 3 campañas: en broad match típicamente 20-30% del gasto se va en queries que ni sabías que estabas comprando

---

## Resumen ejecutivo

1. **Estás 42% sobre presupuesto** ($7,100 vs $5,000). Arregla eso primero.
2. **A es tu mejor campaña** ($46.67 CPA): escala a $3,200 — pero revisa impression share para saber cuánto headroom real tienes.
3. **C no es mala, es cara**: el CVR de 4% es el mejor de las tres. El problema es el CPC de $3.56 y probablemente una sola keyword tóxica. Recorta a $1,500 y reestructura, no la mates.
4. **B a $300** (solo remarketing) — verifica atribución antes de apagarla del todo.
5. **El dato que falta y que cambia todo:** signup → cliente pagado y ACV. Si LTV/CAC > 3x en A, la recomendación correcta no es redistribuir $5,000 sino **pedir $8,000**.

¿Me pasas el % de conversión de signup a cliente pagado, tu ACV, y el Search Impression Share de A? Con eso puedo darte el número exacto de cuánto deberías estar gastando en lugar de asumir que $5,000 es el techo correcto.