#!/usr/bin/env python3
"""
Pipeline maestro de regeneración de artefactos del benchmark.

Orden:
1. export_for_pages.py       -> docs/data/models.json (single source of truth)
2. generate_modelos_md_table.py -i  -> MODELOS.md
3. generate_tests_md.py -o TESTS.md -> TESTS.md
4. generate_per_model_md.py  -> benchmarks/results/per-model/
5. generate_rankings.py      -> docs/mejor-llm-*/
6. generate_comparison.py    -> docs/*-vs-*/
7. generate_sitemap.py       -> docs/sitemap.xml
8. generate_llms_txt.py      -> docs/llms.txt
9. generate_og_image.py      -> docs/og-benchmark.png
10. sync_doc_counts.py       -> README.md y otros MDs/HTMLs con marcadores

Uso:
    python benchmarks/regenerate_all.py              # pipeline completo
    python benchmarks/regenerate_all.py --dry-run    # muestra, no escribe
    python benchmarks/regenerate_all.py --skip-og-image --skip-per-model
    python benchmarks/regenerate_all.py --check      # solo valida counts

Recomendación: correr --dry-run antes de un release para revisar qué tocará.
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PYTHON = ROOT / ".venv" / "bin" / "python"
if not PYTHON.exists():
    PYTHON = Path(sys.executable)


def run_script(name: str, args: list[str], dry_run: bool = False) -> None:
    """Ejecuta un script del benchmark. En dry-run solo imprime el comando."""
    cmd = [str(PYTHON), str(ROOT / "benchmarks" / name)] + args
    cmd_str = " ".join(cmd)
    print(f"\n▶ {cmd_str}")
    if dry_run:
        print("  [dry-run] se ejecutaría")
        return
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=False)
    if result.returncode != 0:
        print(f"\n❌ Error en {name} (exit {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)


def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline maestro de regeneración de artefactos")
    ap.add_argument("--dry-run", action="store_true", help="Muestra comandos sin ejecutar")
    ap.add_argument("--check", action="store_true", help="Solo valida counts con sync_doc_counts.py --dry-run")
    ap.add_argument("--skip-og-image", action="store_true", help="No regenera docs/og-benchmark.png")
    ap.add_argument("--skip-per-model", action="store_true", help="No regenera benchmarks/results/per-model/")
    ap.add_argument("--skip-comparisons", action="store_true", help="No regenera páginas de comparación/ranking")
    ap.add_argument("--skip-sitemap", action="store_true", help="No regenera sitemap ni llms.txt")
    ap.add_argument("--skip-sync", action="store_true", help="No sincroniza counts en MDs/HTMLs")
    args = ap.parse_args()

    if args.check:
        run_script("sync_doc_counts.py", ["--dry-run"], dry_run=False)
        return 0

    # 1. Single source of truth para la calculadora y todo lo demás
    run_script("export_for_pages.py", [], dry_run=args.dry_run)

    # 2. Tabla de modelos en MODELOS.md
    run_script("generate_modelos_md_table.py", ["-i"], dry_run=args.dry_run)

    # 2b. Top-10 del README. Se escribia a mano y driftaba en silencio: el
    # score es z-score contra la poblacion, asi que agregar un modelo cambia
    # TODOS los scores y deja obsoleta cualquier tabla estatica.
    run_script("generate_readme_ranking.py", ["-i"], dry_run=args.dry_run)

    # 3. TESTS.md
    run_script("generate_tests_md.py", ["-o", "TESTS.md"], dry_run=args.dry_run)

    # 4. Páginas por modelo
    if not args.skip_per_model:
        run_script("generate_per_model_md.py", [], dry_run=args.dry_run)

    # 5. pSEO: rankings y comparaciones
    if not args.skip_comparisons:
        run_script("generate_rankings.py", [], dry_run=args.dry_run)
        run_script("generate_comparison.py", [], dry_run=args.dry_run)
        run_script("generate_manual_landings.py", [], dry_run=args.dry_run)

    # 6. Sitemap y llms.txt
    if not args.skip_sitemap:
        run_script("generate_sitemap.py", [], dry_run=args.dry_run)
        run_script("generate_llms_txt.py", [], dry_run=args.dry_run)

    # 7. OG image (PIL requerido)
    if not args.skip_og_image:
        run_script("generate_og_image.py", [], dry_run=args.dry_run)

    # 8. Sincronización de counts con marcadores
    if not args.skip_sync:
        run_script("sync_doc_counts.py", [], dry_run=args.dry_run)

    print("\n✅ Pipeline de regeneración completado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
