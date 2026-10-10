"""
Suite noticias_verificacion — Fact-checking y detección de claims dudosos.

**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

Mide si el modelo puede:
1. Identificar claims verificables en una nota
2. Señalar cifras/hechos que requieren fuente
3. Detectar posibles exageraciones o imprecisiones

Entrada: nota completa (título + contenido HTML)
Salida: JSON {
  "claims": [{claim, verificable: bool, requiere_fuente: bool, confianza: 1-10}],
  "alertas": [{tipo, descripcion, gravedad: low|medium|high}]
}

Scoring: heurístico (busca patterns de claims verificables)
"""

from typing import List, Dict, Any
import random
import re
from ._noticias_data import load_full_posts, extract_text, truncate_html


def _extract_claims(content_html: str) -> List[Dict]:
    """Extrae claims heurísticamente (números, fechas, nombres propios)."""
    # Buscar patrones de cifras
    money_pattern = r'\$[\d,.]+ ?[MKB]|\€[\d,.]+ ?M|[\d,.]+ millones'
    number_pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d+)?%?'
    date_pattern = r'\d{1,2} de \w+ de \d{4}|[A-Z][a-z]+ \d{4}'
    
    claims = []
    text = content_html[:2000]  # Primeros 2000 chars
    
    # Dinero
    for match in re.finditer(money_pattern, text):
        claims.append({
            'claim': match.group(),
            'verificable': True,
            'requiere_fuente': True,
            'confianza': 8
        })
    
    # Números grandes
    for match in re.finditer(number_pattern, text):
        num_str = match.group()
        # Solo si es >1000
        try:
            num = float(num_str.replace(',', ''))
            if num >= 1000:
                claims.append({
                    'claim': f'cifra: {num_str}',
                    'verificable': True,
                    'requiere_fuente': True,
                    'confianza': 7
                })
        except:
            pass
    
    return claims[:10]  # Limitar a 10 claims


def _generate_alerts(title: str, content: str) -> List[Dict]:
    """Genera alertas heurísticas."""
    alerts = []
    
    # Palabras de exageración
    hype_words = ['revoluciona', 'cambia el juego', 'disruptivo', 'innovador']
    for word in hype_words:
        if word in content.lower():
            alerts.append({
                'tipo': 'hype_word',
                'descripcion': f'Palabra de marketing: "{word}"',
                'gravedad': 'low'
            })
    
    # Falta de fuente
    if 'según' not in content.lower() and 'fuente' not in content.lower():
        alerts.append({
            'tipo': 'missing_source',
            'descripcion': 'No se menciona fuente explícita',
            'gravedad': 'medium'
        })
    
    return alerts


def _calculate_verificacion_score(
    predicted: Dict,
    expected_claims: List[Dict],
    expected_alerts: List[Dict]
) -> float:
    """
    Score de verificación.
    
    - Identificó claims: hasta 5 pts
    - Alertas razonables: hasta 3 pts
    - Confianza calibrada: hasta 2 pts
    """
    score = 0.0
    
    pred_claims = predicted.get('claims', [])
    
    # Claims identificados
    if len(pred_claims) >= 3:
        score += 2.0
    if len(pred_claims) >= 5:
        score += 2.0
    if len(pred_claims) >= 8:
        score += 1.0
    
    # Verificables marcados
    verificables = sum(1 for c in pred_claims if c.get('verificable', False))
    if verificables >= len(pred_claims) * 0.6:
        score += 1.0
    
    # Alertas
    pred_alerts = predicted.get('alertas', [])
    if len(pred_alerts) >= 1:
        score += 1.5
    if len(pred_alerts) >= 3:
        score += 1.5
    
    return min(score, 10.0)


# Cargar datos
full_posts = load_full_posts()
random.seed(2026)

TESTS = []

# Seleccionar 5 notas para verificación
selected = random.sample(full_posts, 5)

for i, post in enumerate(selected, 1):
    title = extract_text(post['title'])
    content = extract_text(post['content'])
    content_truncated = truncate_html(content, 3000)
    
    expected_claims = _extract_claims(content)
    expected_alerts = _generate_alerts(title, content)
    
    prompt = f"""Fact-check esta nota:

TÍTULO: {title}

CONTENIDO:
{content_truncated}

Identifica:
1. Claims verificables (cifras, hechos, declaraciones)
2. Qué requiere fuente
3. Alertas (exageraciones, imprecisiones, sesgos)

Responde en JSON estricto:
{{
  "claims": [
    {{"claim": "<string>", "verificable": <bool>, "requiere_fuente": <bool>, "confianza": <1-10>}},
    ...
  ],
  "alertas": [
    {{"tipo": "<string>", "descripcion": "<string>", "gravedad": "low|medium|high"}},
    ...
  ]
}}
"""

    TESTS.append({
        'name': f'verificacion_{i}',
        'description': f'Fact-check y detección de claims en nota ID {post["id"]}',
        'messages': [
            {'role': 'system', 'content': 'Eres un fact-checker que verifica claims en noticias.'},
            {'role': 'user', 'content': prompt}
        ],
        'expected_answer': {
            'claims': expected_claims,
            'alertas': expected_alerts
        },
        'criteria': {
            'format': {
                'json_structure': ['claims', 'alertas'],
                'claims_is_list': True,
                'alertas_is_list': True
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_verificacion_score(
                    pred,
                    expected_claims,
                    expected_alerts
                )
            }
        }
    })
