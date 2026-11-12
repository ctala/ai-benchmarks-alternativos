#!/usr/bin/env python3
"""No hay veredicto sin alcance, y un empate no se vende como «lo mismo». (12-nov-2026, motor-sitio 2.6)

POR QUÉ EXISTE
--------------
/claude-haiku-sonnet-opus/ decía «Los 5 tiers empatan en calidad» y «pagar más no compra calidad
que se pueda medir». Cristian (12-nov): en Claude Code la diferencia entre tiers se nota mucho y
eso no lo medimos; Planificar da 9,20 en los cinco, y eso es saturación, no empate. La página
generalizaba más allá de lo medido y nada lo impedía. Detalle en `alcance.py`.

Sobre lo compilado (`sitio/dist`):
  A1  todo bloque de veredicto («La respuesta corta», «Veredicto rápido») trae su alcance: un
      elemento `data-alcance` que empieza con «En nuestra(s)…» y enlaza a `#que-mide`;
  A2  toda página con veredicto lleva «Qué mide esta página y qué no» (`#que-mide`): al menos
      una suite o tarea con su enlace, y un enlace a cada benchmark externo de cada eje;
  A3  ninguna página publica una frase retirada por generalizar un empate («empatan en
      calidad», «no compra nada»…);
  A4  toda página con «claude» o «fable» en la URL y veredicto dice que no responde si conviene para
      programar con un agente, con el enlace al benchmark externo de ese eje;
y sobre `benchmarks/benchmarks_externos.json`:
  E1  están los ejes mínimos, cada uno con al menos un benchmark;
  E2  cada benchmark tiene id, nombre, eje, qué mide, URL https y fecha de revisión;
  E3  ninguna revisión tiene más de 120 días.

Que la URL exista y que lo citado siga vigente se verifica a mano al revisar (la fecha queda en
`revisado`); un chequeo de red en el QA fallaría por la red y no por el dato.

Mide `sitio/dist`; si está más viejo que sus fuentes, primero compila (el postbuild corre este
mismo chequeo).

Uso:
    python benchmarks/check_alcance.py
    python benchmarks/check_alcance.py --dist <dir> --sin-compilar
"""
from __future__ import annotations

import argparse
import html as H
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "benchmarks"))
import alcance  # noqa: E402

RETIRADAS = (
    "empatan en calidad",
    "no compra nada",
    "no compra calidad",
    "empatan con los mejores",
    "los de arriba empatan",
    "empate técnico en calidad",
)
TITULOS_VEREDICTO = ("La respuesta corta", "Veredicto rápido")
NO_RESPONDE = "esta página no responde esa pregunta"

SECCION = re.compile(r"<section\b[^>]*>.*?</section>", re.S)


def visible(txt: str) -> str:
    txt = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", txt, flags=re.S)
    txt = H.unescape(re.sub(r"<[^>]+>", " ", txt))
    return re.sub(r"\s+", " ", txt).strip()


def veredictos(pagina: str) -> list[str]:
    """Las secciones que dan un veredicto: las que nombran «La respuesta corta» o «Veredicto
    rápido», como título o en la prosa (la review de Fable 5 lo dice en el primer párrafo)."""
    return [s for s in SECCION.findall(pagina) if any(t in visible(s) for t in TITULOS_VEREDICTO)]


def revisar_pagina(rel: str, pagina: str, ext: dict) -> list[str]:
    fallos = []
    txt = visible(pagina).lower()
    for f in RETIRADAS:
        if f in txt:
            fallos.append(f"A3 · {rel}: publica «{f}», que generaliza un empate más allá de lo medido")
    vs = veredictos(pagina)
    if not vs:
        return fallos
    for s in vs:
        m = re.search(r"<[^>]*\bdata-alcance\b[^>]*>(.*?)</(?:span|p)>", s, re.S)
        if not m:
            fallos.append(f"A1 · {rel}: un bloque de veredicto sin alcance (`data-alcance`)")
            continue
        if not visible(m.group(1)).startswith("En nuestra"):
            fallos.append(f"A1 · {rel}: el alcance no dice «En nuestra(s)…»: «{visible(m.group(1))[:60]}»")
        if 'href="#que-mide"' not in m.group(0) + s[m.end():m.end() + 400]:
            fallos.append(f"A1 · {rel}: el alcance no enlaza a la lista (#que-mide)")
    q = re.search(r'<section\b[^>]*id="que-mide".*?</section>', pagina, re.S)
    if not q:
        fallos.append(f"A2 · {rel}: tiene veredicto y no lleva «Qué mide esta página y qué no» (#que-mide)")
    else:
        bloque = q.group(0)
        if not re.search(r'href="' + re.escape(alcance.REPO) + r'/(?:blob/main/benchmarks/tests|tree/main/tareas-agente)/', bloque):
            fallos.append(f"A2 · {rel}: #que-mide no enlaza ninguna suite ni tarea")
        for b in ext["benchmarks"]:
            if f'href="{b["url"]}"' not in bloque:
                fallos.append(f"A2 · {rel}: #que-mide no enlaza a {b['nombre']} ({b['eje']})")
    if "claude" in rel or "fable" in rel:
        urls = [b["url"] for b in ext["benchmarks"] if b["eje"] == "codigo_agente"]
        if NO_RESPONDE not in txt or not any(f'href="{u}"' in pagina for u in urls):
            fallos.append(f"A4 · {rel}: falta «{NO_RESPONDE}» con el enlace a un benchmark de programar con agente")
    return fallos


def revisar(dist: Path) -> tuple[list[str], int, int]:
    ext = alcance.externos()
    fallos, n, con = [], 0, 0
    for f in sorted(dist.rglob("*.html")):
        rel = "/" + str(f.relative_to(dist)).removesuffix("index.html")
        pagina = f.read_text(encoding="utf-8", errors="ignore")
        n += 1
        con += bool(veredictos(pagina))
        fallos += revisar_pagina(rel, pagina, ext)
    return fallos, n, con


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=ROOT / "sitio" / "dist")
    ap.add_argument("--sin-compilar", action="store_true", help="revisar el dist tal cual está")
    a = ap.parse_args()
    if not a.sin_compilar and a.dist == ROOT / "sitio" / "dist":
        import subprocess
        import check_movil
        motivo = check_movil.viejo(a.dist)
        if motivo:
            # Un verde sobre el dist de ayer miraría las plantillas de ayer. El postbuild corre
            # este mismo chequeo sobre el dist nuevo.
            print(f"  · {motivo}: compilo con `npm run build` (su postbuild revisa el alcance)", flush=True)
            r = subprocess.run(["npm", "run", "build"], cwd=ROOT / "sitio", capture_output=True, text=True)
            if r.returncode != 0:
                print("  ❌ el build falló:")
                print("\n".join("     " + x for x in (r.stdout + r.stderr).strip().splitlines()[-15:]))
                return 1
            tramo = (r.stdout or "").split("ALCANCE DE LOS VEREDICTOS", 1)
            print("ALCANCE DE LOS VEREDICTOS" + tramo[1].split("\n\n")[0].rstrip() if len(tramo) == 2
                  else "  ✅ el build revisó el alcance y pasó")
            return 0
    print("ALCANCE DE LOS VEREDICTOS")
    if not (a.dist / "index.html").is_file():
        print(f"  ❌ no hay build en {a.dist}: correr `npm run build` en sitio/")
        return 1
    fallos = alcance.errores_externos()
    f2, n, con = revisar(a.dist)
    fallos += f2
    if con == 0:
        fallos.append("A1 · ninguna página tiene un bloque de veredicto: el chequeo no estaría mirando nada")
    for x in fallos[:40]:
        print(f"  ❌ {x}")
    if len(fallos) > 40:
        print(f"  … y {len(fallos) - 40} más")
    if fallos:
        print(f"\n  ❌ {len(fallos)} problema(s). Detalle y motivo: benchmarks/alcance.py")
        return 1
    print(f"  ✅ {con} página(s) con veredicto, todas con su alcance y su «Qué mide esta página y qué no»; "
          f"ninguna de las {n} publica una frase retirada; benchmarks externos al día")
    return 0


if __name__ == "__main__":
    sys.exit(main())
