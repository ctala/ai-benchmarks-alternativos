# Claude Opus 5 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.04 | quality: 8.48
- latency_total: 23.118s | tokens_per_second: 88.6
- input_tokens: 154 | output_tokens: 2048
- judge_score: 4.2 | justificación: 

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

## Código

```python
"""
Cliente mínimo para /products con retry + backoff exponencial.
Solo requiere httpx (y stdlib).
"""

from __future__ import annotations

import logging
import random
import time
from typing import Any, Iterable

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
DEFAULT_TIMEOUT = 10.0          # segundos, por intento
MAX_ATTEMPTS = 3                # 1 intento inicial + 2 reintentos
BACKOFF_BASE = 0.5              # 0.5s, 1s, 2s ... (+ jitter)
BACKOFF_MAX = 10.0

# Solo estos status justifican reintentar; un 401/404 no se arregla repitiendo.
RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})


class ProductFetchError(RuntimeError):
    """No se pudo obtener el catálogo tras agotar los reintentos."""


def fetch_expensive_products(
    token: str,
    *,
    min_price: float = 100.0,
    url: str = API_URL,
    timeout: float = DEFAULT_TIMEOUT,
    max_attempts: int = MAX_ATTEMPTS,
    client: httpx.Client | None = None,
) -> list[dict[str, Any]]:
    """
    Devuelve [{"id": ..., "name": ..., "price": ...}, ...] con price > min_price.

    Lanza ProductFetchError si la red/servidor falla tras `max_attempts`,
    o httpx.HTTPStatusError para errores 4xx no recuperables (401, 404, ...).
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    owns_client = client is None
    client = client or httpx.Client(timeout=httpx.Timeout(timeout))
    try:
        response = _get_with_retry(client