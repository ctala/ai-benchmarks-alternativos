# Muse Ember — noticias_extraccion/extraccion_rappi

- model_id: `meta/muse-ember`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 12.044s | tokens_per_second: 588.4
- input_tokens: 918 | output_tokens: 7087

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
Rappi raises more than $500 million at a $5.25 billion valuation

Bogotá — Rappi, the Colombian on-demand delivery company, has raised more than $500 million in a Series F round that values it at $5.25 billion. The round, announced in July 2021, was led by T. Rowe Price.

Baillie Gifford, Third Point, Octahedron and GIC also invested, and SoftBank, an existing shareholder, participated as well.

Delivery apps grew into one of the most visible technology categories in Latin American cities. Their basic proposition is simple, but the economics are difficult: each order requires a courier, the average ticket is small and customers are quick to switch to whichever app offers the best promotion. Most companies in the segment try to improve the math by adding higher-margin services on top of delivery, such as advertising for restaurants and brands, subscriptions and financial products.

Rappi has followed that playbook. Besides restaurant and grocery delivery, it offers a payments service, a credit card in partnership with banks and a subscription that waives delivery fees.

The company was founded in Bogotá in 2015 by Simón Borrero, Sebastián Mejía and Felipe Villamarín. It operates in nine countries in Latin America.

The company's previous raise was a $300 million round in September 2020, which reportedly valued Rappi at $3.5 billion. Before that, SoftBank had made a large investment in 2019 through its first Latin America fund, which made the Japanese group the company's biggest backer.

Rappi said it would use the new capital to expand its financial services and its network of dark stores, small warehouses in dense neighborhoods that allow groceries to be delivered in minutes instead of hours.

Competition remains intense. Global platforms and local players in each country are fighting for the same couriers, restaurants and customers, and regulators in several countries are debating whether delivery workers should be treated as employees.

The quick-commerce model has drawn skepticism from some investors. Dark stores require rent, staff and inventory in expensive neighborhoods, and the promise of delivery in minutes only pays off if each store processes enough orders per hour. Several companies in the United States and Europe that expanded aggressively with this model later closed locations or merged with competitors when funding became harder to obtain, and the companies that survived usually concentrated on fewer, denser cities.

According to Crunchbase data, the new financing brings the total Rappi has raised since its founding to more than $2 billion.



## Respuesta completa

{"claims": [{"texto": "Rappi es una empresa colombiana de entrega bajo demanda.", "nucleo": false}, {"texto": "Rappi recaudó más de 500 millones de dólares en una ronda Serie F.", "nucleo": true}, {"texto": "La ronda Serie F de Rappi valoró a Rappi en 5.250 millones de dólares.", "nucleo": true}, {"texto": "La ronda Serie F de Rappi fue anunciada en julio de 2021.", "nucleo": true}, {"texto": "La ronda Serie F de Rappi fue liderada por T. Rowe Price.", "nucleo": true}, {"texto": "Baillie Gifford invirtió en la ronda Serie F de Rappi.", "nucleo": true}, {"texto": "Third Point invirtió en la ronda Serie F de Rappi.", "nucleo": true}, {"texto": "Octahedron invirtió en la ronda Serie F de Rappi.", "nucleo": true}, {"texto": "GIC invirtió en la ronda Serie F de Rappi.", "nucleo": true}, {"texto": "SoftBank participó en la ronda Serie F de Rappi.", "nucleo": true}, {"texto": "SoftBank ya era accionista de Rappi antes de la ronda Serie F.", "nucleo": false}, {"texto": "Rappi ofrece entrega de restaurantes.", "nucleo": false}, {"texto": "Rappi ofrece entrega de supermercados.", "nucleo": false}, {"texto": "Rappi ofrece un servicio de pagos.", "nucleo": false}, {"texto": "Rappi ofrece una tarjeta de crédito en alianza con bancos.", "nucleo": false}, {"texto": "Rappi ofrece una suscripción que exime del pago de cargos de entrega.", "nucleo": false}, {"texto": "Rappi fue fundada en Bogotá.", "nucleo": false}, {"texto": "Rappi fue fundada en 2015.", "nucleo": false}, {"texto": "Simón Borrero es uno de los fundadores de Rappi.", "nucleo": false}, {"texto": "Sebastián Mejía es uno de los fundadores de Rappi.", "nucleo": false}, {"texto": "Felipe Villamarín es uno de los fundadores de Rappi.", "nucleo": false}, {"texto": "Rappi opera en nueve países de América Latina.", "nucleo": false}, {"texto": "La ronda anterior de Rappi recaudó 300 millones de dólares.", "nucleo": false}, {"texto": "La ronda anterior de Rappi fue en septiembre de 2020.", "nucleo": false}, {"texto": "Según reportes, la ronda anterior de Rappi valoró a Rappi en 3.500 millones de dólares.", "nucleo": false}, {"texto": "SoftBank invirtió en Rappi en 2019.", "nucleo": false}, {"texto": "SoftBank invirtió en Rappi a través de su primer fondo para América Latina.", "nucleo": false}, {"texto": "SoftBank es un grupo japonés.", "nucleo": false}, {"texto": "La inversión de SoftBank en Rappi convirtió a SoftBank en el principal respaldo de Rappi.", "nucleo": false}, {"texto": "Rappi dijo que usaría el nuevo capital para expandir sus servicios financieros.", "nucleo": false}, {"texto": "Rappi dijo que usaría el nuevo capital para expandir su red de dark stores.", "nucleo": false}, {"texto": "Según datos de Crunchbase, la nueva financiación eleva el total recaudado por Rappi desde su fundación a más de 2.000 millones de dólares.", "nucleo": false}]}