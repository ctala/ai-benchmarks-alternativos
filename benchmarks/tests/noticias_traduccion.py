"""
Noticias · traducción de fragmentos CJK — reparar la fuga sin reescribir la nota.

POR QUÉ EXISTE (9-nov-2026)
---------------------------
La fuga de CJK es un fallo real de producción (ver `integridad_idioma`): un modelo
escribe la nota en español y mete «硬件» o «直接» en medio. El pipeline de Ecosistema
Startup la repara con un paso dedicado («Traducir fragmentos»): un modelo barato recibe
la frase con el trozo en chino, japonés o coreano y tiene que traducir SOLO ese trozo.

Ese paso falla de tres formas que cualquier founder con un pipeline de contenido
reconoce: deja el CJK (o lo pone entre paréntesis «por si acaso»), aprovecha para
reescribir la frase entera —y entonces la nota verificada ya no es la que se publica—,
o traduce mal el término o la cifra (亿 = 100 millones, no un millón).

DISEÑO
------
  · 15 párrafos en español neutro con 1-3 fragmentos CJK incrustados: nombres de
    empresas (se transliteran), términos técnicos simples y, en cuatro casos, una cifra
    dentro del fragmento (5亿美元, 10億円, 100억 원, 增长了30%).
  · Solo términos de traducción inequívoca y verificable; cada fragmento trae su lista
    de equivalentes aceptados.
  · Verdad objetiva, sin juez: cero CJK, el resto del párrafo intacto (tolerancia de
    espacios y puntuación de borde), el término esperado en el hueco del fragmento y la
    cifra preservada. Fórmula en `benchmarks/scoring_noticias_redaccion.py`
    (`type: noticias_traduccion`).
  · Prompt común en `PROMPT`; los casos son datos.
"""

SYSTEM_PROMPT = "Eres editor de una publicación digital en español neutro para emprendedores."

PROMPT = """Este párrafo de una nota en español tiene fragmentos en chino, japonés o coreano que se colaron por error. Devuelve el párrafo completo con SOLO esos fragmentos traducidos al español neutro; si un fragmento es un nombre propio, translitéralo al alfabeto latino. No cambies nada más del párrafo. Responde solo con el párrafo.

{parrafo}"""

# Cada caso: name, parrafo, fragmentos [{cjk, aceptados}], cifras (valores que deben quedar).
CASOS = [
    {"name": "xiaomi_auto", "parrafo": "La empresa china 小米 presentó su primer auto eléctrico en Pekín y abrió las reservas el mismo día.",
     "fragmentos": [{"cjk": "小米", "aceptados": ["Xiaomi"]}], "cifras": []},
    {"name": "ia_pymes", "parrafo": "Según el informe, el uso de 人工智能 en las pymes de la región creció durante el último año.",
     "fragmentos": [{"cjk": "人工智能", "aceptados": ["inteligencia artificial", "IA"]}], "cifras": []},
    {"name": "ronda_yi_dolares", "parrafo": "La startup cerró una ronda de 5亿美元 liderada por fondos locales, la más grande del sector este año.",
     "fragmentos": [{"cjk": "5亿美元", "aceptados": ["500 millones de dólares", "500 millones", "US$500M", "USD 500M"]}],
     "cifras": [500e6]},
    {"name": "softbank_latam", "parrafo": "La japonesa ソフトバンク anunció una nueva inversión en startups de América Latina.",
     "fragmentos": [{"cjk": "ソフトバンク", "aceptados": ["SoftBank"]}], "cifras": []},
    {"name": "samsung_semiconductores", "parrafo": "El fabricante 삼성전자 informó que sus ventas de 반도체 se recuperaron en el trimestre.",
     "fragmentos": [{"cjk": "삼성전자", "aceptados": ["Samsung Electronics", "Samsung"]},
                    {"cjk": "반도체", "aceptados": ["semiconductores", "semiconductor", "chips"]}], "cifras": []},
    {"name": "centros_de_datos", "parrafo": "Los nuevos 数据中心 de la compañía se construirán en el norte de México.",
     "fragmentos": [{"cjk": "数据中心", "aceptados": ["centros de datos", "centro de datos", "data centers"]}], "cifras": []},
    {"name": "toyota_oku_yenes", "parrafo": "La automotriz トヨタ destinará 10億円 a un programa de baterías en Japón.",
     "fragmentos": [{"cjk": "トヨタ", "aceptados": ["Toyota"]},
                    {"cjk": "10億円", "aceptados": ["1.000 millones de yenes", "mil millones de yenes", "1000 millones de yenes",
                                                   "1.000 millones", "mil millones"]}],
     "cifras": [1e9]},
    {"name": "kakao_eok_wones", "parrafo": "La plataforma 카카오 recibió 100억 원 para expandir su servicio de pagos.",
     "fragmentos": [{"cjk": "카카오", "aceptados": ["Kakao"]},
                    {"cjk": "100억 원", "aceptados": ["10.000 millones de wones", "diez mil millones de wones",
                                                     "10 mil millones de wones", "10.000 millones de won", "10.000 millones"]}],
     "cifras": [1e10]},
    {"name": "alibaba_codigo_abierto", "parrafo": "El gigante 阿里巴巴 lanzó un modelo de 开源 que cualquier desarrollador puede descargar.",
     "fragmentos": [{"cjk": "阿里巴巴", "aceptados": ["Alibaba"]},
                    {"cjk": "开源", "aceptados": ["código abierto", "open source"]}], "cifras": []},
    {"name": "huawei_chips", "parrafo": "La caída afectó a 华为 y a otros fabricantes de 芯片 de la región.",
     "fragmentos": [{"cjk": "华为", "aceptados": ["Huawei"]},
                    {"cjk": "芯片", "aceptados": ["chips", "semiconductores", "microchips"]}], "cifras": []},
    {"name": "autos_electricos_pct", "parrafo": "Las ventas de 电动汽车 en China 增长了30% en el primer semestre, según la asociación del sector.",
     "fragmentos": [{"cjk": "电动汽车", "aceptados": ["autos eléctricos", "vehículos eléctricos", "coches eléctricos",
                                                    "carros eléctricos", "automóviles eléctricos"]},
                    {"cjk": "增长了30%", "aceptados": ["crecieron", "aumentaron", "subieron", "se incrementaron", "crecimiento"]}],
     "cifras": [30]},
    {"name": "rakuten_tokio", "parrafo": "El servicio de 楽天 ya acepta pagos con código QR en tiendas de 東京.",
     "fragmentos": [{"cjk": "楽天", "aceptados": ["Rakuten"]},
                    {"cjk": "東京", "aceptados": ["Tokio", "Tokyo"]}], "cifras": []},
    {"name": "naver_ia_seul", "parrafo": "La empresa 네이버 abrió un laboratorio de 인공지능 en 서울 para investigar modelos de lenguaje.",
     "fragmentos": [{"cjk": "네이버", "aceptados": ["Naver"]},
                    {"cjk": "인공지능", "aceptados": ["inteligencia artificial", "IA"]},
                    {"cjk": "서울", "aceptados": ["Seúl", "Seoul"]}], "cifras": []},
    {"name": "bytedance_usuarios", "parrafo": "Los 用户 de la aplicación de 字节跳动 podrán comprar sin salir del video.",
     "fragmentos": [{"cjk": "用户", "aceptados": ["usuarios"]},
                    {"cjk": "字节跳动", "aceptados": ["ByteDance"]}], "cifras": []},
    {"name": "sony_robot", "parrafo": "La división de 人工知能 de ソニー presentó un robot para atención en tiendas.",
     "fragmentos": [{"cjk": "人工知能", "aceptados": ["inteligencia artificial", "IA"]},
                    {"cjk": "ソニー", "aceptados": ["Sony"]}], "cifras": []},
]

TESTS = [
    {
        "name": f"traducir_{c['name']}",
        "description": f"Traducir solo {len(c['fragmentos'])} fragmento(s) CJK sin reescribir el párrafo",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT.format(parrafo=c["parrafo"])},
        ],
        "expected_answer": {
            "type": "noticias_traduccion",
            "original": c["parrafo"],
            "fragmentos": c["fragmentos"],
            "cifras": c["cifras"],
        },
    }
    for c in CASOS
]
