# GPT-6.1 Terra — noticias_verificacion/mixto_instacart_debut

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 1.942s | tokens_per_second: 39.6
- input_tokens: 979 | output_tokens: 77

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el verificador de datos de una redacción. Recibes una FUENTE (en español o en inglés) y una lista numerada de AFIRMACIONES que alguien quiere publicar citándola. Decide, para CADA afirmación, si la fuente la respalda.

Responde SOLO con JSON válido, con un veredicto por cada afirmación y el mismo id:
{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}]}

RESPALDADO: la fuente afirma lo mismo, aunque con otras palabras, en otro idioma o con la cifra escrita en otro formato («US$1.500 millones» = «$1.5 billion»).
NO_RESPALDADO: la fuente no dice nada sobre eso, o lo que dice no alcanza para afirmarlo. La AUSENCIA nunca es contradicción.
CONTRADICE: la fuente afirma algo incompatible: otra cifra, otra fecha, otra entidad haciendo la acción (quién lideró, quién paga, quién confirma), o lo opuesto.

Reglas:
- Usa SOLO la fuente. No uses lo que sabes del mundo, aunque estés seguro.
- Si la fuente está truncada (muro de pago, «Suscríbete para seguir leyendo»), lo que no aparece en el fragmento es NO_RESPALDADO, nunca CONTRADICE.
- La atribución es parte del dato: «según Reuters» no es «la empresa confirmó».
- Lee la fuente completa, hasta el último párrafo, antes de decidir.
- Devuelve exactamente un veredicto por afirmación: ni menos, ni repetidos.

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

AFIRMACIONES A VERIFICAR (5):
1. Instacart recaudó US$660 millones con la venta de 22 millones de acciones.
2. Instacart comenzó a cotizar en Nasdaq el 19 de septiembre de 2023.
3. A inicios de 2021, Instacart fue valorada en US$39.000 millones.
4. Instacart destinará lo recaudado a expandirse en Europa.
5. En sus primeros minutos en bolsa, la acción de Instacart tocó US$42,95.


## Respuesta completa

{"veredictos":[{"id":1,"veredicto":"RESPALDADO"},{"id":2,"veredicto":"RESPALDADO"},{"id":3,"veredicto":"RESPALDADO"},{"id":4,"veredicto":"NO_RESPALDADO"},{"id":5,"veredicto":"RESPALDADO"}]}