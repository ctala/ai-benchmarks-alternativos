#!/usr/bin/env python3
"""Caza AFIRMACIONES caducas: docs vivos que contradicen una decisión vigente.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
Cristian, revisando el repo: *"creo que el README es un caos"*. Lo era, y de una forma
específica: **un título de sección negaba la decisión vigente del repo.**

    README.md L16   «## Score = combinación ponderada (NO solo calidad)»
    README.md L41   «⚠️ Disclaimer crítico: nuestro score_global NO es solo quality»
    DECISIONES.md   13-ago · VIGENTE · «El titular es el índice de calidad»

Y ningún guardrail lo cazaba. `check_consistency` compara **cifras** citadas contra
`models.json`; esto son **claims** —afirmaciones de método sin un número— y pasaban
limpio. Es la contracara del hueco que el repo ya tiene documentado: los detectores cazan
lo que FALTA (un dato ausente, un score viejo) y esto es lo que SOBRA: prosa correcta en
su momento que quedó afirmando lo contrario de lo que hoy hacemos.

Pasó dos veces —la explicación del compuesto sobrevivió a v4.1 y a v4.2— así que
documentarlo por tercera vez no lo iba a arreglar.

CÓMO FUNCIONA
-------------
Cada regla es un par: un patrón que NO debe aparecer en docs vivos, y la decisión que lo
prohíbe. Al agregar una decisión que reemplaza a otra, se agrega su patrón acá — en el
mismo commit, como manda la regla de las superficies.

Uso:  python benchmarks/check_claims.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Docs que describen el estado ACTUAL. Los snapshots con fecha (CHANGELOG, DATASHEET_*)
# quedan fuera a propósito: ahí la afirmación vieja es correcta, es historia.
DOCS_VIVOS = ["README.md", "METODOLOGIA.md", "CLAUDE.md", "AGENTS.md",
              "MODELOS.md", "RECOMENDACIONES.md", "COMPARATIVA.md"]

# patrón prohibido · por qué · decisión que lo reemplaza
CLAIMS = [
    (r"score\s*=\s*combinaci[oó]n ponderada",
     "el titular dejó de ser un compuesto en v4.1",
     "13-ago-2026 · el titular es el índice de calidad; precio y latencia van al lado"),
    (r"score_global\s+NO es solo quality",
     "presenta el compuesto como el número principal",
     "13-ago-2026 · el titular es el índice de calidad"),
    (r"Top 10 Global Ranking\s*—\s*score compuesto",
     "el ranking publicado es el índice de calidad, no el compuesto",
     "13-ago-2026 · el titular es el índice de calidad"),
    (r"el score se recalcula con cada modelo nuevo",
     "eso era cierto con z-score vivo; desde v4.0 la referencia está congelada y desde "
     "v4.1 la escala es absoluta",
     "17-jul-2026 · referencia congelada por versión · 13-ago-2026 · escala absoluta"),
    (r"\b23 suites\b",
     "el número de suites cambió y quedó escrito a mano",
     "los conteos se sincronizan con sync_doc_counts.py, no se escriben"),
]


# Marcas de que la línea CITA una afirmación vieja en vez de sostenerla.
CITA = re.compile(r"«|»|dec[íi]a|hasta v\d|Antes\b|~~|ya no\b|dejó de", re.I)


def main() -> int:
    hallazgos = []
    for doc in DOCS_VIVOS:
        p = ROOT / doc
        if not p.exists():
            continue
        for n, linea in enumerate(p.read_text(errors="replace").splitlines(), 1):
            # CITAR un error no es cometerlo. `METODOLOGIA.md` explica por qué el
            # compuesto se abandonó, y para eso tiene que nombrarlo. Sin esta excepción,
            # el guardrail castigaría justo al documento que hace bien las cosas — y la
            # salida sería borrar la explicación, que es peor que el problema original.
            if CITA.search(linea):
                continue
            for pat, por_que, decision in CLAIMS:
                if re.search(pat, linea, re.I):
                    hallazgos.append((doc, n, linea.strip()[:90], por_que, decision))

    print(f"\nVerificando afirmaciones de método en {len(DOCS_VIVOS)} docs vivos…\n")
    if not hallazgos:
        print(f"  ✅ ningún doc vivo contradice una decisión vigente "
              f"({len(CLAIMS)} claims vigilados).")
        return 0

    print(f"  ❌ {len(hallazgos)} afirmación(es) que contradicen una decisión vigente:\n")
    for doc, n, txt, por_que, dec in hallazgos:
        print(f"  · {doc}:{n}")
        print(f"      dice:     {txt}")
        print(f"      problema: {por_que}")
        print(f"      vigente:  {dec}\n")
    print("  Una cifra caduca la caza check_consistency. Esto es una AFIRMACIÓN caduca:")
    print("  prosa que fue correcta y hoy dice lo contrario de lo que hacemos.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
