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
S6. Lo que el registro DECLARA sobre el promedio es lo que el export HACE. También
    AVISO: hoy nace en rojo, y un bloqueante que arranca fallando se aprende a ignorar.

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


def s5_nadie_reimplementa_el_indice(verbose=False) -> list[str]:
    """Nadie decide «qué suites cuentan» con una heurística de nombres.

    20-ago-2026. El criterio vivía en `SUITES[s]["en_promedio"]` desde siempre, pero no
    había una FUNCIÓN a la que llamar — así que cinco archivos se escribieron la suya:

        APARTE = ("niah", "prompt_injection")

    Esa tupla cubre 2 de las 6 suites fuera del índice. Las otras cuatro
    (`integridad_idioma`, `dominio_entidad`, `extraer_claims`, `verificar_claims_lote`)
    quedaban del lado equivocado. Costó medir tres modelos para nada y publicar un
    `examen_completo: true` junto a un `ranked: false` en el mismo JSON.

    Hoy la respuesta es `suites.del_indice()`. Este chequeo existe para que no vuelva a
    haber una segunda: es barato escribir la tupla de nuevo y carísimo descubrirlo.
    """
    patron = re.compile(r'\(\s*["\']niah["\']\s*,\s*["\']prompt_injection["\']')
    malos = []
    for f in sorted(ROOT.glob("benchmarks/*.py")):
        if f.name in ("check_suites.py", "suites.py"):
            continue
        txt = f.read_text(errors="ignore")
        # los comentarios explican por qué NO se usa; no cuentan como uso
        codigo = re.sub(r"#.*", "", re.sub(r'"""[\s\S]*?"""', "", txt))
        if patron.search(codigo):
            malos.append(f.name)
    if malos:
        return [f"S5 · {len(malos)} archivo(s) deciden qué suites cuentan por prefijo de "
                f"nombre en vez de llamar a `suites.del_indice()`: {', '.join(malos)}"]
    if verbose:
        print("  ✅ S5 · nadie reimplementa el índice de suites")
    return []


def s6_lo_declarado_es_lo_que_promedia(verbose=False) -> list[str]:
    """El registro dice qué suites promedian. ¿Es eso lo que el export hace?

    17-sep-2026. Salió de simular la jubilación de las suites saturadas
    (`simular_jubilacion.py`): al reconstruir el índice REAL se vio que `del_indice()`
    declara 29 suites y el conjunto que de verdad promedia el titular también son 29 —
    pero NO son las mismas:

      · `tool_calling` declara `en_promedio: True` y `export_for_pages.general` lo excluye
        POR CÓDIGO (el juez sólo lee texto y lo puntúa al revés: al que hace la llamada
        limpia le pone 1/5).
      · `integridad_idioma` declara `en_promedio: False` y NADA lo excluye, así que
        promedia en el titular en cuanto su cobertura pasa el umbral. Hoy la pasa.

    Los dos errores se compensan AL CONTAR (29 = 29), que es exactamente por qué nadie lo
    vio: contar da lo mismo y las listas difieren. Y no es cosmético — sacar
    `integridad_idioma` del promedio cambia el #1 del ranking.

    No importa `export_for_pages` (arrastra el SDK de OpenAI, que tuvo el CI 40 días en
    rojo): lee su FUENTE y saca de ahí qué excluye, para que agregar una exclusión nueva
    quede cubierto solo.
    """
    fuente = (ROOT / "benchmarks" / "export_for_pages.py").read_text(errors="ignore")
    bloque = fuente[fuente.find("def _is_niah"):fuente.find("def _is_agentic")]
    if not bloque:
        return ["S6 · no se pudo leer qué excluye `general` en export_for_pages.py"]
    prefijos = set(re.findall(r'startswith\(\s*["\'](\w+)["\']', bloque))
    exactos = set(re.findall(r'==\s*["\'](\w+)["\']', bloque))
    m = re.search(r"MIN_SUITE_COVERAGE\s*=\s*([\d.]+)", fuente)
    umbral = f"{float(m.group(1)):.0%}" if m else "el umbral"

    def excluida_por_codigo(s: str) -> bool:
        return any(s.startswith(p) for p in prefijos) or s in exactos

    avisos = []
    contradicen = [k for k, s in SUITES.items()
                   if s["en_promedio"] and excluida_por_codigo(k)]
    for k in sorted(contradicen):
        avisos.append(f"S6 · `{k}` declara `en_promedio: True` y el export lo EXCLUYE por "
                      f"código: nunca promedia, diga lo que diga el registro")
    colados = sorted(k for k, s in SUITES.items()
                     if not s["en_promedio"] and not excluida_por_codigo(k))
    if colados:
        avisos.append(f"S6 · {len(colados)} suite(s) declaran `en_promedio: False` y nada "
                      f"las excluye: entran al titular en cuanto su cobertura pase "
                      f"{umbral}, sin que nadie lo decida → {', '.join(colados)}")
    if verbose and not avisos:
        print("  ✅ S6 · lo que el registro declara es lo que el export promedia")
    return avisos


def main() -> int:
    fallos, avisos = [], []
    fallos += s5_nadie_reimplementa_el_indice(True)
    avisos += s6_lo_declarado_es_lo_que_promedia(True)
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
