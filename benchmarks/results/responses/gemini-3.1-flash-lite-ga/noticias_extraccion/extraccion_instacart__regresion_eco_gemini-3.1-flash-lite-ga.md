# Gemini 3.1 Flash Lite (GA) — noticias_extraccion/extraccion_instacart

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.24 | quality: 9.7
- latency_total: 1.759s | tokens_per_second: 204.1
- input_tokens: 931 | output_tokens: 359

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
Instacart prices IPO at $30 a share

San Francisco — Instacart priced its initial public offering at $30 per share, the top of its marketed range, raising $660 million from the sale of 22 million shares. The price gives the grocery delivery company a market value of around $10 billion.

The company's shares began trading on the Nasdaq on September 19, 2023, under the ticker CART.

Grocery delivery was one of the clearest winners of the pandemic. Households that had never ordered food online started doing so almost overnight, and retailers that had resisted working with third-party platforms signed on to keep up. As stores reopened, growth slowed, and companies in the sector shifted their focus from adding customers to making each order profitable, mostly by selling advertising to the consumer brands whose products appear in the app.

Instacart works with grocery chains rather than running its own stores. Shoppers pick items from store shelves and deliver them, and the company also sells software that lets retailers run their own online stores and in-store technology such as smart carts.

The company was founded in 2012 by Apoorva Mehta, a former Amazon engineer. Fidji Simo, a former Meta executive, has been its chief executive since 2021.

The listing was closely watched as one of the first large technology IPOs after a long drought, along with that of the chip designer Arm earlier in the same month. Bankers hoped that a strong debut would encourage other companies to follow.

The valuation is far below what private investors once paid. In early 2021, at the height of the delivery boom, Instacart announced a funding round that valued it at $39 billion.

Analysts covering the listing pointed to the company's advertising business as the key to its valuation. Consumer goods companies pay to have their products appear prominently when shoppers search the app, and that revenue carries much higher margins than delivery fees. The question for investors is how much of that advertising can grow without annoying shoppers, and whether grocery chains will keep sharing their customers with a platform that also competes for their attention. Several of the largest chains have been building their own delivery and advertising operations, which could reduce how much they depend on a third-party marketplace over time. For now, most of them still rely on the platform to reach customers who expect to compare stores and products in a single app before deciding where to buy.

Demand on the first day was strong. In the first minutes of trading, the shares reached a peak of $42.95.



## Respuesta completa

{
  "claims": [
    {
      "texto": "Instacart fijó el precio de su oferta pública inicial en 30 dólares por acción.",
      "nucleo": true
    },
    {
      "texto": "Instacart recaudó 660 millones de dólares mediante la venta de 22 millones de acciones en su salida a bolsa.",
      "nucleo": true
    },
    {
      "texto": "Instacart alcanzó una valoración de mercado de aproximadamente 10.000 millones de dólares tras su salida a bolsa.",
      "nucleo": true
    },
    {
      "texto": "Las acciones de Instacart comenzaron a cotizar en el Nasdaq el 19 de septiembre de 2023 bajo el ticker CART.",
      "nucleo": true
    },
    {
      "texto": "Instacart fue fundada en 2012 por Apoorva Mehta.",
      "nucleo": false
    },
    {
      "texto": "Fidji Simo es la directora ejecutiva de Instacart desde 2021.",
      "nucleo": false
    },
    {
      "texto": "A principios de 2021, Instacart anunció una ronda de financiación que la valoró en 39.000 millones de dólares.",
      "nucleo": false
    },
    {
      "texto": "En los primeros minutos de cotización, las acciones de Instacart alcanzaron un precio máximo de 42,95 dólares.",
      "nucleo": true
    }
  ]
}