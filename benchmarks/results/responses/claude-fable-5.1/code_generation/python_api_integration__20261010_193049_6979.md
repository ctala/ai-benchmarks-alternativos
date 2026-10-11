# Claude Fable 5.1 — code_generation/python_api_integration

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.47 | quality: 9.28
- latency_total: 22.517s | tokens_per_second: 88.8
- input_tokens: 156 | output_tokens: 2000
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
import time
import logging
from typing import Any

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_SECONDS = 10.0
MAX_ATTEMPTS = 3
MIN_PRICE = 100
BASE_BACKOFF = 1.0  # segundos: 1s, 2s, 4s


class ProductsFetchError(Exception):
    """Error final tras agotar los reintentos o por respuesta inválida."""


def fetch_expensive_products(token: str, min_price: float = MIN_PRICE) -> list[dict[str, Any]]:
    """
    Obtiene productos con precio > min_price desde la API.

    Args:
        token: Bearer token para autenticación.
        min_price: Umbral de precio (exclusivo).

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        ProductsFetchError: si fallan todos los intentos o la respuesta no es válida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    last_error: Exception | None = None

    with httpx.Client(timeout=TIMEOUT_SECONDS, headers=headers) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(API_URL)

                # Errores 5xx son reintentables; 4xx no (salvo 429)
                if response.status_code >= 500 or response.status_code == 429:
                    raise httpx.HTTPStatusError(
                        f"Respuesta reintentable: {response.status_code}",
                        request=response.request,
                        response=response,
                    )

                response.raise_for_status()  # lanza para 4xx -> no se reintenta
                data = response.json()

                return _filter_and_project(data, min_price)

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                # Timeout, DNS, conexión rechazada, etc.
                last_error = exc
                logger.warning("Intento %d/%d: error de red/timeout: %s", attempt, MAX_ATTEMPTS, exc)

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status >= 500 or status == 429:
                    last_error = exc
                    logger.warning("Intento %d/%d: HTTP %d, reintentando", attempt, MAX_ATTEMPTS, status)
                else:
                    # 4xx (401, 403, 404...) no tiene sentido reintentar
                    raise ProductsFetchError(f"Error HTTP no reintentable: {status}") from exc

            except ValueError as exc:
                # JSON inválido o estructura inesperada
                raise ProductsFetchError(f"Respuesta inválida: {exc}") from exc

            # Backoff exponencial antes del siguiente intento (no esperar tras el último)
            if attempt < MAX_ATTEMPTS:
                wait = BASE_BACKOFF * (2 ** (attempt - 1))
                logger.info("Esperando %.1fs antes de reintentar...", wait)
                time.sleep(wait)

    raise ProductsFetchError(
        f"No se pudo obtener productos tras {MAX_ATTEMPTS} intentos"
    ) from last_error


def _filter_and_project(data: Any, min_price: float) -> list[dict[str, Any]]:
    """Filtra por precio y proyecta solo {id, name, price}."""
    # Soporta tanto una lista directa como {"products": [...]} / {"data": [...]}
    if isinstance(data, dict):
        products = data.get("products") or data.get("data") or []
    elif isinstance(data, list):
        products = data
    else:
        raise ValueError("Formato de respuesta no reconocido")

    result = []
    for p in products:
        if not isinstance(p, dict):
            continue
        price = p.get("price")
        if isinstance(price, (int, float)) and price > min_price:
            result.append({"id": p.get("id"), "name": p.get("name"), "price": price})

    return result


# ---- Ejemplo de uso ----
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        products = fetch_expensive_products(token="mi_token_secreto")
        for prod in products:
            print(prod)
    except ProductsFetchError as e:
        print(f"Fallo: {e}")
```

**Notas sobre la implementación:**

- **Timeout de 10 s**: configurado a nivel de `httpx.Client`, aplica a conexión, lectura y escritura.
- **Reintentos**: solo ante errores de red, timeouts, `5xx` y `429`. Los `4xx` (p. ej. `401` por token inválido) fallan inmediatamente, ya que reintentar no los arreglaría.
- **Backoff exponencial**: 1 s → 2 s → 4 s (no espera tras el último intento). Si quieres añadir *jitter* para evitar "thundering herd", puedes sumar `random.uniform(0, 0.5)` al `wait`.
- **Respuesta flexible**: acepta una lista directa o un dict con clave `products`/`data`; ajusta `_filter_and_project` según el contrato real de tu API.
- **Versión async**: si lo necesitas, basta con cambiar a `httpx.AsyncClient`, `await client.get(...)` y `await asyncio.sleep(wait)`.