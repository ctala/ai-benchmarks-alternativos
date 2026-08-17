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


# ── la ficha: nuestros números, sin adornos ──────────────────────────────────
def ficha(m: dict, puesto: int | None, total: int) -> str:
    filas = []
    if puesto:
        filas.append(("Puesto en el ranking global", f"#{puesto} de {total}"))
    filas += [
        ("Índice de calidad (0-10)", _n(m.get("quality_avg"))),
        ("Runs que puntúan", str(m.get("runs") or 0)),
    ]
    for p in PILARES:
        if cal_pilar(m, p) is not None:
            filas.append((f"— Calidad en {p}", _n(cal_pilar(m, p))))
    filas += [
        ("Tool calling", _n(m.get("tool_calling_score_avg"))),
        ("Precio por 1.000 llamadas", _usd(m.get("cost_per_1k_calls_usd"))),
        ("Precio por millón (in / out)",
         f"{_usd(m.get('cost_input_per_M'))} / {_usd(m.get('cost_output_per_M'))}"),
        ("Velocidad", "—" if not m.get("tokens_per_second") else f"{m['tokens_per_second']:.0f} tok/s"),
        ("Latencia total media", "—" if not m.get("latency_avg_s") else f"{m['latency_avg_s']:.1f} s"),
        ("Ventana de contexto", "—" if not m.get("context_window") else f"{m['context_window']:,}".replace(",", ".")),
    ]
    if m.get("effective_context"):
        filas.append(("Contexto útil medido", f"{m['effective_context']:,}".replace(",", ".")))
    if m.get("security_score") is not None:
        filas.append(("Resistencia a prompt injection", _n(m.get("security_score"))))
    tr = "\n        ".join(
        f"<tr><th scope=\"row\">{esc(k)}</th><td>{esc(str(v))}</td></tr>" for k, v in filas)
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
{ficha(m, puesto, len(ranked))}
{por_tarea(m)}
{alt_html}
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
