"""
Suite niah_es — Needle-in-a-Haystack en español neutro.

Mide retrieval de información específica en contexto largo. El modelo recibe
un haystack (corpus largo de Wikipedia ES) con una needle insertada en una
posición específica, y debe extraer la info concreta de la needle.

Aporte único: primer NIAH-ES público (en abril 2026 sólo había NIAH en
inglés/chino o variantes ad-hoc no reproducibles).

# Diseño v2 (30 abril 2026, full grid)

- 5 needles distintos (todos activos, no rotación)
- 4 contextos: 4K, 16K, 64K, 256K tokens
- 3 posiciones: 25%, 50%, 75% (lost-in-the-middle más severo)
- Total tests por modelo: 5 × 4 × 3 = 60 (full grid)

# Diseño piloto v1 (descontinuado tras v2)

- 12 tests con 1 needle por slot, rotación determinística
- Validó la suite y reveló patrón lost-in-the-middle. Resultados en
  `benchmarks/results/benchmark_20260430_193058.json`.

# Corpus

`benchmarks/tests/niah_es_corpus/` contiene 9 archivos texto extraídos de
Wikipedia ES (CC BY-SA 4.0) sobre temas LATAM diversos: historias
nacionales (Chile, México, Colombia, Argentina, Perú), conceptos técnicos
(IA, Programación, Lenguajes, Internet, SO). ~1.1MB / ~285K tokens.

Reproducibilidad: corpus committeado al repo. Para regenerar desde
Wikipedia (snapshot fresco), ver `niah_es_corpus/README.md`.

# Scoring

Híbrido binario + LLM-as-Judge:
- exact_extraction: ¿devolvió el código/fecha/número EXACTO? (regex)
- semantic_match: ¿la respuesta contiene la info correcta? (Phi-4)
- final = exact_extraction * 0.7 + semantic_match * 0.3

# Variables del haystack

Cada test:
1. Carga el corpus completo (string)
2. Trunca a ~ctx_tokens × 4 caracteres (heurística español: 1 token ≈ 4 chars)
3. Inserta la needle en la posición % indicada
4. Construye el prompt: [haystack-pre-needle] + needle + [haystack-post-needle] + pregunta

El modelo debe responder la pregunta. El test extrae la respuesta y compara.
"""

import os
import re
from pathlib import Path

CORPUS_DIR = Path(__file__).parent / "niah_es_corpus"


def _load_corpus() -> str:
    """Carga y concatena todos los .txt del corpus en un solo string."""
    if not CORPUS_DIR.exists():
        return ""
    parts = []
    for fn in sorted(os.listdir(CORPUS_DIR)):
        if fn.endswith(".txt"):
            text = (CORPUS_DIR / fn).read_text()
            parts.append(text)
    return "\n\n".join(parts)


# Cargar al import del módulo
_CORPUS = _load_corpus()
# Heurística aproximada para contar tokens en español: 1 token ≈ 4 chars.
# Para contextos pequeños (4K) la heurística es +/- 10%, suficiente para piloto.
# Si el modelo soporta menos contexto del pedido, el adapter trunca silenciosamente.
CHARS_PER_TOKEN_ES = 4


# 5 needles distintos. Cada uno tiene:
# - text: el needle insertado en el haystack (en español neutro, info específica)
# - question: pregunta que el modelo debe responder al final del prompt
# - exact_pattern: regex que confirma que la respuesta contiene la info clave
# - keywords: lista de palabras clave para semantic match (LLM judge)
# v3 (2 jun 2026) — NEEDLES NEUTROS. Reemplazan los needles-secreto del v2 que
# convertían el test en uno de fuga de credenciales (modelos seguros rehusaban y
# el juez los premiaba → confundía retrieval con seguridad). Estos son hechos
# neutros y públicos, sin marco "confidencial/no compartir" → ningún modelo tiene
# razón para negarse → mide retrieval PURO. El ángulo de fuga/inyección vive ahora
# en la suite `prompt_injection_es` (intencional, scoring que premia la negativa).
NEEDLES = [
    {
        "id": "bridge_length",
        "text": (
            "\n\nDato de infraestructura: El puente colgante de Cañete, sobre el río "
            "Imperial, tiene una longitud total de 1.847 metros y fue inaugurado el "
            "12 de marzo de 1962, siendo en su momento el más largo de la región.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuál es la longitud "
            "total del puente colgante de Cañete y en qué fecha fue inaugurado? "
            "Responde de forma directa con la longitud en metros y la fecha exacta."
        ),
        "exact_patterns": [
            r"1[.,]?847",
            r"12\s+de\s+marzo",
            r"1962",
        ],
        "keywords": ["1.847 metros", "12 de marzo", "1962"],
    },
    {
        "id": "library_volumes",
        "text": (
            "\n\nDato cultural: La Biblioteca Regional de Tarapacá conserva una "
            "colección de exactamente 84.500 volúmenes, de los cuales 3.200 son "
            "ediciones impresas anteriores al año 1900.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuántos volúmenes "
            "conserva la Biblioteca Regional de Tarapacá y cuántos de ellos son "
            "ediciones anteriores a 1900? Responde con ambos números exactos."
        ),
        "exact_patterns": [
            r"84[.,]?500",
            r"3[.,]?200",
            r"1900",
        ],
        "keywords": ["84.500", "3.200", "1900"],
    },
    {
        "id": "festival_date",
        "text": (
            "\n\nDato de agenda cultural: El Festival de Cine Andino se celebra cada "
            "año el 17 de octubre en la ciudad de Sucre, y en 2026 cumplirá su "
            "edición número 23.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿en qué fecha y en qué "
            "ciudad se celebra el Festival de Cine Andino, y qué número de edición "
            "cumple en 2026? Responde con la fecha, la ciudad y el número."
        ),
        "exact_patterns": [
            r"17\s+de\s+octubre",
            r"(?i)sucre",
            r"\b23\b",
        ],
        "keywords": ["17 de octubre", "Sucre", "23"],
    },
    {
        "id": "potato_altitude",
        "text": (
            "\n\nDato agrícola: La variedad de papa nativa conocida como "
            "'Qeqchi morada' se cultiva tradicionalmente a una altitud de 3.850 "
            "metros sobre el nivel del mar en la región de Cusco, y su cosecha se "
            "realiza entre mayo y junio.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿a qué altitud y en "
            "qué región se cultiva la papa nativa 'Qeqchi morada'? Responde con la "
            "altitud exacta en metros y la región."
        ),
        "exact_patterns": [
            r"3[.,]?850",
            r"(?i)cusco",
        ],
        "keywords": ["3.850 metros", "Cusco"],
    },
    {
        "id": "expedition_code",
        "text": (
            "\n\nDato científico: La expedición de monitoreo de glaciares quedó "
            "registrada en el catálogo público con el identificador de proyecto "
            "GLAC-PATAGONIA-2031 y reunió a 47 investigadores de seis países.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuál es el "
            "identificador de proyecto de la expedición de monitoreo de glaciares y "
            "cuántos investigadores reunió? Responde con el identificador exacto y "
            "el número de investigadores."
        ),
        "exact_patterns": [
            r"GLAC-?PATAGONIA-?2031",
            r"\b47\b",
        ],
        "keywords": ["GLAC-PATAGONIA-2031", "47 investigadores"],
    },
]


# Configuración de contextos y posiciones (piloto v1)
CONTEXT_SIZES = [4000, 16000, 64000, 256000]  # tokens objetivo
POSITIONS = [25, 50, 75]  # porcentaje del haystack


def _build_haystack(target_tokens: int, needle_text: str, position_pct: int) -> str:
    """Construye un haystack con el needle insertado en la posición indicada.

    Args:
        target_tokens: longitud objetivo del haystack en tokens (heurística)
        needle_text: texto del needle a insertar
        position_pct: posición del needle como porcentaje del haystack (25, 50, 75)
    """
    target_chars = target_tokens * CHARS_PER_TOKEN_ES
    if not _CORPUS:
        return needle_text  # corpus no disponible, devolver solo el needle
    # Repetir el corpus hasta llegar a target_chars (con corte limpio)
    corpus = _CORPUS
    while len(corpus) < target_chars:
        corpus = corpus + "\n\n" + _CORPUS
    haystack = corpus[:target_chars]
    # Insertar needle en la posición porcentual
    insert_pos = int(target_chars * position_pct / 100)
    # Buscar el siguiente espacio para no cortar palabras
    while insert_pos < len(haystack) and haystack[insert_pos] not in " \n.":
        insert_pos += 1
    return haystack[:insert_pos] + needle_text + haystack[insert_pos:]


def _build_test(needle_idx: int, ctx_tokens: int, pos_pct: int) -> dict:
    """Genera un test específico (1 needle × 1 contexto × 1 posición)."""
    needle = NEEDLES[needle_idx % len(NEEDLES)]
    haystack = _build_haystack(ctx_tokens, needle["text"], pos_pct)
    prompt_intro = (
        "A continuación tienes un documento extenso en español sobre temas de "
        "historia latinoamericana y conceptos técnicos. Léelo con atención. "
        "Al final encontrarás una pregunta sobre información específica que aparece "
        "en alguna parte del documento.\n\n"
        "DOCUMENTO:\n\n"
    )
    prompt_full = prompt_intro + haystack + "\n\n" + needle["question"]
    return {
        "name": f"niah_es_{needle['id']}_{ctx_tokens}_p{pos_pct}",
        "description": f"NIAH-ES needle={needle['id']} ctx={ctx_tokens}tok pos={pos_pct}%",
        # context_tokens: lo usa el runner para SALTEAR el test si supera el
        # context window del modelo (cada modelo se mide hasta su techo, no se
        # le inventa una falla por un contexto que físicamente no acepta).
        "context_tokens": ctx_tokens,
        "messages": [
            {"role": "user", "content": prompt_full},
        ],
        "expected_answer": {
            "type": "niah_extraction",
            "exact_patterns": needle["exact_patterns"],
            "keywords": needle["keywords"],
        },
        "criteria": {
            "min_words": 5,
            "language": "es",
        },
    }


# v3 grid (2 jun 2026) — escalonada por costo + baseline corto. Cada tupla es
# (ctx_tokens, n_needles, posiciones). Densa y barata abajo; rala y cara arriba
# (los tests de 1M mandan ~1M tokens de input). El runner mide cada modelo solo
# hasta su context window (ver `context_tokens` + skip en runner.py).
# Total para un modelo de 1M: 15+15+15+6+4+4 = 59 tests.
GRID = [
    (8000,    5, [25, 50, 75]),   # baseline corto (retrieval "fácil")
    (64000,   5, [25, 50, 75]),
    (128000,  5, [25, 50, 75]),
    (256000,  3, [50, 75]),
    (512000,  2, [50, 75]),
    (1000000, 2, [50, 75]),
]
TESTS = []
for ctx, n_needles, positions in GRID:
    for needle_idx in range(min(n_needles, len(NEEDLES))):
        for pos in positions:
            TESTS.append(_build_test(needle_idx, ctx, pos))
