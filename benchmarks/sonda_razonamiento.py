#!/usr/bin/env python3
"""Mide, empíricamente, CUÁNTO razona cada modelo cuando no le pedís nada.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
Cristian: *"necesitamos entender cuál es el default del proveedor para poder
documentarlo. Luego podemos mantener el mismo en los distintos tests para no mezclar o
ensuciar los resultados con distintos thinking entre mismo modelo."*

El benchmark ya declara `reasoning_medido: "default del proveedor"` para 178 modelos —
derivado del config, correcto—. Pero «el default del proveedor» es una etiqueta, no un
dato: no dice si ese default es razonar mucho, poco o nada, ni si cambia con el tiempo.

Ya se sondeó una vez, el 13-ago… y la respuesta terminó **dentro de un comentario en
`adapters.py`** («Opus 5: 87 tokens, Sonnet 5: 152, Luna: 46, Hy3: 199»). Un dato que
solo existe en un comentario no se puede citar, ni comparar contra el mes que viene, ni
detectar cuando el proveedor lo cambie sin avisar.

Esto lo convierte en una medición repetible, con salida versionada.

QUÉ MIDE
--------
Manda UN prompt corto que invita a razonar y lee `reasoning_tokens` de la respuesta. Eso
es el default real: lo que el proveedor hace cuando el cliente no configura nada — que es
el caso de quien lee este benchmark.

NO mide calidad. No puntúa. No entra a ningún ranking.

Uso:
    python benchmarks/sonda_razonamiento.py --models gpt-5.6-luna claude-opus-5
    python benchmarks/sonda_razonamiento.py --rankeados        # todos los del ranking
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.config import MODELS  # noqa: E402
from providers.registry import build_providers, provider_for  # noqa: E402

SALIDA = ROOT / "benchmarks" / "results" / "sonda_razonamiento.json"
_P = build_providers()

# Un prompt que INVITA a razonar sin exigirlo: si el modelo razona por default, se nota.
# Corto a propósito — la sonda cuesta centavos y se corre seguido.
PROMPT = [{"role": "user", "content":
           "Un producto cuesta 4.800 con IVA incluido (19%). ¿Cuál es el neto? "
           "Responde solo el número."}]


def sondear(key: str, cfg: dict, effort: str | None = None) -> dict:
    """Con `effort=None` mide el DEFAULT del proveedor; con un nivel, lo fuerza.

    Comparar las dos respuestas es lo que permite FIJAR el default: si mandar el nivel
    explícito da el mismo gasto de razonamiento que no mandar nada, se puede pinnear sin
    invalidar ninguna medición previa. Si da distinto, el default no era ese nivel — y eso
    hay que saberlo ANTES de tocar el adapter, no después de re-medir 190 modelos.
    """
    try:
        # Mismo ruteo que el runner: si falta la credencial de un provider propio,
        # `provider_for` levanta MissingCredential en vez de caer a OpenRouter con un id
        # que no le pertenece — el fallo que hizo marcar como muerto a un modelo vivo.
        prov = provider_for(cfg, _P)
        kw = {}
        if effort:
            kw["extra_body"] = {"reasoning": {"effort": effort}}
        r = prov.chat(model=cfg["id"], messages=PROMPT, max_tokens=512,
                      temperature=0.7, **kw)
        rt = (r.metadata or {}).get("reasoning_tokens")
        return {"modelo": key, "id": cfg["id"], "ok": bool(r.success),
                "reasoning_tokens": rt, "output_tokens": r.output_tokens,
                "razona_por_default": bool(rt),
                "respuesta": (r.response or "")[:60]}
    except Exception as e:
        return {"modelo": key, "id": cfg["id"], "ok": False, "error": str(e)[:120]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*")
    ap.add_argument("--rankeados", action="store_true")
    ap.add_argument("--comparar-niveles", action="store_true",
                    help="mide el default y cada nivel explícito, para saber cuál es el default")
    a = ap.parse_args()

    keys = a.models or []
    if a.rankeados:
        d = json.loads((ROOT / "docs/data/models.json").read_text())
        keys = [m["key"] for m in d["models"] if m.get("ranked")]
    if not keys:
        ap.error("pasá --models o --rankeados")

    filas = []
    for k in keys:
        cfg = MODELS.get(k)
        if not cfg:
            print(f"  ⚠️  {k}: no está en MODELS"); continue
        if a.comparar_niveles:
            base = sondear(k, cfg)
            fila = {"modelo": k, "default": base.get("reasoning_tokens")}
            for lvl in ("low", "medium", "high"):
                fila[lvl] = sondear(k, cfg, lvl).get("reasoning_tokens")
            filas.append(fila)
            print(f"  {k:<26} default={str(fila['default'] or '—'):>6}  "
                  f"low={str(fila['low'] or '—'):>6}  medium={str(fila['medium'] or '—'):>6}  "
                  f"high={str(fila['high'] or '—'):>6}")
            continue
        f = sondear(k, cfg)
        filas.append(f)
        rt = f.get("reasoning_tokens")
        estado = ("razona por default" if rt else "no razona" if f.get("ok") else "ERROR")
        print(f"  {k:<28} {str(rt or '—'):>6} tok razonamiento · {estado}")

    prev = json.loads(SALIDA.read_text()) if SALIDA.exists() else {"sondas": []}
    prev["sondas"].append({"fecha": date.today().isoformat(), "resultados": filas})
    SALIDA.write_text(json.dumps(prev, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    con = [f for f in filas if f.get("reasoning_tokens")]
    print(f"\n  {len(con)} de {len(filas)} razonan por default.")
    print(f"  ✅ {SALIDA.relative_to(ROOT)} — histórico, para detectar cuando un proveedor "
          f"cambie su default sin avisar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
