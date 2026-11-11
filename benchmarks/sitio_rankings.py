#!/usr/bin/env python3
"""Los datos de los rankings «Mejor LLM para…» y de las páginas de variantes. (11-nov-2026)

POR QUÉ EXISTE
--------------
Change `motor-sitio`, tarea 2.1. `generate_rankings.py` y `generate_variants.py` arman el HTML
con unas 770 líneas de prosa, y parte de esa prosa afirma cosas que el dato ya no respalda:
«el score de cada modelo es relativo a todos los demás» (la referencia está congelada desde
v4.0), «score global ≥ 6,8» (el piso es de calidad, 8,4), «8-12 turnos» (la suite va de 2 a 13),
«103 corridas» o «10×» escritos a mano en las variantes. Cristian (11-nov): la prosa no se copia
a la plantilla como texto fijo. Cada frase que afirma algo sobre los modelos sale de un campo de
este JSON, calculado con las funciones de los generadores (una sola autoridad), y cada cifra va
con `data-cifra`.

REGLA DEL RUIDO (la misma que la frontera de redacción, DECISIONES 11-nov-2026)
-----------------------------------------------------------------------------------
El top 3 no se lee por puesto: se recorren las bandas de calidad (`bands.quality_bands`, prueba
de diferencia de medias sobre el margen de error de la dimensión que ordena la página). Dentro de
una banda de más de un modelo se muestra «≈» y va primero el más barato por API; un modelo solo
en su banda conserva su puesto. En la página de precio no hay ruido: el orden es un dato exacto.

LA FRONTERA
-----------
Antes eran siete nombres escritos a mano y buscados como subcadena en el nombre (el mismo error
que `family()`), sin mirar si rankeaban: la página podía ubicar a un modelo retirado. Ahora son
las familias de los cuatro laboratorios cerrados grandes (`FAMILIAS_FRONTERA`) y, de cada una, su
modelo mejor ubicado EN ESTA PÁGINA, leído del campo `familia`.

`afirmaciones` resume lo que la página asegura (grupo de cabeza, mejor compra, top 3, frontera;
en variantes, el veredicto y la escalera) para que `paridad_sitio.py` lo contraste con lo que
publica hoy Python y declare cada diferencia con su motivo.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))
sys.path.insert(0, str(ROOT))

import contrato_pagina  # noqa: E402
import elegibilidad  # noqa: E402
import generate_comparison as gc  # noqa: E402
import generate_rankings as gr  # noqa: E402
import generate_variants as gv  # noqa: E402
from bands import _indistinguishable, is_local, quality_bands, SUITE  # noqa: E402

DOCS = ROOT / "docs"

# Las familias que la gente busca como «frontier». Es una decisión editorial, no un dato: los
# cuatro laboratorios cerrados grandes. Qué modelo de cada una aparece sale del ranking.
FAMILIAS_FRONTERA = {"gpt": "GPT (OpenAI)", "claude": "Claude (Anthropic)",
                     "gemini": "Gemini (Google)", "grok": "Grok (xAI)"}

# En una página que solo admite pesos abiertos, ninguna familia de arriba puede aparecer: la
# frontera es la de los laboratorios que publican pesos. Mismo campo `familia`, mismo criterio
# (el mejor rankeado de cada una en esta página). (motor-sitio 2.3: una sección no sale vacía)
FAMILIAS_FRONTERA_ABIERTA = {"qwen": "Qwen (Alibaba)", "deepseek": "DeepSeek", "glm": "GLM (Z.ai)",
                             "kimi": "Kimi (Moonshot)", "minimax": "MiniMax", "llama": "Llama (Meta)",
                             "gemma": "Gemma (Google)", "gpt-oss": "gpt-oss (OpenAI)",
                             "mistral": "Mistral"}


def familias_frontera(cfg) -> dict:
    return FAMILIAS_FRONTERA_ABIERTA if cfg.get("criterion") == "open_source" else FAMILIAS_FRONTERA


# Dónde enlaza «comparativas específicas»: la comparación por familia de las dos más buscadas
# (la de versión exacta que enlazaba antes ahora redirige aquí).
COMPARATIVA_FRONTERA = "claude-vs-chatgpt"
COMPARATIVAS_FRONTERA = {"cerrada": {"href": f"/{COMPARATIVA_FRONTERA}/", "texto": "Claude vs ChatGPT"},
                         "abierta": {"href": "/qwen-vs-llama/", "texto": "Qwen vs Llama"}}


# ── Piezas comunes ────────────────────────────────────────────────────────────

def _ficha(m) -> str | None:
    k = m.get("key")
    return f"/modelo/{k}/" if k and (DOCS / "modelo" / k / "index.html").exists() else None


def _modelo(m) -> dict:
    return {"key": m.get("key"), "name": m.get("name"), "ranked": bool(m.get("ranked")),
            "ficha": _ficha(m) if m.get("ranked") else None}


def _precio(m) -> dict:
    return {"costo_in": round(m.get("cost_input_per_M") or 0, 2),
            "costo_out": round(m.get("cost_output_per_M") or 0, 2),
            "c1k": round(gr.cost_for_calls(m), 2), "tps": round(m.get("tokens_per_second") or 0)}


def _fuera(m) -> dict:
    motivo = ((m.get("elegible") or {}).get("motivos") or {}).get("ranking")
    return {"key": m.get("key"), "name": m.get("name"), "motivo": motivo,
            "motivo_texto": elegibilidad.MOTIVOS.get(motivo, motivo), "ficha": _ficha(m)}


def _eje(m, cfg) -> dict:
    """El valor que ordena la página: nota /10, o «N de M» tareas en Agentes."""
    if gr.es_agentes(cfg):
        a = m.get("agentico") or {}
        return {"harbor": {"superadas": a.get("superadas"), "de": a.get("de")} if a.get("de") else None}
    v = gr.score_for(m, cfg)
    return {"nota": round(v, 1) if v is not None else None}


def _por_nombre(ms, nombre):
    xs = [m for m in ms if m.get("name") == nombre]
    if len(xs) != 1:
        raise SystemExit(f"sitio_rankings: «{nombre}» aparece {len(xs)} veces entre los rankeados; "
                         "el veredicto nombra por nombre y no puede elegir (indexar por key).")
    return xs[0]


def turnos_horizonte_largo() -> tuple[int, int]:
    """Cuántos turnos tiene una conversación de `agent_long_horizon`: lo que la página de tareas
    largas afirma. Se cuenta del guion de cada test, no se escribe a mano."""
    from benchmarks.tests import agent_long_horizon as alh
    n = [len(t["script"]) for t in alh.TESTS]
    return min(n), max(n)


# Lo que algunas páginas dicen en su entrada con una cifra adentro. El texto editorial de la
# config es de Python y no cambia hasta el corte; acá va la versión cuya cifra sale del dato.
def _lead_sitio(cfg) -> list:
    if cfg["slug"] == "mejor-llm-barato":
        return ["El modelo más caro casi nunca es el que necesitas. Filtramos los que rinden bien "
                "(calidad ≥ ", {"cifra": cfg.get("min_score", 8.4), "d": 1},
                ", examen y tareas reales de agente) y los ordenamos del más barato al más caro."]
    if cfg["slug"] == "mejor-llm-para-tareas-largas":
        _, mx = turnos_horizonte_largo()
        return ["Un asistente que se pierde a mitad de la conversación no sirve, por bien que responda "
                "al principio. Este corte ordena por la suite de horizonte largo, con conversaciones de "
                "hasta ", {"cifra": mx}, " turnos, no por el promedio."]
    return [cfg["lead"]]


def _caso(cfg) -> str:
    if cfg["slug"] == "mejor-llm-para-tareas-largas":
        return "tareas multi-paso donde el modelo tiene que sostener el hilo"
    return cfg["case"]


# ── Rankings ──────────────────────────────────────────────────────────────────

def top3_ruido(cfg, all_ranked) -> list[dict]:
    """Los tres que la página explica, con la regla del ruido (ver el docstring del módulo)."""
    pos = {m.get("key"): i for i, m in enumerate(all_ranked, 1)}
    if cfg["criterion"] == "cost":
        return [{"m": m, "marca": pos[m.get("key")], "banda": 1} for m in all_ranked[:3]]
    por_key = {m.get("key"): m for m in all_ranked}
    pool = gr._pool_banda(cfg, [m for m in all_ranked if m.get("ranked")])
    out = []
    for b in quality_bands(pool, gr._dim_banda(cfg)):
        orden = sorted(b, key=lambda x: (is_local(x), gr.cost_for_calls(por_key[x["key"]])))
        for x in orden:
            out.append({"m": por_key[x["key"]], "marca": "≈" if len(b) > 1 else pos[x["key"]],
                        "banda": len(b)})
        if len(out) >= 3:
            break
    return out[:3]


def frontera(cfg, all_ranked) -> list[dict]:
    """De cada familia de `familias_frontera(cfg)`, su modelo mejor ubicado en esta página. Si está en
    el grupo de cabeza no lleva puesto (`en_grupo`): ahí el puesto es ruido, igual que en la tabla."""
    pos = {m.get("key"): i for i, m in enumerate(all_ranked, 1)}
    grupo = gr.cabeza(cfg, all_ranked)
    en_grupo = {g.get("key") for g in grupo} if len(grupo) > 1 else set()
    out = []
    for fam, etiqueta in familias_frontera(cfg).items():
        m = next((x for x in all_ranked if x.get("familia") == fam and x.get("ranked")), None)
        out.append({"familia": fam, "etiqueta": etiqueta,
                    "m": ({**_modelo(m), **_eje(m, cfg), **_precio(m), "pos": pos[m["key"]],
                           "en_grupo": m["key"] in en_grupo}
                          if m else None)})
    out.sort(key=lambda f: f["m"]["pos"] if f["m"] else 10**6)
    return out


def correlacion_ordenes(cfg, models) -> float | None:
    """La misma cuenta que `generate_rankings._lleva_segunda_tabla`, devolviendo la correlación
    de puestos: la página la publica en vez de afirmar que «el eje satura»."""
    from scoring import cost_score_log
    vals = [(gr.score_for(m, cfg), m) for m in models if gr.score_for(m, cfg)]
    if len(vals) < 10:
        return None
    por_q = sorted(vals, key=lambda x: -x[0])
    por_v = sorted(vals, key=lambda x: -(0.7 * x[0] + 0.3 * cost_score_log(gr.cost_for_calls(x[1]) / 1000.0)))
    rq = {id(m): i for i, (_, m) in enumerate(por_q)}
    rv = {id(m): i for i, (_, m) in enumerate(por_v)}
    xs = [rq[k] for k in rq]
    ys = [rv[k] for k in rq]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    den = (sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys)) ** 0.5
    return round(num / den, 2) if den else None


def _segunda_tabla(cfg, all_ranked):
    if not gr._lleva_segunda_tabla(cfg, all_ranked):
        return None
    if gr.es_agentes(cfg):
        con = [m for m in all_ranked if gr.harbor_superadas(m) >= 0]
        con.sort(key=lambda m: (-gr.harbor_superadas(m), gr.cost_for_calls(m)))
        tope = gr.harbor_superadas(con[0])
        return {"tipo": "agentes", "n_tope": sum(1 for m in con if gr.harbor_superadas(m) == tope),
                "n": len(con), "tope": _eje(con[0], cfg)["harbor"],
                "filas": [{**_modelo(m), **_eje(m, cfg), **_precio(m), "rank": i}
                          for i, m in enumerate(con[:8], 1)]}
    from scoring import cost_score_log
    vals = []
    for m in all_ranked:
        q = gr.score_for(m, cfg)
        if q:
            vals.append((0.7 * q + 0.3 * cost_score_log(gr.cost_for_calls(m) / 1000.0), m))
    vals.sort(key=lambda x: -x[0])
    return {"tipo": "valor", "r": correlacion_ordenes(cfg, all_ranked),
            "filas": [{**_modelo(m), **_eje(m, cfg), **_precio(m), "rank": i, "valor": round(v, 2)}
                      for i, (v, m) in enumerate(vals[:8], 1)]}


def _veredicto(cfg, models, all_ranked):
    v = gr._verdict_data(cfg, models)
    if not v:
        return None

    def carta(c):
        m = _por_nombre(all_ranked, c["name"])
        out = {**_modelo(m), "mes": c.get("cost_month"), "sub": c.get("sub"), **_eje(m, cfg)}
        if not gr.es_agentes(cfg):
            out["calidad"] = round(c["quality"], 2) if c.get("quality") is not None else None
        return out

    b, lider = carta(v["best"]), carta(v["leader"])
    out = {"agentes": gr.es_agentes(cfg), "n": v["band_size"] or 0, "pool": v["pool_size"],
           "pct": round(v["band_share"] * 100), "inconcluso": bool(v.get("inconclusive")) and not gr.es_agentes(cfg),
           "mejor": b, "lider": lider, "mismo": v["leader"]["name"] == v["best"]["name"]}
    if v.get("priciest") and v["priciest"]["name"] != v["best"]["name"]:
        p = v["priciest"]
        out["caro"] = {**carta(p), "veces": p.get("times"), "brecha": p.get("quality_gap")}
    if v.get("local"):
        out["local"] = carta(v["local"])
    pil = cfg.get("pillar") if cfg.get("criterion") == "pillar" else None
    preset = {"Agentes": "agentes", "Coding": "coding", "Contenido": "contenido",
              "Razonamiento": "razonamiento"}.get(pil or "", "")
    out["calc"] = f"/?preset={preset}&calls=3000" if preset else "/?calls=3000"
    return out, v


def ranking(cfg: dict, models: list[dict]) -> dict:
    gr._cargar_puestos(models)
    all_ranked = gr.rank_models(models, cfg)
    if not all_ranked:
        raise SystemExit(f"sitio_rankings: /{cfg['slug']}/ no tiene modelos para su criterio")
    ranked = all_ranked[:8]

    ver = _veredicto(cfg, models, all_ranked)
    v = ver[1] if ver else None
    badges = {}
    if v:
        if v.get("best"):
            badges[v["best"]["name"]] = "← la mejor compra"
        if v.get("priciest") and v["priciest"]["name"] not in badges:
            badges[v["priciest"]["name"]] = "← el caro"
        nombres = {m.get("name") for m in ranked}
        for extra in [v.get("best"), v.get("priciest")]:
            if extra and extra["name"] not in nombres:
                m = next((x for x in all_ranked if x.get("name") == extra["name"]), None)
                if m is not None:
                    ranked.append(m)
                    nombres.add(extra["name"])
    grupo = gr.cabeza(cfg, all_ranked)
    en_grupo = {g.get("key") for g in grupo} if len(grupo) > 1 else set()
    barato = gr.mas_barato(grupo) if len(grupo) > 1 else None
    for m in ranked:
        if barato is not None and m.get("key") == barato.get("key"):
            badges.setdefault(m.get("name"), "grupo de cabeza · el más barato")
        elif m.get("key") in en_grupo:
            badges.setdefault(m.get("name"), "grupo de cabeza")
    pos_of = {m.get("key"): i for i, m in enumerate(all_ranked, 1)}
    ranked.sort(key=lambda m: pos_of.get(m.get("key"), 10**6))

    total = len(gr._PUESTO_GLOBAL) or 1
    filas = []
    for i, m in enumerate(ranked):
        pg = gr._PUESTO_GLOBAL.get(m.get("name"))
        marca = "≈" if m.get("key") in en_grupo else pos_of[m.get("key")]
        filas.append({
            **_modelo(m), **_eje(m, cfg), **_precio(m),
            "marca": marca, "top": i == 0, "badge": badges.get(m.get("name")),
            "calidad": m.get("score_calidad"), "global": round(m.get("score_global") or 0, 2),
            "puesto_global": pg, "total_global": total,
            "contraste": bool(pg and (marca == "≈" or marca <= 5) and pg > total * 0.5),
            "pilares": {p: (round(gr.pillar_quality(m, p), 1) if gr.pillar_quality(m, p) > 0 else None)
                        for p in gc.PILLARS}})

    t3 = top3_ruido(cfg, all_ranked)
    top3 = [{**_modelo(x["m"]), **_eje(x["m"], cfg), **_precio(x["m"]), "marca": x["marca"],
             "proveedor": x["m"].get("provider") or "", "abierto": bool(x["m"].get("open_source")),
             "en_grupo": x["m"].get("key") in en_grupo} for x in t3]
    if len(grupo) > 1:
        claves_t3 = {x["key"] for x in top3}
        assert claves_t3 <= {g.get("key") for g in grupo} or len(grupo) < 3, \
            f"/{cfg['slug']}/: el top 3 por ruido sale del grupo de cabeza"

    if len(grupo) > 1:
        primeros = [m.get("key") for m in all_ranked[:len(grupo)]] == [m.get("key") for m in grupo]
        cabeza = {"n": len(grupo), "keys": sorted(m.get("key") for m in grupo), "primeros": primeros, "margen": gr.margen_grupo(grupo, cfg),
                  "barato": {**_modelo(barato), **_precio(barato)},
                  "nombres": [_modelo(m) for m in grupo[:8]], "mas": max(0, len(grupo) - 8),
                  "eje_lider": _eje(all_ranked[0], cfg)}
    else:
        cabeza = None
    solo = None
    if len(grupo) == 1:
        seg = all_ranked[1] if len(all_ranked) > 1 else None
        solo = {"lider": {**_modelo(all_ranked[0]), **_eje(all_ranked[0], cfg)},
                "segundo": ({**_modelo(seg), **_eje(seg, cfg)} if seg else None)}

    hoy = date.today().isoformat()
    url = f"{gc.SITE}/{cfg['slug']}/"
    from export_for_pages import MIN_RUNS_RANKED
    criterio = "agentes" if gr.es_agentes(cfg) else cfg["criterion"]
    afirm = {"grupo_cabeza": sorted(m.get("key") for m in grupo) if len(grupo) > 1 else [],
             "mejor_compra": ver[0]["mejor"]["name"] if ver else None,
             "top3": [x["name"] for x in top3],
             "frontera": [f["m"]["name"] for f in frontera(cfg, all_ranked) if f["m"]]}
    contrato = contrato_pagina.emitir(
        tipo="ranking", generador="exportar_sitio",
        recomienda=[m.get("name") for m in ranked[:8]], ordena_por=gr.score_label(cfg),
        tablas=[{"rol": "principal", "ordena_por": gr.score_label(cfg), "filas": len(ranked[:8])}])
    return {
        "slug": cfg["slug"], "url": url, "titulo": cfg["title"], "h1": cfg["h1"],
        "keywords": cfg["intent_kw"], "lead": _lead_sitio(cfg), "que": cfg["what"],
        "caso": _caso(cfg), "usos": cfg["use_cases"], "criterio": criterio,
        "pilar": cfg.get("pillar"), "suite": cfg.get("suite"), "etiqueta": gr.score_label(cfg),
        "min_calidad": cfg.get("min_score", 8.4) if cfg["criterion"] == "cost" else None,
        "min_runs": MIN_RUNS_RANKED, "n_ranking": len(all_ranked),
        "fecha_publicada": gc.existing_published(url, hoy),
        "filas": filas, "veredicto": ver[0] if ver else None,
        "segunda": _segunda_tabla(cfg, all_ranked),
        "cabeza": cabeza, "solo": solo, "top3": top3, "frontera": frontera(cfg, all_ranked),
        "comparativa_frontera": COMPARATIVAS_FRONTERA[
            "abierta" if familias_frontera(cfg) is FAMILIAS_FRONTERA_ABIERTA else "cerrada"],
        "frontera_abierta": familias_frontera(cfg) is FAMILIAS_FRONTERA_ABIERTA,
        "relacionadas": [{"href": f"/{s}/", "texto": gr.RELATED_TITLES.get(s, s.replace("-", " ").title())}
                         for s in cfg.get("related", [])],
        "afirmaciones": afirm, "contrato_html": contrato,
    }


# ── Variantes ─────────────────────────────────────────────────────────────────

def _q(m):
    return m.get("score_calidad")


def _escalera(vs, cfg):
    """Cada suite de `SUITES_ESCALERA`: quién está arriba, con la regla del ruido de la suite
    (margen de error de `quality_ci95_by_suite`), no con el umbral fijo de 0,25 de antes."""
    cheapest, priciest = vs[0], vs[-1]
    filas, gana_caro, empates = [], [], 0
    for suite, label, desc in gv.SUITES_ESCALERA:
        vals = [(m, (m.get("quality_by_suite") or {}).get(suite)) for m in vs]
        if any(x is None for _, x in vals):
            continue
        mejor = max(vs, key=lambda m: (m.get("quality_by_suite") or {})[suite])
        cima = [m for m in vs if m is mejor or _indistinguishable(mejor, m, SUITE + suite)]
        if len(cima) == len(vs):
            veredicto, cls = {"tipo": "empatan_todos"}, "empate"
            empates += 1
        elif len(cima) > 1:
            veredicto = {"tipo": "empatan_arriba", "n": len(cima), "de": len(vs),
                         "quienes": [gv.short(m, cfg) for m in cima]}
            cls = "empate"
            empates += 1
        elif mejor is priciest:
            veredicto, cls = {"tipo": "compra"}, "compra"
            gana_caro.append(label)
        elif mejor is cheapest:
            veredicto, cls = {"tipo": "al_reves"}, "al-reves"
        else:
            veredicto, cls = {"tipo": "gana", "quien": gv.short(mejor, cfg)}, "empate"
        filas.append({"suite": suite, "label": label, "desc": desc, "clase": cls, "veredicto": veredicto,
                      "celdas": [{"v": round(x, 2), "arriba": m in cima} for m, x in vals]})
    return filas, gana_caro, empates



def variantes(cfg: dict, entrada: dict, models: list[dict]) -> dict:
    todos = gv.variants_of(models, cfg)
    vs = [m for m in todos if m.get("ranked")]
    fuera = [_fuera(m) for m in todos if not m.get("ranked")]
    hoy = date.today().isoformat()
    url = f"{gc.SITE}/{cfg['slug']}/"
    congelada = entrada.get("congelada")
    base = {"slug": cfg["slug"], "url": url, "titulo": cfg["title"], "h1": cfg["h1"],
            "keywords": cfg["intent_kw"], "familia": cfg["family"],
            "fecha_publicada": gc.existing_published(url, hoy), "post": None}

    def fila(m, marca=None):
        return {**_modelo(m), "corto": gv.short(m, cfg), "calidad": _q(m),
                "pilares": {p: round(gc.pillar(m, p), 1) for p in gc.PILLARS},
                "mes": round(gv.month(m) or 0), "latencia": round(m.get("latency_avg_s") or 0, 1),
                "global": round(m.get("score_global") or 0, 2), "runs": m.get("runs") or 0,
                "marca": marca, "no_rankea": None if m.get("ranked") else
                elegibilidad.MOTIVOS.get(((m.get("elegible") or {}).get("motivos") or {}).get("ranking"),
                                         "no entra al ranking")}

    if congelada or len(vs) < 2:
        if not congelada:
            raise SystemExit(f"sitio_rankings: /{cfg['slug']}/ tiene {len(vs)} variantes rankeadas. "
                             "Con menos de dos no hay escalera que auditar: se congela o se redirige "
                             "en el registro; no se publica con modelos fuera del ranking.")
        enlaces = [{"href": "/", "texto": "la calculadora con el ranking vigente"}]
        contrato = contrato_pagina.emitir(tipo="variantes", generador="exportar_sitio",
                                          recomienda=[m.get("name") for m in vs],
                                          nota="familia en el histórico: no elige entre tiers")
        return {**base, "historico": True, "congelada": {**congelada, "enlaces": enlaces},
                "vigentes": [fila(m) for m in vs], "filas": [fila(m) for m in vs + [x for x in todos if not x.get("ranked")]],
                "fuera": [], "afirmaciones": {"veredicto": None, "escalera": {}},
                "contrato_html": contrato}

    cheapest, priciest = vs[0], vs[-1]
    mejor_q = max(vs, key=lambda m: _q(m) or 0)
    banda = [m for m in vs if m is mejor_q or _indistinguishable(mejor_q, m, None)]
    empiece = min(banda, key=lambda m: m.get("cost_per_1k_calls_usd") or 0)
    veces = (gv.month(priciest) / gv.month(cheapest)) if gv.month(cheapest) else None
    caro_en_banda = priciest in banda
    filas_esc, gana_caro, empates = _escalera(vs, cfg)
    runs = sorted(m.get("runs") or 0 for m in vs)
    veredicto = {
        "empatan_todos": len(banda) == len(vs), "n": len(vs), "banda": len(banda),
        "mejor": fila(mejor_q), "empiece": fila(empiece), "caro": fila(priciest),
        "barato": fila(cheapest), "veces": round(veces) if veces else None,
        "empiece_es_barato": empiece is cheapest,
        "caro_en_banda": caro_en_banda,
        "caro_mas_lento": (priciest.get("latency_avg_s") or 0) > (empiece.get("latency_avg_s") or 0),
    }
    escalera = {"filas": filas_esc, "gana_caro": gana_caro, "n": len(filas_esc), "empates": empates,
                "empatan_todos": sum(1 for f in filas_esc if f["veredicto"]["tipo"] == "empatan_todos"),
                "veces": round(veces) if veces else None,
                "caro": gv.short(priciest, cfg), "barato": gv.short(cheapest, cfg),
                "columnas": [{**_modelo(m), "corto": gv.short(m, cfg),
                              "c1k": round(m.get("cost_per_1k_calls_usd") or 0, 2)} for m in vs]}
    contrato = contrato_pagina.emitir(tipo="variantes", generador="exportar_sitio",
                                      recomienda=[m.get("name") for m in vs],
                                      nota="compara versiones de una misma familia")
    afirm = {"veredicto": {"empiece": gv.short(empiece, cfg), "caro": gv.short(priciest, cfg),
                           "empatan_todos": veredicto["empatan_todos"]},
             "escalera": {f["label"]: f["veredicto"]["tipo"] for f in filas_esc}}
    return {**base, "historico": False, "congelada": None,
            "post": ({"href": cfg["post"][0], "texto": cfg["post"][1]} if cfg.get("post") else None),
            "filas": [fila(m, "barato" if m is cheapest else None) for m in vs],
            "veredicto": veredicto, "escalera": escalera,
            "runs_min": runs[0], "runs_max": runs[-1], "fuera": fuera,
            "afirmaciones": afirm, "contrato_html": contrato}
