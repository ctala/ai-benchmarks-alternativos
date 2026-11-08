# Claude Haiku 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.71 | quality: 8.0
- latency_total: 9.096s | tokens_per_second: 202.3
- input_tokens: 393 | output_tokens: 1840

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

## 1. Métricas por campaña

**Campaña A (Landing principal)**
- CTR = 1,500 / 50,000 = **3.0%**
- CPC = $2,100 / 1,500 = **$1.40**
- Conversion rate (signups/clicks) = 45 / 1,500 = **3.0%**
- CPA = $2,100 / 45 = **$46.67**

**Campaña B (Blog content)**
- CTR = 4,800 / 120,000 = **4.0%**
- CPC = $1,800 / 4,800 = **$0.375 (≈ $0.38)**
- Conversion rate = 24 / 4,800 = **0.5%**
- CPA = $1,800 / 24 = **$75.00**

**Campaña C (Competidor)**
- CTR = 900 / 15,000 = **6.0%**
- CPC = $3,200 / 900 = **$3.56**
- Conversion rate = 36 / 900 = **4.0%**
- CPA = $3,200 / 36 = **$88.89**

**Resumen comparativo**

| Campaña | CTR | CPC | Conv. Rate | CPA |
|---|---|---|---|---|
| A | 3.0% | $1.40 | 3.0% | $46.67 |
| B | 4.0% | $0.38 | 0.5% | $75.00 |
| C | 6.0% | $3.56 | 4.0% | $88.89 |

Gasto total: $7,100 (sobre el presupuesto de $5,000, conviene revisarlo). Signups totales: 105, CPA promedio: $67.62.

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.** Tiene el mejor CPA ($46.67), un volumen de signups sólido (45) y una conversión saludable (3%). Es la campaña más eficiente en el embudo completo, con intención de compra clara en las keywords ("software gestión inventario").

**Revisar o reducir: Campaña B.** Su CTR es excelente y su CPC muy bajo, pero la conversión (0.5%) es muy baja. El tráfico atrae curiosos del blog, no compradores. Puede tener valor como generador de awareness o para remarketing, pero no como captación directa. Antes de pausarla, verifica si el blog tiene un CTA claro hacia el signup y si la página de destino es la adecuada.

**Pausar o reducir fuertemente: Campaña C.** Tiene la mejor conversión (4%) pero el CPC más alto ($3.56) y el CPA más caro ($88.89). Además, las búsquedas de competidores suelen implicar riesgos: alto costo por clic y, en algunos casos, problemas de política de Google Ads con el uso de marcas de terceros en anuncios. Si la mantienes, limítala a keywords exactas y revisa el texto del anuncio.

Nota: la Campaña C tiene una conversión muy alta, así que podría valer la pena optimizarla (landing específica de comparación, precio o features) antes de descartarla.

## 3. Redistribución del presupuesto de $5,000

Considerando que tu gasto actual fue de $7,100, la reducción es necesaria. Propuesta:

- **Campaña A: $3,000 (60%)**: principal motor de signups. Puedes incluso intentar subirla si el CPA se mantiene.
- **Campaña B: $800 (16%)**: reducida, enfocada en awareness y como puente hacia remarketing.
- **Campaña C: $600 (12%)**: prueba controlada, solo keywords exactas, con landing optimizada.
- **Reserva de testing: $600 (12%)**: para los experimentos del próximo mes.

Si tu prioridad es volumen de signups a costo fijo, el criterio es simple: pon el dinero donde el CPA es más bajo. Si tu prioridad es lead quality o valor de cliente, deberías cruzar estos datos con el LTV o la tasa de activación por campaña, que no incluiste y podría cambiar la conclusión.

## 4. A/B tests sugeridos para el próximo mes

1. **Campaña A - Landing:** probar un titular orientado a resultado ("Controla tu inventario en 10 minutos") vs. uno orientado a funcionalidad. Métrica: conversion rate.
2. **Campaña A - Formulario:** reducir campos del signup (por ejemplo, quitar teléfono) vs. versión actual. Métrica: conversion rate y calidad del lead.
3. **Campaña B - CTA del blog:** CTA intermedio ("Descarga la plantilla gratis") vs. CTA directo a signup. Métrica: conversion rate hacia signup.
4. **Campaña C - Landing de comparación:** tabla comparativa vs. página genérica. Métrica: conversion rate y CPA.
5. **Anuncios de Google (todas):** RSA con distintos enfoques de copy (precio, prueba gratis, beneficio). Métrica: CTR.

**Recomendación metodológica:** cambia una sola variable por test, define el criterio de éxito antes de empezar, y deja correr al menos 2 semanas o hasta tener ~100 conversiones por variante para tener significancia razonable.

¿Quieres que te ayude a estimar cuántas conversiones necesitas por variante según tu tasa base actual?