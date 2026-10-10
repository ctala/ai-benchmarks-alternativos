"""
Suite noticias_verificacion — Verificar afirmaciones contra fuente.

**Diseño aprobado:** benchmark-pack-noticias_e470.md § 4.4
**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

- **8 tests** (8 notas × 12 afirmaciones cada una = 96 afirmaciones total)
- **Input:** Prompt de verificación + nota fuente + 12 afirmaciones
  - 4 copiadas de la nota
  - 3 parafraseadas
  - 3 con cifra alterada sutilmente
  - 2 inventadas pero verosímiles
- **Output:** JSON `[{id, veredicto: "RESPALDA"|"CONTRADICE"|"SIN_RESPALDO", razon}, ...]`
- **Scoring:** veredictos correctos / afirmaciones enviadas (0-10)

**BLOQUEANTE:** Requiere construir las 96 afirmaciones manualmente.
"""

from typing import List, Dict, Any
from ._noticias_common import load_full_posts, extract_rendered

# Prompt de verificación (de producción, verificar_claims_lote.py)
PROMPT_VERIFICACION = """
Eres un verificador de datos. Tu trabajo es determinar si cada afirmación está respaldada por la fuente.

**Veredictos:**
- RESPALDA: La afirmación está directamente respaldada por la fuente
- CONTRADICE: La fuente dice explícitamente lo contrario
- SIN_RESPALDO: La fuente no menciona esto, o la información es insuficiente

**Reglas:**
1. Una cifra alterada (aunque sea sutilmente) es CONTRADICE
2. Una afirmación inventada pero verosímil es SIN_RESPALDO
3. Una paráfrasis correcta es RESPALDA
4. Si tienes duda, usa SIN_RESPALDO (nunca inventes)
"""


def _load_afirmaciones() -> List[Dict[str, Any]]:
    """
    Carga las 8 notas con sus 12 afirmaciones construidas.
    
    Formato esperado:
    [
      {
        "test_id": <int>,
        "nota_id": <int>,
        "nota_texto": "<texto completo de la nota>",
        "afirmaciones": [
          {
            "id": <int 1-12>,
            "texto": "<afirmación>",
            "tipo": "copiada" | "parafraseada" | "cifra_alterada" | "inventada",
            "veredicto_correcto": "RESPALDA" | "CONTRADICE" | "SIN_RESPALDO",
            "nota": "<opcional: explicación del tipo>"
          },
          ...  # 12 afirmaciones
        ]
      },
      ...  # 8 tests
    ]
    
    **PENDIENTE:** 8 × 12 = 96 afirmaciones construidas manualmente.
    """
    import os
    import json
    
    path = '/home/ubuntu/.cursor/projects/workspace/uploads/afirmaciones_verificacion.json'
    
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"❌ AFIRMACIONES FALTANTES\n\n"
            f"El archivo {path} NO existe.\n"
            f"Esta suite requiere 8 notas con 12 afirmaciones cada una:\n"
            f"- 4 copiadas (veredicto: RESPALDA)\n"
            f"- 3 parafraseadas (veredicto: RESPALDA)\n"
            f"- 3 con cifra alterada sutilmente (veredicto: CONTRADICE)\n"
            f"- 2 inventadas pero verosímiles (veredicto: SIN_RESPALDO)\n\n"
            f"Total: 96 afirmaciones construidas.\n"
            f"Tiempo estimado: ~2-3 horas"
        )
    
    with open(path) as f:
        return json.load(f)


def _calculate_verificacion_score(
    predicted: List[Dict],
    expected: List[Dict]
) -> float:
    """
    Calcula score de verificación.
    
    Score = (veredictos correctos / afirmaciones enviadas) * 10
    
    Una afirmación sin veredicto cuenta como error.
    """
    if not expected:
        return 0.0
    
    pred_by_id = {p.get('id'): p for p in predicted if 'id' in p}
    
    correct = 0
    for exp in expected:
        pred = pred_by_id.get(exp['id'])
        if pred and pred.get('veredicto') == exp['veredicto_correcto']:
            correct += 1
    
    score = (correct / len(expected)) * 10
    return score


# Intentar cargar afirmaciones
try:
    tests_data = _load_afirmaciones()
except FileNotFoundError as e:
    print(f"\n⚠️  WARNING: {e}\n")
    tests_data = []

TESTS = []

if tests_data:
    for test_data in tests_data:
        # Construir prompt
        afirmaciones_text = []
        for afirm in test_data['afirmaciones']:
            afirmaciones_text.append(f"{afirm['id']}. {afirm['texto']}")
        
        prompt = f"""{PROMPT_VERIFICACION}

**Fuente:**

{test_data['nota_texto']}

**Afirmaciones a verificar:**

{chr(10).join(afirmaciones_text)}

Responde en JSON estricto:
[
  {{
    "id": <int>,
    "veredicto": "RESPALDA" | "CONTRADICE" | "SIN_RESPALDO",
    "razon": "<breve explicación>"
  }},
  ...
]
"""

        TESTS.append({
            'name': f'verificacion_{test_data["test_id"]}',
            'description': f'Verificar 12 afirmaciones contra nota {test_data["nota_id"]}',
            'messages': [
                {'role': 'system', 'content': 'Eres un verificador de datos riguroso.'},
                {'role': 'user', 'content': prompt}
            ],
            'expected_answer': test_data['afirmaciones'],
            'criteria': {
                'format': {
                    'is_list': True,
                    'list_length': 12,
                    'required_keys': ['id', 'veredicto']
                },
                'substance': {
                    'custom_scorer': lambda pred, exp, ctx: _calculate_verificacion_score(
                        pred if isinstance(pred, list) else [],
                        test_data['afirmaciones']
                    )
                }
            }
        })
else:
    print("\n⚠️  noticias_verificacion: suite vacía (faltan afirmaciones construidas)\n")
