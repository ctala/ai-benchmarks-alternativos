"""Verificar un claim contra su fuente — la decisión que sostiene cualquier gate de datos.

POR QUÉ EXISTE ESTA SUITE (17-ago-2026)
---------------------------------------
Cualquier flujo que publique información sin humano revisando termina con la misma pieza:
un modelo que recibe una afirmación y su fuente, y decide si la fuente la respalda. Es la
decisión más barata de automatizar y la más cara de equivocar.

Y se puede equivocar en **dos direcciones opuestas**, que es lo que casi nadie mide:

    deja pasar lo inventado   → se publica un dato falso, con fuente citada
    bloquea lo que sí estaba  → se tira trabajo ya pagado, y nadie se entera

Medir una sola engaña. Un modelo que bloquea todo se ve perfecto si solo mirás
alucinaciones, y es carísimo en producción. Por eso la mitad de los casos **deben pasar**
y la otra mitad **deben bloquear**.

EL CASO QUE MÁS DUELE
---------------------
`titular_contradice_cuerpo`: el titular afirma una cosa y el cuerpo del mismo artículo
dice otra. Un verificador que se queda en el titular lo aprueba, y sale publicado un dato
falso **citando una fuente que dice lo contrario**. Es el fallo más caro precisamente
porque parece verificado.

La respuesta es objetiva: el claim está en el texto, o no está, o lo contradice. No hay
juicio editorial que discutir.
"""

SISTEMA = (
    "Sos el verificador de datos de una redacción. Recibís un CLAIM y la FUENTE de la que "
    "supuestamente sale. Tu única tarea es decidir si la fuente respalda el claim.\n\n"
    "Respondé SOLO con un JSON:\n"
    '{"veredicto": "RESPALDADO" | "NO_RESPALDADO" | "CONTRADICE", "motivo": "<una frase>"}\n\n'
    "RESPALDADO: la fuente afirma el claim, o algo equivalente.\n"
    "NO_RESPALDADO: la fuente no dice nada sobre eso.\n"
    "CONTRADICE: la fuente dice algo incompatible con el claim.\n\n"
    "No uses conocimiento propio: solo lo que está en la fuente."
)


def _caso(claim, fuente):
    return [
        {"role": "system", "content": SISTEMA},
        {"role": "user", "content": f"CLAIM:\n{claim}\n\nFUENTE:\n{fuente}"},
    ]


TESTS = [
    {
        "name": "claim_respaldado_literal",
        "description": "El dato está en la fuente, textual. Debe pasar.",
        "messages": _caso(
            "Nordvia levantó una ronda semilla de 4,2 millones de dólares.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 "
            "millones liderada por Aurora Ventures, con participación de dos fondos "
            "regionales. La compañía, fundada en 2024, opera en logística de última milla y "
            "planea abrir oficinas en Chile durante el primer trimestre de 2027."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "RESPALDADO"}},
    },
    {
        "name": "claim_respaldado_parafraseado",
        "description": (
            "El dato está pero dicho con otras palabras y otra unidad. Un verificador que "
            "exige coincidencia literal lo bloquea, y eso es exactamente el sobre-bloqueo "
            "que tira redacciones pagadas."),
        "messages": _caso(
            "Nordvia emplea a unas 50 personas.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de US$ 4,2 millones. Su equipo, que hoy suma "
            "medio centenar de empleados entre Montevideo y Buenos Aires, se duplicará "
            "durante el próximo año según su CEO."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "RESPALDADO"}},
    },
    {
        "name": "claim_ausente_en_la_fuente",
        "description": (
            "La fuente habla del tema y NO dice eso. Es la alucinación típica: plausible, "
            "del mismo rubro, y no está."),
        "messages": _caso(
            "Nordvia alcanzó la rentabilidad en 2026.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 "
            "millones liderada por Aurora Ventures. La compañía opera en logística de "
            "última milla y planea abrir oficinas en Chile."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    {
        "name": "titular_contradice_cuerpo",
        "description": (
            "EL CASO CARO Y REAL. El titular afirma una cosa y el cuerpo del mismo artículo "
            "dice otra. Un verificador que se queda en el titular aprueba una nota falsa "
            "que además cita fuente — parece verificada."),
        "messages": _caso(
            "Meridian Labs fue adquirida por Grupo Antares.",
            "MERIDIAN LABS SERÍA ADQUIRIDA POR GRUPO ANTARES\n"
            "Diario Económico — 12 de agosto de 2026\n\n"
            "Según tres fuentes cercanas a la operación, Grupo Antares habría iniciado "
            "conversaciones para adquirir Meridian Labs. Consultada por este medio, la "
            "compañía **desmintió la operación**: «no existe ningún acuerdo de compra ni "
            "negociaciones en curso», señaló su directora de comunicaciones. Grupo Antares "
            "declinó comentar."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "CONTRADICE"}},
    },
    {
        "name": "cifra_alterada",
        "description": (
            "La fuente dice 4,2 millones y el claim dice 42. Un dígito. Es el error que "
            "más rápido destruye la credibilidad de un medio."),
        "messages": _caso(
            "Nordvia levantó una ronda semilla de 42 millones de dólares.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "La startup uruguaya Nordvia anunció el cierre de una ronda semilla de US$ 4,2 "
            "millones liderada por Aurora Ventures."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "CONTRADICE"}},
    },
    {
        "name": "fuente_de_otro_tema",
        "description": (
            "La fuente es real y no tiene nada que ver con el claim. Pasa cuando el "
            "pipeline asocia mal una URL a una nota."),
        "messages": _caso(
            "Nordvia levantó una ronda semilla de 4,2 millones de dólares.",
            "TechFinance — 9 de agosto de 2026\n\n"
            "El Banco Central de Uruguay mantuvo la tasa de política monetaria en 8,5% en "
            "su reunión de agosto, en línea con lo esperado por el mercado."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
]
