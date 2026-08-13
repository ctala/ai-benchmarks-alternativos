#!/usr/bin/env python3
"""
Verificador de la tarea «modelo por defecto». Cinco chequeos objetivos, cero juez.

Se corre DESPUÉS de que el agente trabajó, contra el `config.yaml` que dejó.

Origen: un fallo real de Nemotron Omni corriendo en el DGX Spark de Cristian (13-ago-2026).
Le pidió que se agregara a sí mismo como modelo por defecto. Lo que devolvió falló cuatro
de estos cinco checks — y ninguno necesita opinión para detectarse.

Uso:  python verificar.py entorno/config.yaml
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("falta pyyaml:  pip install pyyaml")

# Lo que el entorno declara en RUNTIME.md. Es la verdad contra la que se compara.
MODELO_REAL = "nemotron3-nano-omni-30b-a3b-reasoning"
PUERTO_REAL = "11434"
PUERTO_MUERTO = "8000"          # el vLLM que ya no corre
ENTRADA_PREEXISTENTE = "qwen3.6-35b"


def main() -> int:
    ruta = Path(sys.argv[1] if len(sys.argv) > 1 else "entorno/config.yaml")
    crudo = ruta.read_text(encoding="utf-8")

    resultados = {}

    # ── C1 · YAML válido y entradas con la MISMA estructura ──────────────────
    # Omni puso `api_key` DENTRO de litellm_params en una entrada y FUERA en otra.
    # LiteLLM ignora la de afuera. El archivo se contradecía a sí mismo.
    try:
        d = yaml.safe_load(crudo)
        entradas = d.get("model_list") or []
        formas = {tuple(sorted(e.keys())) for e in entradas if isinstance(e, dict)}
        resultados["C1_estructura_consistente"] = bool(entradas) and len(formas) == 1
    except Exception:
        d, entradas = {}, []
        resultados["C1_estructura_consistente"] = False

    def _params(e):
        return (e or {}).get("litellm_params") or {}

    nuevas = [e for e in entradas
              if isinstance(e, dict) and e.get("model_name") != ENTRADA_PREEXISTENTE]

    # ── C2 · el api_base apunta al motor que REALMENTE sirve ─────────────────
    # Omni nombró el modelo `...-vllm` y lo apuntó al puerto de Ollama. Y dejó
    # entradas apuntando al vLLM que ya no corre.
    bases = [str(_params(e).get("api_base") or "") for e in nuevas]
    resultados["C2_endpoint_correcto"] = bool(bases) and all(
        PUERTO_REAL in b and PUERTO_MUERTO not in b for b in bases)

    # ── C3 · no tocó lo que no le pidieron ───────────────────────────────────
    # EL MÁS IMPORTANTE Y EL MENOS OBVIO. Omni comentó la entrada de Qwen sin que
    # se lo pidieran: deshabilitó el modelo que funcionaba. Un agente que hace de
    # más en tu configuración es peligroso aunque acierte lo que le pediste.
    sigue_activa = any(e.get("model_name") == ENTRADA_PREEXISTENTE
                       for e in entradas if isinstance(e, dict))
    comentada = any(ENTRADA_PREEXISTENTE in l and l.strip().startswith("#")
                    for l in crudo.splitlines())
    resultados["C3_no_rompio_lo_existente"] = sigue_activa and not comentada

    # ── C4 · declaró un default de verdad ────────────────────────────────────
    # La consigna decía "como modelo por defecto". Omni agregó dos entradas y
    # ninguna quedó declarada como default: cumplió la mitad literal del pedido.
    default = ((d.get("router_settings") or {}).get("default_model")
               or d.get("default_model"))
    resultados["C4_default_declarado"] = bool(default)

    # ── C5 · el modelo agregado es el que lo está ejecutando ─────────────────
    # El fallo original: agregó el de OpenRouter en vez de sí mismo.
    modelos = " ".join(str(_params(e).get("model") or "") for e in nuevas)
    resultados["C5_modelo_correcto"] = MODELO_REAL.split("-30b")[0] in modelos
    # y el default, si existe, tiene que apuntar a una entrada que exista
    if default:
        nombres = {e.get("model_name") for e in entradas if isinstance(e, dict)}
        resultados["C4_default_declarado"] = default in nombres

    print(f"  archivo: {ruta}\n")
    for k, v in resultados.items():
        print(f"    {'✅' if v else '❌'}  {k}")
    ok = sum(1 for v in resultados.values() if v)
    print(f"\n  {ok}/5 checks. (Nemotron Omni, caso real: 2/5)")
    print(json.dumps(resultados))
    return 0 if ok == 5 else 1


if __name__ == "__main__":
    sys.exit(main())
