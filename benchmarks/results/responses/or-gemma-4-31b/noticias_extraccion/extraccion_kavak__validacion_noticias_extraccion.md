# Gemma 4 31B — noticias_extraccion/extraccion_kavak

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.46 | quality: 10.0
- latency_total: 3.752s | tokens_per_second: 180.7
- input_tokens: 1036 | output_tokens: 678

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el extractor de afirmaciones de una redacción que publica noticias de startups, inversión y tecnología en español. Recibes una FUENTE (en español o en inglés). Tu trabajo es sacar TODAS las afirmaciones verificables que la fuente hace sobre la noticia, para que un verificador las contraste una por una antes de publicar.

Responde SOLO con JSON válido:
{"claims": [{"texto": "<una afirmación, en español, autocontenida>", "nucleo": true}]}

QUÉ ES UNA AFIRMACIÓN VERIFICABLE (sí se extrae):
- cifras, montos, porcentajes, valoraciones, cantidades;
- fechas de HECHOS relatados (cuándo se cerró, cotizó o aprobó algo);
- entidades y quién hizo qué: quién lideró, quién participó, quién compró, quién aprobó;
- atribuciones: si la fuente dice «según la empresa» o «según Reuters», la afirmación conserva la atribución («Según la empresa, …»).

QUÉ NO SE EXTRAE:
- conocimiento de dominio (cómo funciona una Serie B, qué es un marketplace), opiniones y adjetivos sin dato;
- la fecha de publicación de la propia nota;
- nada que la fuente no diga: no conviertas monedas, no sumes, no restes, no calcules.

nucleo=true → el hecho de la noticia misma: qué pasó, quién, cuánto, cuándo, con quién.
nucleo=false → contexto: rondas anteriores, historia de la empresa, tamaño de mercado, comparaciones, planes y declaraciones accesorias.

Cada afirmación debe nombrar a la entidad de la que habla (nada de «la empresa» sin nombre). Una afirmación por dato. Lee la fuente COMPLETA, hasta el último párrafo: los datos del final cuentan igual que los del principio.

**user:**

FUENTE:
Kavak doubles its valuation with a $700 million Series E

Mexico City — Kavak, the Mexican marketplace for buying and selling pre-owned cars, has raised $700 million in a Series E round that values the company at $8.7 billion, roughly twice what investors were willing to pay for it earlier in the year.

The round was led by General Catalyst. Tiger Global, D1 Capital Partners, SoftBank and Founders Fund also took part, along with several funds that had backed the company in earlier rounds.

Used cars are one of the largest consumer categories in Latin America and also one of the least trusted. Buyers worry about hidden mechanical problems, sellers worry about being paid late or not at all, and financing is expensive or simply unavailable for a large part of the population. Companies in the segment try to remove that friction by inspecting each vehicle, reconditioning it in their own facilities and offering a warranty and a return window. The model is capital intensive: the marketplace usually owns the inventory for weeks, which ties up working capital and makes every additional market an expensive bet.

The new money arrives only five months after Kavak closed a $485 million Series D at a $4 billion valuation. With this round, Kavak became the most valuable private technology company in Latin America after Nubank, the Brazilian digital bank.

Kavak was founded in 2016 in Mexico by Carlos García Ottati together with a group of co-founders. The company grew first in Mexico City and later added other Mexican cities before expanding abroad. Today it operates in Mexico, Brazil and Argentina.

Investors in the sector say the attraction is less the margin on each car and more the financial products that can be attached to it: credit, insurance and maintenance plans. A buyer who finances a car through the platform stays connected to it for years, which turns a one-off transaction into a recurring relationship. That is also where the risks are, because consumer credit in the region is sensitive to interest rates and to the economic cycle.

According to the company, part of the new capital will go to expanding across Latin America, and Kavak plans to begin operating in several new markets over the next year. The company did not name the countries.

Executives also said the money would fund new reconditioning centers and technology to price vehicles automatically, a capability that becomes more valuable as the inventory grows and pricing mistakes multiply.

For buyers, the practical difference shows up after the sale. A car bought from a private seller rarely comes with any guarantee, and disputes usually end with the buyer absorbing the cost of repairs. Platforms that offer inspections, warranties and a return window are betting that customers will pay a premium for that certainty, and that the premium will cover the cost of reconditioning and holding inventory.

The company runs 40 logistics and reconditioning hubs across the three countries where it operates. Its workforce, which numbered around 300 people a few years ago, has grown to more than 5,000 employees in Latin America.



## Respuesta completa

```json
{
  "claims": [
    {
      "texto": "Kavak ha recaudado 700 millones de dólares en una ronda de Serie E.",
      "nucleo": true
    },
    {
      "texto": "La ronda de Serie E valora a Kavak en 8.700 millones de dólares.",
      "nucleo": true
    },
    {
      "texto": "General Catalyst lideró la ronda de Serie E de Kavak.",
      "nucleo": true
    },
    {
      "texto": "Tiger Global participó en la ronda de Serie E de Kavak.",
      "nucleo": true
    },
    {
      "texto": "D1 Capital Partners participó en la ronda de Serie E de Kavak.",
      "nucleo": true
    },
    {
      "texto": "SoftBank participó en la ronda de Serie E de Kavak.",
      "nucleo": true
    },
    {
      "texto": "Founders Fund participó en la ronda de Serie E de Kavak.",
      "nucleo": true
    },
    {
      "texto": "Varios fondos que habían respaldado a Kavak en rondas anteriores participaron en la Serie E.",
      "nucleo": true
    },
    {
      "texto": "Kavak cerró una Serie D de 485 millones de dólares con una valoración de 4.000 millones de dólares cinco meses antes de la Serie E.",
      "nucleo": false
    },
    {
      "texto": "Kavak se convirtió en la empresa tecnológica privada más valiosa de América Latina después de Nubank.",
      "nucleo": false
    },
    {
      "texto": "Kavak fue fundada en 2016 en México por Carlos García Ottati y un grupo de cofundadores.",
      "nucleo": false
    },
    {
      "texto": "Kavak opera actualmente en México, Brasil y Argentina.",
      "nucleo": false
    },
    {
      "texto": "Según Kavak, parte del nuevo capital se destinará a la expansión por América Latina.",
      "nucleo": true
    },
    {
      "texto": "Kavak planea comenzar a operar en varios mercados nuevos durante el próximo año.",
      "nucleo": true
    },
    {
      "texto": "Ejecutivos de Kavak afirmaron que el dinero financiará nuevos centros de reacondicionamiento y tecnología para valorar vehículos automáticamente.",
      "nucleo": true
    },
    {
      "texto": "Kavak opera 40 centros de logística y reacondicionamiento en los tres países donde tiene presencia.",
      "nucleo": false
    },
    {
      "texto": "La plantilla de Kavak ha crecido de unas 300 personas hace unos años a más de 5.000 empleados en América Latina.",
      "nucleo": false
    }
  ]
}
```