#!/usr/bin/env python3
"""¿Hay algo con forma de credencial en lo que se versiona? Lo responde gitleaks, no nosotros.

POR QUÉ EXISTE (3-nov-2026, corte-v5 1.7)
-----------------------------------------
La auditoría de los guardrails encontró que `check_secretos` da exit 0 con una clave hex de 64
al azar (AUDITORIA-GUARDRAILS-2026-11, H3). No es un bug: `check_secretos` busca los VALORES
EXACTOS del `.env`, que es lo que habría cazado la clave de R2 del 17-ago. Lo que nadie
miraba es lo que tiene FORMA de credencial sin estar en el `.env`. Para eso se adopta
gitleaks con sus reglas por defecto, sin escribir patrones propios (CLAUDE.md: no reinventar
el motor).

QUÉ MIRA
--------
El árbol de trabajo tal como lo versionaría git: lo commiteado más lo nuevo que no está
ignorado (`git ls-files -co --exclude-standard`). No el historial, que se revisa aparte, y no
lo ignorado: el `.env` real vive ahí. Las exclusiones por ruta y su porqué están en
`.gitleaks.toml`; los 3 secretos de mentira de los prompts, por huella en `.gitleaksignore`.

Sin gitleaks instalado sale en ROJO con la instrucción: un chequeo de secretos que se omite
en silencio es el verde vacío que la auditoría vino a cerrar.

Uso:  python benchmarks/check_gitleaks.py
"""

import json
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION = "8.30.1"   # la misma que instala el Action
SALTEADO = "benchmarks/results/"   # excluido en .gitleaks.toml; no copiarlo ahorra minutos


def instruccion() -> str:
    so = "darwin" if platform.system() == "Darwin" else "linux"
    arq = "arm64" if platform.machine() in ("arm64", "aarch64") else "x64"
    destino = "/opt/homebrew/bin" if so == "darwin" else "/usr/local/bin"
    return (f"curl -sSL https://github.com/gitleaks/gitleaks/releases/download/v{VERSION}/"
            f"gitleaks_{VERSION}_{so}_{arq}.tar.gz | tar -xz -C {destino} gitleaks")


def archivos() -> list[str]:
    r = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "-z"],
                       capture_output=True, text=True, cwd=ROOT, check=True)
    return [p for p in r.stdout.split("\0") if p and not p.startswith(SALTEADO)]


def main() -> int:
    exe = shutil.which("gitleaks")
    if not exe:
        print("  ❌ gitleaks no está instalado: sin él no se revisa nada con forma de credencial.")
        print(f"     Instalar la versión fijada ({VERSION}):\n     {instruccion()}")
        return 1
    v = subprocess.run([exe, "version"], capture_output=True, text=True).stdout.strip().lstrip("v")
    if v != VERSION:
        print(f"  ⚠️  gitleaks {v} instalado; el fijado es {VERSION} (el que usa el Action).")

    # Se copia a un directorio aparte lo que versionaría git: `gitleaks dir` no respeta
    # `.gitignore`, y escanear el árbol crudo lee el `.env` real, `.venv/` y `jobs/`.
    tmp = Path(tempfile.mkdtemp(prefix="gitleaks_"))
    try:
        lista = archivos()
        for rel in lista:
            src = ROOT / rel
            if src.is_file():
                (tmp / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, tmp / rel)
        reporte = tmp / "_reporte_gitleaks.json"
        r = subprocess.run(
            [exe, "dir", ".", "--no-banner", "--redact", "--exit-code", "1",
             "-c", str(ROOT / ".gitleaks.toml"), "-i", str(ROOT / ".gitleaksignore"),
             "--report-format", "json", "--report-path", str(reporte)],
            capture_output=True, text=True, cwd=tmp)
        hallazgos = json.loads(reporte.read_text() or "[]") if reporte.exists() else None
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if hallazgos is None or r.returncode not in (0, 1):
        print(f"  ❌ gitleaks no terminó (exit {r.returncode}): {r.stderr.strip()[-300:]}")
        return 1
    print(f"gitleaks {v} sobre {len(lista)} archivos versionables (sin `{SALTEADO}`)\n")
    if not hallazgos:
        print("  ✅ nada con forma de credencial en lo que se versiona.")
        return 0
    for h in hallazgos:
        print(f"  ❌ {h['File']}:{h['StartLine']} · {h['RuleID']} · {h['Match'][:60]}")
    print(f"\n  ❌ {len(hallazgos)} hallazgo(s). Si es una credencial: sacarla y ROTARLA. Si es un")
    print("     JSON generado con keys de modelos, agregar su ruta a .gitleaks.toml con su porqué.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
