#!/usr/bin/env python3
"""Rellena en los posts del blog los datos de un modelo y quién manda hoy en cada eje.

POR QUÉ EXISTE (16-sep-2026)
----------------------------
Es el hermano chico de `generate_blog_tablas.py`, y nació de una medición que mató la idea
anterior. El plan era **verificar** los precios que citan los posts (369 menciones en 33
posts). No funciona: cuando una línea nombra dos modelos y dos precios —una fila de tabla, una
comparación— atribuir «este precio es de este modelo» se equivoca, y la regla acusaba a
«Opus 4.8» por el precio de Luna. Acotarla a líneas inequívocas la deja en 10 de 369 (3% de
cobertura) y aun así con dos falsos positivos. Un bloqueante así nace rojo y se aprende a
ignorar.

Lo que sí funcionó con las tablas del pilar: **lo que se genera no se verifica**. Así que en
vez de un detector de precios, marcadores que el generador rellena:

    <!-- D:qwen3.8-flash:calidad -->8,53<!-- /D -->      un dato de UN modelo
    <!-- V:codigo -->Granite 4.2 8B (9,77)<!-- /V -->    quién manda HOY en un eje

El segundo existe por el otro agujero, que abrí yo mismo: los bloques «¿Llegaste buscando qué
usar hoy?» que se agregaron a 7 posts afirman a mano quién es el mejor. El día que cambie el
ranking, esos puentes mienten en silencio — la misma deuda que se acababa de pagar.

NO lo corre `regenerate_all.py`: el blog es otro repo y otras sesiones empujan su `main`.
Escribir ahí en silencio es publicar sin revisión. Se corre a mano, y el hook de pre-push del
blog usa `--check`.

POR DEFECTO NO ESCRIBE (8-nov-2026). Escribir exige `--write`. Antes bastaba olvidar `--check`
para reescribir 54 cifras en 8 posts: pasó en una sesión que solo quería listar el drift, y
escribió en el worktree del blog que esperaba aprobación. Sin flags, verifica.

Los posts CONGELADOS (`benchmarkEra` + nota visible, ver `check_blog_consistency.congelado`)
no se tocan: son del examen anterior y una cifra v5 mezclaría dos exámenes. Un post congelado
a medias (una marca sin la otra) es error, con o sin `--write`.

Uso:
    python benchmarks/generate_blog_datos.py                  # verifica: exit 1 si algo quedó viejo
    python benchmarks/generate_blog_datos.py --write          # rellena los marcadores
    python benchmarks/generate_blog_datos.py --blog /ruta/al/blog
"""

import argparse
import os
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
# `BENCH_BLOG` apunta los chequeos a otro checkout (un worktree que espera aprobación) sin
# tocar el principal; qa.py avisa cuando está puesta (8-nov-2026).
DEFAULT_BLOG = Path(os.environ.get("BENCH_BLOG")
                    or Path.home() / "Playground" / "sitios" / "cristiantala-blog")

MARCA_DATO = re.compile(r"<!-- D:([\w.\-+]+):([\w:]+) -->(.*?)<!-- /D -->", re.S)
MARCA_EJE = re.compile(r"<!-- V:([\w:]+) -->(.*?)<!-- /V -->", re.S)
# Un dato de TODO el ranking, no de un modelo (8-nov-2026): la mediana de seguridad y la
# correlación precio-calidad estaban escritas a mano en el pilar y en la guía.
MARCA_GLOBAL = re.compile(r"<!-- G:([\w]+) -->(.*?)<!-- /G -->", re.S)


def _num(x) -> str:
    """8.53 → «8,53». El blog escribe los decimales con coma."""
    return f"{x:.2f}".replace(".", ",")


def _usd(x) -> str:
    """0.795 → «$0,80» — media vuelta arriba, como se leen los precios."""
    d = Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return "$" + str(d).replace(".", ",")


def rankeados(data: dict) -> list[dict]:
    return sorted([m for m in data["models"] if m.get("ranked")],
                  key=lambda m: -(m.get("quality_avg") or 0))


def dato(m: dict, campo: str, orden: list[dict]) -> str:
    """El valor de UN modelo. Campos deliberadamente pocos: los que el blog cita."""
    if campo.startswith("suite:"):
        # `suite:code_generation` — la nota del modelo en UNA suite. Existe por las tablas
        # «qué le pides a cada tier» del post de GPT-5.6: 24 celdas que, escritas a mano,
        # envejecieron hasta dar vuelta la conclusión (decía que el caro ganaba dos de ocho;
        # hoy no gana ninguna).
        clave = campo.split(":", 1)[1]
        v = (m.get("quality_by_suite") or {}).get(clave)
        if v is None:
            raise SystemExit(f"ERROR: «{m['name']}» no tiene medida la suite «{clave}». "
                             f"Un post no puede citar una nota que no existe.")
        return _num(v)
    if campo == "calidad":
        return _num(m["quality_avg"])
    if campo == "precio1k":
        return _usd(m["cost_per_1k_calls_usd"])
    if campo == "posicion":
        return str(orden.index(m) + 1)
    if campo == "puesto_compuesto":
        # El puesto en el SCORE COMPUESTO (calidad + costo + velocidad + latencia), que es
        # otro orden que `posicion` (calidad pura). Existe porque dos posts escribían a mano
        # «puesto 51» y «puesto 90» del compuesto y ya no coincidían (4-nov-2026).
        por_score = sorted(orden, key=lambda x: -x["score_global"])
        return str(por_score.index(m) + 1)
    if campo == "compuesto":
        return _num(m["score_global"])
    if campo == "velocidad":
        return f"{round(m['tokens_per_second'])} tok/s"
    if campo == "latencia":
        # Latencia TOTAL de respuesta, no time-to-first-token: el dataset no mide TTFT y
        # llamarlo así es un claim que la data no sostiene (lo dice el estándar del repo).
        # Un post del blog lo llamaba «espera hasta el primer token»; de ahí este campo.
        return f"{m['latency_avg_s']:.1f} s".replace(".", ",")
    if campo == "contexto":
        return f"{int(m['effective_context']) // 1000}K" if m.get("effective_context") else "—"
    if campo == "harbor":
        ok, n = _harbor(m)
        if not n:
            raise SystemExit(f"ERROR: «{m['name']}» no tiene tareas agénticas de Harbor medidas.")
        return f"{ok} de {n}"
    if campo == "seguridad":
        return _num(m["security_score"]) if m.get("security_score") is not None else "—"
    raise SystemExit(f"ERROR: campo desconocido «{campo}» (calidad, precio1k, posicion, "
                     f"puesto_compuesto, compuesto, velocidad, contexto, seguridad, harbor)")


# Cada eje es una pregunta que un post le hace al ranking: «¿quién manda hoy en esto?».
# La clave es que la respuesta salga del dato, no de la memoria de quien escribió el post.
EJES = {
    "calidad":   lambda ms: max(ms, key=lambda m: m["quality_avg"]),
    "compuesto": lambda ms: max(ms, key=lambda m: m["score_global"]),
    "barato":    lambda ms: min(ms, key=lambda m: m["cost_per_1k_calls_usd"]),
    "abierto":   lambda ms: max([m for m in ms if m.get("open_source")],
                                key=lambda m: m["quality_avg"]),
    "codigo":    lambda ms: max([m for m in ms if (m.get("quality_by_suite") or {}).get("code_generation")],
                                key=lambda m: m["quality_by_suite"]["code_generation"]),
    "seguridad": lambda ms: max([m for m in ms if m.get("security_score") is not None],
                                key=lambda m: m["security_score"]),
    # El más barato de los que superan TODAS las tareas agénticas de Harbor en todos sus
    # intentos. Es «barato entre los que no fallan», no «el mejor»: en Harbor los perfectos
    # empatan, así que la decisión entre ellos es de precio.
    "harbor_barato": lambda ms: min([m for m in ms if _harbor(m)[0] and _harbor(m)[0] == _harbor(m)[1]],
                                    key=lambda m: m["cost_per_1k_calls_usd"]),
}

# 8-nov-2026: el eje `agentico` leía `agentic_score`, que NO es trabajo agéntico: es el
# compuesto (calidad + costo + velocidad) de `agent_long_horizon`, una suite multi-turno
# sin herramientas (ver export_for_pages, «SE LLAMABA agentic_score Y ERA UNA ETIQUETA
# FALSA»). El pilar lo publicaba como «tareas agénticas reales en Docker». Un marcador
# viejo con ese eje falla en vez de seguir publicando la etiqueta falsa.
EJES_RETIRADOS = {
    "agentico": "lee agentic_score, que es el compuesto multi-turno sin herramientas, no "
                "trabajo agéntico. Usa `harbor_barato` o el dato `D:<key>:harbor`.",
}


def _harbor(m: dict) -> tuple[int, int]:
    """(tareas superadas en todos sus intentos, tareas medidas) en Harbor."""
    tareas = ((m.get("agentico") or {}).get("tareas") or {}).values()
    return sum(1 for x in tareas if x.get("estado") == "ok_siempre"), len(tareas)


def _landings():
    """El elegidor de las landings: un solo criterio de «quién lidera» para el sitio y el blog."""
    sys.path.insert(0, str(ROOT / "benchmarks"))
    import generate_manual_landings as g
    return g


def vigente_compuesto(eje: str, data: dict) -> str:
    """`pilar:<Pilar>` o `suite:<suite>`, con `:nombre` / `:nota` y un puesto opcional.

        <!-- V:pilar:Agentes -->Qwen 3.7 Flash (8,12)<!-- /V -->
        <!-- V:suite:tool_calling:nombre -->Gemini 3.1 Flash Lite<!-- /V -->
        <!-- V:suite:tool_calling:nota:2 -->7,10<!-- /V -->

    Elige `generate_manual_landings._lider`: conjunto base (rankeado, recomendable, sin
    `unavailable` ni `pendiente_proveedor`) y el desempate de DECISIONES (4-nov-2026). Existe
    porque el blog recomendaba a mano a modelos retirados («DeepSeek R1 (7,45)» en tool calling).
    """
    partes = eje.split(":")
    tipo, cual, resto = partes[0], partes[1] if len(partes) > 1 else "", partes[2:]
    puesto = int(resto.pop()) if resto and resto[-1].isdigit() else 1
    forma = resto[0] if resto else "ambos"
    if forma not in ("ambos", "nombre", "nota") or not cual:
        raise SystemExit(f"ERROR: marcador «V:{eje}» mal formado (pilar|suite:<cual>[:nombre|:nota][:n])")
    g = _landings()
    if tipo == "pilar":
        m = g._lider_pilar_modelo(data, cual, puesto)
        nota = m["score_by_pillar"][cual]
    elif tipo == "suite":
        m = g._lider(data, lambda x: (x.get("quality_by_suite") or {}).get(cual),
                     lambda x: x.get("quality_avg") or 0, puesto, f"suite {cual}")
        nota = m["quality_by_suite"][cual]
    else:
        raise SystemExit(f"ERROR: eje desconocido «{eje}»")
    if forma == "nombre":
        return m["name"]
    if forma == "nota":
        return _num(nota)
    return f"{m['name']} ({_num(nota)})"


def vigente(eje: str, ms: list[dict]) -> str:
    if eje in EJES_RETIRADOS:
        raise SystemExit(f"ERROR: el eje «{eje}» está retirado: {EJES_RETIRADOS[eje]}")
    if eje not in EJES:
        raise SystemExit(f"ERROR: eje desconocido «{eje}» ({', '.join(EJES)})")
    m = EJES[eje](ms)
    if eje == "barato":
        return f"{m['name']} ({_usd(m['cost_per_1k_calls_usd'])})"
    if eje == "codigo":
        return f"{m['name']} ({_num(m['quality_by_suite']['code_generation'])})"
    if eje == "seguridad":
        return f"{m['name']} ({_num(m['security_score'])})"
    if eje == "harbor_barato":
        return f"{m['name']} ({_usd(m['cost_per_1k_calls_usd'])})"
    return f"{m['name']} ({_num(m['quality_avg'])})"


def global_(campo: str, data: dict) -> str:
    """`G:seguridad_mediana` → «2,50» · `G:correlacion_precio` → «+0,16» ·
    `G:precio_explica_pct` → «3» (el % de la diferencia de calidad que explica el precio)."""
    if campo == "seguridad_mediana":
        v = (data.get("seguridad_mediana") or {}).get("mediana")
        if v is None:
            raise SystemExit("ERROR: models.json no trae `seguridad_mediana`.")
        return _num(v)
    if campo == "seguridad_medidos":
        v = (data.get("seguridad_mediana") or {}).get("de")
        if not v:
            raise SystemExit("ERROR: models.json no trae `seguridad_mediana`.")
        return str(v)
    pc = data.get("precio_calidad") or {}
    if campo == "correlacion_precio":
        if pc.get("pearson") is None:
            raise SystemExit("ERROR: models.json no trae `precio_calidad`.")
        return ("+" if pc["pearson"] >= 0 else "−") + _num(abs(pc["pearson"]))
    if campo == "precio_explica_pct":
        if pc.get("r2_pct") is None:
            raise SystemExit("ERROR: models.json no trae `precio_calidad`.")
        return str(pc["r2_pct"])
    raise SystemExit(f"ERROR: dato global desconocido «{campo}» "
                     "(seguridad_mediana, seguridad_medidos, correlacion_precio, precio_explica_pct)")


def aplicar(texto: str, data: dict, archivo: str) -> tuple[str, list[str]]:
    orden = rankeados(data)
    por_key = {m["key"]: m for m in data["models"]}
    cambios = []

    def _dato(mm):
        key, campo, viejo = mm.group(1), mm.group(2), mm.group(3)
        m = por_key.get(key)
        if m is None:
            raise SystemExit(f"ERROR: {archivo} cita el modelo «{key}», que no está en "
                             f"models.json. Un post no puede apuntar a un modelo inexistente.")
        nuevo = dato(m, campo, orden)
        if nuevo != viejo:
            cambios.append(f"{archivo}: {key}.{campo} «{viejo}» → «{nuevo}»")
        return f"<!-- D:{key}:{campo} -->{nuevo}<!-- /D -->"

    base = {m["key"] for m in _landings()._conjunto_base(data)}
    orden_base = [m for m in orden if m["key"] in base]

    def _eje(mm):
        eje, viejo = mm.group(1), mm.group(2)
        nuevo = vigente_compuesto(eje, data) if ":" in eje else vigente(eje, orden_base)
        if nuevo != viejo:
            cambios.append(f"{archivo}: vigente[{eje}] «{viejo}» → «{nuevo}»")
        return f"<!-- V:{eje} -->{nuevo}<!-- /V -->"

    def _global(mm):
        campo, viejo = mm.group(1), mm.group(2)
        nuevo = global_(campo, data)
        if nuevo != viejo:
            cambios.append(f"{archivo}: global[{campo}] «{viejo}» → «{nuevo}»")
        return f"<!-- G:{campo} -->{nuevo}<!-- /G -->"

    texto = MARCA_DATO.sub(_dato, texto)
    texto = MARCA_EJE.sub(_eje, texto)
    texto = MARCA_GLOBAL.sub(_global, texto)
    return texto, cambios


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blog", default=str(DEFAULT_BLOG))
    modo = ap.add_mutually_exclusive_group()
    modo.add_argument("--check", action="store_true",
                      help="no escribe: exit 1 si algún marcador quedó con un valor viejo "
                           "(es el comportamiento por defecto)")
    modo.add_argument("--write", action="store_true",
                      help="escribe los valores nuevos en los posts")
    args = ap.parse_args()
    args.check = not args.write

    posts = Path(args.blog) / "src" / "content" / "blog"
    if not posts.is_dir():
        # Mismo criterio que el resto: el blog es otro repo y puede no estar clonado.
        print(f"  ⏭️  sin el repo del blog en {args.blog}: no se verificó ningún marcador")
        return 0
    if not MODELS_JSON.exists():
        sys.exit("Falta docs/data/models.json — corré export_for_pages.py primero")

    sys.path.insert(0, str(ROOT / "benchmarks"))
    from check_blog_consistency import congelado

    data = json.loads(MODELS_JSON.read_text())
    cambios, tocados, con_marcas, congelados, a_medias = [], 0, 0, 0, []
    for p in sorted(posts.glob("*.md")):
        texto = p.read_text()
        frio, error = congelado(texto)
        if error:
            a_medias.append(f"{p.name}: post congelado a medias — {error}")
            continue
        if frio:
            congelados += 1
            continue
        if "<!-- D:" not in texto and "<!-- V:" not in texto and "<!-- G:" not in texto:
            continue
        con_marcas += 1
        nuevo, cs = aplicar(texto, data, p.name)
        if cs:
            cambios += cs
            if not args.check:
                p.write_text(nuevo)
                tocados += 1

    for e in a_medias:
        print(f"  ❌ {e}")
    if a_medias:
        print("\n  Un post congelado necesita las dos marcas: `benchmarkEra` en el frontmatter y la "
              "nota visible arriba del primer ##. No se escribió nada en esos posts.")
    if not cambios:
        if a_medias:
            return 1
        print(f"  ✅ los datos marcados en {con_marcas} post(s) coinciden con models.json "
              f"({congelados} congelado(s) en su era, sin tocar)")
        return 0
    for c in cambios:
        print(f"  {'❌' if args.check else '✓'} {c}")
    if args.check:
        print(f"\n  {len(cambios)} dato(s) viejos. Corré "
              f"`python benchmarks/generate_blog_datos.py --write` y revisá la prosa alrededor: "
              f"el marcador cambia el número, no la frase que lo explica.")
        return 1
    print(f"\n  {len(cambios)} dato(s) actualizados en {tocados} post(s).")
    return 1 if a_medias else 0


if __name__ == "__main__":
    sys.exit(main())
