# Ling 3.0 Flash VL — noticias_verificacion/pasa_kushki_sin_cifras

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.242s | tokens_per_second: 187.3
- input_tokens: 1254 | output_tokens: 420

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
Kushki se convierte en el primer unicornio de Ecuador

Quito — Kushki, la empresa ecuatoriana de infraestructura de pagos, anunció en junio de 2022 una extensión de US$100 millones de su ronda Serie B, con la que su valoración sube a US$1.500 millones. La compañía pasa a ser el primer unicornio de Ecuador.

En la extensión participaron Kaszek, Clocktower Ventures, el SoftBank Latin America Fund y DILA Capital. Con este tramo, la Serie B completa suma US$186 millones.

Las empresas de infraestructura de pagos son poco visibles para el consumidor, pero están detrás de casi cada compra en línea. Conectan a los comercios con las redes de tarjetas, los bancos adquirentes y los métodos de pago locales, y se encargan de autorizar, liquidar y conciliar cada transacción. En América Latina ese trabajo es más complejo que en otros mercados porque cada país tiene sus propios métodos de pago, reglas cambiarias y requisitos regulatorios.

El primer tramo de la Serie B, de US$86 millones, se había anunciado en junio de 2021 a una valoración posterior de US$600 millones. En un año, la compañía más que duplicó su valor.

Kushki fue fundada en 2016 en Quito por Aaron Gruber y Sebastián Castro. Opera en Ecuador, Colombia, Perú, Chile y México, donde además de procesar pagos con tarjeta ofrece transferencias, pagos en efectivo y adquirencia propia.

Los fondos se usarán, según la empresa, para ampliar su red de adquirencia directa en la región y para sumar productos para comercios.

Para el ecosistema ecuatoriano, que históricamente recibió muy poco capital de riesgo, la noticia tiene un peso simbólico. Inversionistas locales destacan que un unicornio suele generar una segunda ola de emprendimientos, cuando los primeros empleados salen a fundar sus propias empresas con experiencia y, a veces, con capital propio.

La competencia en infraestructura de pagos es intensa. Procesadores globales con presencia en decenas de países, bancos que ofrecen adquirencia a sus propios clientes y otras startups regionales buscan a los mismos comercios. La diferenciación suele estar en la cobertura de métodos de pago locales, la tasa de aprobación de las transacciones y la velocidad para integrar a un comercio nuevo. Para los grandes clientes, como plataformas de comercio electrónico o aplicaciones de transporte, una diferencia pequeña en la tasa de aprobación puede significar millones en ventas que se ganan o se pierden, y por eso suelen trabajar con más de un procesador a la vez y mover volumen hacia el que mejor rinde.

La compañía no entregó cifras de ingresos. Sí afirmó que sus ingresos crecieron 200% durante 2021.

AFIRMACIONES A VERIFICAR (5):
1. Kushki es el primer unicornio de Ecuador.
2. La Serie B completa de Kushki suma US$186 millones.
3. El primer tramo de la Serie B se valoró en US$600 millones.
4. Kushki no dio a conocer cuánto factura.
5. Según Kushki, sus ingresos crecieron 200% en 2021.


## Respuesta completa

{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "RESPALDADO"}, {"id": 3, "veredicto": "RESPALDADO"}, {"id": 4, "veredicto": "RESPALDADO"}, {"id": 5, "veredicto": "RESPALDADO"}]}