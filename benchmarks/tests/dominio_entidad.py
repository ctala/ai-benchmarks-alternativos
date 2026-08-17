"""Elegir el sitio oficial de una empresa — o decir que no lo sabe.

POR QUÉ EXISTE ESTA SUITE (17-ago-2026)
---------------------------------------
Resolver a qué dominio pertenece una empresa es una de esas tareas que parecen triviales
hasta que se automatizan. El modelo recibe candidatas de una búsqueda y tiene que elegir.
Elegir mal no rompe nada: publica un dato equivocado que se ve perfectamente normal.

Los tres modos de fallo son los que aparecen una y otra vez:

  · **el subdominio de plataforma** — `<empresa>.squarespace.com` responde, tiene el logo
    y el nombre, y no es un sitio propio;
  · **el artículo de prensa** — un medio escribió sobre la empresa, así que la URL lleva su
    nombre y el texto habla de ella; tampoco es su sitio;
  · **el homónimo** — otra empresa con el mismo nombre, en otro país o rubro.

QUÉ HACE MEDIBLE A ESTA SUITE
-----------------------------
La respuesta es **binaria y verificable sin opinar**: o es el dominio oficial, o es NULL.
Ninguna de las trampas es «casi». Y hay casos donde la respuesta correcta es
**abstenerse** — que es lo que separa a un modelo útil de uno que siempre contesta algo.

Es el mismo patrón que BFCL usa para alucinación de herramientas y τ²-bench para
información incompleta: **premiar el «no sé» cuando corresponde**. Un extractor que
siempre elige el candidato más parecido acierta por suerte y falla en silencio.

Los nombres son ficticios; los patrones de trampa son los que se repiten en la práctica.
"""

SISTEMA = (
    "Recibís el nombre de una empresa y una lista de URLs candidatas encontradas en una "
    "búsqueda. Elegí cuál es su SITIO WEB OFICIAL.\n\n"
    "Respondé SOLO con un JSON:\n"
    '{"dominio": "<dominio.com>" | null, "motivo": "<una frase>"}\n\n'
    "Reglas duras:\n"
    "- Un subdominio de una plataforma de sitios (squarespace, wixsite, myshopify, "
    "webflow.io, github.io) NO es el sitio oficial de la empresa.\n"
    "- Un artículo de prensa QUE HABLA de la empresa no es su sitio.\n"
    "- Un perfil en una red social o directorio no es su sitio.\n"
    "- Si ninguno es claramente el sitio oficial, respondé null. Es preferible null a "
    "adivinar: una ficha con el dominio equivocado es peor que una sin dominio."
)


def _caso(nombre, contexto, urls):
    lista = "\n".join(f"- {u}" for u in urls)
    return [
        {"role": "system", "content": SISTEMA},
        {"role": "user", "content": f"EMPRESA: {nombre}\nCONTEXTO: {contexto}\n\nCANDIDATAS:\n{lista}"},
    ]


TESTS = [
    {
        "name": "dominio_oficial_claro",
        "description": "El sitio real está entre las candidatas. Caso base: debe elegirlo.",
        "messages": _caso(
            "Nordvia", "Startup uruguaya de logística de última milla, fundada en 2024.",
            ["https://nordvia.com",
             "https://www.linkedin.com/company/nordvia",
             "https://techfinance.example/nordvia-levanta-ronda-semilla"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": "nordvia.com"}},
    },
    {
        "name": "subdominio_de_plataforma",
        "description": (
            "EL CASO REAL. El sitio está hecho en una plataforma y vive en su subdominio. "
            "Responde, tiene el logo y el nombre — y no es un dominio propio. Un extractor "
            "que lo toma publica una ficha que envejece el día que la empresa migra."),
        "messages": _caso(
            "Vertelia", "Tienda de indumentaria sustentable, opera en Argentina.",
            ["https://vertelia.squarespace.com",
             "https://www.instagram.com/vertelia",
             "https://emprendedores.example/vertelia-el-caso-de-la-moda-circular"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": None}},
    },
    {
        "name": "solo_articulos_de_prensa",
        "description": (
            "La empresa existe y solo hay notas de medios sobre ella. La URL contiene su "
            "nombre y el artículo habla de ella: es la trampa más fácil de morder."),
        "messages": _caso(
            "Kaltrix", "Empresa de software de gestión mencionada en prensa sectorial.",
            ["https://diarioeconomico.example/kaltrix-cierra-acuerdo-con-retail",
             "https://startupnews.example/tag/kaltrix",
             "https://medium.example/@analista/por-que-kaltrix-crece"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": None}},
    },
    {
        "name": "homonimo_de_otro_rubro",
        "description": (
            "Hay un dominio con el nombre exacto — de otra empresa, en otro rubro y otro "
            "país. Elegirlo manda al lector a un sitio que no tiene nada que ver."),
        "messages": _caso(
            "Aurora Ventures", "Fondo de inversión de etapa temprana con foco en LATAM.",
            ["https://auroraventures.co.jp",
             "https://auroraventures.vc",
             "https://www.crunchbase.example/organization/aurora-ventures"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": "auroraventures.vc"}},
    },
    {
        "name": "sitio_que_anuncia_cierre",
        "description": (
            "CASO REAL. El dominio es el oficial y el sitio anuncia que la empresa cerró. "
            "Sigue siendo su dominio: la ficha es correcta, la que cambia es la nota. "
            "Un modelo que devuelve null acá pierde un dato que sí tenía."),
        "messages": _caso(
            "Trevian", "Empresa de movilidad. El contexto indica que cesó operaciones en 2026.",
            ["https://trevian.com  (el sitio muestra: «Trevian cesó operaciones el 30 de "
             "junio de 2026. Gracias a nuestros usuarios.»)",
             "https://movilidadhoy.example/trevian-cierra-tras-cuatro-anos"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": "trevian.com"}},
    },
    {
        "name": "ninguna_candidata_sirve",
        "description": (
            "Ninguna es el sitio. La respuesta correcta es abstenerse — y es el test que "
            "separa a un modelo útil de uno que siempre contesta algo."),
        "messages": _caso(
            "Belmar Systems", "Consultora tecnológica pequeña, poca presencia digital.",
            ["https://www.linkedin.com/company/belmar-systems",
             "https://directorio-empresas.example/belmar-systems",
             "https://facebook.example/belmarsystems"]),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["dominio"],
                            "expected_values": {"dominio": None}},
    },
]
