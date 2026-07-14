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


def run_script(name: str, args: list[str], dry_run: bool = False,
               allow_fail: bool = False) -> int:
    """Ejecuta un script del benchmark. En dry-run solo imprime el comando.

    `allow_fail=True` devuelve el exit code en vez de abortar: lo usa el chequeo de
    consistencia final, que necesita reportar el drift completo antes de que el pipeline
    decida qué hacer.
    """
    cmd = [str(PYTHON), str(ROOT / "benchmarks" / name)] + args
    cmd_str = " ".join(cmd)
    print(f"\n▶ {cmd_str}")
    if dry_run:
        print("  [dry-run] se ejecutaría")
        return 0
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=False)
    if result.returncode != 0 and not allow_fail:
        print(f"\n❌ Error en {name} (exit {result.returncode})", file=sys.stderr)
        sys.exit(result.returncode)
    return result.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Pipeline maestro de regeneración de artefactos")
    ap.add_argument("--dry-run", action="store_true", help="Muestra comandos sin ejecutar")
    ap.add_argument("--check", action="store_true", help="Solo valida counts con sync_doc_counts.py --dry-run")
    ap.add_argument("--skip-og-image", action="store_true", help="No regenera docs/og-benchmark.png")
    ap.add_argument("--skip-per-model", action="store_true", help="No regenera benchmarks/results/per-model/")
    ap.add_argument("--skip-comparisons", action="store_true", help="No regenera páginas de comparación/ranking")
    ap.add_argument("--skip-sitemap", action="store_true", help="No regenera sitemap ni llms.txt")
    ap.add_argument("--skip-sync", action="store_true", help="No sincroniza counts en MDs/HTMLs")
    ap.add_argument("--skip-endpoints", action="store_true",
                    help="No chequea si los modelos del ranking siguen vivos (no recomendado)")
    args = ap.parse_args()

    if args.check:
        run_script("sync_doc_counts.py", ["--dry-run"], dry_run=False)
        return 0

    # 0. ¿Siguen vivos los modelos que recomendamos?
    #
    # Devstral Small estuvo **#5 del ranking** meses después de que Mistral apagara su
    # endpoint, y llegó a aparecer en 11 páginas del sitio — incluida /mejor-llm-barato/
    # y las cuatro de "alternativas a X". Todas recomendando un modelo que devuelve 404.
    #
    # Nos enteramos por accidente, cuando un lote se estrelló contra él. Este chequeo
    # cuesta centavos (un ping de 16 tokens por modelo) y lo detecta antes de publicar.
    # Va PRIMERO: si un modelo murió, todo lo que se genere después lo va a recomendar.
    #
    # No aborta el pipeline — reporta. Retirarlo es una decisión (check_endpoints --fix).
    if not args.dry_run and not args.skip_endpoints:
        rc = run_script("check_endpoints.py", ["--ranked"], dry_run=False, allow_fail=True)
        if rc != 0:
            print("\n⚠️  Hay modelos MUERTOS en el ranking (arriba).")
            print("   Retiralos antes de publicar:  python benchmarks/check_endpoints.py --ranked --fix")
            print("   Sus datos NO se pierden: quedan como estadística histórica, fuera de las")
            print("   recomendaciones y de la calculadora.\n")

    # 1. Single source of truth para la calculadora y todo lo demás
    run_script("export_for_pages.py", [], dry_run=args.dry_run)

    # 2. Tabla de modelos en MODELOS.md
    run_script("generate_modelos_md_table.py", ["-i"], dry_run=args.dry_run)

    # 2b. Top-10 del README. Se escribia a mano y driftaba en silencio: el
    # score es z-score contra la poblacion, asi que agregar un modelo cambia
    # TODOS los scores y deja obsoleta cualquier tabla estatica.
    run_script("generate_readme_ranking.py", ["-i"], dry_run=args.dry_run)

    # 2c. RECOMENDACIONES.md. Estaba FUERA del pipeline y se pudrio: 81 dias
    # stale, recomendando modelos hoy en el puesto #86-#97. Era el unico doc con
    # forma de DECISION y era el unico que no se regeneraba. Ya no.
    run_script("generate_recomendaciones.py", ["-i"], dry_run=args.dry_run)

    # 3. TESTS.md
    run_script("generate_tests_md.py", ["-o", "TESTS.md"], dry_run=args.dry_run)

    # 4. Páginas por modelo
    if not args.skip_per_model:
        run_script("generate_per_model_md.py", [], dry_run=args.dry_run)

    # 5. pSEO: rankings y comparaciones
    if not args.skip_comparisons:
        run_script("generate_rankings.py", [], dry_run=args.dry_run)
        run_script("generate_comparison.py", [], dry_run=args.dry_run)
        # Paginas "que tier de <familia> elegir": todas las variantes juntas.
        # Las comparaciones A-vs-B no responden "cual de los TRES tomo".
        run_script("generate_variants.py", [], dry_run=args.dry_run)
        run_script("generate_manual_landings.py", [], dry_run=args.dry_run)
        # Bloque "Explora" del home -> paginas pSEO. Sin esto las 35 comparaciones
        # y las 6 paginas de familia quedan huerfanas: cero enlaces internos desde
        # la pagina mas autoritativa del sitio. /claude-vs-chatgpt/ vale 2.480
        # busquedas/mes y no se podia llegar a ella.
        # "El mismo modelo rinde distinto segun quien lo sirva". Sale de las filas
        # `provider_variant` (el mismo modelo medido en dos infras). Ollama Cloud sirve
        # un Qwen 3.5 397B que rinde 2.74 puntos menos que el de NIM: quien elige el
        # modelo eligio la mitad de la decision, y nadie le cuenta la otra mitad.
        run_script("generate_providers_page.py", [], dry_run=args.dry_run)
        run_script("generate_home_explore.py", [], dry_run=args.dry_run)

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

    # 9. GUARDRAIL — el pipeline no puede decir "listo" si dejó drift.
    #
    # El score es un z-score contra la población: medir UN modelo nuevo recalcula el
    # score de TODOS. Cualquier cifra escrita a mano en un doc caduca sola, sin que nadie
    # toque el doc. Ya pasó: el README decía que Grok 4.5 sacaba 6.99 mientras el sitio
    # decía 5.84, y RECOMENDACIONES.md recomendaba modelos que estaban en el puesto #86.
    #
    # Regenerar sin verificar es exactamente cómo se llega ahí. Si esto falla, el pipeline
    # falla — no imprime "✅ completado" sobre un sitio inconsistente.
    if not args.dry_run:
        print()
        rc = run_script("check_consistency.py", [], dry_run=False, allow_fail=True)
        if rc != 0:
            print("\n❌ El pipeline regeneró, pero hay docs vivos citando cifras obsoletas.")
            print("   Arreglalos antes de publicar: los números de arriba NO coinciden con models.json.")
            return 1

    print("\n✅ Pipeline de regeneración completado — y sin drift.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
