#!/usr/bin/env python3
"""`docs/` es la copia de `sitio/dist`, y nada más la escribe. (12-nov-2026, motor-sitio 2.6)

POR QUÉ EXISTE
--------------
GitHub Pages sirve `docs/` desde `main`. Desde el corte, lo publicado es lo que compila Astro
(`sitio/dist`), que ya lleva las páginas de Python copiadas desde `sitio/legado/`. Al preparar
el corte se vio que la copia `dist` → `docs/` que describía `design.md` no existía, y que
`regenerate_all` y el Action seguían escribiendo en `docs/` con los generadores de Python: la
primera regeneración después del corte habría pisado las páginas de Astro con las de Python, sin
que nada fallara. Cristian (12-nov): «Desde el corte, docs/ solo se escribe con esa copia».

Por eso los generadores escriben en `sitio/legado/` (su carpeta intermedia), el build copia de
ahí a `dist`, y este script copia `dist` a `docs/` en espejo: lo que `dist` no tiene, `docs/` no
lo tiene.

  P1  `docs/` es igual a `dist`, archivo por archivo y byte por byte. Si difiere, algo escribió
      en `docs/` por fuera de la copia, o se compiló y no se copió.
  P2  ningún script del repo construye una ruta a `docs/`, salvo los que la lista `PERMITIDOS`
      nombra con su motivo. Un generador que vuelve a escribir ahí cae acá antes de correr.
  P3  si lo publicado tiene una carpeta que empieza con `_` (Astro deja su CSS y su JS en
      `_astro/`), lleva `.nojekyll`. Pages construye con Jekyll y Jekyll descarta esas carpetas:
      sin el archivo, las páginas de Astro salen sin estilos.

Uso:
    python benchmarks/publicar_dist.py            # copia sitio/dist → docs/ (espejo)
    python benchmarks/publicar_dist.py --check    # P1-P3; compila antes si dist está viejo
    python benchmarks/publicar_dist.py --check --dist <d> --docs <d> --sin-compilar
"""
from __future__ import annotations

import argparse
import filecmp
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

DIST = ROOT / "sitio" / "dist"
DOCS = ROOT / "docs"
IGNORAR = {".DS_Store"}

# Dónde se busca código que escriba en docs/ (P2).
CODIGO = ["benchmarks/*.py", "benchmarks/*.mjs", "cheatsheet/*.py", "sitio/*.mjs", "sitio/pruebas/*.mjs"]
RUTA_A_DOCS = re.compile(r"""/\s*["']docs["']|join\([^)]*["']docs["']|["']docs/""")
# Los únicos que nombran docs/, cada uno con su motivo.
PERMITIDOS = {
    "benchmarks/publicar_dist.py": "es la copia",
    "benchmarks/release_diff.py": "lee del historial de git lo que cada release publicó en docs/",
    "benchmarks/fechar_dist.py": "siembra las fechas contra `main:docs/`, lo publicado",
    "benchmarks/check_changelog.py": "lista lo generado, y docs/ lo es",
    "benchmarks/test_guardrails.py": "el sabotaje de P2 escribe una ruta a docs/ en un generador",
}


def archivos(base: Path) -> dict[str, Path]:
    return {str(f.relative_to(base)): f for f in sorted(base.rglob("*"))
            if f.is_file() and f.name not in IGNORAR}


def comparar(dist: Path, docs: Path) -> list[str]:
    """P1: diferencias entre dist y docs/."""
    a, b = archivos(dist), archivos(docs) if docs.is_dir() else {}
    fallos = [f"P1 · docs/{r} no está en dist: algo lo escribió por fuera de la copia" for r in sorted(set(b) - set(a))]
    fallos += [f"P1 · docs/{r} falta: dist lo tiene y no se copió" for r in sorted(set(a) - set(b))]
    fallos += [f"P1 · docs/{r} difiere de dist" for r in sorted(set(a) & set(b))
               if not filecmp.cmp(a[r], b[r], shallow=False)]
    return fallos


def sin_comentarios(txt: str, sufijo: str) -> str:
    if sufijo == ".py":
        txt = re.sub(r'"""[\s\S]*?"""', "", txt)
        return re.sub(r"(?m)^\s*#.*$", "", txt)
    txt = re.sub(r"/\*[\s\S]*?\*/", "", txt)
    return re.sub(r"(?m)^\s*//.*$", "", txt)


def escritores(raiz: Path = ROOT) -> list[str]:
    """P2: archivos de código que construyen una ruta a docs/ sin estar permitidos."""
    fallos = []
    for pat in CODIGO:
        for f in sorted(raiz.glob(pat)):
            rel = str(f.relative_to(raiz))
            if rel in PERMITIDOS:
                continue
            txt = sin_comentarios(f.read_text(encoding="utf-8", errors="ignore"), f.suffix)
            for m in RUTA_A_DOCS.finditer(txt):
                linea = txt[:m.start()].count("\n") + 1
                fallos.append(f"P2 · {rel}: arma una ruta a docs/ («{m.group(0)}», cerca de la línea {linea}); "
                              "los generadores escriben en sitio/legado/")
                break
    return fallos


def jekyll(base: Path) -> list[str]:
    """P3: con una carpeta `_…` publicada, hace falta `.nojekyll`."""
    raya = sorted({p.parts[0] for p in (f.relative_to(base) for f in base.rglob("*")) if p.parts[0].startswith("_")})
    if raya and not (base / ".nojekyll").is_file():
        return [f"P3 · {base.name}/ publica {', '.join(raya)} y no lleva .nojekyll: Pages (Jekyll) las descarta"]
    return []


def copiar(dist: Path, docs: Path) -> tuple[int, int]:
    """Espejo dist → docs/. (copiados o cambiados, borrados)."""
    a, b = archivos(dist), archivos(docs) if docs.is_dir() else {}
    n = 0
    for r, f in a.items():
        d = docs / r
        if r in b and filecmp.cmp(f, b[r], shallow=False):
            continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, d)
        n += 1
    sobran = sorted(set(b) - set(a))
    for r in sobran:
        (docs / r).unlink()
    for d in sorted((p for p in docs.rglob("*") if p.is_dir()), key=lambda p: -len(p.parts)):
        if not any(d.iterdir()):
            d.rmdir()
    return n, len(sobran)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="no copia: verifica P1-P3")
    ap.add_argument("--dist", type=Path, default=DIST)
    ap.add_argument("--docs", type=Path, default=DOCS)
    ap.add_argument("--sin-compilar", action="store_true", help="con --check, no compila aunque dist esté viejo")
    a = ap.parse_args()

    if a.check and not a.sin_compilar and a.dist == DIST:
        import check_movil
        motivo = check_movil.viejo(a.dist)
        if motivo:
            print(f"  · {motivo}: compilo con `npm run build`", flush=True)
            r = subprocess.run(["npm", "run", "build"], cwd=ROOT / "sitio", capture_output=True, text=True)
            if r.returncode != 0:
                print("  ❌ el build falló:")
                print("\n".join("     " + x for x in (r.stdout + r.stderr).strip().splitlines()[-15:]))
                return 1
    if not (a.dist / "index.html").is_file():
        print(f"  ❌ no hay build en {a.dist}: correr `npm run build` en sitio/")
        return 1

    if not a.check:
        fallos = jekyll(a.dist)
        if fallos:
            print("\n".join(f"  ❌ {x}" for x in fallos))
            return 1
        n, borrados = copiar(a.dist, a.docs)
        print(f"  ✓ docs/ ← dist: {n} archivo(s) copiados o cambiados, {borrados} borrado(s); "
              f"{len(archivos(a.docs))} en total")
        return 0

    fallos = comparar(a.dist, a.docs) + escritores() + jekyll(a.docs if a.docs.is_dir() else a.dist)
    n = len(archivos(a.dist))
    print(f"LO PUBLICADO ES LA COPIA DE DIST — {n} archivos en {a.dist.name}, contra {a.docs}")
    if fallos:
        for x in fallos[:30]:
            print(f"  ❌ {x}")
        if len(fallos) > 30:
            print(f"  … y {len(fallos) - 30} más")
        print(f"\n  ❌ {len(fallos)} problema(s): `docs/` solo se escribe con `python benchmarks/publicar_dist.py`.")
        return 1
    print(f"  ✅ docs/ es dist byte a byte ({n} archivos), ningún script escribe en docs/ y .nojekyll está")
    return 0


if __name__ == "__main__":
    sys.exit(main())
