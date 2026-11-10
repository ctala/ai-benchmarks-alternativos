#!/usr/bin/env python3
"""Empaqueta las trayectorias de Harbor para adjuntarlas al release de GitHub. (10-nov-2026)

POR QUÉ EXISTE
--------------
Las trayectorias (`jobs/`) no se versionan en git: pesan cientos de MB y el repo es público.
Hasta la v6.1 tampoco se publicaban en ningún lado, así que un resultado agéntico raro no se
podía auditar: solo creerle. Cristian decidió (DECISIONES, 10-nov-2026) que vayan como un
`.tar.zst` adjunto al release de cada versión, y en el repo quede un manifiesto con el sha256 del
paquete y la lista de archivos.

LA CLAVE, Y POR QUÉ EL ESCANEO NO ES OPCIONAL
---------------------------------------------
El agente lleva la clave de OpenRouter en el entorno del contenedor. En tareas como
`verificar-entorno` algunos modelos corren `env`, y la clave queda escrita en la trayectoria:
12 archivos de la v6.1 la tienen. Por eso:

1. se copia a un directorio de trabajo y ahí se reemplaza toda clave por `[REDACTADO]`;
2. **antes de empaquetar**, se escanea esa copia buscando CUALQUIER clave (`sk-or-…` y las otras
   formas conocidas), no solo la vieja;
3. si el escaneo encuentra una, el script sale con error **sin crear el paquete ni el
   manifiesto**: no queda nada que subir.

La subida al release la hace una persona con OK (es publicar), nunca este script.

Uso:
    python benchmarks/empaquetar_trayectorias.py --version v6.1.0 --prefijos v61r v61n
    python benchmarks/empaquetar_trayectorias.py --version historico --historico v61r v61n
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JOBS = ROOT / "jobs"
SALIDA = ROOT / "dist" / "trayectorias"          # gitignored: el paquete va al release
MANIFIESTOS = ROOT / "benchmarks" / "results" / "trayectorias"

# Cualquier clave, no solo la de hoy: la vieja, la nueva y las que vengan.
PATRON_CLAVE = re.compile(rb"sk-(?:or|ant|proj)-[A-Za-z0-9_-]{16,}")
REDACTADO = b"[REDACTADO]"


def escanear(raiz: Path) -> list[str]:
    """Rutas (relativas a `raiz`) que todavía contienen una clave."""
    return sorted(str(p.relative_to(raiz)) for p in raiz.rglob("*")
                  if p.is_file() and PATRON_CLAVE.search(p.read_bytes()))


def redactar(raiz: Path) -> int:
    """Reemplaza toda clave en la copia; devuelve cuántos archivos tocó."""
    n = 0
    for p in raiz.rglob("*"):
        if p.is_file():
            b = p.read_bytes()
            nb = PATRON_CLAVE.sub(REDACTADO, b)
            if nb != b:
                p.write_bytes(nb)
                n += 1
    return n


def elegir_jobs(prefijos: list[str], historico: list[str] | None) -> list[Path]:
    """Con `prefijos`: los jobs que empiezan por ellos. Con `historico`: todos MENOS esos."""
    dirs = sorted(p for p in JOBS.iterdir() if p.is_dir())
    if historico is not None:
        return [p for p in dirs if not any(p.name.startswith(f"{x}__") for x in historico)]
    return [p for p in dirs if any(p.name.startswith(f"{x}__") for x in prefijos)]


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def empaquetar(version: str, jobs: list[Path], trabajo: Path, salida: Path,
               manifiestos: Path, redactar_antes: bool = True) -> int:
    """0 si quedó el paquete y su manifiesto; 1 si el escaneo encontró una clave (no deja nada)."""
    staging = trabajo / f"trayectorias-{version}"
    for j in jobs:
        shutil.copytree(j, staging / j.name, symlinks=False)
    n = redactar(staging) if redactar_antes else 0
    quedan = escanear(staging)
    if quedan:
        print(f"❌ {len(quedan)} archivo(s) con una clave después de redactar; no se empaqueta nada:")
        for q in quedan[:20]:
            print(f"   {q}")
        return 1
    salida.mkdir(parents=True, exist_ok=True)
    tar = salida / f"trayectorias-{version}.tar.zst"
    subprocess.run(["tar", "--zstd", "-cf", str(tar), "-C", str(trabajo), staging.name]
                   if _tar_tiene_zstd() else
                   ["sh", "-c", f'tar -cf - -C "{trabajo}" "{staging.name}" | zstd -19 -T0 -q -o "{tar}"'],
                   check=True)
    archivos = [{"ruta": str(p.relative_to(staging)), "bytes": p.stat().st_size, "sha256": _sha(p)}
                for p in sorted(staging.rglob("*")) if p.is_file()]
    manifiesto = {
        "version": version,
        "paquete": tar.name,
        "sha256": _sha(tar),
        "bytes": tar.stat().st_size,
        "jobs": len(jobs),
        "archivos_redactados": n,
        "escaneo": f"0 claves ({PATRON_CLAVE.pattern.decode()})",
        "archivos": archivos,
    }
    manifiestos.mkdir(parents=True, exist_ok=True)
    (manifiestos / f"{version}.json").write_text(
        json.dumps(manifiesto, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ {tar.name}: {len(jobs)} jobs, {len(archivos)} archivos, {n} redactados, "
          f"{tar.stat().st_size / 1e6:.1f} MB · manifiesto en {manifiestos.name}/{version}.json")
    return 0


def _tar_tiene_zstd() -> bool:
    r = subprocess.run(["tar", "--help"], capture_output=True, text=True)
    return "--zstd" in (r.stdout + r.stderr)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--prefijos", nargs="+")
    g.add_argument("--historico", nargs="+", metavar="EXCLUIR")
    a = ap.parse_args()
    jobs = elegir_jobs(a.prefijos or [], a.historico)
    if not jobs:
        print("❌ ningún job coincide")
        return 1
    with tempfile.TemporaryDirectory() as t:
        return empaquetar(a.version, jobs, Path(t), SALIDA, MANIFIESTOS)


if __name__ == "__main__":
    sys.exit(main())
