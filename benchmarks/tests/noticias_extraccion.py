"""noticias_extraccion — sacar TODAS las afirmaciones verificables de una fuente larga.

POR QUÉ EXISTE (9-nov-2026)
---------------------------
Antes de verificar una nota hay que haber extraído lo que afirma. Un extractor que saca 4
de 11 afirmaciones —las cuatro bien— se ve perfecto en cualquier medición de precisión, y
deja siete datos que nadie va a contrastar con la fuente. Es el eslabón que hace que un
gate de verificación «pase» notas que nunca revisó.

`extraer_claims` mide eso mismo y SATURÓ (94-97 % de respuestas perfectas, rechazada por la
Regla 0.7 del runbook): sus notas tenían 5 líneas y 3-8 datos a la vista, y su scorer
buscaba una cadena literal. Esta suite es más difícil a propósito y se agrega sin tocar
aquélla (las suites se agregan, nunca se editan):

  · fuentes de 400-900 palabras, reescritas desde noticias públicas reales (una
    `# fuente:` por caso), en español o en inglés — un pipeline de noticias en español
    recibe la mitad de sus fuentes en inglés y publica en español;
  · 8-12 afirmaciones PLANTADAS por caso, entre párrafos de conocimiento de dominio que NO
    son afirmaciones de la noticia (la regla de producción: lo que un experto da por
    sabido no se extrae);
  · al menos una afirmación ENTERRADA en el último párrafo, que es donde los extractores
    dejan de leer;
  · afirmaciones con ATRIBUCIÓN («según la empresa», «según Reuters»), que son un hecho
    distinto de la afirmación desnuda.

Sirve a cualquier founder hispanohablante que va a publicar o decidir con datos de una
nota ajena, no solo al pipeline de Ecosistema Startup.

CÓMO SE PUNTÚA (sin juez; `benchmarks/scoring_noticias_claims.py`)
-------------------------------------------------------------------
Cada afirmación plantada se reconoce por ANCLAS —una cifra normalizada («US$100M»,
«100 millones de dólares» y «$100 million» son el mismo número), una entidad, una fecha—
y no por texto literal. Nota = 8,5 × recall + 1,5 × acierto de `nucleo` (ponderado por el
recall) − 1 por cada afirmación que trae una cifra que la fuente no contiene (inventada o
calculada), con tope de 3. La verdad es POR CONSTRUCCIÓN: la fuente la escribimos
nosotros, así que sabemos exactamente qué afirma.

El prompt (`PROMPT_EXTRACCION`) está separado de los casos (`FUENTES`, `PLANTADOS`): para
probar otro prompt sobre los mismos casos basta `construir_tests(otro_prompt)`.
`noticias_verificacion` reutiliza `FUENTES`.
"""

# ── prompt común ─────────────────────────────────────────────────────────────

PROMPT_EXTRACCION = (
    "Eres el extractor de afirmaciones de una redacción que publica noticias de startups, "
    "inversión y tecnología en español. Recibes una FUENTE (en español o en inglés). Tu "
    "trabajo es sacar TODAS las afirmaciones verificables que la fuente hace sobre la "
    "noticia, para que un verificador las contraste una por una antes de publicar.\n\n"
    "Responde SOLO con JSON válido:\n"
    '{"claims": [{"texto": "<una afirmación, en español, autocontenida>", "nucleo": true}]}\n\n'
    "QUÉ ES UNA AFIRMACIÓN VERIFICABLE (sí se extrae):\n"
    "- cifras, montos, porcentajes, valoraciones, cantidades;\n"
    "- fechas de HECHOS relatados (cuándo se cerró, cotizó o aprobó algo);\n"
    "- entidades y quién hizo qué: quién lideró, quién participó, quién compró, quién aprobó;\n"
    "- atribuciones: si la fuente dice «según la empresa» o «según Reuters», la afirmación "
    "conserva la atribución («Según la empresa, …»).\n\n"
    "QUÉ NO SE EXTRAE:\n"
    "- conocimiento de dominio (cómo funciona una Serie B, qué es un marketplace), opiniones "
    "y adjetivos sin dato;\n"
    "- la fecha de publicación de la propia nota;\n"
    "- nada que la fuente no diga: no conviertas monedas, no sumes, no restes, no calcules.\n\n"
    "nucleo=true → el hecho de la noticia misma: qué pasó, quién, cuánto, cuándo, con quién.\n"
    "nucleo=false → contexto: rondas anteriores, historia de la empresa, tamaño de mercado, "
    "comparaciones, planes y declaraciones accesorias.\n\n"
    "Cada afirmación debe nombrar a la entidad de la que habla (nada de «la empresa» sin "
    "nombre). Una afirmación por dato. Lee la fuente COMPLETA, hasta el último párrafo: los "
    "datos del final cuentan igual que los del principio."
)


# ── helpers de anclas ────────────────────────────────────────────────────────

_MES_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
           "septiembre", "octubre", "noviembre", "diciembre"]
_MES_EN = ["january", "february", "march", "april", "may", "june", "july", "august",
           "september", "october", "november", "december"]


def N(valor):
    """Ancla numérica: alguna cifra del claim ≈ valor (tolerancia 0,5 %)."""
    return {"num": valor}


def T(*alternativas):
    """Ancla de texto: alguna alternativa aparece (sin acentos ni mayúsculas)."""
    return {"txt": list(alternativas)}


def MES(mes, anio):
    """Mes y año de un hecho, en español o inglés («mayo de 2022», «May 2022», «05/2022»)."""
    es, en = _MES_ES[mes - 1], _MES_EN[mes - 1]
    return T(f"{es} de {anio}", f"{es} {anio}", f"{en} {anio}", f"{en} of {anio}",
             f"{en[:3]} {anio}", f"{en[:3]}. {anio}", f"{mes:02d}/{anio}", f"{mes}/{anio}",
             f"{es} del {anio}")


def DIA(dia, mes):
    """Día y mes de un hecho («9 de diciembre», «December 9», «9/12»)."""
    es, en = _MES_ES[mes - 1], _MES_EN[mes - 1]
    return T(f"{dia} de {es}", f"{en} {dia}", f"{dia} {en}", f"{en[:3]} {dia}",
             f"{en[:3]}. {dia}", f"{es} {dia}", f"{dia}/{mes:02d}", f"{dia}/{mes}")


def NO_N(*valores):
    """El claim NO debe traer estas cifras (desambigua dos afirmaciones con la misma entidad)."""
    return {"no_num": list(valores)}


def NO_T(*alternativas):
    return {"no_txt": list(alternativas)}


def P(id_, texto, nucleo, *grupos, final=False):
    """Una afirmación plantada. `grupos`: uno o más grupos de anclas (basta uno entero)."""
    return {"id": id_, "texto": texto, "nucleo": nucleo,
            "anclas": [list(g) for g in grupos], "final": final}


# ── fuentes ──────────────────────────────────────────────────────────────────
# Reescritas a partir de HECHOS públicos (no hay texto copiado). Los párrafos de
# conocimiento de dominio son relleno deliberado: un extractor que los convierte en
# claims no pierde nota por eso, pero gasta su presupuesto en lo que no importa.

FUENTES = {}
PLANTADOS = {}

# fuente: https://techcrunch.com/2021/09/22/kavak-raises-700m-at-an-8-7b-valuation/ · https://latamlist.com/kavak-raises-700m-series-e-at-8-7b-valuation/
FUENTES["kavak"] = {"idioma": "en", "url": "https://latamlist.com/kavak-raises-700m-series-e-at-8-7b-valuation/", "texto": """\
Kavak doubles its valuation with a $700 million Series E

Mexico City — Kavak, the Mexican marketplace for buying and selling pre-owned cars, has raised $700 million in a Series E round that values the company at $8.7 billion, roughly twice what investors were willing to pay for it earlier in the year.

The round was led by General Catalyst. Tiger Global, D1 Capital Partners, SoftBank and Founders Fund also took part, along with several funds that had backed the company in earlier rounds.

Used cars are one of the largest consumer categories in Latin America and also one of the least trusted. Buyers worry about hidden mechanical problems, sellers worry about being paid late or not at all, and financing is expensive or simply unavailable for a large part of the population. Companies in the segment try to remove that friction by inspecting each vehicle, reconditioning it in their own facilities and offering a warranty and a return window. The model is capital intensive: the marketplace usually owns the inventory for weeks, which ties up working capital and makes every additional market an expensive bet.

The new money arrives only five months after Kavak closed a $485 million Series D at a $4 billion valuation. With this round, Kavak became the most valuable private technology company in Latin America after Nubank, the Brazilian digital bank.

Kavak was founded in 2016 in Mexico by Carlos García Ottati together with a group of co-founders. The company grew first in Mexico City and later added other Mexican cities before expanding abroad. Today it operates in Mexico, Brazil and Argentina.

Investors in the sector say the attraction is less the margin on each car and more the financial products that can be attached to it: credit, insurance and maintenance plans. A buyer who finances a car through the platform stays connected to it for years, which turns a one-off transaction into a recurring relationship. That is also where the risks are, because consumer credit in the region is sensitive to interest rates and to the economic cycle.

According to the company, part of the new capital will go to expanding across Latin America, and Kavak plans to begin operating in several new markets over the next year. The company did not name the countries.

Executives also said the money would fund new reconditioning centers and technology to price vehicles automatically, a capability that becomes more valuable as the inventory grows and pricing mistakes multiply.

For buyers, the practical difference shows up after the sale. A car bought from a private seller rarely comes with any guarantee, and disputes usually end with the buyer absorbing the cost of repairs. Platforms that offer inspections, warranties and a return window are betting that customers will pay a premium for that certainty, and that the premium will cover the cost of reconditioning and holding inventory.

The company runs 40 logistics and reconditioning hubs across the three countries where it operates. Its workforce, which numbered around 300 people a few years ago, has grown to more than 5,000 employees in Latin America.
"""}
PLANTADOS["kavak"] = [
    P(1, "Kavak levantó US$700 millones en una Serie E", True, [N(700e6)]),
    P(2, "La ronda valora a Kavak en US$8.700 millones", True, [N(8.7e9)]),
    P(3, "General Catalyst lideró la ronda", True, [T("general catalyst")]),
    P(4, "Tiger Global, D1, SoftBank y Founders Fund participaron", True,
      [T("tiger global")], [T("d1 capital")], [T("founders fund")]),
    P(5, "Cinco meses antes, Kavak cerró una Serie D de US$485 millones", False, [N(485e6)]),
    P(6, "La Serie D fue a una valoración de US$4.000 millones", False, [N(4e9)]),
    P(7, "Kavak es la startup privada más valiosa de LatAm después de Nubank", False, [T("nubank")]),
    P(8, "Kavak fue fundada en 2016 en México (Carlos García Ottati)", False,
      [T("2016")], [T("garcia ottati")]),
    P(9, "Kavak opera en México, Brasil y Argentina", False, [T("brasil", "brazil"), T("argentina")]),
    P(10, "Kavak tiene 40 centros logísticos y de reacondicionamiento", False, [N(40), T("hub", "centro", "centros")]),
    P(11, "La plantilla pasó de unas 300 personas a más de 5.000 empleados", False,
      [N(5000)], final=True),
]

# fuente: https://www.businesswire.com/news/home/20210726005214/en/ · https://techcrunch.com/2021/07/26/notco-gets-its-horn-following-235m-round-to-expand-plant-based-food-products
FUENTES["notco"] = {"idioma": "es", "url": "https://www.businesswire.com/news/home/20210726005214/en/", "texto": """\
NotCo levanta US$235 millones y se convierte en unicornio

Santiago — La foodtech chilena NotCo, que desarrolla alternativas de origen vegetal a la leche, la mayonesa, los helados y la carne, cerró una ronda Serie D de US$235 millones que la valora en US$1.500 millones.

La ronda fue liderada por Tiger Global. Se sumaron como nuevos inversionistas DFJ Growth y Zoma Lab, el fondo de Kenneth Zomosa, y también participaron figuras del deporte y la música: el piloto de Fórmula 1 Lewis Hamilton, el tenista Roger Federer y el músico Questlove.

La categoría de alimentos de origen vegetal se apoya en una promesa sencilla de explicar y difícil de cumplir: reproducir el sabor, la textura y el comportamiento en la cocina de un producto animal usando solo plantas. La mayoría de las empresas del sector trabaja por prueba y error en laboratorios de alimentos, con ciclos de desarrollo que pueden durar años. La diferencia que reclaman las compañías más nuevas es usar modelos de aprendizaje automático para recorrer miles de combinaciones de ingredientes antes de llevar una receta a la cocina de pruebas.

NotCo fue fundada en 2015 en Santiago por Matías Muchnick, Karim Pichara y Pablo Zamora. Su sistema, al que llama Giuseppe, cruza la estructura molecular de los alimentos de origen animal con una base de datos de plantas para proponer recetas que imiten el producto original.

Según la compañía, los fondos se destinarán a ampliar su presencia en nuevas categorías en Norteamérica, a escalar su tecnología de inteligencia artificial y a acelerar su llegada a Europa y Asia.

En el comunicado, Scott Shleifer, socio de Tiger Global, sostuvo que NotCo ha creado productos de origen vegetal de primer nivel que están ganando participación de mercado con rapidez.

La categoría vive un momento de presión. Los fondos que entraron con fuerza a las proteínas alternativas en los últimos años empiezan a exigir crecimiento en ventas y no solo en distribución, y varias marcas del hemisferio norte han tenido que recortar personal o retirar productos de las góndolas. En ese contexto, los inversionistas miran con atención la capacidad de cada compañía de mantener el precio cerca del producto tradicional, que es lo que define si el consumidor repite la compra.

Para las startups de la región, la ronda vuelve a mostrar que los fondos globales de crecimiento están dispuestos a apostar por compañías latinoamericanas que compiten fuera de su mercado de origen. También muestra el peso que tiene la presencia en Estados Unidos a la hora de fijar una valoración.

En las góndolas, la competencia no se limita a otras startups. Las grandes empresas de alimentos y bebidas lanzaron sus propias líneas vegetales y tienen una ventaja difícil de igualar: acceso a distribución, poder de negociación con los supermercados y presupuestos de marketing muy superiores. Por eso varias foodtech optaron por asociarse con esos mismos gigantes en lugar de enfrentarlos, y licencian su tecnología o desarrollan productos en conjunto.

Con esta operación, NotCo suma más de US$350 millones levantados desde su fundación.
"""}
PLANTADOS["notco"] = [
    P(1, "NotCo cerró una Serie D de US$235 millones", True, [N(235e6)]),
    P(2, "La ronda valora a NotCo en US$1.500 millones", True, [N(1.5e9)]),
    P(3, "Tiger Global lideró la ronda", True, [T("tiger global"), T("lider", "encabez", "led")],
      [T("liderada por tiger", "led by tiger")]),
    P(4, "DFJ Growth y Zoma Lab entraron como nuevos inversionistas", True, [T("dfj")], [T("zoma")]),
    P(5, "Lewis Hamilton, Roger Federer y Questlove participaron", True,
      [T("hamilton")], [T("federer")], [T("questlove")]),
    P(6, "NotCo fue fundada en 2015 en Santiago por Muchnick, Pichara y Zamora", False,
      [T("2015")], [T("muchnick")]),
    P(7, "Según la compañía, los fondos irán a Norteamérica, IA y Europa y Asia", False,
      [T("europa", "europe"), T("asia")]),
    P(8, "Scott Shleifer, de Tiger Global, dijo que NotCo gana participación de mercado", False,
      [T("shleifer")]),
    P(9, "NotCo suma más de US$350 millones levantados", False, [N(350e6)], final=True),
]

# fuente: https://www.pbs.org/newshour/nation/google-to-buy-cybersecurity-firm-wiz-for-32-billion-the-largest-deal-in-26-year-company-history · https://siliconangle.com/?p=690099
FUENTES["wiz"] = {"idioma": "en", "url": "https://www.pbs.org/newshour/nation/google-to-buy-cybersecurity-firm-wiz-for-32-billion-the-largest-deal-in-26-year-company-history", "texto": """\
Google agrees to buy Wiz for $32 billion in its largest deal ever

Google has agreed to acquire Wiz, the New York-based cloud security company, for $32 billion in cash. The purchase is the largest in Google's 26-year history and the biggest all-cash deal the company has ever signed.

Wiz builds software that scans the infrastructure companies run on public clouds and flags misconfigurations, exposed credentials and vulnerable workloads. Its pitch is that security teams no longer need to install agents on every server: the platform connects to the cloud account and builds a map of everything that is running.

The price is well above the roughly $23 billion that Google reportedly offered for Wiz the previous year. Wiz turned down that offer and said at the time that it would pursue the initial public offering it had been planning instead.

Cloud security has become one of the most contested categories in enterprise software. As companies moved workloads to several clouds at once, the number of permissions, keys and connections to watch grew faster than the teams in charge of watching them. Large buyers increasingly prefer a single platform over a patchwork of tools, which favors the vendors that can cover the most ground and explains the premiums being paid for leaders in the category.

Once the deal closes, Wiz will join Google Cloud. Both companies said Wiz's products will keep working across the major cloud providers, including Amazon Web Services, Microsoft Azure and Oracle Cloud, and not only on Google's own platform. That commitment matters to customers, many of whom use Wiz precisely because it is not tied to any single provider.

The acquisition still needs regulatory approval, and the companies said they expect it to close in 2026. Analysts expect antitrust authorities in the United States and Europe to look closely at the deal, given Google's position in other markets and the growing concentration among large cloud security vendors.

Wiz was founded in 2020 by Assaf Rappaport, Ami Luttwak, Yinon Costica and Roy Reznik, who had previously built a security company that they sold to Microsoft. The founders lead the company from New York and Tel Aviv.

For customers, large acquisitions in security bring a familiar worry. Products that were neutral can drift toward the acquirer's own platform over time, prices can change once the buyer integrates its sales teams, and roadmaps can slow down while two organizations merge. Buyers typically negotiate longer contracts and price protections when they suspect that a vendor is about to change hands, and procurement teams watch closely for signs that support quality is slipping during the integration.

The deal also carries protection for Wiz if regulators get in the way. According to Reuters, Google agreed to pay Wiz a termination fee of $3.2 billion if the acquisition falls through.
"""}
PLANTADOS["wiz"] = [
    P(1, "Google acordó comprar Wiz por US$32.000 millones", True, [N(32e9)]),
    P(2, "El pago es en efectivo", True, [T("efectivo", "cash", "contado")]),
    P(3, "Es la mayor adquisición en la historia de Google", True,
      [T("historia", "history")]),
    P(4, "Google había ofrecido unos US$23.000 millones el año anterior", False, [N(23e9)]),
    P(5, "Wiz rechazó esa oferta para seguir con su plan de OPI", False,
      [T("ipo", "opi", "salida a bolsa", "oferta publica", "bolsa", "public offering")]),
    P(6, "Wiz se integrará a Google Cloud", True, [T("google cloud")]),
    P(7, "Los productos de Wiz seguirán funcionando en AWS, Azure y Oracle Cloud", False,
      [T("azure")], [T("oracle")]),
    P(8, "Se espera que la operación cierre en 2026", True, [T("2026")]),
    P(9, "Wiz fue fundada en 2020 por Rappaport, Luttwak, Costica y Reznik", False,
      [T("2020"), T("wiz")], [T("rappaport")]),
    P(10, "Según Reuters, Google pagará a Wiz US$3.200 millones si el acuerdo fracasa", True,
      [N(3.2e9)], final=True),
]

# fuente: https://www.forbes.com.au/news/investing/adobe-terminates-20-billion-deal-for-figma/ · https://nairametrics.com/2023/12/18/adobe-to-pay-1-billion-after-terminating-figma-startup-acquisition
FUENTES["adobe_figma"] = {"idioma": "es", "url": "https://www.forbes.com.au/news/investing/adobe-terminates-20-billion-deal-for-figma/", "texto": """\
Adobe y Figma renuncian a su fusión de US$20.000 millones

Adobe y Figma acordaron poner fin a la operación por la que Adobe iba a comprar a la plataforma de diseño colaborativo por US$20.000 millones. Las compañías anunciaron la decisión en diciembre de 2023, después de concluir que no veían un camino claro para obtener las aprobaciones de la Comisión Europea y de la Autoridad de Competencia y Mercados del Reino Unido (CMA).

La compra se había anunciado en septiembre de 2022 y desde el primer día despertó dudas entre los reguladores. Figma se había convertido en la herramienta preferida de muchos equipos de producto para diseñar interfaces en el navegador, un terreno en el que Adobe competía con sus propios productos.

Las fusiones entre una empresa dominante y un competidor emergente son las que más preocupan a las autoridades de competencia. La teoría es conocida: una compañía grande puede pagar una prima alta por un rival pequeño no por lo que vale hoy, sino para evitar que le quite clientes mañana. Para demostrarlo, los reguladores analizan documentos internos, superposición de productos y el efecto probable sobre los precios y la innovación, un proceso que puede tomar más de un año.

Durante la revisión, la CMA británica planteó que la operación solo podría seguir adelante si Adobe se desprendía de activos y de código fuente, una propuesta que Adobe rechazó. En Europa, la Comisión había abierto una investigación a fondo y luego informó que estaba al tanto de la decisión de terminar el acuerdo.

El director ejecutivo de Adobe, Shantanu Narayen, dijo que ambas compañías estaban en profundo desacuerdo con las conclusiones de los reguladores, pero que habían decidido que lo mejor era seguir adelante por separado. Dylan Field, cofundador y director ejecutivo de Figma, sostuvo que la empresa seguiría operando de forma independiente.

Para las startups, el caso deja una lección práctica sobre los acuerdos de venta: el riesgo regulatorio no es abstracto y puede tomar más de un año resolverlo, tiempo en el que el equipo vendedor trabaja con el futuro en pausa. Por eso los compradores grandes suelen aceptar cláusulas que compensan al vendedor si la operación se cae por motivos regulatorios.

El caso también mostró cómo cambió la actitud de los reguladores frente a las grandes tecnológicas. Durante años, la mayoría de las compras de startups por parte de empresas dominantes se aprobaron sin mayor revisión. Hoy, las autoridades de Europa y del Reino Unido revisan con más atención las operaciones en las que el comprador ya tiene una posición fuerte, incluso cuando la empresa comprada todavía es pequeña en ingresos, y exigen remedios que muchas veces los compradores no están dispuestos a aceptar.

Ese es justamente el punto final de esta historia. De acuerdo con los documentos presentados ante el regulador bursátil estadounidense, Adobe deberá pagar a Figma una comisión de terminación de US$1.000 millones en efectivo.
"""}
PLANTADOS["adobe_figma"] = [
    P(1, "Adobe y Figma terminaron su acuerdo de fusión", True,
      [T("figma"), T("terminaron", "terminan", "pusieron fin", "ponen fin", "poner fin", "renunci",
                     "cancelaron", "cancelan", "abandon", "terminated", "called off", "desist")]),
    P(2, "La operación era de US$20.000 millones", True, [N(20e9)]),
    P(3, "La decisión se anunció en diciembre de 2023", True, [MES(12, 2023)]),
    P(4, "No veían camino claro para la aprobación de la Comisión Europea y la CMA", True,
      [T("comision europea", "european commission", "europea"), T("cma", "reino unido", "britanic")]),
    P(5, "La compra se había anunciado en septiembre de 2022", False, [MES(9, 2022)]),
    P(6, "La CMA pidió desprenderse de activos y código fuente; Adobe lo rechazó", False,
      [T("codigo fuente", "source code", "desprend", "desinver", "activos")]),
    P(7, "Shantanu Narayen dijo que estaban en desacuerdo con los reguladores", False, [T("narayen")]),
    P(8, "Dylan Field dijo que Figma seguirá de forma independiente", False, [T("dylan field", "field")]),
    P(9, "Adobe pagará a Figma US$1.000 millones de comisión de terminación", True,
      [N(1e9)], final=True),
]

# fuente: https://techcrunch.com/2021/08/13/argentine-fintech-uala-lands-350m-at-a-2-45b-valuation/ · https://www.ua.la/prensa/uala-raises-350m-in-new-investment-round-led-by-softbank-and-tencent
FUENTES["uala"] = {"idioma": "es", "url": "https://techcrunch.com/2021/08/13/argentine-fintech-uala-lands-350m-at-a-2-45b-valuation/", "texto": """\
Ualá recauda US$350 millones en una Serie D liderada por SoftBank y Tencent

Buenos Aires — Ualá, la fintech argentina que ofrece una cuenta y una tarjeta prepaga gestionadas desde el teléfono, cerró en agosto de 2021 una ronda Serie D de US$350 millones con una valoración posterior a la inversión de US$2.450 millones.

La ronda fue codirigida por el SoftBank Latin America Fund y por afiliadas de Tencent. También participaron inversionistas que ya estaban en la compañía, entre ellos Goldman Sachs, Soros Fund Management y Ribbit Capital.

Según la empresa, se trata de la mayor ronda privada de inversión de la historia para una compañía argentina.

Las billeteras digitales crecieron en América Latina sobre una base conocida: una parte grande de la población no tiene cuenta bancaria o la usa poco, y el efectivo sigue dominando los pagos cotidianos. Una app que permite recibir dinero, pagar servicios y comprar en línea con una tarjeta asociada resuelve un problema concreto. El desafío está en ganar dinero con eso: las comisiones por transacción son bajas y el negocio rentable suele venir del crédito, que exige gestionar riesgo en economías con inflación alta y tasas que cambian rápido.

La empresa fue fundada por Pierpaolo Barbieri, que es su director ejecutivo. Ualá opera en Argentina y en México, y la compañía dijo que usará los fondos para sumar productos financieros, como inversiones, seguros y préstamos, y para fortalecer su operación mexicana.

No es la primera vez que estos inversionistas apuestan por la compañía. SoftBank y Tencent ya habían liderado una ronda de US$150 millones en 2019, que fue la primera operación conocida de SoftBank en Argentina.

En el mercado argentino, las fintech compiten con bancos tradicionales que también aceleraron sus aplicaciones y con billeteras de grandes plataformas de comercio electrónico. La ventaja de una compañía independiente suele estar en la experiencia de uso y en la velocidad para lanzar productos; su desventaja, en el costo de fondear el crédito sin una base de depósitos estable.

Analistas del sector advierten que las valoraciones de 2021 reflejan un ciclo de capital abundante y que la prueba real será sostener el crecimiento cuando ese ciclo termine.

La experiencia de otras billeteras de la región muestra que la escala no basta. Las empresas que lograron sostenerse combinaron una base grande de usuarios activos con productos de crédito bien calibrados y una estructura de costos ajustada. Las que crecieron solo con promociones vieron cómo sus clientes se iban apenas terminaban los beneficios. Por eso los inversionistas miran cada vez más la actividad mensual y el uso de los productos financieros, y menos el número total de cuentas abiertas.

Con esta operación, el financiamiento total de Ualá llega a US$544 millones.
"""}
PLANTADOS["uala"] = [
    P(1, "Ualá cerró una Serie D de US$350 millones", True, [N(350e6)]),
    P(2, "La valoración posterior es de US$2.450 millones", True, [N(2.45e9)]),
    P(3, "La ronda fue en agosto de 2021", True, [MES(8, 2021)]),
    P(4, "SoftBank Latin America Fund y Tencent codirigieron la ronda", True,
      [T("softbank"), T("tencent"), NO_N(150e6)]),
    P(5, "Goldman Sachs, Soros y Ribbit participaron", True, [T("goldman")], [T("soros")], [T("ribbit")]),
    P(6, "Según la empresa, es la mayor ronda privada de una compañía argentina", False,
      [T("mayor", "largest", "mas grande"), T("argentin")]),
    P(7, "Pierpaolo Barbieri es fundador y CEO", False, [T("barbieri")]),
    P(8, "Ualá opera en Argentina y México", False, [T("mexic"), T("opera", "presencia", "operación", "operacion")]),
    P(9, "SoftBank y Tencent lideraron una ronda de US$150 millones en 2019", False, [N(150e6)]),
    P(10, "El financiamiento total de Ualá llega a US$544 millones", False, [N(544e6)], final=True),
]

# fuente: https://www.bloomberg.com/news/articles/2023-12-11/mistral-france-s-openai-rival-closes-385-million-round · https://pulse2.com/mistral-ai-generative-ai-company-raises-e385-million/
FUENTES["mistral"] = {"idioma": "en", "url": "https://pulse2.com/mistral-ai-generative-ai-company-raises-e385-million/", "texto": """\
Mistral AI raises €385 million, its second round in seven months

Paris — Mistral AI, the French startup that builds large language models, has raised €385 million in a round led by Andreessen Horowitz and Lightspeed Venture Partners. Reuters put the amount at about $414.41 million. The round values the company at about $2 billion, according to Bloomberg.

Salesforce, the French public investment bank Bpifrance and the shipping group CMA CGM also invested, along with individual backers including former Google chief executive Eric Schmidt and the investor Elad Gil.

Building foundation models is among the most expensive activities in software. Training a competitive model requires thousands of specialized chips for weeks or months, and the cost of that compute has to be paid before a single customer signs up. For that reason, most labs raise capital at a pace that would be unusual for any other kind of startup, and investors accept losses for years in exchange for a position in what they see as a platform shift.

Mistral has taken a different route from some of its American rivals by releasing several of its models with open weights, which lets developers download and run them on their own infrastructure. The company argues that this builds trust with enterprises that do not want to send sensitive data to a third party, and that it creates a community that improves and tests the models for free.

The company was founded in Paris in 2023 by Arthur Mensch, a former researcher at Google DeepMind, and Timothée Lacroix and Guillaume Lample, who previously worked at Meta.

European governments have treated the startup as a strategic asset. Policymakers in France have argued that the continent needs its own model developers rather than depending entirely on companies in the United States, and that argument has shaped the debate over how the European Union regulates artificial intelligence.

Customers evaluating models now look beyond raw benchmark results. Price per token, latency, the ability to run a model inside their own data centers and the terms under which their data is processed all weigh on the decision. That opens room for smaller developers whose models are not the most capable on every test but are cheaper to run, easier to customize or better suited to regulated industries such as banking, health care and the public sector, where control over data is often a legal requirement rather than a preference.

This is Mistral's second funding round in seven months. Its earlier seed round, of €105 million and led by Lightspeed, was described at the time as the largest seed round in European history. That round valued the young company at €240 million.
"""}
PLANTADOS["mistral"] = [
    P(1, "Mistral AI levantó 385 millones de euros", True, [N(385e6)]),
    P(2, "Según Reuters, unos US$414 millones", False, [N(414.41e6)]),
    P(3, "La ronda valora a Mistral en unos US$2.000 millones (según Bloomberg)", True, [N(2e9)]),
    P(4, "Andreessen Horowitz y Lightspeed lideraron", True,
      [T("andreessen", "a16z")]),
    P(5, "Salesforce, Bpifrance y CMA CGM invirtieron", True, [T("salesforce")], [T("bpifrance")], [T("cma cgm")]),
    P(6, "Eric Schmidt y Elad Gil participaron", True, [T("schmidt")], [T("elad gil")]),
    P(7, "Mistral fue fundada en París en 2023 por Mensch, Lacroix y Lample", False,
      [T("2023"), T("fund")], [T("mensch")]),
    P(8, "Es su segunda ronda en siete meses", False, [T("siete meses", "seven months", "7 meses")]),
    P(9, "La semilla previa fue de 105 millones de euros, liderada por Lightspeed", False, [N(105e6)]),
    P(10, "La semilla valoró a Mistral en 240 millones de euros", False, [N(240e6)], final=True),
]

# fuente: https://techcrunch.com/2021/05/05/with-backers-like-tiger-global-latam-crypto-exchange-bitso-raises-250m-at-a-2-2b-valuation/ · https://www.theblock.co/linked/103844/tiger-global-and-coatue-back-bitso-in-250-million-series-c
FUENTES["bitso"] = {"idioma": "en", "url": "https://www.theblock.co/linked/103844/tiger-global-and-coatue-back-bitso-in-250-million-series-c", "texto": """\
Bitso becomes Latin America's first crypto unicorn with $250 million Series C

Mexico City — Bitso, the Mexican cryptocurrency exchange, has raised $250 million in a Series C round co-led by Tiger Global and Coatue that values the company at $2.2 billion. The round, announced in May 2021, makes Bitso the first cryptocurrency company in Latin America to be valued at more than $1 billion.

New investors Paradigm, BOND and Valor Capital Group joined the round. Existing backers QED Investors, Pantera Capital and Kaszek also participated.

Crypto exchanges in the region play a role that differs from their counterparts in the United States or Europe. Trading for speculation exists, but a large share of the activity comes from people who use digital assets to protect savings from inflation, to move money across borders or to receive payments from abroad. Stablecoins pegged to the dollar are especially popular because they offer the stability of the currency without the need for a bank account in the United States.

Remittances are a central part of the pitch. Mexico is one of the largest recipients of remittances in the world, and traditional transfer services charge fees that crypto rails can undercut. Bitso has partnered with companies that move money from the United States to Mexico and uses its exchange to settle those transfers.

Bitso was founded in 2014 by Pablo González, Ben Peters and Daniel Vogel. The company says it serves customers in Mexico, Argentina and Brazil and plans to keep expanding in Latin America.

Regulation remains the main uncertainty. Mexico's financial technology law, passed in 2018, set rules for virtual assets but left many questions open, and central banks across the region have been cautious about allowing traditional financial institutions to offer crypto to their customers.

For users, the main risks are well known. Prices of digital assets can swing sharply in a matter of hours, and an exchange that fails can leave customers unable to withdraw their funds. That is why regulators and investors pay close attention to how exchanges hold customer assets, whether they keep reserves that match their obligations and how they protect accounts from fraud. Exchanges that want to work with banks and payment companies usually have to submit to audits and compliance reviews that go well beyond what the law strictly requires, and those costs weigh on smaller competitors.

The new round comes only a few months after the company's previous raise. In December 2020, Bitso closed a $62 million Series B.
"""}
PLANTADOS["bitso"] = [
    P(1, "Bitso levantó US$250 millones en una Serie C", True, [N(250e6)]),
    P(2, "La valoración es de US$2.200 millones", True, [N(2.2e9)]),
    P(3, "Tiger Global y Coatue codirigieron la ronda", True, [T("coatue")]),
    P(4, "La ronda se anunció en mayo de 2021", True, [MES(5, 2021)]),
    P(5, "Primera empresa cripto de LatAm valorada en más de US$1.000 millones", False,
      [T("primer", "first"), T("unicornio", "unicorn", "1.000 millones", "mil millones", "1 billion")]),
    P(6, "Paradigm, BOND y Valor Capital Group entraron como nuevos", True,
      [T("paradigm")], [T("valor capital")]),
    P(7, "QED, Pantera y Kaszek participaron", True, [T("qed")], [T("pantera")], [T("kaszek")]),
    P(8, "Bitso fue fundada en 2014 por González, Peters y Vogel", False,
      [T("2014")], [T("vogel")], [T("ben peters")]),
    P(9, "Bitso dice atender clientes en México, Argentina y Brasil", False,
      [T("argentina"), T("brasil", "brazil")]),
    P(10, "La ley fintech de México se aprobó en 2018", False, [T("2018")]),
    P(11, "En diciembre de 2020 Bitso cerró una Serie B de US$62 millones", False, [N(62e6)], final=True),
]

# fuente: https://www.cmswire.com/the-wire/databricks-is-raising-10b-series-j-investment-at-62b-valuation/ · https://fintech.global/2024/12/20/databricks-secures-monumental-10bn-series-j-catapulting-valuation-to-62bn/
FUENTES["databricks"] = {"idioma": "en", "url": "https://www.cmswire.com/the-wire/databricks-is-raising-10b-series-j-investment-at-62b-valuation/", "texto": """\
Databricks raises $10 billion at a $62 billion valuation

San Francisco — Databricks, the data and artificial intelligence company, said it is raising $10 billion in a Series J round at a $62 billion valuation, one of the largest venture rounds ever recorded. The company described the financing as non-dilutive and said $8.6 billion had been completed so far.

The round is led by Thrive Capital, a new investor in the company. Andreessen Horowitz, DST Global, GIC, Insight Partners and WCM Investment Management are co-leads, and Ontario Teachers' Pension Plan is also taking part. New investors include ICONIQ Growth, MGX, Sands Capital and Wellington Management.

Data platforms have become the plumbing behind most corporate AI projects. Before a company can train or fine-tune a model, or even ask a chatbot questions about its own documents, it needs its data in one place, cleaned and governed so that only the right people and systems can reach it. Vendors that already store and process that data are well positioned to sell the AI tools that sit on top of it, which is why the category has attracted so much capital.

The new valuation is 44% higher than the $43 billion the company was valued at in September 2023.

Databricks said it plans to use the money to invest in new AI products, make acquisitions and significantly expand its international go-to-market operations. Part of the proceeds will provide liquidity for current and former employees, and to pay related taxes.

That last item says as much about the market as about the company. Late-stage startups are staying private for longer, and many employees hold stock that they cannot sell until there is an initial public offering. Large rounds that include a secondary component let those employees turn part of their equity into cash without the company having to go public.

Databricks has not said when it might list its shares. Executives have repeatedly said the company could go public when market conditions are right, but that it does not need to.

Competition in the category is intense. Cloud providers offer their own data warehouses and AI tools, often bundled with other services, and rival independent vendors compete on price and ease of use. Customers increasingly ask for open formats that let them move data between platforms without being locked in, which pushes vendors to compete on performance, governance and the quality of the tools built on top of the data rather than on the storage itself.

The company also gave an update on its finances. Databricks said it expects to cross a $3 billion revenue run-rate and to be free cash flow positive for the first time in the fourth quarter of its fiscal year, which ends January 31, 2025. Separately, it closed a $5.25 billion credit facility led by JPMorgan Chase.
"""}
PLANTADOS["databricks"] = [
    P(1, "Databricks levanta US$10.000 millones en una Serie J", True, [N(10e9)]),
    P(2, "A una valoración de US$62.000 millones", True, [N(62e9)]),
    P(3, "Se han completado US$8.600 millones hasta ahora", True, [N(8.6e9)]),
    P(4, "Thrive Capital lidera la ronda", True, [T("thrive")]),
    P(5, "a16z, DST, GIC, Insight y WCM son colíderes", True,
      [T("dst global")], [T("gic"), T("insight")], [T("wcm")]),
    P(6, "Nuevos: ICONIQ, MGX, Sands Capital, Wellington", True, [T("iconiq")], [T("mgx")], [T("wellington")]),
    P(7, "La valoración sube 44% frente a la anterior", False, [N(44), T("%", "por ciento", "percent")]),
    P(8, "En septiembre de 2023 estaba valorada en US$43.000 millones", False, [N(43e9)]),
    P(9, "Parte del dinero dará liquidez a empleados actuales y anteriores", False,
      [T("liquidez", "liquidity"), T("emplead", "employee")]),
    P(10, "Databricks espera superar US$3.000 millones de ingresos anualizados", False, [N(3e9)]),
    P(11, "Espera flujo de caja libre positivo en el trimestre que termina el 31 de enero de 2025", False,
      [T("flujo de caja", "free cash flow", "cash flow")]),
    P(12, "Cerró una línea de crédito de US$5.250 millones liderada por JPMorgan", False,
      [N(5.25e9)], final=True),
]

# fuente: https://latamlist.com/insurtech-betterfly-becomes-a-unicorn-latamlist/ · https://www.lavca.org/?p=22224
FUENTES["betterfly"] = {"idioma": "es", "url": "https://latamlist.com/insurtech-betterfly-becomes-a-unicorn-latamlist/", "texto": """\
Betterfly alcanza valoración de US$1.000 millones con una Serie C de US$125 millones

Santiago — Betterfly, la insurtech chilena que combina seguros de vida con una aplicación de hábitos saludables, levantó en febrero de 2022 una ronda Serie C de US$125 millones que la valora en US$1.000 millones.

La ronda fue liderada por Glade Brook Capital Partners. Entraron como nuevos inversionistas Greycroft, Lightrock y Mundi Ventures, y también participaron QED Investors, que había liderado la Serie A de la compañía, y DST Global Partners, que había encabezado la Serie B.

El modelo de Betterfly se vende principalmente a empleadores. Las empresas contratan la plataforma como beneficio para su personal, y cada trabajador acumula una moneda virtual cuando camina, medita o duerme bien. Esa moneda se convierte en cobertura de un seguro de vida que crece con el tiempo o en donaciones a causas sociales. La apuesta es que la prevención reduce el riesgo del asegurado y, con ello, el costo para la aseguradora.

Los seguros fueron durante años una de las industrias menos digitalizadas de la región. La venta depende de corredores, los productos son difíciles de comparar y la penetración de los seguros de vida en América Latina es baja frente a la de los países desarrollados. Las insurtech intentan cambiar eso con distribución digital y productos más simples, aunque la mayoría termina asociándose con aseguradoras tradicionales, que son las que asumen el riesgo.

La compañía fue fundada en 2018 por Eduardo della Maggiora, quien antes había creado otras empresas de tecnología en Chile.

Según la empresa, los fondos permitirán iniciar operaciones en siete nuevos mercados durante 2022, entre ellos México, Colombia y Argentina, y acelerar el desarrollo de su plataforma.

La industria de beneficios corporativos es competitiva. Plataformas de bienestar, gimnasios con convenios y las propias aseguradoras compiten por el mismo presupuesto de recursos humanos, y la retención de clientes depende de que los trabajadores realmente usen la aplicación.

Betterfly se presenta además como una empresa de impacto social, y varios medios la describieron como el primer unicornio social de América Latina, una etiqueta que la propia compañía promueve.

Para las aseguradoras tradicionales, las alianzas con plataformas como esta tienen un atractivo claro: llegan a clientes jóvenes que difícilmente comprarían un seguro de vida por iniciativa propia y obtienen datos sobre sus hábitos. Para la startup, el reto está en que el valor percibido por el trabajador se mantenga en el tiempo, porque la novedad de acumular puntos por caminar se desgasta rápido si la aplicación no ofrece algo más.

Con esta ronda, Betterfly se convierte en el tercer unicornio de Chile, después de Cornershop y NotCo.
"""}
PLANTADOS["betterfly"] = [
    P(1, "Betterfly levantó una Serie C de US$125 millones", True, [N(125e6)]),
    P(2, "La valoración es de US$1.000 millones", True, [N(1e9)]),
    P(3, "La ronda fue en febrero de 2022", True, [MES(2, 2022)]),
    P(4, "Glade Brook Capital Partners lideró", True, [T("glade brook")]),
    P(5, "Greycroft, Lightrock y Mundi Ventures son nuevos", True,
      [T("greycroft")], [T("lightrock")], [T("mundi")]),
    P(6, "QED (que lideró la Serie A) participó", False, [T("qed")]),
    P(7, "DST Global (que lideró la Serie B) participó", False, [T("dst")]),
    P(8, "Fundada en 2018 por Eduardo della Maggiora", False, [T("2018")], [T("della maggiora")]),
    P(9, "Según la empresa, abrirá siete mercados en 2022, incluidos México, Colombia y Argentina", False,
      [T("siete", "7 nuevos", "7 mercados", "seven"), T("mercado", "market", "pais", "paises")],
      [T("colombia"), T("mexic")]),
    P(10, "Betterfly es el tercer unicornio de Chile, tras Cornershop y NotCo", False,
      [T("tercer", "third", "3er")], [T("cornershop")], final=True),
]

# fuente: https://latamlist.com/e-commerce-platform-nuvemshop-raises-500m-series-e/ · https://www.lavca.org/?p=22023
FUENTES["nuvemshop"] = {"idioma": "en", "url": "https://latamlist.com/e-commerce-platform-nuvemshop-raises-500m-series-e/", "texto": """\
Nuvemshop raises $500 million at a $3.1 billion valuation

São Paulo — Nuvemshop, the e-commerce platform for small and medium-sized merchants that operates as Tiendanube in Spanish-speaking countries, has raised $500 million in a Series E round at a $3.1 billion valuation. The company announced the round in August 2021.

The round was co-led by Insight Partners and Tiger Global Management. Alkeon, Owl Rock, Sunley House Capital and VMG Partners also invested, and Accel, an existing shareholder, returned with a follow-on investment.

Software that lets merchants open an online store without writing code is a crowded category worldwide, dominated by a handful of large players. In Latin America, local platforms have competed by adapting to details that global providers tend to treat as afterthoughts: local payment methods, installment plans, integrations with regional logistics companies and support in Spanish and Portuguese. The pandemic accelerated the shift, as small shops that had relied entirely on physical traffic needed to sell online almost overnight.

The new funding comes just five months after Nuvemshop raised $90 million in a round led by Accel.

Nuvemshop was founded in Argentina in 2011 by Santiago Sosa, Alejandro Vázquez, Martín Palombo and Lucas Mosquera. It later moved its headquarters to São Paulo, as Brazil became its largest market.

The company said it will use the capital to develop new products for merchants, including payments and logistics tools, and to expand into other countries in the region. Those adjacent services matter for the business model: subscription fees from small merchants are modest, and platforms increasingly earn more from processing payments and shipping orders than from the store software itself.

Investors in the round pointed to the size of the opportunity. Online sales still represent a small share of total retail in Latin America compared with the United States or China, and millions of small businesses have yet to open their first online store.

For merchants, choosing a platform is a decision that is hard to reverse. Moving a store from one provider to another means migrating the catalog, customer data and order history, reconfiguring payments and shipping, and often redesigning the storefront. That switching cost is part of what investors pay for: once a merchant builds its operation on a platform, it tends to stay for years and to adopt the additional services the platform offers. It also means that platforms compete fiercely for merchants at the moment they open their first store, often with free trials, migration help and discounted fees for the first months.

With the Series E, the total Nuvemshop has raised in the previous ten months exceeds $620 million.
"""}
PLANTADOS["nuvemshop"] = [
    P(1, "Nuvemshop levantó US$500 millones en una Serie E", True, [N(500e6)]),
    P(2, "A una valoración de US$3.100 millones", True, [N(3.1e9)]),
    P(3, "Insight Partners y Tiger Global codirigieron", True, [T("insight")]),
    P(4, "Accel volvió a invertir", True, [T("accel"), NO_N(90e6)]),
    P(5, "Alkeon, Owl Rock, Sunley House y VMG invirtieron", True,
      [T("alkeon")], [T("owl rock")], [T("sunley")]),
    P(6, "Opera como Tiendanube en países de habla hispana", False, [T("tiendanube")]),
    P(7, "Cinco meses antes levantó US$90 millones liderados por Accel", False, [N(90e6)]),
    P(8, "Fundada en Argentina en 2011", False, [T("2011")]),
    P(9, "La ronda se anunció en agosto de 2021", True, [MES(8, 2021)]),
    P(10, "En los diez meses previos levantó más de US$620 millones", False, [N(620e6)], final=True),
]

# fuente: https://techcrunch.com/2022/06/07/ecuadorian-payments-infrastructure-startup-kushki-lands-100m-at-a-1-5b-valuation/ · https://www.fintechfutures.com/paytech/latam-paytech-kushki-valued-at-over-1bn-following-series-b-extension
FUENTES["kushki"] = {"idioma": "es", "url": "https://techcrunch.com/2022/06/07/ecuadorian-payments-infrastructure-startup-kushki-lands-100m-at-a-1-5b-valuation/", "texto": """\
Kushki se convierte en el primer unicornio de Ecuador

Quito — Kushki, la empresa ecuatoriana de infraestructura de pagos, anunció en junio de 2022 una extensión de US$100 millones de su ronda Serie B, con la que su valoración sube a US$1.500 millones. La compañía pasa a ser el primer unicornio de Ecuador.

En la extensión participaron Kaszek, Clocktower Ventures, el SoftBank Latin America Fund y DILA Capital. Con este tramo, la Serie B completa suma US$186 millones.

Las empresas de infraestructura de pagos son poco visibles para el consumidor, pero están detrás de casi cada compra en línea. Conectan a los comercios con las redes de tarjetas, los bancos adquirentes y los métodos de pago locales, y se encargan de autorizar, liquidar y conciliar cada transacción. En América Latina ese trabajo es más complejo que en otros mercados porque cada país tiene sus propios métodos de pago, reglas cambiarias y requisitos regulatorios.

El primer tramo de la Serie B, de US$86 millones, se había anunciado en junio de 2021 a una valoración posterior de US$600 millones. En un año, la compañía más que duplicó su valor.

Kushki fue fundada en 2016 en Quito por Aaron Gruber y Sebastián Castro. Opera en Ecuador, Colombia, Perú, Chile y México, donde además de procesar pagos con tarjeta ofrece transferencias, pagos en efectivo y adquirencia propia.

Los fondos se usarán, según la empresa, para ampliar su red de adquirencia directa en la región y para sumar productos para comercios.

Para el ecosistema ecuatoriano, que históricamente recibió muy poco capital de riesgo, la noticia tiene un peso simbólico. Inversionistas locales destacan que un unicornio suele generar una segunda ola de emprendimientos, cuando los primeros empleados salen a fundar sus propias empresas con experiencia y, a veces, con capital propio.

La competencia en infraestructura de pagos es intensa. Procesadores globales con presencia en decenas de países, bancos que ofrecen adquirencia a sus propios clientes y otras startups regionales buscan a los mismos comercios. La diferenciación suele estar en la cobertura de métodos de pago locales, la tasa de aprobación de las transacciones y la velocidad para integrar a un comercio nuevo. Para los grandes clientes, como plataformas de comercio electrónico o aplicaciones de transporte, una diferencia pequeña en la tasa de aprobación puede significar millones en ventas que se ganan o se pierden, y por eso suelen trabajar con más de un procesador a la vez y mover volumen hacia el que mejor rinde.

La compañía no entregó cifras de ingresos. Sí afirmó que sus ingresos crecieron 200% durante 2021.
"""}
PLANTADOS["kushki"] = [
    P(1, "Kushki anunció una extensión de Serie B de US$100 millones", True, [N(100e6)]),
    P(2, "La valoración sube a US$1.500 millones", True, [N(1.5e9)]),
    P(3, "Es el primer unicornio de Ecuador", True, [T("primer", "first"), T("ecuador")]),
    P(4, "Anunciada en junio de 2022", True, [MES(6, 2022)]),
    P(5, "Participaron Kaszek, Clocktower, SoftBank LatAm y DILA Capital", True,
      [T("clocktower")], [T("dila")]),
    P(6, "La Serie B completa suma US$186 millones", True, [N(186e6)]),
    P(7, "El primer tramo fue de US$86 millones en junio de 2021", False, [N(86e6)]),
    P(8, "A una valoración posterior de US$600 millones", False, [N(600e6)]),
    P(9, "Fundada en 2016 en Quito por Aaron Gruber y Sebastián Castro", False,
      [T("2016")], [T("gruber")]),
    P(10, "Opera en Ecuador, Colombia, Perú, Chile y México", False, [T("peru"), T("colombia")]),
    P(11, "Según la empresa, sus ingresos crecieron 200% en 2021", False, [N(200), T("%", "por ciento")],
      final=True),
]

# fuente: https://theprint.in/tech/reddit-prices-ipo-at-top-of-indicated-range-to-raise-748-million/2009226 · https://www.clickondetroit.com/business/2024/03/20/reddit-poised-to-make-its-stock-market-debut-after-ipo-prices-at-34-per-share-amid-strong-demand/
FUENTES["reddit"] = {"idioma": "en", "url": "https://theprint.in/tech/reddit-prices-ipo-at-top-of-indicated-range-to-raise-748-million/2009226", "texto": """\
Reddit prices IPO at top of range, raising $748 million

San Francisco — Reddit priced its initial public offering at $34 per share in March 2024, the top of the $31 to $34 range it had marketed to investors, raising about $748 million. At that price, the social media company is valued at about $6.4 billion.

Not all of the money goes to the company. About $228 million corresponds to shares sold by existing shareholders who chose to cash out part of their holdings. Excluding those secondary sales, Reddit raised gross proceeds of $519.4 million.

The shares are set to begin trading on the New York Stock Exchange under the ticker RDDT. Morgan Stanley, Goldman Sachs, JPMorgan Chase and Bank of America are the lead underwriters.

Initial public offerings of consumer internet companies had been rare for more than two years. Rising interest rates pushed investors toward profitable companies and away from businesses that promised growth in the future, and many startups that had planned to list in 2022 postponed their plans. Bankers had been watching the Reddit listing as a test of whether that window was reopening.

Reddit's business depends on advertising, which makes it sensitive to the same swings that affect other social platforms. The company has also started to license its archive of public conversations to companies that train artificial intelligence models, a source of revenue that did not exist a few years ago and that investors are still trying to value.

The company took an unusual step for a listing of its size: it set aside part of the offering for some of its most active users and moderators, who could buy shares at the IPO price before trading began. The move reflects how much the platform depends on volunteers who run its communities without pay.

Founded in 2005 by Steve Huffman and Alexis Ohanian, Reddit was acquired by Condé Nast a year later and became independent again in 2011. Huffman is the company's chief executive.

Investors also weighed the company's governance. Like many technology companies that list their shares, Reddit set up a structure that gives some shareholders more voting power than others, which limits the influence of the investors who buy in the offering. Supporters say such structures let management plan for the long term; critics say they weaken accountability. The debate has accompanied almost every large technology listing of the past decade, and index providers have at times excluded companies with unequal voting rights from some benchmarks.

The IPO valuation is well below what private investors paid for the company before the market downturn. In a private fundraising round in 2021, Reddit was valued at $10 billion.
"""}
PLANTADOS["reddit"] = [
    P(1, "Reddit fijó el precio de su OPI en US$34 por acción", True, [N(34), T("accion", "share")]),
    P(2, "Fue el tope del rango de US$31 a US$34", False, [N(31)]),
    P(3, "La OPI recaudó unos US$748 millones", True, [N(748e6)]),
    P(4, "Valoración de unos US$6.400 millones", True, [N(6.4e9)]),
    P(5, "Unos US$228 millones corresponden a accionistas que vendieron", True, [N(228e6)]),
    P(6, "Reddit recaudó ingresos brutos de US$519,4 millones", True, [N(519.4e6)]),
    P(7, "Cotizará en la Bolsa de Nueva York con el ticker RDDT", True, [T("rddt")]),
    P(8, "Colocadores: Morgan Stanley, Goldman Sachs, JPMorgan y Bank of America", False,
      [T("morgan stanley")], [T("bank of america")]),
    P(9, "La OPI fue en marzo de 2024", True, [MES(3, 2024)]),
    P(10, "Fundada en 2005 por Huffman y Ohanian", False, [T("2005")], [T("ohanian")]),
    P(11, "En una ronda privada de 2021 Reddit fue valorada en US$10.000 millones", False,
      [N(10e9)], final=True),
]

# fuente: https://www.xataka.com.mx/empresas-y-economia/mercado-libre-apuesta-que-nunca-mexico-invertira-3-400-millones-dolares-2025-creara-10-mil-nuevos-empleos · https://elceo.com/negocios/mercado-libre-anuncia-inversion-de-3400-mdd-para-2025-en-mexico/
FUENTES["mercadolibre_mx"] = {"idioma": "es", "url": "https://www.xataka.com.mx/empresas-y-economia/mercado-libre-apuesta-que-nunca-mexico-invertira-3-400-millones-dolares-2025-creara-10-mil-nuevos-empleos", "texto": """\
Mercado Libre invertirá US$3.400 millones en México durante 2025

Ciudad de México — Mercado Libre anunció que invertirá US$3.400 millones en México a lo largo de 2025, la mayor cifra que la empresa ha destinado al país. El anuncio lo hizo David Geisen, director general de la compañía en México, durante la conferencia matutina de la presidenta Claudia Sheinbaum.

La compañía prevé crear unos 10.000 empleos nuevos con este plan, principalmente en logística y en áreas administrativas.

El comercio electrónico en México ha crecido con rapidez desde la pandemia, pero todavía representa una parte pequeña del comercio minorista total. Las plataformas compiten en tres frentes a la vez: la variedad de productos, la velocidad de entrega y el acceso a medios de pago para una población en la que muchas personas no tienen tarjeta de crédito. Ganar en entrega rápida exige construir centros de distribución, flotas y puntos de recolección, inversiones que se recuperan en muchos años.

Los recursos se destinarán a tres áreas, según la empresa: tecnología e inteligencia artificial, la ampliación de su red logística y los servicios financieros de Mercado Pago, su brazo fintech.

La compañía tiene actualmente más de 25.000 empleados en México. Con las nuevas contrataciones, Mercado Libre espera que su plantilla en el país supere las 35.000 personas al cierre de 2025.

Mercado Pago es una pieza cada vez más importante de la estrategia. La empresa ha buscado convertirla en un banco con licencia en México, lo que le permitiría captar depósitos y ofrecer más productos de crédito. Los analistas siguen de cerca ese paso, porque el negocio financiero suele tener márgenes más altos que el comercio electrónico, pero también más riesgo.

La empresa competirá en un mercado donde Amazon, Walmart y nuevas plataformas asiáticas de bajo precio también están invirtiendo. La guerra por el consumidor mexicano se libra sobre todo en la última milla, donde cada día menos de entrega se traduce en más compras repetidas.

Para los vendedores pequeños, la expansión de la red logística tiene un efecto directo: entregar más rápido mejora la posición de sus productos en los resultados de búsqueda y reduce las cancelaciones. A cambio, deben adaptarse a reglas de inventario, tiempos de despacho y comisiones que fija la plataforma. La dependencia de un solo canal de venta es uno de los riesgos que más mencionan los comerciantes, junto con los cambios en las tarifas de envío y en las condiciones de pago a vendedores.

La inversión anunciada es 38% mayor que la de 2024, año en que la compañía invirtió alrededor de US$2.500 millones en el país. Al tipo de cambio citado en el anuncio, los US$3.400 millones equivalen a unos 69.952 millones de pesos.
"""}
PLANTADOS["mercadolibre_mx"] = [
    P(1, "Mercado Libre invertirá US$3.400 millones en México en 2025", True, [N(3.4e9)]),
    P(2, "Creará unos 10.000 empleos nuevos", True, [N(10000), T("emple", "trabaj", "puesto", "job")]),
    P(3, "Lo anunció David Geisen", True, [T("geisen")]),
    P(4, "En la conferencia matutina de Claudia Sheinbaum", True, [T("sheinbaum")]),
    P(5, "Destino: tecnología e IA, logística y Mercado Pago", False, [T("mercado pago")]),
    P(6, "Tiene más de 25.000 empleados en México", False, [N(25000)]),
    P(7, "Espera superar 35.000 empleados al cierre de 2025", False, [N(35000)]),
    P(8, "La inversión es 38% mayor que la de 2024", False, [N(38), T("%", "por ciento")]),
    P(9, "En 2024 invirtió alrededor de US$2.500 millones", False, [N(2.5e9)]),
    P(10, "Equivale a unos 69.952 millones de pesos", False, [N(69952e6)], final=True),
]

# fuente: https://techcrunch.com/2023/09/25/amazon-to-invest-up-to-4-billion-in-ai-startup-anthropic · https://www.geekwire.com/2023/amazon-pours-up-to-4b-into-ai-startup-anthropic-boosting-rivalry-with-microsoft-and-google/
FUENTES["amazon_anthropic"] = {"idioma": "en", "url": "https://techcrunch.com/2023/09/25/amazon-to-invest-up-to-4-billion-in-ai-startup-anthropic", "texto": """\
Amazon to invest up to $4 billion in Anthropic

Seattle — Amazon will invest up to $4 billion in Anthropic, the artificial intelligence company behind the Claude family of models, in exchange for a minority stake, the two companies said in September 2023.

The deal is structured in stages. Amazon has committed an initial $1.25 billion and holds an option to invest a further $2.75 billion, which would bring the total to $4 billion. Neither company disclosed the size of the stake or its valuation.

As part of the agreement, Amazon Web Services becomes Anthropic's primary cloud provider for mission-critical workloads, including safety research and the development of future foundation models. Anthropic also committed to build, train and deploy its models on Trainium and Inferentia, the chips that AWS designs in-house, and to make them available to AWS customers through Amazon Bedrock.

Partnerships between cloud providers and model developers have become a defining feature of the AI industry. Model developers need enormous amounts of computing capacity, and cloud companies want the most popular models to run on their infrastructure, where every customer request turns into billable usage. The investments often flow back to the investor in the form of cloud spending, which is why analysts look closely at how such deals are accounted for.

Anthropic was founded in 2021 by Dario Amodei and Daniela Amodei together with other former employees of OpenAI. The company has emphasized research on how to make AI systems safer and more predictable.

The agreement also puts pressure on Amazon's rivals. Microsoft is the largest investor in OpenAI, and Google has its own models as well as investments in other developers. For Amazon, which was seen as slower to respond to the rise of chatbots, the deal secures access to a leading model maker.

For enterprise customers, the practical effect of such partnerships is choice. A company already running its systems on one cloud can use models from several developers through that provider's platform, with the same contracts, billing and security controls. That convenience has become a competitive weapon among cloud providers, which now race to offer the widest catalog of models alongside their own, and it has made distribution through the cloud marketplaces one of the main ways model developers reach large companies.

Anthropic said the investment will not change its corporate governance structure or its commitment to the responsible development of artificial intelligence. The company also said it will continue to make its models available through Google Cloud.
"""}
PLANTADOS["amazon_anthropic"] = [
    P(1, "Amazon invertirá hasta US$4.000 millones en Anthropic", True, [N(4e9)]),
    P(2, "A cambio de una participación minoritaria", True, [T("minorit")]),
    P(3, "El compromiso inicial es de US$1.250 millones", True, [N(1.25e9)]),
    P(4, "Opción de invertir US$2.750 millones adicionales", True, [N(2.75e9)]),
    P(5, "AWS será el proveedor principal de nube de Anthropic", True,
      [T("proveedor principal", "primary cloud", "principal proveedor", "nube principal")]),
    P(6, "Anthropic usará los chips Trainium e Inferentia", True, [T("trainium")]),
    P(7, "El anuncio fue en septiembre de 2023", True, [MES(9, 2023)]),
    P(8, "No se reveló el tamaño de la participación", False,
      [T("no se revel", "no revel", "disclos", "sin revelar", "no divulg", "no se divulg", "no informaron", "no detall")],
      # 9-nov-2026: «Ni Amazon ni Anthropic revelaron el tamaño…» / «hicieron público el
      # porcentaje…» no tocaban el grupo de arriba; 8 de 8 modelos lo extraían y se contaba
      # omitido. Verbo + participación juntos (DECISIONES, regresión de Eco).
      [T("revelaron", "revelo", "hicieron publico", "dieron a conocer", "divulgaron", "informaron"),
       T("particip", "stake", "porcentaje")]),
    P(9, "Anthropic fue fundada en 2021 por Dario y Daniela Amodei", False, [T("2021")], [T("amodei")]),
    P(10, "Anthropic dijo que su gobierno corporativo no cambia", False,
      [T("gobierno corporativo", "governance", "gobernanza")]),
    P(11, "Anthropic seguirá ofreciendo sus modelos en Google Cloud", False, [T("google cloud")], final=True),
]

# fuente: https://www.fintechfutures.com/bankingtech/mexican-fintech-clip-raises-250m-in-softbank-led-investment · https://www.bloomberg.com/news/articles/2021-06-10/softbank-viking-invest-250-million-in-latam-fintech-unicorn
FUENTES["clip"] = {"idioma": "es", "url": "https://www.fintechfutures.com/bankingtech/mexican-fintech-clip-raises-250m-in-softbank-led-investment", "texto": """\
Clip recibe US$250 millones de SoftBank y Viking y se convierte en unicornio

Ciudad de México — Clip, la fintech mexicana que vende lectores de tarjetas y servicios de cobro a pequeños comercios, recibió en junio de 2021 una inversión de US$250 millones del SoftBank Latin America Fund y de Viking Global Investors. La operación valora a la empresa en cerca de US$2.000 millones, según la propia compañía.

Clip se convierte así en el primer unicornio de pagos de México.

Para un comercio pequeño, aceptar tarjetas era hasta hace pocos años un trámite largo: había que abrir una cuenta con un banco, firmar un contrato de adquirencia y rentar una terminal con costo fijo mensual. Las empresas como Clip simplificaron ese proceso con un lector barato que se conecta al teléfono y una comisión por venta, sin plazo forzoso. El modelo se apoya en el volumen, porque el margen por cada transacción es pequeño.

El fundador y director ejecutivo de la compañía, Adolfo Babatz, dijo que el dinero permitirá seguir creciendo de forma agresiva. Según Bloomberg, la empresa planea contratar a 320 personas en los próximos 18 meses.

Antes de esta ronda, Clip había recibido cerca de US$100 millones de inversionistas como General Atlantic, su mayor accionista. General Atlantic y SoftBank habían invertido en 2019, en una operación que, según reportes de la época, valoró a la empresa en US$400 millones.

El mercado sigue siendo amplio. Babatz estimó que de los casi 11 millones de negocios que hay en México, solo alrededor de 1 millón acepta pagos con tarjeta.

La competencia, sin embargo, también creció. Bancos, billeteras digitales y las terminales de grandes plataformas de comercio electrónico buscan a los mismos comerciantes, y la guerra de comisiones presiona los márgenes de todo el sector.

Para el pequeño comerciante, aceptar tarjetas tiene beneficios que van más allá de la venta inmediata. Los pagos digitales dejan un registro que puede servir para pedir un crédito, reducen el riesgo de manejar efectivo y permiten vender a clientes que ya no cargan billetes. Las empresas del sector aprovechan ese historial para ofrecer préstamos a sus comerciantes, un negocio con mejores márgenes que el cobro por transacción y que se ha vuelto central en la estrategia de casi todas las plataformas de adquirencia de la región.

Babatz dijo además que la empresa evalúa una oferta pública inicial para captar más capital y dar liquidez a sus inversionistas, aunque aclaró que no ocurriría durante 2021.
"""}
PLANTADOS["clip"] = [
    P(1, "Clip recibió una inversión de US$250 millones", True, [N(250e6)]),
    P(2, "De SoftBank Latin America Fund y Viking Global", True, [T("viking")]),
    P(3, "Según la compañía, la valoración es de cerca de US$2.000 millones", True, [N(2e9)]),
    P(4, "La inversión fue en junio de 2021", True, [MES(6, 2021)]),
    P(5, "Primer unicornio de pagos de México", False, [T("primer", "first"), T("pago", "payment")]),
    P(6, "Adolfo Babatz es fundador y CEO", False,
      [T("babatz"), T("fundador", "ceo", "director", "founder", "cofundador")]),
    P(7, "Según Bloomberg, contratará a 320 personas en 18 meses", False, [N(320)]),
    P(8, "Antes recibió cerca de US$100 millones (General Atlantic, mayor accionista)", False,
      [N(100e6)], [T("general atlantic"), T("mayor accionista", "largest shareholder", "principal accionista")]),
    P(9, "En 2019 fue valorada en US$400 millones", False, [N(400e6)]),
    P(10, "De casi 11 millones de negocios, solo cerca de 1 millón acepta tarjeta", False, [N(11e6)]),
    P(11, "Babatz dijo que una OPI no ocurriría en 2021", False,
      [T("opi", "oferta publica", "ipo", "bolsa")], final=True),
]

# fuente: https://techcrunch.com/2021/07/19/colombian-on-demand-delivery-startup-rappi-raises-over-500m-at-a-5-25b-valuation/ · https://www.lavca.org/t-rowe-price-leads-usd500m-series-f-round-for-rappi/
FUENTES["rappi"] = {"idioma": "en", "url": "https://techcrunch.com/2021/07/19/colombian-on-demand-delivery-startup-rappi-raises-over-500m-at-a-5-25b-valuation/", "texto": """\
Rappi raises more than $500 million at a $5.25 billion valuation

Bogotá — Rappi, the Colombian on-demand delivery company, has raised more than $500 million in a Series F round that values it at $5.25 billion. The round, announced in July 2021, was led by T. Rowe Price.

Baillie Gifford, Third Point, Octahedron and GIC also invested, and SoftBank, an existing shareholder, participated as well.

Delivery apps grew into one of the most visible technology categories in Latin American cities. Their basic proposition is simple, but the economics are difficult: each order requires a courier, the average ticket is small and customers are quick to switch to whichever app offers the best promotion. Most companies in the segment try to improve the math by adding higher-margin services on top of delivery, such as advertising for restaurants and brands, subscriptions and financial products.

Rappi has followed that playbook. Besides restaurant and grocery delivery, it offers a payments service, a credit card in partnership with banks and a subscription that waives delivery fees.

The company was founded in Bogotá in 2015 by Simón Borrero, Sebastián Mejía and Felipe Villamarín. It operates in nine countries in Latin America.

The company's previous raise was a $300 million round in September 2020, which reportedly valued Rappi at $3.5 billion. Before that, SoftBank had made a large investment in 2019 through its first Latin America fund, which made the Japanese group the company's biggest backer.

Rappi said it would use the new capital to expand its financial services and its network of dark stores, small warehouses in dense neighborhoods that allow groceries to be delivered in minutes instead of hours.

Competition remains intense. Global platforms and local players in each country are fighting for the same couriers, restaurants and customers, and regulators in several countries are debating whether delivery workers should be treated as employees.

The quick-commerce model has drawn skepticism from some investors. Dark stores require rent, staff and inventory in expensive neighborhoods, and the promise of delivery in minutes only pays off if each store processes enough orders per hour. Several companies in the United States and Europe that expanded aggressively with this model later closed locations or merged with competitors when funding became harder to obtain, and the companies that survived usually concentrated on fewer, denser cities.

According to Crunchbase data, the new financing brings the total Rappi has raised since its founding to more than $2 billion.
"""}
PLANTADOS["rappi"] = [
    P(1, "Rappi levantó más de US$500 millones en una Serie F", True, [N(500e6)]),
    P(2, "A una valoración de US$5.250 millones", True, [N(5.25e9)]),
    P(3, "T. Rowe Price lideró", True, [T("rowe price")]),
    P(4, "Baillie Gifford, Third Point, Octahedron y GIC invirtieron", True,
      [T("baillie")], [T("third point")], [T("octahedron")]),
    P(5, "Anunciada en julio de 2021", True, [MES(7, 2021)]),
    P(6, "Fundada en Bogotá en 2015 por Borrero, Mejía y Villamarín", False,
      [T("2015")], [T("borrero")]),
    P(7, "Opera en nueve países", False, [T("nueve", "nine", "9 paises", "9 países")]),
    P(8, "Su ronda anterior fue de US$300 millones en septiembre de 2020", False, [N(300e6)]),
    P(9, "Esa ronda la valoró en US$3.500 millones", False, [N(3.5e9)]),
    P(10, "Según Crunchbase, ha levantado más de US$2.000 millones en total", False,
      [N(2e9)], final=True),
]

# fuente: https://www.crowdfundinsider.com/2021/12/184008-nubank-prices-ipo-at-9-a-share-will-trade-on-nyse-under-ticker-nu/ · https://news.crunchbase.com/news/nubank-ipo-sequoia-decacorn-latam-fintech
FUENTES["nubank"] = {"idioma": "es", "url": "https://www.crowdfundinsider.com/2021/12/184008-nubank-prices-ipo-at-9-a-share-will-trade-on-nyse-under-ticker-nu/", "texto": """\
Nubank recauda US$2.600 millones en su salida a la bolsa de Nueva York

São Paulo — Nu Holdings, la empresa matriz del banco digital brasileño Nubank, fijó el precio de su oferta pública inicial en US$9 por acción, el tope del rango de US$8 a US$9 que había presentado a los inversionistas. La compañía vendió 289 millones de acciones y recaudó unos US$2.600 millones.

Las acciones empezaron a cotizar el 9 de diciembre de 2021 en la Bolsa de Nueva York con el símbolo NU. También se negocian en São Paulo como certificados de depósito, con el código NUBR33.

Al precio de la oferta, la valoración implícita de la compañía ronda los US$41.400 millones, lo que la convierte en la institución financiera más valiosa de América Latina, por encima de Itaú Unibanco, que vale unos US$38.000 millones en bolsa.

Los bancos digitales ganaron terreno en Brasil por una combinación de factores: una banca tradicional muy concentrada, con tarifas altas y mala experiencia de servicio, y una población que adoptó el teléfono como principal puerta de entrada a internet. La estrategia de estas empresas suele empezar con un producto gratuito y fácil de contratar, como una tarjeta sin comisión anual, para luego ofrecer cuentas, inversiones, seguros y créditos a la misma base de clientes.

Nubank fue fundada en 2013 por David Vélez, Cristina Junqueira y Edward Wible. Vélez, nacido en Colombia, es el director ejecutivo. La compañía opera en Brasil, México y Colombia.

Entre los inversionistas de la empresa antes de la salida a bolsa figuraban Sequoia Capital, Tencent y Berkshire Hathaway, que había invertido meses antes.

Las salidas a bolsa de empresas latinoamericanas en Estados Unidos son poco frecuentes, y los banqueros esperaban que el resultado de Nubank sirviera de referencia para otras compañías de la región que preparan su debut.

Para los inversionistas, la pregunta central sobre los bancos digitales es cuánto ganan por cliente y cuánto les cuesta adquirirlo. Las empresas que crecen con tarjetas de crédito asumen riesgo desde el primer día, y la calidad de su modelo de aprobación se pone a prueba recién cuando la economía se desacelera. Por eso los analistas siguen de cerca los indicadores de morosidad y el costo del fondeo, además del crecimiento de la base de clientes, y comparan esas cifras con las de los bancos tradicionales del mismo mercado.

El camino hasta el precio final no fue lineal. La semana anterior, Nubank había rebajado el rango de precio; con el rango original, la empresa aspiraba a recaudar hasta US$3.180 millones.
"""}
PLANTADOS["nubank"] = [
    P(1, "Nubank fijó su OPI en US$9 por acción", True, [N(9), T("accion", "share")]),
    # 9-nov-2026: sale «Fue el tope del rango de US$8 a US$9». Es discutible como afirmación
    # aparte: los modelos dan el precio y el rango por separado sin la palabra «tope», y eso no
    # es omitir nada. Una verdad discutible no reprueba a un candidato (DECISIONES).
    P(3, "Vendió 289 millones de acciones", True, [N(289e6)]),
    P(4, "Recaudó unos US$2.600 millones", True, [N(2.6e9)]),
    P(5, "Empezó a cotizar el 9 de diciembre de 2021 en la NYSE con el símbolo NU", True,
      [DIA(9, 12)], [T("diciembre de 2021", "december 2021")]),
    P(6, "Cotiza en São Paulo con el código NUBR33", False, [T("nubr33")]),
    P(7, "Valoración implícita de unos US$41.400 millones", True, [N(41.4e9)]),
    P(8, "Supera a Itaú Unibanco (unos US$38.000 millones)", False, [N(38e9)], [T("itau")]),
    P(9, "Fundada en 2013 por Vélez, Junqueira y Wible", False, [T("2013")], [T("junqueira")]),
    P(10, "Sequoia, Tencent y Berkshire Hathaway eran inversionistas", False, [T("berkshire")]),
    P(11, "Con el rango original aspiraba a recaudar hasta US$3.180 millones", False,
      [N(3.18e9)], final=True),
]

# fuente: https://www.nbcnews.com/business/business-news/elon-musks-ai-startup-now-valued-24-billion-fresh-funding-rcna154171 · https://siliconangle.com/2024/05/27/elon-musks-xai-raises-6b-build-new-ai-services
FUENTES["xai"] = {"idioma": "en", "url": "https://www.nbcnews.com/business/business-news/elon-musks-ai-startup-now-valued-24-billion-fresh-funding-rcna154171", "texto": """\
Elon Musk's xAI raises $6 billion in Series B

Elon Musk's artificial intelligence company xAI has raised $6 billion in a Series B round, the company said in May 2024. According to Reuters, the round gives xAI a post-money valuation of $24 billion.

The investors include Valor Equity Partners, Vy Capital, Andreessen Horowitz, Sequoia Capital and Fidelity Management & Research Company, as well as Prince Alwaleed Bin Talal and Kingdom Holding.

xAI said the money will be used to take its first products to market, build advanced infrastructure and accelerate research and development of future technologies.

The race to build frontier models has turned into a race for capital. Training each new generation of models costs more than the last, and the companies at the front of the pack are raising amounts that, only a few years ago, would have been reserved for public companies. Investors justify the checks by pointing to the size of the markets these models could reshape, from software development to customer service, while skeptics note how few of these companies have shown a path to profit.

Musk launched xAI in 2023, after years of public criticism of OpenAI, the company he helped found and later left. xAI's chatbot, Grok, is available to subscribers of X, the social network Musk also owns, and the two companies share data and users.

The round places xAI among the most valuable AI startups in the world, though still well behind OpenAI. Musk has said the company intends to catch up with the leaders by building one of the largest computing clusters in the world, a plan that depends on securing tens of thousands of specialized chips at a time when supply is tight.

The company has hired researchers from Google DeepMind, OpenAI and other labs, and has said it wants to build systems that seek to understand the universe.

Rivals have taken different approaches to the same problem. Some labs rely on partnerships with large cloud providers, trading equity for computing capacity; others build their own data centers or rent capacity from specialized providers. Each path carries trade-offs in cost, control and speed, and the choice increasingly shapes how quickly a lab can train and ship new models. Investors evaluating these companies now ask as much about access to chips and electricity as about research talent, a shift that has favored founders with deep pockets and strong relationships with chip suppliers.

In a post on X, Musk put the pre-money valuation at $18 billion.
"""}
PLANTADOS["xai"] = [
    P(1, "xAI levantó US$6.000 millones en una Serie B", True, [N(6e9)]),
    P(2, "Según Reuters, valoración post-money de US$24.000 millones", True, [N(24e9)]),
    P(3, "Anunciado en mayo de 2024", True, [MES(5, 2024)]),
    P(4, "Valor Equity, Vy Capital, a16z, Sequoia y Fidelity invirtieron", True,
      [T("valor equity")], [T("vy capital")], [T("fidelity")]),
    P(5, "Alwaleed Bin Talal y Kingdom Holding invirtieron", True, [T("alwaleed")], [T("kingdom holding")]),
    P(6, "El dinero irá a productos, infraestructura e I+D", False,
      [T("infraestructura", "infrastructure")]),
    P(7, "Musk lanzó xAI en 2023", False, [T("2023")]),
    P(8, "Grok está disponible para suscriptores de X", False, [T("grok")]),
    P(9, "Según Musk en X, la valoración pre-money fue de US$18.000 millones", False,
      [N(18e9)], final=True),
]

# fuente: https://www.df.cl/empresas/empresas-y-startups/fintual-levanta-us-39-millones-en-ronda-liderada-por-sequoia-capital · https://forbes.cl/negocios/2021-11-02/fintual-recauda-39-millones-dolares-sequoia-capital/
FUENTES["fintual"] = {"idioma": "es", "url": "https://www.df.cl/empresas/empresas-y-startups/fintual-levanta-us-39-millones-en-ronda-liderada-por-sequoia-capital", "texto": """\
Fintual levanta US$39 millones en una ronda liderada por Sequoia Capital

Santiago — Fintual, la administradora de fondos chilena que permite invertir desde una aplicación, cerró en noviembre de 2021 una ronda Serie B de US$39 millones liderada por Sequoia Capital. También participaron ALLVP y Kaszek, que ya eran inversionistas desde la Serie A.

Es la primera inversión de Sequoia en Chile y, según la prensa local, la tercera del fondo en una empresa latinoamericana, después de Rappi y Nubank.

Fintual nació con una idea concreta: que una persona sin conocimientos financieros pueda invertir en fondos diversificados con montos pequeños y comisiones bajas, sin pasar por un ejecutivo. En Chile, el ahorro voluntario para la jubilación es un mercado relevante porque las pensiones del sistema obligatorio suelen quedar por debajo de lo que las personas esperan, y eso empuja a muchos trabajadores a buscar alternativas.

La compañía fue fundada en 2016 por Pedro Pineda, Agustín Feuerhake, Alfonso Valdés y Pablo Mansilla. Opera en Chile y en México, donde lanzó su servicio en 2020.

Según la empresa, los recursos se destinarán principalmente a acelerar su operación en México, aunque también seguirá creciendo en Chile.

Unos meses antes, Fintual había levantado cerca de US$15 millones en una Serie A liderada por Kaszek.

Las plataformas de inversión digital compiten con bancos y administradoras tradicionales que han lanzado sus propias aplicaciones, y con corredoras que ofrecen acciones sin comisión. El costo de adquirir clientes es alto y la rentabilidad depende de acumular un volumen grande de activos administrados, porque las comisiones, por diseño, son bajas.

Para los inversionistas de riesgo, el atractivo del modelo está en su escala potencial: una vez que la plataforma funciona en un país, sumar clientes cuesta poco y cada peso administrado genera ingresos durante años. El riesgo está en que la regulación y la cultura de ahorro cambian de un país a otro, y lo que funcionó en Chile no necesariamente se replica en México.

Los reguladores también observan de cerca a estas plataformas. Las administradoras de fondos deben cumplir reglas sobre cómo invierten el dinero de sus clientes, cómo informan las comisiones y cómo protegen los activos ante una eventual quiebra de la propia administradora. Para las empresas nuevas, cumplir esas exigencias desde el inicio es costoso, pero también es lo que les permite competir en confianza con instituciones que llevan décadas en el mercado y que tienen marcas reconocidas por varias generaciones de ahorrantes.

La ronda dejó también una meta explícita: alcanzar la rentabilidad. Según Diario Financiero, la empresa reportó utilidades por primera vez en el primer semestre de 2024.
"""}
PLANTADOS["fintual"] = [
    P(1, "Fintual cerró una Serie B de US$39 millones", True, [N(39e6)]),
    P(2, "Liderada por Sequoia Capital", True, [T("sequoia"), T("lider", "encabez", "led ", "lead")]),
    P(3, "Participaron ALLVP y Kaszek", True, [T("allvp")]),
    P(4, "La ronda fue en noviembre de 2021", True, [MES(11, 2021)]),
    P(5, "Es la primera inversión de Sequoia en Chile", False, [T("primera", "first"), T("chile"), T("sequoia")]),
    P(6, "Según la prensa, la tercera de Sequoia en LatAm, tras Rappi y Nubank", False, [T("rappi")]),
    P(7, "Fundada en 2016 por Pineda, Feuerhake, Valdés y Mansilla", False, [T("2016")], [T("feuerhake")]),
    P(8, "Lanzó su servicio en México en 2020", False, [T("2020")]),
    P(9, "Antes levantó cerca de US$15 millones en una Serie A liderada por Kaszek", False, [N(15e6)]),
    P(10, "Según DF, reportó utilidades por primera vez en el primer semestre de 2024", False,
      [T("2024"), T("utilidad", "ganancia", "rentab", "profit", "beneficio")], final=True),
]

# fuente: https://qz.com/instacart-sets-ipo-price-at-30-a-share-valuing-the-co-1850851226 · https://www.barchart.com/story/news/20384700/instacart-goes-from-the-supermarket-to-the-stock-market-raising-660-million-with-its-ipo
FUENTES["instacart"] = {"idioma": "en", "url": "https://qz.com/instacart-sets-ipo-price-at-30-a-share-valuing-the-co-1850851226", "texto": """\
Instacart prices IPO at $30 a share

San Francisco — Instacart priced its initial public offering at $30 per share, the top of its marketed range, raising $660 million from the sale of 22 million shares. The price gives the grocery delivery company a market value of around $10 billion.

The company's shares began trading on the Nasdaq on September 19, 2023, under the ticker CART.

Grocery delivery was one of the clearest winners of the pandemic. Households that had never ordered food online started doing so almost overnight, and retailers that had resisted working with third-party platforms signed on to keep up. As stores reopened, growth slowed, and companies in the sector shifted their focus from adding customers to making each order profitable, mostly by selling advertising to the consumer brands whose products appear in the app.

Instacart works with grocery chains rather than running its own stores. Shoppers pick items from store shelves and deliver them, and the company also sells software that lets retailers run their own online stores and in-store technology such as smart carts.

The company was founded in 2012 by Apoorva Mehta, a former Amazon engineer. Fidji Simo, a former Meta executive, has been its chief executive since 2021.

The listing was closely watched as one of the first large technology IPOs after a long drought, along with that of the chip designer Arm earlier in the same month. Bankers hoped that a strong debut would encourage other companies to follow.

The valuation is far below what private investors once paid. In early 2021, at the height of the delivery boom, Instacart announced a funding round that valued it at $39 billion.

Analysts covering the listing pointed to the company's advertising business as the key to its valuation. Consumer goods companies pay to have their products appear prominently when shoppers search the app, and that revenue carries much higher margins than delivery fees. The question for investors is how much of that advertising can grow without annoying shoppers, and whether grocery chains will keep sharing their customers with a platform that also competes for their attention. Several of the largest chains have been building their own delivery and advertising operations, which could reduce how much they depend on a third-party marketplace over time. For now, most of them still rely on the platform to reach customers who expect to compare stores and products in a single app before deciding where to buy.

Demand on the first day was strong. In the first minutes of trading, the shares reached a peak of $42.95.
"""}
PLANTADOS["instacart"] = [
    P(1, "Instacart fijó su OPI en US$30 por acción", True, [N(30), T("accion", "share")]),
    P(2, "Fue el tope del rango", False, [T("tope", "top", "extremo superior", "parte alta", "maximo")]),
    P(3, "Recaudó US$660 millones", True, [N(660e6)]),
    P(4, "Vendió 22 millones de acciones", True, [N(22e6)]),
    P(5, "Valor de mercado de unos US$10.000 millones", True, [N(10e9)]),
    P(6, "Empezó a cotizar el 19 de septiembre de 2023 en Nasdaq con el ticker CART", True,
      [DIA(19, 9)],
      [T("ticker cart", "simbolo cart", "codigo cart", "(cart", "cart)", "«cart", '"cart', "'cart", ": cart")]),
    P(7, "Fundada en 2012 por Apoorva Mehta", False, [T("2012")], [T("mehta")]),
    P(8, "Fidji Simo es CEO desde 2021", False, [T("simo")]),
    P(9, "A inicios de 2021 fue valorada en US$39.000 millones", False, [N(39e9)]),
    P(10, "En los primeros minutos la acción llegó a US$42,95", False, [N(42.95)], final=True),
]

# fuente: https://techcrunch.com/2021/12/06/platzi-picks-up-62-million-series-b-to-re-skill-latin-american-professionals/ · https://www.prosus.com/news-insights/2021/platzi-raises-60-million-in-series-funding-led-by-prosus
FUENTES["platzi"] = {"idioma": "es", "url": "https://techcrunch.com/2021/12/06/platzi-picks-up-62-million-series-b-to-re-skill-latin-american-professionals/", "texto": """\
Platzi cierra una Serie B liderada por Prosus

Bogotá — Platzi, la plataforma de educación en línea para profesionales de tecnología, cerró en diciembre de 2021 una ronda Serie B liderada por Prosus. La empresa informó un monto de US$62 millones; en su propio comunicado, Prosus habló de US$60 millones.

En la ronda también participaron Foundation Capital y Y Combinator, aceleradora por la que pasó la compañía en sus primeros años.

La educación en línea para adultos vive de una promesa: que un curso permita conseguir un empleo mejor pagado o un ascenso. El problema clásico del sector es la deserción. La mayoría de las personas que se inscribe en un curso en línea no lo termina, y las plataformas que logran retener a sus estudiantes lo hacen con comunidades, rutas de aprendizaje con objetivos claros y contenido que se actualiza al ritmo de la industria.

La compañía fue fundada por Freddy Vega y Christian Van Der Henst, y dice haber atendido a más de 3 millones de estudiantes en América Latina.

Según la empresa, los fondos se destinarán a hacer la plataforma más accesible, a ampliar su academia de inglés y a fortalecer su oferta para empresas y gobiernos, que compran licencias para capacitar a sus equipos.

El mercado de talento tecnológico en la región explica parte del interés de los inversionistas. Las empresas de software de Estados Unidos y Europa contratan cada vez más desarrolladores latinoamericanos de forma remota, y la demanda de perfiles con buen nivel de inglés supera a la oferta disponible.

La competencia incluye a plataformas globales con catálogos más grandes y a bootcamps intensivos que prometen un cambio de carrera en pocos meses. La apuesta de Platzi es ofrecer contenido producido en español y pensado para el mercado laboral latinoamericano.

La venta a empresas se volvió una pieza central para las plataformas de educación en línea. Las compañías prefieren pagar licencias anuales para capacitar a sus equipos en lugar de reembolsar cursos individuales, y ese tipo de contrato es más predecible que las suscripciones de personas que se inscriben y cancelan según su momento laboral. Para la plataforma, el reto es demostrar que la capacitación tiene un efecto medible en el desempeño, porque eso es lo que justifica la renovación de los contratos cuando los presupuestos de recursos humanos se ajustan y las áreas de formación compiten con otras prioridades.

La empresa anunció además que, con estos recursos, iniciará operaciones en Brasil.
"""}
PLANTADOS["platzi"] = [
    P(1, "Según la empresa, Platzi levantó US$62 millones en una Serie B", True, [N(62e6)]),
    P(2, "Prosus comunicó un monto de US$60 millones", False, [N(60e6)]),
    P(3, "Prosus lideró la ronda", True, [T("prosus"), T("lider", "encabez", "led ", "lead")]),
    P(4, "Foundation Capital y Y Combinator participaron", True, [T("foundation capital")], [T("y combinator")]),
    P(5, "La ronda fue en diciembre de 2021", True, [MES(12, 2021)]),
    P(6, "Fundada por Freddy Vega y Christian Van Der Henst", False, [T("freddy vega")], [T("van der henst")]),
    P(7, "Dice haber atendido a más de 3 millones de estudiantes", False, [N(3e6)]),
    P(8, "Ampliará su academia de inglés", False, [T("ingles", "english")]),
    P(9, "Fortalecerá su oferta para empresas y gobiernos", False, [T("gobierno", "government")]),
    P(10, "Iniciará operaciones en Brasil", False, [T("brasil", "brazil")], final=True),
]

# fuente: https://www.df.cl/empresas/consumo/uber-confirma-pagara-hasta-us-459-millones-por-el-control-de-cornershop · https://lexlatin.com/noticias/uber-triunfa-walmart-compra-cornershop
FUENTES["cornershop"] = {"idioma": "es", "url": "https://www.df.cl/empresas/consumo/uber-confirma-pagara-hasta-us-459-millones-por-el-control-de-cornershop", "texto": """\
Uber pagará hasta US$459 millones por el control de Cornershop

Santiago — Uber confirmó en un documento presentado ante el regulador bursátil de Estados Unidos que pagará hasta US$459 millones, en efectivo y en acciones de Uber, por una participación mayoritaria en Cornershop, la aplicación chilena de compras de supermercado a domicilio. Las estimaciones publicadas cuando se anunció el acuerdo, en octubre de 2019, hablaban de unos US$450 millones.

Cornershop fue fundada en 2015 por Oskar Hjertonsson, Daniel Undurraga y Juan Pablo Cuevas, y opera en Chile, México, Perú, Colombia y Canadá. Su modelo conecta a los clientes con compradores independientes que hacen el pedido en el supermercado y lo llevan a domicilio.

La venta de supermercado en línea es un negocio de márgenes estrechos. A diferencia de la comida preparada, una compra de supermercado tiene decenas de productos, algunos refrigerados, y los errores de reemplazo o de calidad son frecuentes. Por eso las plataformas invierten en catálogos actualizados, en entrenar a sus compradores y en acuerdos con las cadenas para acceder a inventario en tiempo real.

El camino de Cornershop hacia una venta no fue sencillo. Antes de Uber, Walmart había acordado comprar la empresa por unos US$225 millones, pero la Comisión Federal de Competencia Económica de México (COFECE) rechazó esa operación en 2019 por riesgos para la competencia.

La compra por parte de Uber también tuvo que pasar por los reguladores. La Fiscalía Nacional Económica de Chile (FNE) la aprobó en enero de 2020, y la COFECE dio su autorización en diciembre de 2020.

Los pagos se hicieron por etapas. A septiembre de 2020, Uber ya había desembolsado US$379 millones, y quedaban unos US$80 millones pendientes, sujetos a la aprobación mexicana.

Para Uber, la operación fue la puerta de entrada al reparto de supermercado, un negocio que la pandemia volvió mucho más relevante para su división de entregas.

Las autoridades de competencia de la región han aumentado su atención sobre las plataformas digitales. Las adquisiciones de empresas pequeñas por parte de grupos grandes, que antes pasaban casi sin revisión, ahora se analizan con más detalle cuando pueden reducir la competencia en mercados que todavía se están formando. Para los fundadores, eso significa que una venta puede tardar muchos meses en concretarse, y que el contrato debe prever qué ocurre si un regulador la bloquea o exige condiciones.

La historia tuvo un capítulo final. En junio de 2021, Uber anunció que compraría el resto de las acciones de Cornershop para quedarse con el 100% de la empresa.
"""}
PLANTADOS["cornershop"] = [
    P(1, "Uber pagará hasta US$459 millones por el control de Cornershop", True, [N(459e6)]),
    P(2, "El pago es en efectivo y acciones de Uber", True, [T("acciones", "shares", "stock"), T("efectivo", "cash")]),
    P(3, "El acuerdo se anunció en octubre de 2019", True, [MES(10, 2019)]),
    P(4, "Estimaciones previas hablaban de unos US$450 millones", False, [N(450e6)]),
    P(5, "Fundada en 2015 por Hjertonsson, Undurraga y Cuevas", False, [T("2015")], [T("hjertonsson")]),
    P(6, "Walmart había acordado comprarla por unos US$225 millones", False, [N(225e6)]),
    P(7, "COFECE rechazó la compra de Walmart en 2019", False, [T("walmart"), T("rechaz", "bloque", "blocked", "rejected")]),
    P(8, "La FNE aprobó la compra de Uber en enero de 2020", True, [MES(1, 2020)], [T("fne"), T("aprob")]),
    P(9, "COFECE autorizó en diciembre de 2020", True, [MES(12, 2020)]),
    P(10, "A septiembre de 2020 Uber había pagado US$379 millones", False, [N(379e6)]),
    P(11, "Quedaban unos US$80 millones pendientes", False, [N(80e6)]),
    P(12, "En junio de 2021 Uber anunció que compraría el 100%", False, [MES(6, 2021)],
      [N(100), T("%", "por ciento", "totalidad")], final=True),
]

# fuente: https://latamlist.com/mexican-fintech-klar-raises-190m-series-c/ · https://www.fintechfutures.com/venture-capital-funding/mexicos-klar-bags-190m-in-new-funding-at-reported-800m-valuation
FUENTES["klar"] = {"idioma": "en", "url": "https://latamlist.com/mexican-fintech-klar-raises-190m-series-c/", "texto": """\
Mexican fintech Klar raises $190 million Series C led by General Atlantic

Mexico City — Klar, the Mexican digital bank, has raised $190 million in a Series C round led by General Atlantic, Bloomberg reported. The round, closed in mid-2025, values the company at more than $800 million.

The financing combines $170 million in equity with $20 million in venture debt.

Existing investors Prosus, IFC, Mouro Capital and Quona Capital took part, and the round brought in new backers including Santander Group, Grupo Televisa and Grupo Fórmula.

Digital banks in Mexico target a population that has historically been underserved by traditional lenders. A large share of adults do not have a credit card, and many who apply are rejected because they lack a credit history. The newer players try to solve that with secured cards, small initial credit limits that grow with good payment behavior, and underwriting models that use alternative data. The trade-off is risk: lending to customers without a history requires careful collection practices and enough capital to absorb losses in a downturn.

Klar was founded in 2019 by Stefan Möller. The company offers a debit account, a credit card and personal loans through its app.

According to the company, the money will go toward growth in Mexico, new products and reaching more customers. Klar is also expanding into services for small businesses and is pursuing a banking license, which would allow it to take deposits under the same rules as a traditional bank.

The round comes as investment in Mexican fintech recovers after two quiet years. Larger rounds are again going to companies that can show both growth and a credible path to profitability. One report cited in the coverage said Klar is approaching $300 million in annual revenue as it shifts its focus from growth to profitability.

For investors, the appeal of the segment lies in the size of the gap. Mexico has one of the lowest rates of credit penetration among large Latin American economies, and every customer who builds a good payment record becomes eligible for larger and more profitable products. The risk is that competition for those same customers is intensifying: traditional banks have improved their apps, retailers offer their own credit, and other digital banks with deep-pocketed backers are chasing the same users with promotional rates and rewards programs that compress margins for everyone in the market.

This is not the first time General Atlantic has led a round for the company. In an earlier round, Klar raised $70 million at a $500 million valuation, also led by General Atlantic.
"""}
PLANTADOS["klar"] = [
    P(1, "Klar levantó US$190 millones en una Serie C", True, [N(190e6)]),
    P(2, "Liderada por General Atlantic", True, [T("general atlantic"), NO_N(70e6, 500e6)]),
    P(3, "Valoración de más de US$800 millones", True, [N(800e6)]),
    P(4, "US$170 millones son capital", True, [N(170e6)]),
    P(5, "US$20 millones son deuda de riesgo", True, [N(20e6)]),
    P(6, "Prosus, IFC, Mouro y Quona participaron", True, [T("mouro")], [T("quona")], [T("ifc")]),
    P(7, "Santander, Televisa y Grupo Fórmula entraron como nuevos", True,
      [T("santander")], [T("televisa")], [T("formula")]),
    P(8, "Fundada en 2019 por Stefan Möller", False, [T("2019")], [T("moller", "möller", "moeller")]),
    P(9, "Busca una licencia bancaria", False, [T("licencia", "license")]),
    P(10, "Según un reporte, se acerca a US$300 millones de ingresos anuales", False, [N(300e6)]),
    P(11, "Antes levantó US$70 millones a US$500 millones de valoración, también con General Atlantic", False,
      [N(70e6)], [N(500e6)], final=True),
]

# fuente: https://www.elfinanciero.com.mx/empresas/2022/05/24/nowports-startup-regia-se-convierte-en-el-primer-unicornio-en-logitech-de-hispanoamerica/ · https://www.freightwaves.com/news/nowports-hits-unicorn-status-at-1b-valuation-with-new-funding
FUENTES["nowports"] = {"idioma": "es", "url": "https://www.elfinanciero.com.mx/empresas/2022/05/24/nowports-startup-regia-se-convierte-en-el-primer-unicornio-en-logitech-de-hispanoamerica/", "texto": """\
Nowports se convierte en el primer unicornio logístico de Hispanoamérica

Monterrey — Nowports, la empresa mexicana de logística y agenciamiento de carga, cerró en mayo de 2022 una ronda Serie C de US$150 millones que la valora en US$1.100 millones. La ronda fue liderada por el SoftBank Latin America Fund y contó con la participación de Tencent.

Con esta operación, la compañía regiomontana se convierte en el primer unicornio de tecnología logística de Hispanoamérica.

El agenciamiento de carga es uno de los eslabones menos digitalizados del comercio internacional. Para mover un contenedor de un puerto asiático a una bodega en México intervienen navieras, agentes aduanales, transportistas terrestres, almacenes y bancos, y buena parte de esa coordinación todavía se hace por correo electrónico y hojas de cálculo. Las empresas como Nowports ofrecen una plataforma que centraliza el seguimiento de la carga, los documentos y los pagos, y en algunos casos financian a los importadores mientras la mercancía está en tránsito.

La compañía fue fundada en 2018 por Maximiliano Casal y Alfonso de los Ríos.

El financiamiento de inventario es una parte importante del negocio. Muchos importadores pequeños deben pagar a sus proveedores antes de recibir la mercancía y venderla, y esa brecha de caja limita cuánto pueden comprar. Prestarles contra la carga en tránsito permite a la plataforma cobrar intereses además de las tarifas logísticas.

Según la empresa, los nuevos recursos se usarán para ampliar sus servicios financieros en América Latina y para abrir oficinas en Brasil, México y Chile.

La relocalización de cadenas de suministro hacia América del Norte, conocida como nearshoring, ha puesto a Monterrey en el centro del interés de inversionistas y fabricantes, y las empresas de logística de la ciudad buscan aprovechar ese impulso.

El sector tiene una dificultad estructural: el negocio logístico depende de ciclos de comercio internacional que nadie controla. Cuando las tarifas de los fletes marítimos se dispararon durante la pandemia, las empresas de agenciamiento de carga facturaron más que nunca; cuando las tarifas cayeron, los ingresos se contrajeron con la misma rapidez. Los inversionistas valoran por eso a las compañías que logran ingresos recurrentes por software o por servicios financieros, menos expuestos a los vaivenes del precio del flete y más fáciles de proyectar en el tiempo. Esa es también la razón por la que muchas empresas del rubro intentan venderse como compañías de tecnología y no como agentes de carga tradicionales.

Pocos meses antes, en diciembre de 2021, Nowports había cerrado una Serie B de US$60 millones liderada por Tiger Global.
"""}
PLANTADOS["nowports"] = [
    P(1, "Nowports cerró una Serie C de US$150 millones", True, [N(150e6)]),
    P(2, "La valoración es de US$1.100 millones", True, [N(1.1e9)]),
    P(3, "La ronda fue en mayo de 2022", True, [MES(5, 2022)]),
    P(4, "Liderada por SoftBank Latin America Fund", True, [T("softbank")]),
    P(5, "Tencent participó", True, [T("tencent")]),
    P(6, "Primer unicornio de tecnología logística de Hispanoamérica", False,
      [T("primer", "first"), T("logist", "logtech")]),
    P(7, "Fundada en 2018 por Maximiliano Casal y Alfonso de los Ríos", False, [T("2018")], [T("casal")]),
    P(8, "Abrirá oficinas en Brasil, México y Chile", False, [T("oficina", "office"), T("brasil", "brazil")]),
    P(9, "Con sede en Monterrey", False, [T("monterrey", "regiomontana")]),
    P(10, "En diciembre de 2021 cerró una Serie B de US$60 millones liderada por Tiger Global", False,
      [N(60e6)], final=True),
]

# fuente: https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/ · https://techcrunch.com/2023/01/23/microsoft-invests-billions-more-dollars-in-openai-extends-partnership/
FUENTES["microsoft_openai"] = {"idioma": "en", "url": "https://blogs.microsoft.com/blog/2023/01/23/microsoftandopenaiextendpartnership/", "texto": """\
Microsoft extends OpenAI partnership with multibillion-dollar investment

Redmond — Microsoft announced in January 2023 a new multiyear, multibillion-dollar investment in OpenAI, the research company behind ChatGPT, extending a partnership that began four years earlier. Microsoft did not disclose the amount. Media reports, citing people familiar with the matter, put it at $10 billion.

Under the agreement, Microsoft Azure will remain OpenAI's exclusive cloud provider, powering all of OpenAI's workloads across research, products and API services. Microsoft also said it will deploy OpenAI's models across its consumer and enterprise products and build new categories of digital experiences on top of them.

The partnership is a bet on a particular division of labor. Training and serving large models requires data centers with specialized chips, networking and power on a scale that only a handful of companies can build. Model developers bring the research; cloud providers bring the infrastructure and the sales channels to large companies. Each side needs the other, but each also worries about depending too much on a single partner.

Microsoft first invested in OpenAI in 2019, with $1 billion, and invested again in 2021. The relationship gave Microsoft early access to the technology that it later integrated into its search engine, its office software and its developer tools.

The announcement came only weeks after the public launch of ChatGPT, in November 2022, which drew millions of users in a matter of days and set off a race among large technology companies to bring generative AI to their products. Google and Amazon, Microsoft's main rivals in cloud computing, accelerated their own work in response.

OpenAI was founded in 2015 as a nonprofit research laboratory. In 2019 it created a for-profit arm with a cap on the returns that investors can receive, a structure designed to raise the large amounts of capital its research requires.

The arrangement also raised questions that regulators would later examine. Competition authorities in the United States, the United Kingdom and the European Union looked at whether large technology companies were using investments in AI developers to gain influence over them without the scrutiny that a formal acquisition would bring. Both companies have said that OpenAI remains independent and that the partnership does not give Microsoft control over its decisions, and similar questions have since been raised about other investments by large cloud providers in model developers.

Microsoft also said that, as part of the agreement, it will build specialized supercomputing systems to support OpenAI's research.
"""}
PLANTADOS["microsoft_openai"] = [
    P(1, "Microsoft anunció una inversión plurianual multimillonaria en OpenAI", True,
      [T("openai"), T("plurianual", "multiyear", "varios anos", "multianual", "multimillonaria", "multibillion")]),
    P(2, "El anuncio fue en enero de 2023", True, [MES(1, 2023)]),
    P(3, "Microsoft no reveló el monto", True,
      [T("no revel", "not disclos", "no divulg", "sin revelar", "no precis", "no inform", "no detall")]),
    P(4, "Según medios, la inversión es de US$10.000 millones", True, [N(10e9)]),
    P(5, "Azure seguirá siendo el proveedor de nube exclusivo de OpenAI", True, [T("azure"), T("exclusiv")]),
    P(6, "Microsoft invirtió por primera vez en 2019, con US$1.000 millones", False, [N(1e9)]),
    P(7, "Volvió a invertir en 2021", False, [T("2021")]),
    P(8, "ChatGPT se lanzó en noviembre de 2022", False, [MES(11, 2022)]),
    P(9, "OpenAI fue fundada en 2015 como laboratorio sin fines de lucro", False, [T("2015")]),
    P(10, "Microsoft construirá supercomputadoras especializadas para OpenAI", False,
      [T("supercomput")], final=True),
]


# ── construcción de los tests ────────────────────────────────────────────────

def mensajes(prompt, fuente_key):
    f = FUENTES[fuente_key]
    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"FUENTE:\n{f['texto']}"},
    ]


def _descripcion(key):
    plant = PLANTADOS[key]
    final = next((p["texto"] for p in plant if p.get("final")), "—")
    idioma = "inglés" if FUENTES[key]["idioma"] == "en" else "español"
    return (f"Fuente en {idioma} de {len(FUENTES[key]['texto'].split())} palabras con "
            f"{len(plant)} afirmaciones plantadas ({sum(1 for p in plant if p['nucleo'])} de núcleo). "
            f"Enterrada al final: «{final}».")


def construir_tests(prompt=PROMPT_EXTRACCION):
    """Los mismos casos con cualquier prompt (para comparar prompts sin tocar los datos)."""
    from benchmarks.scoring_noticias_claims import normalizar_cifras
    tests = []
    for key in FUENTES:
        tests.append({
            "name": f"extraccion_{key}",
            "description": _descripcion(key),
            "messages": mensajes(prompt, key),
            "expected_answer": {
                "type": "noticias_extraccion",
                "fuente_key": key,
                "plantados": PLANTADOS[key],
                "cifras_fuente": normalizar_cifras(FUENTES[key]["texto"]),
            },
        })
    return tests


TESTS = construir_tests()
