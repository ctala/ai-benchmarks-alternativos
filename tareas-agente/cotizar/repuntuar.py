#!/usr/bin/env python3
"""Re-puntúa las corridas guardadas SIN volver a llamar a ningún modelo.

Existe por la misma razón que `rescore_all.py` en el repo: arreglar un check no puede
costar re-medir. Uso: python repuntuar.py
"""
import json, subprocess, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
for f in sorted(AQUI.glob("res_*.json")):
    d = json.loads(f.read_text())
    for modelo, corridas in d.items():
        for r in corridas:
            ruta = r.get("respuesta")
            if not ruta or not (AQUI / ruta).exists():
                continue
            out = subprocess.run([sys.executable, str(AQUI / "verificar.py"),
                                  str(AQUI / ruta)], capture_output=True, text=True).stdout
            for l in out.splitlines()[::-1]:
                if l.startswith("{"):
                    r.update(json.loads(l)); break
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1))
print("  re-puntuado desde las respuestas guardadas, sin re-medir")
