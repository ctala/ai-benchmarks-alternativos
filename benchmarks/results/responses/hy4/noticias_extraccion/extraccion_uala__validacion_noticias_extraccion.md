# Tencent Hy4 — noticias_extraccion/extraccion_uala

- model_id: `tencent/hy4`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 111.102s | tokens_per_second: 116.2
- input_tokens: 1200 | output_tokens: 12905

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
Ualá recauda US$350 millones en una Serie D liderada por SoftBank y Tencent

Buenos Aires — Ualá, la fintech argentina que ofrece una cuenta y una tarjeta prepaga gestionadas desde el teléfono, cerró en agosto de 2021 una ronda Serie D de US$350 millones con una valoración posterior a la inversión de US$2.450 millones.

La ronda fue codirigida por el SoftBank Latin America Fund y por afiliadas de Tencent. También participaron inversionistas que ya estaban en la compañía, entre ellos Goldman Sachs, Soros Fund Management y Ribbit Capital.

Según la empresa, se trata de la mayor ronda privada de inversión de la historia para una compañía argentina.

Las billeteras digitales crecieron en América Latina sobre una base conocida: una parte grande de la población no tiene cuenta bancaria o la usa poco, y el efectivo sigue dominando los pagos cotidianos. Una app que permite recibir dinero, pagar servicios y comprar en línea con una tarjeta asociada resuelve un problema concreto. El desafío está en ganar dinero con eso: las comisiones por transacción son bajas y el negocio rentable suele venir del crédito, que exige gestionar riesgo en economías con inflación alta y tasas que cambian rápido.

La empresa fue fundada por Pierpaolo Barbieri, que es su director ejecutivo. Ualá opera en Argentina y en México, y la compañía dijo que usará los fondos para sumar productos financieros, como inversiones, seguros y préstamos, y para fortalecer su operación mexicana.

No es la primera vez que estos inversionistas apuestan por la compañía. SoftBank y Tencent ya habían liderado una ronda de US$150 millones en 2019, que fue la primera operación conocida de SoftBank en Argentina.

En el mercado argentino, las fintech compiten con bancos tradicionales que también aceleraron sus aplicaciones y con billeteras de grandes plataformas de comercio electrónico. La ventaja de una compañía independiente suele estar en la experiencia de uso y en la velocidad para lanzar productos; su desventaja, en el costo de fondear el crédito sin una base de depósitos estable.

Analistas del sector advierten que las valoraciones de 2021 reflejan un ciclo de capital abundante y que la prueba real será sostener el crecimiento cuando ese ciclo termine.

La experiencia de otras billeteras de la región muestra que la escala no basta. Las empresas que lograron sostenerse combinaron una base grande de usuarios activos con productos de crédito bien calibrados y una estructura de costos ajustada. Las que crecieron solo con promociones vieron cómo sus clientes se iban apenas terminaban los beneficios. Por eso los inversionistas miran cada vez más la actividad mensual y el uso de los productos financieros, y menos el número total de cuentas abiertas.

Con esta operación, el financiamiento total de Ualá llega a US$544 millones.



## Respuesta completa

{"claims":[{"texto":"Según el titular de la nota, Ualá recaudó US$350 millones.","nucleo":true},{"texto":"Según el titular de la nota, la ronda de Ualá de US$350 millones fue una Serie D.","nucleo":true},{"texto":"Según el titular de la nota, la Serie D de Ualá fue liderada por SoftBank y Tencent.","nucleo":true},{"texto":"Ualá es una fintech argentina.","nucleo":false},{"texto":"Ualá ofrece una cuenta gestionada desde el teléfono.","nucleo":false},{"texto":"Ualá ofrece una tarjeta prepaga gestionada desde el teléfono.","nucleo":false},{"texto":"Ualá cerró una ronda Serie D en agosto de 2021.","nucleo":true},{"texto":"La ronda Serie D que Ualá cerró en agosto de 2021 fue de US$350 millones.","nucleo":true},{"texto":"La ronda Serie D que Ualá cerró en agosto de 2021 tuvo una valoración posterior a la inversión de US$2.450 millones.","nucleo":true},{"texto":"La ronda Serie D de Ualá de US$350 millones fue codirigida por el SoftBank Latin America Fund.","nucleo":true},{"texto":"La ronda Serie D de Ualá de US$350 millones fue codirigida por afiliadas de Tencent.","nucleo":true},{"texto":"Goldman Sachs participó en la ronda Serie D de Ualá de US$350 millones.","nucleo":true},{"texto":"Soros Fund Management participó en la ronda Serie D de Ualá de US$350 millones.","nucleo":true},{"texto":"Ribbit Capital participó en la ronda Serie D de Ualá de US$350 millones.","nucleo":true},{"texto":"Goldman Sachs ya era inversionista de Ualá antes de la ronda Serie D de US$350 millones.","nucleo":false},{"texto":"Soros Fund Management ya era inversionista de Ualá antes de la ronda Serie D de US$350 millones.","nucleo":false},{"texto":"Ribbit Capital ya era inversionista de Ualá antes de la ronda Serie D de US$350 millones.","nucleo":false},{"texto":"Según Ualá, su ronda Serie D de US$350 millones es la mayor ronda privada de inversión de la historia para una compañía argentina.","nucleo":false},{"texto":"Ualá fue fundada por Pierpaolo Barbieri.","nucleo":false},{"texto":"Pierpaolo Barbieri es el director ejecutivo de Ualá.","nucleo":false},{"texto":"Ualá opera en Argentina.","nucleo":false},{"texto":"Ualá opera en México.","nucleo":false},{"texto":"Ualá dijo que usará los fondos de la ronda Serie D de US$350 millones para sumar productos financieros como inversiones, seguros y préstamos.","nucleo":false},{"texto":"Ualá dijo que usará los fondos de la ronda Serie D de US$350 millones para fortalecer su operación mexicana.","nucleo":false},{"texto":"SoftBank lideró una ronda de inversión en Ualá en 2019.","nucleo":false},{"texto":"Tencent lideró una ronda de inversión en Ualá en 2019.","nucleo":false},{"texto":"La ronda de Ualá liderada por SoftBank y Tencent en 2019 fue de US$150 millones.","nucleo":false},{"texto":"La ronda de Ualá de US$150 millones de 2019 fue la primera operación conocida de SoftBank en Argentina.","nucleo":false},{"texto":"Con la ronda Serie D de US$350 millones, el financiamiento total de Ualá llega a US$544 millones.","nucleo":false}]}