# Claude Opus 5 Fast — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.91 | quality: 10.0
- latency_total: 28.298s | tokens_per_second: 205.9
- input_tokens: 393 | output_tokens: 5827

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

# Análisis de Campañas Google Ads

## ⚠️ Primero, un problema de aritmética

Tu gasto total fue **$7,100**, no $5,000. Estás **42% por encima del presupuesto**. Todas las recomendaciones abajo asumen que hay que recortar ~$2,100 reales, no solo "redistribuir".

---

## 1. Métricas calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) | **Blended** |
|---|---|---|---|---|
| Impresiones | 50,000 | 120,000 | 15,000 | 185,000 |
| Clicks | 1,500 | 4,800 | 900 | 7,200 |
| **CTR** | 3.00% | **4.00%** | **6.00%** | 3.89% |
| Costo | $2,100 | $1,800 | $3,200 | $7,100 |
| **CPC** | $1.40 | **$0.38** | $3.56 | $0.99 |
| Signups | 45 | 24 | 36 | 105 |
| **CVR (click→signup)** | 3.00% | **0.50%** | **4.00%** | 1.46% |
| **CPA** | **$46.67** | $75.00 | $88.89 | $67.62 |
| Signups / $1,000 | **21.4** | 13.3 | 11.3 | 14.8 |

**Lectura rápida:**
- **A** es tu campaña más eficiente en costo por resultado.
- **B** tiene el tráfico más barato pero la peor intención de compra (0.5% CVR = 1 de cada 200 visitantes).
- **C** tiene la mejor intención (4% CVR, 6% CTR) pero el click más caro del mundo ($3.56).

---

## 2. Qué escalar y qué pausar

### 🟢 ESCALAR: Campaña A
Es la única con CPA por debajo del blended ($46.67 vs $67.62) y produce **21.4 signups por cada $1,000** vs 11-13 de las otras. Si le quitas $1,000 a C y se los das a A, en teoría ganas ~10 signups netos con el mismo dinero.

**Advertencia:** el CPA marginal siempre sube al escalar. Un +50% de presupuesto rara vez da +50% de signups; espera CPA de $55-60 en el tramo nuevo. **Antes de escalar, revisa "Search Impression Share Lost (budget)"** en A. Si es <10%, no hay volumen que capturar y el dinero extra solo va a inflar tus CPCs.

### 🟡 ARREGLAR, NO ESCALAR: Campaña C
Este es tu problema más interesante. C convierte **33% mejor que A** (4% vs 3%) pero su CPA es **90% más alto**. El problema no es la audiencia, **es el CPC de $3.56**.

Causa típica: keywords de marca ajena tienen **Quality Score bajo** (2-4/10) porque tu landing no menciona al competidor → Google te cobra una prima brutal. Además solo hay 15,000 impresiones/mes: es un mercado con techo, no escalable por volumen.

**Matemática del arreglo:** si bajas el CPC de $3.56 a $2.20 (realista con landings de comparación dedicadas), con el mismo $3,200 obtienes 1,450 clicks → 58 signups → **CPA de $55**. Pasa de ser tu peor campaña a tu segunda mejor sin gastar un dólar más.

### 🔴 PAUSAR / REESTRUCTURAR: Campaña B
0.5% de CVR significa que 4,776 de 4,800 visitantes se fueron sin hacer nada. Estás pagando búsquedas informativas ("cómo gestionar inventario") con dinero de performance. **Ese es territorio de SEO/contenido orgánico, no de search pagado.**

**Pero antes de matarla, dos verificaciones obligatorias:**

1. **Conversiones asistidas.** Revisa el reporte de rutas de conversión. Si B es el primer toque de conversiones que el last-click atribuye a A o C, no es una campaña mala, es una campaña mal medida. Con modelo data-driven en vez de last-click el panorama puede cambiar.
2. **Segmenta por keyword.** "problemas inventario restaurante" es intención de dolor con vertical específica — probablemente convierte 5-10x mejor que "cómo gestionar inventario", que es tarea escolar. Es muy posible que 20 de los 24 signups vengan de un puñado de keywords y el resto sea puro desperdicio.

---

## 3. Redistribución de los $5,000

### Fase 1 — Mes 1 (movimiento gradual)

| Campaña | Antes | Después | Cambio | Acción |
|---|---|---|---|---|
| A | $2,100 | **$2,500** | +19% | Escalar con cuidado, vigilar CPA marginal |
| B | $1,800 | **$400** | -78% | Solo keywords de "dolor" + retargeting |
| C | $3,200 | **$2,100** | -34% | Bajar pujas, mejorar QS, no volumen |
| **Total** | $7,100 | **$5,000** | -30% | |

**Proyección conservadora:** ~85-92 signups a un CPA blended de **$55-59** (vs. $67.62 actual). Si mantuvieras la mezcla actual recortada a prorrata a $5,000, obtendrías solo ~74 signups. **La reasignación te da ~15-20% más signups con el mismo dinero.**

### Por qué dejar $400 en B en lugar de $0
Esos 4,800 clicks a $0.38 son la audiencia de retargeting más barata que tienes. Cambia el objetivo: en vez de empujar signup a tráfico frío informativo, ofrece un **lead magnet** (plantilla de control de inventario, calculadora de merma) y remercadea después. Mide B por costo-por-lead, no por signup directo.

### No muevas todo de golpe
Cambios >30% en el presupuesto de una campaña reactivan la fase de aprendizaje de Google y desestabilizan el rendimiento 1-2 semanas. Mueve en dos pasos quincenales y ancla las decisiones en 7 días de datos post-cambio, no en 2.

---

## 4. A/B tests sugeridos

### ⚠️ Realidad estadística primero
Con 45 conversiones/mes en A, detectar una mejora de 3.0% → 3.5% de CVR con significancia requiere **~10,000 clicks por variante** (≈6 meses). **No tienes volumen para tests de matices.** Solo prueba cambios grandes (MDE de +40-50% relativo, ~1,700 clicks/variante ≈ 2 meses) y **un test a la vez**.

### Prioridad 1 — Landings de comparación para C *(mayor ROI, no es A/B)*
Crea una página por competidor: `/vs/[competidor]`, con tabla comparativa, precio y el nombre del competidor en H1 y title. **Objetivo: subir Quality Score de ~3 a ~6.** Impacto esperado: CPC de $3.56 → $2.00-2.40. Esto no es un test, es una corrección — el upside es 2-3x mayor que cualquier test de copy.

### Prioridad 2 — Test de fricción en el formulario de A
- **Control:** formulario actual
- **Variante:** solo email + password (mueve empresa/teléfono/tamaño a onboarding)
- **Hipótesis:** +40-60% en CVR de signup
- **Riesgo a medir:** peor calidad de lead. Trackea signup→activación, no solo signup.

### Prioridad 3 — Test de oferta en el anuncio
- **Control:** "Prueba gratis 14 días"
- **Variante:** "Diagnóstico gratuito de tu inventario en 15 min"
- Para SaaS B2B de pymes, la oferta consultiva suele bajar volumen pero subir calidad. Mide CPA de *cliente pagado*, no de signup.

### Prioridad 4 — Precio en el copy del anuncio
Poner "Desde $XX/mes" reduce CTR (~-20%) pero sube CVR al pre-calificar. Con CPC de $1.40 en A, filtrar curiosos tiene valor directo. Mide CPA, ignora el CTR.

### Prioridad 5 — Landing por vertical
"problemas inventario restaurante" apunta a una landing genérica. Crea `/restaurantes` con lenguaje del sector (merma, food cost, recetas). Es la única parte de B que probablemente merezca vivir.

---

## Lo que te falta medir para decidir bien

Tus métricas se detienen en el signup, que es una **métrica proxy**. Las decisiones de presupuesto reales necesitan:

1. **Tasa signup → cliente pagado, por campaña.** Casi con seguridad C convierte a pago mucho mejor que B (alguien buscando "alternativa a [competidor]" ya tiene presupuesto y dolor). Si C convierte a pago al 30% y B al 5%, el CAC real es $296 vs $1,500 — y tu ranking de campañas se invierte completamente.
2. **LTV / ACV.** Sin esto no puedes saber si $47 de CPA es excelente o desastroso.
3. **Impression Share y IS perdido por presupuesto vs. por ranking** en cada campaña. Determina si A es escalable o ya está saturada.
4. **Lag de conversión.** Si tu ciclo de venta es de 20-30 días, los signups de las últimas 2 semanas aún no aparecieron. Los números de C pueden estar subestimados.

**Regla de decisión:** hasta tener el dato #1, trata este análisis como una hipótesis fuerte, no como una conclusión. La reasignación propuesta es defendible con lo que tienes, pero la magnitud del recorte a C podría ser un error si sus signups valen 3x los de A.