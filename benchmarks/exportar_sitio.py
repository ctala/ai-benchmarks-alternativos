#!/usr/bin/env python3
"""Python decide, Astro dibuja: los datos de cada página del sitio nuevo. (11-nov-2026)

POR QUÉ EXISTE
--------------
Change `motor-sitio`, D2. Las plantillas de Astro no deciden nada: quién gana, qué filas
entran, qué modelo sale del ranking y por qué, todo llega acá calculado con el MISMO código
que usa `generate_comparison.py` (`family`, `datos_eje`, `datos_pilares`, `extremos`,
`ganador_calidad`). Reimplementarlo en JS serían dos autoridades de lo mismo.

Escribe `sitio/src/datos/` (ignorado por git; lo regenera `npm run build`):
  - `registro.json`: las páginas que compila Astro (`registro_paginas.py`);
  - `meta.json`: conteos, pesos, fechas y el sha de `models.json`;
  - `comparaciones/<slug>.json`: todo lo que muestra cada comparación;
  - `rankings/<slug>.json` y `variantes/<slug>.json`: lo mismo para los rankings «Mejor LLM
    para…» y las páginas de variantes (`sitio_rankings.py`, sesión 2).

R1 ESTRICTA (Cristian, 11-nov-2026, opción A): una comparación por familia muestra solo
modelos rankeados. Los que salen van en `fuera`, con su motivo y su ficha, para el pie
«Versiones anteriores →» y para la paridad. Una congelada se compila con los datos de hoy,
tal como la publica Python, y arriba lleva el aviso (D7).

Uso:
    python benchmarks/exportar_sitio.py
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))
sys.path.insert(0, str(ROOT))

import contrato_pagina  # noqa: E402
import elegibilidad  # noqa: E402
import generate_comparison as gc  # noqa: E402
import registro_paginas as rp  # noqa: E402
import sitio_rankings as sr  # noqa: E402

SALIDA = ROOT / "sitio" / "src" / "datos"
DOCS = ROOT / "sitio" / "legado"


def _ficha(m) -> str | None:
    k = m.get("key")
    return f"/modelo/{k}/" if k and (DOCS / "modelo" / k / "index.html").exists() else None


def _modelo(m) -> dict:
    """Lo mínimo que una plantilla necesita para nombrar a un modelo y enlazarlo."""
    return {"key": m.get("key"), "name": m.get("name"), "ranked": bool(m.get("ranked")),
            "ficha": _ficha(m) if m.get("ranked") else None}


def medido(m) -> dict:
    """«Medido en»: el proveedor que sirvió la mayoría de los runs (y qué parte, si no fueron
    todos), su cuantización y el razonamiento con que se llamó. Sale de `medido_en` y
    `reasoning_medido` del export; lo que no está registrado se dice, no se supone. Función pura.
    (motor-sitio 2.4)"""
    me = m.get("medido_en") or {}
    pct = me.get("proveedor_pct")
    return {"proveedor": me.get("proveedor") or "proveedor sin registrar",
            "pct": pct if me.get("proveedor") and pct is not None and pct < 100 else None,
            "cuantizacion": me.get("cuantizacion") or "cuantización no declarada",
            "razonamiento": m.get("reasoning_medido") or "sin registrar"}


def linea_medido_en(m) -> str:
    """La misma línea como texto plano: lo que la página tiene que mostrar (guardrail M1)."""
    x = medido(m)
    pct = f" ({x['pct']} % de los runs)" if x["pct"] is not None else ""
    return f"{x['proveedor']}{pct} · {x['cuantizacion']} · razonamiento: {x['razonamiento']}"


def _fila(rank, m, top):
    c = gc.capacidad(m)
    motivo = ((m.get("elegible") or {}).get("motivos") or {}).get("ranking")
    return {**_modelo(m), "rank": rank, "top": top,
            "no_rankea": None if m.get("ranked") else elegibilidad.MOTIVOS.get(motivo, "no entra al ranking"),
            "calidad": round(c, 2) if c >= 0 else None,
            "pilares": {p: (round(gc.pillar(m, p), 1) if gc.pillar(m, p) > 0 else None) for p in gc.PILLARS},
            "costo_in": round(m.get("cost_input_per_M") or 0, 2),
            "costo_out": round(m.get("cost_output_per_M") or 0, 2),
            "tps": round(m.get("tokens_per_second") or 0),
            "medido": medido(m), "medido_en": linea_medido_en(m)}


def _fuera(m) -> dict:
    motivo = ((m.get("elegible") or {}).get("motivos") or {}).get("ranking")
    return {"key": m.get("key"), "name": m.get("name"), "motivo": motivo,
            "motivo_texto": elegibilidad.MOTIVOS.get(motivo, motivo),
            "ficha": _ficha(m)}


def _campeon(m):
    if not m:
        return None
    return {**_modelo(m), "runs": m.get("runs", 0)}


def comparacion(cfg: dict, entrada: dict, models: list[dict]) -> dict:
    A_todos, B_todos = gc.family(models, cfg["a"]), gc.family(models, cfg["b"])
    congelada = entrada.get("congelada")
    if congelada:
        A, B = A_todos, B_todos
        fuera = []
    else:
        A = [m for m in A_todos if m.get("ranked")]
        B = [m for m in B_todos if m.get("ranked")]
        fuera = [_fuera(m) for m in A_todos + B_todos if not m.get("ranked")]
    if not A or not B:
        raise SystemExit(f"exportar_sitio: /{cfg['slug']}/ se queda sin modelos rankeados en un lado. "
                         "Se congela o se redirige en el registro; no se publica vacía.")

    # El orden de la tabla es el de Python (6-nov-2026): rankeados de A, de B, y al final
    # los que no rankean (solo pueden quedar en una congelada).
    vis = A[:5] + B[:5]
    cola = sorted([m for m in vis if not m.get("ranked")], key=lambda m: -gc.capacidad(m))
    orden = [m for m in A[:5] if m.get("ranked")] + [m for m in B[:5] if m.get("ranked")] + cola
    foto = gc.es_foto_historica(A, B)
    filas = [_fila(i + 1, m, top=(i == 0 and not foto)) for i, m in enumerate(orden)]

    ca, cb = gc.campeon(A), gc.campeon(B)
    eje = gc.datos_eje(ca, cb) if not foto else None
    pilares, extremos, ganador = [], None, None
    if not foto:
        for v in gc.datos_pilares(A, B):
            p = v["pilar"]
            d = {"pilar": p, "label": v["label"], "que_mide": v["what"], "empate": v["empate"]}
            if v["empate"]:
                d["a"], d["b"] = _modelo(v["ba"]), _modelo(v["bb"])
                d["nota_max"] = round(max(gc.pillar(v["ba"], p), gc.pillar(v["bb"], p)), 1)
                d["barato"] = {**_modelo(v["cheaper"]), "costo_in": round(v["cheaper"].get("cost_input_per_M") or 0, 2),
                               "costo_out": round(v["cheaper"].get("cost_output_per_M") or 0, 2)}
                d["otro"] = _modelo(v["other"])
            else:
                d["gana"] = {**_modelo(v["w"]), "nota": round(gc.pillar(v["w"], p), 1),
                             "costo_in": round(v["w"].get("cost_input_per_M") or 0, 2),
                             "costo_out": round(v["w"].get("cost_output_per_M") or 0, 2)}
                d["pierde"] = {**_modelo(v["l"]), "nota": round(gc.pillar(v["l"], p), 1)}
                d["margen"] = round(v["margin"], 1)
                d["fuerza"] = v["strength"]
            pilares.append(d)
        cheap, fast = gc.extremos(A, B)
        extremos = {"barato": {**_modelo(cheap), "costo_in": round(cheap.get("cost_input_per_M") or 0, 2),
                               "costo_out": round(cheap.get("cost_output_per_M") or 0, 2)},
                    "rapido": {**_modelo(fast), "tps": round(fast.get("tokens_per_second") or 0)}}
        w, l, emp = gc.ganador_calidad(A[0], B[0])
        ganador = {"empate": bool(emp), "gana": {**_modelo(w), "nota": w.get("score_calidad")},
                   "pierde": {**_modelo(l), "nota": l.get("score_calidad")}}

    enlaces = []
    if congelada:
        fam = gc.pagina_familia(cfg)
        if fam:
            fcfg = next(c for c in gc.COMPARISONS if c["slug"] == fam)
            enlaces.append({"href": f"/{fam}/", "texto": " vs ".join(gc.etiquetas_titulo(fcfg["title"]))})
        enlaces.append({"href": "/", "texto": "la calculadora con el ranking vigente"})
        congelada = {**congelada, "enlaces": enlaces}

    url = f"{gc.SITE}/{cfg['slug']}/"
    contrato = contrato_pagina.emitir(
        tipo="comparacion", generador="exportar_sitio",
        recomienda=[] if foto else [m.get("name") for m in vis],
        ordena_por="Calidad (media de los 4 pilares)",
        tablas=[{"rol": "principal", "ordena_por": "Calidad", "filas": len(vis), "bloques": 2}])
    return {
        "slug": cfg["slug"], "url": url, "titulo": cfg["title"], "keywords": cfg["intent_kw"],
        "a": cfg["a"]["name"], "b": cfg["b"]["name"],
        "congelada": congelada, "foto": foto,
        "fecha_publicada": gc.existing_published(url, date.today().isoformat()),
        "versiones": {"a": [m["name"] for m in A[:6]], "a_mas": max(0, len(A) - 6),
                      "b": [m["name"] for m in B[:6]], "b_mas": max(0, len(B) - 6)},
        "filas": filas, "fuera": fuera,
        "campeones": {"a": _campeon(ca), "b": _campeon(cb)},
        "eje": eje, "pilares": pilares, "extremos": extremos, "ganador": ganador,
        "contrato_html": contrato,
    }


def models_sha(ruta: Path | None = None) -> str:
    """La huella de `models.json` que cada página de Astro lleva en `<meta name="datos-sha">`.
    `check_datos_dist` la compara con la del `models.json` de ahora: un `dist` compilado con
    datos de ayer no se publica (motor-sitio 2.5)."""
    ruta = ruta or DOCS / "data" / "models.json"
    return hashlib.sha256(ruta.read_bytes()).hexdigest()[:16]


def meta(d: dict) -> dict:
    c = gc.get_counts()
    w = d.get("default_weights", {})
    return {"modelos_catalogados": c["total_models"], "modelos_testeados": c["tested_count"],
            "runs_k": (c["total_runs"] // 1000) * 1000, "pilares": gc.PILLARS,
            "pilar_desc": {p: {"titulo": gc.PILLAR_DESC[p][0], "que": gc.PILLAR_DESC[p][1]} for p in gc.PILLARS},
            "pesos": {k: round(w.get(k, 0) * 100, 1) for k in ("quality", "cost", "speed", "latency", "tool_calling")},
            "hoy": date.today().isoformat(),
            # El año de un título sale de la medición, nunca fijo (motor-sitio 2.4).
            "anio": __import__("fechas").anio(d),
            "models_sha": models_sha()}


def main() -> int:
    regs = rp.paginas()
    fallos = rp.errores(regs)
    if fallos:
        print("exportar_sitio: el registro no es coherente:\n  " + "\n  ".join(fallos))
        return 1
    d = gc.load_json()
    contra = elegibilidad.contradicciones(d["models"])
    if contra:
        print("exportar_sitio: models.json se contradice (R5):\n  " + "\n  ".join(contra))
        return 1
    models = gc.load_models()
    por_slug = {c["slug"]: c for c in gc.COMPARISONS}
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    for sub in ("comparaciones", "rankings", "variantes"):
        (SALIDA / sub).mkdir(parents=True)
    astro = [e for e in regs if e["motor"] == "astro"]
    for e in astro:
        if e["redirect_a"]:
            # El redirect también declara qué es (`generate_comparison._contrato_redirect`).
            e["destino"] = f"{gc.SITE}/{e['redirect_a']}/"
            e["contrato_html"] = contrato_pagina.emitir(
                tipo="redirect", generador="exportar_sitio", recomienda=[], nota=e["motivo"])
    (SALIDA / "registro.json").write_text(json.dumps(astro, ensure_ascii=False, indent=1), encoding="utf-8")
    (SALIDA / "meta.json").write_text(json.dumps(meta(d), ensure_ascii=False, indent=1), encoding="utf-8")
    import generate_rankings as gr
    import generate_variants as gv
    rk = {c["slug"]: c for c in gr.RANKINGS}
    va = {c["slug"]: c for c in gv.FAMILIES}
    n = {"comparacion": 0, "ranking": 0, "variantes": 0}
    for e in astro:
        if e["redirect_a"] or e["tipo"] not in n:
            continue
        if e["tipo"] == "comparacion":
            datos, sub = comparacion(por_slug[e["slug"]], e, models), "comparaciones"
        elif e["tipo"] == "ranking":
            datos, sub = sr.ranking(rk[e["slug"]], models), "rankings"
        else:
            datos, sub = sr.variantes(va[e["slug"]], e, models), "variantes"
        (SALIDA / sub / f"{e['slug']}.json").write_text(
            json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
        n[e["tipo"]] += 1
    print(f"✓ sitio/src/datos: {len(astro)} páginas Astro ({n['comparacion']} comparaciones, "
          f"{n['ranking']} rankings, {n['variantes']} variantes, "
          f"{sum(1 for e in astro if e['redirect_a'])} redirects)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
