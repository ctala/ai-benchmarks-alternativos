# KAT Coder Air v2.5 — code_generation/python_api_integration

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.02 | quality: 9.52
- latency_total: 4.971s | tokens_per_second: 185.9
- input_tokens: 113 | output_tokens: 924
- judge_score: 4.8 | justificación: 

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



```python
import httpx
import time
import logging

logger = logging.getLogger(__name__)

def get_expensive_products(token: str) -> list[dict]:
    """
    Fetches products from the API, filters those with price > 100,
    and returns a list of dicts with {id, name, price}.

    Args:
        token: Bearer authentication token.

    Returns:
        List of dicts containing id, name, and price for products
        whose price is greater than 100.

    Raises:
        httpx.HTTPError: If all retry attempts fail.
    """
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(
                    "https://api.example.com/products",
                    headers=headers,
                )
                response.raise_for_status()

            products = response.json()

            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]

            return filtered

        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError) as exc:
            logger.warning("Attempt %d/%d failed: %s", attempt, max_retries, exc)
            if attempt == max_retries:
                raise

        except httpx.HTTPStatusError as exc:
            # Retry only on server errors (5xx) or client errors that might be
            # transient (429 Too Many Requests)
            if exc.response.status_code in (429, 500, 502, 503, 504):
                logger.warning(
                    "Attempt %d/%d: HTTP %d — %s",
                    attempt, max_retries, exc.response.status_code, exc,
                )
                if attempt == max_retries:
                    raise
            else:
                raise

        # Exponential backoff: 1s, 2s, 4s
        wait = 2 ** (attempt - 1)
        logger.info("Retrying in %d second(s)...", wait)
        time.sleep(wait)

    # Should never reach here, but keeps the type checker happy
    return []
```

### Explicación

| Requisito | Implementación |
|---|---|
| **GET con Bearer token** | Header `Authorization: Bearer {token}` en cada request |
| **Filtro precio > 100** | Comprensión de lista que verifica `p["price"] > 100` |
| **Campos {id, name, price}** | Dict comprehension con solo esos tres campos |
| **Timeout 10s** | `httpx.Client(timeout=10.0)` |
| **Errores de red** | Captura `TimeoutException`, `ConnectError`, `NetworkError` |
| **Retry exponencial** | Backoff de `2^(attempt-1)` → 1s, 2s, 4s, máximo 3 intentos |

### Notas

- **Solo se retry en errores transitorios**: `429`, `5xx`, y errores de red/timeout. Errores `4xx` distintos (ej. `401`, `404`) se propagan de inmediato.
- **`with httpx.Client(...)`** cierra la conexión después de cada intento.
- Si la respuesta no es JSON o falta un campo, la excepción se propaga (puedes agregar un try/except adicional si quieres ser más permisivo).