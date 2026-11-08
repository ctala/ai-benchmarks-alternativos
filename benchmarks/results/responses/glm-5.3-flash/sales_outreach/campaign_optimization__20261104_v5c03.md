# GLM 5.3 Flash — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 66.555s | tokens_per_second: 78.5
- input_tokens: 278 | output_tokens: 5224

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

# Análisis de campañas

## 1. Métricas calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| CTR | 3.0% | 4.0% | 6.0% |
| CPC | $1.40 | $0.38 | $3.56 |
| Tasa de conversión (click→signup) | 3.0% | 0.5% | 4.0% |
| CPA | **$46.67** | $75.00 | $88.89 |
| Signups por cada $1,000 | **21.4** | 13.3 | 11.25 |

**Totales:** 185,000 impresiones | 7,200 clicks | 105 signups | $7,100 gastados → CPA blended de **$67.62**

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.** Es la más eficiente en todas las métricas que importan: CPA de $46.67 (casi la mitad de C), tasa de conversión sólida de 3%, y genera el 43% de tus signups con solo el 30% del gasto. Tiene margen para crecer (50K impresiones es volumen moderado; puedes expandir keywords y ubicaciones antes de saturar).

**Pausar (como campaña de conversión directa): Campaña B.** Los números son claros: 4,800 clicks para solo 24 signups es una tasa de conversión de 0.5%, 6x peor que A. El problema es de intención: alguien buscando "como gestionar inventario" está investigando, no comprando. Pedirle un signup directo a ese tráfico es un mismatch de funnel. **Ojo:** no tires ese tráfico a la basura — 4,800 clicks a $0.38 son una audiencia de retargeting excelente (más en la sección 4).

**No pausar, sino optimizar: Campaña C.** Aunque tiene el CPA más alto ($88.89), tiene la mejor tasa de conversión (4%) y el CTR más alto (6%) — señales de máxima intención de compra. Pausar tu tráfico de mayor intención suele ser un error. Además, hay un matiz importante: **los signups de keywords de competidor suelen tener el mejor LTV** — son personas activamente evaluando cambiar de proveedor. Si aún no mides signup→cliente pagando por campaña, hazlo antes de matar a C.

## 3. Redistribución del presupuesto

⚠️ **Antes, una alerta:** gastaste **$7,100** el mes pasado contra un presupuesto declarado de $5,000. Verifica si fue overspend de presupuestos diarios o si el $5,000 es tu meta real hacia adelante. Esto es un 42% por encima del presupuesto.

Propuesta para $5,000/mes:

| Campaña | Presupuesto | % | Rol |
|---|---|---|---|
| A | $2,600 | 52% | Motor principal de signups |
| C | $1,700 | 34% | Captura de alta intención, optimizada |
| B | $700 | 14% | Retargeting + contenido con CTAs mejorados |

**Proyección conservadora:**
- A a $2,600: aunque el CPA suba a ~$55 por escala → ~47 signups
- C a $1,700: CPA ~$85 → ~20 signups (baja a ~$75 si mejoras la landing, sección 4)
- B a $700: si subes la conversión de 0.5% a 1–1.5% con retargeting y CTAs → CPA baja de $75 a ~$40–50

Resultado estimado: ~85–90 signups con CPA blended de ~$55–60, vs. $67.62 actual. Mejor eficiencia por dólar, con 30% menos gasto.

## 4. A/B tests para el próximo mes

**Campaña A (prioridad máxima — es donde va tu presupuesto):**
1. **Landing page:** versión actual vs. una con precios visibles + prueba social arriba del fold. Métrica: tasa de conversión. Hipótesis: reducir fricción informativa sube la conversión de 3% a 3.5–4%.
2. **Ángulo del copy:** dolor ("¿Pierdes ventas por stock faltante?") vs. funcionalidad ("Controla tu inventario en tiempo real"). Métrica: CTR y conversión por variante.
3. **Matching keyword-landing:** página específica para pymes vs. landing genérica para la keyword "inventario pymes". Métrica: conversion rate y Quality Score.

**Campaña B:**
4. **El test más importante del mes:** signup directo vs. lead magnet (ej. "Checklist de inventario para restaurantes") que alimente secuencia de email. Hipótesis: el tráfico de blog no convierte a signup pero sí a una oferta de menor compromiso, y de ahí bajas costos de adquisición downstream.
5. **Formato del CTA en el blog:** banner lateral vs. CTA inline dentro del texto vs. exit-intent. Métrica: clicks hacia la captura.

**Campaña C:**
6. **Landing de comparación dedicada:** tabla "Nosotros vs. [Competidor]" con precios, migración de datos incluida, vs. tu landing actual. Hipótesis: al matching de intención de comparación, la conversión sube y el CPA baja de $89 a ~$70.
7. **Oferta:** trial gratis vs. "importamos tus datos gratis en 48h". Métrica: signups y, sobre todo, signup→cliente pagado.

**Recomendación final:** no lances los 7 a la vez. Prioriza el #6 (mayor impacto potencial en CPA), el #4 (reescribe el modelo de B) y el #1 (protege tu campaña principal). Y antes de todo: **configura el tracking de signup→venta por campaña**. Sin ese dato, estás optimizando a ciegas — especialmente para decidir el futuro de C, que puede valer más de lo que su CPA sugiere.