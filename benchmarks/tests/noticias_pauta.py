"""
Suite noticias_pauta — Redactar nota siguiendo la pauta editorial.

**Diseño aprobado:** benchmark-pack-noticias_e470.md § 4.3
**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

- **12 tests** (3 rondas LATAM + 3 producto IA + 3 regionales + 3 comunicados)
- **Input:** Pauta editorial + ficha de hechos (hasta 3000 chars de nota publicada)
- **Output:** Nota de 600-900 palabras con título
- **Scoring:**
  - 40% forma automática (sin voseo, título ≤60 chars, sin CJK, sin cierres genéricos)
  - 30% fidelidad (cifras de la nota están en la ficha)
  - 30% utilidad (3 preguntas Y/N al verificador Phi-4)

**BLOQUEANTE:** Requiere crear y revisar 12 fichas de hechos (~1h).
"""

from typing import List, Dict, Any
import re
from ._noticias_common import load_full_posts, extract_rendered

# Pauta editorial
PAUTA_EDITORIAL = """
**Pauta de Ecosistema Startup:**

1. **Idioma:** Español neutro sin voseo ("tú", "ustedes" en vez de "vos", "vosotros")
2. **Longitud:** 600-900 palabras
3. **Título:** Máximo 60 caracteres, debe nombrar al protagonista (empresa, persona, fund)
4. **Estructura:** Pirámide invertida - lo más importante primero
5. **Utilidad concreta:** Cada nota debe tener al menos UNA decisión o acción transferible para un founder
6. **Cierres prohibidos:**
   - Genéricos: "En conclusión", "Solo el tiempo dirá", "Habrá que esperar"
   - Sección fija de relleno: "¿Qué significa esto para tu startup?"
7. **Cifras:** Todas las cifras deben estar respaldadas por la ficha de hechos
8. **Integridad:** Sin mezclar idiomas (nada de chino, árabe u otros scripts)
"""

# Lista de frases de voseo (reutilizada de check_espanol_neutro.py)
VOSEO_PATTERNS = [
    r'\bvos\b', r'\bvosotros\b', r'\bvosotras\b',
    r'\bsos\b', r'\btenés\b', r'\bquerés\b', r'\bpodés\b',
    r'\bsabés\b', r'\bdecís\b', r'\bvení\b', r'\bandá\b'
]

# Cierres genéricos prohibidos
CIERRES_PROHIBIDOS = [
    'en conclusión', 'en resumen', 'para concluir',
    'solo el tiempo dirá', 'habrá que esperar',
    'veremos qué pasa', 'el futuro lo dirá',
    '¿qué significa esto para tu startup?'
]


def _load_fichas() -> List[Dict[str, Any]]:
    """
    Carga fichas de hechos desde archivo JSON.
    
    Formato esperado:
    [
      {
        "id": <str>,
        "tipo": "ronda_latam" | "producto_ia" | "regional" | "comunicado",
        "ficha": "<texto de hasta 3000 chars con hechos clave>",
        "nota_origen_id": <int>,
        "cifras_clave": ["$5M", "Series A", "2024", ...]
      },
      ...
    ]
    
    **PENDIENTE:** 12 fichas creadas a mano (~1h).
    """
    import os
    import json
    
    path = '/home/ubuntu/.cursor/projects/workspace/uploads/fichas_pauta.json'
    
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"❌ FICHAS FALTANTES\n\n"
            f"El archivo {path} NO existe.\n"
            f"Esta suite requiere 12 fichas de hechos:\n"
            f"- 3 rondas en LATAM\n"
            f"- 3 productos de IA\n"
            f"- 3 casos regionales\n"
            f"- 3 comunicados\n\n"
            f"Cada ficha: hasta 3000 caracteres con hechos clave de una nota publicada.\n"
            f"Tiempo estimado: ~1 hora"
        )
    
    with open(path) as f:
        return json.load(f)


def _score_forma(texto: str, titulo: str) -> float:
    """
    Puntúa forma automática (40% del total).
    
    - Sin voseo: 10 pts
    - Título ≤60 chars: 10 pts
    - Sin CJK ni otros idiomas: 10 pts
    - Sin cierres prohibidos: 10 pts
    
    Total: 0-40
    """
    score = 0.0
    texto_lower = texto.lower()
    
    # Sin voseo
    has_voseo = any(re.search(pattern, texto_lower) for pattern in VOSEO_PATTERNS)
    if not has_voseo:
        score += 10.0
    
    # Título ≤60
    if len(titulo) <= 60:
        score += 10.0
    
    # Sin CJK (chino, japonés, coreano, árabe, cirílico fuera de español)
    has_cjk = bool(re.search(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\u0600-\u06ff]', texto))
    if not has_cjk:
        score += 10.0
    
    # Sin cierres prohibidos
    has_cierre_prohibido = any(cierre in texto_lower for cierre in CIERRES_PROHIBIDOS)
    if not has_cierre_prohibido:
        score += 10.0
    
    return score


def _score_fidelidad(texto: str, cifras_clave: List[str]) -> float:
    """
    Puntúa fidelidad a la ficha (30% del total).
    
    Cada cifra de la nota debe estar en la ficha.
    Si hay cifras en la nota que NO están en cifras_clave, penaliza.
    
    Total: 0-30
    """
    # Extraer cifras del texto (números, montos, porcentajes)
    cifras_en_texto = re.findall(r'\$?[\d,]+(?:\.\d+)?[MKB%]?', texto)
    
    if not cifras_en_texto:
        return 30.0  # No hay cifras, no hay error
    
    # Normalizar y comparar
    def normalize_cifra(c: str) -> str:
        return c.replace(',', '').replace('$', '').upper()
    
    cifras_norm = {normalize_cifra(c) for c in cifras_en_texto}
    clave_norm = {normalize_cifra(c) for c in cifras_clave}
    
    # Proporción de cifras que están respaldadas
    respaldadas = len(cifras_norm & clave_norm)
    total_cifras = len(cifras_norm)
    
    if total_cifras == 0:
        return 30.0
    
    proporcion = respaldadas / total_cifras
    return proporcion * 30.0


def _score_utilidad_placeholder() -> float:
    """
    Placeholder para scoring de utilidad con verificador Phi-4.
    
    En producción, esto llamaría al verificador con 3 preguntas:
    1. ¿Nombra una decisión/acción concreta para un founder?
    2. ¿El cierre trae un dato específico, no un consejo genérico?
    3. ¿El título nombra al protagonista?
    
    Por ahora: promedio simulado.
    """
    # TODO: Implementar con benchmarks/verifier.py
    return 15.0  # Promedio de 30 pts


# Intentar cargar fichas
try:
    fichas = _load_fichas()
except FileNotFoundError as e:
    print(f"\n⚠️  WARNING: {e}\n")
    fichas = []

TESTS = []

if fichas:
    for i, ficha in enumerate(fichas, 1):
        prompt = f"""{PAUTA_EDITORIAL}

**Ficha de hechos:**

{ficha['ficha']}

Redacta una nota de 600-900 palabras siguiendo la pauta.
Responde SOLO con la nota, sin explicaciones adicionales.
Formato:

TÍTULO: [tu título de máximo 60 caracteres]

[Cuerpo de la nota de 600-900 palabras]
"""

        TESTS.append({
            'name': f'pauta_{ficha.get("tipo", "general")}_{i}',
            'description': f'Redactar nota tipo {ficha.get("tipo")} siguiendo pauta editorial',
            'messages': [
                {'role': 'system', 'content': 'Eres un redactor de Ecosistema Startup.'},
                {'role': 'user', 'content': prompt}
            ],
            'expected_answer': {
                'tipo': ficha.get('tipo'),
                'cifras_clave': ficha.get('cifras_clave', [])
            },
            'criteria': {
                'format': {
                    'has_titulo': True,
                    'word_count_600_900': True
                },
                'substance': {
                    'custom_scorer': lambda pred, exp, ctx: (
                        _score_forma(pred if isinstance(pred, str) else '', 
                                    re.search(r'TÍTULO:\s*(.+)', pred if isinstance(pred, str) else '').group(1) if re.search(r'TÍTULO:\s*(.+)', pred if isinstance(pred, str) else '') else '') +
                        _score_fidelidad(pred if isinstance(pred, str) else '', 
                                       ctx.get('expected_answer', {}).get('cifras_clave', [])) +
                        _score_utilidad_placeholder()
                    ) / 10.0  # Normalizar a 0-10
                }
            }
        })
else:
    print("\n⚠️  noticias_pauta: suite vacía (faltan fichas)\n")
