"""
Suite `business_strategy` — PLANIFICAR un negocio, no auditarlo.

LA DIFERENCIA CON `business_audit`
---------------------------------
Auditar es VERIFICAR: hay una respuesta correcta escondida (un costo que no suma,
una causalidad falsa) y el modelo la encuentra o no. Es fácil de puntuar.

Planificar es GENERAR: no hay una respuesta correcta, hay muchas. Y ahí el juez se
rinde — le pone 4.7/5 a cualquier plan que suene coherente. Por eso "hazme un plan
de negocio" es un test inútil tal como se suele escribir.

COMO SE MIDE UN PLAN SIN CAER EN EL GUSTO
-----------------------------------------
No se pregunta "¿es bueno?" (subjetivo, el juez satura). Se pregunta **"¿es
VÁLIDO?"**, que sí es verificable:

  1. RESTRICCIONES: si el enunciado dice que no hay presupuesto de publicidad y el
     plan arranca con publicidad, es inválido. Objetivo.
  2. ARITMÉTICA: si el objetivo es $5.000/mes y el plan, con sus PROPIOS números,
     llega a $1.200, está roto. Objetivo.
  3. ACTIVOS: proponer "monetiza tu lista de correo" a un negocio que no tiene lista
     es inventar un activo. Objetivo.
  4. FALSACIÓN: un plan que solo dice cómo CONSTRUIR y nunca cómo MATAR la idea
     barato es un deseo, no un plan. Objetivo (¿propuso el test de kill o no?).

Un modelo flojo produce un plan precioso, con fases y bullets, que viola una
restricción explícita del enunciado o cuya aritmética no llega ni cerca del objetivo.
Eso es lo que separa a un modelo con el que puedes planificar de uno que solo
suena a consultor.

ANONIMIZADO
-----------
Los escenarios están inspirados en negocios reales (un medio digital de nicho
buscando rentabilizar, una comunidad de pago, una firma de servicios que arranca)
pero **todas las cifras, nombres y marcas son inventados**. Este repo es público.

REGLA DEL PROYECTO
------------------
Suite NUEVA. No se toca ningún test existente (línea base de comparabilidad).
"""

TESTS = [
    # ─────────────────────────────────────────────────────────────────────────
    # T1 · El caso clásico del medio con tráfico y sin plata. TRES trampas:
    #   (a) La salida "obvia" (publicidad display / programática) está PROHIBIDA
    #       de forma explícita. Un modelo flojo la propone igual: es lo primero
    #       que sale al hablar de monetizar un medio.
    #   (b) NO hay lista de correo. Proponer "monetiza tu lista" es inventar un
    #       activo que el negocio no tiene.
    #   (c) La aritmética tiene que CERRAR contra el objetivo. Decir "vende un
    #       curso" sin mostrar cuántas ventas hacen falta es una idea, no un plan.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "plan_monetizar_medio_con_restricciones",
        "description": "Plan de monetización que debe respetar restricciones duras y cerrar la aritmética",
        "messages": [
            {"role": "system", "content": (
                "Eres un estratega de negocio que trabaja con fundadores solos y sin capital. "
                "Todo plan que propones respeta las restricciones que te dan y muestra la "
                "aritmética que lo sostiene. Si un plan no llega al objetivo con sus propios "
                "números, lo dices en vez de maquillarlo."
            )},
            {"role": "user", "content": (
                "Tengo un medio digital de nicho (noticias de tecnología) y necesito hacerlo "
                "rentable. Quiero un plan para llegar a **$5.000 USD/mes** en 90 días.\n\n"
                "LO QUE TENGO:\n"
                "- 300.000 visitas/mes de tráfico orgánico (SEO), creciendo.\n"
                "- El contenido lo genero de forma automatizada, así que publicar más "
                "no me cuesta tiempo.\n"
                "- Audiencia: profesionales y curiosos de tecnología, mayormente LATAM.\n"
                "- Autoridad de dominio decente, los artículos rankean.\n\n"
                "LO QUE NO TENGO:\n"
                "- **No tengo lista de correo.** Cero suscriptores hoy.\n"
                "- **No tengo presupuesto para publicidad pagada.** Cero.\n"
                "- Soy una sola persona y le puedo dedicar ~4 horas al día.\n\n"
                "RESTRICCIONES DURAS (si las rompes, el plan no me sirve):\n"
                "- **NO quiero publicidad display ni programática** (AdSense y similares). "
                "Ya lo decidí: destroza la velocidad del sitio y la experiencia, y el RPM en "
                "LATAM es miserable. No insistas con esto.\n"
                "- No puedo contratar a nadie en 90 días.\n\n"
                "Dame el plan. Y muéstrame la aritmética: cómo llegan los $5.000/mes con "
                "los números que tú mismo propongas."
            )},
        ],
        "criteria": {
            "min_words": 300,
            "required_sections": ["aritmetica", "90 dias", "captura", "riesgo"],
            "language": "es",
        },
        "expected_answer": {
            # ⚠️ BUG CORREGIDO (13-jul-2026). La primera versión metía las cosas
            # PROHIBIDAS ("publicidad display", "adsense") en penalize_cliches. Error
            # grave: penaliza que la palabra APAREZCA, no que el modelo la PROPONGA.
            #
            # Resultado real del smoke test: Claude Opus 4.8 escribió
            #   "300k visitas LATAM en display: RPM real $2–4 → $600–1.200/mes.
            #    Para llegar a $5.000 necesitarías un RPM de ~$16. Eso no existe en
            #    LATAM. Tu decisión es correcta y la aritmética la respalda."
            # ...es decir, VERIFICÓ la restricción con números en vez de obedecerla a
            # ciegas — la mejor respuesta posible — y mi test la castigó por nombrarla.
            # Penalicé a un modelo por razonar bien.
            #
            # Detectar "propuso X" vs "descartó X" con matching de strings no se puede
            # hacer sin falsos positivos. Así que el castigo queda SOLO para el relleno
            # de consultor (que es genérico se mire como se mire), y la violación de
            # restricciones la juzga el juez, que sí lee el contexto.
            "type": "creativity_check",
            "penalize_cliches": [
                "crea contenido de valor",
                "llevar tu negocio al siguiente nivel",
                "es importante destacar",
                "en el mundo actual",
                "aprovecha las redes sociales",
                "construye una comunidad",
                "define tu propuesta de valor",
                "escucha a tu audiencia",
                "hazlo escalable",
                "en resumen",
            ],
            "require_specificity": True,
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T2 · La aritmética que no cierra. Acá le doy el plan YA HECHO y le pido que
    # verifique si llega. NO llega, ni cerca:
    #   200.000 visitas × 1,5% a lista = 3.000 suscriptores
    #   3.000 × 2% de conversión = 60 compradores
    #   60 × $30 = $1.800/mes  (el objetivo era $6.000: falta 3,3× )
    # Un modelo flojo valida el plan porque "suena razonable". Uno bueno hace la
    # multiplicación y dice que falta más del triple.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "plan_aritmetica_no_cierra",
        "description": "Verificar si un plan llega al objetivo con sus propios números (no llega)",
        "messages": [
            {"role": "system", "content": (
                "Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus "
                "propios números llegan al objetivo. La mayoría de los planes mueren en la "
                "multiplicación."
            )},
            {"role": "user", "content": (
                "Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. "
                "¿Lo aprobamos y lo ejecutamos?\n\n"
                "PLAN:\n"
                "1. Tenemos 200.000 visitas al mes en el sitio.\n"
                "2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor "
                "del 1,5% (es un número conservador y realista para nuestro sector).\n"
                "3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los "
                "suscriptores compra (también conservador).\n"
                "4. Con eso llegamos cómodos a los $6.000/mes recurrentes.\n\n"
                "Los porcentajes me parecen sanos y alcanzables. ¿Le damos?"
            )},
        ],
        "criteria": {
            "min_words": 120,
            "language": "es",
        },
        "expected_answer": {
            "type": "numeric",
            "values": {
                "suscriptores": 3000,     # 200.000 × 1,5%
                "compradores": 60,        # 3.000 × 2%
                "ingreso_real": 1800,     # 60 × $30
            },
            "tolerance": 5,
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T3 · Elegir entre negocios. La opción más atractiva en el papel (A) tiene una
    # dependencia oculta: necesita un activo que el fundador NO tiene y que tarda
    # más que el plazo entero. La C, aburrida, es la única ejecutable ya.
    # Un modelo flojo elige A porque tiene el mayor mercado.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "elegir_negocio_con_dependencia_oculta",
        "description": "Elegir entre líneas de negocio cuando la más atractiva es inejecutable",
        "messages": [
            {"role": "system", "content": (
                "Eres asesor de fundadores. Eliges por lo que se puede EJECUTAR con los "
                "activos actuales, no por el tamaño del mercado en una diapositiva."
            )},
            {"role": "user", "content": (
                "Tengo que elegir en qué me enfoco los próximos 3 meses. Soy uno solo, "
                "4 horas al día, y necesito ingresos ANTES de que se me acabe el colchón "
                "(me quedan 3 meses de caja).\n\n"
                "OPCIÓN A — Vender datos vía API a empresas.\n"
                "  Mercado: enorme. Ticket: $500-2.000/mes por cliente.\n"
                "  Requisito: contratos B2B con empresas. Mi ciclo de venta B2B histórico "
                "es de 5 a 7 meses desde el primer contacto hasta el cobro.\n"
                "  Producto: habría que construirlo (~6 semanas).\n\n"
                "OPCIÓN B — Marca blanca de mi tecnología para agencias.\n"
                "  Mercado: mediano. Ticket: $300/mes.\n"
                "  Requisito: necesito 3 casos de éxito documentados para que alguien me "
                "compre. Hoy tengo 0.\n\n"
                "OPCIÓN C — Contenido patrocinado en el medio que ya opero.\n"
                "  Mercado: chico. Ticket: $400-800 por pieza.\n"
                "  Requisito: ya tengo el tráfico y la audiencia. Ya me escribieron 2 marcas "
                "preguntando precios el mes pasado (no les respondí).\n"
                "  Producto: no hay que construir nada.\n\n"
                "¿Cuál agarro? Justifica."
            )},
        ],
        "criteria": {
            "min_words": 160,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "la opcion A es inejecutable el ciclo de venta de 5 a 7 meses excede los 3 meses de caja",
                "la opcion B requiere casos de exito que hoy no existen es una dependencia bloqueante",
                "la opcion C es la unica que se puede ejecutar ya no hay que construir nada",
                "en C ya hay demanda entrante dos marcas preguntaron precios",
                "con 3 meses de caja la prioridad es ingreso rapido no el mercado mas grande",
            ],
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T4 · Falsación. Le pido el experimento más BARATO para MATAR la idea, no para
    # validarla. Un modelo flojo propone construir un MVP (semanas, plata) o hacer
    # encuestas (que ya sabemos que no miden nada). Uno bueno propone algo que se
    # hace en días y cuyo resultado NEGATIVO es concluyente.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "disenar_experimento_para_matar_la_idea",
        "description": "Diseñar el test más barato que MATE la idea, no que la valide",
        "messages": [
            {"role": "system", "content": (
                "Eres un fundador experimentado. Sabes que el objetivo de un experimento no "
                "es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas "
                "tests que pueden FALLAR de forma concluyente."
            )},
            {"role": "user", "content": (
                "Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una "
                "herramienta que les automatice los reportes a clientes.\n\n"
                "Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el "
                "experimento **más barato y más rápido** que pueda MATAR esta hipótesis.\n\n"
                "No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si "
                "estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, "
                "y cuál sería el resultado que me hace abandonar la idea."
            )},
        ],
        "criteria": {
            "min_words": 180,
            "required_sections": ["criterio", "abandonar", "costo", "dias"],
            "language": "es",
        },
        "expected_answer": {
            "type": "creativity_check",
            "penalize_cliches": [
                "construye un mvp",              # es exactamente lo que quiere evitar
                "producto minimo viable",
                "haz una encuesta",              # la intención declarada no valida nada
                "valida con tu red de contactos",
                "crea una landing page y mide el interes",  # "interés" ≠ pago
                "iterar rapidamente",
                "escuchar a tus usuarios",
                "es importante validar",
            ],
            "require_specificity": True,
        },
    },

    # ─────────────────────────────────────────────────────────────────────────
    # T5 · Rentabilizar SIN romper lo que ya funciona. Trampa: el activo (tráfico
    # SEO) es frágil. Varias monetizaciones obvias lo destruyen. Un modelo flojo
    # propone poner un muro de pago sobre el contenido que TRAE el tráfico — y con
    # eso se corta la rama en la que está sentado.
    # ─────────────────────────────────────────────────────────────────────────
    {
        "name": "monetizar_sin_matar_el_activo",
        "description": "Monetizar un activo frágil sin destruir la fuente misma del valor",
        "messages": [
            {"role": "system", "content": (
                "Eres estratega de negocios de medios. Antes de proponer una monetización, "
                "verificas qué le hace al activo que genera el valor. Muchas monetizaciones "
                "matan la gallina."
            )},
            {"role": "user", "content": (
                "Mi negocio vive del tráfico orgánico de Google: 300.000 visitas/mes. "
                "El 100% de mis ingresos futuros depende de que ese tráfico siga llegando.\n\n"
                "Estoy pensando en poner un muro de pago: que el contenido solo se vea "
                "pagando $9/mes. Con solo 600 suscriptores llego a $5.400/mes y listo.\n\n"
                "¿Lo hago? Si no, ¿qué hago en su lugar?"
            )},
        ],
        "criteria": {
            "min_words": 180,
            "language": "es",
        },
        "expected_answer": {
            "type": "reasoning",
            "key_insights": [
                "un muro de pago sobre el contenido que rankea destruye el trafico organico que lo alimenta",
                "google necesita ver el contenido para indexarlo y posicionarlo",
                "estarias cortando la fuente misma del valor la gallina de los huevos de oro",
                "monetizar la audiencia sin bloquear el contenido que atrae",
                "capturar correo o vender algo aparte en vez de cobrar por el articulo",
            ],
        },
    },
]
