#!/usr/bin/env python3
"""
Ciclo de vida de la documentación: que un doc podrido no pase por vigente.

POR QUÉ EXISTE (13-ago-2026)
----------------------------
Cristian: *"¿harás algo con los hallazgos? ¿los mantendrás actualizados? ¿o hay
documentos que no deberían existir?"*

La respuesta honesta a la segunda pregunta es **no, no a mano** — es exactamente lo que
falló durante 102 días. Auditado ese día, de 34 documentos en la raíz:

  · 5 llevaban **más de 90 días** sin tocarse, describiendo cosas que ya cambiaron
    (`NIAH_ES_DESIGN.md` dice "v1 piloto" y la suite va por v3 con grilla recortada)
  · 9 recomendaban modelos **retirados**, Devstral Small incluido
  · `PROVEEDORES.md` llevaba 113 días y citaba 4 modelos muertos

Ninguno rompía nada. Un doc podrido no falla: se lee, convence, y manda a alguien a
integrar un modelo que devuelve 404.

EL MECANISMO
------------
Cada doc **curado** declara su estado en el frontmatter:

    <!-- doc: vigente | verificado: 2026-08-13 -->
    <!-- doc: snapshot -->            ← fechado a propósito, NO se actualiza jamás
    <!-- doc: generado -->            ← lo escribe el pipeline, no se edita a mano

Este chequeo marca los **vigentes** cuya verificación tiene más de `--dias` (90 por
defecto). No verifica el contenido —eso no se automatiza— sino que **alguien lo haya
mirado**. Es la diferencia entre "está desactualizado" y "nadie sabe si lo está".

Uso:
    python benchmarks/check_docs.py            # reporta
    python benchmarks/check_docs.py --marcar   # pone la marca a los que no la tienen
"""

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Los escribe el pipeline. Editarlos a mano es el error, no no-actualizarlos.
GENERADOS = {
    "MODELOS.md", "TESTS.md", "RECOMENDACIONES.md", "PROMPTS.md", "README.md",
}
# Fechados a propósito: conservan el valor del momento. Reescribirlos sería el bug.
SNAPSHOTS_PREFIJO = ("DATASHEET_", "POST-MORTEM")
SNAPSHOTS = {"CHANGELOG.md"}

MARCA = re.compile(r"<!--\s*doc:\s*(\w+)(?:\s*\|\s*verificado:\s*([\d-]+))?\s*-->")


def _clase_por_defecto(nombre: str) -> str:
    if nombre in GENERADOS:
        return "generado"
    if nombre in SNAPSHOTS or nombre.startswith(SNAPSHOTS_PREFIJO):
        return "snapshot"
    return "vigente"


def _ultimo_commit(nombre: str) -> str | None:
    out = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short", "--", nombre],
                         cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=90,
                    help="antigüedad máxima de la verificación antes de avisar")
    ap.add_argument("--marcar", action="store_true",
                    help="agregar la marca a los docs que no la tienen, usando su último commit")
    ap.add_argument("--hoy", default=None, help="fecha de referencia (YYYY-MM-DD), para tests")
    args = ap.parse_args()

    hoy = (datetime.date.fromisoformat(args.hoy) if args.hoy
           else datetime.date.today())

    sin_marca, vencidos, ok = [], [], 0
    for p in sorted(ROOT.glob("*.md")):
        cabeza = p.read_text(encoding="utf-8", errors="ignore")[:400]
        m = MARCA.search(cabeza)
        clase_def = _clase_por_defecto(p.name)

        # Un doc GENERADO no necesita marca: el pipeline lo reescribe entero y se la
        # lleva puesta en cada corrida. Su clase se sabe por el nombre, que es más
        # confiable que una marca que se borra sola. (Lo destapó test_guardrails el
        # 13-ago: tras regenerate_all, los 5 generados quedaban «sin declarar».)
        if not m and clase_def == "generado":
            ok += 1
            continue

        if not m:
            if args.marcar:
                fecha = _ultimo_commit(p.name) or hoy.isoformat()
                marca = (f"<!-- doc: {clase_def} -->\n" if clase_def != "vigente"
                         else f"<!-- doc: vigente | verificado: {fecha} -->\n")
                p.write_text(marca + p.read_text(encoding="utf-8"), encoding="utf-8")
            else:
                sin_marca.append((p.name, clase_def))
            continue

        clase, verificado = m.group(1), m.group(2)
        if clase != "vigente":
            ok += 1
            continue
        if not verificado:
            sin_marca.append((p.name, "vigente sin fecha"))
            continue
        dias = (hoy - datetime.date.fromisoformat(verificado)).days
        if dias > args.dias:
            vencidos.append((p.name, dias))
        else:
            ok += 1

    if args.marcar:
        print(f"  ✓ marcas agregadas. Corré sin --marcar para ver el estado.")
        return 0

    if sin_marca:
        print(f"  {len(sin_marca)} doc(s) sin declarar su estado:")
        for n, c in sin_marca:
            print(f"     {n:<36} (sería «{c}»)")
        print("     → `python benchmarks/check_docs.py --marcar` las agrega\n")

    if vencidos:
        print(f"  ⚠️  {len(vencidos)} doc(s) vigentes sin verificar hace más de {args.dias} días:")
        for n, d in sorted(vencidos, key=lambda x: -x[1]):
            print(f"     {n:<36} {d} días")
        print("     Un doc vigente que nadie mira no es documentación, es una afirmación")
        print("     sin dueño. Revisalo y actualizá la fecha, o marcalo como snapshot.\n")

    print(f"  ✅ {ok} doc(s) en regla.")
    return 1 if (vencidos or sin_marca) else 0


if __name__ == "__main__":
    sys.exit(main())
