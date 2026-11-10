# Ling 3.0 Flash — noticias_extraccion/extraccion_microsoft_openai

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.8 | quality: 9.25
- latency_total: 16.059s | tokens_per_second: 118.6
- input_tokens: 1017 | output_tokens: 1905

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
Microsoft extends OpenAI partnership with multibillion-dollar investment

Redmond — Microsoft announced in January 2023 a new multiyear, multibillion-dollar investment in OpenAI, the research company behind ChatGPT, extending a partnership that began four years earlier. Microsoft did not disclose the amount. Media reports, citing people familiar with the matter, put it at $10 billion.

Under the agreement, Microsoft Azure will remain OpenAI's exclusive cloud provider, powering all of OpenAI's workloads across research, products and API services. Microsoft also said it will deploy OpenAI's models across its consumer and enterprise products and build new categories of digital experiences on top of them.

The partnership is a bet on a particular division of labor. Training and serving large models requires data centers with specialized chips, networking and power on a scale that only a handful of companies can build. Model developers bring the research; cloud providers bring the infrastructure and the sales channels to large companies. Each side needs the other, but each also worries about depending too much on a single partner.

Microsoft first invested in OpenAI in 2019, with $1 billion, and invested again in 2021. The relationship gave Microsoft early access to the technology that it later integrated into its search engine, its office software and its developer tools.

The announcement came only weeks after the public launch of ChatGPT, in November 2022, which drew millions of users in a matter of days and set off a race among large technology companies to bring generative AI to their products. Google and Amazon, Microsoft's main rivals in cloud computing, accelerated their own work in response.

OpenAI was founded in 2015 as a nonprofit research laboratory. In 2019 it created a for-profit arm with a cap on the returns that investors can receive, a structure designed to raise the large amounts of capital its research requires.

The arrangement also raised questions that regulators would later examine. Competition authorities in the United States, the United Kingdom and the European Union looked at whether large technology companies were using investments in AI developers to gain influence over them without the scrutiny that a formal acquisition would bring. Both companies have said that OpenAI remains independent and that the partnership does not give Microsoft control over its decisions, and similar questions have since been raised about other investments by large cloud providers in model developers.

Microsoft also said that, as part of the agreement, it will build specialized supercomputing systems to support OpenAI's research.



## Respuesta completa

{"claims": [{"texto": "Microsoft anunció en enero de 2023 una nueva inversión multianual de miles de millones de dólares en OpenAI, extendiendo una asociación que comenzó cuatro años antes.", "nucleo": true}, {"texto": "Microsoft no reveló el monto de la inversión.", "nucleo": true}, {"texto": "Según informes de medios citando personas familiarizadas con el asunto, la inversión ascendería a 10.000 millones de dólares.", "nucleo": true}, {"texto": "Según el acuerdo, Microsoft Azure seguirá siendo el proveedor exclusivo de nube de OpenAI, impulsando todas las cargas de trabajo de OpenAI en investigación, productos y servicios API.", "nucleo": true}, {"texto": "Microsoft dijo que desplegará los modelos de OpenAI en sus productos de consumo y empresariales y construirá nuevas categorías de experiencias digitales sobre ellos.", "nucleo": true}, {"texto": "Microsoft invirtió por primera vez en OpenAI en 2019 con 1.000 millones de dólares e invirtió de nuevo en 2021.", "nucleo": true}, {"texto": "Esa relación dio a Microsoft acceso anticipado a la tecnología que luego integró en su motor de búsqueda, su software de oficina y sus herramientas para desarrolladores.", "nucleo": true}, {"texto": "El anuncio tuvo lugar solo semanas después del lanzamiento público de ChatGPT en noviembre de 2022, que atrajo a millones de usuarios en cuestión de días.", "nucleo": true}, {"texto": "El lanzamiento de ChatGPT desató una carrera entre las grandes empresas tecnológicas por incorporar la IA generativa a sus productos.", "nucleo": true}, {"texto": "Google y Amazon, los principales rivales de Microsoft en computación en la nube, aceleraron sus propios trabajos en respuesta.", "nucleo": true}, {"texto": "OpenAI fue fundada en 2015 como un laboratorio de investigación sin ánimo de lucro.", "nucleo": true}, {"texto": "En 2019, OpenAI creó una rama con fines de lucro con un límite en los rendimientos que los inversores pueden recibir, una estructura diseñada para recaudar las grandes cantidades de capital que su investigación requiere.", "nucleo": true}, {"texto": "Las autoridades de competencia de Estados Unidos, el Reino Unido y la Unión Europea examinaron si las grandes empresas tecnológicas estaban utilizando inversiones en desarrolladores de IA para ganar influencia sobre ellos sin la supervisión que una adquisición formal traería.", "nucleo": true}, {"texto": "Ambas empresas han declarado que OpenAI sigue siendo independiente y que la asociación no les da a Microsoft control sobre sus decisiones.", "nucleo": true}, {"texto": "Se han planteado preguntas similares sobre otras inversiones de grandes proveedores de nube en desarrolladores de modelos.", "nucleo": true}, {"texto": "Microsoft dijo que, como parte del acuerdo, construirá sistemas de supercomputación especializados para apoyar la investigación de OpenAI.", "nucleo": true}]}