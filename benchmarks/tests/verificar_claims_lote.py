#!/usr/bin/env python3
"""verificar_claims_lote — devolver N juicios, no juzgar uno.

POR QUÉ EXISTE (17-ago-2026)
----------------------------
El benchmark recomendó **DeepSeek V4 Flash** para el gate de verificación del pipeline
de noticias de Eco (`verificar_claim` 8,60 · `content_verificable` 10,00, y cuatro veces
más barato). Se aplicó a producción y **falló en dos horas**:

    gate            notas   claims/nota   veredictos/nota   claims bloqueados
    gemini-2.5-flash   66       6,7        6,4  (96%)              19
    deepseek-v4-flash  14       4,7        2,2  (47%)               0

Cuatro notas —las de 9, 10, 10 y 11 claims— devolvieron **CERO veredictos**. Un claim sin
veredicto no puede bloquear, así que esas notas se publicaron sin verificar. El gate pasó
de frenar el 15,6% a frenar el 0,0%, **y en el tablero eso se veía como una mejora**.

POR QUÉ NUESTRO 8,60 NO LO PREDIJO
-----------------------------------
Porque `verificar_claim` manda **UN claim por test** —prompt de ~750 caracteres, respuesta
`{"veredicto": "..."}`— y mide la calidad del juicio. Producción manda **once**, con un
prompt de 4.218 caracteres, tres bloques de evidencia, reglas de precedencia, y pide `id`
y `razon` por cada uno.

Son tareas distintas. La de producción no es *juzgar un claim*: es **devolver N juicios
bien formados desde un prompt hostil**. Un modelo puede sacar 10,00 en la primera y 0 en
la segunda, y eso es exactamente lo que pasó.

LA CAUSA, MEDIDA
----------------
El nodo corre con `max_tokens: 2000`. DeepSeek V4 Flash razona (el benchmark lo tiene en
`THINKING_MODELS` y por eso le da 8.192). Un solo claim le consume 236 tokens de mediana
y 926 en el p90: **once no caben en 2.000**, y el JSON se corta antes de cerrar. Con
`response_format: json_object`, un objeto incompleto no es un veredicto malo — es ningún
veredicto. `gemini-2.5-flash` no razona, y por eso los mismos 2.000 le alcanzaban.

Es el mismo modo de falla que el 17-ago dejó a Claude Opus 5 en el puesto #79 de 83 con
el 31% de su examen cortado, con otra cara: allá texto truncado, acá un JSON que no cierra.

CÓMO SE MIDE
------------
Una sola nota, objetiva y sin juez: **claims con veredicto correcto / claims enviados**.
Un claim no devuelto cuenta como error, que es lo que es en producción. Devolver 2 de 11
—aunque los 2 estén perfectos— da 1,8, no 10.

El barrido es 1, 3, 5, 8, 12 y 15 claims **sobre el mismo material**: los tests chicos son
prefijos de los grandes, así que lo único que cambia es la carga. Un promedio de los seis
escondería el fallo (aparece recién pasados ~9); la curva lo muestra.

SE AGREGA, NO SE EDITA
----------------------
`verificar_claim` no se toca: mide bien lo que mide, y editarla invalidaría su histórico
(regla dura del repo). Esta suite mide la otra mitad, y entra al índice cuando tenga
cobertura, no antes.

Fuente del prompt: nodo «Verificar vs Fuente» de
`workflows/noticias-eco/b-generador-cola-a-verificado.json`, copiado literal.
Detalle del incidente: `operacion/eco-news-pipeline-fix/21-brief-benchmark-que-medir-en-el-gate.md`
"""

TESTS = [
    {
        "name": "lote_01_claims",
        "description": "Devolver 1 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (1):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO"
            }
        }
    },
    {
        "name": "lote_03_claims",
        "description": "Devolver 3 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (3):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek.\nc2: Kubo alcanzó una facturación anual de US$ 8 millones en 2025.\nc3: Kubo fue fundada en 2019."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO",
                "c2": "NO_RESPALDADO",
                "c3": "CONTRADICE"
            }
        }
    },
    {
        "name": "lote_05_claims",
        "description": "Devolver 5 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (5):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek.\nc2: Kubo alcanzó una facturación anual de US$ 8 millones en 2025.\nc3: Kubo fue fundada en 2019.\nc4: Kubo participó del programa Endeavor Chile en marzo de 2026.\nc5: Kubo procesa unos US$ 40 millones mensuales en transacciones."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO",
                "c2": "NO_RESPALDADO",
                "c3": "CONTRADICE",
                "c4": "RESPALDADO_RESEARCH",
                "c5": "RESPALDADO"
            }
        }
    },
    {
        "name": "lote_08_claims",
        "description": "Devolver 8 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (8):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek.\nc2: Kubo alcanzó una facturación anual de US$ 8 millones en 2025.\nc3: Kubo fue fundada en 2019.\nc4: Kubo participó del programa Endeavor Chile en marzo de 2026.\nc5: Kubo procesa unos US$ 40 millones mensuales en transacciones.\nc6: Kubo abrirá operación en México en el primer trimestre de 2027.\nc7: Kubo contratará 60 personas durante el próximo año.\nc8: Marta Riquelme es la CEO de Kubo."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO",
                "c2": "NO_RESPALDADO",
                "c3": "CONTRADICE",
                "c4": "RESPALDADO_RESEARCH",
                "c5": "RESPALDADO",
                "c6": "RESPALDADO",
                "c7": "NO_RESPALDADO",
                "c8": "RESPALDADO"
            }
        }
    },
    {
        "name": "lote_12_claims",
        "description": "Devolver 12 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (12):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek.\nc2: Kubo alcanzó una facturación anual de US$ 8 millones en 2025.\nc3: Kubo fue fundada en 2019.\nc4: Kubo participó del programa Endeavor Chile en marzo de 2026.\nc5: Kubo procesa unos US$ 40 millones mensuales en transacciones.\nc6: Kubo abrirá operación en México en el primer trimestre de 2027.\nc7: Kubo contratará 60 personas durante el próximo año.\nc8: Marta Riquelme es la CEO de Kubo.\nc9: Kubo prepara su desembarco en Colombia para 2027.\nc10: Kaszek confirmó públicamente la inversión el 14 de agosto de 2026.\nc11: Kubo había levantado una ronda semilla de US$ 5 millones en 2023.\nc12: Amador Ventures participó de la ronda."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO",
                "c2": "NO_RESPALDADO",
                "c3": "CONTRADICE",
                "c4": "RESPALDADO_RESEARCH",
                "c5": "RESPALDADO",
                "c6": "RESPALDADO",
                "c7": "NO_RESPALDADO",
                "c8": "RESPALDADO",
                "c9": "NO_RESPALDADO",
                "c10": "RESPALDADO_RESEARCH",
                "c11": "CONTRADICE",
                "c12": "RESPALDADO"
            }
        }
    },
    {
        "name": "lote_15_claims",
        "description": "Devolver 15 veredicto(s) bien formados desde el prompt REAL del gate de producción (4.218 caracteres de reglas, tres bloques de evidencia). El fallo aparece pasados ~9 claims: con menos, cualquier modelo lo resuelve.",
        "messages": [
            {
                "role": "system",
                "content": "Eres un verificador de hechos riguroso. Recibes tres cosas: (1) el CONTENIDO FUENTE original de una URL, (2) opcionalmente un RESEARCH ADICIONAL que el redactor obtuvo via Perplexity, y (3) una lista de claims extraidos de un articulo derivado. Verifica cada claim contra AMBAS evidencias: la fuente original y el research.\n\nResponde SOLO con JSON valido, sin markdown:\n{\"veredictos\": [{\"id\": \"c1\", \"veredicto\": \"RESPALDADO|RESPALDADO_RESEARCH|NO_RESPALDADO|CONTRADICE\", \"razon\": \"breve explicacion\"}]}\n\nREGLA DE PRECEDENCIA (la MAS importante, aplicala PRIMERO a cada claim):\n- La FUENTE ORIGINAL manda. Si el dato del claim aparece en la fuente original, el veredicto es RESPALDADO, SIN IMPORTAR lo que diga o deje de decir el research. El research NUNCA degrada un claim que ya esta en la fuente.\n- AUSENCIA NO ES CONTRADICCION. Que el research \"no encuentre informacion\", \"no confirme\", \"no tenga datos\", \"no mencione\" o diga \"no se encontro\" sobre un hecho es SILENCIO, no una contradiccion. El silencio del research jamas convierte un claim en NO_RESPALDADO ni en CONTRADICE cuando el claim SI esta en la fuente: en ese caso sigue siendo RESPALDADO.\n- El research solo puede: (a) AGREGAR respaldo a un claim que NO estaba en la fuente (RESPALDADO_RESEARCH), o (b) producir CONTRADICE unicamente si AFIRMA de forma explicita lo contrario (ver definicion). Nunca degrada por ausencia.\n\nDefiniciones de veredicto:\n- RESPALDADO = el dato del claim aparece en la FUENTE ORIGINAL (aunque el research no lo mencione o diga que no encontro informacion).\n- RESPALDADO_RESEARCH = el dato NO esta en la fuente, pero SI aparece de forma explicita y concreta en el RESEARCH ADICIONAL (el dato exacto: la cifra, la entidad o la fecha; no una mencion vaga ni un tema apenas relacionado). El enriquecimiento con research es LEGITIMO y buscado: NO penalices un claim por no estar en la fuente si el research lo respalda de forma explicita.\n- NO_RESPALDADO = el claim no aparece ni en la fuente ni en el research. Un claim que SI esta en la fuente NUNCA es NO_RESPALDADO.\n- CONTRADICE = la fuente o el research AFIRMAN de forma directa y explicita lo OPUESTO al claim: dan el dato contrario, o declaran expresamente que el hecho es falso, ficticio, un bulo desmentido, o un escenario especulativo/hipotetico presentado como real. Usalo SOLO ante una afirmacion contraria explicita. NUNCA por ausencia, silencio, \"no se encontro\", \"no confirmado\", \"no hay informacion\" ni falta de mencion.\n\nREGLA HECHO FICTICIO (acotada): aplica CONTRADICE por este motivo SOLO si el research (o la fuente) AFIRMA explicitamente que el hecho central es ficticio, falso, un bulo desmentido, especulativo o hipotetico presentado como real (ej: \"el evento no ocurrio\", \"se trata de un escenario hipotetico\", \"el trafico continua con normalidad\"). Si el research simplemente NO encuentra, NO confirma o NO menciona el hecho, NO es CONTRADICE: el claim se juzga por la fuente (RESPALDADO si esta ahi).\n\nREGLA DE ATRIBUCION: si la fuente contiene un titular y un cuerpo de articulo, y el titular atribuye una accion (invertir, adquirir, financiar) a una marca, pero el CUERPO del articulo especifica que la entidad real que ejecuta la accion es distinta o mas precisa (una filial, un holding, o la persona detras de la marca), tu veredicto se basa SIEMPRE en lo que dice el CUERPO, nunca en el titular. El titular NO es evidencia valida para RESPALDADO cuando contradice al cuerpo en la atribucion del sujeto de la accion; en ese caso el veredicto es CONTRADICE.\n\nREGLA FINANCIERA (aplica solo a claims que NO estan en la fuente original): un claim de inversion, adquisicion o financiamiento que involucre a un tercero nombrado (empresa o persona distinta de Cristian Tala, CAR o ecosistemastartup.com) y que NO este en la fuente solo puede ser RESPALDADO_RESEARCH si el research menciona el MISMO monto Y la MISMA entidad que el claim. Si el monto o la entidad no coinciden (coincidencia parcial, monto distinto, entidad distinta), el veredicto es NO_RESPALDADO. Si el research entrega un monto o una entidad que contradice directamente al claim, el veredicto es CONTRADICE. Si el claim SI esta en la fuente, manda la REGLA DE PRECEDENCIA (RESPALDADO)."
            },
            {
                "role": "user",
                "content": "CONTENIDO FUENTE:\nTechFinance LATAM — 14 de agosto de 2026\n\nKubo, la fintech chilena de pagos entre empresas, cerró una ronda Serie A de\nUS$ 12,5 millones liderada por Kaszek, con participación de Amador Ventures. La\ncompañía, fundada en 2021 por Marta Riquelme y Diego Sotomayor, procesa hoy unos\nUS$ 40 millones mensuales en transacciones.\n\n\"Vamos a duplicar el equipo de 60 personas durante el próximo año y abrir\noperación en México en el primer trimestre de 2027\", dijo Riquelme, CEO de Kubo.\n\nLa empresa había levantado una semilla de US$ 3 millones en 2023. No entregó\ncifras de facturación ni de rentabilidad.\n\nRESEARCH ADICIONAL:\nBúsqueda adicional (Perplexity, 14-ago-2026):\n- Kaszek confirmó en su blog la inversión en Kubo el 14 de agosto de 2026.\n- Kubo fue seleccionada en el programa Endeavor Chile en marzo de 2026.\n- No se encontró información sobre la facturación anual de Kubo.\n- No se encontró información sobre planes de Kubo en Colombia.\n- Amador Ventures reporta un ticket promedio de US$ 1,5 millones por operación.\n\nCLAIMS A VERIFICAR (15):\nc1: Kubo cerró una Serie A de US$ 12,5 millones liderada por Kaszek.\nc2: Kubo alcanzó una facturación anual de US$ 8 millones en 2025.\nc3: Kubo fue fundada en 2019.\nc4: Kubo participó del programa Endeavor Chile en marzo de 2026.\nc5: Kubo procesa unos US$ 40 millones mensuales en transacciones.\nc6: Kubo abrirá operación en México en el primer trimestre de 2027.\nc7: Kubo contratará 60 personas durante el próximo año.\nc8: Marta Riquelme es la CEO de Kubo.\nc9: Kubo prepara su desembarco en Colombia para 2027.\nc10: Kaszek confirmó públicamente la inversión el 14 de agosto de 2026.\nc11: Kubo había levantado una ronda semilla de US$ 5 millones en 2023.\nc12: Amador Ventures participó de la ronda.\nc13: Kubo es rentable desde 2025.\nc14: Amador Ventures invirtió US$ 1,5 millones en Kubo.\nc15: Kubo tiene hoy un equipo de 60 personas."
            }
        ],
        "expected_answer": {
            "type": "list_completeness",
            "list_key": "veredictos",
            "id_key": "id",
            "value_key": "veredicto",
            "expected": {
                "c1": "RESPALDADO",
                "c2": "NO_RESPALDADO",
                "c3": "CONTRADICE",
                "c4": "RESPALDADO_RESEARCH",
                "c5": "RESPALDADO",
                "c6": "RESPALDADO",
                "c7": "NO_RESPALDADO",
                "c8": "RESPALDADO",
                "c9": "NO_RESPALDADO",
                "c10": "RESPALDADO_RESEARCH",
                "c11": "CONTRADICE",
                "c12": "RESPALDADO",
                "c13": "NO_RESPALDADO",
                "c14": "NO_RESPALDADO",
                "c15": "RESPALDADO"
            }
        }
    }
]
