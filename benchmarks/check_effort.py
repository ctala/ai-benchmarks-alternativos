#!/usr/bin/env python3
"""Verifica que el effort de razonamiento salga de la regla, no de un string fijo.

POR QUÉ EXISTE (14-sep-2026)
----------------------------
Del 2 al 14-sep se mandó `effort: medium` a todo thinking model por OpenRouter. Nadie lo
contrastó con lo que cada modelo declara soportar, y en 10 de los rankeados `medium` no
era un nivel válido: GLM 5.3 reportaba 0 tokens de razonamiento contra 619 de su default.
La regla era razonable; faltaba el instrumento. La vigente —el examen es el default de
cada modelo, y se sabe cuál es— está en `effort.py`.

QUÉ VERIFICA
------------
E1. Todo modelo del catálogo que va por OpenRouter está en la foto (o en sus ausentes).
    Uno nuevo sin foto rendiría sin que el run sepa en qué modo lo hizo.
E2. Todo `reasoning_effort` declarado en un test es un nivel que existe. Y que el
    detector haya leído tests: un E2 que no encuentra ninguno está ciego, no en verde.
E3. Sobre CADA modelo de la foto y CADA nivel:
      · sin pedido no se manda nada, y la etiqueta registra el default declarado;
      · un pedido nunca manda un effort fuera de `supported_efforts`;
      · nunca se le enciende el razonamiento a un modelo con `default_enabled: false`.
E4. (aviso) la foto tiene más de 45 días: el default de un proveedor pudo cambiar.
    Se confirma con `python benchmarks/effort.py --vivo`.

Uso:  python benchmarks/check_effort.py
"""
import importlib.util
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "benchmarks"))

from benchmarks import effort  # noqa: E402

DIAS_AVISO = 45
MIN_TESTS = 100   # hay más de 200; bajo esto el detector no está leyendo lo que cree


def e1_cobertura(foto: dict, catalogo: dict) -> list[str]:
    conocidos = set(foto.get("modelos", {})) | set(foto.get("ausentes", []))
    return [f"E1 {k} ({c['id']}) no está en la foto — correr `effort.py --actualizar`"
            for k, c in sorted(catalogo.items())
            if c.get("id") and c.get("provider", "openrouter") == "openrouter"
            and not c.get("retired") and c["id"] not in conocidos]


def _tests_declarados() -> list[tuple[str, dict]]:
    out = []
    for py in sorted((ROOT / "benchmarks" / "tests").glob("*.py")):
        if py.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"_check_effort_{py.stem}", py)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for v in vars(mod).values():
            if isinstance(v, list):
                out += [(py.stem, t) for t in v
                        if isinstance(t, dict) and "name" in t
                        and ("messages" in t or "reasoning_effort" in t)]
    return out


def e2_niveles(tests: list[tuple[str, dict]]) -> list[str]:
    if len(tests) < MIN_TESTS:
        return [f"E2 sólo leyó {len(tests)} tests (se esperan ≥{MIN_TESTS}): el detector "
                "está ciego, no en verde"]
    return [f"E2 {archivo}/{t['name']}: reasoning_effort={t['reasoning_effort']!r} no es "
            f"un nivel ({', '.join(effort.NIVELES)})"
            for archivo, t in tests
            if t.get("reasoning_effort") is not None
            and str(t["reasoning_effort"]).strip().lower() not in effort.NIVELES]


def e3_resolver(foto: dict) -> list[str]:
    out = []
    for mid, rz in sorted(foto.get("modelos", {}).items()):
        rz = rz or {}
        niveles = rz.get("supported_efforts") or []

        ef, etiqueta = effort.resolver(mid, None, foto=foto)
        if ef is not None:
            out.append(f"E3 {mid}: sin pedido manda {ef!r} — el examen es el default, "
                       "no se manda nada")
        default = rz.get("default_effort")
        if (niveles and rz.get("default_enabled") is not False and default
                and etiqueta != f"default:{default}"):
            out.append(f"E3 {mid}: la etiqueta {etiqueta!r} no registra el default "
                       f"declarado {default!r}")

        for pedido in effort.NIVELES:
            ef, _ = effort.resolver(mid, pedido, foto=foto)
            if ef is None:
                continue
            if ef not in niveles:
                out.append(f"E3 {mid}: pedido={pedido!r} manda {ef!r}, fuera de {niveles}")
            elif rz.get("default_enabled") is False:
                out.append(f"E3 {mid}: le enciende el razonamiento (default_enabled=false)")
    return out


def main() -> int:
    foto = effort.cargar_foto()
    if not foto.get("modelos"):
        print("❌ E0 no hay foto de effort (benchmarks/reasoning_openrouter.json) — "
              "correr `python benchmarks/effort.py --actualizar`")
        return 1

    from benchmarks.models import MODELS
    tests = _tests_declarados()
    fallos = e1_cobertura(foto, MODELS) + e2_niveles(tests) + e3_resolver(foto)

    tomada = foto.get("tomada")
    if tomada and (date.today() - date.fromisoformat(tomada)).days > DIAS_AVISO:
        print(f"  ⚠ E4 la foto es del {tomada}: confirmar con `effort.py --vivo` antes de un lote")

    for f in fallos:
        print(f"  ❌ {f}")
    if fallos:
        print(f"❌ {len(fallos)} problema(s) con el effort de razonamiento")
        return 1

    con = sum(1 for v in foto["modelos"].values() if v and v.get("supported_efforts"))
    print(f"✅ effort: foto del {tomada} · {len(foto['modelos'])} modelos ({con} con niveles "
          f"declarados) · {len(tests)} tests leídos · E1-E3 en verde")
    return 0


if __name__ == "__main__":
    sys.exit(main())
