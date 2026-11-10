# Ling 3.0 Flash VL — noticias_extraccion/extraccion_nubank

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 8.29 | quality: 8.41
- latency_total: 9.784s | tokens_per_second: 268.8
- input_tokens: 1229 | output_tokens: 2630

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
Nubank recauda US$2.600 millones en su salida a la bolsa de Nueva York

São Paulo — Nu Holdings, la empresa matriz del banco digital brasileño Nubank, fijó el precio de su oferta pública inicial en US$9 por acción, el tope del rango de US$8 a US$9 que había presentado a los inversionistas. La compañía vendió 289 millones de acciones y recaudó unos US$2.600 millones.

Las acciones empezaron a cotizar el 9 de diciembre de 2021 en la Bolsa de Nueva York con el símbolo NU. También se negocian en São Paulo como certificados de depósito, con el código NUBR33.

Al precio de la oferta, la valoración implícita de la compañía ronda los US$41.400 millones, lo que la convierte en la institución financiera más valiosa de América Latina, por encima de Itaú Unibanco, que vale unos US$38.000 millones en bolsa.

Los bancos digitales ganaron terreno en Brasil por una combinación de factores: una banca tradicional muy concentrada, con tarifas altas y mala experiencia de servicio, y una población que adoptó el teléfono como principal puerta de entrada a internet. La estrategia de estas empresas suele empezar con un producto gratuito y fácil de contratar, como una tarjeta sin comisión anual, para luego ofrecer cuentas, inversiones, seguros y créditos a la misma base de clientes.

Nubank fue fundada en 2013 por David Vélez, Cristina Junqueira y Edward Wible. Vélez, nacido en Colombia, es el director ejecutivo. La compañía opera en Brasil, México y Colombia.

Entre los inversionistas de la empresa antes de la salida a bolsa figuraban Sequoia Capital, Tencent y Berkshire Hathaway, que había invertido meses antes.

Las salidas a bolsa de empresas latinoamericanas en Estados Unidos son poco frecuentes, y los banqueros esperaban que el resultado de Nubank sirviera de referencia para otras compañías de la región que preparan su debut.

Para los inversionistas, la pregunta central sobre los bancos digitales es cuánto ganan por cliente y cuánto les cuesta adquirirlo. Las empresas que crecen con tarjetas de crédito asumen riesgo desde el primer día, y la calidad de su modelo de aprobación se pone a prueba recién cuando la economía se desacelera. Por eso los analistas siguen de cerca los indicadores de morosidad y el costo del fondeo, además del crecimiento de la base de clientes, y comparan esas cifras con las de los bancos tradicionales del mismo mercado.

El camino hasta el precio final no fue lineal. La semana anterior, Nubank había rebajado el rango de precio; con el rango original, la empresa aspiraba a recaudar hasta US$3.180 millones.



## Respuesta completa

```json
{"claims": [{"texto": "Nu Holdings fijó el precio de su oferta pública inicial en US$9 por acción", "nucleo": true}, {"texto": "El rango de precio presentado por Nu Holdings a los inversionistas fue de US$8 a US$9", "nucleo": true}, {"texto": "Nu Holdings vendió 289 millones de acciones en su oferta pública inicial", "nucleo": true}, {"texto": "Nu Holdings recaudó unos US$2.600 millones en su oferta pública inicial", "nucleo": true}, {"texto": "Las acciones de Nu Holdings empezaron a cotizar el 9 de diciembre de 2021 en la Bolsa de Nueva York con el símbolo NU", "nucleo": true}, {"texto": "Las acciones de Nu Holdings también se negocian en São Paulo como certificados de depósito con el código NUBR33", "nucleo": true}, {"texto": "La valoración implícita de Nu Holdings al precio de la oferta ronda los US$41.400 millones", "nucleo": true}, {"texto": "Nu Holdings es la institución financiera más valiosa de América Latina", "nucleo": true}, {"texto": "Itaú Unibanco vale unos US$38.000 millones en bolsa", "nucleo": true}, {"texto": "Nubank fue fundada en 2013 por David Vélez, Cristina Junqueira y Edward Wible", "nucleo": true}, {"texto": "David Vélez, nacido en Colombia, es el director ejecutivo de Nubank", "nucleo": true}, {"texto": "Nubank opera en Brasil, México y Colombia", "nucleo": true}, {"texto": "Entre los inversionistas de Nubank antes de la salida a bolsa figuraban Sequoia Capital, Tencent y Berkshire Hathaway", "nucleo": true}, {"texto": "Berkshire Hathaway había invertido en Nubank meses antes de la salida a bolsa", "nucleo": true}, {"texto": "Nubank había rebajado el rango de precio la semana anterior a la fijación del precio final de la oferta", "nucleo": true}, {"texto": "Con el rango original de precio, Nubank aspiraba a recaudar hasta US$3.180 millones", "nucleo": true}, {"texto": "Los bancos digitales ganaron terreno en Brasil porque la banca tradicional es muy concentrada, con tarifas altas y mala experiencia de servicio", "nucleo": false}, {"texto": "Los bancos digitales ganaron terreno en Brasil porque la población adoptó el teléfono como principal puerta de entrada a internet", "nucleo": false}, {"texto": "Las salidas a bolsa de empresas latinoamericanas en Estados Unidos son poco frecuentes", "nucleo": false}, {"texto": "Los banqueros esperaban que el resultado de Nubank sirviera de referencia para otras compañías de la región que preparan su debut", "nucleo": false}]}
```