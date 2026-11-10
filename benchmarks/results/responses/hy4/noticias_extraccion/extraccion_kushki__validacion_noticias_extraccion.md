# Tencent Hy4 — noticias_extraccion/extraccion_kushki

- model_id: `tencent/hy4`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 116.432s | tokens_per_second: 114.1
- input_tokens: 1181 | output_tokens: 13280

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



## Respuesta completa

{"claims":[{"texto":"Kushki es una empresa ecuatoriana de infraestructura de pagos.","nucleo":false},{"texto":"Kushki anunció en junio de 2022 una extensión de US$100 millones de su ronda Serie B.","nucleo":true},{"texto":"La valoración de Kushki sube a US$1.500 millones con la extensión de su ronda Serie B anunciada en junio de 2022.","nucleo":true},{"texto":"Kushki pasa a ser el primer unicornio de Ecuador.","nucleo":true},{"texto":"En la extensión de la ronda Serie B de Kushki anunciada en junio de 2022 participaron Kaszek, Clocktower Ventures, el SoftBank Latin America Fund y DILA Capital.","nucleo":true},{"texto":"Con el tramo anunciado en junio de 2022, la Serie B completa de Kushki suma US$186 millones.","nucleo":true},{"texto":"El primer tramo de la Serie B de Kushki, de US$86 millones, se había anunciado en junio de 2021.","nucleo":false},{"texto":"La valoración posterior del primer tramo de la Serie B de Kushki fue de US$600 millones.","nucleo":false},{"texto":"En un año, Kushki más que duplicó su valor.","nucleo":false},{"texto":"Kushki fue fundada en 2016 en Quito por Aaron Gruber y Sebastián Castro.","nucleo":false},{"texto":"Kushki opera en Ecuador, Colombia, Perú, Chile y México.","nucleo":false},{"texto":"En Ecuador, Colombia, Perú, Chile y México, Kushki ofrece transferencias, pagos en efectivo y adquirencia propia, además de procesar pagos con tarjeta.","nucleo":false},{"texto":"Según la empresa, Kushki usará los fondos de la extensión de su ronda Serie B para ampliar su red de adquirencia directa en la región.","nucleo":false},{"texto":"Según la empresa, Kushki usará los fondos de la extensión de su ronda Serie B para sumar productos para comercios.","nucleo":false},{"texto":"Kushki no entregó cifras de ingresos.","nucleo":false},{"texto":"Kushki afirmó que sus ingresos crecieron 200% durante 2021.","nucleo":false}]}