#!/usr/bin/env python3
"""
El portero del benchmark. Si algo no cuadra, no se publica.

POR QUÉ EXISTE
--------------
Durante meses el benchmark publicó números que no se sostenían, y ninguno era un error de
tipeo: eran promedios calculados sobre datos que no permitían ese promedio. El patrón se
repitió tantas veces que dejó de ser casualidad:

  · Se promediaban runs puntuados con FÓRMULAS DISTINTAS (43% del dataset usaba una
    obsoleta). 24 suites mezclaban dos o tres escalas en un mismo número.
  · Por eso un modelo medido en julio salía +2.5 puntos arriba de uno medido en abril:
    el ranking medía CUÁNDO te evaluamos, no qué tan bueno sos.
  · Se comparaban modelos que habían rendido EXÁMENES DISTINTOS (MiniMax M3 hizo 4 de 10
    tests de business_audit; Opus hizo los 10) y se publicaba el resultado como si fuera
    una comparación.
  · Se promediaba por RUN y no por TEST, así que repetir un test fácil te subía la nota.
  · Se recomendaban modelos con el endpoint MUERTO — Devstral Small estuvo #5 y llegó al
    schema de FAQ que Google muestra en los resultados.
  · Los docs citaban scores que la fuente ya no decía.

Ninguno explotó. Todos produjeron números plausibles y falsos. Un crash se ve; esto no.

QUÉ HACE
--------
Corre TODAS las invariantes de una vez y sale con código 1 si alguna se rompe. Está
enganchado a `regenerate_all.py` como gate final: el pipeline no puede decir "listo"
sobre un sitio que no cuadra.

La regla de fondo, y es una sola:

    Un número solo se publica si los datos que lo sostienen son comparables entre sí.
    Si hay duda, se descarta la muestra. Perder datos es mejor que publicar un promedio
    de peras y manzanas.

Uso:
    python benchmarks/validate.py           # todas las invariantes
    python benchmarks/validate.py -v        # además, el detalle de cada una
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

RESULTS = ROOT / "benchmarks" / "results"
MODELS_JSON = ROOT / "docs" / "data" / "models.json"

FALLOS: list[str] = []
AVISOS: list[str] = []


def fallo(regla: str, detalle: str):
    FALLOS.append(f"{regla}: {detalle}")


def aviso(regla: str, detalle: str):
    AVISOS.append(f"{regla}: {detalle}")


# ─────────────────────────────────────────────────────────────────────────────
# A · LOS DATOS CRUDOS
# ─────────────────────────────────────────────────────────────────────────────

def cargar_runs():
    runs = []
    for f in sorted(RESULTS.glob("benchmark_*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            fallo("A0 · archivo ilegible", f.name)
            continue
        for r in (d if isinstance(d, list) else d.get("results", [])):
            if isinstance(r, dict) and r.get("success"):
                runs.append(r)
    return runs


def a1_procedencia(runs, verbose):
    """Los runs sin procedencia NO entran al promedio (el export los descarta).

    No es un fallo que existan en disco — son mediciones reales de antes de que la marca
    existiera. El fallo sería PROMEDIARLOS, y eso ya no pasa. Acá solo se informa cuánta
    muestra se está perdiendo, porque perder demasiada también es un problema.
    """
    sin = [r for r in runs if r.get("quality") is not None and not r.get("scoring")]
    pct = len(sin) / len(runs) if runs else 0
    if pct > 0.35:
        fallo("A1 · procedencia",
              f"{len(sin)} runs ({pct:.0%}) no se pueden clasificar y se descartan. "
              f"Es demasiada muestra perdida: re-puntualos con rescore_all.py o el "
              f"ranking se apoya en muy poco.")
    elif sin:
        aviso("A1 · procedencia",
              f"{len(sin)} runs ({pct:.0%}) sin procedencia → descartados del promedio. "
              f"Son de antes de que existiera la marca. No contaminan.")
    elif verbose:
        print("  ✅ A1 · todo run declara con qué fórmula fue puntuado")


def a2_una_formula_por_suite(runs, verbose):
    """Dentro de una suite, todos los runs CONTADOS usan la misma fórmula.

    Mezclar `verificable` (quality = ¿cazó el hecho?) con `juez-30-70` (quality = opinión
    de un LLM) en un promedio es sumar escalas distintas. El número sale, y no significa
    nada.
    """
    from benchmarks.export_for_pages import FORMULA_ESPERADA
    # La fórmula correcta es POR TEST: una suite puede tener tests verificables y tests
    # blandos, y cada uno se puntúa distinto. Exigir una sola por suite era un error mío.
    malas = defaultdict(lambda: defaultdict(int))
    for r in runs:
        s, tn, m = r.get("suite"), r.get("test_name"), r.get("scoring")
        if not (s and m):
            continue
        if m != FORMULA_ESPERADA(s, tn):
            malas[s][m] += 1

    malas = [(s, FORMULA_ESPERADA(s), o, sum(o.values())) for s, o in malas.items()]

    # Estos runs NO entran al promedio: el export los filtra. Que existan en disco no es
    # el fallo — el fallo sería promediarlos, y eso ya no pasa.
    #
    # La consecuencia REAL de descartarlos es que algunos exámenes quedan incompletos, y
    # de eso se encarga B1, que es el gate de verdad. Duplicar el bloqueo acá solo genera
    # ruido.
    if malas:
        total = sum(n for _, _, _, n in malas)
        det = ", ".join(f"{s} ({sum(o.values())})" for s, _, o, _ in sorted(malas, key=lambda x: -x[3])[:3])
        aviso("A2 · fórmula obsoleta",
              f"{total} runs con una fórmula vieja quedan FUERA del promedio ({det}…). "
              f"Si eso deja exámenes incompletos, B1 lo bloquea.")
    elif verbose:
        print("  ✅ A2 · cada test promedia una sola fórmula")


def a3_sin_doble_conteo(verbose):
    """Ningún archivo se lee dos veces (originales + re-juzgados en la misma carpeta)."""
    sospechosos = [f.name for f in RESULTS.glob("benchmark_*.json")
                   if re.search(r"(rejudged|copy|backup|\(1\))", f.name)]
    if sospechosos:
        fallo("A3 · doble conteo",
              f"{len(sospechosos)} archivos duplicados en results/ — el export los sumaría "
              f"al original: {', '.join(sospechosos[:3])}")
    elif verbose:
        print("  ✅ A3 · sin archivos duplicados en results/")


# ─────────────────────────────────────────────────────────────────────────────
# B · LA AGREGACIÓN
# ─────────────────────────────────────────────────────────────────────────────

# Suites que NO alimentan `quality` — son pilares aparte con su propia métrica.
# Un examen incompleto acá no corrompe el ranking: significa que de ese modelo no
# sabemos su contexto usable (o su resistencia a inyección). Eso se DICE, no se inventa.
PILARES_APARTE = ("niah", "prompt_injection")


def b1_examen_completo(models, verbose):
    """Un modelo solo puntúa una suite si rindió TODOS sus tests.

    Comparar el promedio de quien hizo 4 de 10 tests contra el de quien hizo los 10 no es
    comparar modelos. Publiqué "MiniMax M3 audita mejor que Opus (8.24 vs 6.94)" y en los
    4 tests que ambos rindieron, Opus GANABA 10.00 a 9.00.

    Distinción que importa: una suite que alimenta `quality` con el examen incompleto
    BLOQUEA (contamina el ranking). Un pilar aparte —contexto largo, seguridad— con el
    examen incompleto se MARCA como "no medido". No es lo mismo publicar un número falso
    que decir "de este modelo no sabemos el contexto usable".
    """
    bloquean, marcan = [], []
    for m in models:
        if not m.get("ranked"):
            continue
        for s, i in (m.get("suites_incompletas") or {}).items():
            (marcan if s.startswith(PILARES_APARTE) else bloquean).append((m["name"], s, i))

    if bloquean:
        peor = min(bloquean, key=lambda x: x[2]["rindio"] / x[2]["total"])
        fallo("B1 · examen completo",
              f"{len(bloquean)} pares (modelo, suite) con tests faltantes en suites que "
              f"ALIMENTAN LA CALIDAD. Peor: {peor[0]} rindió {peor[2]['rindio']}/"
              f"{peor[2]['total']} de {peor[1]}. Su promedio sale de otro examen.")
    if marcan:
        aviso("B1 · pilares aparte",
              f"{len(marcan)} pares con examen incompleto en contexto largo / seguridad. "
              f"NO contaminan el ranking (son pilares propios), pero su score en ese pilar "
              f"no se puede publicar: hay que mostrarlo como «no medido».")
    if not bloquean and verbose:
        print("  ✅ B1 · todo modelo rankeado rindió completos los exámenes que puntúan")


def b2_rankeable(models, verbose):
    """Rankeado ⟹ muestra sólida, endpoint vivo, plano común, no self-hosted."""
    from benchmarks.export_for_pages import MIN_RUNS_RANKED
    malos = []
    for m in models:
        if not m.get("ranked"):
            continue
        if (m.get("runs") or 0) < MIN_RUNS_RANKED:
            malos.append(f"{m['name']} ({m.get('runs')} runs < {MIN_RUNS_RANKED})")
        if m.get("retired"):
            malos.append(f"{m['name']} (endpoint MUERTO)")
        if m.get("provider_variant"):
            malos.append(f"{m['name']} (variante de proveedor: compite contra sí mismo)")
        if m.get("self_hosted"):
            malos.append(f"{m['name']} (self-hosted: su velocidad es la de otra máquina)")
    if malos:
        fallo("B2 · quién puede competir", f"{len(malos)} modelos mal rankeados: {malos[:3]}")
    elif verbose:
        print("  ✅ B2 · el ranking solo tiene modelos vivos, con muestra y en el plano común")


# ─────────────────────────────────────────────────────────────────────────────
# C · LO QUE SE PUBLICA
# ─────────────────────────────────────────────────────────────────────────────

def c1_nada_muerto_recomendado(models, verbose):
    """Ningún modelo con el endpoint muerto aparece en una página de recomendación.

    Devstral Small estuvo #5 del ranking MESES después de que Mistral apagara su endpoint,
    y llegó a aparecer en 11 páginas — incluido el schema de FAQ que Google muestra como
    respuesta destacada. Le recomendábamos a la gente, en la SERP, un modelo que da 404.
    """
    muertos = [m["name"] for m in models if m.get("retired")]
    docs = ROOT / "docs"
    culpables = defaultdict(list)
    # La home ENTRA al barrido. Era el punto ciego: docs.glob("*/index.html") solo mira
    # subpáginas, y la FAQ de la home (visible + schema FAQPage que Google muestra como
    # snippet) siguió recomendando a Devstral Small muerto sin que C1 chistara. (14-jul-2026)
    paginas = [docs / "index.html", *docs.glob("*/index.html")]
    for pagina in paginas:
        try:
            txt = pagina.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for n in muertos:
            if n in txt:
                culpables[n].append("home" if pagina.parent == docs else pagina.parent.name)
    if culpables:
        det = "; ".join(f"«{n}» en {len(p)} páginas" for n, p in list(culpables.items())[:3])
        fallo("C1 · nada muerto recomendado",
              f"{len(culpables)} modelos con endpoint muerto siguen en páginas del sitio: {det}. "
              f"Regenerá: python benchmarks/regenerate_all.py")
    elif verbose:
        print("  ✅ C1 · ninguna página recomienda un modelo muerto")


def c2_docs_cuadran(verbose):
    """Los docs vivos citan las cifras que dice la fuente."""
    import subprocess
    r = subprocess.run([sys.executable, str(ROOT / "benchmarks" / "check_consistency.py")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        fallo("C2 · docs vs fuente",
              "hay docs vivos citando scores obsoletos (corré check_consistency.py para el detalle)")
    elif verbose:
        print("  ✅ C2 · los docs citan lo que dice la fuente")


def c3_superficies_coinciden(models, verbose):
    """El #1 y el conteo son LOS MISMOS en models.json, README y MODELOS.md.

    Ya pasó: models.json rankeaba a un modelo #3 con 10 runs mientras las páginas pSEO
    —que sí filtran ≥50— mostraban otro ganador. Misma data, dos rankings públicos
    contradictorios.
    """
    r = sorted([m for m in models if m.get("ranked")],
               key=lambda x: -(x.get("score_global") or 0))
    if not r:
        fallo("C3 · superficies", "no hay modelos rankeados")
        return
    n1, n = r[0]["name"], len(r)

    for doc in ("README.md", "MODELOS.md"):
        p = ROOT / doc
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        # el #1 tiene que aparecer; si el doc nombra OTRO como #1, es contradicción
        if n1 not in txt:
            aviso("C3 · superficies", f"{doc} no menciona al #1 actual ({n1})")

    if verbose:
        print(f"  ✅ C3 · el #1 ({n1}) y el conteo ({n} rankeados) coinciden entre superficies")


# ─────────────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    print("\n  VALIDANDO EL BENCHMARK\n" + "  " + "─" * 66)

    runs = cargar_runs()
    if not MODELS_JSON.exists():
        sys.exit("  No existe models.json — corré export_for_pages.py primero")
    models = json.loads(MODELS_JSON.read_text())["models"]

    print(f"  {len(runs):,} runs · {len(models)} modelos · "
          f"{sum(1 for m in models if m.get('ranked'))} rankeados\n")

    a1_procedencia(runs, args.verbose)
    a2_una_formula_por_suite(runs, args.verbose)
    a3_sin_doble_conteo(args.verbose)
    b1_examen_completo(models, args.verbose)
    b2_rankeable(models, args.verbose)
    c1_nada_muerto_recomendado(models, args.verbose)
    c2_docs_cuadran(args.verbose)
    c3_superficies_coinciden(models, args.verbose)

    if AVISOS:
        print("\n  AVISOS (no bloquean):")
        for a in AVISOS:
            print(f"    ⚠️  {a}")

    if FALLOS:
        print(f"\n  ❌ {len(FALLOS)} INVARIANTE(S) ROTA(S) — NO SE PUEDE PUBLICAR\n")
        for f in FALLOS:
            print(f"    · {f}\n")
        print("  Un número solo se publica si los datos que lo sostienen son comparables.")
        print("  Si hay duda, se descarta la muestra: perder datos es mejor que publicar")
        print("  un promedio de peras y manzanas.\n")
        return 1

    print("\n  ✅ TODO CUADRA — el benchmark se puede publicar\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
