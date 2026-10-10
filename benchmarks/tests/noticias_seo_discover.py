"""
Suite noticias_seo_discover — Optimización para Google Discover.

**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

Mide si el modelo puede optimizar notas para Google Discover según guidelines:
1. Título: engaging, 55-65 chars, incluye keyword principal
2. Excerpt/meta: 120-156 chars, gancho sin clickbait
3. Estructura: usa headings (H2/H3), listas, datos
4. Contenido: profundidad >800 palabras, fuentes citadas
5. Engagement: pregunta que hook, ángulo único

Entrada: nota (título + contenido)
Salida: JSON {
  "titulo_optimizado": "<string>",
  "excerpt_optimizado": "<string>",
  "mejoras": [{aspecto, actual, propuesta, prioridad: high|medium|low}],
  "score_discover": <1-10>
}

Scoring: evaluación heurística de optimización SEO
"""

from typing import List, Dict, Any
import random
import re
from ._noticias_data import load_full_posts, extract_text, truncate_html


def _analyze_seo(title: str, content_html: str) -> Dict:
    """Analiza SEO actual de la nota."""
    analysis = {
        'titulo_length': len(title),
        'tiene_h2': '<h2' in content_html,
        'tiene_h3': '<h3' in content_html,
        'tiene_lista': '<ul>' in content_html or '<ol>' in content_html,
        'tiene_numeros': bool(re.search(r'\d+', title)),
        'palabras': len(content_html.split()),
        'tiene_pregunta': '¿' in title or '?' in title
    }
    
    # Calcular score actual
    score = 0
    if 50 <= analysis['titulo_length'] <= 70:
        score += 2
    if analysis['tiene_h2']:
        score += 1
    if analysis['tiene_lista']:
        score += 1
    if analysis['tiene_numeros']:
        score += 1
    if analysis['palabras'] >= 800:
        score += 2
    if analysis['tiene_pregunta']:
        score += 1
    
    analysis['score_actual'] = min(score, 10)
    return analysis


def _generate_mejoras(analysis: Dict, title: str) -> List[Dict]:
    """Genera sugerencias de mejora."""
    mejoras = []
    
    if analysis['titulo_length'] < 50:
        mejoras.append({
            'aspecto': 'titulo_corto',
            'actual': f'{analysis["titulo_length"]} caracteres',
            'propuesta': 'Ampliar a 55-65 chars con keyword principal',
            'prioridad': 'high'
        })
    elif analysis['titulo_length'] > 70:
        mejoras.append({
            'aspecto': 'titulo_largo',
            'actual': f'{analysis["titulo_length"]} caracteres',
            'propuesta': 'Reducir a 55-65 chars, más directo',
            'prioridad': 'medium'
        })
    
    if not analysis['tiene_h2']:
        mejoras.append({
            'aspecto': 'sin_headings',
            'actual': 'Sin H2',
            'propuesta': 'Agregar 3-5 H2 con keywords secundarias',
            'prioridad': 'high'
        })
    
    if not analysis['tiene_lista']:
        mejoras.append({
            'aspecto': 'sin_listas',
            'actual': 'Sin listas',
            'propuesta': 'Agregar lista de puntos clave o datos',
            'prioridad': 'medium'
        })
    
    if analysis['palabras'] < 800:
        mejoras.append({
            'aspecto': 'contenido_superficial',
            'actual': f'{analysis["palabras"]} palabras',
            'propuesta': 'Ampliar a 1000+ palabras con contexto y fuentes',
            'prioridad': 'high'
        })
    
    if not analysis['tiene_pregunta']:
        mejoras.append({
            'aspecto': 'falta_hook',
            'actual': 'Título enunciativo',
            'propuesta': 'Usar pregunta o cifra impactante',
            'prioridad': 'low'
        })
    
    return mejoras


def _calculate_seo_score(
    predicted: Dict,
    expected_analysis: Dict,
    expected_mejoras: List[Dict]
) -> float:
    """
    Score de optimización SEO.
    
    - Título optimizado razonable: hasta 3 pts
    - Excerpt optimizado: hasta 2 pts
    - Identificó mejoras clave: hasta 3 pts
    - Score Discover calibrado: hasta 2 pts
    """
    score = 0.0
    
    # Título optimizado
    titulo_opt = predicted.get('titulo_optimizado', '')
    if 50 <= len(titulo_opt) <= 70:
        score += 2.0
    if titulo_opt:  # Al menos intentó
        score += 1.0
    
    # Excerpt
    excerpt_opt = predicted.get('excerpt_optimizado', '')
    if 120 <= len(excerpt_opt) <= 160:
        score += 1.5
    if excerpt_opt:
        score += 0.5
    
    # Mejoras identificadas
    pred_mejoras = predicted.get('mejoras', [])
    if len(pred_mejoras) >= 3:
        score += 1.5
    if len(pred_mejoras) >= 5:
        score += 1.5
    
    # Score Discover
    pred_score_discover = predicted.get('score_discover', 0)
    if 3 <= pred_score_discover <= 8:  # Rango razonable
        score += 1.0
    if pred_score_discover > 0:
        score += 1.0
    
    return min(score, 10.0)


# Cargar datos
full_posts = load_full_posts()
random.seed(2026)

TESTS = []

# Seleccionar 4 notas para optimización SEO
selected = random.sample(full_posts, 4)

for i, post in enumerate(selected, 1):
    title = extract_text(post['title'])
    content = extract_text(post['content'])
    content_truncated = truncate_html(content, 2000)
    
    expected_analysis = _analyze_seo(title, content)
    expected_mejoras = _generate_mejoras(expected_analysis, title)
    
    prompt = f"""Optimiza esta nota para Google Discover:

TÍTULO ACTUAL: {title}

CONTENIDO (excerpt):
{content_truncated}

Guidelines Google Discover:
- Título: 55-65 chars, engaging, keyword principal
- Meta/excerpt: 120-156 chars, gancho sin clickbait
- Estructura: H2/H3, listas, datos
- Profundidad: >800 palabras, fuentes citadas
- Engagement: pregunta hook, ángulo único

Responde en JSON estricto:
{{
  "titulo_optimizado": "<string 55-65 chars>",
  "excerpt_optimizado": "<string 120-156 chars>",
  "mejoras": [
    {{"aspecto": "<string>", "actual": "<string>", "propuesta": "<string>", "prioridad": "high|medium|low"}},
    ...
  ],
  "score_discover": <1-10>
}}
"""

    TESTS.append({
        'name': f'seo_discover_{i}',
        'description': f'Optimizar nota ID {post["id"]} para Google Discover',
        'messages': [
            {'role': 'system', 'content': 'Eres un especialista en SEO para Google Discover.'},
            {'role': 'user', 'content': prompt}
        ],
        'expected_answer': {
            'score_actual': expected_analysis['score_actual'],
            'mejoras_esperadas': expected_mejoras
        },
        'criteria': {
            'format': {
                'json_structure': ['titulo_optimizado', 'excerpt_optimizado', 'mejoras', 'score_discover'],
                'mejoras_is_list': True
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_seo_score(
                    pred,
                    expected_analysis,
                    expected_mejoras
                )
            }
        }
    })
