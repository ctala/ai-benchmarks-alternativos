# Claude Opus 5 Fast — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.99 | quality: 8.28
- latency_total: 8.416s | tokens_per_second: 243.4
- input_tokens: 154 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales.


## Respuesta completa

## Implementación

```python
"""
Cliente mínimo para la API de productos.
Solo requiere: httpx (+ stdlib).
"""

from __future__ import annotations

import json
import logging
import random
import time
from typing import Any, Iterable

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
DEFAULT_TIMEOUT = 10.0          # segundos (connect + read + write + pool)
MAX_ATTEMPTS = 3                # 1 intento inicial + 2 reintentos
BACKOFF_BASE = 0.5              # 0.5s -> 1s -> 2s (+ jitter)
MAX_BACKOFF = 30.0

# Solo estos códigos just