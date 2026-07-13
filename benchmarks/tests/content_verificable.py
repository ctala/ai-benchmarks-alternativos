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
    # T2 · La restricción enterrada. Está escrita, clarísima, en el medio de un
    # brief largo. El modelo que lee en diagonal la pisa. Es el fallo más caro
    # en la práctica: te obliga a releer todo lo que te entrega.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "restriccion_enterrada",
        "description": "Una restricción explícita en medio del brief: ¿la respeta o lee en diagonal?",
        "messages": [
            {"role": "system", "content": "Eres redactor. Sigues el brief al pie de la letra."},
            {"role": "user", "content": (
                "Necesito un post para LinkedIn sobre mi comunidad de emprendedores.\n\n"
                "Contexto: llevo 18 meses construyéndola. Empezó como un grupo de WhatsApp "
                "y hoy es una comunidad con cursos y sesiones en vivo. La mayoría son "
                "founders en etapa temprana, muchos todavía sin facturar.\n\n"
                "IMPORTANTE: no menciones NINGÚN precio, ni cifras de facturación, ni "
                "número de miembros. Nada de números de negocio. Quiero que el post hable "
                "solo de la experiencia de la gente.\n\n"
                "Tono directo, sin corporativismo. Unas 200 palabras. Que cierre invitando "
                "a conversar en comentarios."
            )},
        ],
        "criteria": {"min_words": 120, "language": "es"},
        "expected_answer": {
            # Verificable sin opinar: ¿aparece un precio, una facturación o un conteo de
            # miembros? Si aparece, ignoró una instrucción que estaba escrita.
            "type": "constraint_check",
            "forbidden_patterns": [
                r"\$\s?\d", r"\d+\s?(usd|dólares|dolares|euros)",
                r"\d+\s?(miembros|integrantes|personas en la comunidad)",
                r"(facturación|facturacion|ingresos|mrr|revenue)\s+de\s+\$?\d",
                r"\d+\s?(mil|k)\s?(de)?\s?(mrr|ingresos|facturación)",
            ],
            "description": "precios, facturación o número de miembros",
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
    # T5 · El call-to-action reflejo. Se lo prohibís explícitamente y lo mete
    # igual, porque "cerrar con un CTA" está grabado en el entrenamiento. Mide
    # si el modelo sigue la instrucción o su propio hábito.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "sin_call_to_action",
        "description": "Se prohíbe el CTA explícitamente: ¿obedece o gana el reflejo?",
        "messages": [
            {"role": "system", "content": "Eres redactor. El brief manda."},
            {"role": "user", "content": (
                "Escribe ~180 palabras contando una cagada que me costó plata: automaticé "
                "el envío de un email a 2.000 personas sin probarlo antes, y salió con el "
                "nombre de variable sin reemplazar. 'Hola {{nombre}}' a dos mil personas.\n\n"
                "REGLA ABSOLUTA: sin call-to-action de ningún tipo. No invites a comentar, "
                "no invites a suscribirse, no preguntes '¿te pasó algo así?', no cierres con "
                "una pregunta al lector, no menciones mi comunidad ni ningún link. El texto "
                "termina y ya. Que la historia se sostenga sola."
            )},
        ],
        "criteria": {"min_words": 110, "language": "es"},
        "expected_answer": {
            # Verificable: ¿hay pregunta al lector, invitación a comentar/suscribirse/
            # sumarse? Es el hábito más arraigado de los modelos de contenido.
            "type": "constraint_check",
            "forbidden_patterns": [
                r"¿(te|les|alguna vez).{0,60}\?", r"(coment[aá]|cuéntame|cuentame|comparte)\b",
                r"(suscr[ií]b|s[uú]mate|únete|unete|agenda|reserva)\w*",
                r"(déjame|dejame) (saber|en los comentarios)",
                r"¿(y t[uú]|qué opinas|que opinas|te ha pasado)",
            ],
            "description": "cualquier call-to-action, pregunta al lector o invitación",
        },
    },
]
