#!/usr/bin/env python3
"""
Genera tabla de modelos probados para MODELOS.md con links a:
1. MD por modelo en benchmarks/results/per-model/
2. Carpeta de responses individuales

El score mostrado es el `score_global` z-scoreado de docs/data/models.json,
exactamente el mismo que usa la calculadora web. No recalcula nada desde los
JSONs crudos para evitar discrepancias.

Uso:
    python benchmarks/generate_modelos_md_table.py        # imprime tabla a stdout
    python benchmarks/generate_modelos_md_table.py -i     # actualiza MODELOS.md in-place
"""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
RESULTS_DIR = ROOT / "benchmarks" / "results"
PER_MODEL_DIR = RESULTS_DIR / "per-model"
RESPONSES_DIR = RESULTS_DIR / "responses"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"


def model_id_to_per_model_filename(model_id: str) -> str:
    safe = model_id.replace("/", "_").replace(".", "_").replace(":", "_")
    return f"{safe}.md"


def load_models_export():
    """Devuelve (ranked, in_review).

    ranked     = muestra solida (>=50 runs) -> entra a los rankings.
    in_review  = tiene score pero muestra chica (<50 runs) -> se muestra aparte.

    La separacion importa: con 3-12 runs un modelo puede liderar por azar. Antes
    esta tabla mezclaba ambos y coronaba #1 a un modelo con 39 runs mientras las
    paginas pSEO (que si filtran >=50) mostraban otro ganador.
    """
    if not MODELS_JSON.exists():
        raise FileNotFoundError(
            f"No existe {MODELS_JSON}. Corré `python benchmarks/export_for_pages.py` primero."
        )
    data = json.loads(MODELS_JSON.read_text())
    scored = [m for m in data.get("models", []) if m.get("score_global") is not None]
    ranked = [m for m in scored if m.get("ranked")]
    # Los retirados se toman del catálogo COMPLETO, no de `scored`: un modelo retirado
    # sin runs también tiene que avisar que no se puede usar.
    retired = [m for m in data.get("models", []) if m.get("retired")]
    # Plano suscripción: medidos vía Claude Code (claude -p). Camino distinto al plano
    # común — comparables ENTRE SÍ, no contra los de API (ver build_subscription_table).
    subscription = [m for m in scored if m.get("provider") == "claude_code"
                    and not m.get("retired")]
    # Variantes de proveedor / self-hosted: el mismo modelo por otra infra. Se comparan
    # en /mismo-modelo-distinto-proveedor/, no acá.
    variants = [m for m in scored if (m.get("provider_variant") or m.get("self_hosted"))
                and m.get("provider") != "claude_code" and not m.get("retired")]
    # `in_review` = muestra chica DE VERDAD (<50 runs). Antes este bucket mezclaba las
    # variantes (100+ runs) bajo el título "muestra parcial <50 runs" — etiqueta falsa.
    in_review = [m for m in scored if not m.get("ranked") and not m.get("retired")
                 and not m.get("provider_variant") and not m.get("self_hosted")]
    return ranked, in_review, retired, subscription, variants, data.get("models", [])


def find_response_dirs(model_id: str) -> list[str]:
    if not RESPONSES_DIR.exists():
        return []
    found = []
    safe_id = model_id.replace("/", "_").replace(":", "_")
    for ts_dir in sorted(RESPONSES_DIR.iterdir(), reverse=True):
        if not ts_dir.is_dir():
            continue
        for f in ts_dir.iterdir():
            if not f.name.endswith(".md"):
                continue
            stem = f.name.split("__")[0]
            mid_short = model_id.split("/")[-1].replace(".", "")
            if mid_short.lower() in stem.lower() or stem.lower() in mid_short.lower():
                found.append(ts_dir.name)
                break
    return found


def build_links(model_id: str) -> tuple[str, str]:
    fname = model_id_to_per_model_filename(model_id)
    md_path = PER_MODEL_DIR / fname
    link_md = f"[per-model](benchmarks/results/per-model/{fname})" if md_path.exists() else "—"
    response_dirs = find_response_dirs(model_id)
    link_resp = f"[responses](benchmarks/results/responses/{response_dirs[0]}/)" if response_dirs else "—"
    return link_md, link_resp


def row_for_model(m: dict, score_key: str = "score_calidad") -> str:
    """Fila con calidad + marcador de frontera (v4.1).

    NO lleva columna de "valor": el compuesto correlaciona r=0,943 con el índice de
    calidad, así que publicarlo al lado era repetir la misma información con otro
    nombre. El marcador ⭐ sí agrega algo — deja fuera a 69 de 82.
    """
    mid = m.get("id", "?")
    fmt = lambda v: f"{v:.2f}" if v is not None else "—"
    # La columna de score muestra SIEMPRE el criterio que ordena esa tabla — si no,
    # una tabla por suite quedaría ordenada por una cosa y mostrando otra.
    cal_s = f"**{fmt(m.get(score_key))}**"
    # Marcador agéntico (v4.2). Va en la tabla de CALIDAD a propósito: es justo ahí donde
    # el dato falta más. Hermes 4 405B aparece con 8,20 —arriba de 40 modelos que sí
    # resuelven la tarea— y no puede ejecutarla; sin marcador, la fila entera invita a
    # integrarlo. `⛔` = medido y no puede. Vacío = sin medir, que NO es lo mismo que apto.
    if m.get("sirve_para_agentes") is False:
        cal_s += " ⛔"
    val_s = "⭐" if m.get("pareto") else ""
    runs = m.get("runs", 0)
    os_label = "✅" if m.get("open_source") else "❌" if m.get("open_source") is False else "?"
    license_str = m.get("license") or ""
    ci = m.get("cost_input_per_M")
    co = m.get("cost_output_per_M")
    cost = f"${ci}/{co}" if ci is not None and co is not None else "—"
    link_md, link_resp = build_links(mid)
    return (
        f"| `{mid}` | {os_label} {license_str} | {cost} | {cal_s} | {val_s} | {runs} "
        f"| {link_md} | {link_resp} |"
    )


def table_header(title: str) -> list[str]:
    return [
        f"#### {title}",
        "",
        # El ⛔ sale en TODAS las tablas porque `row_for_model` es compartido, así que la
        # leyenda va acá y no solo en la primera: quien entra por un ancla a «Mejor
        # coding» ve el símbolo y necesita saber qué significa en el mismo sitio.
        "> ⛔ = medido dentro de un agente real y **no puede ejecutar la tarea** "
        "(sin endpoint con herramientas, o no sostiene el bucle). "
        "Ver [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md).",
        "",
        "| Modelo | OS | $ in/out | Calidad | Frontera | Runs | Per-model MD | Responses |",
        "|---|---|---:|---:|:-:|---:|---|---|",
    ]


def build_global_table(models: list[dict]) -> str:
    """Tabla principal, ordenada por CALIDAD desde v4.1 (PLAN-V4.1.md §3).
    `Valor` queda como columna al lado para que se vea el trade-off, no escondido
    dentro de un solo número."""
    lines = table_header(
        "Índice de calidad — qué modelo responde mejor "
        "(⭐ = en la frontera de Pareto: nadie lo supera a la vez en calidad, precio y latencia)"
    )
    for m in sorted(models, key=lambda x: -(x.get("score_calidad") or -1)):
        lines.append(row_for_model(m, "score_calidad"))
    return "\n".join(lines)


def build_quality_table(models: list[dict]) -> str:
    lines = table_header("Mejor calidad pura (sin considerar costo ni velocidad)")
    for m in sorted(models, key=lambda x: -(x.get("quality_avg") or -1)):
        lines.append(row_for_model(m, "quality_avg"))
    return "\n".join(lines)


def build_suite_table(models: list[dict], suites: list[str], title: str) -> str:
    def score(m):
        by_suite = m.get("score_by_suite", {})
        vals = [by_suite.get(s) for s in suites if by_suite.get(s) is not None]
        return sum(vals) / len(vals) if vals else -1

    lines = table_header(title)
    for m in sorted(models, key=lambda x: -score(x)):
        s = score(m)
        if s < 0:
            continue
        # Mostramos el score compuesto como score_key temporal
        m["_tmp_score"] = s
        lines.append(row_for_model(m, "_tmp_score"))
        del m["_tmp_score"]
    return "\n".join(lines)


def build_cost_efficiency_table(models: list[dict]) -> str:
    """Calidad por dólar: `score_calidad` ÷ ($/1k calls). Un ratio, no un compuesto.

    Reemplaza (13-ago-2026) al ranking de pesos v2.9 (60/20/10/10), que se sacó por
    redundante: correlacionaba **r = 0,882** con el índice de calidad. Todos los
    compuestos que probamos terminan igual — el costo z-scoreado aporta ±0,30 contra
    ±1,3 de la calidad, así que el precio casi no mueve el orden y la tabla resultante
    es el ranking de calidad otra vez, con otro título.

    El ratio **sí** es información nueva: **r = 0,052** con el índice de calidad, o sea
    prácticamente ortogonal. Y responde una pregunta real que ninguna otra tabla
    responde: *"con el presupuesto como límite duro, ¿qué rinde más por peso?"*

    ⚠️ Por construcción premia lo barato: un modelo de calidad media a $0,10 le gana a
    uno excelente a $1. Eso NO es un defecto a corregir — es literalmente lo que la
    métrica dice. Por eso la columna de calidad va al lado: para que se vea qué se
    está resignando.
    """
    tested = [m for m in models if (m.get("cost_per_1k_calls_usd") or 0) > 0
              and m.get("score_calidad") is not None]
    for m in tested:
        m["_qpd"] = m["score_calidad"] / m["cost_per_1k_calls_usd"]

    lines = table_header(
        "Calidad por dólar — cuánta calidad rinde cada peso "
        "(calidad ÷ $/1k calls; premia lo barato a propósito, mirá la columna Calidad)"
    )
    # Cabecera propia: acá el número que ordena NO es un score 0-10, es un ratio.
    lines[2] = "| Modelo | OS | $ in/out | Calidad/$ | Frontera | Runs | Per-model MD | Responses |"
    for m in sorted(tested, key=lambda x: -x["_qpd"]):
        lines.append(row_for_model(m, "_qpd"))
        del m["_qpd"]
    return "\n".join(lines)


def build_in_review_table(models: list[dict]) -> str:
    """Modelos con score pero muestra insuficiente para rankear (<50 runs).

    Se publican por transparencia -- no se esconden -- pero fuera del ranking:
    su score es indicativo, no comparable de igual a igual.
    """
    lines = [
        "#### En evaluación — muestra parcial (<50 runs, NO rankeados)",
        "",
        "> Estos modelos tienen menos runs que el piso del ranking, así que su score es "
        "**indicativo, no comparable**: con pocas muestras la varianza permite que un modelo "
        "quede arriba (o abajo) por azar. Se listan para no esconderlos, pero **no compiten** "
        "en las tablas de arriba hasta completar la cobertura.",
        "",
        "| Modelo | OS | $ in/out | Calidad (indic.) | Frontera | Runs "
        "| Per-model MD | Responses |",
        "|---|---|---:|---:|:-:|---:|---|---|",
    ]
    for m in sorted(models, key=lambda x: -(x.get("score_calidad") or -1)):
        lines.append(row_for_model(m, "score_calidad"))
    return "\n".join(lines)


def build_subscription_table(models: list[dict]) -> str:
    """Plano suscripción Claude: medidos vía Claude Code (claude -p), $0 marginal.

    Es un CAMINO distinto al plano común: arrastra ~8.8K tokens de scaffolding del CLI.
    Medimos el sesgo con los 2 modelos que rindieron el examen por AMBOS caminos:
    la calidad por suscripción da −0.22 (Opus 4.8) y −0.15 (Opus 4.7) vs API, la
    velocidad −7..11%, y la latencia queda 2.5-4× peor (arranque del CLI, basura para
    comparar). Por eso estos números se comparan ENTRE SÍ (mismo camino para todos)
    y como PISO conservador del modelo — no compiten en el ranking principal.
    """
    lines = [
        "#### Vía suscripción Claude — plano propio (comparables entre sí)",
        "",
        "> Medidos aprovechando la **suscripción de Claude Code** (costo marginal $0), todos "
        "por el mismo camino → **comparables entre ellos**. Ese camino arrastra ~8.8K tokens "
        "de scaffolding del CLI y **deprime la nota**: en los 2 modelos medidos por ambos "
        "caminos, la calidad por API dio **+0.15 y +0.22 más** que por suscripción. Leé estos "
        "números como **piso conservador**, no como techo — y no los compares 1:1 contra la "
        "tabla principal (la latencia por CLI es 2.5-4× peor y no es del modelo). Sirven para "
        "la pregunta de quien ya paga el plan: *¿qué modelo uso dentro de mi suscripción?*",
        "",
        "| Modelo | Calidad (piso) | Velocidad | Runs | Per-model MD | Responses |",
        "|---|---:|---:|---:|---|---|",
    ]
    for m in sorted(models, key=lambda x: -(x.get("quality_avg") or -1)):
        mid = m.get("id", "?")
        link_md, link_resp = build_links(mid)
        q = m.get("quality_avg")
        tps = m.get("tokens_per_second")
        lines.append(
            f"| `{mid}` | **{q:.2f}** | {tps:.0f} tok/s | {m.get('runs', 0)} | {link_md} | {link_resp} |"
        )
    return "\n".join(lines)


def build_variants_note(models: list[dict]) -> str:
    """Variantes de proveedor: solo un puntero — su comparación vive en su propia página."""
    n = len(models)
    return (
        f"#### Variantes de proveedor ({n} mediciones)\n"
        "\n"
        "> El mismo modelo servido por otra infraestructura (Groq, NVIDIA NIM, Ollama Cloud, "
        "API directa del proveedor, self-hosted). **No compiten acá** — comparar infra contra "
        "infra es otra pregunta, y tiene su propia página: "
        "[el proveedor te cambia el modelo](https://benchmarks.cristiantala.com/mismo-modelo-distinto-proveedor/). "
        "El caso extremo medido: el mismo Qwen 3.5 397B da **7.96 en NVIDIA NIM y 5.46 en "
        "Ollama Cloud** — 2.5 puntos por la infraestructura, no por el modelo."
    )


def build_retired_table(models: list[dict], todos: list[dict] = ()) -> str:
    """Modelos retirados, con CUÁNDO, POR QUÉ y si siguen vivos por otra ruta.

    Alguien que buscó "Devstral Small" y llega acá merece enterarse de que el endpoint
    ya no existe — no encontrar una tabla que se lo recomienda. Los datos históricos
    quedan (son reales), pero fuera del ranking.

    Tres cosas que esta tabla NO hacía hasta el 12-ago-2026, y por qué importan:

    1. **No decía cuándo ni por qué.** El dato existía como comentario en `models.py`,
       ilegible para este generador. Un retiro sin fecha no se puede comunicar ni auditar.
    2. **Mezclaba dos cosas distintas bajo "el proveedor ya no los sirve".** Phi-4 figuraba
       ahí siendo que es el JUEZ del benchmark: no lo retiró nadie, decidimos que no
       compite. El título mentía para ese caso.
    3. **No decía que el modelo puede seguir vivo por otra ruta.** Nemotron Super 49B salió
       de OpenRouter y sigue en NVIDIA NIM, donde lo tenemos medido con 92 runs. "Retirado"
       a secas hace pensar que el modelo murió, y lo que murió fue UNA ruta.
    """
    por_id = {}
    for m in todos:
        if not m.get("retired"):
            por_id.setdefault(m.get("id"), []).append(m)

    def alternativa(m: dict) -> str:
        otras = [o for o in por_id.get(m.get("id"), []) if o.get("key") != m.get("key")]
        if not otras:
            return "—"
        o = max(otras, key=lambda x: x.get("runs") or 0)
        return f"✅ {o['name']} ({o.get('runs', 0)} runs)"

    ETIQUETA = {
        "provider": "proveedor",
        "policy": "decisión propia",
        "unknown": "sin registrar",
    }
    lines = [
        "#### Retirados — fuera del ranking y de las recomendaciones",
        "",
        "> **Un modelo que no puedes usar no es un candidato.** Sus números son reales y "
        "quedan acá por transparencia (alimentan el análisis histórico), pero no compiten. "
        "Devstral Small llegó a estar **#5** antes de que su endpoint desapareciera, y "
        "Nemotron Super 49B v1.5 estaba **#8** el día que NVIDIA lo sacó de OpenRouter.",
        "",
        "> **`Quién`** distingue lo que decidió el proveedor de lo que decidimos nosotros: "
        "Phi-4 no lo retiró nadie, es el modelo juez y no compite. **`Sigue vivo en`** "
        "avisa cuando lo que murió fue *una ruta* y no el modelo — el caso normal, no la "
        "excepción. Y el retiro **se re-verifica** (`check_endpoints.py --recheck-retired`): "
        "el 12-ago-2026 dos modelos retirados en julio habían vuelto a responder porque un "
        "proveedor los recogió, y volvieron al catálogo.",
        "",
        "| Modelo | Retirado | Quién | Causa | Sigue vivo en | Score (histórico) | Runs |",
        "|---|---|---|---|---|---:|---:|",
    ]
    for m in sorted(models, key=lambda x: (x.get("retired_at") or "", -(x.get("score_global") or -1)), reverse=True):
        score = m.get("score_global")
        lines.append(
            f"| `{m.get('id') or m.get('key')}` | {m.get('retired_at') or '—'} "
            f"| {ETIQUETA.get(m.get('retired_kind'), '—')} | {m.get('retired_reason') or '—'} "
            f"| {alternativa(m)} | **{score:.2f}** | {m.get('runs', 0)} |"
            if score is not None else
            f"| `{m.get('id') or m.get('key')}` | {m.get('retired_at') or '—'} "
            f"| {ETIQUETA.get(m.get('retired_kind'), '—')} | {m.get('retired_reason') or '—'} "
            f"| {alternativa(m)} | — | {m.get('runs', 0)} |"
        )
    return "\n".join(lines)


def build_table(ranked: list[dict], in_review: list[dict], retired: list[dict] = (),
                subscription: list[dict] = (), variants: list[dict] = (),
                todos: list[dict] = ()) -> str:
    # `build_quality_table` ("Mejor calidad pura") salió del output en v4.1: ordenaba por
    # `quality_avg` y la tabla principal ahora ordena por `score_calidad`, que es su
    # z-score — misma monotonía, mismo orden, dos tablas idénticas. La función queda por
    # si se la necesita en otro contexto, pero no se publica.
    sections = [
        build_global_table(ranked),
        "",
        build_suite_table(ranked, ["code_generation", "structured_output", "string_precision"], "Mejor coding"),
        "",
        build_suite_table(ranked, ["deep_reasoning", "reasoning"], "Mejor razonamiento"),
        "",
        build_suite_table(ranked, ["content_generation", "startup_content", "news_seo_writing"], "Mejor contenido/marketing"),
        "",
        build_cost_efficiency_table(ranked),
    ]
    if subscription:
        sections += ["", build_subscription_table(list(subscription))]
    if variants:
        sections += ["", build_variants_note(list(variants))]
    if in_review:
        sections += ["", build_in_review_table(in_review)]
    if retired:
        sections += ["", build_retired_table(list(retired), list(todos))]
    return "\n".join(sections)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in-place", action="store_true", help="Actualiza MODELOS.md in-place")
    args = ap.parse_args()

    ranked, in_review, retired, subscription, variants, todos = load_models_export()
    table = build_table(ranked, in_review, retired, subscription, variants, todos)

    if args.in_place:
        modelos_md = ROOT / "MODELOS.md"
        content = modelos_md.read_text()
        START = "<!-- AUTO-TABLE-START -->"
        END = "<!-- AUTO-TABLE-END -->"
        new_block = (
            f"{START}\n\n"
            "> Auto-generado por `benchmarks/generate_modelos_md_table.py`.\n\n"
            "> **No existe un único 'mejor modelo'.** El score global combina calidad, costo, "
            "velocidad y latencia con pesos elegidos para emprendedores (70% calidad, 15% costo, "
            "7.5% velocidad, 7.5% latencia) — **es un punto de partida, no un veredicto**. "
            "Un modelo puede quedar bajo en el global y ser el correcto para vos: si tu caso es "
            "batch nocturno, la latencia no te importa y el ranking la está penalizando igual. "
            "Mirá las tablas por caso de uso, y para tus propios pesos usá la "
            "[calculadora](https://benchmarks.cristiantala.com/).\n\n"
            "> **Piso de ranking: 50 runs.** Los modelos con menos muestra van a *En evaluación* "
            "al final — su score es indicativo, no comparable.\n\n"
            f"{table}\n\n"
            f"{END}"
        )

        if START in content and END in content:
            new_content = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", new_block, content, flags=re.DOTALL)
        else:
            new_content = content.replace("## Probados", f"## Probados\n\n{new_block}\n\n#### Tabla manual (legacy):", 1)
        modelos_md.write_text(new_content)
        print(f"OK: MODELOS.md actualizado — {len(ranked)} rankeados, "
              f"{len(subscription)} vía suscripción, {len(variants)} variantes, "
              f"{len(in_review)} en evaluación, {len(retired)} retirados")
    else:
        print(table)


if __name__ == "__main__":
    main()
