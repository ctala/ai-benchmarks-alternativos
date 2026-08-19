# Sakana Namazu — sales_outreach/campaign_optimization

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 8.431s | tokens_per_second: 242.9
- input_tokens: 359 | output_tokens: 2048

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

El usuario está preguntando en español sobre resultados de campañas de Google Ads. Necesito responder en español según las instrucciones (respond in the same language as the user).

Primero, debo calcular las métricas solicitadas:
- CTR = Clicks / Impresiones
- CPC = Costo / Clicks
- CPA = Costo / Signups (conversiones)
- Conversion Rate = Signups / Clicks

Campaña A:
- CTR: 1,500 / 50,000 = 0.03 = 3%
- CPC: $2,100 / 1,500 = $1.40
- CPA: $2,100 / 45 = $46.67
- Conv. Rate: 45 / 1,500 = 0.03 = 3%

Campaña B:
- CTR: 4,800 / 120,000 = 0.04 = 4%
- CPC: $1,800 / 4,800 = $0.375
- CPA: $1,800 / 24 = $75.00
- Conv. Rate: 24 / 4,800 = 0.005 = 0.5%

Campaña C:
- CTR: 900 / 15,000 = 0.06 = 6%
- CPC: $3,200 / 900 = $3.556 (redondeado a $3.56)
- CPA: $3,200 / 36 = $88.89
- Conv. Rate: 36 / 900 = 0.04 = 4%

Ahora, análisis:
- Campaña A: CPA más bajo ($46.67), buen conversion rate (3%), CPC medio ($1.40). Es la más eficiente en términos de costo por adquisición. Intención de búsqueda alta (transaccional).
- Campaña B: CTR decente (4%), CPC muy bajo ($0.375), pero conversion rate muy bajo (0.5%) y CPA alto ($75). Esto es típico de contenido/blog (intención informativa). Genera volumen pero no calidad.
- Campaña C: CTR más alto (6%), CPC muy alto ($3.56), CPA más alto ($88.89), pero buen conversion rate (4%). Intención comparativa/competidor. Es cara pero califica bien.

Recomendación:
- Escalar: Campaña A (mejor CPA, eficiente, intención clara de compra). Quizás también C si el LTV de esos usuarios es alto (usuarios de competidor pueden ser más calificados), pero con optimización.
- Pausar/reducir: Campaña B. Aunque trae tráfico barato, el CPA es 60% más caro que A y el conversion rate es terrible. Con el presupuesto limitado, no es eficiente.
- Nota: Si el LTV de Campaña C es significativamente mayor (usuarios cambiando de competidor suelen quedarse más tiempo), podría justificarse el CPA más alto. Pero con datos actuales, A es la reina.

Redistribución de presupuesto $5,000:
Actual gasto: $2,100 + $1,800 + $3,200 = $7,100. El usuario está gastando $7,100 pero dice presupuesto es $5,000/mes. Está sobrepresupuesto.

Si necesita bajar a $5,000:
Opción 1: Priorizar A y C con ajustes
- Campaña A: $2,500 (escalar lo que funciona)
- Campaña C: $1,800 (mantener, optimizar, buscar reducir CPC)
- Campaña B: $700 (reducir drásticamente, solo para remarketing o pruebas)

O mejor aún:
- Campaña A: $3,000 (escalar 43%)
- Campaña C: $1,500 (optimizar, reducir puja para bajar CPC, pausar keywords caras)
- Campaña B: $500 (test/blog, o pausar y usar para remarketing)

Espera, el usuario está gastando $7,100 actualmente pero presupuesto es $5,000. Entonces DEFINITIVamente necesita cortar algo.

Estrategia más agresiva:
- Campaña A: $3,500 (máxima eficiencia, sacar más volumen)
- Campaña C: $1,500 (mantener, buscar reducir CPA pausando keywords con CPA alto o ajustando puja)
- Campaña B: $0 (pausar o reducir a mínimo para test sólo si hay capacidad, pero con $5,000 y viendo los números, mejor pausar y redistribuir)

O si quiere mantener diversidad:
- A: 60% = $3,000
- C: 30% = $1,500  
- B: 10% = $500 (remarketing al blog)

Espera, necesito revisar si escalar A mantiene el CPA. Normalmente al escalar CPA sube, pero es el mejor candidato.

A/B Tests para próximo mes:
1. Campaña A:
   - Test de landing page: Actual vs. versión con testimonios/pricing más visible/demo video (la intención es alta, mejorar CVR puede bajar más el CPA)
   - Test de keywords: Ampliar a términos más específicos como "software inventario pymes mexico/argentina/etc" o agregar BMM/phrase de intención alta. También test de match types.
   - Anuncios: Test con extensiones de precio, sitelinks a funciones específicas vs. la landing general.

2. Campaña B:
   - Test de oferta/lead magnet: En vez de pedir signup directo en blog, ofrecer ebook "Guía de inventario para restaurantes" o herramienta gratuita (calculadora) para capturar email y luego nutrir. El signup directo no funciona en contenido informativo.
   - Test de audience: Excluir audiencias de remarketing ya convertidas, enfocar en usuarios que visitaron paginas de precios.
   - Redireccionar tráfico a una landing de "demo gratuita" específica para restaurantes vs. blog.

3. Campaña C:
   - Test de anuncios comparativos: "vs [competidor]" vs. "alternativa moderna a [competidor]" o "más barato que X"
   - Test de landing: Página de comparación lado a lado (competidor vs nosotros) vs. landing principal. Esto puede mejorar CVR mucho.
   - Optimización de puja/costo: Reducir puja máxima o usar estrategia ROAS/CPA target para no pagar tanto por clic.

4. General/Cross-campaign:
   - Remarketing: Crear campañas de remarketing separadas para visitantes de A y C (alta intención) con presupuesto separado.
   - Exclusiones: Negative keywords para B (agregar "gratis", "plantilla", "excel" si es software pago).
   - Test de horarios/días: Verificar qué días/horarios dan mejor CPA y aplicar ad schedule bid adjustments.

Debo estructurar esto bien con tablas claras y recomendaciones accionables. Usaré markdown para que sea legible. Mantendré un tono profesional pero directo.

Verificación números:
A: 1500/50000 = 0.03 exacto. 2100/1500 = 1.4 exacto. 2100/45 = 46.666... 45/1500 = 0.03 exacto.
B: 4800/120000 = 0.04 exacto. 1800/4800 = 0.375 exacto. 1800/24 = 75 exacto. 24/4800 = 0.005 exacto.
C: 900/15000 = 0.06 exacto. 3200/900 = 3.555... redondeo a $3.56. 3200/36 = 88.888... redondeo a $88.89. 36/900 = 0.04 exacto.

Gasto total actual: 2100+1800+3200 = 7100. Sí, está $2,100 sobre presupuesto.

Para la redistribución:
Voy a proponer:
- A: $2,750 (55%) - Escalar la más eficiente
- C: $1,500 (30%) - Mantener pero optimizar/negociar (realmente no se negocia en Google Ads pero sí reducir puja)
- B: $750 (15%) - Reducir a test, solo como fuente de remarketing/audience

Otra opción más drástica:
Pausar B completamente ($0), poner A