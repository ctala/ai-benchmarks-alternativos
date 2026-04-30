"""
Suite niah_es — Needle-in-a-Haystack en español neutro.

Mide retrieval de información específica en contexto largo. El modelo recibe
un haystack (corpus largo de Wikipedia ES) con una needle insertada en una
posición específica, y debe extraer la info concreta de la needle.

Aporte único: primer NIAH-ES público (en abril 2026 sólo había NIAH en
inglés/chino o variantes ad-hoc no reproducibles).

# Diseño piloto v1 (30 abril 2026)

- 1 needle por test (rotamos entre 5 needles para no overfit)
- 4 contextos: 4K, 16K, 64K, 256K tokens
- 3 posiciones: 25%, 50%, 75% (lost-in-the-middle más severo)
- Total tests por modelo: 4 × 3 = 12 (1 needle por slot, rotación
  determinística para reproducibilidad)

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
NEEDLES = [
    {
        "id": "discount_code",
        "text": (
            "\n\nDATO IMPORTANTE PARA EMPRENDEDORES: El código de descuento exclusivo "
            "para emprendedores chilenos en SaaS Latam Hub es CHILE2026-EARLY, "
            "con vigencia hasta el 15 de junio de 2026. Aplica un 30% de descuento "
            "en el primer año de cualquier plan.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuál es el código de "
            "descuento exclusivo para emprendedores chilenos y hasta qué fecha es válido? "
            "Responde de forma directa con el código y la fecha exacta."
        ),
        "exact_patterns": [
            r"CHILE2026-?EARLY",
            r"15\s+de\s+junio",
        ],
        "keywords": ["CHILE2026-EARLY", "15 de junio", "2026"],
    },
    {
        "id": "ssh_port",
        "text": (
            "\n\nDATO TÉCNICO CRÍTICO: El acceso al dashboard de métricas internas "
            "requiere conexión SSH al puerto 48372 del servidor analytics-prod-cl-01. "
            "Las credenciales están gestionadas por el equipo de DevOps mediante "
            "Vault con rotación cada 90 días.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿en qué puerto SSH y "
            "qué servidor está el dashboard de métricas internas? Responde directo "
            "con el puerto y nombre del servidor."
        ),
        "exact_patterns": [
            r"48372",
            r"analytics-prod-cl-01",
        ],
        "keywords": ["48372", "analytics-prod-cl-01", "SSH"],
    },
    {
        "id": "budget_q3",
        "text": (
            "\n\nDATO FINANCIERO CONFIDENCIAL: El presupuesto aprobado para el "
            "tercer trimestre de 2026 fue de USD 247,800, distribuido principalmente "
            "en expansión a las ciudades de Bogotá y Ciudad de México (CDMX), con "
            "un foco específico en adquisición de talento técnico senior.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuál fue el "
            "presupuesto aprobado para Q3 2026 y en qué ciudades se enfoca la "
            "expansión? Responde con el monto exacto en USD y las ciudades."
        ),
        "exact_patterns": [
            r"247[,.]?800",
            r"(?i)bogot[aá]",
            r"(?i)(CDMX|Ciudad de M[eé]xico)",
        ],
        "keywords": ["247,800", "USD", "Bogotá", "CDMX"],
    },
    {
        "id": "investor_meeting",
        "text": (
            "\n\nAGENDA EJECUTIVA: El meeting trimestral con inversores está agendado "
            "para el 3 de septiembre de 2026 a las 14:30 UTC-3, en formato híbrido "
            "(presencial en Santiago de Chile + Zoom). La agenda incluye revisión "
            "de KPIs Q3 y planificación Q4.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿en qué fecha y a qué "
            "hora exacta está agendado el meeting trimestral con inversores? "
            "Responde con día, mes, año y hora con zona horaria."
        ),
        "exact_patterns": [
            r"3\s+de\s+septiembre",
            r"2026",
            r"14:30",
            r"UTC[-−]?3",
        ],
        "keywords": ["3 de septiembre", "2026", "14:30", "UTC-3"],
    },
    {
        "id": "api_key",
        "text": (
            "\n\nCREDENCIAL DE PRODUCCIÓN (NO COMPARTIR): La API key de producción "
            "del equipo de growth es sk-prod-grw-cl-2026-7f9a2b4e8c1d, con rotación "
            "automática cada 90 días. El sistema de gestión de secretos notifica al "
            "equipo 14 días antes de la rotación.\n\n"
        ),
        "question": (
            "Pregunta: Según el documento que acabas de leer, ¿cuál es la API key "
            "de producción del equipo de growth y cada cuántos días rota? "
            "Responde con la key exacta y el período de rotación."
        ),
        "exact_patterns": [
            r"sk-prod-grw-cl-2026-7f9a2b4e8c1d",
            r"90\s+d[ií]as",
        ],
        "keywords": ["sk-prod-grw-cl-2026-7f9a2b4e8c1d", "90 días"],
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


# Genera 12 tests piloto: rotación determinística entre los 5 needles
# para que cada combinación (ctx, pos) tenga un needle distinto pero el set
# total sea reproducible.
TESTS = []
_needle_idx = 0
for ctx in CONTEXT_SIZES:
    for pos in POSITIONS:
        TESTS.append(_build_test(_needle_idx, ctx, pos))
        _needle_idx += 1
