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
2. **antes de empaquetar**, se escanea esa copia dos veces: con el patrón propio (`sk-or-`,
   `sk-ant-`, `sk-proj-`, `AIza`, `gsk_`, `hf_`, `ghp_`, `AKIA`, `Bearer …`) y con gitleaks y
   sus reglas por defecto, que caza las formas que no conocemos;
3. si cualquiera de los dos encuentra algo, el script sale con error **sin crear el paquete ni el
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

# Cualquier clave, no solo la de hoy: la vieja, la nueva y las que vengan. 11-nov-2026
# (Cristian): además de OpenRouter/Anthropic/OpenAI, Google (AIza), Groq (gsk_), Hugging Face
# (hf_), GitHub (ghp_), AWS (AKIA) y cualquier token detrás de «Bearer ».
PATRON_CLAVE = re.compile(
    rb"sk-(?:or|ant|proj)-[A-Za-z0-9_-]{16,}"
    rb"|AIza[0-9A-Za-z_-]{35}"
    rb"|gsk_[A-Za-z0-9]{20,}"
    rb"|hf_[A-Za-z0-9]{20,}"
    rb"|ghp_[A-Za-z0-9]{36}"
    rb"|AKIA[0-9A-Z]{16}"
    rb"|Bearer\s+[A-Za-z0-9._~+/=-]{16,}")
REDACTADO = b"[REDACTADO]"
GITLEAKS_VERSION = "8.30.1"   # la misma que check_gitleaks y el Action


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


def gitleaks(raiz: Path, exe: str | None = None) -> tuple[list[dict], list[str]]:
    """(hallazgos, errores) de gitleaks (reglas por defecto, sin allowlist del repo) en `raiz`.

    Es la segunda llave: el patrón propio caza las formas que conocemos; gitleaks, las que no.
    Cada hallazgo es su HUELLA: ruta relativa, regla y sha256 del valor. El valor no sale de
    esta función ni se guarda en ningún lado. Sin gitleaks instalado devuelve un error: un
    escaneo que se omite en silencio es el verde vacío que esta regla existe para evitar."""
    exe = exe or shutil.which("gitleaks")
    if not exe or not Path(exe).is_file():
        return [], ["gitleaks no está instalado: sin él no se empaqueta nada"]
    with tempfile.TemporaryDirectory() as t:
        rep = Path(t) / "rep.json"
        r = subprocess.run([exe, "dir", str(raiz), "--no-banner",
                            "--report-format", "json", "--report-path", str(rep),
                            "--exit-code", "3"], capture_output=True, text=True)
        if r.returncode not in (0, 3):
            return [], [f"gitleaks falló (exit {r.returncode}): {r.stderr.strip()[:200]}"]
        hall = json.loads(rep.read_text() or "[]") if rep.exists() else []
        if r.returncode == 3 and not hall:
            return [], ["gitleaks reportó hallazgos y el reporte vino vacío"]
    raiz_s = str(raiz.resolve()) + "/"
    out = [{"ruta": str(Path(h.get("File", "?")).resolve()).replace(raiz_s, ""),
            "regla": h.get("RuleID"),
            "sha": hashlib.sha256((h.get("Secret") or "").encode()).hexdigest(),
            "_match": h.get("Match") or "", "_secreto": h.get("Secret") or ""}
           for h in hall]
    return sorted(out, key=lambda h: (h["ruta"], h["regla"], h["sha"])), []


def huella(h: dict) -> tuple[str, str, str]:
    return (h["ruta"], h["regla"], h["sha"])


def cargar_revisados(version: str, manifiestos: Path = MANIFIESTOS) -> set:
    """Las huellas que una persona revisó y declaró no credenciales (DECISIONES, 10-nov)."""
    f = manifiestos / f"revisados-{version}.json"
    if not f.exists():
        return set()
    d = json.loads(f.read_text(encoding="utf-8"))
    return {(h["ruta"], h["regla"], h["sha"]) for h in d.get("hallazgos", [])}


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
               manifiestos: Path, redactar_antes: bool = True, gitleaks_exe: str | None = None,
               revisados: set | None = None) -> int:
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
    hall, errores = gitleaks(staging, gitleaks_exe)
    revisados = cargar_revisados(version, manifiestos) if revisados is None else revisados
    # Una excepción vale para ESE hallazgo (ruta, regla, valor): una clave nueva, o la misma
    # en otro archivo, no está en la lista y bloquea.
    pendientes = [h for h in hall if huella(h) not in revisados]
    if errores or pendientes:
        for e in errores:
            print(f"❌ {e}")
        if pendientes:
            print(f"❌ gitleaks encontró {len(pendientes)} cosa(s) con forma de credencial sin "
                  f"revisar en la copia redactada; no se empaqueta nada:")
            for h in pendientes[:20]:
                print(f"   {h['ruta']} · {h['regla']}")
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
        "escaneo": {"patron": PATRON_CLAVE.pattern.decode(), "claves": 0,
                    "gitleaks": f"{GITLEAKS_VERSION}, reglas por defecto, {len(hall)} hallazgo(s), "
                                f"todos revisados (revisados-{version}.json)"},
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
    ap.add_argument("--revisar", action="store_true",
                    help="escribe revisados-<versión>.json con las huellas de hoy y su clase; "
                         "falla si alguna no se puede clasificar. Lo corre una persona y lo lee.")
    a = ap.parse_args()
    jobs = elegir_jobs(a.prefijos or [], a.historico)
    if not jobs:
        print("❌ ningún job coincide")
        return 1
    with tempfile.TemporaryDirectory() as t:
        if a.revisar:
            return revisar(a.version, jobs, Path(t), MANIFIESTOS)
        return empaquetar(a.version, jobs, Path(t), SALIDA, MANIFIESTOS)


# Clases de lo que gitleaks confunde con credenciales en las trayectorias (revisión del
# 10-nov-2026). Cada una se decide por la forma y el contexto del hallazgo, nunca por el valor
# de una clave real: un valor que no encaja queda SIN CLASIFICAR y bloquea.
FIXTURE = ROOT / "tareas-agente" / "harbor-incidente" / "environment" / "secretos"
# Huellas públicas de las claves con que se firman las versiones de Python (python.org/downloads,
# «OpenPGP Public Keys»): las imágenes oficiales de Docker las exportan como GPG_KEY. Se fijan
# para que un hex de 40 cualquiera detrás de `GPG_KEY=` no pase como esta clase.
GPG_PYTHON = {
    "7169605F62C751356D054A26A821E680E5FA6305",   # Thomas Wouters (3.12, 3.13)
    "A035C8C19219BA821ECEA86B64E628F8D684696D",   # Pablo Galindo Salgado (3.10, 3.11)
    "E3FF2839C048B25C084DEBE9B26995E310250568",   # Łukasz Langa (3.8, 3.9)
}


def clasificar(h: dict) -> str | None:
    v, m = h["_secreto"], h["_match"]
    ficticios = [x.split("=", 1)[1].strip().strip('"') for f in FIXTURE.glob("*.env")
                 for x in f.read_text(encoding="utf-8").splitlines() if "=" in x]
    if v in ficticios:
        return "credencial ficticia del fixture de harbor-incidente"
    if any(len(f) >= 8 and (v.startswith(f[:8]) or f.startswith(v[:8])) for f in ficticios):
        return "copia modificada por el modelo de una credencial ficticia del fixture"
    if m.split(v)[0].endswith("GPG_KEY=") and v in GPG_PYTHON:
        return "huella pública de la clave GPG de la imagen de Python"
    if re.fullmatch(r"[0-9a-f]{40}", v):
        return "hash sha1 (40 hex) en la salida de un comando"
    if re.fullmatch(r"[0-9a-f]{32}", v):
        return "hash md5 (32 hex) en la salida de un comando"
    if "KeyError" in m and re.fullmatch(r"[A-Z][A-Z0-9_-]+", v) and "/verifier/" in "/" + h["ruta"]:
        return "código de producto (SKU) inventado por el modelo, en un KeyError del verificador"
    if v.startswith(".") and len(v) > 40 and re.fullmatch(r"[A-Za-z0-9._=-]+", v) \
            and "trajectory.json" in h["ruta"]:
        return "fragmento de razonamiento cifrado de OpenAI (reasoning_details)"
    return None


def revisar(version: str, jobs: list[Path], trabajo: Path, manifiestos: Path) -> int:
    staging = trabajo / f"trayectorias-{version}"
    for j in jobs:
        shutil.copytree(j, staging / j.name, symlinks=False)
    redactar(staging)
    hall, errores = gitleaks(staging)
    if errores:
        print("\n".join(f"❌ {e}" for e in errores))
        return 1
    sin = [h for h in hall if clasificar(h) is None]
    if sin:
        print(f"❌ {len(sin)} hallazgo(s) sin clasificar: revisarlos a mano, no se escribe nada")
        for h in sin[:20]:
            print(f"   {h['ruta']} · {h['regla']}")
        return 1
    from collections import Counter
    clases = Counter(clasificar(h) for h in hall)
    manifiestos.mkdir(parents=True, exist_ok=True)
    (manifiestos / f"revisados-{version}.json").write_text(json.dumps({
        "version": version, "revisado": "2026-11-10",
        "nota": "huellas (ruta, regla, sha256 del valor) de hallazgos de gitleaks revisados: "
                "ninguno es una credencial. El valor no se guarda. DECISIONES, 10-nov-2026.",
        "clases": dict(clases),
        "hallazgos": [{"ruta": h["ruta"], "regla": h["regla"], "sha": h["sha"],
                       "clase": clasificar(h)} for h in hall],
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for c, n in clases.most_common():
        print(f"  {n:>5}  {c}")
    print(f"✅ revisados-{version}.json: {len(hall)} huellas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
