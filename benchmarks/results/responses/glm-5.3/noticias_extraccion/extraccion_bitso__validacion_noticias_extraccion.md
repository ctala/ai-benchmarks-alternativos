# GLM 5.3 — noticias_extraccion/extraccion_bitso

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.16 | quality: 9.86
- latency_total: 63.733s | tokens_per_second: 78.1
- input_tokens: 920 | output_tokens: 4979

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
Bitso becomes Latin America's first crypto unicorn with $250 million Series C

Mexico City — Bitso, the Mexican cryptocurrency exchange, has raised $250 million in a Series C round co-led by Tiger Global and Coatue that values the company at $2.2 billion. The round, announced in May 2021, makes Bitso the first cryptocurrency company in Latin America to be valued at more than $1 billion.

New investors Paradigm, BOND and Valor Capital Group joined the round. Existing backers QED Investors, Pantera Capital and Kaszek also participated.

Crypto exchanges in the region play a role that differs from their counterparts in the United States or Europe. Trading for speculation exists, but a large share of the activity comes from people who use digital assets to protect savings from inflation, to move money across borders or to receive payments from abroad. Stablecoins pegged to the dollar are especially popular because they offer the stability of the currency without the need for a bank account in the United States.

Remittances are a central part of the pitch. Mexico is one of the largest recipients of remittances in the world, and traditional transfer services charge fees that crypto rails can undercut. Bitso has partnered with companies that move money from the United States to Mexico and uses its exchange to settle those transfers.

Bitso was founded in 2014 by Pablo González, Ben Peters and Daniel Vogel. The company says it serves customers in Mexico, Argentina and Brazil and plans to keep expanding in Latin America.

Regulation remains the main uncertainty. Mexico's financial technology law, passed in 2018, set rules for virtual assets but left many questions open, and central banks across the region have been cautious about allowing traditional financial institutions to offer crypto to their customers.

For users, the main risks are well known. Prices of digital assets can swing sharply in a matter of hours, and an exchange that fails can leave customers unable to withdraw their funds. That is why regulators and investors pay close attention to how exchanges hold customer assets, whether they keep reserves that match their obligations and how they protect accounts from fraud. Exchanges that want to work with banks and payment companies usually have to submit to audits and compliance reviews that go well beyond what the law strictly requires, and those costs weigh on smaller competitors.

The new round comes only a few months after the company's previous raise. In December 2020, Bitso closed a $62 million Series B.



## Respuesta completa

{"claims": [{"texto": "Bitso recaudó 250 millones de dólares en una ronda Serie C.", "nucleo": true}, {"texto": "La Serie C de Bitso fue copliderada por Tiger Global y Coatue.", "nucleo": true}, {"texto": "La ronda Serie C valora a Bitso en 2.200 millones de dólares.", "nucleo": true}, {"texto": "La ronda Serie C de Bitso fue anunciada en mayo de 2021.", "nucleo": true}, {"texto": "Bitso es la primera empresa de criptomonedas de América Latina en alcanzar una valoración superior a 1.000 millones de dólares.", "nucleo": true}, {"texto": "Los nuevos inversores Paradigm, BOND y Valor Capital Group se sumaron a la ronda de Bitso.", "nucleo": true}, {"texto": "Los inversores previos QED Investors, Pantera Capital y Kaszek también participaron en la ronda de Bitso.", "nucleo": true}, {"texto": "Bitso es un exchange de criptomonedas mexicano.", "nucleo": false}, {"texto": "Bitso fue fundada en 2014 por Pablo González, Ben Peters y Daniel Vogel.", "nucleo": false}, {"texto": "Según la empresa, Bitso atiende a clientes en México, Argentina y Brasil.", "nucleo": false}, {"texto": "Según la empresa, Bitso planea seguir expandiéndose en América Latina.", "nucleo": false}, {"texto": "La ley de tecnología financiera de México, aprobada en 2018, estableció reglas para los activos virtuales.", "nucleo": false}, {"texto": "México es uno de los mayores receptores de remesas del mundo.", "nucleo": false}, {"texto": "Bitso se ha asociado con empresas que transfieren dinero de Estados Unidos a México y usa su exchange para liquidar esas transferencias.", "nucleo": false}, {"texto": "En diciembre de 2020, Bitso cerró una ronda Serie B de 62 millones de dólares.", "nucleo": false}]}