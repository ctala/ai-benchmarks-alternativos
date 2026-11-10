# Ling 3.0 Flash — noticias_extraccion/extraccion_reddit

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.94 | quality: 9.45
- latency_total: 11.98s | tokens_per_second: 159.6
- input_tokens: 1060 | output_tokens: 1912

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

```json
{"claims": [{"texto": "Reddit fijó el precio de su oferta pública inicial en 34 dólares por acción en marzo de 2024, en el extremo superior del rango de 31 a 34 dólares que había comercializado entre inversores.", "nucleo": true}, {"texto": "Reddit recaudó aproximadamente 748 millones de dólares con su oferta pública inicial.", "nucleo": true}, {"texto": "A ese precio, la empresa de redes sociales está valorada en aproximadamente 6.400 millones de dólares.", "nucleo": true}, {"texto": "Unos 228 millones de dólares corresponden a acciones vendidas por accionistas existentes que decidieron vender parte de sus participaciones.", "nucleo": true}, {"texto": "Excluyendo esas ventas secundarias, Reddit recaudó 519,4 millones de dólares en ingresos brutos.", "nucleo": true}, {"texto": "Las acciones comenzarán a cotizar en la Bolsa de Nueva York (NYSE) bajo el símbolo RDDT.", "nucleo": true}, {"texto": "Morgan Stanley, Goldman Sachs, JPMorgan Chase y Bank of America son los sindicatos gestores principales de la oferta.", "nucleo": true}, {"texto": "Muchas startups que habían planeado salir a bolsa en 2022 pospusieron sus planes.", "nucleo": true}, {"texto": "Reddit ha comenzado a licenciar su archivo de conversaciones públicas a empresas que entrenan modelos de inteligencia artificial.", "nucleo": true}, {"texto": "Reddit reservó parte de la oferta para algunos de sus usuarios más activos y moderadores, quienes pudieron comprar acciones al precio de la OPV antes de que comenzara la negociación.", "nucleo": true}, {"texto": "Reddit fue fundada en 2005 por Steve Huffman y Alexis Ohanian.", "nucleo": true}, {"texto": "Reddit fue adquirida por Condé Nast un año después de su fundación, en 2006.", "nucleo": true}, {"texto": "Reddit volvió a ser independiente en 2011.", "nucleo": true}, {"texto": "Steve Huffman es el director ejecutivo de la empresa.", "nucleo": true}, {"texto": "Reddit estableció una estructura de gobierno corporativo que otorga a algunos accionistas más poder de voto que a otros, limitando la influencia de los inversores que compran en la oferta pública.", "nucleo": true}, {"texto": "En una ronda de financiación privada en 2021, Reddit estuvo valorada en 10.000 millones de dólares.", "nucleo": true}, {"texto": "La valoración de la OPV está muy por debajo de lo que los inversores privados pagaron por la empresa antes de la caída del mercado.", "nucleo": true}]}
```