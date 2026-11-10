# Tencent Hy4 — noticias_extraccion/extraccion_reddit

- model_id: `tencent/hy4`
- success: True  | final: 8.02 | quality: 9.59
- latency_total: 236.308s | tokens_per_second: 133.3
- input_tokens: 1022 | output_tokens: 31510

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
Reddit prices IPO at top of range, raising $748 million

San Francisco — Reddit priced its initial public offering at $34 per share in March 2024, the top of the $31 to $34 range it had marketed to investors, raising about $748 million. At that price, the social media company is valued at about $6.4 billion.

Not all of the money goes to the company. About $228 million corresponds to shares sold by existing shareholders who chose to cash out part of their holdings. Excluding those secondary sales, Reddit raised gross proceeds of $519.4 million.

The shares are set to begin trading on the New York Stock Exchange under the ticker RDDT. Morgan Stanley, Goldman Sachs, JPMorgan Chase and Bank of America are the lead underwriters.

Initial public offerings of consumer internet companies had been rare for more than two years. Rising interest rates pushed investors toward profitable companies and away from businesses that promised growth in the future, and many startups that had planned to list in 2022 postponed their plans. Bankers had been watching the Reddit listing as a test of whether that window was reopening.

Reddit's business depends on advertising, which makes it sensitive to the same swings that affect other social platforms. The company has also started to license its archive of public conversations to companies that train artificial intelligence models, a source of revenue that did not exist a few years ago and that investors are still trying to value.

The company took an unusual step for a listing of its size: it set aside part of the offering for some of its most active users and moderators, who could buy shares at the IPO price before trading began. The move reflects how much the platform depends on volunteers who run its communities without pay.

Founded in 2005 by Steve Huffman and Alexis Ohanian, Reddit was acquired by Condé Nast a year later and became independent again in 2011. Huffman is the company's chief executive.

Investors also weighed the company's governance. Like many technology companies that list their shares, Reddit set up a structure that gives some shareholders more voting power than others, which limits the influence of the investors who buy in the offering. Supporters say such structures let management plan for the long term; critics say they weaken accountability. The debate has accompanied almost every large technology listing of the past decade, and index providers have at times excluded companies with unequal voting rights from some benchmarks.

The IPO valuation is well below what private investors paid for the company before the market downturn. In a private fundraising round in 2021, Reddit was valued at $10 billion.



## Respuesta completa

{"claims": [{"texto": "Reddit fijó el precio de su oferta pública inicial en marzo de 2024.", "nucleo": true}, {"texto": "Reddit fijó el precio de su oferta pública inicial en 34 dólares por acción.", "nucleo": true}, {"texto": "Reddit había comercializado su oferta pública inicial a inversores en un rango de 31 a 34 dólares por acción.", "nucleo": true}, {"texto": "Reddit fijó el precio de su oferta pública inicial en el extremo superior del rango de 31 a 34 dólares por acción.", "nucleo": true}, {"texto": "Reddit recaudó aproximadamente 748 millones de dólares con su oferta pública inicial.", "nucleo": true}, {"texto": "Al precio de 34 dólares por acción, Reddit está valorada en aproximadamente 6.400 millones de dólares.", "nucleo": true}, {"texto": "No todo el dinero de la oferta pública inicial de Reddit va a Reddit.", "nucleo": true}, {"texto": "Aproximadamente 228 millones de dólares de la oferta pública inicial de Reddit corresponden a acciones vendidas por accionistas existentes de Reddit.", "nucleo": true}, {"texto": "Accionistas existentes de Reddit eligieron vender parte de sus participaciones en la oferta pública inicial.", "nucleo": true}, {"texto": "Excluyendo las ventas secundarias de acciones de accionistas existentes de Reddit, Reddit obtuvo ingresos brutos de 519,4 millones de dólares.", "nucleo": true}, {"texto": "Las acciones de Reddit están previstas para comenzar a cotizar en la New York Stock Exchange.", "nucleo": false}, {"texto": "Las acciones de Reddit están previstas para comenzar a cotizar bajo el símbolo bursátil RDDT.", "nucleo": false}, {"texto": "Morgan Stanley es uno de los suscriptores principales de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "Goldman Sachs es uno de los suscriptores principales de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "JPMorgan Chase es uno de los suscriptores principales de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "Bank of America es uno de los suscriptores principales de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "Las ofertas públicas iniciales de empresas de internet de consumo habían sido raras durante más de dos años.", "nucleo": false}, {"texto": "El aumento de las tasas de interés empujó a los inversores hacia empresas rentables.", "nucleo": false}, {"texto": "El aumento de las tasas de interés alejó a los inversores de negocios que prometían crecimiento futuro.", "nucleo": false}, {"texto": "Muchas startups que habían planeado salir a bolsa en 2022 postergaron sus planes.", "nucleo": false}, {"texto": "Los banqueros habían estado observando la salida a bolsa de Reddit como una prueba de si la ventana de ofertas públicas iniciales para empresas de internet de consumo se estaba reabriendo.", "nucleo": false}, {"texto": "El negocio de Reddit depende de la publicidad.", "nucleo": false}, {"texto": "La dependencia del negocio de Reddit de la publicidad hace que Reddit sea sensible a las mismas fluctuaciones que afectan a otras plataformas sociales.", "nucleo": false}, {"texto": "Reddit ha comenzado a licenciar su archivo de conversaciones públicas a empresas que entrenan modelos de inteligencia artificial.", "nucleo": false}, {"texto": "La licencia del archivo de conversaciones públicas de Reddit es una fuente de ingresos que no existía hace unos años.", "nucleo": false}, {"texto": "Los inversores todavía están intentando valorar la fuente de ingresos de Reddit por la licencia de su archivo de conversaciones públicas.", "nucleo": false}, {"texto": "Reddit reservó parte de su oferta pública inicial para algunos de sus usuarios y moderadores más activos.", "nucleo": true}, {"texto": "Algunos de los usuarios y moderadores más activos de Reddit pudieron comprar acciones de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "Algunos de los usuarios y moderadores más activos de Reddit pudieron comprar acciones al precio de 34 dólares por acción de la oferta pública inicial de Reddit.", "nucleo": true}, {"texto": "Algunos de los usuarios y moderadores más activos de Reddit pudieron comprar acciones de la oferta pública inicial de Reddit antes de que comenzara la cotización.", "nucleo": true}, {"texto": "Reddit depende de voluntarios que gestionan sus comunidades sin remuneración.", "nucleo": false}, {"texto": "Voluntarios gestionan las comunidades de Reddit sin remuneración.", "nucleo": false}, {"texto": "Reddit fue fundada en 2005.", "nucleo": false}, {"texto": "Steve Huffman fundó Reddit.", "nucleo": false}, {"texto": "Alexis Ohanian fundó Reddit.", "nucleo": false}, {"texto": "Condé Nast adquirió Reddit un año después de la fundación de Reddit.", "nucleo": false}, {"texto": "Reddit volvió a ser independiente en 2011.", "nucleo": false}, {"texto": "Steve Huffman es el director ejecutivo de Reddit.", "nucleo": false}, {"texto": "Los inversores también evaluaron el gobierno corporativo de Reddit.", "nucleo": false}, {"texto": "Al igual que muchas empresas tecnológicas que cotizan sus acciones, Reddit estableció una estructura que otorga a algunos accionistas más poder de voto que a otros.", "nucleo": false}, {"texto": "La estructura de voto desigual de Reddit limita la influencia de los inversores que compran acciones en la oferta pública inicial de Reddit.", "nucleo": false}, {"texto": "Según los defensores de las estructuras de voto desigual, dichas estructuras permiten a la dirección planificar a largo plazo.", "nucleo": false}, {"texto": "Según los críticos de las estructuras de voto desigual, dichas estructuras debilitan la rendición de cuentas.", "nucleo": false}, {"texto": "El debate sobre las estructuras de voto desigual ha acompañado a casi todas las grandes salidas a bolsa tecnológicas de la última década.", "nucleo": false}, {"texto": "Los proveedores de índices han excluido en ocasiones a empresas con derechos de voto desiguales de algunos índices de referencia.", "nucleo": false}, {"texto": "La valoración de la oferta pública inicial de Reddit está muy por debajo de lo que pagaron los inversores privados por Reddit antes de la caída del mercado.", "nucleo": false}, {"texto": "Reddit fue valorada en 10.000 millones de dólares en una ronda de financiación privada.", "nucleo": false}, {"texto": "La ronda de financiación privada en la que Reddit fue valorada en 10.000 millones de dólares fue en 2021.", "nucleo": false}]}