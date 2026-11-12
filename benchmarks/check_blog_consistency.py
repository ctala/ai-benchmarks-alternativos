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
  · ejecuciones ("más de 80.000 ejecuciones", contra `conteos.ejecuciones`)
  · posts congelados: con `benchmarkEra` Y nota visible se audita solo lo que muestra Google;
    con una sola de las dos marcas, rojo
Los contrasta contra sitio/legado/data/models.json y falla si algo ya no coincide.

Revisa el FRONTMATTER (title, seoTitle, description) con prioridad, porque es lo que
Google muestra — y es justo donde se coló el bug: se corrigió el `description` y se
dejó vivo el `seoTitle`, que en este blog PISA al title.

Uso:
    python benchmarks/check_blog_consistency.py
    python benchmarks/check_blog_consistency.py --blog /ruta/al/blog
"""
import argparse
import os
import json
import re
import sys
from pathlib import Path

BENCH = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import conteos  # noqa: E402
MODELS_JSON = BENCH / "sitio" / "legado" / "data" / "models.json"
# `BENCH_BLOG` apunta los chequeos a otro checkout (un worktree que espera aprobación) sin
# tocar el principal; qa.py avisa cuando está puesta (8-nov-2026).
DEFAULT_BLOG = Path(os.environ.get("BENCH_BLOG")
                    or Path.home() / "Playground" / "sitios" / "cristiantala-blog")

# Campos del frontmatter que Google muestra. El seoTitle PISA al title en este blog
# ([...slug].astro) — corregir solo el title o el description no sirve de nada.
SERP_FIELDS = ("title", "seoTitle", "description")

TOLERANCE = 0.06  # los posts redondean (8.1 vs 8.14): solo marcamos drift real


def load_bench():
    d = json.loads(MODELS_JSON.read_text())
    # Por ÍNDICE DE CALIDAD, que es el titular desde v4.1 — no por el compuesto.
    #
    # El detector seguía ordenando por `score_global` y por eso acusaba al post de citar
    # mal: decía que Claude Opus 4.8 «es #13» cuando en el ranking publicado es **#5**.
    # Los dos números existen y miden cosas distintas; el que se publica es la calidad.
    # Un guardrail que compara contra el criterio viejo convierte un post correcto en un
    # falso positivo, y eso enseña a ignorarlo.
    ranked = sorted(
        [m for m in d["models"] if m.get("ranked") and m.get("score_calidad") is not None],
        key=lambda m: -m["score_calidad"],
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

# Escape POR CIFRA, no por post: se pone en la misma línea del número.
#
# Hay conteos que son correctos y no deben "actualizarse" nunca: cuántos modelos probó un
# post en SU fecha («evalué 18 modelos en marzo»), o un conteo citado de un estudio ajeno
# («16 modelos de todos los labs chantajean», de Anthropic). Antes la única salida era
# declarar el post ENTERO como snapshot, y Cristian lo rechazó el 16-sep-2026: los posts
# viejos se mantienen al día, no se congelan. Congelar el post entero además apagaba el
# chequeo sobre sus otras cifras, que sí caducan.
MARCA_HISTORICA = "<!-- cifra-historica -->"


# ── Post CONGELADO (8-nov-2026) ─────────────────────────────────────────────────────
# Un post cuyo análisis se midió con el examen anterior no recibe cifras v5: mezclaría dos
# exámenes en el mismo texto. Se congela en su fecha, y para que eso no sea una excusa para
# no actualizar, exige DOS marcas: la era en el frontmatter (`benchmarkEra: "v4"`) y una nota
# VISIBLE arriba del cuerpo, antes del primer `## `, con el enlace al ranking vigente. Con una
# sola de las dos, rojo: una era sin nota engaña al lector, y una nota sin era no la lee nadie.
# Lo usan este chequeo y `generate_blog_datos.py` (una sola definición).
ERA_CONGELADA = re.compile(r'^benchmarkEra:\s*["\']?(v\d+)["\']?\s*$', re.M)
NOTA_CONGELADA = re.compile(
    r"Medido con el examen anterior\.\*{0,2}\s+El ranking vigente está "
    r"\[acá\]\((https://benchmarks\.cristiantala\.com/[^)\s]*)\)")


def congelado(raw: str) -> tuple[bool, str | None]:
    """(congelado, error). Congelado solo con era Y nota visible; con una sola, error."""
    parts = raw.split("---", 2)
    fm = parts[1] if len(parts) > 2 else ""
    body = parts[2] if len(parts) > 2 else raw
    era = ERA_CONGELADA.search(fm)
    cabeza = body.split("\n## ", 1)[0]
    # La nota tiene que verse: fuera de un comentario HTML.
    cabeza_visible = re.sub(r"<!--.*?-->", "", cabeza, flags=re.S)
    nota = NOTA_CONGELADA.search(cabeza_visible)
    if era and nota:
        return True, None
    if era:
        return False, (f"declara benchmarkEra: {era.group(1)} pero no tiene la nota visible "
                       "«Medido con el examen anterior. El ranking vigente está [acá](…)» "
                       "arriba del primer ##")
    if NOTA_CONGELADA.search(body):
        return False, ("tiene la nota de post congelado pero no declara `benchmarkEra` en el "
                       "frontmatter" if nota else
                       "tiene la nota de post congelado, pero no arriba del primer ## (o dentro "
                       "de un comentario) y sin `benchmarkEra`")
    return False, None


def _serp(fm: str) -> str:
    """Solo las líneas de title/seoTitle/description: lo que Google muestra."""
    return "\n".join(l for l in fm.splitlines()
                     if any(l.startswith(f + ":") for f in SERP_FIELDS))


# «más de 80.000 ejecuciones», «68.000+ ejecuciones»: el total medido, que sale de
# models.json (vía `conteos.ejecuciones`, la definición única). Vale si está entre el total redondeado hacia abajo
# a la decena de mil y el total: «más de 80.000» con 82.267 sí; «más de 68.000», no.
EJECUCIONES = re.compile(r"(\d{1,3}(?:\.\d{3})+)\s*\+?\s*(?:ejecuciones|runs)\b")


# Una cifra de ejecuciones es del benchmark solo si su frase habla del benchmark o de
# modelos. «8.000 ejecuciones al mes» de 20 workflows de n8n no lo es (falso positivo del
# primer corte, 8-nov-2026).
_EJEC_DEL_BENCH = ("benchmark", "modelo")
_EJEC_AJENA = ("al mes", "por mes", "/mes", "mensual", "workflow", "n8n")


def ejecuciones_del_benchmark(texto: str, ini: int, fin: int) -> bool:
    ctx = texto[max(0, ini - 120): fin + 40].lower()
    return any(w in ctx for w in _EJEC_DEL_BENCH) and not any(w in ctx for w in _EJEC_AJENA)


def ejecuciones_validas(n: int, total: int) -> bool:
    return (total // 10_000) * 10_000 <= n <= total


def check_post(path, d, ranked, pos):
    findings = []
    raw = path.read_text()
    total = d["total_models"]
    n_ranked = d["ranked_count"]

    # separar frontmatter (lo que ve Google) del cuerpo
    parts = raw.split("---", 2)
    fm = parts[1] if len(parts) > 2 else ""
    body = parts[2] if len(parts) > 2 else raw

    frio, error = congelado(raw)
    if error:
        findings.append(f"post congelado a medias: {error}")
    if frio:
        # Congelado: su cuerpo y su FAQ son del examen anterior, a propósito. Lo que Google
        # muestra hoy (title, seoTitle, description) se sigue auditando.
        zones = [("SERP (frontmatter)", _serp(fm))]
    else:
        # El cuerpo de un snapshot es historia legítima: solo se audita el frontmatter.
        zones = [("SERP (frontmatter)", fm)]
        if not is_snapshot(raw):
            zones.append(("cuerpo", body))
    total_runs = conteos.ejecuciones(d)

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
            ini = low.rfind("\n", 0, mm.start()) + 1
            fin = low.find("\n", mm.end())
            if MARCA_HISTORICA in low[ini: fin if fin != -1 else len(low)]:
                continue  # declarada histórica en SU línea (ver MARCA_HISTORICA)
            if int(n) not in (total, n_ranked, d.get("tested_count", 0)):
                findings.append(
                    f"{zone}: dice «{n} modelos» — hoy son {n_ranked} rankeados "
                    f"({total} catalogados)"
                )

        # 1b) total de ejecuciones: también sale de models.json, no de la memoria
        for mm in EJECUCIONES.finditer(low):
            ini = low.rfind("\n", 0, mm.start()) + 1
            fin = low.find("\n", mm.end())
            if MARCA_HISTORICA in low[ini: fin if fin != -1 else len(low)]:
                continue
            if not ejecuciones_del_benchmark(low, mm.start(), mm.end()):
                continue
            n = int(mm.group(1).replace(".", ""))
            if total_runs and not ejecuciones_validas(n, total_runs):
                piso = (total_runs // 10_000) * 10_000
                findings.append(
                    f"{zone}: dice «{mm.group(1)} ejecuciones» — hoy son {total_runs:,} "
                    f"medidas (escribe «más de {piso:,}»)".replace(",", "."))

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
    # 16-sep-2026. El hook de pre-push del blog revisa SÓLO los posts que toca el push.
    # Así el guardrail nace en verde —los 19 posts viejos con cifras caducas son deuda
    # conocida, y un bloqueante que arranca rojo se aprende a ignorar— y frena el drift
    # nuevo desde hoy. Arreglar los viejos es publicar contenido: lo decide Cristian.
    ap.add_argument("--posts", nargs="*", metavar="POST",
                    help="revisar sólo estos .md (los que cambia un push)")
    args = ap.parse_args()

    blog = Path(args.blog) / "src" / "content" / "blog"
    if not blog.exists():
        # El blog es OTRO repo y puede no estar clonado (CI, otra máquina). Desde que este
        # chequeo es bloqueante (16-sep-2026), morir acá bloquearía cada push desde cualquier
        # máquina sin el blog — y así es como se enseña a ignorar un bloqueante. Saltar es un
        # agujero conocido (un chequeo que no corre y pasa igual), así que avisa fuerte.
        print(f"  ⏭️  sin el repo del blog en {args.blog}: NO se verificó ninguna cifra")
        return 0
    if not MODELS_JSON.exists():
        sys.exit("Falta sitio/legado/data/models.json — corré export_for_pages.py primero")

    # Un post borrado en el push ya no existe en disco: no hay nada que verificar.
    objetivo = ([p for p in (Path(x) for x in args.posts) if p.exists()]
                if args.posts is not None else sorted(blog.glob("*.md")))

    d, ranked, pos = load_bench()
    alcance = (f"{len(objetivo)} post(s) de este push" if args.posts is not None
               else "todos los posts del blog")
    print(f"Verificando {alcance} contra models.json "
          f"({d['ranked_count']} modelos rankeados, generado {d['generated_at']})\n")

    total = 0
    for p in objetivo:
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
    print("  El titular es el ÍNDICE DE CALIDAD (escala absoluta, v4.1): una cifra citada")
    print("  ya NO caduca al medir un modelo nuevo. Lo que sí se mueve son las POSICIONES,")
    print("  porque el catálogo crece. Preferí lenguaje durable ('de los más baratos que")
    print("  empatan arriba') a una posición exacta.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
