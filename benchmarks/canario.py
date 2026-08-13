#!/usr/bin/env python3
"""
Canario — 5 tests en 1 modelo antes de lanzar un lote. Si algo chilla, no arranca.

POR QUÉ EXISTE
--------------
El 12-ago-2026 los fallos se partieron en dos grupos limpios:

  ANTICIPADOS (todos tenían un chequeo previo)
    · Glimmer y Muse Spark thinking      → 2 exámenes en blanco evitados
    · 5 de 9 del lote devolvían vacío    → medio lote
    · 19 keys inventadas en un script    → 19 corridas fallidas
    · 2 modelos muertos en el ranking    → seguir recomendándolos

  DESCUBIERTOS TARDE (ninguno tenía chequeo)
    · `temperature` + require_parameters → 4 runs
    · skip de niah sin margen de salida  → 378 runs en 23 modelos
    · juez corriendo donde se descarta   → horas por modelo, meses
    · `orchestration` midiendo prosa     → meses de recomendación equivocada

**Anticipamos lo que tiene instrumento; descubrimos tarde lo que no lo tiene.** No es
cuestión de atención.

La diferencia con los otros detectores del repo: `audit_suites.py`, `E7`, `E8` y
`check_endpoints.py` buscan **problemas conocidos**. El canario verifica **invariantes**,
así que caza regresiones que todavía no conocemos — que es la clase que más duele.

El caso que lo motivó: activar `require_parameters` (arreglo de la mañana) dejó
`temperature` en el request, y ningún proveedor de `gpt-5.6-luna-pro` la declara. El lote
falló las 4 pruebas de tool calling. Con canario se cazaba en **1 test**, antes de lanzar.

QUÉ VERIFICA
------------
1. **Responde** — success, y `content` no vacío (el modo de falla de los thinking).
2. **Emite tool calls** cuando el test da herramientas.
3. **Registra el proveedor upstream** — si falta, no vamos a poder auditar después.
4. **Guarda la entrada** — `prompt_sha` presente.
5. **Tasa de fallo bajo el umbral.**

Uso:
    python benchmarks/canario.py --models gpt-5.6-luna-pro
    python benchmarks/canario.py --models claude-opus-5 --extra --allow-anthropic-api
    python benchmarks/canario.py --models a b c        # uno por modelo
"""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Un test por dimensión de riesgo. `tool_calling` es obligatorio: es donde se rompió
# el ruteo dos veces el 12-ago y donde más cambia v4.1.
SUITES_CANARIO = ["tool_calling", "structured_output", "business_audit"]
MAX_FALLO = 0.34   # más de un tercio fallando = algo sistémico, no mala suerte


def correr(model_key: str, extra: list[str]) -> list[dict]:
    with tempfile.NamedTemporaryFile("w", suffix=".json", dir=ROOT / "benchmarks/results",
                                     delete=False) as f:
        tmp = Path(f.name)
        json.dump({"metadata": {"timestamp": "canario", "partial": True}, "results": []}, f)
    try:
        cmd = [str(ROOT / ".venv/bin/python"), str(ROOT / "benchmarks/runner.py"),
               "--quick", "--models", model_key, "--tests", *SUITES_CANARIO,
               "--resume", str(tmp.relative_to(ROOT))] + extra
        subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=1800)
        return json.loads(tmp.read_text()).get("results", [])
    finally:
        tmp.unlink(missing_ok=True)


def revisar(model_key: str, runs: list[dict]) -> list[str]:
    """Devuelve la lista de invariantes rotos. Vacía = puede lanzarse el lote."""
    problemas = []
    if not runs:
        return [f"{model_key}: CERO runs — el runner no midió nada "
                f"(¿key inexistente? ¿modelo bloqueado por default?)"]

    ok = [r for r in runs if r.get("success")]
    tasa = 1 - len(ok) / len(runs)
    if tasa > MAX_FALLO:
        errores = {str(r.get("error"))[:70] for r in runs if not r.get("success")}
        problemas.append(f"{model_key}: {tasa:.0%} de fallo ({len(runs)-len(ok)}/{len(runs)}). "
                         f"Errores: {list(errores)[:2]}")
    if not ok:
        return problemas

    # 1. Respuestas vacías: el modo de falla de los thinking sin su patrón declarado.
    vacias = [r for r in ok if not (r.get("response_preview") or "").strip()]
    if len(vacias) > len(ok) * 0.3:
        problemas.append(f"{model_key}: {len(vacias)}/{len(ok)} respuestas VACÍAS — "
                         f"¿falta el patrón en THINKING_MODELS?")

    # 2. Tool calls donde el test da herramientas.
    #
    # ⚠️ Se mira sobre TODOS los runs de la suite, no solo los exitosos. La primera
    # versión filtraba por `ok` y el chequeo se salteaba solo cuando los tests de
    # herramientas fallaban ENTEROS — que es justo el caso que hay que cazar.
    # Detectado al validar el canario contra Nemotron 3.5 Lightning, que no tiene
    # ningún proveedor con tools en OpenRouter: dijo "invariantes OK" con las 4
    # pruebas de tool calling caídas. Un chequeo que no puede fallar no es un chequeo:
    # es la misma falla que veníamos persiguiendo, cometida por su propio detector.
    tool_all = [r for r in runs if r.get("suite") == "tool_calling"]
    tool_ok = [r for r in tool_all if r.get("success")]
    if tool_all and not tool_ok:
        errs = {str(r.get("error"))[:70] for r in tool_all}
        problemas.append(f"{model_key}: los {len(tool_all)} tests con herramientas "
                         f"FALLARON. {list(errs)[:1]}")
    elif tool_ok and not any((r.get("tool_calls_made") or 0) > 0 for r in tool_ok):
        problemas.append(f"{model_key}: CERO tool calls en {len(tool_ok)} tests con "
                         f"herramientas — ¿el proveedor las soporta? ¿require_parameters?")
    elif tool_all and len(tool_ok) < len(tool_all):
        problemas.append(f"{model_key}: {len(tool_all)-len(tool_ok)} de {len(tool_all)} "
                         f"tests con herramientas fallaron (parcial, revisar por qué)")

    # 3. Proveedor upstream registrado: sin esto no se puede auditar después.
    if not any(r.get("upstream_provider") for r in ok):
        problemas.append(f"{model_key}: ningún run registró `upstream_provider`")

    # 4. Entrada guardada.
    if not any(r.get("prompt_sha") for r in ok):
        problemas.append(f"{model_key}: ningún run guardó `prompt_sha`")

    return problemas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--extra", nargs=argparse.REMAINDER, default=[],
                    help="flags extra para el runner (ej. --allow-anthropic-api)")
    args = ap.parse_args()

    print(f"CANARIO — {len(SUITES_CANARIO)} suites en {len(args.models)} modelo(s)")
    print(f"  suites: {', '.join(SUITES_CANARIO)}\n")

    todos = []
    for k in args.models:
        runs = correr(k, args.extra)
        problemas = revisar(k, runs)
        ok = sum(1 for r in runs if r.get("success"))
        estado = "✅" if not problemas else "🔴"
        print(f"  {estado} {k:<28} {ok}/{len(runs)} ok")
        for p in problemas:
            print(f"       └ {p}")
        todos += problemas

    print()
    if todos:
        print("=" * 70)
        print(f"  {len(todos)} INVARIANTE(S) ROTO(S) — NO lanzar el lote")
        print("=" * 70)
        return 1
    # Recibo. El canario estaba documentado en SEIS lugares y exigido en cero: se
    # corría cuando alguien se acordaba. Con el recibo, el runner puede negarse a
    # lanzar un lote grande sin uno fresco — que es la diferencia entre una regla
    # escrita y una regla que se cumple.
    import datetime as _dt
    recibo = ROOT / "benchmarks" / "results" / "_canario_ultimo.json"
    recibo.write_text(json.dumps({
        "cuando": _dt.datetime.now().isoformat(timespec="seconds"),
        "modelos": list(args.models),
        "suites": list(SUITES_CANARIO),
        "ok": True,
    }, ensure_ascii=False, indent=2))
    print("  ✓ invariantes OK — el lote puede lanzarse")
    return 0


if __name__ == "__main__":
    sys.exit(main())
