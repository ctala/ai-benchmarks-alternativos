#!/usr/bin/env python3
"""¿Se publicó un modelo en el ranking sin haberle corrido la tarea agéntica?

POR QUÉ EXISTE (22-ago-2026)
----------------------------
Cristian, al ver GLM 5.3 recién publicado: *"¿de nuevo no usaste harbor antes de
publicar un modelo?"*. **De nuevo**, sí — y esa es la parte que importa. La primera vez
fueron 12 modelos, se corrigió a mano; la segunda, 5 GPT; la tercera, GLM 5.3 el mismo
día de su release. Tres veces el mismo hueco, arreglado tres veces sin dejar nada que
lo detecte.

Publicar un modelo sin tarea agéntica no rompe ninguna página: entra al ranking, se ve
completo, y lo único que pasa es que el eje agéntico y el wizard **no pueden
recomendarlo** — desaparece de la pregunta «para agentes» sin decir por qué. Es un hueco
que no se nota desde afuera, que es exactamente la clase que este repo caza.

QUÉ VERIFICA
------------
  A1  Todo modelo rankeado servido por OpenRouter tiene tarea agéntica medida, o un
      estado explícito de `ESTADOS_PERMITIDOS` con su motivo.
  A2  Un estado declarado no convive con cifras: si dice «sin dato», no publica tareas
      (ninguna página puede mostrar un 0 que no es del modelo).
  A3  Ninguna página pública rotula como agéntico un número que no sale de Harbor
      (8-nov-2026, Cristian). La única cifra agéntica es «N de M» tareas superadas en
      todos sus intentos, o «sin dato agéntico», en una celda `data-agentico="harbor"`:
        a. toda columna cuyo encabezado dice «agéntic…» tiene sus celdas marcadas así;
        b. toda celda marcada dice «N de M» o «sin dato agéntico», y si la fila enlaza a
           una ficha, coincide con `agentico.superadas` / `agentico.de` del export;
        c. ningún texto visible pone «agéntic…» junto a un decimal (8,38, 9.20…);
        d. la calculadora no rotula como agéntico un eje que no es de Harbor;
        e. en una página agéntica (publica celdas de Harbor), ninguna tabla con columna
           de Harbor lleva al lado un compuesto con decimales («Calidad×precio»,
           «capacidad», «score»);
        f. en una página agéntica, ningún texto publica «calidad 9,20/10» ni
           «−0,04 de calidad»: ahí esa cifra es `score_agentico` (60 % Harbor + 40 % tool
           calling) y se lee como la nota agéntica de la página.
      Existe porque `agentic_score` —multi-turno SIN herramientas— se publicó meses
      como «trabajo agéntico», y las landings mostraban como «tarea real» una mezcla
      de Harbor con tool calling. e y f (8-nov-2026): /mejor-llm-para-agentes/ ya mostraba
      «4 de 4» en su columna, pero el veredicto decía «calidad 9.20/10» y la segunda tabla
      «Calidad×precio 8,86», las dos de `score_agentico`, sin la palabra «agéntico»: a–c
      no las veían.

ESTADO PERMITIDO (6-nov-2026)
-----------------------------
«Sin dato agéntico · formato del endpoint»: el endpoint devuelve la llamada en un
formato que el parser del agente no lee (GPT-OSS en DeepInfra la manda dentro de
`reasoning_content` con `content` vacío). No es un hueco ni un cero del modelo: es un
estado que se publica como tal. Si el modelo no llamó o entró en un bucle, el cero es
real y entra como tarea medida.

POR QUÉ NO LO DETECTÓ ANTES (6-nov-2026)
----------------------------------------
Los tres Claude 5.5 entraron rankeados sin Harbor y el QA mostró ✅. El script SÍ los
listaba con ❌, pero solo salía con 1 bajo `--duro`, y `qa.py` lo corría sin el flag y
como informativo: exit 0, marca ✅. La prueba de sabotaje pasaba `--duro`, así que probaba
el detector y no el cableado. Hoy no hay flag (el rojo es rojo) y `check_cobertura` R9
caza cualquier `--duro` que `qa.py` no le pase a su script.

LO QUE NO CUENTA COMO FALTA
---------------------------
Un modelo servido por otro proveedor (`openai_direct`, `claude_code`, NIM, Groq) NO
puede heredar el resultado de OpenRouter: es otro endpoint, con su config. Eso ya lo
decide `export_for_pages` y acá se respeta — se listan aparte, como deuda declarada, no
como fallo. Correrles Harbor exige lanzarlo por SU ruta, que es otro trabajo.

Uso:
    python benchmarks/check_agentico_publicado.py      # exit 1 si falta alguno
"""

import argparse
import html as _html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS_JSON = ROOT / "docs" / "data" / "models.json"


# `agentico.sin_dato` → cómo se publica. Uno fuera de esta tabla es rojo: no se inventan.
ESTADOS_PERMITIDOS = {
    "formato_endpoint": "sin dato agéntico · formato del endpoint",
}


def clasificar(m: dict, prov: str) -> tuple[str, str]:
    """('medido' | 'estado' | 'otra_ruta' | 'falta' | 'invalido', detalle). Función pura."""
    # El estado explícito vive en `agentico.sin_dato`, NO en `agentico.estado`: ese campo
    # ya lo usa el export para apto / irregular / no_apto de lo MEDIDO. La v1 del 6-nov leía
    # `estado` y marcaba inválidos a todos los medidos; la prueba no lo vio porque su
    # control borraba `estado` del fixture.
    ag = m.get("agentico") or {}
    estado, tareas = ag.get("sin_dato"), ag.get("tareas")
    if estado:
        if estado not in ESTADOS_PERMITIDOS:
            return "invalido", f"estado desconocido «{estado}»"
        if not str(ag.get("motivo") or "").strip():
            return "invalido", f"«{estado}» sin motivo"
        if tareas:
            return "invalido", f"«{estado}» y además publica tareas: la página mostraría cifras"
        return "estado", ESTADOS_PERMITIDOS[estado]
    if tareas:
        return "medido", ""
    return ("falta" if prov == "openrouter" else "otra_ruta"), prov


DOCS = ROOT / "docs"
APP_JS = DOCS / "app.js"
CIFRA_HARBOR = re.compile(r"^(\d+) de (\d+)$")
SIN_DATO = "sin dato agéntico"
_ROTULO = re.compile(r"(?i)agéntic")
# Un decimal pegado al rótulo, en cualquiera de los dos órdenes: «calidad agéntica 8,38»,
# «trabajo agéntico: 6,27», «agéntico de 8,55» o «6,27 en trabajo agéntico». Solo admite
# una palabra de enlace, para no confundir «tareas agénticas Qwen 3.8 27B» con una cifra.
_DEC = r"(?<![\w.,$])\d{1,2}[.,]\d{1,2}(?![\w])"
_PROSA = re.compile(
    rf"(?i)agéntic\w*\s*(?:[:(=]\s*|(?:de|con|es|en|saca|da)\s+)?{_DEC}"
    rf"|{_DEC}(?:\s*/\s*10)?\s+(?:en|de)\s+(?:el\s+|la\s+)?(?:trabajo|tareas?|calidad|capacidad|score)\s+agéntic")


_COMPUESTO = re.compile(r"(?i)calidad|capacidad|score|puntaje|×")
_DEC_CELDA = re.compile(r"^\$?\d+[.,]\d+")
_NOTA_PAGINA = re.compile(
    r"(?i)calidad\s+\d+[.,]\d+\s*/\s*10|[+\-−]\d+[.,]\d+\s+de\s+calidad")


class _Tablas(HTMLParser):
    """Tablas de una página: encabezados y filas (atributos, texto y enlace a ficha)."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tablas, self._t, self._celda, self._fila = [], None, None, None
        self.texto, self._oculto = [], 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self._oculto += 1
        elif tag == "table":
            self._t = {"head": [], "rows": []}
        elif tag == "tr" and self._t is not None:
            self._fila = {"celdas": [], "ficha": None}
        elif tag in ("td", "th") and self._fila is not None:
            self._celda = {"tag": tag, "attrs": a, "txt": "", "harbor": a.get("data-agentico") == "harbor"}
        elif self._celda is not None and a.get("data-agentico") == "harbor":
            # Astro marca el `<span>` de la cifra dentro de la celda (Eje.astro); Python, el `<td>`.
            self._celda["harbor"] = True
        elif tag == "a" and self._fila is not None:
            m = re.match(r"^/modelo/([^/]+)/", a.get("href") or "")
            if m and self._fila["ficha"] is None:
                self._fila["ficha"] = m.group(1)

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._oculto = max(0, self._oculto - 1)
        elif tag in ("td", "th") and self._celda is not None and self._fila is not None:
            self._celda["txt"] = " ".join(self._celda["txt"].split())
            self._fila["celdas"].append(self._celda)
            self._celda = None
        elif tag == "tr" and self._fila is not None and self._t is not None:
            if self._fila["celdas"] and all(c["tag"] == "th" for c in self._fila["celdas"]):
                self._t["head"] = [c["txt"] for c in self._fila["celdas"]]
            else:
                self._t["rows"].append(self._fila)
            self._fila = None
        elif tag == "table" and self._t is not None:
            self.tablas.append(self._t)
            self._t = None

    def handle_data(self, data):
        if self._oculto:
            return
        self.texto.append(data)
        if self._celda is not None:
            self._celda["txt"] += data


def a3_pagina(html: str, por_key: dict) -> list[str]:
    """Hallazgos A3 (a, b, c) de UNA página. Función pura."""
    p = _Tablas()
    p.feed(re.sub(r"<!--.*?-->", "", html, flags=re.S))
    malos = []
    for tb in p.tablas:
        cols = [i for i, h in enumerate(tb["head"]) if _ROTULO.search(h)]
        for f in tb["rows"]:
            for i, c in enumerate(f["celdas"]):
                marcada = c["harbor"]
                if i in cols and not marcada:
                    malos.append(f"a · columna «{tb['head'][i]}» con una celda que no sale de Harbor: «{c['txt']}»")
                if not marcada:
                    continue
                txt = c["txt"]
                mm = CIFRA_HARBOR.match(txt)
                if not mm and txt != SIN_DATO:
                    malos.append(f"b · celda agéntica con «{txt}» (solo «N de M» o «{SIN_DATO}»)")
                    continue
                m = por_key.get(f["ficha"]) if f["ficha"] else None
                if m is not None:
                    ag = m.get("agentico") or {}
                    esperado = (f"{ag['superadas']} de {ag['de']}" if ag.get("de") else SIN_DATO)
                    if txt != esperado:
                        malos.append(f"b · {m.get('name')}: la página dice «{txt}» y Harbor, «{esperado}»")
    texto = " ".join(" ".join(p.texto).split())
    for mm in _PROSA.finditer(texto):
        malos.append(f"c · «{texto[max(0, mm.start() - 30):mm.end() + 10]}»")
    agentica = any(c["harbor"] for tb in p.tablas for f in tb["rows"] for c in f["celdas"])
    if agentica:
        for tb in p.tablas:
            if not any(c["harbor"] for f in tb["rows"] for c in f["celdas"]):
                continue
            for i, h in enumerate(tb["head"]):
                if not _COMPUESTO.search(h):
                    continue
                vals = [f["celdas"][i]["txt"] for f in tb["rows"] if i < len(f["celdas"])]
                dec = [v for v in vals if _DEC_CELDA.match(v) and not v.startswith("$")]
                if dec:
                    malos.append(f"e · en la tabla agéntica, «{h}» publica {dec[0]}: un "
                                 f"compuesto con decimales al lado de Harbor")
        for mm in _NOTA_PAGINA.finditer(texto):
            malos.append(f"f · página agéntica con «{texto[max(0, mm.start() - 30):mm.end() + 10]}»")
    return malos


def a3_app(js: str) -> list[str]:
    """A3 d: en la calculadora, un rótulo agéntico solo para un eje de Harbor."""
    malos = []
    for k, v in re.findall(r"(\w+):\s*\"([^\"]*)\"", js):
        if _ROTULO.search(v) and not k.startswith("harbor"):
            malos.append(f"d · app.js rotula «{k}» como «{v}»")
    if "data-agentico" not in js:
        malos.append("d · app.js no marca la celda agéntica (`data-agentico`): ciego")
    return malos


def a3(d: dict) -> tuple[list[str], int]:
    import paginas_leidas as pl
    por_key = {m["key"]: m for m in d["models"]}
    malos, paginas, leidas = [], 0, set()
    for f in sorted(DOCS.rglob("*.html")):
        paginas += 1
        if f.name == "index.html":
            leidas.add(pl.url_de(DOCS, f))
        for x in a3_pagina(f.read_text(encoding="utf-8", errors="ignore"), por_key):
            malos.append(f"{f.relative_to(DOCS)}: {x}")
    malos += a3_app(APP_JS.read_text(encoding="utf-8"))
    # Regla de páginas leídas (motor-sitio 2.3): todas las páginas con contenido del registro.
    malos += pl.exigir("A3", leidas, pl.esperadas())
    return malos, paginas


def main() -> int:
    global DOCS, APP_JS
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dist", type=Path, default=None,
                    help="leer lo que compila Astro (sitio/dist); los datos siguen saliendo de docs/")
    a = ap.parse_args()
    if a.dist:
        DOCS, APP_JS = a.dist, a.dist / "app.js"

    sys.path.insert(0, str(ROOT / "benchmarks"))
    from models import MODELS

    d = json.loads(MODELS_JSON.read_text())
    rank = [m for m in d["models"] if m.get("ranked")]
    if not rank:
        print("❌ A0 models.json no trae rankeados: el chequeo está ciego")
        return 1
    grupos: dict[str, list] = {"medido": [], "estado": [], "otra_ruta": [], "falta": [], "invalido": []}
    for m in rank:
        cfg = MODELS.get(m.get("key") or "", {})
        clase, det = clasificar(m, cfg.get("provider", "openrouter"))
        grupos[clase].append((m["name"], cfg.get("id"), det))

    print("TAREA AGÉNTICA EN LO PUBLICADO\n")
    print(f"  A1 · rankeados con tarea real ejecutada: {len(grupos['medido'])}/{len(rank)}")
    if grupos["estado"]:
        print(f"\n  ℹ️  {len(grupos['estado'])} con estado explícito (permitido, se publica así):")
        for n, i, det in grupos["estado"]:
            print(f"     {n:<24} {str(i):<32} {det}")
    if grupos["otra_ruta"]:
        print(f"\n  ℹ️  {len(grupos['otra_ruta'])} servidos por otra ruta — no pueden heredar el "
              f"resultado de OpenRouter:")
        for n, i, p in grupos["otra_ruta"]:
            print(f"     {n:<24} {str(i):<18} ({p})")
    rojo = False
    if grupos["invalido"]:
        rojo = True
        print(f"\n  ❌ A2 · {len(grupos['invalido'])} con un estado que no se sostiene:\n")
        for n, i, det in grupos["invalido"]:
            print(f"     {n:<24} {det}")
    if grupos["falta"]:
        rojo = True
        print(f"\n  ❌ {len(grupos['falta'])} rankeado(s) publicados SIN tarea agéntica:\n")
        for n, i, _ in grupos["falta"]:
            print(f"     {n:<24} {i}")
        print("\n     No rompe ninguna página: entran al ranking y se ven completos. Lo que")
        print("     pasa es que el eje agéntico y el wizard NO pueden recomendarlos, y nada")
        print("     lo dice. Correr:")
        print("       harbor run -p tareas-agente/<tarea> -a mini-swe-agent \\")
        print("         -m openrouter/<id> -k 3 -n 3 --agent-env \"OPENROUTER_API_KEY=$K\"")
        print("     y después `python benchmarks/export_harbor.py`.")
    malos, paginas = a3(d)
    marcadas = sum(f.read_text(encoding="utf-8", errors="ignore").count('data-agentico="harbor"')
                   for f in DOCS.rglob("*.html"))
    print(f"\n  A3 · {paginas} páginas leídas, {marcadas} celdas agénticas de Harbor")
    if not paginas or not marcadas:
        rojo = True
        print("  ❌ A3 ciego: no leyó páginas o ninguna publica la cifra de Harbor")
    if malos:
        rojo = True
        print(f"  ❌ A3 · {len(malos)} rótulo(s) agéntico(s) sobre algo que no es Harbor:\n")
        for x in malos[:30]:
            print(f"     {x}")
    if not rojo:
        print("\n  ✅ todo rankeado por OpenRouter tiene su tarea agéntica medida o un estado explícito,")
        print("     y lo único que se publica como agéntico sale de Harbor.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
