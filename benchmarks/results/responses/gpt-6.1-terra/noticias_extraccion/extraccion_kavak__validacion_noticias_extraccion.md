# GPT-6.1 Terra — noticias_extraccion/extraccion_kavak

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.89 | quality: 9.09
- latency_total: 12.237s | tokens_per_second: 81.4
- input_tokens: 1000 | output_tokens: 996

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

{"claims":[{"texto":"Kavak recaudó 700 millones de dólares en una ronda Serie E.","nucleo":true},{"texto":"La ronda Serie E valoró a Kavak en 8.700 millones de dólares.","nucleo":true},{"texto":"La valoración de Kavak en la Serie E fue aproximadamente el doble de la que había recibido a principios del mismo año.","nucleo":true},{"texto":"General Catalyst lideró la ronda Serie E de Kavak.","nucleo":true},{"texto":"Tiger Global participó en la ronda Serie E de Kavak.","nucleo":true},{"texto":"D1 Capital Partners participó en la ronda Serie E de Kavak.","nucleo":true},{"texto":"SoftBank participó en la ronda Serie E de Kavak.","nucleo":true},{"texto":"Founders Fund participó en la ronda Serie E de Kavak.","nucleo":true},{"texto":"Varios fondos que habían respaldado a Kavak en rondas anteriores también participaron en la Serie E.","nucleo":true},{"texto":"Kavak es un marketplace mexicano de compra y venta de automóviles usados.","nucleo":false},{"texto":"Kavak cerró una ronda Serie D cinco meses antes de la ronda Serie E.","nucleo":false},{"texto":"Kavak recaudó 485 millones de dólares en su ronda Serie D.","nucleo":false},{"texto":"La ronda Serie D valoró a Kavak en 4.000 millones de dólares.","nucleo":false},{"texto":"Tras la Serie E, Kavak se convirtió en la segunda empresa tecnológica privada más valiosa de América Latina, después de Nubank.","nucleo":true},{"texto":"Nubank es un banco digital brasileño.","nucleo":false},{"texto":"Kavak fue fundada en 2016.","nucleo":false},{"texto":"Kavak fue fundada en México.","nucleo":false},{"texto":"Carlos García Ottati fundó Kavak junto con un grupo de cofundadores.","nucleo":false},{"texto":"Kavak creció primero en Ciudad de México.","nucleo":false},{"texto":"Kavak se expandió a otras ciudades mexicanas antes de expandirse al extranjero.","nucleo":false},{"texto":"Kavak opera en México.","nucleo":false},{"texto":"Kavak opera en Brasil.","nucleo":false},{"texto":"Kavak opera en Argentina.","nucleo":false},{"texto":"Según Kavak, parte del nuevo capital se destinará a su expansión por América Latina.","nucleo":false},{"texto":"Según Kavak, la empresa planea comenzar a operar en varios mercados nuevos durante el año siguiente a la ronda.","nucleo":false},{"texto":"Kavak no nombró los países en los que planea comenzar a operar.","nucleo":false},{"texto":"Según directivos de Kavak, el dinero de la ronda financiará nuevos centros de reacondicionamiento.","nucleo":false},{"texto":"Según directivos de Kavak, el dinero de la ronda financiará tecnología para fijar automáticamente los precios de los vehículos.","nucleo":false},{"texto":"Kavak opera 40 centros de logística y reacondicionamiento en los tres países donde tiene presencia.","nucleo":false},{"texto":"Kavak contaba con alrededor de 300 trabajadores unos años antes de la ronda Serie E.","nucleo":false},{"texto":"Kavak cuenta con más de 5.000 empleados en América Latina.","nucleo":false}]}