"""Extraer los datos verificables de un texto — y sacarlos TODOS.

POR QUÉ EXISTE ESTA SUITE (17-ago-2026)
---------------------------------------
Antes de verificar un dato hay que haberlo extraído. Y ahí hay un fallo que **es invisible
para cualquier medición de precisión**: el modelo que saca de menos.

Un extractor que devuelve dos datos de un texto que tiene ocho, y los dos correctos, saca
100% de precisión. Y dejó el 75% del texto sin verificar — con lo cual un dato inventado
pasa el control siguiente porque **nadie lo extrajo para revisarlo**. El eslabón se ve
perfecto y el sistema falla.

Es el mismo punto ciego que este repo ya se encontró en sus propios detectores: medían lo
que faltaba, no lo que sobraba. Acá era al revés — se medía si lo extraído estaba bien, no
si estaba completo.

QUÉ MIDE
--------
Las dos mitades, siempre juntas:

    COBERTURA   ¿sacó todos los datos verificables que había?
    PRECISIÓN   ¿lo que sacó está bien, sin inventar?

Sacar de más es tan inútil como sacar de menos: manda a verificar cosas que el texto
nunca afirmó.

LAS TRAMPAS
-----------
  · cifras en formatos mezclados (US$, €, «millones», «M», «mil millones»)
  · una cifra que aparece en un EJEMPLO y no es un hecho del texto
  · una negación que un extractor descuidado invierte
  · un dato atribuido a un tercero, que es un hecho distinto de la afirmación
"""

SISTEMA = (
    "Extraé de la nota TODOS los datos verificables: cifras, fechas, nombres de empresas "
    "con su acción, y afirmaciones factuales que un verificador podría contrastar contra "
    "una fuente.\n\n"
    "Devolvé SOLO un JSON:\n"
    '{"claims": [{"texto": "<el dato, en una frase>", "tipo": "cifra|fecha|evento|cita"}]}\n\n'
    "Reglas:\n"
    "- NO extraigas opiniones, adjetivos ni proyecciones sin cifra.\n"
    "- NO inventes: si no está en el texto, no va.\n"
    "- Una cifra usada como EJEMPLO o comparación general no es un hecho de la nota.\n"
    "- Respetá las negaciones: «no cerró» no es «cerró»."
)


def _caso(nota):
    return [
        {"role": "system", "content": SISTEMA},
        {"role": "user", "content": nota},
    ]


TESTS = [
    {
        "name": "cobertura_ocho_claims",
        "description": (
            "EL CASO QUE MOTIVÓ LA SUITE. La nota tiene ocho datos verificables. Un modelo "
            "que saca dos correctos tiene precisión perfecta y deja el 75% sin verificar."),
        "messages": _caso(
            "Nordvia cerró una ronda semilla de US$ 4,2 millones el 14 de agosto de 2026, "
            "liderada por Aurora Ventures. La empresa, fundada en 2024 en Montevideo, "
            "emplea a 50 personas y opera en 3 países. Su facturación anual llegó a "
            "€ 1,8 millones en 2025. Según su CEO, Marta Iribarne, la compañía abrirá "
            "oficinas en Chile durante el primer trimestre de 2027."),
        "criteria": {"max_words": 400},
        # Los 8 datos tienen que estar. Se verifica por contenido, no por conteo: un
        # modelo podría partir uno en dos y seguir estando completo.
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": ["4,2", "14 de agosto", "Aurora Ventures", "2024",
                                   "50", "3 país", "1,8", "Iribarne"],
        },
    },
    {
        "name": "cifra_de_ejemplo_no_es_hecho",
        "description": (
            "«Como referencia, una ronda semilla promedio en la región ronda los US$ 2 "
            "millones» es contexto, no un dato de esta empresa. Extraerlo manda a "
            "verificar algo que la nota nunca afirmó."),
        "messages": _caso(
            "Nordvia cerró una ronda semilla de US$ 4,2 millones. Como referencia, una "
            "ronda semilla promedio en América Latina ronda los US$ 2 millones, según "
            "datos del sector."),
        "criteria": {"max_words": 300},
        "expected_answer": {
            "type": "must_not_assert",
            "must_not_assert": ["que Nordvia levantó 2 millones de dólares"],
        },
    },
    {
        "name": "negacion_no_se_invierte",
        "description": (
            "«No cerró la ronda» extraído como «cerró la ronda» publica lo contrario de lo "
            "que dice la fuente, y con fuente citada."),
        "messages": _caso(
            "Meridian Labs no cerró la ronda Serie A que había anunciado en junio. La "
            "compañía confirmó que las negociaciones con Aurora Ventures se suspendieron."),
        "criteria": {"max_words": 300},
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": ["no cerró"],
        },
    },
    {
        "name": "formatos_de_cifra_mezclados",
        "description": (
            "US$, €, «millones», «M» y «mil millones» en la misma nota. Un extractor que "
            "normaliza mal convierte 1,8 M€ en 1,8 dólares."),
        "messages": _caso(
            "La operación combinó US$ 4,2 millones de capital nuevo con € 1,8 M de deuda "
            "convertible. El fondo administra 2 mil millones de dólares en activos."),
        "criteria": {"max_words": 300},
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": ["4,2", "1,8", "2 mil millones"],
        },
    },
    {
        "name": "atribucion_es_parte_del_hecho",
        "description": (
            "«Según su CEO, la empresa abrirá oficinas» y «la empresa abrirá oficinas» son "
            "verificables contra cosas distintas: una es que lo dijo, la otra que pasará."),
        "messages": _caso(
            "Según su CEO, Marta Iribarne, Nordvia abrirá oficinas en Chile en 2027. La "
            "empresa cerró una ronda de US$ 4,2 millones en agosto de 2026."),
        "criteria": {"max_words": 300},
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": ["Iribarne", "4,2"],
        },
    },
]
