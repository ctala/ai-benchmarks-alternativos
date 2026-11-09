"""Filtro de relevancia de noticias: decidir si una nota es para tu medio, con un criterio escrito.

POR QUÉ EXISTE ESTA SUITE (9-nov-2026)
--------------------------------------
Todo founder que se informa con un flujo automático termina con la misma pieza: un modelo que
lee una nota y decide si pasa o no pasa según un criterio editorial escrito. En Ecosistema
Startup esa pieza es el A-Filtro, y decide qué entra a un medio de startups para founders y VCs
de habla hispana. Pero la decisión es general: cualquiera que filtre noticias, alertas o
comunicados con una regla escrita (un newsletter, un radar de competencia, un canal interno)
necesita lo mismo.

Y se equivoca en **dos direcciones**, igual que `verificar_claim`:

    deja pasar el ruido      → se publica un gadget, un tip de hashtags o la misma ronda dos veces
    bloquea lo que sirve     → se pierde la ronda que llegó por comunicado o con titular de gadget

Por eso la mitad de los casos **debe pasar** y la otra mitad **no**.

QUÉ MIDE
--------
Si el modelo aplica el MISMO criterio escrito a 58 notas, una por test (eran 60; el 9-nov se
quitaron dos casos que admitían las dos lecturas: utilidades de Rappi e inversión de Meta en
EssilorLuxottica):

- ~20 que cumplen con claridad (rondas, adquisiciones, salidas a bolsa, tecnología que un founder
  puede usar, regulación que abre un mercado);
- ~20 que violan con claridad un veto o un rechazo automático (gadget, redes sociales, despidos
  sin ángulo, deportes, celebridades, política, guerra, escándalo, lifestyle, utilidad local,
  clickbait);
- ~20 trampas armadas, que es donde se separan los modelos:
    · duplicado: el mismo hecho que el medio ya publicó, contado por otro medio con otras palabras;
    · hecho nuevo: otra ronda de una empresa ya cubierta (que SÍ pasa);
    · comunicado promocional sin hecho (no pasa) contra comunicado que anuncia una ronda o una
      salida a bolsa con datos (sí pasa) — muchas rondas llegan por comunicado;
    · titular de gadget con cuerpo sobre la ronda o el modelo de negocio (la excepción: pasa);
    · gran tecnológica con ángulo de negocio (pasa) contra sin ángulo (no pasa).

VERDAD POR CONSTRUCCIÓN
-----------------------
Ningún caso se etiquetó «a ojo» ni sale de lo que Eco publicó o descartó: cada uno se escribió
para caer de un lado de UNA regla del criterio, y `expected_answer["regla"]` dice cuál. Los
casos ambiguos se dejaron fuera a propósito. Las notas reales se REESCRIBIERON a partir de hechos
públicos (empresas y cifras reales, sin copiar texto; la URL va en un comentario `# fuente:`).
Las violaciones son texto inventado, con marcas y personas ficticias.

QUÉ NO MIDE
-----------
- Antigüedad de la nota: en producción la resuelve el código antes del modelo, así que el
  criterio le dice al modelo que no evalúe la fecha.
- La categoría editorial (FUNDING, AI_TOOLS…) ni los scores de telemetría: solo la decisión
  binaria que gobierna en producción (`category != SKIP` y `icp_topic_fit == on`).
- La calidad del `motivo`: se pide para auditar, no se puntúa.
- Deduplicación a escala (eso es `noticias_repetidas`): acá la lista de publicadas es corta.

PUNTUACIÓN
----------
Binaria por caso: 10 si la decisión coincide, 0 si no o si no hay decisión parseable
(`benchmarks/scoring_noticias_relevancia.py`). Sin juez: hay verdad objetiva.

El criterio vive en `SISTEMA` y los casos en `CASOS`, separados, para poder aplicar otro prompt
a los mismos casos con `construir_tests(sistema=...)`.
"""

SISTEMA = (
    "Eres el filtro editorial de un medio de noticias sobre startups, tecnología y capital de "
    "riesgo para founders, inversionistas y operadores de habla hispana (América Latina y España). "
    "Recibes UNA nota candidata y la lista de notas que el medio YA publicó. Decides si la nota "
    "pasa a publicación.\n\n"
    "LA PRUEBA: pasa si un founder o un VC podría cambiar una decisión después de leerla. Eso "
    "incluye rondas de inversión, adquisiciones, salidas a bolsa, valoraciones, movimientos "
    "estratégicos de empresas, modelos de negocio, tecnología o herramientas que un founder puede "
    "usar, y regulaciones o licencias que abren un mercado. Las rondas, adquisiciones y salidas a "
    "bolsa de empresas de tecnología pasan, sean de América Latina, de España o de cualquier parte "
    "del mundo. Si un founder o un VC no cambia ninguna decisión después de leerla, no pasa.\n\n"
    "VETO INMEDIATO (no pasa, aunque la fuente sea buena, esté bien escrita y tenga cifras):\n"
    "1. Gadget de consumo: precio, reseña, especificaciones, ranking, lanzamiento o regreso de un "
    "producto para el consumidor final (reloj, teléfono, tablet, consola, audífonos, televisor).\n"
    "2. Tácticas de redes sociales para creadores o marcas: hashtags, alcance, algoritmo, horarios "
    "para publicar, cómo ganar seguidores.\n"
    "3. Despidos o movimientos internos de una gran tecnológica sin ángulo de negocio, producto o "
    "mercado.\n\n"
    "RECHAZO AUTOMÁTICO (no pasa):\n"
    "- Escándalos, casos judiciales y filtraciones sin sustancia tecnológica.\n"
    "- Política partidista y conflictos bélicos, salvo impacto directo en tecnología o startups.\n"
    "- Deportes, entretenimiento y celebridades.\n"
    "- Lifestyle: moda, viajes de lujo, gastronomía, salvo que la nota trate el modelo de negocio "
    "de una startup.\n"
    "- Clickbait sensacionalista sin sustancia.\n"
    "- Utilidad local o del día sin valor duradero: restricciones vehiculares, horarios de "
    "servicios públicos, el «precio hoy» de un producto o de una criptomoneda.\n\n"
    "LA EXCEPCIÓN: la línea es la naturaleza del contenido, no la industria. Si la nota trata el "
    "modelo de negocio, la ronda, la estrategia de mercado o la tecnología que hay detrás de un "
    "producto, SÍ pasa, aunque el titular hable de un teléfono, un anillo o unas gafas.\n\n"
    "COMUNICADOS DE PRENSA: un comunicado puramente promocional, sin un hecho noticioso "
    "(autoelogios, «compromiso con la innovación», nueva identidad de marca, invitación a un "
    "webinar), no pasa. Un comunicado que anuncia una ronda, una adquisición, una salida a bolsa o "
    "un lanzamiento con datos verificables (montos, inversionistas, fechas) SÍ pasa.\n\n"
    "DUPLICADOS: si la nota cuenta el mismo hecho que una nota ya publicada (la misma empresa y el "
    "mismo acontecimiento: la misma ronda, la misma compra, la misma salida a bolsa), es duplicada "
    "y no pasa, aunque venga de otro medio, con otro título y con otras palabras. Un hecho NUEVO "
    "sobre una empresa ya cubierta (otra ronda, otra fecha, otra operación) no es duplicado y se "
    "evalúa normalmente.\n\n"
    "No evalúes la fecha de la nota: la antigüedad se controla en otro paso. El tipo de fuente se "
    "informa solo como contexto: el criterio es el mismo para todas.\n\n"
    "Responde SOLO con un JSON, sin texto adicional:\n"
    '{"decision": "PASA" | "NO_PASA", "motivo": "<una frase>"}'
)

# Lo que el medio ya publicó. Es la MISMA lista en los 60 casos: cinco trampas son el mismo
# hecho que una de estas notas contado por otro medio; tres son un hecho nuevo de la misma
# empresa. Ninguna nota que «cumple» coincide con una de estas.
YA_PUBLICADAS = [
    ("Mistral AI cierra una Serie C de €1.700 millones liderada por ASML",
     "Septiembre de 2025. La ronda valora a la startup francesa en €11.700 millones post-money."),
    ("Google comprará Wiz por US$32.000 millones en efectivo",
     "Marzo de 2025. La startup de ciberseguridad en la nube pasará a Google Cloud."),
    ("Lovable levanta US$200 millones en Serie A y se convierte en unicornio",
     "Julio de 2025. Ronda liderada por Accel con valoración de US$1.800 millones."),
    ("Klarna debuta en la Bolsa de Nueva York tras fijar su precio en US$40 por acción",
     "Septiembre de 2025. La salida a bolsa valoró a la fintech sueca en unos US$15.000 millones."),
    ("Kapital se convierte en unicornio con una Serie C que la valora en US$1.300 millones",
     "Septiembre de 2025. La fintech mexicana cerró la ronda liderada por Tribe Capital."),
    ("Anthropic levanta US$3.500 millones en Serie E con valoración de US$61.500 millones",
     "Marzo de 2025. Ronda liderada por Lightspeed Venture Partners."),
    ("Plata duplica su valoración a US$3.100 millones con una Serie B de US$250 millones",
     "Octubre de 2025. La fintech mexicana suma inversionistas como Kora."),
    ("Cursor levanta US$900 millones con valoración de US$9.900 millones",
     "Junio de 2025. Anysphere, creadora del editor de código Cursor, cerró una ronda liderada "
     "por Thrive Capital."),
    ("OpenAI compra io, la startup de hardware de Jony Ive, por US$6.500 millones",
     "Mayo de 2025. Operación en acciones; el equipo de io se integra a OpenAI."),
]


# Cada caso: id, clase, decisión esperada, regla que lo decide, tipo de fuente, título, texto.
CASOS = [
    # ─────────────────────────── CUMPLE (20) ───────────────────────────
    # fuente: https://techcrunch.com/2025/01/30/elevenlabs-raises-180-million-in-series-c-funding-at-3-3-billion-valuation
    {"id": "cumple_elevenlabs_serie_c", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "ElevenLabs triplica su valoración a US$3.300 millones con una Serie C de US$180 millones",
     "texto": "La startup de voz con inteligencia artificial ElevenLabs cerró una Serie C de US$180 "
              "millones, coliderada por Andreessen Horowitz e ICONIQ Growth, con una valoración "
              "post-money de US$3.300 millones, el triple que un año antes. Fundada en 2022, la "
              "empresa suma US$281 millones en cuatro rondas y destinará el capital a investigación "
              "de voz, herramientas para empresas y expansión global."},
    # fuente: https://www.axios.com/2025/07/31/figma-ipo-stock-adobe
    {"id": "cumple_figma_ipo", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Figma sale a bolsa a US$33 por acción y recauda unos US$1.200 millones",
     "texto": "Figma fijó el precio de su salida a bolsa en US$33 por acción, por encima del rango "
              "que había revisado al alza, y empezó a cotizar en la Bolsa de Nueva York con el "
              "símbolo FIG. La operación recaudó unos US$1.200 millones y valoró a la empresa de "
              "diseño colaborativo en cerca de US$19.300 millones. La acción abrió a US$85 en su "
              "primer día, un año y medio después de que se cayera su venta a Adobe."},
    # fuente: https://www.theregister.com/2025/08/05/openai_open_gpt/
    {"id": "cumple_openai_gpt_oss", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "oficiales",
     "titulo": "OpenAI publica gpt-oss: dos modelos de pesos abiertos con licencia Apache 2.0",
     "texto": "OpenAI liberó gpt-oss-120b y gpt-oss-20b, sus primeros modelos de lenguaje con pesos "
              "abiertos desde GPT-2, bajo licencia Apache 2.0. Son modelos de razonamiento con "
              "arquitectura de mezcla de expertos y ventana de 128.000 tokens; el de 20.000 millones "
              "de parámetros corre con 16 GB de memoria. Se pueden descargar en Hugging Face y usar "
              "en Azure, AWS y Databricks, lo que permite correrlos en infraestructura propia."},
    # fuente: https://blog.cloudflare.com/introducing-pay-per-crawl/
    {"id": "cumple_cloudflare_pay_per_crawl", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "oficiales",
     "titulo": "Cloudflare lanza «pay per crawl» para cobrar a los rastreadores de IA",
     "texto": "Cloudflare presentó en beta privada «pay per crawl», un sistema para que los sitios "
              "cobren a los rastreadores de inteligencia artificial por acceder a su contenido. El "
              "editor fija una tarifa por solicitud y define qué rastreadores permite, cobra o "
              "bloquea; Cloudflare actúa como intermediario del cobro. El mismo día anunció que su "
              "red bloqueará por defecto a los rastreadores de IA."},
    # fuente: https://sg.finance.yahoo.com/news/spains-factorial-raises-120-million-112457527.html
    {"id": "cumple_factorial_unicornio", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "alertas",
     "titulo": "Factorial levanta US$120 millones y se convierte en unicornio",
     "texto": "La startup barcelonesa de software de recursos humanos Factorial cerró una Serie C de "
              "US$120 millones liderada por el fondo Atomico, con una valoración de US$1.000 "
              "millones. La empresa vende a pymes un sistema para gestionar nómina, vacaciones y "
              "evaluaciones, y usará el capital para crecer en nuevos mercados."},
    # fuente: https://www.theblock.co/news/business/2025-11-24-revolut-75-billion-usd-valuation-380141
    {"id": "cumple_revolut_75b", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Revolut alcanza una valoración de US$75.000 millones tras su venta secundaria",
     "texto": "Revolut completó una venta secundaria de acciones que la valora en US$75.000 "
              "millones, un 66 % más que su valoración anterior de US$45.000 millones. La operación "
              "fue liderada por Coatue, Greenoaks, Dragoneer y Fidelity. La compañía no informó el "
              "monto total de la venta."},
    # fuente: https://www.bloomberglinea.com/latinoamerica/mexico/nu-mexico-recibe-licencia-para-convertirse-en-banco-en-mexico/
    {"id": "cumple_nubank_licencia_mexico", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "alertas",
     "titulo": "Nu México recibe licencia para convertirse en banco",
     "texto": "Nu México, filial de Nubank, obtuvo la aprobación de las autoridades mexicanas para "
              "operar como banco, tras una solicitud presentada ante la CNBV en octubre de 2023. La "
              "licencia le permitirá ampliar su oferta de productos en el país, uno de los "
              "mercados donde compite con otras fintech como Plata, Klar y Mercado Pago."},
    # fuente: https://techcrunch.com/2025/04/14/hugging-face-buys-a-humanoid-robotics-startup
    {"id": "cumple_huggingface_pollen", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Hugging Face compra Pollen Robotics y entra al hardware",
     "texto": "Hugging Face adquirió por un monto no revelado a Pollen Robotics, startup francesa "
              "creadora del humanoide Reachy 2. Es su primera compra de hardware. El software del "
              "robot es de código abierto, se programa en Python y corre modelos de la librería "
              "LeRobot de Hugging Face, que apuesta a llevar la IA abierta al mundo físico."},
    # fuente: https://yourstory.com/2024/12/databricks-raises-10b-series-j-investment-at-62b-valuation
    {"id": "cumple_databricks_serie_j", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Databricks levanta US$10.000 millones con valoración de US$62.000 millones",
     "texto": "Databricks anunció una Serie J de US$10.000 millones liderada por Thrive Capital, con "
              "una valoración de US$62.000 millones, 44 % más que en su ronda de 2023. La empresa "
              "de datos e IA invertirá en nuevos productos, adquisiciones y expansión internacional, "
              "y prevé superar US$3.000 millones de ingresos anualizados con flujo de caja libre "
              "positivo."},
    # fuente: https://coreweave.com/news/coreweave-announces-pricing-of-initial-public-offering
    {"id": "cumple_coreweave_ipo", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "CoreWeave sale al Nasdaq a US$40 por acción, por debajo de lo esperado",
     "texto": "El proveedor de nube para inteligencia artificial CoreWeave fijó el precio de su "
              "salida a bolsa en US$40 por acción, por debajo del rango de US$47 a US$55 que había "
              "indicado, y recaudó US$1.500 millones con 37,5 millones de acciones. Cotiza en el "
              "Nasdaq con el símbolo CRWV. Es una de las primeras salidas a bolsa grandes de "
              "infraestructura de IA."},
    # fuente: https://decrypt.co/323795/stablecoin-giant-circle-raises-1-billion-ipo-nyse-debut
    {"id": "cumple_circle_ipo", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "agregador",
     "titulo": "Circle, emisora de USDC, recauda US$1.100 millones en su salida a bolsa",
     "texto": "Circle, la empresa detrás de la stablecoin USDC, fijó su precio de salida a bolsa en "
              "US$31 por acción, por encima del rango previsto, y recaudó unos US$1.100 millones en "
              "la Bolsa de Nueva York con el símbolo CRCL. La operación valoró a la compañía en "
              "cerca de US$6.900 millones."},
    # fuente: https://techcrunch.com/2025/07/15/mira-muratis-thinking-machines-lab-is-worth-12b-in-seed-round/
    {"id": "cumple_thinking_machines_seed", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Thinking Machines Lab, de Mira Murati, cierra una semilla de US$2.000 millones",
     "texto": "Thinking Machines Lab, la startup de IA fundada por la exdirectora de tecnología de "
              "OpenAI Mira Murati, cerró una ronda semilla de US$2.000 millones liderada por "
              "Andreessen Horowitz, con una valoración de US$12.000 millones. Participaron también "
              "Nvidia, AMD, Accel y Cisco. Según reportes, Murati conserva derechos de voto en el "
              "directorio superiores a los del resto combinado."},
    # fuente: https://businesstoday.in/technology/news/story/openai-lands-historic-40-billion-investment-led-by-softbank-hits-300-billion-valuation-amid-ai-boom-470093-2025-04-01
    {"id": "cumple_openai_40b_softbank", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "OpenAI levanta hasta US$40.000 millones liderados por SoftBank",
     "texto": "OpenAI anunció una ronda de hasta US$40.000 millones liderada por SoftBank, con una "
              "valoración post-money de US$300.000 millones. Una parte se entrega de inmediato y el "
              "resto queda condicionado a la reestructuración de la empresa. Participan también "
              "Microsoft, Coatue, Altimeter y Thrive Capital."},
    # fuente: https://www.bloomberglinea.com/latinoamerica/mexico/klar-suma-a-santander-televisa-y-grupo-formula-como-inversionistas-en-ronda-de-us190-millones/
    {"id": "cumple_klar_190m", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "alertas",
     "titulo": "Klar levanta US$190 millones y suma a Santander y Televisa como inversionistas",
     "texto": "La fintech mexicana Klar, que ofrece cuenta digital y crédito, anunció una ronda de "
              "US$190 millones —US$170 millones en capital y US$20 millones en deuda— que la valora "
              "en más de US$800 millones. La lideró General Atlantic y se sumaron Grupo Santander, "
              "Grupo Televisa y Grupo Fórmula. La empresa usará el capital para crecer en México."},
    # fuente: https://builtin.com/articles/harvey-raises-300m-series-e-20250626
    {"id": "cumple_harvey_serie_e", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Harvey, la IA para abogados, levanta US$300 millones a US$5.000 millones",
     "texto": "Harvey, startup de inteligencia artificial para firmas de abogados, cerró una Serie E "
              "de US$300 millones coliderada por Kleiner Perkins y Coatue, con una valoración de "
              "US$5.000 millones. Llega cuatro meses después de su Serie D de US$300 millones a "
              "US$3.000 millones, una señal del apetito inversor por la IA vertical."},
    # fuente: https://stripe.com/in/newsroom/news/employee-liquidity-feb-2025
    {"id": "cumple_stripe_tender_2025", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Stripe se valora en US$91.500 millones en una oferta de compra para empleados",
     "texto": "Stripe anunció una oferta de compra de acciones para dar liquidez a empleados actuales "
              "y antiguos, con inversionistas que compran a una valoración de US$91.500 millones. "
              "La cifra la acerca a su máximo de US$95.000 millones de 2021 y, según analistas, "
              "aleja la urgencia de salir a bolsa."},
    # fuente: https://www.bloomberglinea.com/latinoamerica/argentina/ante-la-presencia-de-milei-uala-anuncia-la-mayor-ronda-de-inversion-privada-de-la-region-en-tres-anos/
    {"id": "cumple_uala_serie_e", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "alertas",
     "titulo": "Ualá cierra una ronda de US$300 millones liderada por Allianz X",
     "texto": "La fintech argentina Ualá anunció una Serie E de US$300 millones liderada por Allianz "
              "X, el brazo inversor de Allianz, con una valoración de US$2.750 millones. Es la mayor "
              "ronda privada de la región en tres años, y la empresa la destinará a crecer en "
              "México, Argentina y Colombia."},
    # fuente: https://www.nasdaq.com/articles/meta-invests-143-bln-scale-ai-taps-ceo-alexandr-wang-lead-superintelligence-push
    {"id": "cumple_meta_scale_ai", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Meta invierte US$14.300 millones por el 49 % de Scale AI",
     "texto": "Meta tomará una participación sin derecho a voto del 49 % en Scale AI, la startup de "
              "etiquetado de datos para entrenar modelos, por US$14.300 millones, lo que la valora "
              "en US$29.000 millones. Su fundador, Alexandr Wang, se suma a Meta para liderar su "
              "trabajo en superinteligencia. Es la segunda operación más grande de Meta después de "
              "WhatsApp."},
    # fuente: https://www.maginative.com/article/cognition-acquires-windsurf-after-googles-talent-raid-left-it-gutted/
    {"id": "cumple_cognition_windsurf", "clase": "cumple", "decision": "PASA",
     "regla": "prueba_founder_vc", "fuente_tipo": "medios",
     "titulo": "Cognition compra Windsurf días después de que Google se llevara a su CEO",
     "texto": "Cognition, creadora del agente de programación Devin, compró la propiedad "
              "intelectual, el producto, la marca y el equipo restante de Windsurf, por un monto no "
              "revelado. Windsurf tenía US$82 millones de ingresos recurrentes anuales y más de 350 "
              "clientes empresariales. Cognition aceleró el vesting de todos los empleados, a "
              "diferencia del acuerdo previo con Google."},

    # ─────────────────────────── VIOLA (20) ── texto inventado, marcas y personas ficticias ───
    # fuente: inventada
    {"id": "viola_gadget_reloj_resena", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_gadget", "fuente_tipo": "medios",
     "titulo": "Reseña del Vela Watch S3: el reloj inteligente de US$229 que dura 10 días",
     "texto": "Probamos durante dos semanas el Vela Watch S3. La pantalla AMOLED de 1,4 pulgadas se "
              "ve bien a pleno sol, la batería llegó a 10 días con uso moderado y el sensor de "
              "ritmo cardíaco es preciso. Cuesta US$229 y viene en tres colores. Lo peor: la correa "
              "de silicona se ensucia rápido. Veredicto: 8 de 10."},
    # fuente: inventada
    {"id": "viola_gadget_ranking_audifonos", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_gadget", "fuente_tipo": "agregador",
     "titulo": "Los cinco mejores audífonos con cancelación de ruido para comprar este año",
     "texto": "Comparamos cinco modelos de audífonos inalámbricos con cancelación activa de ruido. "
              "El primero gana por autonomía (40 horas), el segundo por comodidad y el tercero por "
              "relación precio-calidad. Te contamos cuál conviene según tu presupuesto, desde US$79 "
              "hasta US$399."},
    # fuente: inventada
    {"id": "viola_gadget_consola_specs", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_gadget", "fuente_tipo": "medios",
     "titulo": "Consola portátil Nimbus Go: fecha de venta, precio y especificaciones",
     "texto": "La Nimbus Go llegará a tiendas el 15 de marzo a US$449. Tendrá pantalla de 7 "
              "pulgadas a 120 Hz, 512 GB de almacenamiento, ranura microSD y batería de 6.000 mAh. "
              "Se podrá reservar desde la próxima semana y vendrá con dos juegos incluidos."},
    # fuente: inventada
    {"id": "viola_gadget_tv_vale_la_pena", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_gadget", "fuente_tipo": "alertas",
     "titulo": "Televisor OLED de 65 pulgadas baja de precio: ¿vale la pena?",
     "texto": "El televisor OLED de 65 pulgadas de una conocida marca coreana bajó un 20 % en "
              "tiendas en línea. Repasamos su brillo, sus puertos HDMI 2.1 y su sistema operativo "
              "para que decidas si es buen momento para cambiar tu tele antes del próximo mundial."},
    # fuente: inventada
    {"id": "viola_redes_hashtags_instagram", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_redes", "fuente_tipo": "medios",
     "titulo": "Hashtags en Instagram: cuántos usar para ganar alcance",
     "texto": "El algoritmo de Instagram cambió y los hashtags ya no funcionan como antes. Los "
              "expertos recomiendan usar entre tres y cinco, mezclar etiquetas de nicho con otras "
              "populares y ponerlas en la descripción y no en los comentarios. Así puedes recuperar "
              "el alcance de tus publicaciones."},
    # fuente: inventada
    {"id": "viola_redes_hora_tiktok", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_redes", "fuente_tipo": "agregador",
     "titulo": "La mejor hora para publicar en TikTok, según el algoritmo",
     "texto": "Si quieres más vistas, publica entre las 19:00 y las 21:00 de martes a jueves. Los "
              "primeros 30 minutos son clave para que el algoritmo empuje tu video: responde "
              "comentarios rápido, usa sonidos en tendencia y no borres videos que no despegaron."},
    # fuente: inventada
    {"id": "viola_redes_seguidores_facebook", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_redes", "fuente_tipo": "alertas",
     "titulo": "Diez trucos para ganar seguidores en tu página de Facebook",
     "texto": "Publica todos los días, usa imágenes con caras, haz preguntas al final de cada "
              "publicación y organiza sorteos. Con estos diez trucos tu página puede sumar mil "
              "seguidores al mes sin pagar publicidad."},
    # fuente: inventada
    {"id": "viola_despidos_orbis_voz", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_despidos", "fuente_tipo": "medios",
     "titulo": "Orbis Tech elimina 180 puestos en su división de asistentes de voz",
     "texto": "Orbis Tech, la tecnológica estadounidense de 170.000 empleados, despidió a 180 "
              "personas de su división de asistentes de voz, según un correo interno. La empresa "
              "no dio más detalles ni explicó los motivos, y dijo que los afectados recibirán una "
              "indemnización."},
    # fuente: inventada
    {"id": "viola_movimiento_interno_orbis", "clase": "viola", "decision": "NO_PASA",
     "regla": "veto_despidos", "fuente_tipo": "agregador",
     "titulo": "La directora de diseño de interfaces de Orbis Tech deja la empresa tras 12 años",
     "texto": "La directora de diseño de interfaces de Orbis Tech anunció en su perfil profesional "
              "que deja la compañía después de 12 años. Agradeció a su equipo y dijo que se tomará "
              "unos meses de descanso antes de decidir su próximo paso. Orbis Tech no ha nombrado "
              "reemplazo."},
    # fuente: inventada
    {"id": "viola_deportes_fichaje", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_deportes_entretenimiento_celebridades", "fuente_tipo": "medios",
     "titulo": "El delantero del momento firma con un club europeo por 60 millones de euros",
     "texto": "El delantero uruguayo de 22 años firmó contrato por cinco temporadas con un club de la "
              "liga española, que pagó 60 millones de euros por su pase. Debutará el próximo fin "
              "de semana y llevará la camiseta número 9."},
    # fuente: inventada
    {"id": "viola_entretenimiento_trailer", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_deportes_entretenimiento_celebridades", "fuente_tipo": "agregador",
     "titulo": "Sale el tráiler de la cuarta temporada de la serie de dragones más vista",
     "texto": "La plataforma de streaming publicó el tráiler de la cuarta temporada, que se estrena "
              "en abril. Vuelven los protagonistas, hay dos dragones nuevos y una batalla que, "
              "según los fans, será la más larga de la saga."},
    # fuente: inventada
    {"id": "viola_celebridad_boda", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_deportes_entretenimiento_celebridades", "fuente_tipo": "alertas",
     "titulo": "La cantante Marina Solé se casa en una isla del Caribe",
     "texto": "La cantante Marina Solé se casó con su pareja de hace cinco años en una ceremonia "
              "privada en una isla del Caribe. Asistieron 80 invitados, entre ellos varios actores, "
              "y el vestido fue de una diseñadora italiana."},
    # fuente: inventada
    {"id": "viola_politica_debate", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_politica_guerra", "fuente_tipo": "medios",
     "titulo": "Los candidatos a la alcaldía se acusan de mentir en el último debate",
     "texto": "El último debate antes de la elección municipal terminó con acusaciones cruzadas "
              "entre los dos candidatos punteros por las cifras de seguridad y de transporte. Las "
              "encuestas los muestran empatados a una semana de la votación."},
    # fuente: inventada
    {"id": "viola_guerra_frontera", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_politica_guerra", "fuente_tipo": "agregador",
     "titulo": "Se intensifican los combates en la zona fronteriza",
     "texto": "Los combates entre los dos ejércitos se intensificaron durante la noche en la zona "
              "fronteriza. Las autoridades locales informaron desplazamientos de población y "
              "cortes de carreteras. Organismos internacionales pidieron un alto el fuego."},
    # fuente: inventada
    {"id": "viola_escandalo_filtracion", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_escandalo", "fuente_tipo": "alertas",
     "titulo": "Filtran los mensajes del actor en pleno juicio de divorcio",
     "texto": "Un portal de espectáculos publicó mensajes privados atribuidos a un conocido actor, "
              "que forman parte de su juicio de divorcio. La defensa del actor pidió investigar la "
              "filtración y el juez fijó una nueva audiencia para el próximo mes."},
    # fuente: inventada
    {"id": "viola_lifestyle_restaurante", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_lifestyle", "fuente_tipo": "medios",
     "titulo": "Abre en Madrid el restaurante con menú degustación de 300 euros",
     "texto": "El chef con dos estrellas abrió su nuevo restaurante en Madrid: 18 mesas, un menú "
              "degustación de 14 pasos por 300 euros y una carta de vinos de 900 referencias. Las "
              "reservas para los próximos tres meses ya están agotadas."},
    # fuente: inventada
    {"id": "viola_lifestyle_moda", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_lifestyle", "fuente_tipo": "agregador",
     "titulo": "Las cinco tendencias de moda que vas a ver este verano",
     "texto": "Colores pastel, lino, sandalias planas, bolsos de mimbre y gafas de sol grandes. "
              "Estas son las cinco tendencias que dominan las pasarelas y cómo combinarlas en tu "
              "día a día sin gastar de más."},
    # fuente: inventada
    {"id": "viola_utilidad_hoy_no_circula", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_utilidad_local", "fuente_tipo": "alertas",
     "titulo": "Hoy No Circula: qué autos descansan este jueves en la capital",
     "texto": "Este jueves no circulan los vehículos con engomado verde y terminación de placa 1 y "
              "2, de 5:00 a 22:00 horas. Te decimos qué hologramas están exentos y cuánto es la "
              "multa si te detienen."},
    # fuente: inventada
    {"id": "viola_utilidad_precio_bitcoin", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_utilidad_local", "fuente_tipo": "agregador",
     "titulo": "Precio del bitcoin hoy: así abre la cotización este martes",
     "texto": "El bitcoin abre este martes con una baja de 1,2 % en las últimas 24 horas. Te "
              "mostramos la cotización en dólares, en pesos mexicanos y en euros, y cómo se movió "
              "frente a ethereum durante la última semana."},
    # fuente: inventada
    {"id": "viola_clickbait_truco_celular", "clase": "viola", "decision": "NO_PASA",
     "regla": "rechazo_clickbait", "fuente_tipo": "agregador",
     "titulo": "Este truco del celular que nadie conoce te va a dejar con la boca abierta",
     "texto": "No vas a creer lo que pasa cuando presionas tres veces este botón. Miles de personas "
              "ya lo probaron y quedaron sorprendidas. Te lo contamos al final de la nota."},

    # ─────────────────────────── TRAMPAS (20) ───────────────────────────
    # Duplicado: el mismo hecho que una nota de YA_PUBLICADAS, contado por otro medio.
    # fuente: https://sifted.eu/articles/mistral-confirms-series-c-asml
    {"id": "trampa_dup_mistral_asml", "clase": "trampa_duplicado", "decision": "NO_PASA",
     "regla": "duplicado", "fuente_tipo": "medios",
     "titulo": "ASML se convierte en el mayor accionista de Mistral AI",
     "texto": "El fabricante neerlandés de equipos para chips ASML invirtió €1.300 millones en "
              "Mistral AI y quedó con cerca del 11 % de la empresa, como líder de una Serie C de "
              "€1.700 millones que valora a la startup francesa en €11.700 millones. El director "
              "financiero de ASML entrará al comité estratégico de Mistral."},
    # fuente: https://www.itpro.com/business/business-strategy/google-confirms-wiz-acquisition-in-record-breaking-usd32-billion-deal
    {"id": "trampa_dup_wiz_google", "clase": "trampa_duplicado", "decision": "NO_PASA",
     "regla": "duplicado", "fuente_tipo": "agregador",
     "titulo": "Wiz acepta venderse a Google: la mayor compra de la historia del buscador",
     "texto": "Wiz, la startup de seguridad en la nube que en 2024 había rechazado una oferta de "
              "US$23.000 millones, aceptó la propuesta de Google de unos US$32.000 millones en "
              "efectivo. Supera los US$12.500 millones que Google pagó por Motorola en 2012. La "
              "empresa se integrará a Google Cloud."},
    # fuente: https://tech.eu/2025/07/17/lovable-annointed-europes-latest-unicorn-following-200m-funding-round/
    {"id": "trampa_dup_lovable_unicornio", "clase": "trampa_duplicado", "decision": "NO_PASA",
     "regla": "duplicado", "fuente_tipo": "medios",
     "titulo": "La sueca Lovable ya vale US$1.800 millones a ocho meses de su lanzamiento",
     "texto": "Lovable, la plataforma sueca para crear aplicaciones describiéndolas en lenguaje "
              "natural, cerró la mayor Serie A de la historia de Suecia: US$200 millones liderados "
              "por Accel. Su ingreso recurrente anual llegó a US$75 millones en siete meses."},
    # fuente: https://fortune.com/2025/09/11/swedish-bnpl-giant-klarna-biggest-ipo-2025-nyse
    {"id": "trampa_dup_klarna_ipo", "clase": "trampa_duplicado", "decision": "NO_PASA",
     "regla": "duplicado", "fuente_tipo": "agregador",
     "titulo": "Las acciones de Klarna abren a US$52 en su estreno en Wall Street",
     "texto": "La fintech de «compra ahora, paga después» Klarna empezó a cotizar en la Bolsa de "
              "Nueva York con el símbolo KLAR. Había fijado su precio en US$40 por acción, por "
              "encima del rango de US$35 a US$37, y la acción abrió a US$52 en su primer día."},
    # fuente: https://expansion.mx/economia/2025/09/02/kapital-bank-se-convierte-en-unicornio
    {"id": "trampa_dup_kapital_unicornio", "clase": "trampa_duplicado", "decision": "NO_PASA",
     "regla": "duplicado", "fuente_tipo": "alertas",
     "titulo": "Kapital, el nuevo unicornio mexicano tras una ronda liderada por Tribe Capital",
     "texto": "La fintech Kapital alcanzó una valuación de US$1.300 millones con su Serie C, "
              "liderada por Tribe Capital y coliderada por Pelion Ventures, con participación de "
              "Y Combinator. Su director general la describió como una ronda previa a una futura "
              "salida a bolsa en Nueva York."},

    # Hecho nuevo sobre una empresa ya cubierta: otra ronda, otra fecha. SÍ pasa.
    # fuente: https://builtin.com/articles/anthropic-raises-13b-series-f-183b-valuation-20250902
    {"id": "trampa_nuevo_anthropic_serie_f", "clase": "trampa_hecho_nuevo", "decision": "PASA",
     "regla": "hecho_nuevo_misma_empresa", "fuente_tipo": "medios",
     "titulo": "Anthropic levanta US$13.000 millones y triplica su valoración a US$183.000 millones",
     "texto": "Anthropic cerró en septiembre de 2025 una Serie F de US$13.000 millones liderada por "
              "ICONIQ, con Fidelity y Lightspeed, a una valoración post-money de US$183.000 "
              "millones. Es casi el triple de los US$61.500 millones de su Serie E de marzo. Sus "
              "ingresos anualizados pasaron de unos US$1.000 millones a más de US$5.000 millones "
              "en ocho meses."},
    # fuente: https://www.bloomberglinea.com/latinoamerica/mexico/banco-plata-recauda-us405-millones-y-logra-valuacion-record-en-america-latina/
    {"id": "trampa_nuevo_plata_serie_c", "clase": "trampa_hecho_nuevo", "decision": "PASA",
     "regla": "hecho_nuevo_misma_empresa", "fuente_tipo": "alertas",
     "titulo": "Plata recauda US$405 millones y alcanza una valuación de US$5.000 millones",
     "texto": "La fintech mexicana Plata cerró en abril de 2026 una Serie C de US$405 millones "
              "liderada por Bicycle Capital, que la valora en US$5.000 millones. Seis meses antes "
              "había levantado una Serie B de US$250 millones a US$3.100 millones. La empresa, "
              "que obtuvo licencia bancaria, se prepara para operar como banco digital."},
    # fuente: https://www.businesswire.com/news/home/20251113939996/en
    {"id": "trampa_nuevo_cursor_serie_d", "clase": "trampa_hecho_nuevo", "decision": "PASA",
     "regla": "hecho_nuevo_misma_empresa", "fuente_tipo": "comunicado",
     "titulo": "Cursor cierra una Serie D de US$2.300 millones con valoración de US$29.300 millones",
     "texto": "Cursor anunció en noviembre de 2025 una Serie D de US$2.300 millones coliderada por "
              "Accel y Coatue, con una valoración post-money de US$29.300 millones. Participan "
              "también Google, Nvidia, Thrive y Andreessen Horowitz. La empresa dijo que sus "
              "ingresos anualizados superaron US$1.000 millones. Su Serie C, de junio, había sido "
              "de US$900 millones a US$9.900 millones."},

    # Comunicado promocional sin hecho noticioso (texto inventado, empresas ficticias). NO pasa.
    # fuente: inventada
    {"id": "trampa_comunicado_promo_compromiso", "clase": "trampa_comunicado_promocional",
     "decision": "NO_PASA", "regla": "comunicado_promocional", "fuente_tipo": "comunicado",
     "titulo": "NovaPay reafirma su compromiso con la innovación financiera en América Latina",
     "texto": "COMUNICADO DE PRENSA. NovaPay, empresa líder en soluciones de pago, reafirma su "
              "compromiso con la innovación y con la transformación digital de la región. «Somos "
              "pioneros en poner al cliente en el centro y seguiremos liderando el cambio», afirmó "
              "su director general. NovaPay ofrece soluciones integrales, seguras y escalables "
              "para empresas de todos los tamaños."},
    # fuente: inventada
    {"id": "trampa_comunicado_promo_marca", "clase": "trampa_comunicado_promocional",
     "decision": "NO_PASA", "regla": "comunicado_promocional", "fuente_tipo": "comunicado",
     "titulo": "Grupo Altamira presenta su nueva identidad de marca",
     "texto": "COMUNICADO DE PRENSA. Grupo Altamira presenta su nueva identidad visual, que refleja "
              "su espíritu innovador, cercano y sustentable. El nuevo logotipo y la nueva paleta "
              "de colores acompañarán a la compañía en esta etapa de crecimiento y consolidación. "
              "«Nuestra marca evoluciona con nosotros», señaló su directora de marketing."},
    # fuente: inventada
    {"id": "trampa_comunicado_promo_webinar", "clase": "trampa_comunicado_promocional",
     "decision": "NO_PASA", "regla": "comunicado_promocional", "fuente_tipo": "comunicado",
     "titulo": "Lumen Cloud invita a su webinar «El futuro de la IA en tu empresa»",
     "texto": "COMUNICADO DE PRENSA. Lumen Cloud, referente en soluciones en la nube, invita a "
              "líderes de negocio a su webinar gratuito «El futuro de la IA en tu empresa», el "
              "próximo jueves a las 10:00. Expertos de la compañía compartirán su visión sobre "
              "las tendencias que transformarán la industria. Cupos limitados; inscríbete en el "
              "sitio de Lumen Cloud."},

    # Comunicado CON hecho noticioso verificable: SÍ pasa.
    # fuente: https://www.businesswire.com/news/home/20210726005214/en/5018188/Food-Tech-Pioneer-NotCo-Announces-235M-Series-D-Round-at-1.5-Billion-Valuation
    {"id": "trampa_comunicado_hecho_notco", "clase": "trampa_comunicado_con_hecho",
     "decision": "PASA", "regla": "comunicado_con_hecho", "fuente_tipo": "comunicado",
     "titulo": "NotCo anuncia una Serie D de US$235 millones con valoración de US$1.500 millones",
     "texto": "COMUNICADO DE PRENSA. La foodtech chilena NotCo, que usa inteligencia artificial "
              "para desarrollar alimentos de origen vegetal, anuncia una Serie D de US$235 millones "
              "liderada por Tiger Global, con una valoración de US$1.500 millones. Participan DFJ "
              "Growth, ZOMA Lab, Lewis Hamilton y Roger Federer. NotCo suma más de US$350 millones "
              "levantados y usará el capital para entrar a nuevas categorías en Norteamérica y "
              "lanzar en Europa y Asia."},
    # fuente: https://www.businesswire.com/news/home/20210610005759/en/
    {"id": "trampa_comunicado_hecho_clip", "clase": "trampa_comunicado_con_hecho",
     "decision": "PASA", "regla": "comunicado_con_hecho", "fuente_tipo": "comunicado",
     "titulo": "Clip recibe una inversión de US$250 millones liderada por SoftBank y Viking",
     "texto": "COMUNICADO DE PRENSA. Clip, la plataforma mexicana de pagos digitales para pequeños "
              "comercios, anuncia una inversión de capital de US$250 millones liderada por el "
              "SoftBank Latin America Fund y Viking Global Investors, que eleva su valoración a "
              "cerca de US$2.000 millones. La empresa usará los recursos para ampliar su oferta "
              "de pagos y servicios financieros en México."},
    # fuente: https://www.businesswire.com/news/home/20250611283865/en/Chime-Announces-Pricing-of-Initial-Public-Offering
    {"id": "trampa_comunicado_hecho_chime", "clase": "trampa_comunicado_con_hecho",
     "decision": "PASA", "regla": "comunicado_con_hecho", "fuente_tipo": "comunicado",
     "titulo": "Chime anuncia el precio de su oferta pública inicial",
     "texto": "COMUNICADO DE PRENSA. Chime Financial anuncia el precio de su oferta pública "
              "inicial: 32 millones de acciones Clase A a US$27 cada una, por encima del rango de "
              "US$24 a US$26, por un total de US$864 millones. Las acciones empezarán a cotizar en "
              "el Nasdaq Global Select Market con el símbolo CHYM. Morgan Stanley, Goldman Sachs y "
              "J.P. Morgan actúan como coordinadores."},

    # Titular de gadget, cuerpo sobre la ronda o el modelo de negocio: la excepción. SÍ pasa.
    # fuente: https://technode.com/2025/09/16/nothing-raises-200m-in-series-c-to-advance-ai-native-consumer-devices/
    {"id": "trampa_gadget_nothing_ronda", "clase": "trampa_titular_gadget", "decision": "PASA",
     "regla": "excepcion_negocio_detras", "fuente_tipo": "medios",
     "titulo": "El teléfono transparente de Nothing ya vale US$1.300 millones",
     "texto": "Detrás del teléfono de carcasa transparente hay un negocio que acaba de levantar "
              "US$200 millones: Nothing cerró una Serie C liderada por Tiger Global, con Qualcomm "
              "Ventures y GV, a una valoración de US$1.300 millones. La empresa londinense superó "
              "US$1.000 millones en ventas acumuladas tras crecer 150 % en 2024, y usará el capital "
              "para construir una plataforma de dispositivos con IA nativa en 2026. Además abrirá "
              "una ronda comunitaria a la misma valoración."},
    # fuente: https://www.fiercehealthcare.com/health-tech/oura-raises-900m-series-e-oura-ring-sales-catapult
    {"id": "trampa_gadget_oura_ronda", "clase": "trampa_titular_gadget", "decision": "PASA",
     "regla": "excepcion_negocio_detras", "fuente_tipo": "medios",
     "titulo": "El anillo inteligente Oura: una apuesta de US$11.000 millones",
     "texto": "Oura, el fabricante finlandés del anillo que mide sueño y actividad, levantó una "
              "Serie E de US$900 millones liderada por Fidelity, con ICONIQ, que la valora en unos "
              "US$11.000 millones, más del doble que en diciembre de 2024. La empresa facturó más "
              "de US$500 millones en 2024 y espera superar US$1.000 millones en 2025, con un "
              "modelo que combina la venta del anillo con una suscripción mensual."},

    # Gran tecnológica: con ángulo de negocio pasa; sin ángulo, no.
    # fuente: https://www.scmp.com/tech/big-tech/article/3330714/microsoft-holds-27-openai-revamped-partnership
    {"id": "trampa_bigtech_microsoft_openai", "clase": "trampa_bigtech_con_angulo",
     "decision": "PASA", "regla": "bigtech_con_angulo", "fuente_tipo": "medios",
     "titulo": "Microsoft se queda con el 27 % de OpenAI en un nuevo acuerdo",
     "texto": "Microsoft y OpenAI firmaron un nuevo acuerdo: la parte con fines de lucro de OpenAI "
              "pasa a ser una corporación de beneficio público y Microsoft queda con cerca del 27 %, "
              "valorado en unos US$135.000 millones. Microsoft conserva derechos sobre la propiedad "
              "intelectual de los modelos hasta 2032, OpenAI se compromete a comprar US$250.000 "
              "millones adicionales en Azure y Microsoft pierde el derecho preferente como "
              "proveedor de cómputo."},
    # fuente: https://www.etcentric.org/cognition-acquires-windsurf-following-google-licensing-deal/
    {"id": "trampa_bigtech_google_windsurf", "clase": "trampa_bigtech_con_angulo",
     "decision": "PASA", "regla": "bigtech_con_angulo", "fuente_tipo": "medios",
     "titulo": "Google paga US$2.400 millones por la tecnología y el CEO de Windsurf",
     "texto": "Google pagó unos US$2.400 millones para licenciar de forma no exclusiva la tecnología "
              "de Windsurf, el editor de código con IA, y contratar a su CEO y parte del equipo, "
              "sin tomar participación en la empresa. El acuerdo llegó después de que se cayera "
              "una compra de Windsurf por OpenAI de unos US$3.000 millones. Es un ejemplo del "
              "formato «licencia más contratación» que usan las grandes para evitar una compra."},
    # fuente: inventada
    {"id": "trampa_bigtech_orbis_cafeteria", "clase": "trampa_bigtech_sin_angulo",
     "decision": "NO_PASA", "regla": "bigtech_sin_angulo", "fuente_tipo": "agregador",
     "titulo": "Orbis Tech renueva el menú de las cafeterías de su campus",
     "texto": "Orbis Tech, la tecnológica estadounidense de 170.000 empleados, renovó el menú de las "
              "cafeterías de su campus principal: suma opciones veganas, un día temático de comida "
              "asiática y una máquina de café de especialidad por edificio. Los empleados podrán "
              "votar cada mes el plato del día."},
]


def _bloque_publicadas():
    lineas = [f"{i}. {t} — {r}" for i, (t, r) in enumerate(YA_PUBLICADAS, 1)]
    return "NOTAS YA PUBLICADAS POR EL MEDIO:\n" + "\n".join(lineas)


def _mensaje_usuario(caso):
    return (
        f"NOTA CANDIDATA\n"
        f"Tipo de fuente: {caso['fuente_tipo']}\n"
        f"Título: {caso['titulo']}\n"
        f"Texto:\n{caso['texto']}\n\n"
        f"{_bloque_publicadas()}"
    )


def construir_tests(sistema=SISTEMA, casos=None):
    """Arma la lista TESTS. Permite aplicar otro criterio (`sistema`) a los mismos casos."""
    casos = CASOS if casos is None else casos
    tests = []
    for c in casos:
        tests.append({
            "name": c["id"],
            "description": f"[{c['clase']}] {c['titulo']} → {c['decision']} ({c['regla']})",
            "messages": [
                {"role": "system", "content": sistema},
                {"role": "user", "content": _mensaje_usuario(c)},
            ],
            "expected_answer": {
                "type": "noticias_relevancia",
                "decision": c["decision"],
                "clase": c["clase"],
                "regla": c["regla"],
            },
        })
    return tests


TESTS = construir_tests()
