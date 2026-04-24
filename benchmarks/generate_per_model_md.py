#!/usr/bin/env python3
"""
Genera MDs navegables por modelo a partir de resultados JSON.

Para cada modelo crea un archivo en benchmarks/results/per-model/<slug>.md
con todos los tests agrupados por suite, scores, response preview y
justificación del juez. También genera un index README.md con ranking.

Uso:
    python benchmarks/generate_per_model_md.py
    python benchmarks/generate_per_model_md.py --inputs benchmark_20260422_204025.json benchmark_20260423_051248.json
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

RESULTS_DIR = Path(__file__).parent / "results"
OUT_DIR = RESULTS_DIR / "per-model"

# Agrupación de suites por pilar (matches README.md)
PILARES = {
    "Razonamiento y Estrategia": ["deep_reasoning", "reasoning", "hallucination", "strategy"],
    "Coding y Datos": ["code_generation", "structured_output", "string_precision", "ocr_extraction"],
    "Contenido y Marketing": ["content_generation", "startup_content", "news_seo_writing", "creativity", "sales_outreach", "translation", "presentation"],
    "Agentes y Operaciones": ["tool_calling", "customer_support", "orchestration", "multi_turn", "policy_adherence", "agent_capabilities", "task_management", "summarization"],
}


def slug(s: str) -> str:
    return "".join(c if c.isalnum() or c in "-_" else "_" for c in s.lower())[:80]


def fmt(x, digits=2):
    if x is None or x == "":
        return "-"
    if isinstance(x, float):
        return f"{x:.{digits}f}"
    return str(x)


def load_results(input_files: list[str]) -> list[dict]:
    all_results = []
    for path in input_files:
        p = Path(path)
        if not p.is_absolute():
            p = RESULTS_DIR / p
        with open(p) as f:
            data = json.load(f)
        all_results.extend(data.get("results", []))
    return all_results


def group_by_model(results: list[dict]) -> dict[str, list[dict]]:
    by_model = defaultdict(list)
    for r in results:
        by_model[r["model"]].append(r)
    return by_model


def compute_summary(tests: list[dict]) -> dict:
    ok = [t for t in tests if t.get("success")]
    errors = [t for t in tests if not t.get("success")]
    s = {
        "total": len(tests),
        "ok": len(ok),
        "errors": len(errors),
        "model_id": tests[0].get("model_id", ""),
    }
    if ok:
        s["final"] = mean(t["final"] for t in ok)
        s["quality"] = mean(t["quality"] for t in ok)
        s["tokens_per_second"] = mean(t["tokens_per_second"] for t in ok if t.get("tokens_per_second"))
        s["latency_first_token"] = mean(t.get("latency_first_token", 0) for t in ok)
        s["cost_per_run"] = mean(t.get("cost_usd", 0) for t in ok)
        judges = [t["judge_score"] for t in ok if t.get("judge_score", -1) >= 0]
        s["judge_score"] = mean(judges) if judges else None
    return s


def render_model_md(model_name: str, tests: list[dict], summary: dict) -> str:
    lines = [f"# {model_name}", ""]
    lines.append(f"- **model_id**: `{summary['model_id']}`")
    lines.append(f"- **Total tests**: {summary['ok']}/{summary['total']} exitosos ({summary['errors']} errores)")
    if summary["ok"]:
        lines.append(f"- **Score final**: {fmt(summary['final'])}")
        lines.append(f"- **Calidad**: {fmt(summary['quality'])}")
        if summary.get("judge_score") is not None:
            lines.append(f"- **Judge score (Phi-4)**: {fmt(summary['judge_score'])}/10")
        lines.append(f"- **Velocidad**: {fmt(summary['tokens_per_second'], 0)} tok/s")
        lines.append(f"- **Latencia primera token**: {fmt(summary['latency_first_token'])}s")
        lines.append(f"- **Costo promedio por test**: ${fmt(summary['cost_per_run'], 5)}")
    lines.append("")
    lines.append(f"> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.")
    lines.append("")

    # Resumen por suite
    by_suite = defaultdict(list)
    for t in tests:
        by_suite[t.get("suite", "?")].append(t)

    lines.append("## Resumen por suite")
    lines.append("")
    lines.append("| Suite | Tests | OK | Score promedio | Calidad promedio |")
    lines.append("|-------|-------|----|----|----|")
    for suite_name in sorted(by_suite.keys()):
        suite_tests = by_suite[suite_name]
        ok = [t for t in suite_tests if t.get("success")]
        final_avg = mean(t["final"] for t in ok) if ok else None
        qual_avg = mean(t["quality"] for t in ok) if ok else None
        lines.append(f"| {suite_name} | {len(suite_tests)} | {len(ok)} | {fmt(final_avg)} | {fmt(qual_avg)} |")
    lines.append("")

    # Detalle por pilar → suite → test
    lines.append("## Detalle por test")
    lines.append("")

    seen_suites = set()
    for pilar, pilar_suites in PILARES.items():
        suites_in_pilar = [s for s in pilar_suites if s in by_suite]
        if not suites_in_pilar:
            continue
        lines.append(f"### {pilar}")
        lines.append("")
        for suite_name in suites_in_pilar:
            seen_suites.add(suite_name)
            suite_tests = by_suite[suite_name]
            lines.append(f"#### {suite_name}")
            lines.append("")
            lines.append("| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |")
            lines.append("|------|-------|---------|-------|-------|----------|--------|")
            for t in suite_tests:
                status = "OK" if t.get("success") else f"ERROR"
                judge = fmt(t.get("judge_score"), 1) if t.get("judge_score", -1) >= 0 else "-"
                lines.append(
                    f"| {t['test_name']} | {fmt(t.get('final'))} | {fmt(t.get('quality'))} | "
                    f"{judge} | {fmt(t.get('tokens_per_second'), 0)} | {fmt(t.get('latency_total'))}s | {status} |"
                )
            lines.append("")

            # Preview de cada test en detalle colapsable
            for t in suite_tests:
                preview = t.get("response_preview", "").strip()
                err = t.get("error", "").strip()
                judge_just = t.get("judge_justificacion", "").strip()
                # Solo incluir si hay algo que mostrar
                if not (preview or err or judge_just):
                    continue
                lines.append(f"<details><summary><code>{t['test_name']}</code> — score {fmt(t.get('final'))}</summary>")
                lines.append("")
                if t.get("success"):
                    lines.append(f"**Stats**: latencia {fmt(t.get('latency_total'))}s · {fmt(t.get('tokens_per_second'), 0)} tok/s · "
                                 f"{t.get('input_tokens', 0)}→{t.get('output_tokens', 0)} tokens · ${fmt(t.get('cost_usd', 0), 5)}")
                    lines.append("")
                if t.get("judge_score", -1) >= 0:
                    lines.append(f"**Juez Phi-4**: {fmt(t['judge_score'], 1)}/10 "
                                 f"(precisión:{t.get('judge_precision','?')}, relevancia:{t.get('judge_relevancia','?')}, "
                                 f"profundidad:{t.get('judge_profundidad','?')}, claridad:{t.get('judge_claridad','?')}, "
                                 f"utilidad:{t.get('judge_utilidad','?')})")
                    lines.append("")
                if judge_just:
                    lines.append(f"> {judge_just}")
                    lines.append("")
                if err:
                    lines.append(f"**Error**: `{err[:300]}`")
                    lines.append("")
                if preview:
                    lines.append("**Respuesta (preview 300 chars)**:")
                    lines.append("")
                    lines.append("```")
                    lines.append(preview)
                    lines.append("```")
                    lines.append("")
                if t.get("response_file"):
                    lines.append(f"**Respuesta completa**: [`{t['response_file']}`](../{t['response_file']})")
                    lines.append("")
                lines.append("</details>")
                lines.append("")

    # Suites fuera de pilares (por si aparecen)
    other_suites = [s for s in by_suite if s not in seen_suites]
    if other_suites:
        lines.append("### Otras suites")
        lines.append("")
        for suite_name in other_suites:
            lines.append(f"#### {suite_name}")
            lines.append("")

    return "\n".join(lines)


def render_index_md(summaries: list[tuple[str, dict]]) -> str:
    summaries_sorted = sorted(summaries, key=lambda x: -(x[1].get("final") or 0))
    lines = [
        "# Resultados por modelo",
        "",
        f"Rankings de **{len(summaries_sorted)} modelos** evaluados con Phi-4 judge (Microsoft, 14B, MIT).",
        "",
        "Cada archivo contiene los 91 tests del modelo con scores, preview de respuesta y justificación del juez.",
        "",
        "| # | Modelo | Final | Calidad | tok/s | OK/Total | Ver |",
        "|---|--------|-------|---------|-------|----------|-----|",
    ]
    for i, (model_name, s) in enumerate(summaries_sorted, 1):
        link = f"[{model_name}]({slug(s['model_id'])}.md)"
        lines.append(
            f"| {i} | {link} | {fmt(s.get('final'))} | {fmt(s.get('quality'))} | "
            f"{fmt(s.get('tokens_per_second'), 0)} | {s['ok']}/{s['total']} | "
            f"[ver detalles]({slug(s['model_id'])}.md) |"
        )
    lines.append("")
    lines.append("> Generado con `python benchmarks/generate_per_model_md.py`")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", default=None,
                        help="Archivos JSON de resultados. Si se omite, usa los 2 lotes del v2.1")
    parser.add_argument("--out", default=str(OUT_DIR),
                        help="Directorio de salida")
    args = parser.parse_args()

    if args.inputs is None:
        args.inputs = [
            "benchmark_20260422_204025.json",
            "benchmark_20260423_051248.json",
        ]

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    results = load_results(args.inputs)
    print(f"Cargados {len(results)} resultados de {len(args.inputs)} archivo(s)")

    by_model = group_by_model(results)
    print(f"Modelos: {len(by_model)}")

    summaries = []
    for model_name, tests in by_model.items():
        summary = compute_summary(tests)
        md = render_model_md(model_name, tests, summary)
        fname = f"{slug(summary['model_id'])}.md"
        (out_dir / fname).write_text(md)
        summaries.append((model_name, summary))
        print(f"  {fname}: {summary['ok']}/{summary['total']} tests, score {fmt(summary.get('final'))}")

    index = render_index_md(summaries)
    (out_dir / "README.md").write_text(index)
    print(f"\nIndex: {out_dir}/README.md")


if __name__ == "__main__":
    main()
