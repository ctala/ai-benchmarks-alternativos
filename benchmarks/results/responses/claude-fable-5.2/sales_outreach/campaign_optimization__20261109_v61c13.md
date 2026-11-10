# Claude Fable 5.2 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 54.745s | tokens_per_second: 89.7
- input_tokens: 395 | output_tokens: 4913

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

**Antes de empezar:** las tres campañas suman $7,100 de gasto, no $5,000. O te pasaste del presupuesto o alguna cifra está mal. Asumo que los datos son correctos y que hay que recortar a $5,000.

## 1. Métricas

| Campaña | CTR | CPC | Conversion rate | CPA |
|---|---|---|---|---|
| A (Landing) | 3.0% | $1.40 | 3.0% | **$46.67** |
| B (Blog) | 4.0% | $0.38 | 0.5% | $75.00 |
| C (Competidor) | 6.0% | $3.56 | 4.0% | **$88.89** |

En total son 105 signups a un CPA promedio de $67.62.

## 2. Qué escalar y qué pausar

**Escalar A.** Tiene el CPA más bajo: cada signup cuesta 38% menos que en B y 47% menos que en C.

**Recortar fuerte C, sin pausarla del todo.** Tiene el mejor CTR y la mejor conversión, pero el peor CPA: consume el 45% del gasto y genera el 34% de los signups. El problema es el precio del click ($3.56), no la audiencia. Para igualar el CPA de A, su CPC tendría que bajar a $1.87.

**Reducir B.** Convierte poco (0.5%), pero sus clicks son tan baratos que su CPA es mejor que el de C. Con subir la conversión a 0.8% igualaría a A.

**Matiz importante:** todo esto mide costo por signup, no por cliente. Quien busca "alternativa a [competidor]" suele estar más cerca de comprar que quien lee un blog. Si los signups de C se convierten en clientes de pago a una tasa al menos 1.2 veces la de B, C es más rentable que B y convendría recortar B en su lugar. Revisa ese dato antes de decidir.

## 3. Redistribución de $5,000

| Campaña | Actual | Propuesto | Signups esperados |
|---|---|---|---|
| A | $2,100 | **$3,000** (60%) | ~64 |
| B | $1,800 | **$1,000** (20%) | ~13 |
| C | $3,200 | **$1,000** (20%) | ~11 |
| **Total** | $7,100 | **$5,000** | **~89** (CPA ≈ $56) |

Si solo recortaras todo proporcionalmente a $5,000, obtendrías unos 74 signups. Esta distribución da alrededor de 20% más.

Dos advertencias:
- **El CPA de A puede subir al escalar.** La proyección asume que se mantiene constante, y eso rara vez pasa. Revisa la cuota de impresiones perdida por presupuesto: si es baja, A no podrá absorber los $900 extra de forma eficiente.
- **Sube el presupuesto de A gradualmente**, entre 20% y 30% por semana, para no desestabilizar el algoritmo de pujas.

## 4. A/B tests para el próximo mes

Con 25 a 65 conversiones por campaña al mes, solo podrás detectar diferencias grandes. Haz un test por campaña y prueba cambios radicales, no colores de botón.

1. **Campaña A: landing actual contra una variante con propuesta de valor distinta.** Por ejemplo, un titular enfocado en pymes o un formulario más corto. Es el test prioritario porque A llevará el 60% del presupuesto. Pasar de 3% a 3.5% de conversión bajaría el CPA a $40.
2. **Campaña B: blog contra un lead magnet.** Envía el tráfico a una plantilla de inventario descargable o a un artículo con CTA de prueba gratis integrado. La meta es una conversión de 0.8% o más.
3. **Campaña C: landing genérica contra una página comparativa.** Una página "Nosotros vs [competidor]" con tabla de diferencias y oferta de migración. Combínala con un tope de puja de $3.00 o menos por click, que es el punto donde C iguala el CPA de B.
4. **Campaña A, si queda margen: anuncios con precio o prueba gratis en el titular contra anuncios centrados en beneficios.** Sirve para filtrar clicks poco cualificados.

Si me pasas la tasa de signup a cliente de pago por campaña, puedo rehacer el análisis con costo por cliente, que es la métrica que debería guiar la decisión.