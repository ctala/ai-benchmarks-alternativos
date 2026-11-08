# Claude Opus 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.98 | quality: 10.0
- latency_total: 54.015s | tokens_per_second: 71.5
- input_tokens: 393 | output_tokens: 3861

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

## 1. Métricas calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) | **Total** |
|---|---|---|---|---|
| Impresiones | 50,000 | 120,000 | 15,000 | 185,000 |
| Clicks | 1,500 | 4,800 | 900 | 7,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** | 3.89% |
| Costo | $2,100 | $1,800 | $3,200 | $7,100 |
| **CPC** | **$1.40** | **$0.375** | **$3.56** | $0.99 |
| Signups | 45 | 24 | 36 | 105 |
| **Conv. Rate** | **3.00%** | **0.50%** | **4.00%** | 1.46% |
| **CPA** | **$46.67** | **$75.00** | **$88.89** | $67.62 |

**Métricas derivadas útiles:**

| Métrica | A | B | C |
|---|---|---|---|
| Signups por 1,000 impresiones | 0.90 | 0.20 | 2.40 |
| % del gasto total | 29.6% | 25.4% | 45.1% |
| % de signups totales | 42.9% | 22.9% | 34.3% |
| Eficiencia (share signups / share gasto) | **1.45x** | 0.90x | 0.76x |

---

## ⚠️ Problema crítico antes de seguir

**Estás gastando $7,100 con un presupuesto de $5,000.** Hay un sobregasto del 42%. Esto cambia todo el análisis: no se trata de "dónde pongo más plata", sino de **dónde recorto $2,100**.

También faltan datos clave que condicionan las recomendaciones (ver sección 5).

---

## 2. Qué escalar y qué pausar

### 🟢 ESCALAR: Campaña A
- **CPA más bajo**: $46.67 (33% mejor que B, 47% mejor que C)
- Genera el **43% de los signups con solo el 30% del gasto**
- CTR de 3% en keywords comerciales con intención de compra = relevancia sólida
- Volumen de impresiones intermedio → probablemente **hay headroom** para subir pujas sin degradar mucho el CPA

### 🟡 MANTENER con condiciones: Campaña C
- CPA de $88.89 es el peor, **pero**:
  - CTR de 6% (el doble que A) → intención altísima
  - Conv. rate de 4% (el mejor de las tres) → la gente que llega **convierte**
  - Solo 15,000 impresiones → mercado limitado, no es escalable infinitamente
- **El problema es el CPC de $3.56**, no la calidad del tráfico. Keywords de competidor son caras por subasta competitiva.
- **Acción**: reducir presupuesto ~40%, no pausar. Mantener solo las keywords de mejor desempeño.

### 🔴 REDUCIR DRÁSTICAMENTE: Campaña B
- **Conv. rate de 0.50%** = 6 a 8 veces peor que A y C
- CPA de $75 pese a tener el CPC más barato ($0.375)
- 4,800 clicks → solo 24 signups. **4,776 personas vinieron y se fueron.**
- El tráfico informacional ("cómo gestionar inventario") está en etapa de investigación, no de compra

**Pero no la pausaría al 100%, y esto es importante:**

Hay un argumento legítimo contra matarla: ese tráfico puede estar **asistiendo** conversiones que se atribuyen a A o C (alguien lee el blog hoy, busca tu marca en 3 semanas, convierte). Si tu modelo de atribución es *last-click*, B se ve artificialmente mal.

**Acción**: reducir a presupuesto mínimo de prueba ($400) mientras revisas atribución. **El contenido del blog en sí debería vivir en SEO orgánico, no en paid.** Pagar $0.375 por click para tráfico informacional raramente tiene sentido económico.

---

## 3. Redistribución de los $5,000

### Propuesta base (conservadora)

| Campaña | Actual | Propuesto | Δ | Justificación |
|---|---|---|---|---|
| A | $2,100 | **$2,900** | +38% | Mejor CPA, hay headroom |
| B | $1,800 | **$400** | -78% | Prueba de atribución únicamente |
| C | $3,200 | **$1,700** | -47% | Mantener top keywords, cortar cola |
| **Total** | $7,100 | **$5,000** | -30% | |

### Proyección esperada

| Escenario | Supuesto | Signups estimados | CPA blend |
|---|---|---|---|
| **Optimista** | CPA se mantiene igual | ~98 | $51 |
| **Realista** | A sube a $52 (+11%), C a $95 | ~81 | $62 |
| **Pesimista** | A sube a $58 (+25%), C a $105 | ~72 | $69 |

**Caso realista: ~81 signups vs 105 actuales, pero gastando $2,100 menos.** El CPA blended mejora de $67.62 a ~$62.

> **Nota honesta**: escalar la Campaña A un 38% **no** dará un 38% más de signups. Las pujas más altas compran clicks progresivamente más caros y menos relevantes. Espera retornos decrecientes. Mi estimación es +25-30% de signups, con CPA subiendo 10-15%.

### Alternativa más agresiva (si validas que A escala bien)

Después de 2 semanas de datos:

| Campaña | Presupuesto |
|---|---|
| A | $3,400 |
| B | $0 (pausada, mover a SEO) |
| C | $1,600 |

---

## 4. A/B tests sugeridos (priorizados)

### 🔥 Prioridad 1 — Lo que más mueve la aguja

**Test 1: Landing page de Campaña C**
- **Hipótesis**: una landing de comparación dedicada ("TuProducto vs [Competidor]") convertirá mejor que la landing genérica
- **Por qué**: C ya tiene el mejor conv. rate (4%) con tráfico de altísima intención. Si subes a 6%, el CPA baja de $88.89 a **$59** sin tocar pujas
- **Diseño**: tabla comparativa, migración asistida gratis, testimonios de ex-clientes del competidor
- **Métrica**: conv. rate. **Impacto estimado: -30% CPA**

**Test 2: Estructura de pujas en Campaña A**
- **Hipótesis**: separar keywords en campañas propias (SKAG-lite) con pujas individuales mejora eficiencia
- **Por qué**: "software gestión inventario" y "inventario pymes" probablemente tienen CPAs muy distintos, pero están promediados
- **Métrica**: CPA por keyword. Esto es *análisis* antes que test, pero es el paso previo necesario para escalar A sin quemar presupuesto

### 📊 Prioridad 2 — Aprendizaje estructural

**Test 3: Fricción del formulario de signup**
- **Hipótesis**: reducir campos (ej. de 6 a 3) sube conv. rate >20%
- Afecta las 3 campañas simultáneamente → mayor apalancamiento
- **Métrica**: conv. rate global

**Test 4: Oferta de conversión en Campaña B**
- **Hipótesis**: el tráfico informacional no está listo para signup, pero sí para un lead magnet
- **Variante A**: signup directo (actual, 0.50%)
- **Variante B**: "Descarga: Plantilla de control de inventario" → email → nurture
- **Por qué**: convierte una campaña con CPA de $75 en una máquina de leads baratos. Si captas 5% de emails a $0.375 CPC, el costo por email es ~$7.50
- Este test **decide si B vive o muere**

### 🧪 Prioridad 3 — Si queda bandwidth

**Test 5: Ad copy con precio vs sin precio en Campaña A**
- Mencionar precio filtra tráfico no cualificado → menos clicks, mejor conv. rate
- Mide CPA, no CTR

**Test 6: Expansión de keywords de competidor**
- C tiene solo 15,000 impresiones. Agregar variantes: "[competidor] precio", "[competidor] opiniones", "mejor que [competidor]", "cancelar [competidor]"
- Más que test, es expansión de inventario

### Nota sobre significancia estadística

Con 24-45 conversiones/mes por campaña, **cuidado con sacar conclusiones rápido**. Para detectar una mejora del 30% en conv. rate con confianza razonable necesitas ~150-200 conversiones por variante. En la práctica:

- Testea **cambios grandes**, no botones de colores
- Corre tests mínimo 3-4 semanas
- Prioriza tests que afecten las 3 campañas (como el Test 3) para acumular volumen más rápido
- Con este volumen, decisiones direccionales > certeza estadística

---

## 5. Datos que necesito para afinar esto

Mi recomendación cambiaría significativamente con:

1. **Valor de un signup** (LTV, conversión signup→pago, ticket promedio). Sin esto, no sé si un CPA de $88.89 es excelente o catastrófico. Si tu LTV es $2,000, deberías gastar **mucho más** en C. Si es $120, ninguna campaña es rentable.
2. **Calidad de signups por campaña**. Es plausible que los 36 signups de C valgan más que los 45 de A (vienen con problema claro y ya evaluaron alternativas). Si C convierte a pago al 40% y A al 15%, **C es tu mejor campaña** y el análisis se invierte.
3. **Impression share y lost IS (budget/rank)** — te dice cuánto headroom real hay en cada campaña. Esencial para saber si A puede absorber $800 extra.
4. **Modelo de atribución actual** — determina si B está siendo subvalorada.
5. **Quality Score por keyword** en C — un QS bajo explicaría el CPC de $3.56 y sería más barato arreglarlo que subir pujas.

---

## Resumen ejecutivo

| | |
|---|---|
| **Problema #1** | Sobregasto de $2,100 (42% sobre presupuesto) |
| **Escalar** | Campaña A → $2,900 (CPA $46.67, el mejor) |
| **Reducir** | Campaña C → $1,700 (buen tráfico, CPC caro) |
| **Casi pausar** | Campaña B → $400 (conv. rate 0.50% es insostenible) |
| **Test #1** | Landing comparativa dedicada para Campaña C |
| **Dato bloqueante** | LTV / tasa signup→pago por campaña |