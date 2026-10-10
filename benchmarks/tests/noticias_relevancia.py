"""
Suite noticias_relevancia — Filtrar notas según criterio editorial.

**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

Mide si el modelo puede puntuar y filtrar notas según el criterio editorial de
Ecosistema Startup: startups, VC, emprendimiento, tecnología para negocios.

Entrada: criterio + 10 notas (título + excerpt ~150 chars)
Salida: JSON [{id, decision: KEEP|SKIP, categoria, puntaje: 1-10}, ...]

Scoring:
- Decisión correcta (KEEP/SKIP): +1 punto por acierto
- Puntaje en rango correcto: +0.5 si está a ±2 del esperado
- Total: suma / (N_notas * 1.5) → normalizado 0-10
"""

from typing import List, Dict, Any
import random
from ._noticias_data import load_posts_14d, extract_text


# Criterio editorial de Eco (simplificado)
CRITERIO_ECO = """
Ecosistema Startup es un medio especializado en:
- Startups (inversión, exits, pivotes, fracasos)
- Venture Capital y fondos (levantamientos, retornos, estrategias)
- Emprendimiento (metodologías, casos, ecosistemas regionales)
- Tecnología aplicada a negocios (IA, SaaS, herramientas para empresas)

KEEP si la nota encaja en alguna categoría. SKIP si:
- Es tecnología consumer sin ángulo de negocio (ej: iPhone 17 Pro, specs de hardware)
- Es gaming sin ángulo de startups/VC (ej: GTA 6, Gears of War)
- Es finanzas macro/bolsa sin link a startups (ej: análisis de bonos, forex)
- Es política o sociedad sin conexión al ecosistema

Categorías: startup_funding, vc_strategy, entrepreneurship, business_tech, AI_for_business
"""


def _score_relevancia(posts_sample: List[Dict], seed: int) -> List[Dict]:
    """Genera scoring manual simulado para los posts."""
    # En producción real, esto sería etiquetado humano
    # Aquí uso heurísticas basadas en keywords del título
    
    startup_kw = ['startup', 'emprendedor', 'fundar', 'inversi', 'vc', 'capital', 'levanta', 'fondo']
    tech_biz_kw = ['ia', 'inteligencia artificial', 'saas', 'api', 'cloud', 'ciberseguridad', 'agentes']
    skip_kw = ['iphone', 'gta', 'gears of war', 'bonos', 'fiscal', 'acciones', 'elecciones']
    
    scored = []
    for p in posts_sample:
        title_lower = extract_text(p['title']).lower()
        
        # Detectar SKIPs obvios
        if any(kw in title_lower for kw in skip_kw):
            scored.append({
                'id': p['id'],
                'decision': 'SKIP',
                'puntaje': random.randint(1, 4)
            })
            continue
        
        # Detectar KEEPs
        if any(kw in title_lower for kw in startup_kw):
            scored.append({
                'id': p['id'],
                'decision': 'KEEP',
                'puntaje': random.randint(7, 10)
            })
        elif any(kw in title_lower for kw in tech_biz_kw):
            scored.append({
                'id': p['id'],
                'decision': 'KEEP',
                'puntaje': random.randint(6, 9)
            })
        else:
            # Ambiguo: 50/50
            keep = random.Random(seed + p['id']).choice([True, False])
            scored.append({
                'id': p['id'],
                'decision': 'KEEP' if keep else 'SKIP',
                'puntaje': random.randint(5, 7)
            })
    
    return scored


def _calculate_relevancia_score(
    predicted: List[Dict],
    expected: List[Dict]
) -> float:
    """
    Calcula score de relevancia.
    
    - Decisión correcta (KEEP/SKIP): +1
    - Puntaje en rango (±2): +0.5
    - Max por nota: 1.5
    """
    pred_by_id = {p['id']: p for p in predicted}
    
    total_score = 0.0
    for exp in expected:
        pred = pred_by_id.get(exp['id'], {})
        
        # Decisión
        if pred.get('decision') == exp['decision']:
            total_score += 1.0
        
        # Puntaje
        pred_score = pred.get('puntaje', 0)
        exp_score = exp['puntaje']
        if abs(pred_score - exp_score) <= 2:
            total_score += 0.5
    
    # Normalizar a 0-10
    max_score = len(expected) * 1.5
    return (total_score / max_score) * 10 if max_score > 0 else 0.0


# Cargar datos
posts_14d = load_posts_14d()
random.seed(2026)

# Seleccionar 6 muestras de 10 notas
TESTS = []

for i in range(1, 7):
    # Sample de 10 notas
    sample = random.sample(posts_14d, 10)
    expected_scores = _score_relevancia(sample, seed=2026+i)
    
    # Construir prompt
    posts_text = []
    for p in sample:
        title = extract_text(p['title'])
        excerpt = extract_text(p.get('excerpt', ''))[:150]
        posts_text.append(f"ID {p['id']}: {title}\n{excerpt}...\n")
    
    prompt = f"""{CRITERIO_ECO}

Evalúa estas 10 notas:

{chr(10).join(posts_text)}

Responde en JSON estricto:
[
  {{"id": <int>, "decision": "KEEP|SKIP", "categoria": "<string>", "puntaje": <1-10>}},
  ...
]
"""

    TESTS.append({
        'name': f'relevancia_{i}',
        'description': f'Filtrar 10 notas según criterio editorial de Eco',
        'messages': [
            {'role': 'system', 'content': 'Eres un editor que filtra notas según criterio editorial.'},
            {'role': 'user', 'content': prompt}
        ],
        'expected_answer': expected_scores,
        'criteria': {
            'format': {
                'is_list': True,
                'list_length': 10,
                'required_keys': ['id', 'decision', 'puntaje']
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_relevancia_score(
                    pred if isinstance(pred, list) else [],
                    expected_scores
                )
            }
        }
    })
