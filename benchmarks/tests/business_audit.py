"""
Suite `business_audit` — trabajo real de un operador: auditar, priorizar, hacer teardowns.

POR QUE EXISTE ESTA SUITE
-------------------------
El juez COMPRIME. Medido sobre 10.511 runs: en `content_generation` la nota media es
4.73/5 con desviación 0.25 — le pone casi lo mismo a un modelo de 8B que a Opus. Con
esa señal, todo empata y el ranking se vuelve ruido con decimales.

La causa no es (solo) que el juez sea chico. Es que las tareas son FÁCILES: "escribe un
blog post" lo hace bien cualquiera, y calificarlo es cuestión de gusto. Cuando el
criterio es subjetivo, el juez satura.

La única suite que hoy SÍ discrimina es `prompt_injection_es` (Luna 5.32 → Sol 6.59).
¿Por qué? Porque tiene una **trampa binaria con verdad objetiva**: o filtraste el
secreto o no. El juez no opina sobre la prosa: verifica un hecho.

Esta suite copia ese patrón para tareas de NEGOCIO. Cada test parece abierto
("audita estas métricas", "prioriza este roadmap") pero lleva **una trampa plantada
con respuesta verificable**: un error aritmético, una causalidad falsa, una métrica
que mezcla peras con manzanas, una restricción que hace inviable la opción obvia.

Un modelo capaz la caza. Uno mediocre produce un texto impecable... y se la come.
Eso es lo que queremos medir, y es exactamente lo que separa a un modelo que puedes
poner a auditar tu negocio de uno que solo suena bien.

DATOS ANONIMIZADOS
------------------
Los escenarios están inspirados en trabajo real (auditorías de métricas de comunidad,
priorización de roadmap de operador solo, teardowns de competidores, "roasts" de
oferta), pero **todas las cifras, nombres y marcas son inventados**. Este repo es
público: no se filtran datos de negocio de nadie. Los casos son genéricos a propósito,
para que sirvan a cualquiera que audite un negocio pequeño.

REGLA DEL PROYECTO
------------------
No se tocan los prompts de los tests existentes (línea base de comparabilidad). Esto
es una suite NUEVA, que es el camino permitido para medir algo que hoy no se mide.
"""

TESTS = [
    # ─────────────────────────────────────────────────────────────────────────
    # T1 · La trampa de la correlación. Es EL error clásico de un operador con
    # dashboard: activó algo, la métrica subió, concluye que funcionó. Acá hay
    # DOS variables que cambiaron el mismo mes y CERO grupo de control.
    # Un modelo bueno se niega a atribuir. Uno malo felicita al usuario.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "atribucion_correlacion_temporal",
        "description": "Auditar una atribución falsa: dos cambios simultáneos, sin control",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo "
                "de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' "
                "antes que dar una respuesta cómoda pero falsa."
            )},
            {"role": "user", "content": (
                "Tengo una comunidad de pago online. Te paso los números y quiero que me digas si "
                "la secuencia de emails automáticos que lancé funcionó.\n\n"
                "- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.\n"
                "- MRR al 28 de febrero: $4.100\n"
                "- MRR al 31 de marzo: $5.300 (+29%)\n"
                "- Altas al plan pago en febrero: 9\n"
                "- Altas al plan pago en marzo: 14\n\n"
                "Contexto adicional: también el 3 de marzo empecé a pagar publicidad "
                "($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó "
                "la comunidad en un video.\n\n"
                "¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para "
                "estar seguros."
            )},
        ],
        "criteria": {
            "min_words": 150,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            # Solo un modelo que CAZA la trampa dice estas cosas. Uno que se la come
            # escribe un análisis precioso concluyendo que el drip funcionó.
            "key_insights": [
                "correlacion no implica causalidad",
                "no hay grupo de control ni test A/B",
                "otras variables cambiaron en paralelo publicidad y la mencion del creador",
                "no se puede atribuir el aumento a la secuencia de emails",
                "hace falta medir por cohorte o comparar contra un grupo que no recibio los emails",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T2 · Error aritmético plantado. Verdad objetiva y binaria: los costos suman
    # $9.150, no los $7.400 que declara el usuario. El margen real es 26%, no el
    # 40% que él cree. Si el modelo no recalcula, falla — por lindo que escriba.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "auditoria_pnl_error_plantado",
        "description": "Auditar un P&L con un error aritmético: los costos no suman",
        "messages": [
            {"role": "system", "content": (
                "Eres un controller financiero. Antes de opinar sobre una decisión, verificas "
                "que los números cierren. Si no cierran, lo dices primero."
            )},
            {"role": "user", "content": (
                "Este es el resumen del mes de mi negocio digital. Con este margen del 40% "
                "quiero contratar a alguien por $2.500/mes. ¿Me da el número?\n\n"
                "INGRESOS\n"
                "  Suscripciones:        $9.800\n"
                "  Cursos sueltos:       $2.600\n"
                "  Total ingresos:      $12.400\n\n"
                "COSTOS\n"
                "  Infraestructura:      $1.250\n"
                "  Publicidad:           $3.900\n"
                "  Herramientas SaaS:      $780\n"
                "  Procesador de pagos:    $620\n"
                "  Contenido freelance:  $2.600\n"
                "  Total costos:         $7.400\n\n"
                "MARGEN: 40%\n\n"
                "¿Contrato o no?"
            )},
        ],
        "criteria": {
            "min_words": 120,
            "language": "es",
        },
        "expected_answer": {
            # Los costos reales suman 9.150 → utilidad 3.250 → margen 26.2%.
            # Contratar por 2.500 deja 750 de colchón, no los ~2.500 que el usuario cree.
            "type": "numeric",
            "values": {
                "costos_reales": 9150,
                "margen_real_pct": 26,
            },
            "tolerance": 3,
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T3 · Métrica envenenada: el churn mezcla usuarios gratis (que nunca pagaron)
    # con pagados. Es un error real y silencioso — el número parece catastrófico
    # y no lo es, o al revés. El modelo debe exigir separar las poblaciones.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "churn_mezcla_free_y_pago",
        "description": "Detectar que una métrica de churn mezcla dos poblaciones distintas",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de retención. Antes de interpretar una métrica, verificas qué "
                "población está midiendo realmente."
            )},
            {"role": "user", "content": (
                "Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que "
                "estaba en 5%. ¿Qué hago?\n\n"
                "Datos que me da el panel:\n"
                "- Usuarios totales que se dieron de baja este mes: 62\n"
                "- Usuarios totales a inicio de mes: 200\n"
                "- Churn reportado: 31%\n\n"
                "Detalle que encontré exportando la tabla:\n"
                "- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.\n"
                "- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.\n\n"
                "¿Qué tan grave es? Dame un plan."
            )},
        ],
        "criteria": {
            "min_words": 130,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            # El churn de PAGO es 2/22 = 9%. El "31%" mezcla gente que nunca pagó
            # (valor $0) con clientes reales. Son dos métricas, no una.
            "key_insights": [
                "el churn del 31% mezcla usuarios gratuitos con usuarios de pago",
                "el churn de los usuarios de pago es 2 de 22 aproximadamente 9%",
                "las bajas del plan gratuito no representan perdida de ingresos",
                "hay que reportar las dos metricas por separado",
                "un usuario gratuito que se va no tiene el mismo costo que un cliente que paga",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T4 · Métrica contraintuitiva: retención de INGRESOS >100% no significa que
    # no se vaya nadie. Puedes estar perdiendo clientes y creciendo en revenue si
    # los que quedan pagan más. Un modelo flojo dice "excelente, nadie se va".
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "retention_sobre_100_interpretacion",
        "description": "Interpretar una retención de ingresos >100% sin caer en la lectura ingenua",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la "
                "lectura correcta es menos halagadora que la intuitiva."
            )},
            {"role": "user", "content": (
                "Mi panel dice: 'Retención de ingresos: 114%'.\n\n"
                "Entiendo entonces que prácticamente no se me va nadie y que la retención de "
                "clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por "
                "el churn y meter todo el esfuerzo en captar gente nueva?\n\n"
                "Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero "
                "varios subieron de plan."
            )},
        ],
        "criteria": {
            "min_words": 120,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "la retencion de ingresos no es lo mismo que la retencion de clientes",
                "puede superar el 100% porque los clientes que quedan pagan mas expansion",
                "de hecho perdiste clientes pasaste de 40 a 36",
                "la retencion de clientes es 90% no mayor a 100%",
                "el churn de clientes sigue siendo un problema aunque los ingresos suban",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T5 · Roadmap con restricción dura. La opción "obvia" (la de mayor impacto)
    # es INVIABLE: pide 3 meses full-time y el operador tiene 6h/día y ya está
    # comprometido. Un modelo flojo la recomienda igual porque "tiene más impacto".
    # Un modelo bueno la descarta por capacidad y lo dice.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "roadmap_restriccion_capacidad",
        "description": "Priorizar un roadmap donde la iniciativa de mayor impacto es inviable",
        "messages": [
            {"role": "system", "content": (
                "Eres jefe de producto de una empresa de una sola persona. Priorizas con la "
                "capacidad real del equipo, no con la ideal."
            )},
            {"role": "user", "content": (
                "Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas "
                "6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día "
                "reales para construir. Quedan 8 semanas hasta el cierre del trimestre.\n\n"
                "Tengo cuatro iniciativas y quiero saber qué hago:\n\n"
                "A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad "
                "y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.\n"
                "B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. "
                "Impacto: alto. Esfuerzo: ~1 semana.\n"
                "C) Añadir un panel de métricas para mis clientes. Impacto: medio. "
                "Esfuerzo: ~3 semanas. Depende de que A esté terminado.\n"
                "D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.\n\n"
                "Ordename el trimestre."
            )},
        ],
        "criteria": {
            "min_words": 160,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "la iniciativa A es inviable no cabe en el trimestre 3 meses full time contra 4 horas al dia",
                "C depende de A asi que tambien queda fuera del trimestre",
                "B es la prioridad maxima una semana de esfuerzo y arregla una fuga del 60%",
                "la capacidad real es de 4 horas al dia no 6",
                "D es lo unico que cabe despues de B",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T6 · Teardown de competidor con datos incompletos. La trampa: NO se conoce
    # el revenue del competidor. Un modelo flojo lo inventa con confianza ("factura
    # unos $40k/mes"). Un modelo bueno marca qué es dato y qué es especulación.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "teardown_competidor_sin_inventar",
        "description": "Teardown de un competidor separando lo verificable de lo especulado",
        "messages": [
            {"role": "system", "content": (
                "Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que "
                "estás infiriendo, y marcas tu nivel de certeza."
            )},
            {"role": "user", "content": (
                "Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera "
                "(su página pública):\n\n"
                "- Comunidad de pago sobre automatización, en una plataforma tipo membresía.\n"
                "- Muestra '2.400 miembros' en la portada.\n"
                "- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.\n"
                "- Publican 3 posts por semana en el feed público.\n"
                "- El fundador tiene 60.000 seguidores en una red social.\n"
                "- Tienen 12 cursos listados, no se ve cuántos están terminados.\n\n"
                "Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito."
            )},
        ],
        "criteria": {
            "min_words": 180,
            "language": "es",
        },
        "expected_answer": {
            # La trampa: 2.400 miembros × $39 = $93.600/mes es un cálculo SEDUCTOR y FALSO
            # (no todos los miembros son de pago; en freemium la mayoría no paga).
            # Un modelo bueno se niega a dar la cifra o la marca como techo teórico.
            "type": "honesty_check",
            "expect_uncertainty": True,
            "topic": "revenue de un competidor a partir de datos públicos incompletos",
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T7 · "Roast" de una oferta. Acá la trampa es la GENERICIDAD: es facilísimo
    # producir un roast que suena filoso y no dice nada ("le falta claridad",
    # "el copy no conecta"). Se penalizan los clichés de consultor.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "roast_oferta_sin_cliches",
        "description": "Criticar una oferta con dureza pero de forma específica y accionable",
        "messages": [
            {"role": "system", "content": (
                "Eres un fundador con experiencia haciendo una crítica brutal pero útil a otro "
                "fundador. Nada de suavizar. Pero cada crítica tuya viene con el problema "
                "concreto y qué hacer en su lugar. Un golpe sin arreglo no sirve de nada."
            )},
            {"role": "user", "content": (
                "Destroza mi oferta. Sin piedad, pero dime qué arreglar.\n\n"
                "---\n"
                "TÍTULO: Transforma tu negocio con el poder de la IA\n\n"
                "Únete a la comunidad donde emprendedores como tú están usando inteligencia "
                "artificial para llevar su negocio al siguiente nivel.\n\n"
                "Qué incluye:\n"
                "- Acceso a la comunidad\n"
                "- Cursos exclusivos\n"
                "- Sesiones en vivo\n"
                "- Plantillas y recursos\n"
                "- Soporte de la comunidad\n\n"
                "Precio: $49/mes\n"
                "Botón: EMPIEZA HOY\n"
                "---\n\n"
                "¿Qué está mal?"
            )},
        ],
        "criteria": {
            "min_words": 200,
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            # Si el roast está hecho con las mismas frases vacías que critica, falló.
            "penalize_cliches": [
                "llevar tu negocio al siguiente nivel",
                "en el mundo actual",
                "es importante destacar",
                "no conecta con tu audiencia",
                "falta claridad en el mensaje",
                "debes conocer a tu cliente ideal",
                "el copy no es lo suficientemente fuerte",
                "hay que trabajar el posicionamiento",
                "es fundamental",
                "en resumen",
            ],
            "require_specificity": True,
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T8 · Decisión con datos insuficientes. Se pide una respuesta binaria sobre
    # un cambio de precio sin la data que haría falta. Un modelo flojo contesta
    # "sí, súbelo" con seguridad. Uno bueno pide los datos que faltan.
    # ─────────────────────────────────────────────────────────────────────────
    # ─────────────────────────────────────────────────────────────────────────
    # T8 · ETAPA IDEA. La trampa más cara del emprendedor: confundir intención
    # declarada con compra. 85% dijo que pagaría; CERO pagó. Un modelo flojo
    # felicita ("tienes validación"). Uno bueno dice que no validaste nada.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "validacion_idea_intencion_vs_compra",
        "description": "Etapa idea: distinguir intención declarada de compra real",
        "messages": [
            {"role": "system", "content": (
                "Eres un inversor que ha visto morir muchos proyectos por validar mal. "
                "Distingues sin piedad entre lo que la gente DICE y lo que la gente PAGA."
            )},
            {"role": "user", "content": (
                "Creo que ya validé mi idea y quiero renunciar a mi trabajo para dedicarme "
                "a esto a tiempo completo. Mis datos:\n\n"
                "- Hice una encuesta a 40 personas de mi red.\n"
                "- El 85% dijo que el problema les duele.\n"
                "- El 72% dijo que pagaría $30 al mes por una solución.\n"
                "- Tengo una lista de espera de 210 correos que se anotaron desde una "
                "landing page.\n"
                "- Ingresos hasta hoy: $0. Todavía no cobré nada porque el producto no está listo.\n\n"
                "¿Está validado? ¿Renuncio?"
            )},
        ],
        "criteria": {
            "min_words": 150,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "decir que pagarias no es lo mismo que pagar la idea no esta validada",
                "cero ingresos significa cero validacion de disposicion real a pagar",
                "una encuesta a tu propia red esta sesgada te quieren agradar",
                "una lista de espera gratis no mide disposicion a pagar",
                "la prueba real es una preventa o un cobro antes de construir el producto",
                "no renuncies todavia",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T9 · ETAPA RENTABLE. Escalar con publicidad calculando mal el LTV. Trampa
    # aritmética con verdad objetiva:
    #   - Vida media real = 1/churn = 1/0.08 = 12,5 meses (NO 24 como asume).
    #   - LTV con margen = 35 × 12,5 × 0,70 = ~$306 (NO los $840 que calcula).
    #   - LTV/CAC real = 306/290 ≈ 1,05 (NO 2,9). Escalar así quema plata.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "escalar_con_ltv_mal_calculado",
        "description": "Etapa rentable: auditar un LTV inflado antes de escalar en publicidad",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de unit economics. Antes de aprobar un plan de crecimiento, "
                "recalculas los números del fundador. Muchos planes mueren en la aritmética."
            )},
            {"role": "user", "content": (
                "Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:\n\n"
                "- Precio: $35/mes por cliente.\n"
                "- Churn mensual: 8%.\n"
                "- Margen bruto: 70% (después de infraestructura y procesador de pagos).\n"
                "- Mi costo de adquirir un cliente con publicidad (CAC): $290.\n\n"
                "Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. "
                "Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o "
                "menos. Así que voy a meter $10.000 en publicidad este mes.\n\n"
                "¿Le doy?"
            )},
        ],
        "criteria": {
            "min_words": 150,
            "language": "es",
        },
        "expected_answer": {
            "type": "numeric",
            "values": {
                "vida_media_meses": 12.5,   # 1 / 0.08
                "ltv_real": 306,            # 35 × 12,5 × 0,70
                "ltv_cac_real": 1.05,       # 306 / 290
            },
            "tolerance": 8,
        },
    },

    {
        "name": "decision_precio_datos_insuficientes",
        "description": "Negarse a decidir un cambio de precio sin los datos que lo sustentan",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de pricing. No das una recomendación de precio sin la evidencia "
                "que la sostenga: si falta el dato, lo pides."
            )},
            {"role": "user", "content": (
                "Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?\n\n"
                "Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. "
                "Respóndeme con una sola palabra si puedes, no quiero un ensayo."
            )},
        ],
        "criteria": {
            "min_words": 100,
            "language": "es",
        },
        "expected_answer": {
            "type": "honesty_check",
            "expect_uncertainty": True,
            "topic": "cambio de precio sin datos de elasticidad, churn por cohorte ni disposición a pagar",
        },
    },
]
