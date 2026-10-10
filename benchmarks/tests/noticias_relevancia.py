"""
Suite noticias_relevancia — Puntuar y filtrar notas por criterio editorial.

**Diseño aprobado:** benchmark-pack-noticias_e470.md § 4.1
**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

- **6 tests** de 10 notas cada uno (60 notas totales)
- **Input:** Criterio editorial + título y primeros 1500 caracteres por nota
- **Output:** JSON `[{id, decision: "KEEP"|"SKIP", categoria, puntaje: 1-10}, ...]`
- **Scoring:** decisiones correctas / notas enviadas (0-10)
- **Verdad:** REQUIERE ETIQUETA HUMANA (~1h)
  - 40 notas KEEP (incluir 10 historias regionales tipo Spora)
  - 20 notas SKIP (candidatas: GTA 6 #115391, Gears of War #114806, iPhone 17 Pro #114721)

**BLOQUEANTE:** Este archivo tiene la estructura pero NO los datos etiquetados.
Las etiquetas deben cargarse de un archivo JSON con formato:
[{id, decision, categoria, puntaje}, ...]
"""

from typing import List, Dict, Any
import random
from ._noticias_common import load_posts_14d, extract_rendered, truncate_text

# Criterio editorial de Ecosistema Startup (versión pública resumida)
CRITERIO_EDITORIAL = """
Ecosistema Startup es un medio especializado en el ecosistema de emprendimiento e innovación:

**SÍ publicamos (KEEP):**
- Startups: inversión, exits, pivotes, fracasos, fundadores
- Venture Capital: fondos, estrategias, retornos, LPs
- Emprendimiento: metodologías, casos reales, ecosistemas regionales
- Tecnología para negocios: IA aplicada, SaaS, herramientas empresariales
- Historias regionales con aprendizajes transferibles

**NO publicamos (SKIP):**
- Tecnología consumer sin ángulo de negocio (ej: iPhone 17 Pro, specs de hardware)
- Gaming sin ángulo de startups/VC (ej: GTA 6, Gears of War)
- Finanzas macro/bolsa sin conexión al ecosistema (bonos, forex, índices)
- Política o sociedad sin conexión directa al emprendimiento
- Noticias que solo interesan al mercado local sin ser transferibles

**Categorías:** startup_funding, vc_strategy, entrepreneurship, business_tech, ai_for_business, regional_ecosystem
"""


def _load_human_labels() -> List[Dict[str, Any]]:
    """
    Carga etiquetas humanas desde archivo JSON.
    
    Formato esperado:
    [
      {
        "id": <int>,
        "decision": "KEEP" | "SKIP",
        "categoria": "<string>",
        "puntaje": <1-10>,
        "notas": "<optional: por qué esta decisión>"
      },
      ...
    ]
    
    **PENDIENTE:** Este archivo NO existe aún. Debe ser creado por una persona
    que revise las notas y las etiquete según el criterio editorial.
    
    Ubicación esperada: /home/ubuntu/.cursor/projects/workspace/uploads/etiquetas_relevancia.json
    """
    import os
    import json
    
    path = '/home/ubuntu/.cursor/projects/workspace/uploads/etiquetas_relevancia.json'
    
    if not os.path.exists(path):
        # PLACEHOLDER: devolver lista vacía con un mensaje de error claro
        raise FileNotFoundError(
            f"❌ ETIQUETAS HUMANAS FALTANTES\n\n"
            f"El archivo {path} NO existe.\n"
            f"Esta suite requiere que una persona etiquete 60 notas:\n"
            f"- 40 KEEP (incluir 10 historias regionales)\n"
            f"- 20 SKIP (candidatas: GTA 6 #115391, Gears of War #114806, iPhone 17 #114721)\n\n"
            f"Cada etiqueta debe incluir: id, decision, categoria, puntaje (1-10)\n"
            f"Tiempo estimado: ~1 hora"
        )
    
    with open(path) as f:
        return json.load(f)


def _calculate_relevancia_score(
    predicted: List[Dict],
    expected: List[Dict]
) -> float:
    """
    Calcula score de relevancia.
    
    Score = (decisiones correctas / notas enviadas) * 10
    
    Una nota sin respuesta cuenta como error.
    """
    if not expected:
        return 0.0
    
    pred_by_id = {p.get('id'): p for p in predicted if 'id' in p}
    
    correct = 0
    for exp in expected:
        pred = pred_by_id.get(exp['id'])
        if pred and pred.get('decision') == exp['decision']:
            correct += 1
    
    score = (correct / len(expected)) * 10
    return score


# Intentar cargar etiquetas humanas
try:
    human_labels = _load_human_labels()
    labels_by_id = {label['id']: label for label in human_labels}
except FileNotFoundError as e:
    # Si no hay etiquetas, la suite queda vacía con un mensaje
    print(f"\n⚠️  WARNING: {e}\n")
    human_labels = []
    labels_by_id = {}

# Cargar notas
posts_14d = load_posts_14d()
posts_by_id = {p['id']: p for p in posts_14d}

# Crear 6 tests de 10 notas cada uno
TESTS = []

if human_labels:
    # Dividir las 60 notas etiquetadas en 6 grupos de 10
    random.seed(2026)
    labeled_ids = list(labels_by_id.keys())
    random.shuffle(labeled_ids)
    
    for test_num in range(6):
        start_idx = test_num * 10
        end_idx = start_idx + 10
        test_ids = labeled_ids[start_idx:end_idx]
        
        # Construir prompt
        posts_text = []
        test_labels = []
        
        for pid in test_ids:
            if pid not in posts_by_id:
                continue
                
            p = posts_by_id[pid]
            title = extract_rendered(p['title'])
            content = extract_rendered(p.get('content', ''))
            excerpt = truncate_text(content, 1500)
            
            posts_text.append(f"ID {pid}:\nTítulo: {title}\n{excerpt}\n")
            test_labels.append(labels_by_id[pid])
        
        if not posts_text:
            continue
        
        prompt = f"""{CRITERIO_EDITORIAL}

Evalúa estas {len(posts_text)} notas:

{chr(10).join(posts_text)}

Responde en JSON estricto:
[
  {{
    "id": <int>,
    "decision": "KEEP" | "SKIP",
    "categoria": "<string>",
    "puntaje": <1-10>
  }},
  ...
]

Para cada nota:
- decision: KEEP si encaja en el criterio, SKIP si no
- categoria: una de las del criterio
- puntaje: 1-10 (relevancia para el medio)
"""

        TESTS.append({
            'name': f'relevancia_{test_num+1}',
            'description': f'Filtrar 10 notas según criterio editorial',
            'messages': [
                {'role': 'system', 'content': 'Eres un editor que filtra notas según criterio editorial.'},
                {'role': 'user', 'content': prompt}
            ],
            'expected_answer': test_labels,
            'criteria': {
                'format': {
                    'is_list': True,
                    'list_length': len(test_labels),
                    'required_keys': ['id', 'decision', 'puntaje']
                },
                'substance': {
                    'custom_scorer': lambda pred, exp, ctx: _calculate_relevancia_score(
                        pred if isinstance(pred, list) else [],
                        test_labels
                    )
                }
            }
        })
else:
    # Sin etiquetas, la suite queda vacía pero documentada
    print("\n⚠️  noticias_relevancia: suite vacía (falta etiquetado humano)\n")
