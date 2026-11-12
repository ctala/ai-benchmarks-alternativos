#!/usr/bin/env python3
"""La nota de calidad tiene UNA definición y todas las superficies la leen del export.

POR QUÉ (DECISIONES, 9-nov-2026)
--------------------------------
Desde v6.0.0 la calidad es 75 % examen + 25 % Harbor (`indice.py`). Una nota así tiene dos
formas de romperse en silencio: que una superficie la recalcule con otro peso (una segunda
definición que se desincroniza sola) y que una cifra del grupo de cabeza o un modelo sin
dato agéntico se cuele escrito a mano. Las dos producen números con forma válida: ningún
detector de ausencia las ve.

Qué verifica (exit 1 si algo falla; bloqueante en `qa.py`):
  I1  cada `score_calidad` y `calidad_ci95` publicados salen de `indice.calidad` con los
      componentes publicados (examen, su margen, nota de Harbor y su error)
  I2  ninguna superficie combina examen y Harbor por su cuenta: el peso vive solo en
      `indice.py`, y ni `app.js` ni un generador multiplican `quality_avg`/`nota_harbor`
  I3  el peso que muestra el HTML estático coincide con el export
  I4  `grupo_cabeza` es coherente (n, más barato, margen) y la línea del README dice lo mismo
  I5  un modelo sin dato agéntico no rankea, no tiene nota y no aparece en ningún orden por
      la nota: ni en el grupo, ni en el README, ni en una tabla «Calidad» de las páginas
  I6  ningún tier publicado es una ruta (`cloud_nim` y compañía van en `ruta`)
  I7  cada regla de `indice.CHECKS_SIN_CONTAR` está atada a la versión publicada de su tarea
      (`task_checksum` de `resultados.json`); si se publicó otra versión (la corregida ya se
      midió), la regla se borra. Cuando el directorio de la tarea en disco ES esa versión
      (`dirhash`), cada check excluido existe en su `test_outputs.py` y el total de checks
      coincide (una errata dejaría la regla sin efecto en silencio). `resultados.json` publica
      la misma lista por tarea (DECISIONES, 9-nov-2026)
  I8  si hay checks que no cuentan, la línea de método que los declara sale del export y
      aparece en la calculadora (`#nota-checks`, que llena app.js) y en cada ficha con nota de
      agente; si no hay, no aparece en ninguna

Uso:
    python benchmarks/check_indice_calidad.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from benchmarks import indice  # noqa: E402

TOL = 0.011

# I2: lo que delata una combinación propia de examen y Harbor.
# Un `*` suelto con espacios: el operador. `**` (negrita de markdown, potencia) no cuenta.
_OP = r"(?<![*])\s\*\s(?![*])"
_MULT = re.compile(rf"(quality_avg|nota_harbor|nota_examen)\b[^\n;]{{0,40}}{_OP}|{_OP}[^\n;]{{0,40}}\b(quality_avg|nota_harbor|nota_examen)\b")
_PESO_DEF = re.compile(r"PESO_HARBOR_EN_CALIDAD\s*=")
# El compuesto de «a tu medida» multiplica `quality_avg` por su peso a propósito: es el
# examen dentro del compuesto, no la nota de calidad. Se permite solo esa línea.
_PERMITIDAS_APP = ('{ col: "quality_avg",',)


def i1_nota(models: list[dict]) -> list[str]:
    fallos = []
    for m in models:
        q, ci = indice.calidad(m.get("quality_avg"), m.get("quality_ci95"),
                               m.get("nota_harbor"), m.get("nota_harbor_se"))
        pub, pci = m.get("score_calidad"), m.get("calidad_ci95")
        if (q is None) != (pub is None):
            fallos.append(f"I1 · {m['key']}: score_calidad={pub} y la fórmula da {q}")
        elif q is not None and abs(q - pub) > TOL:
            fallos.append(f"I1 · {m['key']}: score_calidad {pub} ≠ {q:.3f} de `indice.calidad`")
        elif ci is not None and pci is not None and abs(ci - pci) > TOL:
            fallos.append(f"I1 · {m['key']}: calidad_ci95 {pci} ≠ {ci:.3f}")
    return fallos


def i2_peso_unico(fuentes: dict[str, str]) -> list[str]:
    """`fuentes`: {ruta: texto} de los .py del pipeline y de `sitio/legado/app.js`."""
    fallos = []
    for ruta, txt in fuentes.items():
        if ruta.endswith("indice.py") or "test_" in ruta or ruta.endswith("check_indice_calidad.py"):
            continue
        if _PESO_DEF.search(txt):
            fallos.append(f"I2 · {ruta}: define PESO_HARBOR_EN_CALIDAD (vive solo en indice.py)")
        for n, linea in enumerate(txt.splitlines(), 1):
            if ruta.endswith(".js") and any(p in linea for p in _PERMITIDAS_APP):
                continue
            if _MULT.search(linea):
                fallos.append(f"I2 · {ruta}:{n}: combina examen o Harbor por su cuenta: {linea.strip()[:90]}")
    return fallos


def i3_html(data: dict, html: str) -> list[str]:
    ic = data.get("indice_calidad") or {}
    if ic.get("peso_harbor") is None:
        return ["I3 · models.json no trae `indice_calidad.peso_harbor`"]
    ph = round(100 * ic["peso_harbor"])
    fallos = []
    for clase, esperado in (("peso-harbor", ph), ("peso-examen", 100 - ph)):
        for v in re.findall(rf'class="{clase}">(\d+)<', html):
            if int(v) != esperado:
                fallos.append(f"I3 · index.html: .{clase} dice {v} y el export {esperado}")
    if ic["peso_harbor"] != indice.PESO_HARBOR_EN_CALIDAD:
        fallos.append("I3 · el export publica un peso distinto al de indice.py")
    return fallos


def i4_grupo(data: dict, readme: str) -> list[str]:
    g = data.get("grupo_cabeza") or {}
    por_key = {m["key"]: m for m in data["models"]}
    claves = g.get("claves") or []
    fallos = []
    if g.get("n") != len(claves):
        fallos.append(f"I4 · grupo_cabeza.n={g.get('n')} con {len(claves)} claves")
    cab = [por_key[k] for k in claves if k in por_key]
    if any(not m.get("ranked") for m in cab):
        fallos.append("I4 · el grupo de cabeza tiene un modelo que no rankea")
    con_precio = [m for m in cab if m.get("cost_per_1k_calls_usd") is not None]
    if con_precio:
        b = min(con_precio, key=lambda m: m["cost_per_1k_calls_usd"])
        if (g.get("mas_barato") or {}).get("key") != b["key"]:
            fallos.append(f"I4 · mas_barato={g.get('mas_barato')} y el más barato del grupo es {b['key']}")
    cis = [m["calidad_ci95"] for m in cab if m.get("calidad_ci95") is not None]
    if cis and (g.get("margen") is None or abs(round(median(cis), 2) - g["margen"]) > TOL):
        fallos.append(f"I4 · margen={g.get('margen')} y la mediana del grupo es {median(cis):.2f}")
    m = re.search(r"El benchmark no separa a estos \*{0,2}(\d+)\*{0,2} de (\d+) rankeados\*{0,2} "
                  r"\(margen de error ±([\d,]+)\)[^\n]*?el más barato es \*\*([^*]+)\*\*", readme)
    if not m:
        fallos.append("I4 · el README no tiene la línea del grupo de cabeza")
    else:
        n, de, mg, nombre = int(m[1]), int(m[2]), float(m[3].replace(",", ".")), m[4]
        if (n, de) != (g.get("n"), g.get("de")):
            fallos.append(f"I4 · el README dice {n} de {de} y el export {g.get('n')} de {g.get('de')}")
        if g.get("margen") is not None and abs(mg - g["margen"]) > TOL:
            fallos.append(f"I4 · el README dice margen ±{mg} y el export ±{g['margen']}")
        if nombre != (g.get("mas_barato") or {}).get("name"):
            fallos.append(f"I4 · el README nombra a «{nombre}» como el más barato")
    return fallos


def _tablas_calidad(html: str) -> list[str]:
    """Las tablas de una página cuya columna de orden se llama «Calidad»."""
    out = []
    for t in re.findall(r"<table.*?</table>", html, flags=re.S):
        if re.search(r'<th scope="col">Calidad</th>', t):
            out.append(t)
    return out


def i5_sin_dato(data: dict, readme: str, paginas: dict[str, str]) -> list[str]:
    fallos = []
    claves = set((data.get("grupo_cabeza") or {}).get("claves") or [])
    sin = [m for m in data["models"] if (m.get("agentico") or {}).get("sin_dato")]
    bloque = readme.split("<!-- AUTO-RANKING-START -->")[-1].split("<!-- AUTO-RANKING-END -->")[0]
    for m in sin:
        if m.get("ranked") or m.get("score_calidad") is not None:
            fallos.append(f"I5 · {m['key']}: sin dato agéntico y ranked={m.get('ranked')}, "
                          f"score_calidad={m.get('score_calidad')}")
        if m["key"] in claves:
            fallos.append(f"I5 · {m['key']}: sin dato agéntico y en el grupo de cabeza")
        if f"**{m['name']}**" in bloque:
            fallos.append(f"I5 · {m['key']}: sin dato agéntico y en la tabla del README")
        for ruta, html in paginas.items():
            for t in _tablas_calidad(html):
                if f"/modelo/{m['key']}/" in t:
                    fallos.append(f"I5 · {ruta}: lista a {m['key']} (sin dato agéntico) en una tabla por calidad")
    return fallos


def i6_tier(data: dict) -> list[str]:
    return [f"I6 · {m['key']}: tier «{m.get('tier')}» es una ruta, no un precio"
            for m in data["models"] if indice.es_ruta(m.get("tier"))]


def i7_checks_sin_contar(sin_contar: dict, tests: dict[str, str], resultados: dict,
                         checksums_disco: dict[str, str]) -> list[str]:
    """`tests`: {tarea: texto de su test_outputs.py}; `resultados`: tareas-agente/resultados.json;
    `checksums_disco`: {tarea: dirhash del directorio de la tarea tal como está en disco}."""
    fallos = []
    publicadas = (resultados or {}).get("tareas") or {}
    if not publicadas:
        fallos.append("I7 · resultados.json no trae tareas: el chequeo no miró nada")
    for tarea, regla in sin_contar.items():
        src = tests.get(tarea)
        if src is None:
            fallos.append(f"I7 · {tarea}: no existe la tarea, y tiene checks que no cuentan")
            continue
        publicado = (publicadas.get(tarea) or {}).get("task_checksum")
        if publicado != regla.get("checksum"):
            fallos.append(f"I7 · {tarea}: la regla es de la versión {str(regla.get('checksum'))[:12]} y "
                          f"la publicada es {str(publicado)[:12]}: la corregida ya se midió, "
                          "sus checks vuelven a contar y la regla se borra de CHECKS_SIN_CONTAR")
            continue
        if checksums_disco.get(tarea) != regla["checksum"]:
            continue   # la tarea en disco ya es otra versión (corregida, sin medir): no se lee aquí
        for c in regla["checks"]:
            if not re.search(rf"^def {re.escape(c)}\(", src, flags=re.M):
                fallos.append(f"I7 · {tarea}: el check «{c}» no está en su test_outputs.py")
        n = len(re.findall(r"^def test_", src, flags=re.M))
        if n != regla.get("de"):
            fallos.append(f"I7 · {tarea}: la regla dice {regla.get('de')} checks y la tarea tiene {n}")
    for tarea, d in publicadas.items():
        esperado = sorted(indice.checks_excluidos(tarea, d.get("task_checksum")))
        if d.get("checks_sin_contar") != esperado:
            fallos.append(f"I7 · {tarea}: resultados.json publica checks_sin_contar="
                          f"{d.get('checks_sin_contar')} y indice.py dice {esperado}")
    return fallos


def i8_linea_checks(data: dict, html: str, app_js: str, fichas: dict[str, str]) -> list[str]:
    """`fichas`: {key: html de sitio/legado/modelo/<key>/index.html}."""
    from html import escape
    ic = data.get("indice_calidad") or {}
    meta = indice.checks_sin_contar_meta(ROOT)
    linea = indice.linea_checks_sin_contar(meta)
    fallos = []
    if ic.get("checks_sin_contar") != meta:
        fallos.append("I8 · models.json publica otros checks_sin_contar que indice.py")
    if ic.get("linea_checks") != linea:
        fallos.append("I8 · la línea de método publicada no sale de indice.linea_checks_sin_contar")
    con_agente = [m["key"] for m in data["models"] if m.get("nota_harbor") is not None]
    if not fichas:
        fallos.append("I8 · no leí ninguna ficha: el chequeo no miró nada")
    if linea:
        if 'id="nota-checks"' not in html or "linea_checks" not in app_js:
            fallos.append("I8 · la calculadora no muestra la línea de los checks que no cuentan")
        faltan = [k for k in con_agente if k in fichas and escape(linea, quote=False) not in fichas[k]]
        if faltan:
            fallos.append(f"I8 · {len(faltan)} ficha(s) con nota de agente sin la línea de método: {faltan[:3]}")
    else:
        sobran = [k for k, h in fichas.items() if "nota-checks" in h]
        if sobran:
            fallos.append(f"I8 · {len(sobran)} ficha(s) declaran checks excluidos y no hay ninguno")
    return fallos


# Lo publicado se lee de `sitio/legado/` o, con `--dist`, de lo que compila Astro (motor-sitio 2.3).
# Los datos (models.json) siguen saliendo de sitio/legado/.
SITIO = ROOT / "sitio" / "legado"


def _leer(p: Path) -> str:
    """Un archivo publicado, o vacío si no está: su ausencia la cuenta la regla de páginas leídas."""
    return p.read_text(encoding="utf-8") if p.exists() else ""


def leer_fichas() -> dict[str, str]:
    return {p.parent.name: p.read_text(encoding="utf-8")
            for p in sorted((SITIO / "modelo").glob("*/index.html"))}


def leer_harbor() -> tuple[dict, dict, dict]:
    # El checksum de Harbor es `dirhash(dir, "sha256")` (harbor 0.21, `Task.checksum`). Sin
    # el paquete, I7 no puede saber qué versión está en disco: falla con ruido, no en silencio.
    from dirhash import dirhash
    tests = {p.parent.parent.name: p.read_text(encoding="utf-8")
             for p in sorted((ROOT / "tareas-agente").glob("*/tests/test_outputs.py"))}
    resultados = json.loads((ROOT / "tareas-agente" / "resultados.json").read_text(encoding="utf-8"))
    disco = {t: dirhash(str(ROOT / "tareas-agente" / t), "sha256") for t in indice.CHECKS_SIN_CONTAR
             if (ROOT / "tareas-agente" / t).is_dir()}
    return tests, resultados, disco


def revisar(data, readme, html, fuentes, paginas) -> list[str]:
    return (i1_nota(data["models"]) + i2_peso_unico(fuentes) + i3_html(data, html)
            + i4_grupo(data, readme) + i5_sin_dato(data, readme, paginas) + i6_tier(data))


def leer_todo():
    data = json.loads((ROOT / "sitio" / "legado" / "data" / "models.json").read_text(encoding="utf-8"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    html = _leer(SITIO / "index.html")
    fuentes = {str(p.relative_to(ROOT)): p.read_text(encoding="utf-8")
               for p in sorted((ROOT / "benchmarks").glob("*.py"))}
    fuentes["sitio/legado/app.js"] = _leer(SITIO / "app.js")
    paginas = {"sitio/legado/" + str(p.relative_to(SITIO)): p.read_text(encoding="utf-8")
               for p in sorted(SITIO.glob("*/index.html"))}
    return data, readme, html, fuentes, paginas


def main() -> int:
    global SITIO
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", type=Path, default=None,
                    help="leer lo publicado de lo que compila Astro (sitio/dist); los datos, de sitio/legado/")
    a = ap.parse_args()
    if a.dist:
        SITIO = a.dist
    import paginas_leidas as pl
    data, readme, html, fuentes, paginas = leer_todo()
    fichas = leer_fichas()
    # Regla de páginas leídas: I3 lee la home, I5 las páginas de primer nivel e I8 las fichas.
    leidas = ({"/"} if html else set()) | {f"/{Path(k).parent.name}/" for k in paginas} \
        | {f"/modelo/{k}/" for k in fichas}
    ciego = pl.exigir("check_indice_calidad", leidas, pl.esperadas())
    fallos = revisar(data, readme, html, fuentes, paginas)
    fallos += i7_checks_sin_contar(indice.CHECKS_SIN_CONTAR, *leer_harbor())
    fallos += i8_linea_checks(data, html, fuentes["sitio/legado/app.js"], fichas)
    fallos += ciego
    leidos = sum(1 for m in data["models"] if m.get("score_calidad") is not None)
    print(f"  {leidos} notas de calidad leídas · {len(paginas)} páginas · {len(fuentes)} fuentes")
    if not leidos:
        print("  ❌ cero notas leídas: el chequeo no miró nada")
        return 1
    for f in fallos:
        print(f"  ❌ {f}")
    if fallos:
        print(f"  ❌ {len(fallos)} problema(s) con la nota de calidad")
        return 1
    print("  ✅ la nota de calidad tiene una definición y todas las superficies la leen del export")
    return 0


if __name__ == "__main__":
    sys.exit(main())
