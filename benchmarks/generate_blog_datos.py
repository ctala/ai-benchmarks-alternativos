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

Uso:
    python benchmarks/generate_blog_datos.py            # rellena los marcadores
    python benchmarks/generate_blog_datos.py --check    # exit 1 si algún valor quedó viejo
    python benchmarks/generate_blog_datos.py --blog /ruta/al/blog
"""

import argparse
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"
DEFAULT_BLOG = Path.home() / "Playground" / "sitios" / "cristiantala-blog"

MARCA_DATO = re.compile(r"<!-- D:([\w.\-+]+):([\w:]+) -->(.*?)<!-- /D -->", re.S)
MARCA_EJE = re.compile(r"<!-- V:(\w+) -->(.*?)<!-- /V -->", re.S)


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
    if campo == "velocidad":
        return f"{round(m['tokens_per_second'])} tok/s"
    if campo == "latencia":
        # Latencia TOTAL de respuesta, no time-to-first-token: el dataset no mide TTFT y
        # llamarlo así es un claim que la data no sostiene (lo dice el estándar del repo).
        # Un post del blog lo llamaba «espera hasta el primer token»; de ahí este campo.
        return f"{m['latency_avg_s']:.1f} s".replace(".", ",")
    if campo == "contexto":
        return f"{int(m['effective_context']) // 1000}K" if m.get("effective_context") else "—"
    if campo == "seguridad":
        return _num(m["security_score"]) if m.get("security_score") is not None else "—"
    raise SystemExit(f"ERROR: campo desconocido «{campo}» (calidad, precio1k, posicion, "
                     f"velocidad, contexto, seguridad)")


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
    "agentico":  lambda ms: max([m for m in ms if m.get("agentic_score") is not None],
                                key=lambda m: m["agentic_score"]),
}


def vigente(eje: str, ms: list[dict]) -> str:
    if eje not in EJES:
        raise SystemExit(f"ERROR: eje desconocido «{eje}» ({', '.join(EJES)})")
    m = EJES[eje](ms)
    if eje == "barato":
        return f"{m['name']} ({_usd(m['cost_per_1k_calls_usd'])})"
    if eje == "codigo":
        return f"{m['name']} ({_num(m['quality_by_suite']['code_generation'])})"
    if eje == "seguridad":
        return f"{m['name']} ({_num(m['security_score'])})"
    if eje == "agentico":
        return f"{m['name']} ({_num(m['agentic_score'])})"
    return f"{m['name']} ({_num(m['quality_avg'])})"


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

    def _eje(mm):
        eje, viejo = mm.group(1), mm.group(2)
        nuevo = vigente(eje, orden)
        if nuevo != viejo:
            cambios.append(f"{archivo}: vigente[{eje}] «{viejo}» → «{nuevo}»")
        return f"<!-- V:{eje} -->{nuevo}<!-- /V -->"

    texto = MARCA_DATO.sub(_dato, texto)
    texto = MARCA_EJE.sub(_eje, texto)
    return texto, cambios


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blog", default=str(DEFAULT_BLOG))
    ap.add_argument("--check", action="store_true",
                    help="no escribe: exit 1 si algún marcador quedó con un valor viejo")
    args = ap.parse_args()

    posts = Path(args.blog) / "src" / "content" / "blog"
    if not posts.is_dir():
        # Mismo criterio que el resto: el blog es otro repo y puede no estar clonado.
        print(f"  ⏭️  sin el repo del blog en {args.blog}: no se verificó ningún marcador")
        return 0
    if not MODELS_JSON.exists():
        sys.exit("Falta docs/data/models.json — corré export_for_pages.py primero")

    data = json.loads(MODELS_JSON.read_text())
    cambios, tocados, con_marcas = [], 0, 0
    for p in sorted(posts.glob("*.md")):
        texto = p.read_text()
        if "<!-- D:" not in texto and "<!-- V:" not in texto:
            continue
        con_marcas += 1
        nuevo, cs = aplicar(texto, data, p.name)
        if cs:
            cambios += cs
            if not args.check:
                p.write_text(nuevo)
                tocados += 1

    if not cambios:
        print(f"  ✅ los datos marcados en {con_marcas} post(s) coinciden con models.json")
        return 0
    for c in cambios:
        print(f"  {'❌' if args.check else '✓'} {c}")
    if args.check:
        print(f"\n  {len(cambios)} dato(s) viejos. Corré "
              f"`python benchmarks/generate_blog_datos.py` y revisá la prosa alrededor: "
              f"el marcador cambia el número, no la frase que lo explica.")
        return 1
    print(f"\n  {len(cambios)} dato(s) actualizados en {tocados} post(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
