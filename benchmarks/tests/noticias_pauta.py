"""
Suite noticias_pauta — Sugerir pauta editorial y detección de tendencias.

**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

Mide si el modelo puede:
1. Identificar temas/tendencias recurrentes en un flujo de notas
2. Sugerir pauta editorial (qué temas profundizar, qué ángulos faltan)
3. Detectar gaps de cobertura

Entrada: 20-30 notas de un período (títulos + excerpts)
Salida: JSON {
  "tendencias": [{tema, frecuencia, ejemplos: [ids]}],
  "sugerencias": [{tema, razon, angulo_propuesto}],
  "gaps": [temas_no_cubiertos]
}

Scoring: evaluación humana simulada (criterios heurísticos)
"""

from typing import List, Dict, Any
import random
from collections import Counter
from ._noticias_data import load_posts_14d, extract_text


def _extract_topics(posts: List[Dict]) -> Dict[str, List[int]]:
    """Extrae temas de posts (heurística por keywords)."""
    topics = {
        'IA y agentes': [],
        'Inversión y funding': [],
        'Ciberseguridad': [],
        'Regulación y fiscalía': [],
        'Ecosistema regional': [],
        'Tecnología empresarial': []
    }
    
    keywords_map = {
        'IA y agentes': ['ia', 'inteligencia artificial', 'agentes', 'gpt', 'openai', 'llm'],
        'Inversión y funding': ['levanta', 'millones', 'inversi', 'fondo', 'capital', 'vc'],
        'Ciberseguridad': ['ciberseguridad', 'hackeo', 'seguridad', 'filtró', 'breach'],
        'Regulación y fiscalía': ['fiscal', 'regulaci', 'ley', 'gobierno', 'multa'],
        'Ecosistema regional': ['españ', 'méxico', 'chile', 'latam', 'silicon valley', 'startup.*española'],
        'Tecnología empresarial': ['saas', 'cloud', 'api', 'herramienta', 'software']
    }
    
    for p in posts:
        title_lower = extract_text(p['title']).lower()
        for topic, keywords in keywords_map.items():
            if any(kw in title_lower for kw in keywords):
                topics[topic].append(p['id'])
    
    return topics


def _calculate_pauta_score(
    predicted: Dict,
    expected_topics: Dict[str, List[int]]
) -> float:
    """
    Score heurístico para pauta.
    
    - Identificó tendencias principales: hasta 5 pts
    - Sugerencias razonables: hasta 3 pts
    - Detectó gaps: hasta 2 pts
    """
    score = 0.0
    
    # Tendencias identificadas
    pred_tendencias = predicted.get('tendencias', [])
    if len(pred_tendencias) >= 3:
        score += 2.0
    if len(pred_tendencias) >= 5:
        score += 1.5
    
    # Frecuencias coherentes
    for tend in pred_tendencias:
        if tend.get('frecuencia', 0) >= 3:
            score += 0.5
    
    score = min(score, 5.0)
    
    # Sugerencias
    pred_sugerencias = predicted.get('sugerencias', [])
    if len(pred_sugerencias) >= 2:
        score += 1.5
    if len(pred_sugerencias) >= 4:
        score += 1.5
    
    # Gaps
    pred_gaps = predicted.get('gaps', [])
    if len(pred_gaps) >= 1:
        score += 1.0
    if len(pred_gaps) >= 3:
        score += 1.0
    
    return min(score, 10.0)


# Cargar datos
posts_14d = load_posts_14d()
random.seed(2026)

TESTS = []

for i in range(1, 5):
    # Sample de 25 notas
    sample = random.sample(posts_14d, 25)
    expected_topics = _extract_topics(sample)
    
    # Construir prompt
    posts_text = []
    for p in sample:
        title = extract_text(p['title'])
        excerpt = extract_text(p.get('excerpt', ''))[:120]
        posts_text.append(f"ID {p['id']}: {title}")
    
    prompt = f"""Analiza estas {len(sample)} notas del ecosistema startup:

{chr(10).join(posts_text)}

Identifica:
1. Tendencias (temas recurrentes con ejemplos)
2. Sugerencias de pauta (qué profundizar, qué ángulos faltan)
3. Gaps de cobertura (temas importantes no cubiertos)

Responde en JSON estricto:
{{
  "tendencias": [
    {{"tema": "<string>", "frecuencia": <int>, "ejemplos": [id1, id2, ...]}},
    ...
  ],
  "sugerencias": [
    {{"tema": "<string>", "razon": "<string>", "angulo_propuesto": "<string>"}},
    ...
  ],
  "gaps": ["<tema>", ...]
}}
"""

    TESTS.append({
        'name': f'pauta_{i}',
        'description': f'Analizar pauta editorial sobre {len(sample)} notas',
        'messages': [
            {'role': 'system', 'content': 'Eres un editor jefe que sugiere pauta editorial.'},
            {'role': 'user', 'content': prompt}
        ],
        'expected_answer': {
            'tendencias': [
                {'tema': topic, 'frecuencia': len(ids), 'ejemplos': ids[:3]}
                for topic, ids in expected_topics.items() if ids
            ]
        },
        'criteria': {
            'format': {
                'json_structure': ['tendencias', 'sugerencias', 'gaps'],
                'tendencias_is_list': True,
                'sugerencias_is_list': True
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_pauta_score(
                    pred,
                    expected_topics
                )
            }
        }
    })
