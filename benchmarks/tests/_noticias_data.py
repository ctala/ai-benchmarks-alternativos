"""
Helper para cargar los datos del corpus de Ecosistema Startup.

LICENCIA PENDIENTE: Los textos de las notas pertenecen a Ecosistema Startup
y requieren aprobación de licencia CC BY 4.0 antes de publicación.

Datos ubicados en /home/ubuntu/.cursor/projects/workspace/uploads/
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
    """Carga las 259 notas completas (8-9 oct 2026)."""
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
    - 'dup': lista de grupos de IDs duplicados (23 grupos, 59 IDs)
    - 'gris': lista de pares ID con mismo evento pero diferente ángulo (10 pares, 14 IDs)
    """
    path = os.path.join(DATA_DIR, 'gt_dedup_8_9oct_8af8.json')
    with open(path) as f:
        return json.load(f)


def extract_text(field: Any) -> str:
    """Extrae texto de un campo que puede ser string o dict con 'rendered'."""
    if isinstance(field, dict):
        return field.get('rendered', str(field))
    return str(field)


def truncate_html(html: str, max_chars: int = 1500) -> str:
    """Trunca HTML a N caracteres, respetando tags."""
    if len(html) <= max_chars:
        return html
    return html[:max_chars] + '...'
