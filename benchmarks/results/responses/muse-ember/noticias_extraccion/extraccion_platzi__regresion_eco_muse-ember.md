# Muse Ember — noticias_extraccion/extraccion_platzi

- model_id: `meta/muse-ember`
- success: True  | final: 8.87 | quality: 9.85
- latency_total: 5.487s | tokens_per_second: 648.3
- input_tokens: 916 | output_tokens: 3557

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
Platzi cierra una Serie B liderada por Prosus

Bogotá — Platzi, la plataforma de educación en línea para profesionales de tecnología, cerró en diciembre de 2021 una ronda Serie B liderada por Prosus. La empresa informó un monto de US$62 millones; en su propio comunicado, Prosus habló de US$60 millones.

En la ronda también participaron Foundation Capital y Y Combinator, aceleradora por la que pasó la compañía en sus primeros años.

La educación en línea para adultos vive de una promesa: que un curso permita conseguir un empleo mejor pagado o un ascenso. El problema clásico del sector es la deserción. La mayoría de las personas que se inscribe en un curso en línea no lo termina, y las plataformas que logran retener a sus estudiantes lo hacen con comunidades, rutas de aprendizaje con objetivos claros y contenido que se actualiza al ritmo de la industria.

La compañía fue fundada por Freddy Vega y Christian Van Der Henst, y dice haber atendido a más de 3 millones de estudiantes en América Latina.

Según la empresa, los fondos se destinarán a hacer la plataforma más accesible, a ampliar su academia de inglés y a fortalecer su oferta para empresas y gobiernos, que compran licencias para capacitar a sus equipos.

El mercado de talento tecnológico en la región explica parte del interés de los inversionistas. Las empresas de software de Estados Unidos y Europa contratan cada vez más desarrolladores latinoamericanos de forma remota, y la demanda de perfiles con buen nivel de inglés supera a la oferta disponible.

La competencia incluye a plataformas globales con catálogos más grandes y a bootcamps intensivos que prometen un cambio de carrera en pocos meses. La apuesta de Platzi es ofrecer contenido producido en español y pensado para el mercado laboral latinoamericano.

La venta a empresas se volvió una pieza central para las plataformas de educación en línea. Las compañías prefieren pagar licencias anuales para capacitar a sus equipos en lugar de reembolsar cursos individuales, y ese tipo de contrato es más predecible que las suscripciones de personas que se inscriben y cancelan según su momento laboral. Para la plataforma, el reto es demostrar que la capacitación tiene un efecto medible en el desempeño, porque eso es lo que justifica la renovación de los contratos cuando los presupuestos de recursos humanos se ajustan y las áreas de formación compiten con otras prioridades.

La empresa anunció además que, con estos recursos, iniciará operaciones en Brasil.



## Respuesta completa

{"claims": [{"texto": "Platzi cerró una ronda Serie B en diciembre de 2021.", "nucleo": true}, {"texto": "Prosus lideró la ronda Serie B de Platzi.", "nucleo": true}, {"texto": "Platzi informó un monto de US$62 millones para su ronda Serie B.", "nucleo": true}, {"texto": "Prosus habló de US$60 millones en su propio comunicado sobre la ronda Serie B de Platzi.", "nucleo": true}, {"texto": "Foundation Capital participó en la ronda Serie B de Platzi.", "nucleo": true}, {"texto": "Y Combinator participó en la ronda Serie B de Platzi.", "nucleo": true}, {"texto": "Platzi pasó por Y Combinator, una aceleradora, en sus primeros años.", "nucleo": false}, {"texto": "Platzi fue fundada por Freddy Vega y Christian Van Der Henst.", "nucleo": false}, {"texto": "Según Platzi, Platzi ha atendido a más de 3 millones de estudiantes en América Latina.", "nucleo": false}, {"texto": "Según Platzi, los fondos de la ronda Serie B se destinarán a hacer la plataforma de Platzi más accesible.", "nucleo": false}, {"texto": "Según Platzi, los fondos de la ronda Serie B se destinarán a ampliar la academia de inglés de Platzi.", "nucleo": false}, {"texto": "Según Platzi, los fondos de la ronda Serie B se destinarán a fortalecer la oferta de Platzi para empresas y gobiernos.", "nucleo": false}, {"texto": "Las empresas y los gobiernos compran licencias de Platzi para capacitar a sus equipos.", "nucleo": false}, {"texto": "Platzi anunció que, con los recursos de la ronda Serie B, iniciará operaciones en Brasil.", "nucleo": false}]}