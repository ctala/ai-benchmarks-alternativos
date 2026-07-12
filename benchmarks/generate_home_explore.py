#!/usr/bin/env python3
"""
Inyecta en el home (docs/index.html) el bloque "Explora" con enlaces a las páginas pSEO.

POR QUE EXISTE
--------------
El home enlazaba a los rankings desde el nav y a NADA más. Las 35 comparaciones y las
6 páginas de familia estaban huérfanas: sin un solo enlace interno desde la página más
autoritativa del sitio.

Y no eran páginas menores. /claude-vs-chatgpt/ vale **2.480 búsquedas/mes** (ES+MX,
DataForSEO jul-2026) y tenía 0 impresiones y 0 enlaces entrantes. El problema nunca fue
falta de páginas: era que nadie podía llegar a ellas — ni Google ni una persona.

Se genera (no se escribe a mano) para que al agregar una página nueva aparezca sola.
Prioridad = volumen de búsqueda verificado, no intuición.

Uso:
    python benchmarks/generate_home_explore.py
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
INDEX = DOCS / "index.html"

START = "<!-- AUTO-EXPLORE-START -->"
END = "<!-- AUTO-EXPLORE-END -->"

# Volumen verificado con DataForSEO (ES 2724 + MX 2484, es, 12-jul-2026).
# Ordenado por demanda real. `None` = sin volumen medido para la frase exacta;
# se incluye igual si la intención es clara, pero va después de las que sí tienen.
COMPARISONS = [
    ("claude-vs-chatgpt", "Claude vs ChatGPT", 2480),
    ("gemini-vs-chatgpt", "Gemini vs ChatGPT", 2180),
    ("deepseek-vs-chatgpt", "DeepSeek vs ChatGPT", 470),
    ("deepseek-vs-claude", "DeepSeek vs Claude", 90),
    ("gemini-vs-claude", "Gemini vs Claude", None),
    ("grok-vs-chatgpt", "Grok vs ChatGPT", 140),
    ("qwen-vs-llama", "Qwen vs Llama", None),
    ("gpt-5.6-vs-claude-opus-4-8", "GPT-5.6 vs Claude Opus 4.8", None),
]

FAMILIES = [
    ("claude-haiku-sonnet-opus", "Claude", "¿Haiku, Sonnet u Opus?", 720),
    ("minimax-m2-7-o-m3", "MiniMax", "¿M2.7 o M3?", 530),
    ("gpt-5.6-luna-terra-sol", "GPT-5.6", "¿Luna, Terra o Sol?", None),
    ("deepseek-v4-flash-o-r1", "DeepSeek", "¿V4 Flash, R1 o Pro?", None),
    ("gemini-flash-o-pro", "Gemini", "¿Flash o Pro?", None),
    ("grok-4-1-vs-4-5", "Grok", "¿Cuál de las versiones?", None),
]

ALTERNATIVES = [
    ("alternativas-chatgpt", "Alternativas a ChatGPT"),
    ("alternativas-claude", "Alternativas a Claude"),
    ("alternativas-gemini", "Alternativas a Gemini"),
    ("alternativas-deepseek", "Alternativas a DeepSeek"),
]


def build() -> str:
    def exists(slug):
        return (DOCS / slug / "index.html").exists()

    comps = "".join(
        f'<a class="ex-card" href="/{s}/"><span class="ex-name">{n}</span></a>'
        for s, n, _ in COMPARISONS if exists(s)
    )
    fams = "".join(
        f'<a class="ex-card ex-family" href="/{s}/">'
        f'<span class="ex-name">{fam}</span><span class="ex-q">{q}</span></a>'
        for s, fam, q, _ in FAMILIES if exists(s)
    )
    alts = "".join(
        f'<a class="ex-chip" href="/{s}/">{n}</a>'
        for s, n in ALTERNATIVES if exists(s)
    )

    return f"""{START}
  <section class="explore">
    <h2>¿No sabes por dónde empezar?</h2>
    <p class="explore-lead">La calculadora es para cuando ya sabes qué buscas. Si todavía no,
    empieza por una de estas — cada una termina en una recomendación concreta, no en una tabla.</p>

    <h3 class="ex-h3">¿Qué versión de cada modelo elijo?</h3>
    <p class="ex-note">El proveedor te vende una escalera: más caro, mejor. Acá auditamos si es cierto.</p>
    <div class="ex-grid">{fams}</div>

    <h3 class="ex-h3">Cara a cara</h3>
    <div class="ex-grid ex-grid-compact">{comps}</div>

    <h3 class="ex-h3">Buscas reemplazar el que usas hoy</h3>
    <div class="ex-chips">{alts}</div>
  </section>
{END}"""


def main():
    html = INDEX.read_text()
    block = build()
    if START in html and END in html:
        import re
        html = re.sub(rf"{re.escape(START)}.*?{re.escape(END)}", block, html, flags=re.DOTALL)
    else:
        raise SystemExit(
            f"ERROR: faltan los marcadores {START} / {END} en docs/index.html.\n"
            "Agrégalos donde deba ir el bloque (después de la calculadora)."
        )
    INDEX.write_text(html)
    n = block.count('class="ex-card') + block.count('class="ex-chip')
    print(f"OK: docs/index.html — bloque Explora con {n} enlaces a páginas pSEO")


if __name__ == "__main__":
    main()
