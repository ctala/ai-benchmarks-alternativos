# Muse Spark 1.3 — sales_outreach/campaign_optimization

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 26.224s | tokens_per_second: 144.1
- input_tokens: 260 | output_tokens: 3778

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

Aquí tienes el análisis completo. Estás gastando **$7,100 con un presupuesto de $5,000**, o sea un 42% por encima. Hay que recortar y reasignar.

### 1. Cálculo de métricas

Fórmulas:
**CTR = Clicks / Impresiones | CPC = Costo / Clicks | CPA = Costo / Signups | CVR = Signups / Clicks**

| Campaña | CTR | CPC | CPA | CVR Click->Signup |
| :--- | :--- | :--- | :--- | :--- |
| **A - Landing Principal** | 1,500 / 50,000 = **3.0%** | 2,100 / 1,500 = **$1.40** | 2,100 / 45 = **$46.67** | 45 / 1,500 = **3.0%** |
| **B - Blog Content** | 4,800 / 120,000 = **4.0%** | 1,800 / 4,800 = **$0.38** | 1,800 / 24 = **$75.00** | 24 / 4,800 = **0.5%** |
| **C - Competidor** | 900 / 15,000 = **6.0%** | 3,200 / 900 = **$3.56** | 3,200 / 36 = **$88.89** | 36 / 900 = **4.0%** |
| **TOTAL Actual** | 7,200 / 185,000 = **3.89%** | 7,100 / 7,200 = **$0.99** | 7,100 / 105 = **$67.62** | 105 / 7,200 = **1.46%** |

### 2. ¿Cuál escalar y cuál pausar?

**ESCALAR: Campaña A. Es tu ganadora en eficiencia.**
Tiene el **CPA más bajo por lejos: $46.67**. Es un 38% más barata que B ($75) y un 47% más barata que C ($88.89).
Con solo el 29.6% del gasto actual ($2,100 de $7,100) te trae el 42.9% de los signups (45 de 105). Su CVR de 3.0% demuestra intención transaccional real: keywords "software gestion inventario" = gente buscando comprar.

**PAUSAR (como captación pagada): Campaña B. Es una trampa de vanity metrics.**
Parece buena: CTR alto (4.0%) y CPC regalado ($0.38). Pero su CVR es desastroso: **0.5%**. Es **6x peor que A y 8x peor que C**.
¿Por qué? Intención informacional. "como gestionar inventario" quiere aprender, no contratar software. Gastas $1,800 para solo 24 signups. No la escales en Search pagado. Muévela a SEO / orgánico.

**MANTENER CON LÍMITE: Campaña C. Alta intención, costo insostenible.**
Tiene los mejores indicadores de intención: CTR más alto (6.0%) y CVR más alto (4.0%). Quien busca "alternativa a [competidor]" está listo para cambiarse.
El problema: CPC de **$3.56 (9.5x más caro que B y 2.5x que A)** por la guerra de pujas. Consume el 45% de tu presupuesto para solo el 34% de los signups. Su CPA de $88.89 es inviable para escalar sin control. No la pauses, pero ponle cap y optimízala.

> Sin tu LTV no puedo decir si $46.67 es rentable, pero la regla es clara: escala lo que tenga el CPA más bajo.

### 3. Redistribución del presupuesto de $5,000/mes

Te propongo modelo 70 / 20 / 10:

**A: $3,500 (70%) | C: $1,000 (20%) | Experimentos: $500 (10%) | B: $0 Pausada en Paid**

¿Por qué pausar B totalmente? Ya estás sobre-presupuesto. Cada dólar en B rinde menos.

Proyección manteniendo CPC y CVR actuales:
* **A ($3,500):** 2,500 clicks / $1.40 = ~75 signups
* **C ($1,000):** 281 clicks / $3.56 = ~11 signups
* **Total:** ~86 signups por $4,500 + $500 de test = **$5,000 para ~86-90 signups**

Blended CPA nuevo: **~$56-58 vs. $67.62 actual**. Bajas tu CPA ~17% y cumples presupuesto, con 19 signups menos pero ahorrando $2,100.

Acciones inmediatas:
1.  Pausa B en Google Ads. Déjala solo en SEO.
2.  Pon a C una estrategia `tCPA a $60` con presupuesto diario capado para forzar a Google a no pagar clicks de $5+.
3.  Agrega a B como negativas exactas en A: "como", "gratis", "excel", "restaurante", "problemas" si tu ICP son pymes que pagan.

### 4. A/B Tests para el próximo mes

No testees tráfico, testea intención y fricción.

**Test 1 - Campaña A (Prioridad #1): Fricción del formulario**
Hipótesis: El CVR de 3% puede subir a 4.5% si reduces campos.
A: Control (Nombre + Email + Empresa + Tamaño)
B: Solo Email + Botón "Probar Gratis"
KPI: CVR. Necesitas ~1,000 clicks por variante para significancia.

**Test 2 - Campaña A: Headline**
A: "Software de Gestión de Inventario para Pymes" (funcional)
B: "Reduce quiebres de stock 30% en 14 días. Sin Excel." + logos de clientes (beneficio + prueba social)
KPI: CVR y CTR del anuncio.

**Test 3 - Campaña C: Landing comparativa**
A: Enviar a tu landing principal genérica
B: Enviar a página `/vs-competidor` con tabla comparativa Precio / Funciones / Migración en 1-click
Hipótesis: Si pagas $3.56 por click, necesitas un CVR >6% para bajar el CPA a ~$59. La página comparativa es clave.

**Test 4 - Rescatar Campaña B: Cambiar el objetivo**
No pidas Signup directo a alguien que quiere aprender. Testea:
A: Blog -> CTA "Crear cuenta"
B: Blog -> Lead Magnet "Checklist Inventario Restaurante PDF" -> secuencia email 5 días -> Signup
KPI: Ya no es CPA de signup directo, sino Costo por Lead de email + tasa de activación a 14 días. Usa los $500 de experimentación para esto.

**Test 5 - Estructura y puja**
A: Keywords de A en concordancia amplia + Smart Bidding tCPA $47
B: Solo Exacta + Negativas agresivas
KPI: % de búsquedas irrelevantes y CPA real.

Empieza semana 1 con Test 1 y 3, son los que más impacto tendrán en tu CPA.