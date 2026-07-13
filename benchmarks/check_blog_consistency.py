#!/usr/bin/env python3
"""
Verifica que los posts del BLOG no publiquen cifras del benchmark ya caducadas.

POR QUE EXISTE
--------------
`check_consistency.py` protege los docs del repo del benchmark. Pero las cifras se
publican de verdad en el BLOG, que es otro repo — y ahí no había guardrail.

Consecuencia real (jul-2026): ocho posts con claims muertos en producción. El
`seoTitle` de uno decía "Devstral Small es el #1 de mi benchmark" cuando era el #9,
y otro coronaba a "MiMo V2.5 #1 global" cuando estaba #61. Eso es lo que Google le
mostraba a la gente, durante meses.

Y el mecanismo es el de siempre: el score es un z-score contra toda la población, así
que **medir un modelo nuevo recalcula el score de todos**. Ninguna cifra escrita a
mano sobrevive al siguiente lote. No es descuido: es matemática.

QUE VERIFICA
------------
Para cada post del blog que cite el benchmark:
  · posiciones  ("es el #1", "queda #62 de 89")
  · scores      ("8.28 sobre 10", "score 6.99")
  · conteos     ("89 modelos", "145 modelos")
Los contrasta contra docs/data/models.json y falla si algo ya no coincide.

Revisa el FRONTMATTER (title, seoTitle, description) con prioridad, porque es lo que
Google muestra — y es justo donde se coló el bug: se corrigió el `description` y se
dejó vivo el `seoTitle`, que en este blog PISA al title.

Uso:
    python benchmarks/check_blog_consistency.py
    python benchmarks/check_blog_consistency.py --blog /ruta/al/blog
"""
import argparse
import json
import re
import sys
from pathlib import Path

BENCH = Path(__file__).parent.parent
MODELS_JSON = BENCH / "docs" / "data" / "models.json"
DEFAULT_BLOG = Path.home() / "Playground" / "sitios" / "cristiantala-blog"

# Campos del frontmatter que Google muestra. El seoTitle PISA al title en este blog
# ([...slug].astro) — corregir solo el title o el description no sirve de nada.
SERP_FIELDS = ("title", "seoTitle", "description")

TOLERANCE = 0.06  # los posts redondean (8.1 vs 8.14): solo marcamos drift real


def load_bench():
    d = json.loads(MODELS_JSON.read_text())
    ranked = sorted(
        [m for m in d["models"] if m.get("ranked") and m.get("score_global") is not None],
        key=lambda m: -m["score_global"],
    )
    pos = {m["name"]: i for i, m in enumerate(ranked, 1)}
    return d, ranked, pos


def find_model(text_low, ranked):
    """Modelos nombrados en un texto (match más largo primero)."""
    hits = []
    for m in sorted(ranked, key=lambda x: -len(x["name"])):
        base = m["name"].split("(")[0].strip()
        if len(base) >= 5 and base.lower() in text_low:
            hits.append((base, m))
    return hits


def is_snapshot(raw: str) -> bool:
    """Post fechado que reporta el ranking DE SU FECHA a propósito.

    Igual que el CHANGELOG: un post de abril que dice "MiMo V2.5 es #1" era CIERTO
    en abril. Reescribirlo sería falsificar la historia — el bug sería ese, no el fix.
    Lo que sí debe estar al día es el frontmatter, porque es lo que Google muestra HOY.
    """
    low = raw.lower()
    return any(x in low for x in (
        "es una **foto del ranking en su fecha**",
        "foto del ranking en su fecha",
        "snapshot de",
        "no reescribo la historia",
    ))


# Frases donde un número seguido de "modelos" NO es el conteo del catálogo.
# "14 modelos que empatan" es un hallazgo, no la cobertura del benchmark.
_NOT_A_COUNT = ("empatan", "empatados", "que empat", "de esos", "del grupo", "en la cima")


def check_post(path, d, ranked, pos):
    findings = []
    raw = path.read_text()
    total = d["total_models"]
    n_ranked = d["ranked_count"]

    # separar frontmatter (lo que ve Google) del cuerpo
    parts = raw.split("---", 2)
    fm = parts[1] if len(parts) > 2 else ""
    body = parts[2] if len(parts) > 2 else raw

    # El cuerpo de un snapshot es historia legítima: solo se audita el frontmatter.
    zones = [("SERP (frontmatter)", fm)]
    if not is_snapshot(raw):
        zones.append(("cuerpo", body))

    for zone, text in zones:
        low = text.lower()
        if "benchmark" not in low:
            continue

        # 1) conteos de modelos
        for mm in re.finditer(r"\b(\d{2,3}) (?:modelos|llms)\b", low):
            n = mm.group(1)
            ctx = low[max(0, mm.start() - 60): mm.end() + 60]
            if any(w in ctx for w in _NOT_A_COUNT):
                continue  # "14 modelos que empatan" no es la cobertura
            if int(n) not in (total, n_ranked, d.get("tested_count", 0)):
                findings.append(
                    f"{zone}: dice «{n} modelos» — hoy son {n_ranked} rankeados "
                    f"({total} catalogados)"
                )

        # 2) posiciones y scores atribuidos a un modelo
        for base, m in find_model(low, ranked):
            real_pos = pos[m["name"]]
            for line in text.splitlines():
                ll = line.lower()
                if base.lower() not in ll:
                    continue
                clean = ll.replace(base.lower(), " ")  # el "4.5" de "Grok 4.5" no es un score

                for p in re.findall(r"#\s?(\d{1,3})\b", clean):
                    if abs(int(p) - real_pos) > 2:   # ±2 por si el post se escribió hace días
                        findings.append(
                            f"{zone}: «{base}» aparece como #{p} — hoy es #{real_pos}"
                        )
                for s in re.findall(r"score\s*(?:global\s*)?[:=]?\s*\**\s*(\d{1,2}\.\d{1,2})", clean):
                    ok = [m["score_global"], m.get("quality_avg")]
                    if not any(v is not None and abs(float(s) - v) <= TOLERANCE for v in ok):
                        findings.append(
                            f"{zone}: «{base}» con score {s} — hoy score_global="
                            f"{m['score_global']}, quality={m.get('quality_avg')}"
                        )
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--blog", default=str(DEFAULT_BLOG))
    args = ap.parse_args()

    blog = Path(args.blog) / "src" / "content" / "blog"
    if not blog.exists():
        sys.exit(f"No encuentro los posts en {blog}")
    if not MODELS_JSON.exists():
        sys.exit("Falta docs/data/models.json — corré export_for_pages.py primero")

    d, ranked, pos = load_bench()
    print(f"Verificando posts del blog contra models.json "
          f"({d['ranked_count']} modelos rankeados, generado {d['generated_at']})\n")

    total = 0
    for p in sorted(blog.glob("*.md")):
        f = check_post(p, d, ranked, pos)
        if f:
            print(f"  ❌ {p.name}")
            for x in dict.fromkeys(f):
                print(f"       · {x}")
            total += len(f)

    if not total:
        print("  ✅ Ningún post publica cifras caducadas del benchmark.")
        return 0

    print(f"\n  {total} cifra(s) desactualizada(s).")
    print("  Ojo: el `seoTitle` PISA al `title` — es lo que Google muestra.")
    print("  Y recordá que el score es z-score: cambia solo con cada modelo nuevo.")
    print("  Preferí lenguaje durable ('de los más baratos que empatan arriba') a una")
    print("  posición exacta, que vuelve a caducar en el próximo lote.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
