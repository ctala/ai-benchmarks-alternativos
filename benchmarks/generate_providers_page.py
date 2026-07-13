#!/usr/bin/env python3
"""
Genera /mismo-modelo-distinto-proveedor/ — el hallazgo que nadie está publicando.

POR QUÉ EXISTE
--------------
Todo el mundo compara MODELOS. Nadie compara el mismo modelo servido por proveedores
distintos. Y resulta que ahí hay una diferencia enorme que le está costando plata y
calidad a quien elige:

    Qwen 3.5 397B    NVIDIA NIM      calidad 8.17
                     Ollama Cloud    calidad 5.43     ← 2.74 puntos. El MISMO modelo.

Un emprendedor que decide "voy con Qwen 3.5 397B" cree que tomó la decisión. Tomó la
mitad. La otra mitad —por dónde lo llama— le puede costar casi 3 puntos de calidad,
3× la velocidad o el doble de latencia. Y no está en ninguna comparativa.

Este dato lo tenemos por accidente: durante meses el benchmark midió unos modelos en
OpenRouter, otros en NIM, Groq u Ollama Cloud. Eso era un BUG (el ranking medía
modelo × infraestructura, y un mismo modelo llegaba a ocupar dos puestos distintos).
Al arreglarlo, en vez de tirar las mediciones duplicadas las conservamos: son el
único experimento natural que tenemos sobre este tema.

QUÉ MÉTRICAS USA — Y CUÁLES NO
------------------------------
Usa SOLO métricas crudas: calidad promedio del juez, tokens/s y TTFT. NO usa
`score_global`, que es un z-score contra la población: medir un modelo nuevo recalcula
el score de todos, así que cualquier cifra de score que se escriba acá caduca sola.
Las crudas no se mueven cuando entra un modelo nuevo. La página se regenera y sigue
siendo cierta.

Uso:
    python benchmarks/generate_providers_page.py
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

from generate_comparison import DOCS, SITE, esc, funnel_block, methodology, page_shell  # noqa: E402

SLUG = "mismo-modelo-distinto-proveedor"

# Cómo se llama, en castellano, el camino por el que se midió cada modelo.
VIA = {
    "openrouter": "OpenRouter",
    "nvidia_nim": "NVIDIA NIM",
    "groq_direct": "Groq",
    "ollama_cloud": "Ollama Cloud",
    "minimax_direct": "API directa del fabricante",
    "xiaomi_direct": "API directa del fabricante",
    "openai_direct": "API directa del fabricante",
    "claude_code": "Claude Code (CLI)",
    "llama_server": "self-hosted",
    "llama_server_think": "self-hosted (razonamiento)",
    "ollama": "self-hosted",
    "diffusion_cli": "self-hosted",
}
SELF_HOSTED = {"llama_server", "llama_server_think", "ollama", "diffusion_cli"}

MIN_RUNS = 50          # misma vara que el ranking: con menos, la diferencia puede ser azar
UMBRAL_GRAVE = 1.0     # ≥1 punto de calidad = el proveedor te cambia el modelo


def familia(nombre):
    return re.sub(r"\s*\([^)]*\)", "", nombre).strip()


def cargar():
    from benchmarks.models import MODELS
    from generate_comparison import load_models
    models = load_models()
    prov = {c["name"]: (c.get("provider") or "openrouter")
            for c in MODELS.values() if c.get("name")}
    return models, prov


def parejas(models, prov):
    """Modelos medidos por más de un camino, con muestra suficiente en cada uno.

    Se excluyen los self-hosted: su velocidad es la de TU máquina, no la de un
    datacenter, y mezclarlos acá compararía una GPU de escritorio con un cluster.
    Eso no es una diferencia de proveedor, es otra pregunta.
    """
    g = {}
    for m in models:
        if m.get("quality_avg") is None or m.get("runs", 0) < MIN_RUNS or m.get("retired"):
            continue
        if prov.get(m["name"]) in SELF_HOSTED:
            continue
        g.setdefault(familia(m["name"]), []).append(m)
    out = []
    for fam, ms in g.items():
        if len(ms) < 2:
            continue
        ms.sort(key=lambda x: -(x.get("quality_avg") or 0))
        dq = (ms[0]["quality_avg"] or 0) - (ms[-1]["quality_avg"] or 0)
        out.append({"fam": fam, "ms": ms, "dq": dq})
    out.sort(key=lambda x: -x["dq"])
    return out


def n(v, d=2, s=""):
    return "—" if v is None else f"{v:.{d}f}{s}"


def tabla(pares):
    filas = []
    for p in pares:
        grave = p["dq"] >= UMBRAL_GRAVE
        for i, m in enumerate(p["ms"]):
            via = VIA.get(m.get("provider") or "openrouter", "?")
            first = i == 0
            fam_cell = f'<td rowspan="{len(p["ms"])}"><strong>{esc(p["fam"])}</strong></td>' if first else ""
            delta = ""
            if first:
                # Sin clase inventada: el peso lo da <strong>, que ya está estilado.
                v = f"<strong>{p['dq']:+.2f}</strong>" if grave else f"{p['dq']:+.2f}"
                delta = f'<td rowspan="{len(p["ms"])}">{v}</td>'
            mejor = ' class="win"' if first else ""
            filas.append(
                f"<tr{mejor}>{fam_cell}"
                f"<td>{esc(via)}</td>"
                f"<td>{n(m.get('quality_avg'))}</td>"
                f"<td>{n(m.get('tokens_per_second'), 0)}</td>"
                f"<td>{n(m.get('latency_avg_s'), 1, 's')}</td>"
                f"<td>{m['runs']}</td>{delta}</tr>"
            )
    return (
        '<div class="table-scroll"><table class="results-table">'
        "<thead><tr><th>Modelo</th><th>Se llama por</th><th>Calidad</th>"
        "<th>tok/s</th><th>TTFT</th><th>Runs</th><th>Δ calidad</th></tr></thead>"
        f"<tbody>{''.join(filas)}</tbody></table></div>"
    )


def veredicto(pares):
    graves = [p for p in pares if p["dq"] >= UMBRAL_GRAVE]
    if not graves:
        return (
            "<p>Hoy ningún modelo medido por más de un camino cambia más de "
            f"{UMBRAL_GRAVE:.0f} punto de calidad según el proveedor. La velocidad y la "
            "latencia <strong>sí</strong> cambian, y bastante — mirá la tabla.</p>"
        )
    peor = graves[0]
    a, b = peor["ms"][0], peor["ms"][-1]
    va = VIA.get(a.get("provider") or "openrouter", "?")
    vb = VIA.get(b.get("provider") or "openrouter", "?")
    return f"""<p><strong>{esc(peor['fam'])} es el caso más grave.</strong> Servido por
{esc(va)} da <strong>{n(a['quality_avg'])}</strong> de calidad. Servido por {esc(vb)},
<strong>{n(b['quality_avg'])}</strong>. Son <strong>{peor['dq']:.2f} puntos</strong> — el
mismo modelo, los mismos pesos, la misma pregunta. La diferencia no está en el modelo:
está en cómo lo sirven (cuantización, configuración, versión).</p>

<p>Si elegiste {esc(peor['fam'])} porque lo viste bien rankeado y lo estás llamando por
{esc(vb)}, no estás usando el modelo que creés que elegiste.</p>"""


def build():
    models, prov = cargar()
    for m in models:
        m["provider"] = prov.get(m["name"], "openrouter")
    pares = parejas(models, prov)

    graves = [p for p in pares if p["dq"] >= UMBRAL_GRAVE]
    spread_speed = max(
        (max(x.get("tokens_per_second") or 0 for x in p["ms"])
         / max(1, min(x.get("tokens_per_second") or 1 for x in p["ms"])))
        for p in pares
    ) if pares else 1

    title = "El mismo modelo rinde distinto según el proveedor (datos reales)"
    desc = (f"Medimos {len(pares)} modelos por más de un proveedor. "
            f"{len(graves)} cambian ≥1 punto de calidad según por dónde los llames. "
            "Elegir el modelo es la mitad de la decisión.")
    kw = ("mismo modelo distinto proveedor, openrouter vs api directa, "
          "ollama cloud calidad, nvidia nim vs openrouter, groq vs openrouter, "
          "cuantizacion proveedor llm, que proveedor de llm elegir")

    body = f"""
<h1>El mismo modelo no rinde igual según quién lo sirva</h1>

<p class="verdict-lead">Elegís un modelo mirando un ranking. Después lo llamás por el proveedor
que tenías a mano. Y resulta que <strong>esa segunda decisión, la que nadie te ayuda a
tomar, te puede costar más calidad que la primera.</strong></p>

{veredicto(pares)}

<h2>Los datos</h2>

<p>Estos son todos los modelos que medimos por más de un camino, con al menos {MIN_RUNS}
runs en cada uno. La columna <strong>Δ calidad</strong> es la diferencia entre el mejor y
el peor proveedor del mismo modelo. <strong>Si el modelo fuera lo único que importa, esa
columna sería cero en todas las filas.</strong></p>

{tabla(pares)}

<p class="meta">La calidad es el promedio del juez sobre tareas reales (0-10). El TTFT es
el tiempo hasta el primer token. No usamos el score global del ranking acá a propósito:
ese es un z-score contra toda la población y se recalcula cada vez que entra un modelo
nuevo. Estas tres columnas son crudas — no se mueven.</p>

<h2>Por qué pasa esto</h2>

<p>Un proveedor no te entrega "el modelo". Te entrega <em>su forma de servirlo</em>, y ahí
hay decisiones que cambian el resultado:</p>

<ul>
<li><strong>Cuantización.</strong> Correr un modelo en menos bits es más barato y más
rápido — y le baja la calidad. El proveedor rara vez lo dice en la portada.</li>
<li><strong>La infraestructura.</strong> La velocidad y la latencia son del hardware, no
del modelo. En nuestros datos el mismo modelo llega a variar
<strong>{spread_speed:.1f}×</strong> en tokens por segundo según dónde corra.</li>
<li><strong>La configuración por defecto.</strong> Prompt de sistema, parámetros,
truncados, versión del checkpoint. Todo eso viaja con el proveedor.</li>
</ul>

<h2>Qué hacer con esto</h2>

<ol>
<li><strong>Cuando leas cualquier benchmark —incluido el nuestro— preguntá por dónde
midieron.</strong> Un número sin proveedor es medio número. Nosotros medimos todo por
OpenRouter justamente para que la comparación entre modelos sea limpia: si cada modelo se
mide en su propia infra, no estás comparando modelos, estás comparando datacenters.</li>
<li><strong>Si te cambiaste de proveedor y "el modelo empeoró", no era tu impresión.</strong>
Medilo antes de culpar al prompt.</li>
<li><strong>El proveedor más rápido no es gratis.</strong> A veces la velocidad viene de
una cuantización que te está costando calidad. Esa es una decisión que podés tomar — pero
tenés que saber que la estás tomando.</li>
</ol>

<h2>Cómo salió este dato</h2>

<p>Por un error nuestro, honestamente. Durante meses el benchmark midió unos modelos en
OpenRouter y otros en NVIDIA NIM, Groq o la API directa del fabricante. Eso era un bug: el
ranking estaba midiendo <em>modelo × infraestructura</em> y no el modelo, al punto de que
un mismo modelo llegó a ocupar <strong>dos puestos distintos</strong> del ranking.</p>

<p>Al arreglarlo (todo se mide en un plano común) podríamos haber borrado las mediciones
duplicadas. No lo hicimos: son el único experimento natural que tenemos sobre esto. El bug
resultó ser el dato más útil.</p>

{funnel_block()}
{methodology()}
"""
    html = page_shell(title, desc, kw, f"{SITE}/{SLUG}/", body)
    out = DOCS / SLUG
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")

    print(f"OK: /{SLUG}/ — {len(pares)} modelos con más de un proveedor, "
          f"{len(graves)} con Δ calidad ≥ {UMBRAL_GRAVE:.0f} punto")
    for p in pares[:3]:
        print(f"     {p['fam']:<24} Δ {p['dq']:+.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(build())
