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
    # NOTA DE VALIDACIÓN (17-ago-2026). La v1 tenía seis casos y **cinco daban 7/7
    # perfectos**: 95% de runs con nota máxima, dispersión 0,23 contra 0,29 del índice
    # general. Nacía saturada. Lo detectó `validate_suite.py` en 7 modelos repartidos por
    # el rango — yo la había probado en UNO, que es exactamente el error que la Regla 0.7
    # del runbook describe.
    #
    # Lo que la hacía fácil: las trampas eran de tipografía («42» contra «4,2») o de tema
    # («la fuente habla del Banco Central»). Ningún verificador serio falla ahí.
    #
    # Los casos de abajo son los que sí dividen, y son los que aparecen en producción:
    # la distancia entre lo que una fuente AFIRMA y lo que un lector INFIERE.
    {
        "name": "inferencia_aritmetica_correcta",
        "description": (
            "La fuente dice «duplicará su equipo de 50 personas». El claim dice «contratará "
            "50 personas». La cuenta da — y la fuente NO lo afirma. Un verificador que "
            "razona en vez de verificar lo aprueba."),
        "messages": _caso(
            "Nordvia contratará 50 personas durante el próximo año.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de US$ 4,2 millones. Su equipo, de 50 "
            "personas, se duplicará durante el próximo año según su CEO."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    {
        "name": "plan_no_es_hecho",
        "description": (
            "«Planea abrir oficinas» contra «abrirá oficinas». Un plan anunciado no es un "
            "hecho ocurrido, y la diferencia es toda la nota."),
        "messages": _caso(
            "Nordvia abrirá oficinas en Chile en el primer trimestre de 2027.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de US$ 4,2 millones. La compañía **planea** "
            "abrir oficinas en Chile durante el primer trimestre de 2027, aunque la "
            "decisión final depende de la evolución del mercado."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    {
        "name": "atribucion_no_es_afirmacion",
        "description": (
            "La fuente dice que el CEO afirmó algo. El claim lo presenta como hecho. Que "
            "alguien lo haya dicho es verdad; que sea cierto, no está respaldado."),
        "messages": _caso(
            "Nordvia será rentable en 2027.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "«Vamos a ser rentables en 2027», afirmó Marta Iribarne, CEO de Nordvia, "
            "durante la presentación de la ronda. La compañía no publica sus estados "
            "financieros."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    {
        "name": "cifra_de_otra_magnitud",
        "description": (
            "La fuente da el monto de la RONDA; el claim lo presenta como VALUACIÓN. Las "
            "dos cifras son 4,2 millones y significan cosas distintas."),
        "messages": _caso(
            "Nordvia alcanzó una valuación de 4,2 millones de dólares.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de US$ 4,2 millones liderada por Aurora "
            "Ventures. La compañía no reveló su valuación post-money."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "CONTRADICE"}},
    },
    {
        "name": "rango_compatible_pero_no_afirmado",
        "description": (
            "La fuente dice «más de 4 millones»; el claim dice «4,2 millones». Es "
            "compatible y NO está afirmado. El verificador tiene que distinguir «no lo "
            "contradice» de «lo respalda» — y ahí es donde se parten los modelos."),
        "messages": _caso(
            "Nordvia levantó 4,2 millones de dólares.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de más de US$ 4 millones, según fuentes "
            "cercanas a la operación. La compañía no confirmó el monto exacto."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    {
        "name": "anuncio_no_es_cierre",
        "description": (
            "«Anunció el 14 de agosto el cierre» no dice CUÁNDO cerró. El claim fija una "
            "fecha que la fuente no da."),
        "messages": _caso(
            "Nordvia cerró su ronda el 14 de agosto de 2026.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia anunció hoy que completó su ronda semilla de US$ 4,2 millones, "
            "operación que según la compañía se firmó «a comienzos del trimestre»."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "NO_RESPALDADO"}},
    },
    # Los dos que SÍ deben pasar. Sin ellos la suite premiaría al que bloquea todo, que
    # es el fallo caro del otro lado: tirar redacciones ya pagadas.
    {
        "name": "respaldado_pese_a_parafraseo",
        "description": (
            "Dicho con otras palabras y otra unidad, pero es el mismo hecho. Debe pasar: "
            "un verificador que exige literalidad tira trabajo bueno."),
        "messages": _caso(
            "Nordvia emplea a unas 50 personas.",
            "TechFinance — 14 de agosto de 2026\n\n"
            "Nordvia cerró una ronda semilla de US$ 4,2 millones. Su equipo, que hoy suma "
            "medio centenar de empleados entre Montevideo y Buenos Aires, se duplicará "
            "durante el próximo año."),
        "criteria": {"max_words": 120},
        "expected_answer": {"type": "json_valid", "required_keys": ["veredicto"],
                            "expected_values": {"veredicto": "RESPALDADO"}},
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
