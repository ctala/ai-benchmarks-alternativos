# Ling 3.0 Flash — noticias_verificacion/pasa_platzi_dos_montos

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.236s | tokens_per_second: 146.7
- input_tokens: 1166 | output_tokens: 328

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

AFIRMACIONES A VERIFICAR (5):
1. Platzi informó una Serie B de US$62 millones.
2. Prosus habló de un monto de US$60 millones en su comunicado.
3. Prosus lideró la Serie B de Platzi.
4. Y Combinator participó en la ronda.
5. Platzi iniciará operaciones en Brasil.


## Respuesta completa

{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}, {"id": 2, "veredicto": "RESPALDADO"}, {"id": 3, "veredicto": "RESPALDADO"}, {"id": 4, "veredicto": "RESPALDADO"}, {"id": 5, "veredicto": "RESPALDADO"}]}