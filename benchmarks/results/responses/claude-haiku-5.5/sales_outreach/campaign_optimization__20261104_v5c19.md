# Claude Haiku 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 8.925s | tokens_per_second: 191.4
- input_tokens: 393 | output_tokens: 1708

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
- CTR = 1,500 / 50,000 = **3.00%**
- CPC = $2,100 / 1,500 = **$1.40**
- CPA = $2,100 / 45 = **$46.67**
- Conversion rate = 45 / 1,500 = **3.00%**

**Campaña B (Blog content)**
- CTR = 4,800 / 120,000 = **4.00%**
- CPC = $1,800 / 4,800 = **$0.375 ≈ $0.38**
- CPA = $1,800 / 24 = **$75.00**
- Conversion rate = 24 / 4,800 = **0.50%**

**Campaña C (Competidor)**
- CTR = 900 / 15,000 = **6.00%**
- CPC = $3,200 / 900 = **$3.56**
- CPA = $3,200 / 36 = **$88.89**
- Conversion rate = 36 / 900 = **4.00%**

**Resumen total**
- Gasto: $7,100 | Signups: 105 | CPA promedio: **$67.62**
- Nota: el gasto total ($7,100) supera tu presupuesto de $5,000, así que conviene revisar si son datos de otro periodo o si hay sobregasto.

## 2. Escalar o pausar

**Escalar: Campaña A.** Es la más equilibrada: CPA de $46.67, el mejor de las tres, con un volumen de signups considerable (45, el mayor). Tiene intención comercial clara ("software gestión inventario") y una conversion rate de 3% que es sólida para B2B SaaS.

**Pausar o reducir fuertemente: Campaña B.** Aunque tiene el CTR más alto y el CPC más barato, su conversion rate de 0.5% es muy baja. Tiene el peor CPA ($75) de las tres en términos de costo por signup. El tráfico es de búsqueda informativa ("cómo gestionar inventario") y la gente no está lista para registrarse. Su valor probablemente esté en el posicionamiento de marca y el remarketing, no en adquisición directa.

**Campaña C: mantener y optimizar, no escalar a ciegas.** Su conversion rate (4%) es la más alta y muestra intención muy fuerte, pero el CPC de $3.56 eleva el CPA a $88.89. Es rentable solo si el valor de vida del cliente es alto. Antes de escalar, verifica el LTV: si un cliente vale más de ~$90, se justifica; si no, reducir.

## 3. Redistribución de los $5,000

Sugerencia (basada en el CPA y el LTV supuesto):

- **Campaña A: $2,800 (56%)**, aumento de ~$700 respecto al gasto actual, enfocada en keywords de alta intención.
- **Campaña C: $1,400 (28%)**, reducción de gasto, limitándola a los términos de mayor conversión ("alternativa a", "vs") y con pujas más ajustadas.
- **Campaña B: $800 (16%)**, reducción fuerte; mantenerla solo para captar audiencia y alimentar remarketing a visitantes del blog.

Si el LTV de tus clientes es alto (>$150), podrías subir C a ~$1,800 y bajar B a $500. Si es bajo, reduce C a ~$1,000.

Además, considera crear una audiencia de remarketing con quienes visitaron el blog (campaña B) y mostrarles anuncios de la landing de A. Eso puede mejorar la conversion rate de B de forma indirecta.

## 4. Propuestas de A/B tests para el próximo mes

1. **Landing page A:** variante con propuesta de valor específica para restaurantes vs. pymes en general (los keywords de B sugieren un nicho de restaurantes que podrías explorar).
2. **Copy de anuncios en C:** un anuncio que mencione directamente diferencias concretas contra el competidor (precio, funcionalidad) vs. uno más genérico de "alternativa".
3. **Oferta/CTA:** "Prueba gratis 14 días" vs. "Demo personalizada" vs. "Empieza gratis sin tarjeta", midiendo signup rate y calidad posterior.
4. **Campaña B con CTA de conversión:** agregar al blog un banner o CTA contextual de prueba gratuita para medir si sube la conversion rate de 0.5% sin afectar el engagement.
5. **Pujas:** comparar Maximize Conversions vs. Target CPA ($50) en la campaña A, una vez que tenga suficientes datos.
6. **Keywords negativas:** revisar términos de búsqueda en B para excluir consultas sin intención comercial y reducir el gasto desperdiciado.

Si me compartes el LTV aproximado de un cliente y el plan de precios, puedo afinar la redistribución y los umbrales de CPA objetivo.