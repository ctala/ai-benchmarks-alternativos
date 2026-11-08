#!/usr/bin/env python3
"""¿El nombre visible de cada modelo trae la misma versión que su id?

POR QUÉ EXISTE (6-nov-2026)
---------------------------
`or-deepseek-v3` medía `deepseek/deepseek-v3.2` y se publicaba como «DeepSeek V3»: un
rankeado con la versión equivocada en la ficha, la página y las comparaciones. Nadie lo
vio porque nada comparaba el id con el nombre. El nombre es lo que el lector copia para
contratar el modelo; si dice otra versión, contrata otro modelo.

QUÉ VERIFICA
------------
V1. Para cada modelo de models.py: si el id trae un número de versión, el nombre visible
    empieza con la misma secuencia de números (el nombre puede traer más: «Pro 2»).
    No cuentan como versión: el tamaño (`70b`, `49b`, `16e`, `a3b`), la cuantización
    (`q4`), el multiplicador (`x2`) ni las fechas de snapshot (`0813`, `20250514`).
V2. Una excepción sin motivo es roja.
V3. Una excepción huérfana (la key no existe o ya no la necesita) es roja: si el caso se
    corrigió, la excepción tiene que salir.
V0. Catálogo vacío: el detector está ciego, rojo.

Bloqueante desde el día uno: nace en verde (las excepciones están escritas con su motivo).

Uso:  python benchmarks/check_version_en_nombre.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))

# key → motivo. Cada una dice por qué el número del id no es la versión del modelo.
EXCEPCIONES: dict[str, str] = {
    "nim-nemotron-super-1.5": "el 3.3 es la versión del Llama base del que deriva; la versión del modelo (v1.5) está en el nombre",
    "or-nemotron-super-1.5": "el 3.3 es la versión del Llama base del que deriva; la versión del modelo (v1.5) está en el nombre",
}

_TAMANO = ("b", "m", "k", "t", "e")       # 70b, 1t, 16e (expertos)
_PREFIJO_NO_VERSION = ("q", "a", "x")     # q4 (cuantización), a3b (activos), x2


def versiones(texto: str, es_id: bool) -> list[str]:
    """Secuencia de números de versión de un id o un nombre. Función pura."""
    s = texto.lower().replace("_", "-")
    if es_id:
        s = s.split("/", 1)[-1].split(":")[0]
    out: list[str] = []
    for pre, num, suf in re.findall(r"([a-z]*)(\d+(?:\.\d+)*)([a-z]*)", s):
        if suf in _TAMANO or (suf.startswith("a") and suf != "a"):
            continue
        if pre in _PREFIJO_NO_VERSION:
            continue
        if "." not in num and len(num) >= 4:      # fecha o snapshot
            continue
        out += num.split(".")
    return out


def revisar(catalogo: dict, excepciones: dict) -> dict[str, list]:
    malos, sin_motivo, huerfanas = [], [], []
    for k, c in catalogo.items():
        v_id = versiones(c["id"], True)
        v_nom = versiones(c.get("name", k), False)
        if v_id and v_nom[:len(v_id)] != v_id:
            if k in excepciones:
                continue
            malos.append((k, c["id"], c.get("name", k), v_id, v_nom))
        elif k in excepciones:
            huerfanas.append((k, "ya no la necesita: el nombre trae la versión"))
    for k, motivo in excepciones.items():
        if k not in catalogo:
            huerfanas.append((k, "la key no existe en models.py"))
        if not str(motivo or "").strip():
            sin_motivo.append(k)
    return {"malos": malos, "sin_motivo": sin_motivo, "huerfanas": huerfanas}


def main(catalogo: dict | None = None, excepciones: dict | None = None) -> int:
    if catalogo is None:
        from models import MODELS, OLLAMA_MODELS
        catalogo = {**OLLAMA_MODELS, **MODELS}
    excepciones = EXCEPCIONES if excepciones is None else excepciones
    if not catalogo:
        print("❌ V0 catálogo vacío: el detector está ciego")
        return 1
    r = revisar(catalogo, excepciones)
    print(f"VERSIÓN EN EL NOMBRE · {len(catalogo)} modelos · {len(excepciones)} excepción(es)\n")
    for k, mid, nom, a, b in r["malos"]:
        print(f"  ❌ V1 {k}: id `{mid}` trae {'.'.join(a)} y el nombre «{nom}» "
              f"trae {'.'.join(b) or 'ninguna'}")
    for k in r["sin_motivo"]:
        print(f"  ❌ V2 excepción sin motivo: {k}")
    for k, por in r["huerfanas"]:
        print(f"  ❌ V3 excepción huérfana: {k} ({por})")
    if any(r.values()):
        print("\n  El nombre es lo que el lector copia para contratar el modelo: si trae otra"
              "\n  versión, contrata otro. Se corrige el nombre (con `nombres_anteriores`) o"
              "\n  se agrega una excepción con su motivo.")
        return 1
    print("  ✅ todos los nombres traen la versión de su id")
    return 0


if __name__ == "__main__":
    sys.exit(main())
