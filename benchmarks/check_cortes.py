#!/usr/bin/env python3
"""Verifica que los cortes por eje sigan el paso a la data que vamos generando.

POR QUÉ EXISTE (15-ago-2026)
----------------------------
Cristian, al pedirlos: *"recordar que esto tiene que tener guardrails también para
mantenerse actualizado con la data que vamos generando."*

Un corte por eje es una página que ordena por UNA suite en vez de por un promedio, y
existe porque los promedios esconden: **Gemini 3.6 Flash es #3 de 80 en calidad agéntica
y #76 de 80 en el índice general**, y el pilar Agentes tampoco lo mostraba (#65) porque
también promedia.

Ese tipo de página envejece de tres formas distintas, y ninguna rompe nada:

C1. Se mide una suite nueva y **nadie le hace su corte**: el eje existe en los datos y no
    se publica. Es el modo silencioso — la página que falta no da error.
C2. La página **se desincroniza** de `models.json` y publica un orden viejo.
C3. Un corte AGÉNTICO recomienda un modelo que **no corre dentro de un agente**. Pasó de
    verdad: `Llama 3.1 8B Instant` salía #4 en «tareas largas» y rompe el bucle de
    herramientas — la suite mide sostener el hilo SIN herramientas.

Uso:  python benchmarks/check_cortes.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

MODELS_JSON = ROOT / "docs" / "data" / "models.json"
DOCS = ROOT / "docs"

# Suites que describen trabajo DENTRO de un agente: sus cortes no pueden recomendar un
# modelo que no corre en uno. Debe coincidir con `generate_rankings.SUITES_AGENTICAS`.
SUITES_AGENTICAS = {"agent_long_horizon", "tool_calling", "tool_calling_adversarial",
                    "policy_adherence", "agent_capabilities", "orchestration", "multi_turn"}

# Ejes que MERECEN corte aunque todavía no lo tengan: los que deciden una elección real.
# Si se mide una suite nueva de esta lista y no tiene página, se avisa.
#
# La lista es de ids; **la frase humana sale del registro** (`benchmarks/suites.py`), no
# se escribe acá. Antes se escribía, y el 15-ago-2026 se midió el resultado: siete suites
# dichas de dos formas distintas según el archivo que las nombrara.
EJES_QUE_DECIDEN = [
    "agent_long_horizon", "policy_adherence", "string_precision", "tool_calling",
    "tool_calling_adversarial", "structured_output", "prompt_injection_es",
]


def _cortes_publicados() -> dict[str, Path]:
    """slug → path, de las páginas que ordenan por una suite."""
    from benchmarks.generate_rankings import RANKINGS  # noqa: E402
    return {p["suite"]: DOCS / p["slug"] / "index.html"
            for p in RANKINGS if p.get("criterion") == "suite"}


def main() -> int:
    d = json.loads(MODELS_JSON.read_text())
    ranked = [m for m in d["models"] if m.get("ranked")]
    try:
        cortes = _cortes_publicados()
    except Exception as e:
        print(f"  ❌ no se pudo leer la config de cortes: {e}")
        return 1

    fallos, avisos = [], []

    # ── C1 · ejes medidos que deciden y no tienen corte ────────────────────
    from benchmarks.suites import decide as _decide  # noqa: E402
    for suite in EJES_QUE_DECIDEN:
        para_que = _decide(suite)
        n = sum(1 for m in ranked if (m.get("score_by_suite") or {}).get(suite) is not None)
        if n == 0:
            continue                      # todavía no se mide: no corresponde exigirlo
        if suite not in cortes:
            avisos.append(f"`{suite}` está medida en {n} modelos rankeados y NO tiene "
                          f"corte publicado — el eje que decide «{para_que}» no se ve "
                          f"en el sitio")

    # ── C2 · la página existe y está al día con models.json ────────────────
    for suite, path in cortes.items():
        if not path.exists():
            fallos.append(f"`{suite}`: la config declara el corte y la página no existe "
                          f"({path.relative_to(ROOT)})")
            continue
        vals = [(m["name"], (m.get("score_by_suite") or {}).get(suite)) for m in ranked]
        vals = [(n, v) for n, v in vals if v is not None]
        if not vals:
            continue
        esperado = max(vals, key=lambda x: x[1])[0]
        html = path.read_text(errors="replace")
        # el #1 de la tabla
        m1 = re.search(r"<tr><td>1</td><td>(?:<strong>)?([^<]+)", html)
        publicado = m1.group(1).strip() if m1 else None
        if publicado and esperado not in publicado and publicado not in esperado:
            # puede diferir legítimamente si el #1 quedó excluido por el filtro agéntico
            aptos = [(n, v) for n, v in vals
                     if suite not in SUITES_AGENTICAS
                     or next((x for x in ranked if x["name"] == n), {}).get("sirve_para_agentes") is not False]
            esperado_apto = max(aptos, key=lambda x: x[1])[0] if aptos else None
            if esperado_apto and esperado_apto not in publicado:
                fallos.append(f"`{suite}`: la página publica «{publicado}» como #1 y los "
                              f"datos dicen «{esperado_apto}» — está desincronizada")

    # ── C3 · un corte agéntico no puede coronar a quien no corre en un agente ──
    no_aptos = {m["name"] for m in d["models"] if m.get("sirve_para_agentes") is False}
    for suite, path in cortes.items():
        if suite not in SUITES_AGENTICAS or not path.exists():
            continue
        html = path.read_text(errors="replace")
        filas = re.findall(r"<tr><td>\d+</td><td>(?:<strong>)?([^<]+)", html)
        colados = [f.strip() for f in filas if f.strip() in no_aptos]
        if colados:
            fallos.append(f"`{suite}`: el corte recomienda a {', '.join(colados)}, que NO "
                          f"corre dentro de un agente. Esta suite mide sostener el hilo "
                          f"SIN herramientas — lucirse acá y romper el bucle es compatible")


    # ── C4 · la segunda tabla se decide con el dato, no a mano ─────────────
    #
    # POR QUÉ (17-ago-2026). Se activó a mano en dos cortes con el argumento «ahí el eje
    # satura». Medido: ningún corte satura, y el criterio que sí importa —cuánto se
    # parecen el orden por capacidad y el orden por capacidad-precio— decía lo contrario.
    # Las páginas donde MÁS aportaba (español y contenido, correlación +0,244) eran justo
    # las que no la tenían.
    #
    # Un flag a mano envejece con el catálogo: entra un modelo barato y bueno, la
    # correlación cambia, y nadie vuelve a mirar. Esto verifica que lo publicado coincida
    # con lo que el criterio dice HOY.
    try:
        import sys as _s
        _s.path.insert(0, str(ROOT / "benchmarks"))
        from generate_rankings import _lleva_segunda_tabla, RANKINGS, rank_models
        _d = json.loads(MODELS_JSON.read_text())
        for c in RANKINGS:
            pg = DOCS / c["slug"] / "index.html"
            if not pg.exists():
                continue
            debe = _lleva_segunda_tabla(c, rank_models(_d["models"], c))
            tiene = "La misma capacidad, por lo que cuesta" in pg.read_text(errors="replace")
            if debe != tiene:
                fallos.append(
                    f"`{c['slug']}`: {'le falta' if debe else 'le sobra'} la segunda tabla "
                    f"(capacidad-por-precio). El criterio se mide, no se declara: "
                    f"regenerá con generate_rankings.py")
    except Exception as e:
        avisos.append(f"no se pudo verificar la segunda tabla: {e}")

    print(f"\nVerificando {len(cortes)} cortes por eje contra models.json…\n")
    for a in avisos:
        print(f"  ⚠️  {a}")
    for f in fallos:
        print(f"  ❌ {f}")
    if fallos:
        print(f"\n  ❌ {len(fallos)} corte(s) con problema. Corré "
              f"`python benchmarks/generate_rankings.py`.")
        return 1
    print(f"\n  ✅ los {len(cortes)} cortes coinciden con los datos"
          + (f" · {len(avisos)} eje(s) medidos esperando su corte" if avisos else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
