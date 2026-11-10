# GLM 5.3 — noticias_verificacion/bloquea_rappi_magnitud

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 6.257s | tokens_per_second: 98.6
- input_tokens: 1014 | output_tokens: 617

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

AFIRMACIONES A VERIFICAR (6):
1. Rappi levantó más de US$500 millones.
2. La valoración de Rappi es de US$5,25 millones.
3. T. Rowe Price lideró la Serie F de Rappi.
4. SoftBank lideró la Serie F de Rappi.
5. Rappi planea salir a bolsa en 2022.
6. Según Crunchbase, Rappi ha levantado más de US$2.000 millones desde su fundación.


## Respuesta completa

{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "CONTRADICE"}, {"id": 3, "veredicto": "RESPALDADO"}, {"id": 4, "veredicto": "CONTRADICE"}, {"id": 5, "veredicto": "NO_RESPALDADO"}, {"id": 6, "veredicto": "RESPALDADO"}]}