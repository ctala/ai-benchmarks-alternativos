# Qwen 3-Next 80B Instruct — noticias_extraccion/extraccion_fintual

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.78 | quality: 9.25
- latency_total: 3.03s | tokens_per_second: 193.7
- input_tokens: 1156 | output_tokens: 587

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
Fintual levanta US$39 millones en una ronda liderada por Sequoia Capital

Santiago — Fintual, la administradora de fondos chilena que permite invertir desde una aplicación, cerró en noviembre de 2021 una ronda Serie B de US$39 millones liderada por Sequoia Capital. También participaron ALLVP y Kaszek, que ya eran inversionistas desde la Serie A.

Es la primera inversión de Sequoia en Chile y, según la prensa local, la tercera del fondo en una empresa latinoamericana, después de Rappi y Nubank.

Fintual nació con una idea concreta: que una persona sin conocimientos financieros pueda invertir en fondos diversificados con montos pequeños y comisiones bajas, sin pasar por un ejecutivo. En Chile, el ahorro voluntario para la jubilación es un mercado relevante porque las pensiones del sistema obligatorio suelen quedar por debajo de lo que las personas esperan, y eso empuja a muchos trabajadores a buscar alternativas.

La compañía fue fundada en 2016 por Pedro Pineda, Agustín Feuerhake, Alfonso Valdés y Pablo Mansilla. Opera en Chile y en México, donde lanzó su servicio en 2020.

Según la empresa, los recursos se destinarán principalmente a acelerar su operación en México, aunque también seguirá creciendo en Chile.

Unos meses antes, Fintual había levantado cerca de US$15 millones en una Serie A liderada por Kaszek.

Las plataformas de inversión digital compiten con bancos y administradoras tradicionales que han lanzado sus propias aplicaciones, y con corredoras que ofrecen acciones sin comisión. El costo de adquirir clientes es alto y la rentabilidad depende de acumular un volumen grande de activos administrados, porque las comisiones, por diseño, son bajas.

Para los inversionistas de riesgo, el atractivo del modelo está en su escala potencial: una vez que la plataforma funciona en un país, sumar clientes cuesta poco y cada peso administrado genera ingresos durante años. El riesgo está en que la regulación y la cultura de ahorro cambian de un país a otro, y lo que funcionó en Chile no necesariamente se replica en México.

Los reguladores también observan de cerca a estas plataformas. Las administradoras de fondos deben cumplir reglas sobre cómo invierten el dinero de sus clientes, cómo informan las comisiones y cómo protegen los activos ante una eventual quiebra de la propia administradora. Para las empresas nuevas, cumplir esas exigencias desde el inicio es costoso, pero también es lo que les permite competir en confianza con instituciones que llevan décadas en el mercado y que tienen marcas reconocidas por varias generaciones de ahorrantes.

La ronda dejó también una meta explícita: alcanzar la rentabilidad. Según Diario Financiero, la empresa reportó utilidades por primera vez en el primer semestre de 2024.



## Respuesta completa

{
  "claims": [
    {
      "texto": "Fintual cerró en noviembre de 2021 una ronda Serie B de US$39 millones liderada por Sequoia Capital.",
      "nucleo": true
    },
    {
      "texto": "ALLVP participó en la ronda Serie B de Fintual de noviembre de 2021.",
      "nucleo": true
    },
    {
      "texto": "Kaszek participó en la ronda Serie B de Fintual de noviembre de 2021.",
      "nucleo": true
    },
    {
      "texto": "Kaszek ya era inversionista de Fintual desde la Serie A.",
      "nucleo": false
    },
    {
      "texto": "Sequoia Capital hizo su primera inversión en Chile al participar en la ronda Serie B de Fintual.",
      "nucleo": true
    },
    {
      "texto": "Según la prensa local, la inversión de Sequoia Capital en Fintual fue la tercera del fondo en una empresa latinoamericana, después de Rappi y Nubank.",
      "nucleo": false
    },
    {
      "texto": "Fintual fue fundada en 2016 por Pedro Pineda, Agustín Feuerhake, Alfonso Valdés y Pablo Mansilla.",
      "nucleo": true
    },
    {
      "texto": "Fintual opera en Chile y en México.",
      "nucleo": true
    },
    {
      "texto": "Fintual lanzó su servicio en México en 2020.",
      "nucleo": true
    },
    {
      "texto": "Según Fintual, los recursos de la ronda Serie B se destinarán principalmente a acelerar su operación en México.",
      "nucleo": false
    },
    {
      "texto": "Según Fintual, los recursos de la ronda Serie B también se destinarán a seguir creciendo en Chile.",
      "nucleo": false
    },
    {
      "texto": "Fintual había levantado cerca de US$15 millones en una Serie A liderada por Kaszek unos meses antes de la ronda Serie B de noviembre de 2021.",
      "nucleo": true
    },
    {
      "texto": "Fintual reportó utilidades por primera vez en el primer semestre de 2024, según Diario Financiero.",
      "nucleo": true
    }
  ]
}