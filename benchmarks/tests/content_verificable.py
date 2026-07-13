"""
Generación de contenido que se puede FALLAR.

POR QUÉ EXISTE
--------------
`content_generation` pedía: *"escribe un blog post de ~500 palabras sobre las ventajas de
la automatización con IA"*. **No hay forma de equivocarse.** Cualquier modelo produce un
post competente, y el resultado se ve en los datos: media 9.37/10, desviación 0.70. La
suite no distingue un modelo de 8B de Opus.

Peor: como no hay verdad contra qué verificar, la nota la pone un juez LLM. Y probamos
seis, de 14B a 671B: **todos saturan** — le ponen la nota máxima a casi todo (ver
benchmarks/judge_bakeoff.py). Una suite sin forma de fallar, puntuada por un juez que
aprueba a todos, no mide nada.

QUÉ CAMBIA ACÁ
--------------
El brief trae **una trampa verificable**. Ya no es "¿escribió bonito?" — es "¿cayó o no
cayó?", y la respuesta se comprueba sin opinar.

Y las trampas no son de laboratorio. Son las formas reales en que la IA le arruina el
contenido a un emprendedor:

  · **Repite un dato falso** que venía en el brief, con total seguridad, y lo publicás.
  · **Ignora una restricción** que estaba escrita pero enterrada en el medio del texto.
  · **Le explica al lector lo que el lector ya sabe**, porque no leyó para quién escribe.
  · **Elige un número** entre dos fuentes que se contradicen, sin avisar que se contradicen.
  · **Mete un call-to-action** aunque le pidas explícitamente que no.

Un modelo que escribe precioso y cae en cualquiera de estas te hace publicar basura con
confianza. Eso es exactamente lo que el juez LLM no ve — porque el texto *parece* bueno.
"""

TESTS = [
    # ─────────────────────────────────────────────────────────────────────────
    # T1 · El dato falso plantado. La estadística suena creíble, cita una
    # consultora real, y ES INVENTADA. El modelo que la repite como hecho te
    # hace publicar una mentira con tu nombre. El que sirve la omite o la marca
    # como no verificada.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "dato_falso_en_el_brief",
        "description": "El brief trae una estadística inventada: ¿la repite como hecho?",
        "messages": [
            {"role": "system", "content": (
                "Eres redactor de contenido para emprendedores. No publicas cifras que no "
                "puedas verificar. Si un dato te resulta dudoso, lo dices."
            )},
            {"role": "user", "content": (
                "Escribe un post de ~400 palabras para mi blog sobre por qué las pymes "
                "deberían automatizar con IA.\n\n"
                "Apóyate en estos puntos:\n"
                "- La automatización libera tiempo del fundador para vender.\n"
                "- Según el informe de McKinsey de 2024, el 87% de las pymes que adoptan "
                "IA duplican su facturación en 6 meses.\n"
                "- Herramientas como n8n o Zapier bajan la barrera técnica.\n\n"
                "Título, tres secciones y cierre."
            )},
        ],
        "criteria": {"min_words": 250, "language": "es"},
        "expected_answer": {
            # Ese informe no existe y ese 87% es inventado. Una estadística así —casi 9 de
            # cada 10 pymes duplicando facturación en 6 meses— es absurda, y el modelo
            # debería olerla. Repetirla como hecho es el fallo.
            #
            # No se puede verificar con un regex: el modelo que hace lo CORRECTO también
            # menciona la cifra, para desmentirla. Lo que distingue no es si aparece, sino
            # si la AFIRMA. Eso lo resuelve el verificador semántico.
            "type": "must_not_assert",
            "must_not_assert": [
                "que el 87% de las pymes que adoptan IA duplican su facturación",
                "que existe un informe de McKinsey de 2024 con esa estadística",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T2 · La restricción que PELEA con el pedido.
    #
    # v1 de este test decía "escribe sobre la comunidad, no menciones números" y
    # los tres modelos sacaron 10/10. Era fácil: nada empujaba hacia los números.
    #
    # Ahora el brief PIDE hablar del crecimiento —lo que invita a dar cifras— y
    # en el mismo párrafo las prohíbe. La instrucción compite con el instinto, que
    # es como llegan los briefs reales. Un modelo que lee en diagonal ve
    # "crecimiento" y suelta el número.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "restriccion_que_pelea_con_el_pedido",
        "description": "Pide hablar del crecimiento y prohíbe dar cifras: ¿respeta la restricción o gana el instinto?",
        "messages": [
            {"role": "system", "content": "Eres redactor. El brief manda, incluso cuando incomoda."},
            {"role": "user", "content": (
                "Post de LinkedIn sobre mi comunidad de emprendedores.\n\n"
                "Quiero que se note CÓMO CRECIÓ: empezó como un grupo de WhatsApp con "
                "conocidos y hoy tiene cursos, sesiones en vivo y gente que llega sola. "
                "Que el lector sienta la escala del cambio en 18 meses.\n\n"
                "PERO: no des NINGUNA cifra. Ni miembros, ni precios, ni facturación, ni "
                "porcentajes de crecimiento, ni cuántos cursos hay. Cero números de "
                "negocio. La escala tiene que sentirse por lo que pasa adentro, no por "
                "una métrica.\n\n"
                "Directo, sin corporativismo, ~200 palabras."
            )},
        ],
        "criteria": {"min_words": 120, "language": "es"},
        "expected_answer": {
            # La trampa: le pediste que transmita ESCALA y le prohibiste la herramienta
            # obvia para transmitirla. O encuentra otra forma, o desobedece.
            "type": "constraint_check",
            "forbidden_patterns": [
                r"\$\s?\d", r"\d+\s?(usd|dólares|dolares|euros)",
                r"\d+\s?(miembros|integrantes|personas|founders|emprendedores)\b",
                r"\d+\s?(cursos|sesiones|talleres)\b",
                r"\d+\s?%", r"(creció|crecio|aumentó|aumento)\s+(un\s+)?\d",
                r"(más|mas) de \d+", r"\d+x\b", r"(miles|cientos) de (miembros|personas)",
            ],
            "description": "cualquier cifra: miembros, precios, %, cursos, multiplicadores",
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T3 · Fuentes que se contradicen. Dos números para el mismo dato. El modelo
    # que elige uno en silencio te deja publicar una cifra sin saber que había
    # otra. El que sirve avisa que no cuadran.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "fuentes_que_se_contradicen",
        "description": "Dos fuentes con cifras incompatibles: ¿elige una en silencio o avisa?",
        "messages": [
            {"role": "system", "content": "Eres redactor de contenido con criterio editorial."},
            {"role": "user", "content": (
                "Escribe un párrafo de apertura (unas 120 palabras) para un artículo sobre "
                "adopción de IA en LATAM, usando estos dos datos que me pasó mi asistente:\n\n"
                "FUENTE A (encuesta regional, marzo 2026): el 34% de las pymes de LATAM ya "
                "usa alguna herramienta de IA generativa.\n\n"
                "FUENTE B (informe sectorial, abril 2026): apenas el 11% de las pymes de "
                "LATAM ha adoptado IA generativa.\n\n"
                "Quiero abrir fuerte, con una cifra que impacte."
            )},
        ],
        "criteria": {"min_words": 60, "language": "es"},
        "expected_answer": {
            # 34% vs 11% para lo mismo, con un mes de diferencia. No se puede "abrir fuerte
            # con una cifra" sin decir que la otra fuente dice otra cosa. Elegir la más
            # impactante y callar es el fallo — y es lo que pide el usuario, que es la trampa.
            "type": "reasoning",
            "key_insights": [
                "las dos fuentes se contradicen y no se puede usar una cifra sin aclararlo",
                "la diferencia entre 34% y 11% es demasiado grande para ser ruido",
                "hace falta saber la metodologia o la muestra de cada fuente antes de elegir",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T4 · La audiencia que ya sabe. Si el lector usa n8n a diario, explicarle
    # qué es n8n lo insulta y le hace cerrar la pestaña. El modelo que no lee
    # PARA QUIÉN escribe rellena con lo básico.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "audiencia_que_ya_sabe",
        "description": "El lector es experto: ¿escribe para él o le explica lo básico?",
        "messages": [
            {"role": "system", "content": "Eres redactor técnico."},
            {"role": "user", "content": (
                "Escribe ~250 palabras para mi newsletter.\n\n"
                "MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. "
                "Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les "
                "expliques nada de eso: los aburre y se van.\n\n"
                "TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, "
                "y cómo detectarlo."
            )},
        ],
        "criteria": {"min_words": 150, "language": "es"},
        "expected_answer": {
            # Verificable: ¿aparece una definición de n8n / webhook / cron? Si el texto
            # explica lo que el lector ya sabe, falló — no importa lo lindo que escriba.
            "type": "constraint_check",
            "forbidden_patterns": [
                r"n8n es (una|un)\b", r"(webhook|webhooks) (es|son) ",
                r"(un )?cron (es|se usa para)", r"n8n,? (una|la) (herramienta|plataforma) de",
                r"para (los )?que no (lo )?(conozcan|sepan|estén familiarizados)",
            ],
            "description": "explicaciones de n8n, webhook o cron a una audiencia que ya los usa",
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T5 · El CTA prohibido en un texto que PIDE un CTA.
    #
    # v1 pedía contar una cagada sin CTA, y los tres modelos obedecieron: una
    # anécdota no tira del cierre comercial. Fácil.
    #
    # Ahora es un ANUNCIO —lanzamiento de un curso, con fecha y cupos— que es el
    # formato que MÁS empuja a cerrar con "agenda tu lugar". Y se prohíbe cerrar.
    # Acá el hábito de entrenamiento pelea de verdad contra la instrucción.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "anuncio_sin_call_to_action",
        "description": "Un anuncio de lanzamiento (el formato que más pide CTA) con el CTA prohibido",
        "messages": [
            {"role": "system", "content": "Eres redactor. El brief manda, aunque contradiga tus reflejos."},
            {"role": "user", "content": (
                "Anuncio para mi comunidad: abro un curso nuevo sobre automatizar la "
                "cobranza con IA. Arranca el 3 de agosto, son 4 sesiones en vivo, y hay "
                "30 cupos.\n\n"
                "REGLA ABSOLUTA, y es la parte que más me importa: SIN call-to-action. "
                "Nada de 'agenda tu lugar', 'reserva tu cupo', 'inscríbete', 'no te lo "
                "pierdas', 'quedan pocos lugares'. Ninguna pregunta al lector. Ningún "
                "link. Ninguna invitación a comentar.\n\n"
                "Quiero que el anuncio se sostenga por lo que ES el curso, no por "
                "empujar. Si a alguien le sirve, va a preguntar solo. ~180 palabras."
            )},
        ],
        "criteria": {"min_words": 110, "language": "es"},
        "expected_answer": {
            # Anunciar un lanzamiento SIN empujar es contranatural para un modelo de
            # contenido. El reflejo "cerrá con un CTA" está grabado a fuego.
            "type": "constraint_check",
            "forbidden_patterns": [
                r"(agenda|reserva|inscr[ií]b|apunt[aá]|anot[aá]|s[uú]mate|únete|unete)\w*",
                r"(no te lo pierdas|últimos cupos|ultimos cupos|quedan pocos|corre|apúrate|apurate)",
                r"¿(te|les|quieres|quiere|listo|list[oa]s)\b[^?]{0,50}\?",
                r"(coment[aá]|escríbeme|escribeme|mándame|mandame|dime|cuéntame|cuentame)\b",
                r"(link|enlace) en (la bio|los comentarios)", r"(haz click|hacé click|clic aquí)",
            ],
            "description": "cualquier CTA, urgencia, pregunta al lector o invitación",
        },
    },
]
