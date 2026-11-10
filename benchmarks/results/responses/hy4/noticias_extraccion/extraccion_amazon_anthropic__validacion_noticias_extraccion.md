# Tencent Hy4 — noticias_extraccion/extraccion_amazon_anthropic

- model_id: `tencent/hy4`
- success: True  | final: 7.83 | quality: 9.09
- latency_total: 113.351s | tokens_per_second: 122.0
- input_tokens: 980 | output_tokens: 13829

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
Amazon to invest up to $4 billion in Anthropic

Seattle — Amazon will invest up to $4 billion in Anthropic, the artificial intelligence company behind the Claude family of models, in exchange for a minority stake, the two companies said in September 2023.

The deal is structured in stages. Amazon has committed an initial $1.25 billion and holds an option to invest a further $2.75 billion, which would bring the total to $4 billion. Neither company disclosed the size of the stake or its valuation.

As part of the agreement, Amazon Web Services becomes Anthropic's primary cloud provider for mission-critical workloads, including safety research and the development of future foundation models. Anthropic also committed to build, train and deploy its models on Trainium and Inferentia, the chips that AWS designs in-house, and to make them available to AWS customers through Amazon Bedrock.

Partnerships between cloud providers and model developers have become a defining feature of the AI industry. Model developers need enormous amounts of computing capacity, and cloud companies want the most popular models to run on their infrastructure, where every customer request turns into billable usage. The investments often flow back to the investor in the form of cloud spending, which is why analysts look closely at how such deals are accounted for.

Anthropic was founded in 2021 by Dario Amodei and Daniela Amodei together with other former employees of OpenAI. The company has emphasized research on how to make AI systems safer and more predictable.

The agreement also puts pressure on Amazon's rivals. Microsoft is the largest investor in OpenAI, and Google has its own models as well as investments in other developers. For Amazon, which was seen as slower to respond to the rise of chatbots, the deal secures access to a leading model maker.

For enterprise customers, the practical effect of such partnerships is choice. A company already running its systems on one cloud can use models from several developers through that provider's platform, with the same contracts, billing and security controls. That convenience has become a competitive weapon among cloud providers, which now race to offer the widest catalog of models alongside their own, and it has made distribution through the cloud marketplaces one of the main ways model developers reach large companies.

Anthropic said the investment will not change its corporate governance structure or its commitment to the responsible development of artificial intelligence. The company also said it will continue to make its models available through Google Cloud.



## Respuesta completa

{"claims":[{"texto":"Según Amazon y Anthropic, Amazon invertirá hasta 4.000 millones de dólares en Anthropic.","nucleo":true},{"texto":"Anthropic es la empresa de inteligencia artificial detrás de la familia de modelos Claude.","nucleo":false},{"texto":"Según Amazon y Anthropic, la inversión de Amazon en Anthropic se realizará a cambio de una participación minoritaria.","nucleo":true},{"texto":"Amazon y Anthropic informaron en septiembre de 2023 sobre su acuerdo de inversión.","nucleo":true},{"texto":"El acuerdo entre Amazon y Anthropic está estructurado por etapas.","nucleo":true},{"texto":"Amazon se ha comprometido a invertir inicialmente 1.250 millones de dólares en Anthropic.","nucleo":true},{"texto":"Amazon tiene la opción de invertir 2.750 millones de dólares más en Anthropic.","nucleo":true},{"texto":"La opción de Amazon de invertir 2.750 millones de dólares más en Anthropic elevaría el total de la inversión de Amazon en Anthropic a 4.000 millones de dólares.","nucleo":true},{"texto":"Ni Amazon ni Anthropic revelaron el tamaño de la participación minoritaria que Amazon recibiría en Anthropic.","nucleo":true},{"texto":"Ni Amazon ni Anthropic revelaron la valoración de la participación minoritaria que Amazon recibiría en Anthropic.","nucleo":true},{"texto":"Como parte del acuerdo entre Amazon y Anthropic, Amazon Web Services se convierte en el proveedor principal de nube de Anthropic para cargas de trabajo críticas.","nucleo":true},{"texto":"Entre las cargas de trabajo críticas de Anthropic para las que Amazon Web Services se convierte en proveedor principal está la investigación en seguridad.","nucleo":true},{"texto":"Entre las cargas de trabajo críticas de Anthropic para las que Amazon Web Services se convierte en proveedor principal está el desarrollo de futuros modelos fundacionales.","nucleo":true},{"texto":"Anthropic se comprometió a construir sus modelos en los chips Trainium e Inferentia de Amazon Web Services.","nucleo":true},{"texto":"Anthropic se comprometió a entrenar sus modelos en los chips Trainium e Inferentia de Amazon Web Services.","nucleo":true},{"texto":"Anthropic se comprometió a desplegar sus modelos en los chips Trainium e Inferentia de Amazon Web Services.","nucleo":true},{"texto":"Amazon Web Services diseña internamente los chips Trainium e Inferentia.","nucleo":false},{"texto":"Anthropic se comprometió a poner sus modelos a disposición de los clientes de Amazon Web Services a través de Amazon Bedrock.","nucleo":true},{"texto":"Anthropic fue fundada en 2021.","nucleo":false},{"texto":"Dario Amodei fue uno de los fundadores de Anthropic.","nucleo":false},{"texto":"Daniela Amodei fue una de las fundadoras de Anthropic.","nucleo":false},{"texto":"Otros ex empleados de OpenAI participaron en la fundación de Anthropic junto con Dario Amodei y Daniela Amodei.","nucleo":false},{"texto":"Anthropic ha puesto énfasis en la investigación sobre cómo hacer que los sistemas de inteligencia artificial sean más seguros y predecibles.","nucleo":false},{"texto":"Microsoft es el mayor inversor en OpenAI.","nucleo":false},{"texto":"Google tiene modelos propios.","nucleo":false},{"texto":"Google tiene inversiones en otros desarrolladores.","nucleo":false},{"texto":"Según Anthropic, la inversión de Amazon no cambiará la estructura de gobierno corporativo de Anthropic.","nucleo":false},{"texto":"Según Anthropic, la inversión de Amazon no cambiará el compromiso de Anthropic con el desarrollo responsable de la inteligencia artificial.","nucleo":false},{"texto":"Según Anthropic, los modelos de Anthropic seguirán disponibles a través de Google Cloud.","nucleo":false}]}