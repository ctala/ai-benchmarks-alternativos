#!/usr/bin/env python3
"""Redacta secretos (webhooks Slack/Discord, claves sk-*, tokens xox*) en los
artefactos del benchmark (responses .md + results JSON).

Los modelos a veces alucinan webhooks o claves en tests de orquestación/n8n;
GitHub push-protection bloquea el push si llegan al repo público. El runner ya
redacta al guardar (ver `_redact_secrets` en runner.py), pero este script sirve
para:
- limpiar artefactos viejos generados antes del fix,
- correr como paso pre-commit / en la GitHub Action regenerate-auto-artifacts.

Uso:  python benchmarks/sanitize_results.py [ruta]   (default: benchmarks/results)
"""
import re
import sys
import pathlib

SECRET_PATTERNS = [
    (re.compile(r'https://hooks\.slack\.com/services/[A-Za-z0-9/_+=-]+'),
     'https://hooks.slack.com/services/REDACTED'),
    (re.compile(r'https://discord(?:app)?\.com/api/webhooks/[A-Za-z0-9/_-]+'),
     'https://discord.com/api/webhooks/REDACTED'),
    (re.compile(r'sk-(?:or-v1|proj|cp|ant)-[A-Za-z0-9_-]{8,}'), 'REDACTED-SECRET'),
    (re.compile(r'xox[baprs]-[A-Za-z0-9-]{10,}'), 'REDACTED-SLACK-TOKEN'),
]


def redact(text: str) -> str:
    for pat, repl in SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text


def main(root: str = "benchmarks/results") -> int:
    base = pathlib.Path(root)
    n = 0
    for p in list(base.rglob("*.md")) + list(base.rglob("*.json")):
        try:
            t = p.read_text()
        except Exception:
            continue
        nt = redact(t)
        if nt != t:
            p.write_text(nt)
            n += 1
    print(f"sanitize_results: {n} archivos redactados en {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "benchmarks/results"))
