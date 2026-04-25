#!/usr/bin/env python3
"""
Genera TESTS.md auditando las 23 suites de tests del benchmark.

Lee `ALL_TEST_SUITES` desde `benchmarks/runner.py` (sin importarlo) para que
cualquier suite nueva agregada al runner aparezca automaticamente en el doc.

Uso:
    python benchmarks/generate_tests_md.py            # genera TESTS.md
    python benchmarks/generate_tests_md.py -o foo.md  # archivo alternativo
"""

import argparse
import importlib
import sys
from pathlib import Path

# Anadir root al path para importar benchmarks.tests
sys.path.insert(0, str(Path(__file__).parent.parent))

from benchmarks.tests import (
    content_generation, tool_calling, task_management,
    code_generation, reasoning, summarization, presentation,
    startup_content, deep_reasoning, customer_support, structured_output,
    hallucination, creativity, string_precision, news_seo_writing,
    ocr_extraction, orchestration, multi_turn, policy_adherence,
    agent_capabilities, strategy, sales_outreach, translation,
)

# Mismo orden que en runner.py para que el doc coincida con la ejecucion
SUITES = [
    ("content_generation", content_generation, "Contenido/Marketing"),
    ("tool_calling", tool_calling, "Agentes/Operaciones"),
    ("task_management", task_management, "Agentes/Operaciones"),
    ("code_generation", code_generation, "Coding"),
    ("reasoning", reasoning, "Razonamiento"),
    ("summarization", summarization, "Contenido/Marketing"),
    ("presentation", presentation, "Contenido/Marketing"),
    ("startup_content", startup_content, "Contenido/Marketing"),
    ("deep_reasoning", deep_reasoning, "Razonamiento"),
    ("customer_support", customer_support, "Agentes/Operaciones"),
    ("structured_output", structured_output, "Coding"),
    ("hallucination", hallucination, "Razonamiento"),
    ("creativity", creativity, "Contenido/Marketing"),
    ("string_precision", string_precision, "Coding"),
    ("news_seo_writing", news_seo_writing, "Contenido/Marketing"),
    ("ocr_extraction", ocr_extraction, "Coding"),
    ("orchestration", orchestration, "Agentes/Operaciones"),
    ("multi_turn", multi_turn, "Agentes/Operaciones"),
    ("policy_adherence", policy_adherence, "Agentes/Operaciones"),
    ("agent_capabilities", agent_capabilities, "Agentes/Operaciones"),
    ("strategy", strategy, "Razonamiento"),
    ("sales_outreach", sales_outreach, "Contenido/Marketing"),
    ("translation", translation, "Contenido/Marketing"),
]


def truncate(s: str, n: int = 240) -> str:
    s = s.strip().replace("\n", " ").replace("|", "\\|")
    return s if len(s) <= n else s[:n].rstrip() + "..."


def first_user_prompt(test: dict) -> str:
    msgs = test.get("messages", [])
    for m in msgs:
        if m.get("role") == "user":
            return m.get("content", "")
    return msgs[0].get("content", "") if msgs else ""


def summarize_validation(test: dict) -> str:
    parts = []
    if "expected_tools" in test:
        tools = test["expected_tools"]
        if isinstance(tools, list):
            names = []
            for t in tools:
                if isinstance(t, str):
                    names.append(t)
                elif isinstance(t, dict):
                    # tool dict: { "function": {"name": ...}} o {"name": ...}
                    fn = t.get("function", t)
                    n = fn.get("name") if isinstance(fn, dict) else None
                    if n:
                        names.append(n)
            if names:
                parts.append(f"tools=[{', '.join(names)}]")
    crit = test.get("criteria", {})
    if crit:
        bits = []
        if "min_words" in crit: bits.append(f"min_words={crit['min_words']}")
        if "max_words" in crit: bits.append(f"max_words={crit['max_words']}")
        if "language" in crit: bits.append(f"lang={crit['language']}")
        if "required_sections" in crit:
            secs = crit["required_sections"]
            n = len(secs)
            sample = ", ".join(secs[:3]) + ("..." if n > 3 else "")
            bits.append(f"secciones={n} ({sample})")
        if bits:
            parts.append("criteria: " + "; ".join(bits))
    if "expected_answer" in test:
        ea = test["expected_answer"]
        if isinstance(ea, dict):
            keys = list(ea.keys())
            parts.append(f"expected_answer keys: {', '.join(keys)}")
    return " · ".join(parts) if parts else "—"


def module_doc(mod) -> str:
    doc = (mod.__doc__ or "").strip()
    return doc.split("\n\n")[0].replace("\n", " ").strip() if doc else ""


def build_md() -> str:
    total_tests = sum(len(mod.TESTS) for _, mod, _ in SUITES)
    total_suites = len(SUITES)

    out = []
    out.append("# Tests del Benchmark")
    out.append("")
    out.append("> Auto-generado por `benchmarks/generate_tests_md.py`. **No editar a mano** — re-correr el script tras agregar/cambiar tests.")
    out.append("")
    out.append(f"**Total**: {total_tests} tests en {total_suites} suites organizadas en 4 pilares del emprendedor.")
    out.append("")
    out.append("Cada modelo se mide contra los {n} tests con scoring en 3 capas (formato + sustancia + LLM-as-Judge). Detalles del scoring en [README.md](README.md#metodologia) y [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md).".format(n=total_tests))
    out.append("")

    # Resumen por pilar
    out.append("## Resumen por pilar")
    out.append("")
    out.append("| Pilar | Suites | Tests |")
    out.append("|---|---|---|")
    by_pilar: dict[str, list] = {}
    for name, mod, pilar in SUITES:
        by_pilar.setdefault(pilar, []).append((name, len(mod.TESTS)))
    for pilar in ["Razonamiento", "Coding", "Contenido/Marketing", "Agentes/Operaciones"]:
        suites = by_pilar.get(pilar, [])
        suite_names = ", ".join(s[0] for s in suites)
        total = sum(s[1] for s in suites)
        out.append(f"| **{pilar}** | {len(suites)} ({suite_names}) | {total} |")
    out.append("")

    # Indice
    out.append("## Indice de suites")
    out.append("")
    out.append("| # | Suite | Pilar | Tests | Resumen |")
    out.append("|---|---|---|---|---|")
    for i, (name, mod, pilar) in enumerate(SUITES, 1):
        doc = truncate(module_doc(mod), 120)
        out.append(f"| {i} | [{name}](#{name.replace('_','-')}) | {pilar} | {len(mod.TESTS)} | {doc} |")
    out.append("")

    # Detalle por suite
    out.append("## Detalle por suite")
    out.append("")

    for name, mod, pilar in SUITES:
        doc = module_doc(mod)
        out.append(f"### {name}")
        out.append("")
        out.append(f"**Pilar**: {pilar} · **Tests**: {len(mod.TESTS)}")
        out.append("")
        if doc:
            out.append(f"_{doc}_")
            out.append("")

        for j, t in enumerate(mod.TESTS, 1):
            tname = t.get("name", f"test_{j}")
            tdesc = t.get("description", "")
            prompt = truncate(first_user_prompt(t), 280)
            validation = summarize_validation(t)

            out.append(f"<details><summary><b>{j}. {tname}</b> — {tdesc}</summary>")
            out.append("")
            out.append("**Prompt**:")
            out.append("")
            out.append(f"> {prompt}")
            out.append("")
            out.append(f"**Validacion**: {validation}")
            out.append("")
            out.append("</details>")
            out.append("")

    out.append("---")
    out.append("")
    out.append("Para ver respuestas reales por modelo: `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md`.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="TESTS.md", help="Archivo de salida")
    args = ap.parse_args()

    md = build_md()
    out_path = Path(args.output)
    out_path.write_text(md, encoding="utf-8")

    total_tests = sum(len(mod.TESTS) for _, mod, _ in SUITES)
    print(f"OK escrito: {out_path} ({total_tests} tests, {len(SUITES)} suites)")


if __name__ == "__main__":
    main()
