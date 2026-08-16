#!/usr/bin/env python3
"""Verifica que el registro de suites siga siendo UNO.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
El nombre humano de cada eje vivía a mano en tres archivos y ya había divergido:

    policy_adherence   calculadora: "Policy adherence (límites, idioma)"
                       corte:       "hacer exactamente lo que se pidió"

Siete suites dichas de dos formas, y dos (`integridad_idioma`, `niah_es`) sin nombre
humano en ninguna parte — o sea, mostrando el id técnico en la cara del usuario.

Y al medirlo apareció lo que la cosmética tapaba: **siete de 28 suites estaban en pilares
distintos según de dónde se mirara, y tres no figuraban en el mapeo del export**, que es
el que produce los números publicados. `agent_long_horizon` y `tool_calling_adversarial`
—las dos suites más agénticas del benchmark— NO entraban al promedio del pilar Agentes, y
nada lo decía. Eso explica algo que ya estaba anotado sin causa en `check_cortes.py`: que
el pilar Agentes tampoco mostraba a Gemini 3.6 Flash. No era solo que promedia.

QUÉ VERIFICA
------------
S1. Toda suite MEDIDA está en el registro. Una suite nueva sin entrada muestra su id
    técnico al usuario y no aparece en ningún menú.
S2. Nadie mantiene una copia a mano. `docs/app.js` no puede volver a traer su propia
    lista de etiquetas: tiene que leer `models.json`.
S3. El registro que viaja en `models.json` coincide con `suites.py`. Si el export quedó
    viejo, el sitio publica etiquetas de otra generación.
S4. Toda suite con pilar y `en_promedio: False` tiene el motivo escrito. Es la condición
    que estuvo tres veces sin declarar: medida, con pilar natural, y fuera del promedio.
    Se reporta como AVISO, no como fallo — la decisión de meterlas mueve números
    publicados y se toma con simulación (`PLAN-ESTABILIDAD.md`), no de pasada.

Uso:  python benchmarks/check_suites.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks.suites import SUITES  # noqa: E402

MODELS_JSON = ROOT / "docs" / "data" / "models.json"
APP_JS = ROOT / "docs" / "app.js"


def main() -> int:
    fallos, avisos = [], []
    d = json.loads(MODELS_JSON.read_text())

    # ── S1 · toda suite medida está en el registro ─────────────────────────
    medidas = set()
    for m in d["models"]:
        medidas |= set((m.get("score_by_suite") or {}).keys())
    huerfanas = sorted(medidas - set(SUITES))
    for s in huerfanas:
        n = sum(1 for m in d["models"] if s in (m.get("score_by_suite") or {}))
        fallos.append(f"`{s}` está medida en {n} modelos y NO está en el registro "
                      f"(benchmarks/suites.py) — el sitio le mostraría el id técnico al "
                      f"usuario, y no aparecería en ningún menú ni corte")

    # ── S2 · el sitio no puede tener su propia copia ───────────────────────
    js = APP_JS.read_text()
    # Una lista literal de {value: "...", label: "..."} es exactamente la forma que tenía
    # la copia vieja. Si vuelve a aparecer, volvió el problema.
    copias = re.findall(r'\{\s*value:\s*"(\w+)",\s*label:\s*"[^"]+"\s*\}', js)
    copias = [c for c in copias if c in SUITES]
    if copias:
        fallos.append(f"docs/app.js volvió a traer etiquetas de suite escritas a mano "
                      f"({', '.join(sorted(set(copias))[:5])}…). Tiene que leerlas de "
                      f"`models.json` con cargarRegistroDeSuites(): una copia diverge, "
                      f"y ya divergió una vez en 7 suites")

    # ── S3 · lo que viaja coincide con la fuente ───────────────────────────
    viaja = d.get("suites")
    if not viaja:
        fallos.append("`models.json` no trae el registro (`suites`) — el sitio se queda "
                      "sin menú de subcategorías. Corré export_for_pages.py")
    else:
        for k, s in SUITES.items():
            v = viaja.get(k)
            if not v:
                fallos.append(f"`{k}` está en suites.py y no viajó a models.json — "
                              f"el export quedó viejo")
            elif (v.get("menu"), v.get("pilar"), v.get("en_promedio")) != \
                 (s["menu"], s["pilar"], s["en_promedio"]):
                fallos.append(f"`{k}`: models.json publica una versión distinta de la del "
                              f"registro — el export quedó viejo")

    # ── S4 · fuera del promedio, con el motivo escrito ─────────────────────
    for k, s in SUITES.items():
        if s["pilar"] and not s["en_promedio"]:
            n = sum(1 for m in d["models"] if k in (m.get("score_by_suite") or {}))
            if not s.get("nota"):
                fallos.append(f"`{k}` tiene pilar {s['pilar']} y NO suma al promedio, sin "
                              f"motivo escrito. Esa condición ya vivió tres veces sin "
                              f"declarar: agregá `nota` o poné `en_promedio: True`")
            else:
                avisos.append(f"`{k}` medida en {n} modelos, pilar {s['pilar']}, "
                              f"FUERA del promedio")
        if not s.get("menu") or not s.get("decide"):
            fallos.append(f"`{k}` sin etiqueta de menú o sin la línea humana («qué "
                          f"decides mirando esto») — el usuario vería el id técnico")

    print(f"\nVerificando el registro de suites ({len(SUITES)} suites, "
          f"{len(medidas)} medidas)…\n")
    for a in avisos:
        print(f"  ⚠️  {a}")
    if avisos:
        print(f"\n     Meterlas al promedio mueve números publicados: es un cambio de "
              f"presentación\n     y se simula antes (PLAN-ESTABILIDAD.md). El aviso "
              f"existe para que la decisión\n     esté a la vista en vez de ser una "
              f"ausencia.\n")
    for f in fallos:
        print(f"  ❌ {f}")
    if fallos:
        print(f"\n  ❌ {len(fallos)} problema(s) en el registro.")
        return 1
    print(f"  ✅ el registro es uno solo: {len(SUITES)} suites con nombre humano, "
          f"sin copias a mano.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
