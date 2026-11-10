# Qwen 3-Next 80B Instruct — noticias_extraccion/extraccion_notco

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.08 | quality: 9.67
- latency_total: 3.01s | tokens_per_second: 191.3
- input_tokens: 1216 | output_tokens: 576

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

{
  "claims": [
    {
      "texto": "NotCo cerró una ronda Serie D de US$235 millones.",
      "nucleo": true
    },
    {
      "texto": "NotCo fue valorada en US$1.500 millones tras la ronda Serie D.",
      "nucleo": true
    },
    {
      "texto": "La ronda Serie D de NotCo fue liderada por Tiger Global.",
      "nucleo": true
    },
    {
      "texto": "DFJ Growth participó como nuevo inversionista en la ronda Serie D de NotCo.",
      "nucleo": true
    },
    {
      "texto": "Zoma Lab, el fondo de Kenneth Zomosa, participó como nuevo inversionista en la ronda Serie D de NotCo.",
      "nucleo": true
    },
    {
      "texto": "Lewis Hamilton participó como inversionista en la ronda Serie D de NotCo.",
      "nucleo": true
    },
    {
      "texto": "Roger Federer participó como inversionista en la ronda Serie D de NotCo.",
      "nucleo": true
    },
    {
      "texto": "Questlove participó como inversionista en la ronda Serie D de NotCo.",
      "nucleo": true
    },
    {
      "texto": "NotCo fue fundada en 2015 en Santiago por Matías Muchnick, Karim Pichara y Pablo Zamora.",
      "nucleo": true
    },
    {
      "texto": "Según NotCo, los fondos de la ronda Serie D se destinarán a ampliar su presencia en nuevas categorías en Norteamérica.",
      "nucleo": false
    },
    {
      "texto": "Según NotCo, los fondos de la ronda Serie D se destinarán a escalar su tecnología de inteligencia artificial.",
      "nucleo": false
    },
    {
      "texto": "Según NotCo, los fondos de la ronda Serie D se destinarán a acelerar su llegada a Europa y Asia.",
      "nucleo": false
    },
    {
      "texto": "Scott Shleifer, socio de Tiger Global, sostuvo que NotCo ha creado productos de origen vegetal de primer nivel que están ganando participación de mercado con rapidez.",
      "nucleo": false
    },
    {
      "texto": "NotCo suma más de US$350 millones levantados desde su fundación.",
      "nucleo": true
    }
  ]
}