# GLM 5.3 — noticias_extraccion/extraccion_adobe_figma

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.17 | quality: 9.83
- latency_total: 51.417s | tokens_per_second: 83.4
- input_tokens: 1077 | output_tokens: 4290

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
Adobe y Figma renuncian a su fusión de US$20.000 millones

Adobe y Figma acordaron poner fin a la operación por la que Adobe iba a comprar a la plataforma de diseño colaborativo por US$20.000 millones. Las compañías anunciaron la decisión en diciembre de 2023, después de concluir que no veían un camino claro para obtener las aprobaciones de la Comisión Europea y de la Autoridad de Competencia y Mercados del Reino Unido (CMA).

La compra se había anunciado en septiembre de 2022 y desde el primer día despertó dudas entre los reguladores. Figma se había convertido en la herramienta preferida de muchos equipos de producto para diseñar interfaces en el navegador, un terreno en el que Adobe competía con sus propios productos.

Las fusiones entre una empresa dominante y un competidor emergente son las que más preocupan a las autoridades de competencia. La teoría es conocida: una compañía grande puede pagar una prima alta por un rival pequeño no por lo que vale hoy, sino para evitar que le quite clientes mañana. Para demostrarlo, los reguladores analizan documentos internos, superposición de productos y el efecto probable sobre los precios y la innovación, un proceso que puede tomar más de un año.

Durante la revisión, la CMA británica planteó que la operación solo podría seguir adelante si Adobe se desprendía de activos y de código fuente, una propuesta que Adobe rechazó. En Europa, la Comisión había abierto una investigación a fondo y luego informó que estaba al tanto de la decisión de terminar el acuerdo.

El director ejecutivo de Adobe, Shantanu Narayen, dijo que ambas compañías estaban en profundo desacuerdo con las conclusiones de los reguladores, pero que habían decidido que lo mejor era seguir adelante por separado. Dylan Field, cofundador y director ejecutivo de Figma, sostuvo que la empresa seguiría operando de forma independiente.

Para las startups, el caso deja una lección práctica sobre los acuerdos de venta: el riesgo regulatorio no es abstracto y puede tomar más de un año resolverlo, tiempo en el que el equipo vendedor trabaja con el futuro en pausa. Por eso los compradores grandes suelen aceptar cláusulas que compensan al vendedor si la operación se cae por motivos regulatorios.

El caso también mostró cómo cambió la actitud de los reguladores frente a las grandes tecnológicas. Durante años, la mayoría de las compras de startups por parte de empresas dominantes se aprobaron sin mayor revisión. Hoy, las autoridades de Europa y del Reino Unido revisan con más atención las operaciones en las que el comprador ya tiene una posición fuerte, incluso cuando la empresa comprada todavía es pequeña en ingresos, y exigen remedios que muchas veces los compradores no están dispuestos a aceptar.

Ese es justamente el punto final de esta historia. De acuerdo con los documentos presentados ante el regulador bursátil estadounidense, Adobe deberá pagar a Figma una comisión de terminación de US$1.000 millones en efectivo.



## Respuesta completa

{"claims": [{"texto": "Adobe y Figma acordaron poner fin a la operación por la que Adobe iba a comprar a Figma por US$20.000 millones.", "nucleo": true}, {"texto": "Adobe y Figma anunciaron en diciembre de 2023 la decisión de poner fin a la operación de compra.", "nucleo": true}, {"texto": "Adobe y Figma terminaron la operación tras concluir que no veían un camino claro para obtener las aprobaciones de la Comisión Europea y de la Autoridad de Competencia y Mercados del Reino Unido (CMA).", "nucleo": true}, {"texto": "La compra de Figma por parte de Adobe había sido anunciada en septiembre de 2022.", "nucleo": false}, {"texto": "Figma es una plataforma de diseño colaborativo.", "nucleo": false}, {"texto": "Figma se había convertido en la herramienta preferida de muchos equipos de producto para diseñar interfaces en el navegador.", "nucleo": false}, {"texto": "Adobe competía con sus propios productos con Figma en el terreno del diseño de interfaces en el navegador.", "nucleo": false}, {"texto": "La CMA británica planteó que la operación entre Adobe y Figma solo podría seguir adelante si Adobe se desprendía de activos y de código fuente.", "nucleo": true}, {"texto": "Adobe rechazó la propuesta de la CMA de desprenderse de activos y de código fuente para que la operación siguiera adelante.", "nucleo": true}, {"texto": "La Comisión Europea había abierto una investigación a fondo sobre la compra de Figma por Adobe.", "nucleo": true}, {"texto": "La Comisión Europea informó que estaba al tanto de la decisión de Adobe y Figma de terminar el acuerdo.", "nucleo": true}, {"texto": "El director ejecutivo de Adobe, Shantanu Narayen, dijo que Adobe y Figma estaban en profundo desacuerdo con las conclusiones de los reguladores, pero que habían decidido seguir adelante por separado.", "nucleo": false}, {"texto": "Dylan Field, cofundador y director ejecutivo de Figma, sostuvo que Figma seguiría operando de forma independiente.", "nucleo": false}, {"texto": "Según los documentos presentados ante el regulador bursátil estadounidense, Adobe deberá pagar a Figma una comisión de terminación de US$1.000 millones en efectivo.", "nucleo": true}]}