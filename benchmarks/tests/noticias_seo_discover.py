"""
Suite noticias_seo_discover — Título y metadatos para Google Discover.

**Diseño aprobado:** benchmark-pack-noticias_e470.md § 4.5
**LICENCIA:** Textos de Ecosistema Startup, pendiente aprobación CC BY 4.0.

- **15 tests** (15 notas publicadas)
- **Input:** Texto de nota + reglas de Google Discover
- **Output:** JSON con titulo, meta_titulo, meta_descripcion, slug, keyword_principal, 
  alt_imagen, titulos_alternativos
- **Scoring:**
  - 70% automático: largos, formato slug, keyword presente, sin cifras inventadas, sin clickbait
  - 30% verificador Phi-4: 2 preguntas Y/N

**BLOQUEANTE:** Requiere seleccionar 15 notas y anotar el protagonista de cada una (~15 min).
"""

from typing import List, Dict, Any
import re
from ._noticias_common import load_full_posts, extract_rendered

# Reglas de Google Discover (guidelines públicas)
REGLAS_DISCOVER = """
**Google Discover Guidelines:**

1. **Título:** 55-65 caracteres ideales, captura la esencia sin clickbait
2. **Meta título:** Máximo 60 caracteres
3. **Meta descripción:** 120-156 caracteres, gancho sin sensacionalismo
4. **Slug URL:** kebab-case, 6 palabras o menos, incluye keyword
5. **Keyword principal:** presente en título y meta descripción
6. **Alt imagen:** descriptivo, 10-20 palabras

**Evitar:**
- Clickbait: "no vas a creer", "increíble", "!!", mayúsculas sostenidas
- Ocultar información clave en el título
- Prometer algo que la nota no entrega
- Detalles exagerados o sensacionalistas

**Objetivo:** Título engaging que nombre protagonista y hecho principal.
"""

# Patrones de clickbait
CLICKBAIT_PATTERNS = [
    r'no vas a creer', r'increíble', r'impresionante',
    r'!!+', r'[A-Z]{4,}',  # mayúsculas sostenidas
    r'te sorprenderá', r'te dejará', r'alucinante'
]


def _load_notas_seo() -> List[Dict[str, Any]]:
    """
    Carga las 15 notas seleccionadas con protagonista anotado.
    
    Formato esperado:
    [
      {
        "nota_id": <int>,
        "nota_texto": "<texto completo>",
        "protagonista": "<empresa, persona o fund>",
        "hecho_principal": "<brief descripción>"
      },
      ...  # 15 notas
    ]
    
    **PENDIENTE:** Seleccionar 15 notas y anotar protagonista (~15 min).
    """
    import os
    import json
    
    path = '/home/ubuntu/.cursor/projects/workspace/uploads/notas_seo_discover.json'
    
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"❌ NOTAS SEO FALTANTES\n\n"
            f"El archivo {path} NO existe.\n"
            f"Esta suite requiere 15 notas con protagonista anotado:\n"
            f"- nota_id, nota_texto, protagonista, hecho_principal\n\n"
            f"Tiempo estimado: ~15 minutos"
        )
    
    with open(path) as f:
        return json.load(f)


def _score_automatico(respuesta: Dict, nota_texto: str) -> float:
    """
    Puntúa aspectos automáticos (70% del total).
    
    - JSON válido con campos requeridos: 10 pts
    - Largos correctos (titulo ≤60, meta_desc 120-156): 15 pts
    - Slug formato kebab-case, ≤6 palabras: 10 pts
    - Keyword presente en título y meta_desc: 15 pts
    - Sin cifras que no estén en la nota: 10 pts
    - Sin patrones de clickbait: 10 pts
    
    Total: 0-70
    """
    score = 0.0
    
    # JSON válido con campos
    required_fields = ['titulo', 'meta_titulo', 'meta_descripcion', 'slug', 'keyword_principal']
    has_all_fields = all(f in respuesta for f in required_fields)
    if has_all_fields:
        score += 10.0
    
    # Largos
    titulo = respuesta.get('titulo', '')
    meta_desc = respuesta.get('meta_descripcion', '')
    
    if len(titulo) <= 60:
        score += 7.5
    if 120 <= len(meta_desc) <= 156:
        score += 7.5
    
    # Slug
    slug = respuesta.get('slug', '')
    is_kebab = bool(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', slug))
    palabras = len(slug.split('-'))
    
    if is_kebab:
        score += 5.0
    if palabras <= 6:
        score += 5.0
    
    # Keyword presente
    keyword = respuesta.get('keyword_principal', '').lower()
    if keyword:
        if keyword in titulo.lower():
            score += 7.5
        if keyword in meta_desc.lower():
            score += 7.5
    
    # Sin cifras inventadas
    cifras_respuesta = set(re.findall(r'\d+', titulo + meta_desc))
    cifras_nota = set(re.findall(r'\d+', nota_texto))
    
    cifras_inventadas = cifras_respuesta - cifras_nota
    if not cifras_inventadas:
        score += 10.0
    
    # Sin clickbait
    texto_lower = (titulo + meta_desc).lower()
    has_clickbait = any(re.search(pattern, texto_lower) for pattern in CLICKBAIT_PATTERNS)
    if not has_clickbait:
        score += 10.0
    
    return score


def _score_verificador_placeholder() -> float:
    """
    Placeholder para scoring con verificador Phi-4.
    
    2 preguntas:
    1. ¿El título promete algo que la nota no entrega, o esconde el dato clave?
    2. ¿Nombra al protagonista y el hecho?
    
    Por ahora: promedio simulado.
    """
    # TODO: Implementar con benchmarks/verifier.py
    return 15.0  # Promedio de 30 pts


# Intentar cargar notas
try:
    notas_seo = _load_notas_seo()
except FileNotFoundError as e:
    print(f"\n⚠️  WARNING: {e}\n")
    notas_seo = []

TESTS = []

if notas_seo:
    for i, nota_data in enumerate(notas_seo, 1):
        prompt = f"""{REGLAS_DISCOVER}

**Nota a optimizar:**

{nota_data['nota_texto']}

**Protagonista:** {nota_data['protagonista']}
**Hecho principal:** {nota_data['hecho_principal']}

Genera metadatos para Google Discover.

Responde en JSON estricto:
{{
  "titulo": "<55-65 chars>",
  "meta_titulo": "<max 60 chars>",
  "meta_descripcion": "<120-156 chars>",
  "slug": "<kebab-case, max 6 palabras>",
  "keyword_principal": "<string>",
  "alt_imagen": "<10-20 palabras descriptivas>",
  "titulos_alternativos": ["<opción 2>", "<opción 3>"]
}}
"""

        TESTS.append({
            'name': f'seo_discover_{i}',
            'description': f'Optimizar metadatos para Discover - nota {nota_data["nota_id"]}',
            'messages': [
                {'role': 'system', 'content': 'Eres un especialista en SEO para Google Discover.'},
                {'role': 'user', 'content': prompt}
            ],
            'expected_answer': {
                'nota_texto': nota_data['nota_texto'],
                'protagonista': nota_data['protagonista']
            },
            'criteria': {
                'format': {
                    'json_valid': True,
                    'required_keys': ['titulo', 'meta_titulo', 'meta_descripcion', 'slug', 'keyword_principal']
                },
                'substance': {
                    'custom_scorer': lambda pred, exp, ctx: (
                        _score_automatico(pred if isinstance(pred, dict) else {}, 
                                        ctx.get('expected_answer', {}).get('nota_texto', '')) +
                        _score_verificador_placeholder()
                    ) / 10.0  # Normalizar a 0-10
                }
            }
        })
else:
    print("\n⚠️  noticias_seo_discover: suite vacía (faltan notas seleccionadas)\n")
