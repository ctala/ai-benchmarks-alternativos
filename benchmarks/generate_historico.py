#!/usr/bin/env python3
"""
Escribe en el home (docs/index.html) la tabla «histórico», desde models.json.

POR QUÉ EXISTE (7-nov-2026)
---------------------------
La tabla la armaba `app.js` en el navegador, con un título fijo: «Histórico: medidos antes
del examen v5». Desde que un reemplazado pasa al histórico cuando su sucesor está medido
(DECISIONES, 7-nov-2026), 7 de sus filas rindieron el examen v5 ENTERO y salieron del
ranking porque las reemplazó su versión nueva, no por haberse medido antes. La tabla decía
algo falso de ellas y no decía quién las reemplazó. Nada lo cazaba: lo que arma el JS no lo
lee ningún chequeo.

Generada acá, la tabla es HTML estático —la lee un buscador sin ejecutar JS— y
`check_calculator.py` C6 la compara fila por fila con `historico`, `reemplazado_por` y
`era` del export.

Uso:
    python benchmarks/generate_historico.py
"""
import html as _h
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "docs" / "index.html"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

START = "<!-- AUTO-HISTORICO-START -->"
END = "<!-- AUTO-HISTORICO-END -->"

MOTIVO_REEMPLAZO = "reemplazo"
MOTIVO_ANTES = "antes_v5"
MOTIVO_PARCIAL = "parcial_v5"   # la mayoría en la ventana v5, pero no el examen entero


def _num(x) -> str:
    return f"{x:.2f}".replace(".", ",") if x is not None else "—"


def filas(data: dict) -> list[dict]:
    """Las filas de la tabla, en orden alfabético. Función pura: no decide quién entra,
    solo lee `historico`, `reemplazado_por` y `era` del export."""
    por_key = {m["key"]: m for m in data.get("models", [])}
    out = []
    for m in data.get("models", []):
        if not m.get("historico"):
            continue
        suc = m.get("reemplazado_por")
        era = m.get("era") or {}
        out.append({
            "key": m["key"],
            "name": m.get("name") or m["key"],
            "motivo": (MOTIVO_REEMPLAZO if suc
                       else MOTIVO_PARCIAL if era.get("era") == "v5" else MOTIVO_ANTES),
            "reemplazado_por": suc or "",
            "sucesor": (por_key.get(suc) or {}).get("name") or suc or "",
            "era": era.get("era") or "?",
            "etiqueta": era.get("etiqueta") or "",
            "reparto": era.get("reparto") or {},
            "calidad": m.get("quality_avg"),
        })
    return sorted(out, key=lambda f: f["name"].casefold())


def build(data: dict) -> str:
    fs = filas(data)
    n_rem = sum(f["motivo"] == MOTIVO_REEMPLAZO for f in fs)
    # «antes» y «parcial» comparten la frase: los dos rindieron el examen fuera de las
    # condiciones de v5, entero o en parte.
    n_antes = len(fs) - n_rem
    e = _h.escape

    def motivo(f):
        if f["motivo"] == MOTIVO_REEMPLAZO:
            return (f'Lo reemplazó <a href="/modelo/{e(f["reemplazado_por"])}/">{e(f["sucesor"])}</a>, '
                    f'su versión nueva. Rindió el examen v5 entero')
        if f["motivo"] == MOTIVO_PARCIAL:
            fuera = sum(n for k, n in f["reparto"].items() if k != "v5")
            return (f"Rindió el examen completo, pero {fuera} de sus pruebas son de antes "
                    "de la ventana v5")
        return "Medido antes del examen v5"

    def reparto(f):
        return " · ".join(f"{e(k)} {n}" for k, n in f["reparto"].items())

    rows = "\n".join(
        f'      <tr data-modelo="{e(f["key"])}" data-motivo="{f["motivo"]}" '
        f'data-reemplazado-por="{e(f["reemplazado_por"])}" data-era="{e(f["era"])}">'
        f'<td><a href="/modelo/{e(f["key"])}/">{e(f["name"])}</a></td>'
        f'<td>{motivo(f)}</td>'
        f'<td><span class="ctx-badge ctx-nd" title="{e(f["etiqueta"])}">{e(f["era"])}</span> {e(f["etiqueta"])}</td>'
        f'<td>{_num(f["calidad"])}</td>'
        f'<td class="meta">{reparto(f)}</td></tr>'
        for f in fs)

    partes = []
    if n_antes:
        partes.append(f"{n_antes} rindieron el examen completo, pero no en las condiciones de v5 "
                      "(proveedor fijo, razonamiento según la tarea y el harness actual): sus notas "
                      "se midieron con otra versión y llevan la era de la mayoría de sus pruebas")
    if n_rem:
        partes.append(f"{n_rem} rindieron el examen v5 entero y salieron del ranking porque los "
                      "reemplazó su versión nueva, medida con el mismo examen")
    intro = ". ".join(p[0].upper() + p[1:] for p in partes) + "."

    return f"""{START}
    <div class="results-header">
      <h2 id="historico-h">Histórico: fuera del ranking v5</h2>
      <p class="meta">
        {intro} Ninguno compite por un puesto, así que van en orden alfabético.
      </p>
    </div>
    <div id="historico-wrap" class="table-scroll">
    <table class="results-table historico-table">
      <thead><tr><th scope="col">Modelo</th><th scope="col">Por qué está acá</th><th scope="col">Era</th>
        <th scope="col">Calidad (su era)</th><th scope="col">Pruebas por era</th></tr></thead>
      <tbody>
{rows}
      </tbody>
    </table>
    </div>
    {END}"""


def main():
    data = json.loads(MODELS_JSON.read_text())
    html = INDEX.read_text()
    if START not in html or END not in html:
        raise SystemExit(f"ERROR: faltan los marcadores {START} / {END} en docs/index.html, "
                         "dentro de <section id=\"historico\">.")
    html = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", lambda _: build(data), html,
                  flags=re.DOTALL)
    INDEX.write_text(html)
    fs = filas(data)
    print(f"OK: docs/index.html — tabla histórico con {len(fs)} filas "
          f"({sum(f['motivo'] == MOTIVO_REEMPLAZO for f in fs)} reemplazadas)")


if __name__ == "__main__":
    main()
