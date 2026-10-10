"""
Suite noticias_repetidas — Detectar duplicados en un flujo de noticias.

**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

Mide si el modelo puede identificar cuándo dos o más notas cubren el mismo hecho,
usando el ground truth etiquetado manualmente el 10-oct-2026.

Entrada: 8-12 notas (títulos + excerpts de ~150 chars)
Salida: JSON con grupos de duplicados: [[id1, id2], [id3, id4, id5], ...]

Scoring:
- Pares correctamente identificados (TP)
- Pares incorrectamente agrupados (FP)
- Pares que debieron agruparse y no (FN)
- F1 = 2*TP / (2*TP + FP + FN)

Notas en área gris (mismo evento, diferente ángulo) no cuentan ni como acierto ni error.
"""

from typing import List, Dict, Any
import random
from ._noticias_data import load_full_posts, load_gt_dedup, extract_text


def _build_test_from_dup_group(
    group_ids: List[int],
    full_posts: List[Dict],
    noise_posts: List[Dict],
    n_noise: int = 3
) -> Dict[str, Any]:
    """Crea un test a partir de un grupo de duplicados + ruido."""
    posts_by_id = {p['id']: p for p in full_posts}
    
    # Posts del grupo
    group_posts = [posts_by_id[pid] for pid in group_ids if pid in posts_by_id]
    if len(group_posts) < 2:
        return None
    
    # Agregar ruido (posts no duplicados)
    noise_sample = random.sample(noise_posts, min(n_noise, len(noise_posts)))
    
    test_posts = group_posts + noise_sample
    random.shuffle(test_posts)
    
    # Construir input
    posts_text = []
    for p in test_posts:
        title = extract_text(p['title'])
        excerpt = extract_text(p.get('excerpt', ''))[:200]
        posts_text.append(f"ID {p['id']}: {title}\n{excerpt}")
    
    prompt = f"""Identifica qué notas cubren el MISMO HECHO.

Notas a analizar:

{chr(10).join(posts_text)}

Responde en JSON estricto: {{"grupos": [[id1, id2], [id3, id4, id5], ...]}}

Si dos notas hablan del mismo evento pero con diferente dato o ángulo, NO las agrupe.
Solo agrupa las que cubren exactamente el mismo hecho.
"""

    return {
        'posts': test_posts,
        'expected_group': group_ids,
        'prompt': prompt
    }


def _calculate_dup_f1(
    predicted_groups: List[List[int]],
    expected_group: List[int],
    grey_pairs: List[List[int]]
) -> float:
    """
    Calcula F1 para detección de duplicados.
    
    - TP: pares correctamente identificados
    - FP: pares incorrectamente agrupados
    - FN: pares que debieron agruparse y no
    - Pares grises no cuentan
    """
    # Pares esperados
    expected_pairs = set()
    for i in range(len(expected_group)):
        for j in range(i+1, len(expected_group)):
            expected_pairs.add(tuple(sorted([expected_group[i], expected_group[j]])))
    
    # Pares predichos
    predicted_pairs = set()
    for group in predicted_groups:
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                predicted_pairs.add(tuple(sorted([group[i], group[j]])))
    
    # Pares grises (no cuentan)
    grey_set = set(tuple(sorted(pair)) for pair in grey_pairs)
    
    # TP, FP, FN
    tp = len((predicted_pairs & expected_pairs) - grey_set)
    fp = len(predicted_pairs - expected_pairs - grey_set)
    fn = len(expected_pairs - predicted_pairs)
    
    # F1
    if tp == 0:
        return 0.0
    f1 = 2 * tp / (2 * tp + fp + fn)
    return f1


# Cargar datos
full_posts = load_full_posts()
gt = load_gt_dedup()
dup_groups = gt['dup']
grey_pairs = gt['gris']

# IDs en grupos de duplicados
all_dup_ids = set()
for group in dup_groups:
    all_dup_ids.update(group)

# Posts que NO están en duplicados (para ruido)
noise_posts = [p for p in full_posts if p['id'] not in all_dup_ids]

# Seleccionar 6 grupos de duplicados para tests
random.seed(2026)
selected_groups = random.sample([g for g in dup_groups if len(g) >= 3], 6)

TESTS = []

for i, group in enumerate(selected_groups, 1):
    test_data = _build_test_from_dup_group(group, full_posts, noise_posts, n_noise=3)
    if not test_data:
        continue
    
    TESTS.append({
        'name': f'dup_group_{i}',
        'description': f'Detectar {len(test_data["expected_group"])} notas duplicadas entre {len(test_data["posts"])} notas',
        'messages': [
            {'role': 'system', 'content': 'Eres un editor que detecta duplicados en flujos de noticias.'},
            {'role': 'user', 'content': test_data['prompt']}
        ],
        'expected_answer': {
            'grupos': [test_data['expected_group']]
        },
        'criteria': {
            'format': {
                'json_structure': ['grupos'],
                'grupos_is_list_of_lists': True
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_dup_f1(
                    pred.get('grupos', []),
                    test_data['expected_group'],
                    grey_pairs
                )
            }
        }
    })
