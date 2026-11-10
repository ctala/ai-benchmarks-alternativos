# Tencent Hy4 — noticias_extraccion/extraccion_notco

- model_id: `tencent/hy4`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 206.797s | tokens_per_second: 126.1
- input_tokens: 1254 | output_tokens: 26077

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
NotCo levanta US$235 millones y se convierte en unicornio

Santiago — La foodtech chilena NotCo, que desarrolla alternativas de origen vegetal a la leche, la mayonesa, los helados y la carne, cerró una ronda Serie D de US$235 millones que la valora en US$1.500 millones.

La ronda fue liderada por Tiger Global. Se sumaron como nuevos inversionistas DFJ Growth y Zoma Lab, el fondo de Kenneth Zomosa, y también participaron figuras del deporte y la música: el piloto de Fórmula 1 Lewis Hamilton, el tenista Roger Federer y el músico Questlove.

La categoría de alimentos de origen vegetal se apoya en una promesa sencilla de explicar y difícil de cumplir: reproducir el sabor, la textura y el comportamiento en la cocina de un producto animal usando solo plantas. La mayoría de las empresas del sector trabaja por prueba y error en laboratorios de alimentos, con ciclos de desarrollo que pueden durar años. La diferencia que reclaman las compañías más nuevas es usar modelos de aprendizaje automático para recorrer miles de combinaciones de ingredientes antes de llevar una receta a la cocina de pruebas.

NotCo fue fundada en 2015 en Santiago por Matías Muchnick, Karim Pichara y Pablo Zamora. Su sistema, al que llama Giuseppe, cruza la estructura molecular de los alimentos de origen animal con una base de datos de plantas para proponer recetas que imiten el producto original.

Según la compañía, los fondos se destinarán a ampliar su presencia en nuevas categorías en Norteamérica, a escalar su tecnología de inteligencia artificial y a acelerar su llegada a Europa y Asia.

En el comunicado, Scott Shleifer, socio de Tiger Global, sostuvo que NotCo ha creado productos de origen vegetal de primer nivel que están ganando participación de mercado con rapidez.

La categoría vive un momento de presión. Los fondos que entraron con fuerza a las proteínas alternativas en los últimos años empiezan a exigir crecimiento en ventas y no solo en distribución, y varias marcas del hemisferio norte han tenido que recortar personal o retirar productos de las góndolas. En ese contexto, los inversionistas miran con atención la capacidad de cada compañía de mantener el precio cerca del producto tradicional, que es lo que define si el consumidor repite la compra.

Para las startups de la región, la ronda vuelve a mostrar que los fondos globales de crecimiento están dispuestos a apostar por compañías latinoamericanas que compiten fuera de su mercado de origen. También muestra el peso que tiene la presencia en Estados Unidos a la hora de fijar una valoración.

En las góndolas, la competencia no se limita a otras startups. Las grandes empresas de alimentos y bebidas lanzaron sus propias líneas vegetales y tienen una ventaja difícil de igualar: acceso a distribución, poder de negociación con los supermercados y presupuestos de marketing muy superiores. Por eso varias foodtech optaron por asociarse con esos mismos gigantes en lugar de enfrentarlos, y licencian su tecnología o desarrollan productos en conjunto.

Con esta operación, NotCo suma más de US$350 millones levantados desde su fundación.



## Respuesta completa

{"claims":[{"texto":"NotCo es una foodtech.","nucleo":false},{"texto":"NotCo es chilena.","nucleo":false},{"texto":"NotCo desarrolla alternativas de origen vegetal a la leche, la mayonesa, los helados y la carne.","nucleo":false},{"texto":"NotCo cerró una ronda Serie D.","nucleo":true},{"texto":"La ronda Serie D de NotCo fue de US$235 millones.","nucleo":true},{"texto":"NotCo fue valorada en US$1.500 millones en su ronda Serie D.","nucleo":true},{"texto":"NotCo se convirtió en unicornio con su ronda Serie D.","nucleo":true},{"texto":"La ronda Serie D de NotCo fue liderada por Tiger Global.","nucleo":true},{"texto":"DFJ Growth se sumó como nuevo inversionista a la ronda Serie D de NotCo.","nucleo":true},{"texto":"Zoma Lab se sumó como nuevo inversionista a la ronda Serie D de NotCo.","nucleo":true},{"texto":"Zoma Lab es el fondo de Kenneth Zomosa.","nucleo":false},{"texto":"Lewis Hamilton participó en la ronda Serie D de NotCo.","nucleo":true},{"texto":"Roger Federer participó en la ronda Serie D de NotCo.","nucleo":true},{"texto":"Questlove participó en la ronda Serie D de NotCo.","nucleo":true},{"texto":"Lewis Hamilton es piloto de Fórmula 1.","nucleo":false},{"texto":"Roger Federer es tenista.","nucleo":false},{"texto":"Questlove es músico.","nucleo":false},{"texto":"Lewis Hamilton, Roger Federer y Questlove son figuras del deporte y la música.","nucleo":false},{"texto":"NotCo fue fundada en 2015.","nucleo":false},{"texto":"NotCo fue fundada en Santiago.","nucleo":false},{"texto":"NotCo fue fundada por Matías Muchnick.","nucleo":false},{"texto":"NotCo fue fundada por Karim Pichara.","nucleo":false},{"texto":"NotCo fue fundada por Pablo Zamora.","nucleo":false},{"texto":"NotCo llama Giuseppe a su sistema.","nucleo":false},{"texto":"El sistema Giuseppe de NotCo cruza la estructura molecular de los alimentos de origen animal con una base de datos de plantas para proponer recetas que imiten el producto original.","nucleo":false},{"texto":"Según la compañía NotCo, los fondos de la ronda Serie D de NotCo se destinarán a ampliar la presencia de NotCo en nuevas categorías en Norteamérica.","nucleo":false},{"texto":"Según la compañía NotCo, los fondos de la ronda Serie D de NotCo se destinarán a escalar la tecnología de inteligencia artificial de NotCo.","nucleo":false},{"texto":"Según la compañía NotCo, los fondos de la ronda Serie D de NotCo se destinarán a acelerar la llegada de NotCo a Europa y Asia.","nucleo":false},{"texto":"Scott Shleifer es socio de Tiger Global.","nucleo":false},{"texto":"En el comunicado, Scott Shleifer, socio de Tiger Global, sostuvo que NotCo ha creado productos de origen vegetal de primer nivel.","nucleo":false},{"texto":"En el comunicado, Scott Shleifer, socio de Tiger Global, sostuvo que los productos de origen vegetal de NotCo están ganando participación de mercado con rapidez.","nucleo":false},{"texto":"Con su ronda Serie D, NotCo suma más de US$350 millones levantados desde su fundación.","nucleo":false}]}