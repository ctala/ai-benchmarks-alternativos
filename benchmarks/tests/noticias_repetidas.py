"""
Suite noticias_repetidas — Detectar notas que cubren el mismo hecho.

**Diseño aprobado:** benchmark-pack-noticias_e470.md § 4.2
**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

- **6 lotes** de ~43 notas cada uno (259 notas totales del 8-9 oct)
- **Input:** Lista de notas con ID, título y primeros 300 caracteres
- **Output:** JSON `{grupos: [[id1, id2, ...], ...]}`
- **Scoring:** F1 sobre pares (TP/(TP+0.5*(FP+FN)))
  - TP: pares correctamente agrupados
  - FP: pares incorrectamente agrupados
  - FN: pares que debieron agruparse y no se agruparon
  - Pares "grises" (mismo evento, otro ángulo) no cuentan
- **Verdad:** gt_dedup_8_9oct.json con 23 grupos etiquetados manualmente
- **Referencia sin modelo:** embeddings alcanzan 88.9% (32/36 grupos encontrados)
"""

from typing import List, Dict, Any, Set, Tuple
import random
from ._noticias_common import load_full_posts, load_gt_dedup, extract_rendered, truncate_text


def _create_test_batch(
    posts: List[Dict],
    dup_groups: List[List[int]],
    grey_pairs: List[List[int]],
    batch_num: int
) -> Dict[str, Any]:
    """
    Crea un lote de ~43 notas que incluye grupos de duplicados completos.
    
    Distribuye los 23 grupos entre 6 lotes, asegurando que cada grupo
    quede completo dentro de un solo lote.
    """
    # Distribuir grupos entre lotes
    groups_per_batch = len(dup_groups) // 6 + (1 if batch_num <= (len(dup_groups) % 6) else 0)
    start_idx = batch_num * (len(dup_groups) // 6)
    if batch_num > 0:
        start_idx += min(batch_num, len(dup_groups) % 6)
    end_idx = start_idx + groups_per_batch
    
    batch_groups = dup_groups[start_idx:end_idx]
    
    # IDs de este lote
    batch_ids = set()
    for group in batch_groups:
        batch_ids.update(group)
    
    # Agregar notas que NO están en duplicados para completar ~43
    all_dup_ids = set()
    for group in dup_groups:
        all_dup_ids.update(group)
    
    non_dup_posts = [p for p in posts if p['id'] not in all_dup_ids]
    target_size = 43
    needed = max(0, target_size - len(batch_ids))
    
    if needed > 0 and non_dup_posts:
        random.seed(2026 + batch_num)
        extra_ids = set(random.sample([p['id'] for p in non_dup_posts], min(needed, len(non_dup_posts))))
        batch_ids.update(extra_ids)
    
    # Construir lista de notas del lote
    posts_by_id = {p['id']: p for p in posts}
    batch_posts = []
    for pid in batch_ids:
        if pid in posts_by_id:
            p = posts_by_id[pid]
            title = extract_rendered(p['title'])
            content = extract_rendered(p.get('content', ''))
            excerpt = truncate_text(content, 300)
            batch_posts.append({
                'id': pid,
                'title': title,
                'excerpt': excerpt
            })
    
    # Ordenar por ID para consistencia
    batch_posts.sort(key=lambda x: x['id'])
    
    return {
        'posts': batch_posts,
        'expected_groups': batch_groups,
        'batch_num': batch_num
    }


def _calculate_f1_pairs(
    predicted_groups: List[List[int]],
    expected_groups: List[List[int]],
    grey_pairs_list: List[List[int]]
) -> float:
    """
    Calcula F1 sobre pares de IDs.
    
    - TP: pares en predicted que están en expected
    - FP: pares en predicted que NO están en expected (ni en grey)
    - FN: pares en expected que NO están en predicted
    - Grey pairs: no cuentan ni como TP ni como FP
    
    F1 = TP / (TP + 0.5 * (FP + FN))
    """
    # Construir sets de pares
    def make_pairs(groups: List[List[int]]) -> Set[Tuple[int, int]]:
        pairs = set()
        for group in groups:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    pairs.add(tuple(sorted([group[i], group[j]])))
        return pairs
    
    predicted_pairs = make_pairs(predicted_groups)
    expected_pairs = make_pairs(expected_groups)
    
    # Grey pairs
    grey_pairs = set()
    for pair in grey_pairs_list:
        if len(pair) == 2:
            grey_pairs.add(tuple(sorted(pair)))
    
    # Calcular TP, FP, FN
    tp = len((predicted_pairs & expected_pairs) - grey_pairs)
    fp = len((predicted_pairs - expected_pairs) - grey_pairs)
    fn = len(expected_pairs - predicted_pairs)
    
    # F1
    if tp == 0:
        return 0.0
    
    f1 = tp / (tp + 0.5 * (fp + fn))
    return f1


# Cargar datos
full_posts = load_full_posts()
gt = load_gt_dedup()
dup_groups = gt['dup']
grey_pairs = gt['gris']

# Crear 6 lotes
TESTS = []

for batch_num in range(6):
    batch_data = _create_test_batch(full_posts, dup_groups, grey_pairs, batch_num)
    
    if not batch_data['posts']:
        continue
    
    # Construir prompt
    posts_text = []
    for p in batch_data['posts']:
        posts_text.append(f"ID {p['id']}: {p['title']}\n{p['excerpt']}\n")
    
    prompt = f"""Identifica qué notas cubren el MISMO HECHO.

{len(batch_data['posts'])} notas a analizar:

{chr(10).join(posts_text)}

Responde en JSON estricto:
{{
  "grupos": [
    [id1, id2, id3],
    [id4, id5],
    ...
  ]
}}

Solo agrupa las notas que cubren exactamente el mismo hecho.
Si dos notas hablan del mismo evento pero con diferente dato o ángulo, NO las agrupe.
Las notas que no tienen duplicados no van en ningún grupo.
"""

    TESTS.append({
        'name': f'lote_{batch_num+1}',
        'description': f'Detectar duplicados en lote de {len(batch_data["posts"])} notas',
        'messages': [
            {'role': 'system', 'content': 'Eres un editor que detecta cuándo dos notas cubren el mismo hecho.'},
            {'role': 'user', 'content': prompt}
        ],
        'expected_answer': {
            'grupos': batch_data['expected_groups']
        },
        'criteria': {
            'format': {
                'json_valid': True,
                'has_key': 'grupos',
                'grupos_is_list_of_lists': True
            },
            'substance': {
                'custom_scorer': lambda pred, exp, ctx: _calculate_f1_pairs(
                    pred.get('grupos', []),
                    batch_data['expected_groups'],
                    grey_pairs
                )
            }
        }
    })
