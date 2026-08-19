#!/usr/bin/env python3
"""Una página por modelo: lo que NOSOTROS medimos, y un enlace a lo que mide el fabricante.

POR QUÉ EXISTE (17-ago-2026)
----------------------------
Cristian: *"deberíamos tener 'Cards' páginas de los modelos con las comparaciones
oficiales y las nuestras. Y en caso de que el modelo esté en HuggingFace u otro lado,
simplemente enviar al link correspondiente. Nosotros no queremos competir con ellos,
queremos otra cosa, lo que realmente funciona para el emprendedor latino."*

Ese último punto es el diseño entero de esta página, y conviene decirlo explícito porque
es tentador hacer lo contrario: **no replicamos el benchmark oficial**. MMLU, GPQA,
SWE-bench y la tabla de lanzamiento están en HuggingFace y en el sitio del fabricante,
hechas por gente con más recursos y con acceso al modelo antes que nadie. Copiarlas acá
sería competir en el terreno donde no tenemos nada que agregar — y encima quedarían
desactualizadas.

Lo que sí tenemos, y nadie más publica: **qué pasa cuando ese modelo tiene que decidir
algo de un negocio hispanohablante chico**. Verificar un dato contra su fuente antes de
publicarlo. Emitir el JSON que un workflow espera. Llamar la herramienta correcta.
Escribir en español que no suene traducido. A un precio que un emprendedor puede pagar.

Así que la card manda al oficial para lo oficial, y se queda con lo suyo.

QUÉ EVITA
---------
**Nunca inventa una URL.** Un enlace roto en una página pública es peor que no tener
enlace: se ve como descuido y manda al lector a un 404. Por eso el enlace a los pesos
sale de `weights_url` —declarado a mano, verificado— y el del proveedor se construye
solo cuando es determinístico (`openrouter.ai/<id>` lo es, porque el id ES la ruta).
Si no hay ninguno de los dos, la sección no se dibuja.

Uso:  python benchmarks/generate_model_cards.py
"""

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

from benchmarks.generate_comparison import esc, page_shell  # noqa: E402
from benchmarks.suites import SUITES, pilar_del_promedio  # noqa: E402
from contrato_pagina import emitir  # noqa: E402

SITE = "https://benchmarks.cristiantala.com"
DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"
PILARES = ("Coding", "Contenido", "Razonamiento", "Agentes")

# ── el fondo, tal cual el Manual de Marca v2 ─────────────────────────────────
#
# Copiado literal de `~/Playground/brand-manuals/cristian-tala/manual-v2.html` (el repo
# local del manual, que es la fuente; `assets.cristiantala.com/brand/ctala.html` es su
# publicación). Dos radiales —morado arriba-izquierda, cyan abajo-derecha— y un grid de
# perspectiva enmascarado hacia arriba.
#
# Los colores NO se escriben a mano acá: son los tokens del manual (`--color-purple`
# #7a00df y `--color-cyan` #00d4ff) con la misma opacidad. La regla del repo padre es
# clara: nunca inventar un color de marca.
BRAND_CSS = """<style>
  .hero { position: relative; overflow: hidden; }
  .hero::before {
    content: ''; position: absolute; inset: 0; pointer-events: none; z-index: 0;
    background:
      radial-gradient(ellipse 70% 60% at 12% 8%, rgba(122,0,223,.28) 0%, transparent 60%),
      radial-gradient(ellipse 60% 50% at 92% 95%, rgba(0,212,255,.10) 0%, transparent 55%);
  }
  .hero::after {
    content: ''; position: absolute; inset: 0; pointer-events: none; z-index: 0;
    background-image:
      linear-gradient(rgba(122,0,223,.18) 1px, transparent 1px),
      linear-gradient(90deg, rgba(122,0,223,.18) 1px, transparent 1px);
    background-size: 64px 64px;
    -webkit-mask-image: linear-gradient(to top, #000 0%, transparent 75%);
    mask-image: linear-gradient(to top, #000 0%, transparent 75%);
  }
  .hero > * { position: relative; z-index: 1; }

  /* ── Tira de KPIs: lo que se responde sin bajar ──────────────────────────
     Una tabla de 15 filas trata «puesto #45» y «ventana de contexto» como si
     pesaran lo mismo. No pesan igual: cuatro números deciden si el modelo
     entra a la lista corta, y el resto es para cuando ya entró. */
  .kpi-strip { display: grid; grid-template-columns: repeat(2, 1fr); gap: .75rem;
               margin: 1.75rem 0 1.25rem; }
  @media (min-width: 720px) { .kpi-strip { grid-template-columns: repeat(4, 1fr); } }
  .kpi { background: var(--bg-card); border: 1px solid var(--border); border-radius: 10px;
         padding: 1rem 1.1rem; position: relative; overflow: hidden; }
  .kpi::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 3px;
                 background: var(--green); opacity: .8; }
  .kpi.is-cyan::before { background: var(--cyan); }
  .kpi.is-magenta::before { background: var(--magenta); }
  .kpi .k-label { font-family: 'JetBrains Mono', monospace; font-size: .66rem;
                  letter-spacing: .09em; text-transform: uppercase; color: var(--gray);
                  display: block; margin-bottom: .4rem; }
  .kpi .k-value { font-family: 'JetBrains Mono', monospace; font-size: 1.7rem;
                  font-weight: 700; color: var(--white); line-height: 1.05; display: block; }
  .kpi .k-value .k-unit { font-size: .9rem; color: var(--gray); font-weight: 400; }
  .kpi .k-sub { font-size: .72rem; color: var(--gray); display: block; margin-top: .35rem; }

  /* ── Badges: propiedades binarias, que en una tabla ocupan una fila cada una */
  .badges { display: flex; flex-wrap: wrap; gap: .45rem; margin: 0 0 2rem; }
  .badge { font-family: 'JetBrains Mono', monospace; font-size: .68rem; letter-spacing: .04em;
           padding: .32rem .65rem; border-radius: 999px; border: 1px solid var(--border);
           color: var(--gray-dark); background: rgba(255,255,255,.02); }
  .badge.on { color: var(--green); border-color: rgba(57,255,20,.34); background: rgba(57,255,20,.07); }
  .badge.info { color: var(--cyan); border-color: rgba(0,212,255,.30); background: rgba(0,212,255,.06); }
  .badge.warn { color: var(--magenta); border-color: rgba(255,0,110,.34); background: rgba(255,0,110,.07); }

  /* ── Perfil por pilar: una nota suelta no dice nada sin la población al lado.
     La marca vertical es la MEDIANA de los rankeados en ese pilar, así que la
     barra se lee como «arriba o abajo del resto», no como un 0-10 abstracto. */
  .perfil { margin: 0 0 2.25rem; }
  .bar-row { display: grid; grid-template-columns: 1fr auto; gap: .25rem .9rem;
             margin-bottom: 1.15rem; align-items: center; }
  @media (min-width: 720px) { .bar-row { grid-template-columns: 10.5rem 1fr auto; } }
  .bar-row .b-label { font-family: 'JetBrains Mono', monospace; font-size: .78rem;
                      color: var(--white); }
  .bar-track { position: relative; height: 10px; background: rgba(255,255,255,.06);
               border-radius: 999px; grid-column: 1 / -1; }
  @media (min-width: 720px) { .bar-track { grid-column: auto; } }
  .bar-fill { position: absolute; left: 0; top: 0; bottom: 0; border-radius: 999px;
              background: linear-gradient(90deg, var(--cyan), var(--green)); }
  /* 19-ago-2026: era magenta. Un 8,71 sobre 10 se pintaba del mismo rojo que un
     error, porque queda 0,35 bajo la MEDIANA de un grupo que entero cabe en 1,4
     puntos. El color decía «reprobado» de un número muy bueno. Hoy el verde marca
     lo que sobresale y el resto es neutro: estar bajo la mediana de esta población
     no es una falla, es el promedio. */
  .bar-fill.bajo { background: linear-gradient(90deg, #3a3a4e, #6f7690); }
  .bar-median { position: absolute; top: -5px; bottom: -5px; width: 2px;
                background: var(--gray); opacity: .7; }
  .bar-row .b-val { font-family: 'JetBrains Mono', monospace; font-size: .82rem;
                    font-weight: 700; color: var(--green); white-space: nowrap; }
  .bar-row .b-val.bajo { color: var(--muted); }
  .bar-row .b-val .delta { color: var(--gray); font-weight: 400; font-size: .72rem; }
  .perfil .leyenda { font-size: .75rem; color: var(--gray); margin-top: -.35rem; }

  /* ── Tabla agrupada: el mismo dato, pero sabiendo de qué habla cada bloque */
  .results-table tr.grupo th { font-family: 'JetBrains Mono', monospace; font-size: .68rem;
        letter-spacing: .11em; text-transform: uppercase; color: var(--cyan);
        padding-top: 1.35rem; background: transparent; }
  .results-table td .riesgo { color: var(--magenta); font-weight: 700; }
  .results-table td .bien { color: var(--green); font-weight: 700; }
</style>"""


def slug(m: dict) -> str:
    """El `key` ya es kebab-case y es ESTABLE: es lo que identifica al modelo en todo el
    repo. Usarlo como ruta evita que renombrar un modelo cambie su URL — que es cómo se
    pierde el posicionamiento de una página que ya indexó."""
    return m["key"].replace("/", "-").replace(" ", "-").lower()


def _n(v, d=2):
    return "—" if v is None else f"{v:.{d}f}"


def cal_pilar(m: dict, pilar: str):
    """La CALIDAD del modelo en ese pilar — sin costo ni velocidad adentro.

    NO usar `score_by_pillar`: viene pre-horneado con costo y velocidad, y para un modelo
    caro eso hunde un pilar donde es excelente. Medido: Claude Opus 4.8 marca 7,91 en
    Coding por `score_by_pillar` (#56 de 83) y **9,24 de calidad pura** — es de los
    mejores programando, sólo que caro y lento. Publicar el compuesto como si fuera
    habilidad haría que la ficha desaconseje un modelo por la razón equivocada.

    Es el principio que este repo ya adoptó de Artificial Analysis: costo y velocidad se
    reportan APARTE del índice de calidad. La ficha los muestra en su propia fila.
    """
    d = (m.get("dims_by_pillar") or {}).get(pilar) or {}
    return d.get("quality_avg")


def _usd(v):
    if v is None:
        return "—"
    return f"${v:,.3f}" if v < 1 else f"${v:,.2f}"


# ── el veredicto: para qué sirve ESTE, dicho en una línea ─────────────────────
def veredicto(m: dict, ranked: list) -> str:
    """Lo primero que lee alguien que llegó buscando «¿sirve X?».

    Se arma del contraste con la población, no de adjetivos: en qué pilar está más
    arriba de su propia media y qué le cuesta. Un modelo no es «bueno» — es bueno EN
    algo y a un precio.
    """
    medidos = {p: cal_pilar(m, p) for p in PILARES if cal_pilar(m, p) is not None}
    if not medidos:
        return "Medido, pero sin cobertura suficiente en los pilares para dar un veredicto."
    mejor = max(medidos, key=medidos.get)
    peor = min(medidos, key=medidos.get)
    # su puesto en ese pilar, entre los rankeados que lo tienen medido
    conp = [x for x in ranked if cal_pilar(x, mejor) is not None]
    conp.sort(key=lambda x: -cal_pilar(x, mejor))
    pos = next((i + 1 for i, x in enumerate(conp) if x["key"] == m["key"]), None)
    coste = m.get("cost_per_1k_calls_usd")
    baratos = sorted(x.get("cost_per_1k_calls_usd") or 0 for x in ranked
                     if x.get("cost_per_1k_calls_usd"))
    barato = coste is not None and baratos and coste <= baratos[len(baratos) // 3]

    # «Su fuerte es X» dicho de un modelo que está #66 de 83 en X es una mentira por
    # omisión: el pilar es su mejor RELATIVO y su peor ABSOLUTO al mismo tiempo. El
    # lector entiende «acá es bueno» y no lo es. Se dice según dónde cae de verdad.
    if pos and pos <= len(conp) / 3:
        frase = f"Su fuerte es <strong>{mejor}</strong>"
    elif pos and pos > len(conp) * 2 / 3:
        frase = f"Lo mejor que tiene es <strong>{mejor}</strong>, y aun así queda abajo"
    else:
        frase = f"Donde mejor rinde es <strong>{mejor}</strong>"
    if pos:
        frase += f" (#{pos} de {len(conp)} entre los que rinden el examen completo)"
    frase += f", y donde menos rinde es <strong>{peor}</strong>"
    if len(medidos) > 1:
        frase += f" ({_n(medidos[peor])} contra {_n(medidos[mejor])})"
    frase += ". "
    if barato:
        frase += (f"Está en el tercio más barato del ranking: {_usd(coste)} por cada "
                  f"1.000 llamadas.")
    elif coste is not None:
        frase += f"Cuesta {_usd(coste)} por cada 1.000 llamadas."
    return frase


# ── lo que se responde sin bajar: cuatro números y las propiedades binarias ───
# El uso típico con el que se traduce el precio a plata mensual.
#
# 50 llamadas al día es un workflow de n8n corriendo cada media hora en horario hábil, o
# un agente que atiende el feed dos veces al día con varias vueltas cada vez — la escala
# real del ICP de este benchmark, no la de una empresa con tráfico. Se declara acá porque
# el número aparece en 91 fichas: cambiarlo a ojo en una sola sería publicar dos verdades.
LLAMADAS_DIA = 50
LLAMADAS_MES = LLAMADAS_DIA * 30


def kpis(m: dict, puesto: int | None, total: int, ranked: list) -> str:
    """Los cuatro que deciden si el modelo entra a la lista corta.

    El percentil va al lado del puesto porque «#45 de 83» no dice lo mismo en un
    ranking de 83 que en uno de 500, y quien llega desde una búsqueda no tiene el
    tamaño de la población en la cabeza.
    """
    tiles = []
    # 19-ago-2026 · POR QUÉ LA CALIDAD VA PRIMERA Y EL PUESTO ES SU SUBTÍTULO.
    #
    # Hasta hoy el tile #1, el más grande y el primero que se lee, era «Puesto global
    # #59 de 91 · mejor que el 36% de los rankeados». Un founder lee eso y cierra la
    # pestaña — y se va con la conclusión equivocada, porque ese mismo modelo saca 8,21
    # sobre 10 y es #3 de 91 en Contenido.
    #
    # El puesto global comprime en 91 posiciones una población que ENTERA cabe en ~1,4
    # puntos: es la misma trampa que hizo abandonar el z-score en v4.1, servida en el
    # lugar más visible de la página. Es información legítima, así que no se borra: baja
    # a subtítulo y viaja con el dato que desarma la mala lectura (el rango real).
    q = m.get("quality_avg")
    if q is not None:
        qs = sorted((x.get("quality_avg") or 0) for x in ranked if x.get("quality_avg"))
        # El rango se MIDE, no se escribe a mano: cambia con cada modelo nuevo.
        rango = (qs[-1] - qs[0]) if len(qs) > 1 else 0
        sub = f"#{puesto} de {total}" if puesto else f"{sum(1 for x in qs if x > q)} por encima"
        if rango:
            sub += f" · del mejor al peor hay {rango:.1f} puntos"
        tiles.append(("", "Nota de calidad", f"{q:.2f}<span class=\"k-unit\">/10</span>", sub))
    c = m.get("cost_per_1k_calls_usd")
    if c is not None:
        cs = sorted(x.get("cost_per_1k_calls_usd") or 0 for x in ranked
                    if x.get("cost_per_1k_calls_usd"))
        mas_caros = len(cs) - sum(1 for x in cs if x < c) - 1
        # «más barato que 7 de 91» es una forma cortés de decir que es el 8º más caro, y
        # obliga a hacer la resta. Si está en la mitad cara, se dice derecho.
        sub = (f"el {mas_caros + 1}º más caro de {len(cs)}" if mas_caros < len(cs) / 2
               else f"más barato que {mas_caros} de {len(cs)}")
        tiles.append(("is-cyan", "Por 1.000 llamadas", _usd(c), sub))
        # Un founder no razona en «1.000 llamadas»: razona en cuánto le llega a fin de
        # mes. El supuesto va escrito en el tile — es una estimación, y una estimación
        # sin su supuesto a la vista es un número inventado.
        tiles.append(("is-cyan", "Al mes, uso típico",
                      _usd(c * LLAMADAS_MES / 1000),
                      f"{LLAMADAS_DIA} llamadas por día, todos los días"))
    v = m.get("tokens_per_second")
    if v:
        lat = m.get("latency_avg_s")
        tiles.append(("is-cyan", "Velocidad", f"{v:.0f}<span class=\"k-unit\"> tok/s</span>",
                      "—" if not lat else f"{lat:.1f} s de espera media"))
    html = "\n    ".join(
        f'<div class="kpi {cls}"><span class="k-label">{esc(lab)}</span>'
        f'<span class="k-value">{val}</span><span class="k-sub">{esc(sub)}</span></div>'
        for cls, lab, val, sub in tiles)

    # Las binarias: en una tabla ocupan una fila cada una y se leen como si pesaran
    # lo mismo que la calidad. Acá se escanean de un vistazo y no roban jerarquía.
    b = []
    if m.get("open_source"):
        b.append(("on", f"⬡ Open source{' · ' + m['license'] if m.get('license') else ''}"))
    else:
        b.append(("", "⬡ Propietario"))
    # 19-ago-2026 · los badges dicen la capacidad, no su nombre técnico.
    #
    # Decían «Tool calling», «Multimodal», «1000K de contexto» y «Prompt injection
    # 8.7/10». Los cuatro son correctos y los cuatro son opacos para quien viene a
    # decidir qué modelo pone en su n8n: no sabe si 8.7 en prompt injection es bueno,
    # ni qué hace con un contexto de 1000K. El término técnico queda entre paréntesis
    # —el que lo busca lo encuentra, y el que no, igual entiende qué compra.
    b.append(("on" if m.get("tool_calling") else "",
              "⚒ Puede usar herramientas" if m.get("tool_calling")
              else "⚒ No usa herramientas (sin tool calling)"))
    if m.get("multimodal"):
        b.append(("info", "◨ Entiende imágenes"))
    if m.get("thinking"):
        b.append(("info", "◈ Razona antes de responder"))
    if m.get("context_window"):
        k = m["context_window"] // 1000
        # ~750 palabras por cada 1.000 tokens, ~450 palabras por página. Se redondea a
        # dos cifras significativas a propósito: «~1.666 páginas» suena a medición y es
        # una regla de tres. Lo que se comunica es el ORDEN DE MAGNITUD.
        pags = m["context_window"] * 0.75 / 450
        paso = 10 ** max(0, len(str(int(pags))) - 2)
        b.append(("info", f"⌸ Le caben ~{round(pags / paso) * paso:,.0f}".replace(",", ".")
                  + " páginas a la vez"))
    sec = m.get("security_score")
    if sec is not None:
        # «Prompt injection» es el ataque; lo que importa es si AGUANTA. Y 8.7 sin
        # escala no dice nada: se agrega el veredicto en una palabra.
        # «Resiste» / «Cae ante», no «aguanta»: aguantar algo se puede leer como
        # tolerarlo, que es justo lo contrario de lo que mide la nota.
        v = "Resiste bien" if sec >= 8 else "Resiste" if sec >= 7 else "Cae ante"
        b.append(("on" if sec >= 7 else "warn",
                  f"⛨ {v} instrucciones ocultas · {sec:.1f}/10"))
    badges = "\n    ".join(f'<span class="badge {c}">{esc(t)}</span>' for c, t in b)
    return f"""  <div class="kpi-strip">
    {html}
  </div>
  <div class="badges">
    {badges}
  </div>"""


# ── perfil por pilar: la nota, pero contra la población ──────────────────────
def perfil(m: dict, ranked: list) -> str:
    """Cuatro números en una tabla no dicen dónde brilla: hay que restarlos de
    memoria. La barra los ordena sola, y la marca vertical —la mediana de los
    rankeados en ese pilar— convierte «8,33» en «arriba o abajo del resto»."""
    filas = []
    for p in PILARES:
        v = cal_pilar(m, p)
        if v is None:
            continue
        pob = sorted(x for x in (cal_pilar(o, p) for o in ranked) if x is not None)
        if not pob:
            continue
        med = pob[len(pob) // 2]
        # Escala acotada al rango real de la población: en 0-10 todas las barras
        # se ven llenas y no se distingue nada (la población entera cabe en ~1,4).
        lo, hi = pob[0], pob[-1]
        span = max(hi - lo, 0.01)
        pct = max(4, min(100, 100 * (v - lo + span * .06) / (span * 1.06)))
        pmed = 100 * (med - lo + span * .06) / (span * 1.06)
        bajo = v < med
        d = v - med
        filas.append(f"""    <div class="bar-row">
      <span class="b-label">{esc(p)}</span>
      <span class="bar-track"><span class="bar-fill{' bajo' if bajo else ''}" style="width:{pct:.1f}%"></span><span class="bar-median" style="left:{pmed:.1f}%"></span></span>
      <span class="b-val{' bajo' if bajo else ''}">{_n(v)} <span class="delta">({d:+.2f} vs mediana)</span></span>
    </div>""")
    if not filas:
        return ""
    return f"""  <section class="perfil">
    <h2>Dónde está parado, pilar por pilar</h2>
    <p class="leyenda"><strong>La nota de la derecha es sobre 10.</strong> La barra
    compara contra los demás modelos del ranking, no contra el cero: entre el mejor y el
    peor de esta lista hay poco más de un punto, así que en escala 0-10 se verían todas
    iguales. La marca vertical es la <strong>mediana</strong> — quedar por debajo acá no
    es una mala nota, es estar en el promedio de un grupo muy parejo.</p>
{chr(10).join(filas)}
  </section>"""


# ── la ficha: nuestros números, sin adornos ──────────────────────────────────
def ficha(m: dict, puesto: int | None, total: int) -> str:
    """El detalle, agrupado por lo que responde. Sin los cuatro que ya están
    arriba en la tira ni los pilares que ya están en las barras: repetirlos
    llenaría la tabla de ruido que el lector acaba de leer."""
    grupos = [
        ("Calidad medida", [
            ("Runs que puntúan", str(m.get("runs") or 0)),
            ("Tool calling", _n(m.get("tool_calling_score_avg"))),
        ]),
        ("Precio", [
            ("Precio por millón · entrada", _usd(m.get("cost_input_per_M"))),
            ("Precio por millón · salida", _usd(m.get("cost_output_per_M"))),
        ]),
        ("Rendimiento y límites", [
            ("Latencia total media",
             "—" if not m.get("latency_avg_s") else f"{m['latency_avg_s']:.1f} s"),
            ("Ventana de contexto",
             "—" if not m.get("context_window") else f"{m['context_window']:,}".replace(",", ".")),
        ]),
    ]
    if m.get("effective_context"):
        grupos[2][1].append(("Contexto útil medido",
                             f"{m['effective_context']:,}".replace(",", ".")))
    if m.get("security_score") is not None:
        s = m["security_score"]
        cls = "bien" if s >= 7 else "riesgo"
        grupos[0][1].append(("Resistencia a prompt injection",
                             f'<span class="{cls}">{_n(s)}</span>'))
    out = []
    for titulo, filas in grupos:
        if not filas:
            continue
        out.append(f'<tr class="grupo"><th scope="col" colspan="2">{esc(titulo)}</th></tr>')
        for k, v in filas:
            out.append(f'<tr><th scope="row">{esc(k)}</th><td>{v}</td></tr>')
    tr = "\n        ".join(out)
    return f"""  <section class="results">
    <div class="results-header">
      <h2>La ficha: {esc(m['name'])} en números</h2>
      <p class="meta">Todo esto sale de runs propios, guardados y auditables. La latencia es
      la <strong>total</strong> de respuesta, no el time-to-first-token.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <tbody>
        {tr}
      </tbody>
    </table></div>
  </section>"""


# ── contra los frontier: la pregunta que se hace cualquiera ──────────────────
def contra_frontier(m: dict, ranked: list) -> str:
    """*"Algo sencillo para que un humano común entienda las diferencias contra los
    modelos frontier"* (Cristian, 17-ago-2026).

    La comparación honesta para quien paga no es «cuánto le falta para ser GPT-5»:
    es **cuánto más caro es el frontier por cuánta más calidad**. Esa razón —veces
    más caro contra puntos más de nota— es lo que decide si conviene, y es la que
    nunca aparece en la tabla de un lanzamiento.

    Quién es «frontier» no se elige a dedo: es el de MÁS CALIDAD medida (el techo
    real de la población) y el MÁS CARO del top 10 por calidad (el que la gente
    tiene en la cabeza cuando dice «lo mejor»). Los dos salen del dato, así que la
    sección no envejece cuando cambia el ranking.
    """
    q, c = m.get("quality_avg"), m.get("cost_per_1k_calls_usd")
    if q is None or not c:
        return ""
    otros = [x for x in ranked if x["key"] != m["key"] and x.get("quality_avg")]
    if not otros:
        return ""
    mejor = max(otros, key=lambda x: x["quality_avg"])
    top10 = sorted(otros, key=lambda x: -x["quality_avg"])[:10]
    caro = max(top10, key=lambda x: x.get("cost_per_1k_calls_usd") or 0)

    filas, notas = [], []
    for x, etiqueta in ((m, "Este modelo"), (mejor, "El de más calidad medida"),
                        (caro, "El frontier más caro del top 10")):
        xq, xc = x.get("quality_avg"), x.get("cost_per_1k_calls_usd")
        destacar = ' style="color:var(--green);font-weight:700"' if x["key"] == m["key"] else ""
        filas.append(
            f'<tr><td><strong{destacar}>{esc(x["name"])}</strong><br>'
            f'<span class="meta">{esc(etiqueta)}</span></td>'
            f'<td>{_n(xq)}</td><td>{_usd(xc)}</td></tr>')

    def frase(x, como):
        xq, xc = x.get("quality_avg"), x.get("cost_per_1k_calls_usd")
        if x["key"] == m["key"] or not xc:
            return None
        dq = xq - q
        veces = xc / c if c else 0
        if dq <= 0.005:  # empata o le gana
            if veces > 1.15:
                return (f"<strong>{esc(x['name'])}</strong> ({como}) cuesta "
                        f"<strong>{veces:.0f} veces más</strong> y no rinde más: "
                        f"{_n(xq)} contra {_n(q)}.")
            return (f"<strong>{esc(x['name'])}</strong> ({como}) no le saca ventaja de "
                    f"calidad: {_n(xq)} contra {_n(q)}.")
        pct = 100 * dq / q
        if veces >= 1.15:
            return (f"<strong>{esc(x['name'])}</strong> ({como}) rinde "
                    f"<strong>{pct:.0f}% más</strong> ({_n(xq)} contra {_n(q)}) y cuesta "
                    f"<strong>{veces:.0f} veces más</strong> por llamada.")
        if veces <= 0.87:
            return (f"<strong>{esc(x['name'])}</strong> ({como}) rinde {pct:.0f}% más "
                    f"<em>y además</em> es más barato: {_usd(xc)} contra {_usd(c)}. "
                    f"Acá no hay que elegir.")
        return (f"<strong>{esc(x['name'])}</strong> ({como}) rinde {pct:.0f}% más a un "
                f"precio parecido ({_usd(xc)} contra {_usd(c)}).")

    for x, como in ((mejor, "el techo medido"), (caro, "el caro que todos conocen")):
        f = frase(x, como)
        if f and f not in notas:
            notas.append(f)
    lis = "\n      ".join(f"<li>{n}</li>" for n in notas)

    return f"""  <section class="results">
    <div class="results-header">
      <h2>Contra los mejores del ranking, en plata</h2>
      <p class="meta">La pregunta útil no es cuánto le falta a {esc(m['name'])} para ser
      el mejor: es <strong>cuánta calidad extra estás comprando, y a cuántas veces el
      precio</strong>. Eso es lo que decide si conviene.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Calidad</th><th scope="col">$/1.000 llamadas</th></tr></thead>
      <tbody>
        {chr(10).join('        ' + f for f in filas).strip()}
      </tbody>
    </table></div>
    <ul>
      {lis}
    </ul>
    <p class="meta">Los tres salen de las mismas 29 tareas, el mismo juez y los mismos
    límites. Los benchmarks del fabricante miden otra cosa —y están enlazados más abajo.</p>
  </section>"""


# ── el presupuesto de salida: el dato que evita el fallo silencioso ──────────
def presupuesto(m: dict) -> str:
    """Cuántos tokens de salida hay que darle a este modelo, POR TAREA.

    POR QUÉ ESTÁ EN LA FICHA (17-ago-2026)
    --------------------------------------
    Cristian, después de que el gate de noticias de Eco fallara con el modelo que este
    benchmark recomendó: *"de alguna manera tenemos que dar esa información de cuántos
    tokens de salida se necesitan, o no pasarán esos errores"*. Y el matiz que lo hace
    urgente: *"es muy buen dato que los deja pasar cuando se queda corto"*.

    Quedarse corto **no rompe ruidoso**. El modelo entrega menos de lo que se le pidió
    —menos veredictos, un JSON que no cierra— y quien lo consume lo lee como «nada que
    reportar». En Eco eso convirtió un gate que frenaba el 15,6% de los claims en uno que
    frenaba el 0,0%, y en el tablero se vio como una mejora.

    Va por TAREA y no como un número único: el global queda dominado por las tareas
    multi-turno y termina recomendando 23.767 tokens para clasificar una frase. Nadie
    configura un nodo así, y un consejo que no se sigue no protege a nadie.
    """
    p = m.get("presupuesto_salida") or {}
    por_tarea = {k: v for k, v in (p.get("por_tarea") or {}).items() if v and k in SUITES}
    if not por_tarea:
        return ""
    orden = sorted(por_tarea.items(), key=lambda kv: -kv[1]["sugerido"])
    _piso_tag = ' <span class="meta">(piso)</span>'
    filas = "\n        ".join(
        (f'<tr><th scope="row">{esc(SUITES[k]["menu"])}</th>'
         f'<td>{v["p50"]:,}</td><td>{v["max"]:,}</td>'
         f'<td><strong>{v["sugerido"]:,}</strong>'
         f'{_piso_tag if v.get("piso") else ""}</td></tr>').replace(",", ".")
        for k, v in orden)
    piso = any(v.get("piso") for v in por_tarea.values())
    nota_piso = ('<p class="meta">Las marcadas <strong>(piso)</strong> tocaron el techo del '
                 'propio examen (8.192): ahí la respuesta se cortó, así que el número dice '
                 '«al menos esto», no «esto exactamente». Dar más aire en esas.</p>'
                 if piso else "")
    thinking = ('<p class="meta">⚠️ Este modelo <strong>razona</strong>, y los tokens de '
                'razonamiento salen del mismo presupuesto: pide bastante más que uno que no '
                'razona para escribir la misma respuesta. Es el motivo exacto por el que un '
                '<code>max_tokens</code> heredado de otro modelo lo corta.</p>'
                if m.get("thinking") else "")
    return f"""  <section class="results">
    <div class="results-header">
      <h2>Cuánto <code>max_tokens</code> darle, por tarea</h2>
      <p class="meta">Si tu nodo o tu script queda por debajo de esto,
      {esc(m['name'])} <strong>no falla: entrega de menos</strong> — y quien lo consume lo
      lee como que no había nada que reportar. Es el modo de falla más caro que hay,
      porque se parece a que todo salió bien.</p>
      {thinking}
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead><tr><th scope="col">Tarea</th><th scope="col">Mediana</th>
      <th scope="col">Peor caso medido</th><th scope="col">max_tokens sugerido</th></tr></thead>
      <tbody>
        {filas}
      </tbody>
    </table></div>
    {nota_piso}
  </section>"""


# ── dónde brilla y dónde se cae, por tarea concreta ──────────────────────────
def por_tarea(m: dict) -> str:
    """Un promedio de 29 ejes esconde el que le importa a quien lee. Esto lo abre:
    las tareas donde este modelo queda por encima y por debajo de SU PROPIA media."""
    qs = {k: v for k, v in (m.get("score_by_suite") or {}).items() if v is not None}
    qs = {k: v for k, v in qs.items() if k in SUITES}
    if len(qs) < 6:
        return ""
    media = sum(qs.values()) / len(qs)
    orden = sorted(qs.items(), key=lambda x: -x[1])
    arriba, abajo = orden[:4], orden[-4:][::-1]

    def li(items):
        out = []
        for k, v in items:
            s = SUITES[k]
            d = v - media
            out.append(f"<li><strong>{esc(s['menu'])}</strong> — {_n(v)} "
                       f"({d:+.2f} contra su media). <span class=\"meta\">Decide: "
                       f"{esc(s['decide'])}</span></li>")
        return "\n        ".join(out)

    return f"""  <section>
    <h2>Qué hace bien y qué no</h2>
    <p>Su media entre las {len(qs)} tareas medidas es <strong>{_n(media)}</strong>. Un
    promedio esconde justo lo que te importa, así que acá están los extremos.</p>
    <h3>Donde rinde por encima de sí mismo</h3>
    <ul>
        {li(arriba)}
    </ul>
    <h3>Donde se cae</h3>
    <ul>
        {li(abajo)}
    </ul>
  </section>"""


# ── alternativas: la pregunta real es «¿y qué más?» ──────────────────────────
def alternativas(m: dict, ranked: list) -> tuple[str, list]:
    q = m.get("quality_avg")
    c = m.get("cost_per_1k_calls_usd")
    otros = [x for x in ranked if x["key"] != m["key"] and x.get("quality_avg")]
    picks, vistos = [], set()

    def add(cand, etiqueta, porque):
        if cand and cand["key"] not in vistos:
            vistos.add(cand["key"])
            picks.append((cand, etiqueta, porque))

    if q and c:
        # más barato sin perder calidad (tolerancia media punto)
        cbaratos = [x for x in otros if (x.get("cost_per_1k_calls_usd") or 9e9) < c
                    and (x["quality_avg"] or 0) >= q - 0.15]
        cbaratos.sort(key=lambda x: x.get("cost_per_1k_calls_usd") or 9e9)
        add(cbaratos[0] if cbaratos else None, "Más barato, calidad equivalente",
            "misma nota o mejor, menos plata por llamada")
        # mejor calidad a precio parecido
        cerca = [x for x in otros if (x.get("cost_per_1k_calls_usd") or 9e9) <= c * 1.3
                 and (x["quality_avg"] or 0) > q]
        cerca.sort(key=lambda x: -(x["quality_avg"] or 0))
        add(cerca[0] if cerca else None, "Mejor nota, precio parecido",
            "hasta 30% más caro, pero rinde más")
    # más rápido en latencia
    if m.get("latency_avg_s"):
        rap = [x for x in otros if x.get("latency_avg_s")
               and x["latency_avg_s"] < m["latency_avg_s"] * 0.6
               and (x.get("quality_avg") or 0) >= (q or 0) - 0.3]
        rap.sort(key=lambda x: x["latency_avg_s"])
        add(rap[0] if rap else None, "Responde antes",
            "al menos 40% menos de espera, sin caer de nota")

    if not picks:
        return "", []
    def _lat(x):
        return "—" if not x.get("latency_avg_s") else f"{x['latency_avg_s']:.1f} s"

    filas = "\n        ".join(
        f"<tr><td><strong>{esc(c_['name'])}</strong><br><span class=\"meta\">{esc(et)}</span></td>"
        f"<td>{_n(c_.get('quality_avg'))}</td><td>{_usd(c_.get('cost_per_1k_calls_usd'))}</td>"
        f"<td>{_lat(c_)}</td>"
        f"<td class=\"meta\">{esc(pq)}</td></tr>"
        for c_, et, pq in picks)
    return f"""  <section class="results">
    <div class="results-header">
      <h2>Si {esc(m['name'])} no te cierra</h2>
      <p class="meta">Alternativas elegidas por contraste con este modelo, no por ranking general.</p>
    </div>
    <div class="table-scroll"><table class="results-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Calidad</th><th scope="col">$/1k</th><th scope="col">Latencia</th><th scope="col">Por qué</th></tr></thead>
      <tbody>
        {filas}
      </tbody>
    </table></div>
  </section>""", [c_["name"] for c_, _, _ in picks]


# ── el enlace a lo oficial: acá NO competimos ────────────────────────────────
def oficial(m: dict) -> str:
    """Los benchmarks del fabricante van al fabricante. Nunca se inventa una URL:
    `weights_url` está declarado y verificado, y la ficha de OpenRouter se construye
    sólo porque el id ES la ruta. Sin ninguno de los dos, no se dibuja la sección."""
    links = []
    if m.get("weights_url"):
        links.append((m["weights_url"], "Pesos y tarjeta oficial del modelo",
                      "ahí están los benchmarks del fabricante, la licencia y cómo correrlo"))
    prov = m.get("provider") or "openrouter"
    if prov == "openrouter" and m.get("id") and "/" in m["id"] and ":free" not in m["id"]:
        links.append((f"https://openrouter.ai/{m['id']}", "Ficha en OpenRouter",
                      "precio vigente, proveedores que lo sirven y límites de contexto"))
    if not links:
        return ""
    lis = "\n        ".join(
        f'<li><a href="{esc(u)}" target="_blank" rel="noopener nofollow">{esc(t)}</a> — '
        f'<span class="meta">{esc(d)}</span></li>' for u, t, d in links)
    return f"""  <section>
    <h2>Los números oficiales de {esc(m['name'])}</h2>
    <p>Acá no los repetimos, y es a propósito. MMLU, GPQA, SWE-bench y la tabla del
    lanzamiento las publica quien hizo el modelo, con más recursos y antes que nadie:
    <strong>ese enlace es mejor que cualquier copia nuestra</strong>, y no envejece.</p>
    <ul>
        {lis}
    </ul>
    <p>Lo que sí medimos acá es lo otro: <strong>qué pasa cuando este modelo tiene que
    decidir algo de un negocio chico, en español y a un precio que se pueda pagar</strong>.
    Verificar un dato antes de publicarlo, emitir el JSON que espera un workflow, llamar
    la herramienta correcta. Eso no está en la tarjeta del fabricante.</p>
  </section>"""


def render(m: dict, ranked: list, puesto: int | None) -> str:
    nombre = m["name"]
    hoy = date.today().isoformat()
    url = f"{SITE}/modelo/{slug(m)}/"
    alt_html, alt_nombres = alternativas(m, ranked)
    desc = (f"{nombre}: {m.get('runs') or 0} runs propios en español — calidad {_n(m.get('quality_avg'))}, "
            f"{_usd(m.get('cost_per_1k_calls_usd'))} por 1.000 llamadas. Para qué sirve de verdad "
            f"en un negocio chico, y cuándo conviene otro.")
    body = f"""  <section class="hero">
    <h1>{esc(nombre)}: para qué sirve de verdad (benchmark en español)</h1>
    <p class="lead">{veredicto(m, ranked)}</p>
    <p class="meta">Medido con <strong>{m.get('runs') or 0} runs</strong> que puntúan, juez Phi-4 local.
    Última actualización: {hoy} ·
    <a href="https://github.com/ctala/ai-benchmarks-alternativos" target="_blank" rel="noopener">datos abiertos</a></p>
  </section>
{kpis(m, puesto, len(ranked), ranked)}
{perfil(m, ranked)}
{por_tarea(m)}
{alt_html}
{ficha(m, puesto, len(ranked))}
{contra_frontier(m, ranked)}
{presupuesto(m)}
{oficial(m)}
  <section class="cta-block">
    <h2>¿Es el mejor para TU caso?</h2>
    <p>Filtra por presupuesto, calidad mínima y tipo de tarea. En 30 segundos sabés si
    {esc(nombre)} es tu opción o hay algo mejor para lo que hacés.</p>
    <a href="/" class="cta-primary">Ir a la calculadora →</a>
  </section>"""
    contrato = emitir(
        tipo="ficha", generador="generate_model_cards",
        recomienda=[nombre] + alt_nombres,
        nota="ficha de un modelo: publica SUS números y enlaza los oficiales al fabricante",
    )
    html = page_shell(f"{nombre}: benchmark real en español (2026)", desc,
                      f"{nombre.lower()} benchmark, {nombre.lower()} precio, {nombre.lower()} opiniones",
                      url, body, contrato)
    # Las fichas viven UN NIVEL más abajo que el resto (`/modelo/<key>/` contra
    # `/<slug>/`), y `page_shell` enlaza la hoja de estilos con ruta relativa
    # `../style.css`. Sin esto, las 83 fichas saldrían sin CSS — cargando, viéndose rotas
    # y sin que nada fallara, que es el modo de romper más difícil de detectar. Se usa
    # ruta absoluta, que es correcta a cualquier profundidad.
    html = html.replace('href="../style.css"', 'href="/style.css"')
    return html.replace("</head>", BRAND_CSS + "\n</head>")


def main() -> int:
    d = json.loads(MODELS_JSON.read_text())
    ranked = [m for m in d["models"] if m.get("ranked")]
    ranked.sort(key=lambda x: -(x.get("score_global") or 0))
    puestos = {m["key"]: i + 1 for i, m in enumerate(ranked)}

    out = DOCS / "modelo"
    out.mkdir(exist_ok=True)
    n = 0
    for m in ranked:
        p = out / slug(m)
        p.mkdir(exist_ok=True)
        (p / "index.html").write_text(render(m, ranked, puestos.get(m["key"])))
        n += 1
    print(f"✓ {n} fichas de modelo → docs/modelo/<key>/index.html")
    con_pesos = sum(1 for m in ranked if m.get("weights_url"))
    print(f"  con enlace a pesos oficiales: {con_pesos} de {n} "
          f"(el resto enlaza la ficha del proveedor; nunca se inventa una URL)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
