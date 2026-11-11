#!/usr/bin/env python3
"""El JSON-LD y las meta descriptions de la home salen de la página y de models.json. (11-nov-2026, motor-sitio)

POR QUÉ EXISTE
--------------
La home (`docs/index.html`) se escribió a mano, y con ella su JSON-LD y sus tres meta
descriptions. `check_jsonld` encontró dos errores en vivo que nadie veía porque esas partes
no se ven en la página:

  · la FAQPage del JSON-LD era otra versión de la FAQ visible: seis respuestas parafraseadas
    y una pregunta («¿…multimodales o de contexto largo?») que la página ya no mostraba.
    Google exige que la FAQ declarada se vea en la página.
  · «Compara 191 modelos», «82 con muestra suficiente» y «29.000+ tests» estaban escritos a
    mano. Hoy son 193, 74 y 88.000+.

Una sola fuente para cada cosa:
  · la FAQPage se arma con las preguntas y respuestas de `<section class="faq">` tal como
    se ven;
  · las cifras salen de `models.json` (`tested_count`, `ranked_count`) y las ejecuciones de
    `conteos.ejecuciones`, la misma cuenta que usa el resto del sitio.

Lo vigilan `check_jsonld` J4 (bloquea en la home) y `check_consistency` (lee el JSON-LD y
las meta, no solo el texto visible).

Uso:
    python benchmarks/generate_home_jsonld.py           # reescribe docs/index.html
    python benchmarks/generate_home_jsonld.py --check   # exit 1 si la home no está al día
"""
from __future__ import annotations

import argparse
import html as _h
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
INDEX = ROOT / "docs" / "index.html"
MODELS = ROOT / "docs" / "data" / "models.json"

BLOQUE = re.compile(r'(<script type="application/ld\+json">\n)(.*?)(\n</script>)', re.S)
FAQ = re.compile(r'<section class="faq" id="faq">(.*?)</section>', re.S)
ITEM = re.compile(r"<details>\s*<summary><strong>(.*?)</strong></summary>(.*?)</details>", re.S)


def _texto(fragmento: str) -> str:
    """El texto visible de un fragmento de HTML, en una línea."""
    t = re.sub(r"<[^>]+>", " ", fragmento)
    t = re.sub(r"\s+", " ", _h.unescape(t)).strip()
    return re.sub(r" ([,.;:)»])", r"\1", t).replace("( ", "(").replace("« ", "«")


def faq_visible(pagina: str) -> list[tuple[str, str]]:
    """(pregunta, respuesta) de la FAQ tal como la página la muestra. Función pura."""
    sec = FAQ.search(pagina)
    if not sec:
        raise SystemExit("la home no tiene <section class=\"faq\" id=\"faq\">: no hay FAQ que declarar")
    out = [(_texto(q), _texto(a)) for q, a in ITEM.findall(sec.group(1))]
    if not out:
        raise SystemExit("la FAQ de la home no tiene ningún <details> legible")
    return out


def _miles(n: int) -> str:
    """88363 → «88.000+»: redondeo hacia abajo al millar, separador de miles en español."""
    return f"{(n // 1000) * 1000:,}".replace(",", ".") + "+"


def cifras(d: dict) -> dict:
    from conteos import ejecuciones
    return {"modelos": d["tested_count"], "rankeados": d["ranked_count"],
            "tests": _miles(ejecuciones(d))}


def textos(c: dict) -> dict:
    """Las frases con cifras de la home. La prosa es fija; las cifras, no."""
    m, r, t = c["modelos"], c["rankeados"], c["tests"]
    return {
        "description": f"Compara {m} modelos de IA con {t} tests reales: precio, calidad, velocidad y "
                       f"tool calling. Encuentra alternativas a Claude, GPT-5, Gemini para agentes N8N, "
                       f"Hermes y emprendedores. Benchmark gratis y open source.",
        "og:description": f"Compara {m} modelos de IA con {t} tests reales. Encuentra el mejor para tu "
                          f"agente N8N, Hermes o uso personal.",
        "twitter:description": f"Compara {m} modelos con tests reales. Alternativas a Claude, GPT-5 y "
                               f"Gemini para N8N y Hermes.",
        "Dataset": f"Benchmark abierto de {m} modelos de IA (LLMs) con {t} tests reales organizados en 4 "
                   f"pilares (Razonamiento, Coding, Contenido, Agentes) + long-context y seguridad como "
                   f"dimensiones separadas. Evaluación con LLM-as-Judge Phi-4 vía OpenRouter.",
        "SoftwareApplication": f"Calculadora interactiva para encontrar el mejor modelo IA según presupuesto, "
                               f"calidad, velocidad, tarea y caso de uso. Filtra entre {m} modelos "
                               f"benchmarkeados ({r} con muestra suficiente para rankear) con pesos ajustables.",
    }


def generar(pagina: str, d: dict) -> str:
    """La home con su JSON-LD y sus meta al día. Función pura."""
    tx = textos(cifras(d))
    for nombre, attr in (("description", "name"), ("og:description", "property"),
                         ("twitter:description", "name")):
        patron = re.compile(rf'(<meta {attr}="{re.escape(nombre)}" content=")[^"]*(")')
        if not patron.search(pagina):
            raise SystemExit(f"la home no tiene <meta {attr}=\"{nombre}\">")
        pagina = patron.sub(lambda m: m.group(1) + _h.escape(tx[nombre], quote=True) + m.group(2), pagina, count=1)

    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}}
                          for q, a in faq_visible(pagina)]}
    vistos = set()

    def reemplazo(m):
        d_ = json.loads(m.group(2))
        if d_.get("@type") == "FAQPage":
            vistos.add("FAQPage")
            d_ = faq
        else:
            for it in d_.get("@graph", []):
                if it.get("@type") in ("Dataset", "SoftwareApplication"):
                    vistos.add(it["@type"])
                    it["description"] = tx[it["@type"]]
        cuerpo = json.dumps(d_, ensure_ascii=False, indent=2).replace("</", "<\\/")
        return m.group(1) + cuerpo + m.group(3)

    pagina = BLOQUE.sub(reemplazo, pagina)
    faltan = {"FAQPage", "Dataset", "SoftwareApplication"} - vistos
    if faltan:
        raise SystemExit(f"la home no trae {', '.join(sorted(faltan))} en su JSON-LD")
    return pagina


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="no escribe; exit 1 si la home no está al día")
    a = ap.parse_args()
    d = json.loads(MODELS.read_text(encoding="utf-8"))
    antes = INDEX.read_text(encoding="utf-8")
    nuevo = generar(antes, d)
    c = cifras(d)
    if a.check:
        if nuevo != antes:
            print("❌ el JSON-LD o las meta de la home no salen de su FAQ y de models.json: "
                  "corre `python benchmarks/generate_home_jsonld.py`")
            return 1
        print(f"✅ la home declara su FAQ visible y {c['modelos']} modelos, {c['rankeados']} rankeados, {c['tests']} tests")
        return 0
    if nuevo != antes:
        INDEX.write_text(nuevo, encoding="utf-8")
    print(f"home: FAQ de {len(faq_visible(nuevo))} preguntas · {c['modelos']} modelos, "
          f"{c['rankeados']} rankeados, {c['tests']} tests" + (" (sin cambios)" if nuevo == antes else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
