# Muse Ember — noticias_verificacion/bloquea_nubank_mil_vs_millones

- model_id: `meta/muse-ember`
- success: True  | final: 9.27 | quality: 10.0
- latency_total: 2.268s | tokens_per_second: 696.5
- input_tokens: 1029 | output_tokens: 1580

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

AFIRMACIONES A VERIFICAR (6):
1. Nubank recaudó unos US$2.600 millones en su OPI.
2. Nubank vendió 289.000 acciones en su OPI.
3. El precio quedó en el piso del rango de US$8 a US$9.
4. Cristina Junqueira es cofundadora de Nubank.
5. Nubank tiene 50 millones de clientes.
6. Con el rango original, Nubank aspiraba a recaudar hasta US$3.180 millones.


## Respuesta completa

{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "CONTRADICE"}, {"id": 3, "veredicto": "CONTRADICE"}, {"id": 4, "veredicto": "RESPALDADO"}, {"id": 5, "veredicto": "NO_RESPALDADO"}, {"id": 6, "veredicto": "RESPALDADO"}]}