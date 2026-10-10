"""
Helper común para las 5 suites de noticias (Ecosistema Startup corpus).

**LICENCIA PENDIENTE:** Los textos de las notas pertenecen a Ecosistema Startup
y requieren aprobación de licencia CC BY 4.0 antes de publicación/medición.

Ubicación datos: /home/ubuntu/.cursor/projects/workspace/uploads/
"""

import json
import os
from typing import List, Dict, Any

DATA_DIR = '/home/ubuntu/.cursor/projects/workspace/uploads'


def load_posts_14d() -> List[Dict[str, Any]]:
    """Carga las 2441 notas de 14 días (26-sep a 10-oct-2026)."""
    path = os.path.join(DATA_DIR, 'posts_14d_97be.json')
    with open(path) as f:
        return json.load(f)


def load_full_posts() -> List[Dict[str, Any]]:
    """Carga las 259 notas completas con HTML (8-9 oct 2026)."""
    posts = []
    for filename in ['full_p1_e8bb.json', 'full_p2_dd0a.json', 'full_p3_6cc8.json']:
        path = os.path.join(DATA_DIR, filename)
        with open(path) as f:
            posts.extend(json.load(f))
    return posts


def load_gt_dedup() -> Dict[str, Any]:
    """
    Carga el ground truth de duplicados (etiquetado manual 10-oct-2026).
    
    Estructura:
    - 'nota': string descriptivo  
    - 'dup': lista de 23 grupos de IDs duplicados (59 IDs totales)
    - 'gris': lista de 10 pares ID con mismo evento pero diferente ángulo (14 IDs)
    """
    path = os.path.join(DATA_DIR, 'gt_dedup_8_9oct_8af8.json')
    with open(path) as f:
        return json.load(f)


def extract_rendered(field: Any) -> str:
    """Extrae texto de un campo que puede ser string o dict con 'rendered'."""
    if isinstance(field, dict):
        return field.get('rendered', str(field))
    return str(field)


def truncate_text(text: str, max_chars: int) -> str:
    """Trunca texto a N caracteres."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + '...'
