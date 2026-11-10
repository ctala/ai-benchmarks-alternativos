# Tencent Hy4 — noticias_extraccion/extraccion_instacart

- model_id: `tencent/hy4`
- success: True  | final: 8.13 | quality: 9.7
- latency_total: 208.636s | tokens_per_second: 125.7
- input_tokens: 1009 | output_tokens: 26233

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

{"claims":[{"texto":"Instacart fijó el precio de su salida a bolsa en 30 dólares por acción.","nucleo":true},{"texto":"Instacart fijó el precio de su OPV en el extremo superior del rango de precios que había comercializado.","nucleo":true},{"texto":"Instacart recaudó 660 millones de dólares en su OPV.","nucleo":true},{"texto":"Instacart vendió 22 millones de acciones en su OPV.","nucleo":true},{"texto":"El precio de la OPV dio a Instacart una valoración de mercado de alrededor de 10.000 millones de dólares.","nucleo":true},{"texto":"Las acciones de Instacart comenzaron a cotizar en el Nasdaq el 19 de septiembre de 2023.","nucleo":true},{"texto":"Las acciones de Instacart cotizan bajo el ticker CART.","nucleo":true},{"texto":"En los primeros minutos de negociación del primer día, las acciones de Instacart alcanzaron un máximo de 42,95 dólares.","nucleo":true},{"texto":"Instacart trabaja con cadenas de supermercados en lugar de operar tiendas propias.","nucleo":false},{"texto":"Los shoppers de Instacart recogen artículos de los estantes de las tiendas y los entregan.","nucleo":false},{"texto":"Instacart vende software que permite a los minoristas gestionar sus propias tiendas en línea.","nucleo":false},{"texto":"Instacart vende tecnología para tiendas físicas, como carritos inteligentes.","nucleo":false},{"texto":"Instacart fue fundada en 2012.","nucleo":false},{"texto":"Apoorva Mehta fundó Instacart.","nucleo":false},{"texto":"Apoorva Mehta es un exingeniero de Amazon.","nucleo":false},{"texto":"Fidji Simo es la directora ejecutiva de Instacart desde 2021.","nucleo":false},{"texto":"Fidji Simo es una exejecutiva de Meta.","nucleo":false},{"texto":"La salida a bolsa de Instacart fue una de las primeras grandes OPV tecnológicas después de un largo parón.","nucleo":false},{"texto":"La salida a bolsa de Arm fue una de las primeras grandes OPV tecnológicas después de un largo parón.","nucleo":false},{"texto":"La salida a bolsa de Arm ocurrió antes en el mismo mes que la de Instacart.","nucleo":false},{"texto":"Arm es un diseñador de chips.","nucleo":false},{"texto":"Los banqueros esperaban que un debut sólido de Instacart animara a otras empresas a seguir su ejemplo.","nucleo":false},{"texto":"La valoración de Instacart en la OPV quedó muy por debajo de lo que los inversores privados habían pagado anteriormente por Instacart.","nucleo":false},{"texto":"A principios de 2021, Instacart anunció una ronda de financiación.","nucleo":false},{"texto":"La ronda de financiación anunciada por Instacart a principios de 2021 valoró a Instacart en 39.000 millones de dólares.","nucleo":false},{"texto":"Los analistas que cubrían la salida a bolsa de Instacart señalaron el negocio publicitario de Instacart como la clave de su valoración.","nucleo":false},{"texto":"Las empresas de bienes de consumo pagan para que sus productos aparezcan de forma destacada cuando los clientes buscan en la aplicación de Instacart.","nucleo":false},{"texto":"Los ingresos por publicidad de Instacart tienen márgenes mucho más altos que las tarifas de entrega.","nucleo":false},{"texto":"Varias de las mayores cadenas de supermercados han estado construyendo sus propias operaciones de entrega y publicidad.","nucleo":false},{"texto":"Por ahora, la mayoría de las mayores cadenas de supermercados depende de la plataforma de Instacart para llegar a clientes que esperan comparar tiendas y productos en una sola aplicación antes de decidir dónde comprar.","nucleo":false}]}