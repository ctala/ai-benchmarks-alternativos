#!/usr/bin/env python3
"""Audita las 72 páginas publicadas: ¿recomiendan lo que la data sostiene?

POR QUÉ EXISTE (16-ago-2026)
----------------------------
Cristian, tras encontrar tres fallos distintos en dos días mirando páginas sueltas:
*"haz el análisis de todas las páginas por favor, seguimos encontrando errores como estos
que impiden que sean páginas útiles con el contenido y conocimiento generado."*

Tenía razón en el diagnóstico: los fallos no eran casualidad ni eran de una página. Eran
CLASES, y cada una vivía en decenas:

  · 22 de 72 lados de comparación coronados por un modelo que no rankea
  · 3 páginas publicadas que ningún generador regeneraba desde junio
  · el pilar «Agentes» ordenando por un criterio con correlación **negativa** (−0,204)
    contra la única verdad objetiva que tenemos (el reward de las tareas Harbor)
  · una tabla que dice ordenar por «Calidad en Agentes» y ordena por otra cosa

Ninguno rompe nada. Las páginas cargan, se ven bien y recomiendan mal. Es la clase de
fallo que este repo ya tiene nombrada —los detectores cazan AUSENCIA, y esto es presencia
de contenido plausible— y por eso hace falta un instrumento que pregunte lo que un
guardrail de esquema no pregunta: **¿lo que publica esta página lo sostiene la data?**

QUÉ VERIFICA (por clase, no por página)
---------------------------------------
P1. **Criterio ciego.** Una página de ranking que ordena por algo que NO correlaciona con
    la verdad objetiva disponible para ese caso. Hoy solo hay verdad objetiva para lo
    agéntico (Harbor), y es justo donde apareció el problema.
P2. **La tabla miente sobre su propio orden.** La columna de score que se muestra no es la
    que ordena las filas.
P3. **Recomienda lo que no se puede usar.** Retirados, no-aptos para agente en una página
    agéntica, o no-rankeados coronados sin salvedad.
P4. **Muestra vacía o mínima.** Un «top» de 1-3 filas, o una familia con un solo modelo:
    la página existe pero no compara nada.
P5. **Frescura falsa.** Dice «última actualización HOY» y su contenido no se regeneró.
P6. **Cifras que no coinciden** con `models.json` (un score publicado que ya no existe).

Uso:
    python benchmarks/auditar_paginas.py            # reporte completo
    python benchmarks/auditar_paginas.py --solo P1  # una clase
    python benchmarks/auditar_paginas.py --duro     # exit 1 si hay severidad alta
"""

import argparse
import json
import re
import statistics as st
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
DOCS = ROOT / "docs"
MODELS_JSON = DOCS / "data" / "models.json"

ALTA, MEDIA, BAJA = "🔴", "🟡", "⚪"


def _corr(xs, ys):
    if len(xs) < 5:
        return None
    mx, my = st.mean(xs), st.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = (sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) ** 0.5
    return num / den if den else None


def _filas(html):
    """(puesto, nombre) de la tabla principal — solo tablas con columna de puesto."""
    return [(int(i), n.strip()) for i, n in
            re.findall(r"<tr><td>(\d+)</td><td>(?:<strong>)?([^<]+)", html)]


def _filas_datos(html):
    """Cuántas filas de datos publica la página, tenga o no columna de puesto.

    Buscar solo `<tr><td>N</td>` daba 9 falsos positivos de «no publica NINGUNA fila»:
    las páginas de variantes y la de proveedores usan tablas sin columna de puesto —
    tienen 19 y 48 filas respectivamente. Una tabla sin ranking sigue siendo una tabla.
    """
    return len(re.findall(r"<tr[^>]*>\s*<td", html))


def _num_col(html, col=2):
    """Los valores de la columna `col` de cada fila, para ver si el orden es descendente."""
    out = []
    for tr in re.findall(r"<tr><td>\d+</td>.*?</tr>", html, re.S):
        # El contenido COMPLETO de cada celda, tags adentro. Buscar `<td>([^<]*)` se
        # detiene en el primer tag, así que una celda `<td><strong>9.3</strong></td>`
        # se leía vacía — y la columna que ordena, que va en negrita justamente por eso,
        # quedaba invisible para el chequeo que verifica si alguna columna ordena.
        celdas = [re.sub(r"<[^>]+>", " ", c) for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
        if len(celdas) > col:
            m = re.search(r"-?\d+[.,]\d+", celdas[col])
            out.append(float(m.group(0).replace(",", ".")) if m else None)
    return out


def cargar():
    d = json.loads(MODELS_JSON.read_text())
    por_nombre = {m["name"]: m for m in d["models"]}
    real = {}
    for m in d["models"]:
        t = (m.get("agentico") or {}).get("tareas") or {}
        if t:
            real[m["name"]] = sum(x["media"] for x in t.values()) / len(t)
    return d, por_nombre, real


def paginas():
    """slug → (path, generador)."""
    gens = {}
    for g in sorted((ROOT / "benchmarks").glob("generate_*.py")):
        txt = g.read_text()
        for s in re.findall(r'"slug":\s*"([^"]+)"', txt):
            gens.setdefault(s, g.stem)
    out = {}
    for p in sorted(DOCS.rglob("index.html")):
        slug = p.parent.relative_to(DOCS).as_posix()
        if slug == ".":
            continue
        out[slug] = (p, gens.get(slug, "?"))
    return out


# ── P1 · criterio ciego ──────────────────────────────────────────────────────
def p1(pgs, por_nombre, real):
    """¿El orden publicado predice el desempeño real, donde hay con qué comparar?

    Solo se puede juzgar donde existe verdad objetiva. Hoy eso es lo agéntico: el reward
    de las tareas Harbor, verificado por pytest sobre artefactos, no por un juez.
    """
    hallazgos = []
    for slug, (p, gen) in pgs.items():
        if not re.search(r"agent|n8n|tool|herramienta|automatiza", slug):
            continue
        html = p.read_text(errors="replace")
        filas = _filas(html)
        # SOLO LA PRIMERA TABLA. Una página puede tener dos que ordenan distinto a
        # propósito (capacidad · capacidad-por-precio); mezclarlas produce un orden que
        # no es el de ninguna.
        primera = re.search(r"<table.*?</table>", html, re.S)
        filas = _filas(primera.group(0)) if primera else filas
        pares = [(len(filas) - i, real[n]) for i, (_, n) in enumerate(filas) if n in real]
        # Mínimo 10: con 7 modelos una correlación de −0,45 es ruido, y publicarla como
        # hallazgo es el mismo error que se persigue — afirmar más de lo que la muestra
        # sostiene. Se prefiere no decir nada a decir algo que no aguanta.
        if len(pares) < 10:
            continue
        # Y SIN VARIANZA NO HAY NADA QUE CORRELACIONAR. En /mejor-llm-para-agentes/ los
        # ocho publicados sacan **1,000 exacto** en la tarea real: correlacionar un grupo
        # empatado da ruido (+0,09) y el chequeo lo reportaba como «el criterio no
        # predice». Que todos empaten arriba es justamente lo que se quería — el orden lo
        # decide el desempate, no la tarea.
        ys = [y for _, y in pares]
        if st.pstdev(ys) < 0.05:
            continue
        c = _corr([x for x, _ in pares], [y for _, y in pares])
        if c is None:
            continue
        if c < 0.1:
            sev = ALTA if c < 0 else MEDIA
            hallazgos.append((sev, slug, gen,
                              f"el orden publicado correlaciona {c:+.2f} con la tarea real "
                              f"({len(pares)} modelos con Harbor medido). "
                              + ("Correlación NEGATIVA: cuanto más arriba, PEOR le va en un "
                                 "agente de verdad" if c < 0 else
                                 "El criterio no predice el caso que la página promete")))
    return hallazgos


# ── P2 · la tabla miente sobre su propio orden ───────────────────────────────
def _ordenada(vals, bloques=False):
    """¿Esta columna explica el orden?

    `bloques=True` para las comparaciones: su tabla son DOS rankings concatenados (los 5
    mejores de cada familia), así que hay un salto legítimo en el medio. Exigir monotonía
    sobre las 10 filas las marcaba a todas — el salto entre familias no es un desorden,
    es la estructura de la página.
    """
    saltos = sum(1 for a, b in zip(vals, vals[1:]) if a < b - 0.051)
    if saltos == 0:
        return True
    if not bloques:
        return False
    # Las comparaciones apilan bloques: los N mejores de la familia A, los N de la B, y
    # los no-rankeados al final (que van últimos a propósito, no por su nota). Tres
    # bloques ⇒ hasta dos saltos legítimos. Exigir uno solo marcaba como rotas las
    # páginas donde el empuje de los no-rankeados al fondo hacía bien su trabajo.
    return saltos <= 2


def p2(pgs):
    """¿NINGUNA columna explica el orden de las filas?

    La primera versión miraba una columna fija (la 2) y marcaba
    /mejor-llm-para-razonamiento/ porque ahí la columna 2 es «Coding» — que obviamente no
    ordena una página de razonamiento. Falso positivo: el criterio SÍ estaba visible, en
    otra columna.

    La pregunta correcta no es «¿ordena ESTA columna?» sino **«¿ordena ALGUNA?»**. Si
    ninguna columna numérica es monótona decreciente, el número que decide el puesto no
    está en la tabla, y el lector ve un orden que no puede explicarse — que es el caso
    real de /mejor-llm-para-agentes/ (ordena por la tarea Harbor, que no era columna) y
    de las comparaciones (ordenan por calidad media, y muestran «Global»).
    """
    hallazgos = []
    for slug, (p, gen) in pgs.items():
        html_completo = p.read_text(errors="replace")
        # UNA TABLA A LA VEZ. Antes se juntaban las filas de toda la página, así que una
        # página con dos tablas —por ejemplo «calidad pura» y «calidad por precio», que
        # ordenan distinto A PROPÓSITO— se reportaba como desordenada. El chequeo tiene
        # que preguntar «¿esta tabla explica SU orden?», no «¿la página tiene un orden?».
        for html in re.findall(r"<table.*?</table>", html_completo, re.S) or [html_completo]:
            hallazgos += _p2_una_tabla(slug, gen, html)
    return hallazgos


def _p2_una_tabla(slug, gen, html):
    hallazgos = []
    if True:
        filas = re.findall(r"<tr><td>\d+</td>.*?</tr>", html, re.S)
        if len(filas) < 4:
            return hallazgos
        ncols = max(len(re.findall(r"<td[^>]*>", f)) for f in filas)
        alguna, columnas = False, 0
        for c in range(2, ncols):
            vals = [v for v in _num_col(html, c) if v is not None]
            if len(vals) < len(filas) * 0.8:
                continue
            columnas += 1
            if _ordenada(vals, bloques=("-vs-" in slug)):
                alguna = True
                break
        if columnas and not alguna:
            hallazgos.append((ALTA, slug, gen,
                              f"NINGUNA de sus {columnas} columnas numéricas explica el "
                              f"orden de las filas: el número que decide el puesto no "
                              f"está en la tabla. El lector ve un orden que no puede "
                              f"verificar"))
    return hallazgos


# ── P3 · recomienda lo que no se puede usar ──────────────────────────────────
def p3(pgs, d, por_nombre):
    retirados = {m["name"] for m in d["models"] if m.get("retired")}
    no_aptos = {m["name"] for m in d["models"] if m.get("sirve_para_agentes") is False}
    no_rank = {m["name"] for m in d["models"] if not m.get("ranked")}
    hallazgos = []
    for slug, (p, gen) in pgs.items():
        html = p.read_text(errors="replace")
        filas = _filas(html)
        if not filas:
            # SIN TABLA NUMERADA TAMBIÉN SE RECOMIENDA.
            #
            # Medido el 17-ago-2026 al preguntarse si el escrutinio era parejo: **10
            # páginas pasaban por 3 de las 6 clases** —las de variantes («¿cuál de los
            # Grok?») y las explicativas— porque su tabla no lleva columna de puesto y
            # `_filas()` no las veía. Son páginas publicadas que recomiendan modelos, y el
            # chequeo que evita mandar a alguien contra un endpoint muerto no las miraba.
            #
            # Acá se buscan los nombres en el texto: menos preciso que una fila, pero un
            # retirado nombrado en una página de recomendación es un problema igual, y es
            # mejor un aviso revisable que un punto ciego.
            texto = re.sub(r"<[^>]+>", " ", html)
            r = sorted({n for n in retirados if n in texto})
            if r:
                hallazgos.append((MEDIA, slug, gen,
                                  f"nombra modelo(s) RETIRADO(s) sin tabla que auditar: "
                                  f"{', '.join(r[:4])}. Verificá que no los recomiende"))
            continue
        nombres = [n for _, n in filas]
        r = [n for n in nombres if n in retirados]
        if r:
            hallazgos.append((ALTA, slug, gen,
                              f"recomienda modelo(s) RETIRADO(s): {', '.join(sorted(set(r))[:4])}. "
                              f"Su endpoint ya no existe: quien lo integre se estrella"))
        if re.search(r"agent|n8n|tool|herramienta|automatiza", slug):
            na = [f"#{i} {n}" for i, n in filas if n in no_aptos]
            if na:
                hallazgos.append((ALTA, slug, gen,
                                  f"página agéntica que lista modelos que NO corren dentro "
                                  f"de un agente: {', '.join(na[:4])}"))
        # La salvedad vale en cualquiera de sus dos formas: el párrafo de la sección
        # eje-por-eje («X no está rankeado») o el badge en la propia fila. Buscar solo la
        # primera daba 10 falsos positivos con el badge ya puesto — el chequeo exigía una
        # redacción, no la información.
        con_salvedad = "no está rankeado" in html or 'class="row-badge no-rankea"' in html
        top3 = [n for i, n in filas if i <= 3 and n in no_rank]
        if top3 and not con_salvedad:
            hallazgos.append((MEDIA, slug, gen,
                              f"corona en el top 3 a no-rankeado(s) sin salvedad: "
                              f"{', '.join(top3)}"))
    return hallazgos


# ── P4 · muestra vacía o mínima ──────────────────────────────────────────────
def p4(pgs):
    hallazgos = []
    for slug, (p, gen) in pgs.items():
        html = p.read_text(errors="replace")
        if 'http-equiv="refresh"' in html:
            continue                      # es un redirect declarado
        n = _filas_datos(html)
        if n == 0:
            hallazgos.append((ALTA, slug, gen, "no publica NINGUNA fila de datos"))
            continue
        # Una comparación 1-contra-1 tiene 2 filas por diseño y está bien. El umbral
        # bajo solo aplica a los RANKINGS, que prometen un listado: /mejor-llm-barato/
        # con 3 filas no es un ranking, es una terna.
        if "-vs-" not in slug and n < 5:
            hallazgos.append((MEDIA, slug, gen,
                              f"es un ranking y publica solo {n} fila(s): promete un "
                              f"listado y entrega una terna"))
        elif "-vs-" in slug and n < 2:
            hallazgos.append((ALTA, slug, gen,
                              f"comparación con {n} fila(s): un lado quedó sin modelos"))
    return hallazgos


# ── P5 · frescura falsa ──────────────────────────────────────────────────────
def p5(pgs):
    """Dice actualizarse hoy y su contenido no cambió con el último release.

    El caso real: una página congelada en junio que igual imprimía la fecha de hoy porque
    un sweep le tocó el pie. Frescura falsa hacia Google es peor que una fecha vieja.
    """
    hallazgos = []
    # Se compara CONTENIDO, no hashes de commit. La primera versión miraba si el archivo
    # se tocó en el último commit — y el último commit suele ser un merge, así que
    # marcaba páginas perfectamente frescas. Lo que importa no es cuándo se escribió el
    # archivo: es si su tabla concuerda con el models.json que se sirve hoy.
    try:
        d = json.loads(MODELS_JSON.read_text())
    except Exception:
        return hallazgos
    # Los cortes por eje publican el score de la SUITE, no del pilar. Compararlos solo
    # contra `dims_by_pillar` marcaba las 8 páginas de corte como desactualizadas —
    # publicaban su cifra correcta, de otra tabla.
    dims = {}
    for m in d["models"]:
        vals = [v.get("quality_avg") for v in (m.get("dims_by_pillar") or {}).values()]
        vals += list((m.get("score_by_suite") or {}).values())
        dims[m["name"]] = {i: v for i, v in enumerate(vals) if v is not None}
    for slug, (p, gen) in pgs.items():
        html = p.read_text(errors="replace")
        if 'http-equiv="refresh"' in html:
            continue
        m = re.search(r"Última actualización:\s*([\d-]+)", html)
        if not m:
            continue
        # ¿Alguna cifra de pilar publicada corresponde a la generación ANTERIOR?
        viejas = 0
        for nombre, celdas in re.findall(
                r"<tr><td>\d+</td><td>(?:<strong>)?([^<]+)</[^>]*>((?:\s*<td[^>]*>[^<]*)+)", html):
            vals = [float(x) for x in re.findall(r"\b\d\.\d\b", celdas)]
            act = [v for v in (dims.get(nombre.strip()) or {}).values() if v is not None]
            if not act or not vals:
                continue
            # una cifra de pilar que no está a <0,06 de NINGÚN pilar actual = generación vieja
            if any(all(abs(v - a) >= 0.06 for a in act) for v in vals
                   if any(abs(v - a) < 1.5 for a in act)):
                viejas += 1
        if viejas >= 3:
            hallazgos.append((MEDIA, slug, gen,
                              f"declara «última actualización {m.group(1)}» pero {viejas} "
                              f"filas publican cifras de una generación anterior"))
    return hallazgos


# ── P6 · cifras que ya no existen ────────────────────────────────────────────
def p6(pgs, por_nombre):
    hallazgos = []
    for slug, (p, gen) in pgs.items():
        html = p.read_text(errors="replace")
        malas = []
        for tr in re.findall(r"<tr><td>\d+</td><td>(?:<strong>)?([^<]+)</[^>]*>\s*<td[^>]*>([^<]*)",
                             html):
            nombre, celda = tr[0].strip(), tr[1]
            m = re.search(r"\d+[.,]\d+", celda)
            mod = por_nombre.get(nombre)
            if not m or not mod:
                continue
            pub = float(m.group(0).replace(",", "."))
            reales = [mod.get("score_global"), mod.get("score_calidad")]
            reales += list((mod.get("score_by_pillar") or {}).values())
            reales += list((mod.get("score_by_suite") or {}).values())
            reales += [v.get("quality_avg") for v in (mod.get("dims_by_pillar") or {}).values()]
            # Tolerancia 0,06: las páginas publican con UN decimal. `dims_by_pillar`
            # 9,046 sale impreso «9.0», y con 0,02 eso se reportaba como cifra sin
            # respaldo — 30 falsos positivos en la primera corrida. El redondeo no es
            # un error de dato; buscarlo como si lo fuera enterraba los hallazgos reales.
            if not any(v is not None and abs(v - pub) < 0.06 for v in reales):
                malas.append(f"{nombre} publica {pub}")
        if malas:
            hallazgos.append((MEDIA, slug, gen,
                              f"{len(malas)} cifra(s) sin respaldo en models.json: "
                              f"{'; '.join(malas[:3])}"))
    return hallazgos


CLASES = {
    "P1": ("Criterio ciego: el orden no predice el caso que la página promete", p1),
    "P2": ("La tabla miente sobre su propio orden", p2),
    "P3": ("Recomienda lo que no se puede usar", p3),
    "P4": ("Muestra vacía o mínima", p4),
    "P5": ("Frescura falsa", p5),
    "P6": ("Cifras sin respaldo en models.json", p6),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="una clase (P1..P6)")
    ap.add_argument("--duro", action="store_true", help="exit 1 si hay severidad alta")
    a = ap.parse_args()

    d, por_nombre, real = cargar()
    pgs = paginas()
    print(f"\nAuditando {len(pgs)} páginas publicadas contra los datos que las sostienen…")

    todo = {}
    for cid, (titulo, fn) in CLASES.items():
        if a.solo and cid != a.solo:
            continue
        if fn is p1:
            todo[cid] = (titulo, fn(pgs, por_nombre, real))
        elif fn is p3:
            todo[cid] = (titulo, fn(pgs, d, por_nombre))
        elif fn is p6:
            todo[cid] = (titulo, fn(pgs, por_nombre))
        else:
            todo[cid] = (titulo, fn(pgs))

    altas = 0
    for cid, (titulo, hs) in todo.items():
        print(f"\n{'─'*78}\n{cid} · {titulo}\n{'─'*78}")
        if not hs:
            print("  ✅ sin hallazgos")
            continue
        hs.sort(key=lambda x: (x[0] != ALTA, x[1]))
        altas += sum(1 for h in hs if h[0] == ALTA)
        for sev, slug, gen, msg in hs:
            print(f"  {sev} /{slug}/   [{gen}]")
            print(f"      {msg}")

    n = sum(len(hs) for _, hs in todo.values())
    print(f"\n{'═'*78}")
    print(f"  {n} hallazgo(s) · {altas} de severidad ALTA · sobre {len(pgs)} páginas")
    if altas:
        print(f"  Ninguno rompe una página: todas cargan. Por eso hacía falta preguntarles"
              f"\n  si lo que publican lo sostiene la data.")
    return 1 if (a.duro and altas) else 0


if __name__ == "__main__":
    sys.exit(main())
