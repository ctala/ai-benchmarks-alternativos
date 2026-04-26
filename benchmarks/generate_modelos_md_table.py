#!/usr/bin/env python3
"""
Genera tabla de modelos probados para MODELOS.md con links a:
1. MD por modelo en benchmarks/results/per-model/
2. Carpeta de responses individuales

Uso:
    python benchmarks/generate_modelos_md_table.py        # imprime la tabla a stdout
    python benchmarks/generate_modelos_md_table.py -i     # actualiza MODELOS.md in-place
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent
RESULTS_DIR = ROOT / "benchmarks" / "results"
PER_MODEL_DIR = RESULTS_DIR / "per-model"
RESPONSES_DIR = RESULTS_DIR / "responses"


def model_id_to_per_model_filename(model_id: str) -> str:
    """Convierte 'anthropic/claude-opus-4-7' → 'anthropic_claude-opus-4-7.md'.
    Las versiones con punto se reemplazan por '_' (ej. gpt-4.1 → gpt-4_1.md)."""
    safe = model_id.replace("/", "_").replace(".", "_").replace(":", "_")
    return f"{safe}.md"


def load_tested_models():
    """Devuelve dict {model_id: {runs, score, name_safe_for_link}}"""
    by_model = defaultdict(lambda: {"runs": 0, "scores": [], "tier": None, "open_source": None, "license": None, "ci": None, "co": None, "lotes": set(), "name": None})

    # Carga config para metadata
    sys.path.insert(0, str(ROOT / "benchmarks"))
    from config import MODELS

    cfg_by_id = {v["id"]: (k, v) for k, v in MODELS.items()}

    for fn in sorted(os.listdir(RESULTS_DIR)):
        if not (fn.startswith("benchmark_") and fn.endswith(".json")):
            continue
        try:
            data = json.loads((RESULTS_DIR / fn).read_text())
        except Exception:
            continue
        results = data if isinstance(data, list) else data.get("results", [])
        # Lote label desde fecha del archivo
        m = re.match(r"benchmark_(\d{8})_", fn)
        lote = m.group(1) if m else "?"
        for r in results:
            if not r.get("success"):
                continue
            mid = r.get("model_id") or r.get("model") or "?"
            by_model[mid]["runs"] += 1
            if r.get("final") is not None:
                by_model[mid]["scores"].append(r["final"])
            by_model[mid]["lotes"].add(lote)
            cfg = cfg_by_id.get(mid)
            if cfg:
                _key, info = cfg
                by_model[mid]["tier"] = info.get("tier")
                by_model[mid]["open_source"] = info.get("open_source")
                by_model[mid]["license"] = info.get("license", "")
                by_model[mid]["ci"] = info.get("cost_input")
                by_model[mid]["co"] = info.get("cost_output")
                by_model[mid]["name"] = info.get("name", mid)
            elif by_model[mid]["name"] is None:
                by_model[mid]["name"] = mid
    # Filtrar solo testados (>=50 runs)
    return {mid: info for mid, info in by_model.items() if info["runs"] >= 50}


def find_response_dirs(model_id: str) -> list[str]:
    """Devuelve lista de carpetas relative paths donde el modelo tiene responses."""
    if not RESPONSES_DIR.exists():
        return []
    found = []
    safe_id = model_id.replace("/", "_").replace(":", "_")
    for ts_dir in sorted(RESPONSES_DIR.iterdir(), reverse=True):
        if not ts_dir.is_dir():
            continue
        # Buscar archivos que empiecen con el model_id (config key o el id)
        # Los responses se nombran como <key>__<suite>__<test>.md (ej. devstral__...)
        # Usamos mid sanitized para ver si hay match
        for f in ts_dir.iterdir():
            if not f.name.endswith(".md"):
                continue
            # Match flexible: prefijo es model_key normalizado, no model_id
            # Devolvemos la carpeta si tiene al menos un archivo con prefijo del nombre
            stem = f.name.split("__")[0]
            mid_short = model_id.split("/")[-1].replace(".", "")
            if mid_short.lower() in stem.lower() or stem.lower() in mid_short.lower():
                found.append(ts_dir.name)
                break
    return found


def build_links(model_id: str) -> tuple[str, str]:
    """Devuelve (link_md, link_responses)."""
    # MD por modelo
    fname = model_id_to_per_model_filename(model_id)
    md_path = PER_MODEL_DIR / fname
    if md_path.exists():
        link_md = f"[per-model](benchmarks/results/per-model/{fname})"
    else:
        link_md = "—"

    # Responses (link a la primera carpeta con responses para este modelo)
    response_dirs = find_response_dirs(model_id)
    if response_dirs:
        link_resp = f"[responses](benchmarks/results/responses/{response_dirs[0]}/)"
    else:
        link_resp = "—"

    return link_md, link_resp


def build_table(models: dict) -> str:
    out = []
    out.append("| Modelo | OS | $ in/out | Avg score | Runs | Per-model MD | Responses |")
    out.append("|---|---|---|---:|---:|---|---|")

    # Ordenar por avg score descendente
    sorted_models = sorted(models.items(), key=lambda x: -(sum(x[1]["scores"])/len(x[1]["scores"]) if x[1]["scores"] else 0))

    for mid, info in sorted_models:
        avg = sum(info["scores"]) / len(info["scores"]) if info["scores"] else 0
        os_label = "✅" if info["open_source"] else "❌" if info["open_source"] is False else "?"
        ci, co = info.get("ci"), info.get("co")
        cost = f"{ci}/{co}" if ci is not None else "—"
        link_md, link_resp = build_links(mid)
        out.append(f"| `{mid}` | {os_label} {info.get('license') or ''} | ${cost} | **{avg:.2f}** | {info['runs']} | {link_md} | {link_resp} |")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in-place", action="store_true", help="Actualiza MODELOS.md in-place")
    args = ap.parse_args()

    models = load_tested_models()
    table = build_table(models)

    if args.in_place:
        modelos_md = ROOT / "MODELOS.md"
        content = modelos_md.read_text()
        # Reemplazar la sección entre los marcadores. Si no existen, ponerlos.
        START = "<!-- AUTO-TABLE-START -->"
        END = "<!-- AUTO-TABLE-END -->"
        new_block = f"{START}\n\n> Auto-generado por `benchmarks/generate_modelos_md_table.py`. **No editar a mano** — re-correr el script tras cada lote.\n\n{table}\n\n{END}"

        if START in content and END in content:
            new_content = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", new_block, content, flags=re.DOTALL)
        else:
            # Insertar al inicio de "## Probados"
            new_content = content.replace("## Probados", f"## Probados\n\n{new_block}\n\n#### Tabla manual (legacy):", 1)
        modelos_md.write_text(new_content)
        print(f"OK: MODELOS.md actualizado con tabla de {len(models)} modelos")
    else:
        print(table)


if __name__ == "__main__":
    main()
