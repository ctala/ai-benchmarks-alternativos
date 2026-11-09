"""noticias_verificacion — verificar un LOTE de afirmaciones contra su fuente, una por una.

POR QUÉ EXISTE (9-nov-2026)
---------------------------
Es el registro que `suites.py` reservó el 10-oct («verificar afirmaciones contra fuente»,
alteraciones sutiles) y que nunca se construyó. Mide la decisión que sostiene cualquier
gate de datos —de un medio, de un founder que va a citar una cifra en un pitch o de un
analista que decide con una nota ajena—: ¿la fuente dice esto, no dice nada, o dice lo
contrario?

Viene de dos fallos que este repo ya pagó:

  · `verificar_claim` (UN claim por test) SATURÓ al 63 %: sus trampas eran de tipografía o
    de tema, y ningún verificador serio falla ahí.
  · `verificar_claims_lote` registra el incidente de producción: el modelo que el
    benchmark recomendó para el gate de Eco devolvió CERO veredictos en notas de 9-11
    claims. Un claim sin veredicto no bloquea nada y la nota sale publicada sin verificar.
    Por eso aquí devolver menos veredictos que afirmaciones cuenta como error en cada
    faltante.

LO QUE LA HACE DIFÍCIL
----------------------
  · fuentes de 400-500 palabras (las mismas de `noticias_extraccion`), la mitad en inglés,
    con afirmaciones en español: el caso real de un medio hispano que verifica contra
    fuentes en inglés;
  · CIFRA ALTERADA SUTIL: dígitos invertidos (544 → 454, 62 → 26, 43 → 34), magnitud
    cambiada (US$5.250 millones → US$5,25 millones; 289 millones → 289.000);
  · ATRIBUCIÓN CAMBIADA: quien participó pasa a «liderar», quien recibe pasa a «pagar»,
    «según la prensa» pasa a «Microsoft confirmó»;
  · PARÁFRASIS FIEL que DEBE pasar («1,5 mil millones» por «US$1.500 millones», traducida
    del inglés, con otro verbo) — bloquearla es tirar trabajo bueno;
  · AFIRMACIÓN AUSENTE → NO_RESPALDADO, nunca CONTRADICE (que la fuente no lo diga no es
    que diga lo contrario);
  · MURO DE PAGO: la fuente llega truncada con «…Suscríbete para seguir leyendo». Lo que
    no está en el fragmento es NO_RESPALDADO aunque sea verdad en el mundo (y en la nota
    completa): un verificador que «sabe» el dato y lo da por respaldado está usando
    conocimiento propio;
  · DATO AL FINAL: en cada caso al menos una afirmación solo se respalda con el ÚLTIMO
    párrafo de la fuente.

La mitad de los casos (15) DEBE PASAR —todas sus afirmaciones están respaldadas— y la
otra mitad (15) DEBE BLOQUEAR —al menos una no lo está—. Medir solo una dirección
engaña: un verificador que bloquea todo se ve perfecto si solo miras alucinaciones.

CÓMO SE PUNTÚA (sin juez; `benchmarks/scoring_noticias_claims.py`)
-------------------------------------------------------------------
Nota = 10 × veredictos correctos / afirmaciones enviadas. Faltante = error.
CONTRADICE ↔ NO_RESPALDADO = error (no son intercambiables: uno corrige la nota, el otro
pide más fuente). JSON que no parsea = 0. La verdad es POR CONSTRUCCIÓN: escribimos la
fuente y sabemos qué afirma.

El prompt (`PROMPT_VERIFICACION`) está separado de los casos (`CASOS`): para probar otro
prompt sobre los mismos casos, `construir_tests(otro_prompt)`.
"""

from benchmarks.tests.noticias_extraccion import FUENTES

PROMPT_VERIFICACION = (
    "Eres el verificador de datos de una redacción. Recibes una FUENTE (en español o en "
    "inglés) y una lista numerada de AFIRMACIONES que alguien quiere publicar citándola. "
    "Decide, para CADA afirmación, si la fuente la respalda.\n\n"
    "Responde SOLO con JSON válido, con un veredicto por cada afirmación y el mismo id:\n"
    '{"veredictos": [{"id": 1, "veredicto": "RESPALDADO"}]}\n\n'
    "RESPALDADO: la fuente afirma lo mismo, aunque con otras palabras, en otro idioma o con "
    "la cifra escrita en otro formato («US$1.500 millones» = «$1.5 billion»).\n"
    "NO_RESPALDADO: la fuente no dice nada sobre eso, o lo que dice no alcanza para "
    "afirmarlo. La AUSENCIA nunca es contradicción.\n"
    "CONTRADICE: la fuente afirma algo incompatible: otra cifra, otra fecha, otra entidad "
    "haciendo la acción (quién lideró, quién paga, quién confirma), o lo opuesto.\n\n"
    "Reglas:\n"
    "- Usa SOLO la fuente. No uses lo que sabes del mundo, aunque estés seguro.\n"
    "- Si la fuente está truncada (muro de pago, «Suscríbete para seguir leyendo»), lo que "
    "no aparece en el fragmento es NO_RESPALDADO, nunca CONTRADICE.\n"
    "- La atribución es parte del dato: «según Reuters» no es «la empresa confirmó».\n"
    "- Lee la fuente completa, hasta el último párrafo, antes de decidir.\n"
    "- Devuelve exactamente un veredicto por afirmación: ni menos, ni repetidos."
)

R, NR, C = "RESPALDADO", "NO_RESPALDADO", "CONTRADICE"

MURO = "\n\n…\n\nSuscríbete para seguir leyendo. Este contenido es exclusivo para suscriptores."


def texto_fuente(caso):
    """Texto completo de la fuente, o truncado tras `muro` párrafos (incluido el título)."""
    texto = FUENTES[caso["fuente"]]["texto"].strip()
    if caso.get("muro"):
        parrafos = texto.split("\n\n")
        return "\n\n".join(parrafos[:caso["muro"]]) + MURO
    return texto


# Cada afirmación: (texto, veredicto, tipo). Tipos: copia · parafrasis · dato_final ·
# cifra_alterada · dato_alterado · magnitud · atribucion · ausente · muro_pago · opuesto.
CASOS = [
    # ── DEBEN PASAR (todas RESPALDADO) ───────────────────────────────────────
    {"name": "pasa_kavak_traducida", "fuente": "kavak", "afirmaciones": [
        ("Kavak recaudó 700 millones de dólares en su Serie E.", R, "parafrasis"),
        ("La valoración de Kavak llegó a US$ 8.700 millones.", R, "parafrasis"),
        ("La ronda la encabezó General Catalyst.", R, "parafrasis"),
        ("La Serie D de Kavak, cerrada cinco meses antes, fue de US$485 millones.", R, "copia"),
        ("Kavak no reveló a qué países nuevos llegará.", R, "parafrasis"),
        ("Kavak tiene más de 5.000 empleados en América Latina.", R, "dato_final"),
    ]},
    {"name": "pasa_databricks_dato_final", "fuente": "databricks", "afirmaciones": [
        ("Databricks levanta 10.000 millones de dólares en una Serie J.", R, "parafrasis"),
        ("Thrive Capital, inversionista nuevo en la compañía, lidera la ronda.", R, "parafrasis"),
        ("La valoración de US$62.000 millones es 44% superior a la de septiembre de 2023.", R, "parafrasis"),
        ("Del total, ya se completaron US$8.600 millones.", R, "copia"),
        ("Parte del dinero dará liquidez a empleados actuales y antiguos.", R, "parafrasis"),
        ("Databricks cerró una línea de crédito de US$5.250 millones encabezada por JPMorgan Chase.", R, "dato_final"),
    ]},
    {"name": "pasa_notco_formatos", "fuente": "notco", "afirmaciones": [
        ("Tiger Global encabezó la Serie D de NotCo, de US$235 millones.", R, "parafrasis"),
        ("NotCo quedó valorada en 1,5 mil millones de dólares.", R, "parafrasis"),
        ("Roger Federer participó en la ronda de NotCo.", R, "copia"),
        ("NotCo fue fundada en 2015.", R, "copia"),
        ("NotCo acumula más de 350 millones de dólares levantados desde que se fundó.", R, "dato_final"),
    ]},
    {"name": "pasa_nubank_opi", "fuente": "nubank", "afirmaciones": [
        ("Nubank colocó 289 millones de acciones a US$9 cada una.", R, "parafrasis"),
        ("Las acciones debutaron en la Bolsa de Nueva York el 9 de diciembre de 2021 con el símbolo NU.", R, "parafrasis"),
        ("Al precio de salida, Nubank vale más que Itaú Unibanco.", R, "parafrasis"),
        ("Berkshire Hathaway era inversionista de Nubank antes de su salida a bolsa.", R, "parafrasis"),
        ("Con el rango de precio original, Nubank buscaba recaudar hasta US$3.180 millones.", R, "dato_final"),
    ]},
    {"name": "pasa_mistral_euros", "fuente": "mistral", "afirmaciones": [
        ("Mistral AI recaudó 385 millones de euros.", R, "parafrasis"),
        ("Andreessen Horowitz y Lightspeed lideraron la ronda.", R, "parafrasis"),
        ("Según Bloomberg, Mistral vale unos US$2.000 millones.", R, "parafrasis"),
        ("Eric Schmidt invirtió en Mistral.", R, "parafrasis"),
        ("Es la segunda ronda de Mistral en siete meses.", R, "parafrasis"),
        ("La ronda semilla de Mistral, de 105 millones de euros, la valoró en 240 millones de euros.", R, "dato_final"),
    ]},
    {"name": "pasa_cornershop_reguladores", "fuente": "cornershop", "afirmaciones": [
        ("Uber pagará hasta US$459 millones por una participación mayoritaria en Cornershop.", R, "copia"),
        ("El pago combina efectivo y acciones de Uber.", R, "parafrasis"),
        ("Walmart intentó comprar Cornershop antes que Uber, pero la COFECE rechazó esa operación.", R, "parafrasis"),
        ("La FNE de Chile aprobó la compra de Uber en enero de 2020.", R, "parafrasis"),
        ("A septiembre de 2020, Uber había desembolsado US$379 millones.", R, "copia"),
        ("En junio de 2021, Uber anunció que compraría el 100% de Cornershop.", R, "dato_final"),
    ]},
    {"name": "pasa_klar_deuda", "fuente": "klar", "afirmaciones": [
        ("General Atlantic lideró la Serie C de US$190 millones de Klar.", R, "parafrasis"),
        ("De los US$190 millones, US$20 millones son deuda.", R, "parafrasis"),
        ("Grupo Televisa entró como inversionista nuevo de Klar.", R, "parafrasis"),
        ("Klar busca una licencia bancaria.", R, "parafrasis"),
        ("En una ronda anterior, Klar levantó US$70 millones a una valoración de US$500 millones.", R, "dato_final"),
    ]},
    {"name": "pasa_kushki_sin_cifras", "fuente": "kushki", "afirmaciones": [
        ("Kushki es el primer unicornio de Ecuador.", R, "copia"),
        ("La Serie B completa de Kushki suma US$186 millones.", R, "copia"),
        ("El primer tramo de la Serie B se valoró en US$600 millones.", R, "parafrasis"),
        ("Kushki no dio a conocer cuánto factura.", R, "parafrasis"),
        ("Según Kushki, sus ingresos crecieron 200% en 2021.", R, "dato_final"),
    ]},
    {"name": "pasa_reddit_secundaria", "fuente": "reddit", "afirmaciones": [
        ("Reddit fijó el precio de su OPI en el tope del rango, US$34 por acción.", R, "parafrasis"),
        ("Sin contar la venta de accionistas existentes, Reddit obtuvo US$519,4 millones brutos.", R, "parafrasis"),
        ("Reddit cotizará en la Bolsa de Nueva York bajo el símbolo RDDT.", R, "parafrasis"),
        ("Steve Huffman es el director ejecutivo de Reddit.", R, "parafrasis"),
        ("Reddit reservó parte de la oferta para usuarios activos y moderadores.", R, "parafrasis"),
        ("En 2021, una ronda privada valoró a Reddit en US$10.000 millones.", R, "dato_final"),
    ]},
    {"name": "pasa_mercadolibre_pesos", "fuente": "mercadolibre_mx", "afirmaciones": [
        ("Mercado Libre invertirá 3,4 mil millones de dólares en México en 2025.", R, "parafrasis"),
        ("El anuncio lo hizo David Geisen en la conferencia matutina de Claudia Sheinbaum.", R, "parafrasis"),
        ("La empresa espera cerrar 2025 con más de 35.000 empleados en México.", R, "parafrasis"),
        ("La inversión supera en 38% a la de 2024.", R, "parafrasis"),
        ("Los US$3.400 millones equivalen a unos 69.952 millones de pesos.", R, "dato_final"),
    ]},
    {"name": "pasa_fintual_utilidades", "fuente": "fintual", "afirmaciones": [
        ("Sequoia Capital lideró la Serie B de Fintual, por US$39 millones.", R, "parafrasis"),
        ("Es la primera inversión de Sequoia en Chile.", R, "copia"),
        ("ALLVP y Kaszek ya eran inversionistas de Fintual desde la Serie A.", R, "parafrasis"),
        ("Los fondos irán principalmente a la operación en México.", R, "parafrasis"),
        ("Según Diario Financiero, Fintual reportó utilidades por primera vez en el primer semestre de 2024.", R, "dato_final"),
    ]},
    {"name": "pasa_amazon_anthropic_tramos", "fuente": "amazon_anthropic", "afirmaciones": [
        ("Amazon podrá invertir hasta US$4.000 millones en Anthropic.", R, "parafrasis"),
        ("El compromiso inicial de Amazon es de US$1.250 millones.", R, "parafrasis"),
        ("Ninguna de las dos empresas reveló el tamaño de la participación.", R, "parafrasis"),
        ("Anthropic entrenará sus modelos con los chips Trainium e Inferentia de AWS.", R, "parafrasis"),
        ("Anthropic seguirá ofreciendo sus modelos a través de Google Cloud.", R, "dato_final"),
    ]},
    {"name": "pasa_xai_premoney", "fuente": "xai", "afirmaciones": [
        ("xAI recaudó 6.000 millones de dólares en una Serie B.", R, "parafrasis"),
        ("Según Reuters, la valoración post-money de xAI es de US$24.000 millones.", R, "parafrasis"),
        ("Sequoia Capital y Andreessen Horowitz están entre los inversionistas.", R, "parafrasis"),
        ("Grok está disponible para los suscriptores de X.", R, "parafrasis"),
        ("Según Musk, xAI valía US$18.000 millones antes de la inversión.", R, "dato_final"),
    ]},
    {"name": "pasa_platzi_dos_montos", "fuente": "platzi", "afirmaciones": [
        ("Platzi informó una Serie B de US$62 millones.", R, "parafrasis"),
        ("Prosus habló de un monto de US$60 millones en su comunicado.", R, "parafrasis"),
        ("Prosus lideró la Serie B de Platzi.", R, "parafrasis"),
        ("Y Combinator participó en la ronda.", R, "copia"),
        ("Platzi iniciará operaciones en Brasil.", R, "dato_final"),
    ]},
    {"name": "pasa_instacart_debut", "fuente": "instacart", "afirmaciones": [
        ("Instacart recaudó US$660 millones con la venta de 22 millones de acciones.", R, "parafrasis"),
        ("Instacart comenzó a cotizar en Nasdaq el 19 de septiembre de 2023.", R, "parafrasis"),
        ("A inicios de 2021, Instacart fue valorada en US$39.000 millones.", R, "parafrasis"),
        ("Fidji Simo dirige Instacart desde 2021.", R, "parafrasis"),
        ("En sus primeros minutos en bolsa, la acción de Instacart tocó US$42,95.", R, "dato_final"),
    ]},

    # ── DEBEN BLOQUEAR (al menos una no respaldada) ──────────────────────────
    {"name": "bloquea_uala_digitos_invertidos", "fuente": "uala", "afirmaciones": [
        ("Ualá levantó US$350 millones en una Serie D.", R, "copia"),
        ("La valoración de Ualá es de US$2.450 millones.", R, "copia"),
        ("La ronda de Ualá fue liderada por Goldman Sachs.", C, "atribucion"),
        ("SoftBank y Tencent lideraron en 2019 una ronda de US$150 millones en Ualá.", R, "parafrasis"),
        ("Ualá facturó US$100 millones en 2020.", NR, "ausente"),
        ("El financiamiento total de Ualá llega a US$454 millones.", C, "cifra_alterada"),
    ]},
    {"name": "bloquea_bitso_62_vs_26", "fuente": "bitso", "afirmaciones": [
        ("Bitso levantó US$250 millones en su Serie C.", R, "parafrasis"),
        ("La valoración de Bitso es de US$2.200 millones.", R, "parafrasis"),
        ("Kaszek lideró la Serie C de Bitso.", C, "atribucion"),
        ("Bitso fue fundada en 2014.", R, "parafrasis"),
        ("Bitso obtuvo una licencia bancaria en México.", NR, "ausente"),
        ("En diciembre de 2020, Bitso cerró una Serie B de US$26 millones.", C, "cifra_alterada"),
    ]},
    {"name": "bloquea_rappi_magnitud", "fuente": "rappi", "afirmaciones": [
        ("Rappi levantó más de US$500 millones.", R, "parafrasis"),
        ("La valoración de Rappi es de US$5,25 millones.", C, "magnitud"),
        ("T. Rowe Price lideró la Serie F de Rappi.", R, "parafrasis"),
        ("SoftBank lideró la Serie F de Rappi.", C, "atribucion"),
        ("Rappi planea salir a bolsa en 2022.", NR, "ausente"),
        ("Según Crunchbase, Rappi ha levantado más de US$2.000 millones desde su fundación.", R, "dato_final"),
    ]},
    {"name": "bloquea_clip_quien_invierte", "fuente": "clip", "afirmaciones": [
        ("Clip recibió US$250 millones de SoftBank y Viking Global.", R, "parafrasis"),
        ("General Atlantic lideró la inversión de US$250 millones en Clip.", C, "atribucion"),
        ("Clip es el primer unicornio de pagos de México.", R, "copia"),
        ("Clip procesa más de US$5.000 millones al año en pagos.", NR, "ausente"),
        ("Según Bloomberg, Clip contratará a 320 personas en los próximos 18 meses.", R, "parafrasis"),
        ("Babatz dijo que Clip saldría a bolsa durante 2021.", C, "opuesto"),
    ]},
    {"name": "bloquea_wiz_muro_de_pago", "fuente": "wiz", "muro": 4, "afirmaciones": [
        ("Google comprará Wiz por US$32.000 millones en efectivo.", R, "parafrasis"),
        ("Google había ofrecido unos US$23.000 millones por Wiz el año anterior.", R, "parafrasis"),
        ("Wiz aceptó la oferta de unos US$23.000 millones del año anterior.", C, "opuesto"),
        ("Wiz se integrará a Google Cloud.", NR, "muro_pago"),
        ("Se espera que la compra se cierre en 2026.", NR, "muro_pago"),
        ("Google pagará a Wiz US$3.200 millones si el acuerdo fracasa.", NR, "muro_pago"),
    ]},
    {"name": "bloquea_betterfly_muro_de_pago", "fuente": "betterfly", "muro": 3, "afirmaciones": [
        ("Betterfly levantó US$125 millones en una Serie C.", R, "parafrasis"),
        ("Glade Brook Capital Partners lideró la ronda.", R, "copia"),
        ("QED Investors lideró la Serie C de Betterfly.", C, "atribucion"),
        ("Betterfly fue fundada en 2018 por Eduardo della Maggiora.", NR, "muro_pago"),
        ("Betterfly abrirá operaciones en México en 2022.", NR, "muro_pago"),
        ("Betterfly es el tercer unicornio de Chile.", NR, "muro_pago"),
    ]},
    {"name": "bloquea_nowports_muro_de_pago", "fuente": "nowports", "muro": 3, "afirmaciones": [
        ("Nowports cerró una Serie C de US$150 millones.", R, "copia"),
        ("La valoración de Nowports es de US$1.100 millones.", R, "parafrasis"),
        ("Tencent lideró la ronda de Nowports.", C, "atribucion"),
        ("Nowports es el primer unicornio de tecnología logística de Hispanoamérica.", R, "parafrasis"),
        ("Nowports abrirá oficinas en Brasil, México y Chile.", NR, "muro_pago"),
        ("En diciembre de 2021, Nowports cerró una Serie B de US$60 millones liderada por Tiger Global.", NR, "muro_pago"),
    ]},
    {"name": "bloquea_mercadolibre_muro_de_pago", "fuente": "mercadolibre_mx", "muro": 3, "afirmaciones": [
        ("Mercado Libre invertirá US$3.400 millones en México durante 2025.", R, "copia"),
        ("La inversión creará unos 10.000 empleos nuevos.", R, "parafrasis"),
        ("La inversión creará unos 1.000 empleos nuevos.", C, "cifra_alterada"),
        ("El anuncio lo hizo el director general de Mercado Libre en Argentina.", C, "atribucion"),
        ("Mercado Libre tiene más de 25.000 empleados en México.", NR, "muro_pago"),
        ("La inversión es 38% mayor que la de 2024.", NR, "muro_pago"),
    ]},
    {"name": "bloquea_nuvemshop_quien_lidera", "fuente": "nuvemshop", "afirmaciones": [
        ("Nuvemshop levantó US$500 millones a una valoración de US$3.100 millones.", R, "parafrasis"),
        ("Accel lideró la Serie E de Nuvemshop.", C, "atribucion"),
        ("Cinco meses antes, Nuvemshop levantó US$90 millones.", R, "parafrasis"),
        ("Nuvemshop fue fundada en Brasil en 2011.", C, "dato_alterado"),
        ("Nuvemshop factura más de US$100 millones al año.", NR, "ausente"),
        ("En los diez meses previos, Nuvemshop levantó más de US$620 millones.", R, "dato_final"),
    ]},
    {"name": "bloquea_figma_quien_paga", "fuente": "adobe_figma", "afirmaciones": [
        ("Adobe y Figma pusieron fin a su operación de US$20.000 millones.", R, "parafrasis"),
        ("La compra se había anunciado en septiembre de 2022.", R, "copia"),
        ("La CMA británica aprobó la fusión con condiciones que Adobe aceptó.", C, "opuesto"),
        ("Figma pagará a Adobe una comisión de terminación de US$1.000 millones.", C, "atribucion"),
        ("Figma planea salir a bolsa en 2024.", NR, "ausente"),
        ("Adobe pagará a Figma US$1.000 millones como comisión de terminación.", R, "dato_final"),
    ]},
    {"name": "bloquea_openai_quien_confirma", "fuente": "microsoft_openai", "afirmaciones": [
        ("Microsoft anunció en enero de 2023 una inversión plurianual en OpenAI.", R, "parafrasis"),
        ("Microsoft confirmó que la inversión es de US$10.000 millones.", C, "atribucion"),
        ("Según reportes de prensa, la inversión es de US$10.000 millones.", R, "parafrasis"),
        ("Microsoft invirtió US$1.000 millones en OpenAI en 2019.", R, "parafrasis"),
        ("ChatGPT se lanzó en noviembre de 2021.", C, "cifra_alterada"),
        ("OpenAI recibirá una participación accionaria en Microsoft.", NR, "ausente"),
        ("Microsoft construirá supercomputadoras especializadas para la investigación de OpenAI.", R, "dato_final"),
    ]},
    {"name": "bloquea_databricks_43_vs_34", "fuente": "databricks", "afirmaciones": [
        ("Databricks recauda US$10.000 millones a una valoración de US$62.000 millones.", R, "parafrasis"),
        ("GIC es uno de los colíderes de la ronda.", R, "parafrasis"),
        ("La valoración es 44% mayor que los US$34.000 millones de septiembre de 2023.", C, "cifra_alterada"),
        ("Databricks saldrá a bolsa en 2025.", NR, "ausente"),
        ("Databricks espera superar los US$3.000 millones de ingresos anualizados.", R, "parafrasis"),
        ("La línea de crédito de US$5.250 millones la lidera Goldman Sachs.", C, "atribucion"),
    ]},
    {"name": "bloquea_kavak_40_vs_400", "fuente": "kavak", "afirmaciones": [
        ("Kavak levantó US$700 millones.", R, "copia"),
        ("SoftBank lideró la Serie E de Kavak.", C, "atribucion"),
        ("Kavak fue fundada en 2016.", R, "parafrasis"),
        ("Kavak llegará a Colombia y Chile durante el próximo año.", NR, "ausente"),
        ("Kavak opera 400 centros logísticos y de reacondicionamiento.", C, "cifra_alterada"),
        ("Kavak tiene más de 5.000 empleados en América Latina.", R, "dato_final"),
    ]},
    {"name": "bloquea_nubank_mil_vs_millones", "fuente": "nubank", "afirmaciones": [
        ("Nubank recaudó unos US$2.600 millones en su OPI.", R, "parafrasis"),
        ("Nubank vendió 289.000 acciones en su OPI.", C, "magnitud"),
        ("El precio quedó en el piso del rango de US$8 a US$9.", C, "opuesto"),
        ("Cristina Junqueira es cofundadora de Nubank.", R, "parafrasis"),
        ("Nubank tiene 50 millones de clientes.", NR, "ausente"),
        ("Con el rango original, Nubank aspiraba a recaudar hasta US$3.180 millones.", R, "dato_final"),
    ]},
    {"name": "bloquea_cornershop_compra_vs_venta", "fuente": "cornershop", "afirmaciones": [
        ("Uber pagará hasta US$459 millones por el control de Cornershop.", R, "copia"),
        ("La COFECE aprobó la compra de Cornershop por parte de Walmart en 2019.", C, "opuesto"),
        ("Cornershop opera en Chile, México, Perú, Colombia y Canadá.", R, "copia"),
        ("Uber integrará Cornershop a Uber Eats en 2022.", NR, "ausente"),
        ("Quedaban unos US$80 millones pendientes de la aprobación mexicana.", R, "parafrasis"),
        ("En junio de 2021, Uber anunció que vendería su participación en Cornershop.", C, "opuesto"),
    ]},
]


def mensajes(prompt, caso):
    lista = "\n".join(f"{i}. {a[0]}" for i, a in enumerate(caso["afirmaciones"], 1))
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": (
            f"FUENTE:\n{texto_fuente(caso)}\n\n"
            f"AFIRMACIONES A VERIFICAR ({len(caso['afirmaciones'])}):\n{lista}")},
    ]


def _descripcion(caso):
    afs = caso["afirmaciones"]
    cuenta = {v: sum(1 for a in afs if a[1] == v) for v in (R, NR, C)}
    gate = "DEBE PASAR" if cuenta[NR] + cuenta[C] == 0 else "DEBE BLOQUEAR"
    trampas = sorted({a[2] for a in afs if a[2] not in ("copia", "parafrasis")})
    muro = f" Fuente truncada por muro de pago tras {caso['muro']} párrafos." if caso.get("muro") else ""
    idioma = "inglés" if FUENTES[caso["fuente"]]["idioma"] == "en" else "español"
    return (f"{gate}. Fuente en {idioma}, {len(afs)} afirmaciones "
            f"({cuenta[R]} R / {cuenta[NR]} NR / {cuenta[C]} C). Trampas: {', '.join(trampas)}.{muro}")


def construir_tests(prompt=PROMPT_VERIFICACION):
    """Los mismos casos con cualquier prompt (para comparar prompts sin tocar los datos)."""
    return [{
        "name": caso["name"],
        "description": _descripcion(caso),
        "messages": mensajes(prompt, caso),
        "expected_answer": {
            "type": "noticias_verificacion",
            "fuente_key": caso["fuente"],
            "esperados": {str(i): a[1] for i, a in enumerate(caso["afirmaciones"], 1)},
            "tipos": {str(i): a[2] for i, a in enumerate(caso["afirmaciones"], 1)},
            "gate": "PASA" if all(a[1] == R for a in caso["afirmaciones"]) else "BLOQUEA",
        },
    } for caso in CASOS]


TESTS = construir_tests()
