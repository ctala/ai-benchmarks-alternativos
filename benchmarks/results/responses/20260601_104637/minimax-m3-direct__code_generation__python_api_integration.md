# MiniMax M3 (directo / sub) — code_generation/python_api_integration

- model_id: `MiniMax-M3`
- success: True  | final: 7.1 | quality: 8.88
- latency_total: 168.482s | tokens_per_second: 34.9
- input_tokens: 268 | output_tokens: 5872
- judge_score: 4.2 | justificación: 

## Respuesta completa

<think>
The user wants a Python function that:
1. Makes a GET request to https://api.example.com/products with Bearer token authentication
2. Filters products with price > 100
3. Returns a list of dicts with only {id, name, price}
4. Handles network errors and timeout (10 seconds)
5. Includes retry with exponential backoff (max 3 attempts)
6. Uses httpx and no other external dependencies

Let me write a clean, well-documented solution. I should think about:
- How to structure the retry logic with exponential backoff
- How to handle different types of errors (network, timeout, HTTP status codes)
- How to filter products properly (handle missing fields, different price formats)
- How to make the code clean and readable

Let me think about the exponential backoff: typically you start with 1s, then 2s, then 4s, or could be 1, 2, 4 or use 2^attempt. A common pattern is to wait `base * (2 ** attempt)` seconds. With max 3 attempts, we'd have waits of 1s, 2s between retries.

For the retries, I should retry on:
- Network errors (httpx.RequestError)
- Timeout errors (httpx.TimeoutException)
- 5xx server errors
- Maybe 429 (rate limit)

But NOT retry on:
- 4xx client errors (except 429)
- Successful responses

For the price filtering, I should handle:
- Products where price is None or missing (skip them)
- Products where price is not numeric
- Decimal vs float

Let me write the code:

```python
import httpx
from typing import List, Dict, Any, Optional
import time


def get_expensive_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    max_attempts: int = 3,
    timeout: float = 10.0,
) -> List[Dict[str, Any]]:
    """
    Fetch products from an API and return those with price > min_price.
    
    Args:
        token: Bearer token for authentication.
        base_url: API endpoint URL.
        min_price: Minimum price threshold.
        max_attempts: Maximum number of retry attempts.
        timeout: Request timeout in seconds.
    
    Returns:
        List of dicts with keys: id, name, price.
    
    Raises:
        httpx.HTTPError: If all retry attempts fail.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Optional[Exception] = None
    
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                data = response.json()
                break  # Exit retry loop on success
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            last_exception = e
            if attempt == max_attempts:
                raise
            wait = 2 ** (attempt - 1)  # 1, 2, 4 seconds
            time.sleep(wait)
        except httpx.HTTPStatusError as e:
            # Retry on 5xx and 429, but not on other 4xx
            last_exception = e
            if e.response.status_code < 500 and e.response.status_code != 429:
                raise
            if attempt == max_attempts:
                raise
            wait = 2 ** (attempt - 1)
            time.sleep(wait)
    
    products = data if isinstance(data, list) else data.get("products", [])
    
    result = []
    for product in products:
        try:
            price = float(product.get("price", 0))
        except (TypeError, ValueError):
            continue
        if price > min_price:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price,
            })
    
    return result
```

Wait, there's a bug. If the request succeeds, I use `break` to exit the loop, but `data` is defined inside the `with` block. Let me fix that.

Actually, looking again, the `break` only breaks out of the for loop, but `data` is assigned within the try block. I need to make sure `data` is available after the loop. Since the `break` exits the loop while still in the try block, the assignment happens before the break... wait no, the break is after the assignment, so `data` would be in scope. But the variable might be undefined if the loop completes without break (all attempts failed and raised).

Let me restructure to be cleaner:

```python
def get_expensive_products(...) -> List[Dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}"}
    data = None
    last_exception = None
    
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                data = response.json()
        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as e:
            last_exception = e
            # Decide whether to retry
            if isinstance(e, httpx.HTTPStatusError):
                status = e.response.status_code
                if status < 500 and status != 429:
                    raise  # Don't retry on 4xx (except 429)
            if attempt == max_attempts:
                raise
            wait = 2 ** (attempt - 1)
            time.sleep(wait)
        else:
            break  # Success, exit retry loop
    
    if data is None:
        # This shouldn't happen because we either return data or raise
        raise last_exception if last_exception else RuntimeError("No data received")
    
    # ... filter and return
```

Hmm, this is getting a bit complex. Let me think about a cleaner way.

Actually, the `else` on the try/except runs only if no exception. But the data is already assigned inside the `with` block, so the `else` is unnecessary if we just check after the loop. Let me use a different approach:

```python
def get_expensive_products(...) -> List[Dict[str, Any]]:
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                data = response.json()
                return _filter_products(data, min_price)
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            if attempt == max_attempts:
                raise httpx.RequestError(f"All {max_attempts} attempts failed") from e
            _wait_exponential(attempt)
        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            if status < 500 and status != 429:
                raise  # Client error, don't retry
            if attempt == max_attempts:
                raise
            _wait_exponential(attempt)
    
    return []  # Shouldn't reach here
```

This is cleaner. Let me also think about whether I should validate the JSON structure. The user said the API returns products, but doesn't specify the structure. Common patterns:
- Direct list: `[{...}, {...}]`
- Wrapped: `{"products": [...]}`
- Wrapped with data: `{"data": [...]}`

I should handle both. Let me make a helper function.

Also, I should think about whether to log retries. Since the user said "no external dependencies", logging is fine (it's in stdlib). But to keep it simple, maybe just print or use Python's logging.

Let me write the final version with proper structure:

```python
import httpx
import time
import logging
from typing import Any

logger = logging.getLogger(__name__)


def fetch_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    *,
    max_attempts: int = 3,
    timeout: float = 10.0,
    base_backoff: float = 1.0,
) -> list[dict[str, Any]]:
    """
    Get products priced above `min_price` from a paginated-style API.
    
    Uses Bearer-token auth, retries failed network/5xx requests with
    exponential backoff, and times out individual requests after 10s.
    """
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
    
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                payload = response.json()
                return _extract_expensive(payload, min_price)
        
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            logger.warning("Attempt %d failed (network/timeout): %s", attempt, exc)
        
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            last_exc = exc
            # Don't retry on client errors (except 429 rate limit)
            if 400 <= status < 500 and status != 429:
                logger.error("Client error %d, not retrying", status)
                raise
            logger.warning("Attempt %d failed (HTTP %d)", attempt, status)
        
        if attempt < max_attempts:
            wait = base_backoff * (2 ** (attempt - 1))
            logger.info("Backing off for %.1fs before retry", wait)
            time.sleep(wait)
    
    # All attempts failed
    raise RuntimeError(
        f"Failed to fetch products after {max_attempts} attempts"
    ) from last_exc


def _extract_expensive(payload: Any, min_price: float) -> list[dict[str, Any]]:
    """Pull out the products list and filter by price."""
    # Support either a bare list or a dict with a 'products'/'data' key
    if isinstance(payload, list):
        products = payload
    elif isinstance(payload, dict):
        products = payload.get("products") or payload.get("data") or []
    else:
        products = []
    
    result = []
    for item in products:
        if not isinstance(item, dict):
            continue
        try:
            price = float(item.get("price"))
        except (TypeError, ValueError):
            continue
        if price > min_price:
            result.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "price": price,
            })
    return result
```

This looks good. Let me also add a small example of how to use it.

Actually, let me reconsider the structure once more. The user wants:
1. GET to the URL with Bearer auth
2. Filter price > 100
3. Return list of {id, name, price}
4. Handle network errors and timeout (10s)
5. Retry with exponential backoff (max 3 attempts)
6. Use httpx only

I think my solution covers all of these. Let me also think about:
- Should I add jitter to the backoff? It's a nice-to-have for production but the user didn't ask for it. I'll keep it simple.
- Should `min_price` be configurable? The user said "precio > 100" so 100 is the threshold. I'll make it a parameter with default 100.
- Should I add type hints? Yes, this is good practice.
- Should I use `httpx.Client` or `httpx.get()`? Using a Client is better practice even for single requests.

One more thought: in the response handling, what if the response is empty or the JSON parsing fails? I should catch `json.JSONDecodeError` too. Actually, `response.json()` raises `json.JSONDecodeError` which is a subclass of `ValueError`. Should I retry on that? Probably not, since it's a server bug. Let me let it propagate.

Let me also think about: what if `raise_for_status()` raises? That's `httpx.HTTPStatusError` which I catch. Good.

What about connection errors? Those are `httpx.ConnectError` which is a subclass of `httpx.NetworkError`. Good, my except clause catches it.

What about read timeouts? `httpx.ReadTimeout` is a subclass of `httpx.TimeoutException`. Good.

I think the solution is solid. Let me also write a small example usage at the end.

Let me also make sure I handle the case where `data` is None properly. In my current code, if all attempts fail, I raise RuntimeError, so the function will always either return a list or raise. Good.

One thing I want to double-check: the retry should only happen on transient errors. Common pattern:
- Network errors (connection, DNS, etc.) -> retry
- Timeouts -> retry
- 5xx server errors -> retry
- 429 rate limit -> retry (with possibly longer wait)
- 4xx client errors (other) -> don't retry
- 2xx success -> done
- 3xx redirects -> httpx follows automatically

I think my logic is correct.

Let me finalize the code. I'll add a `if __name__ == "__main__"` block or just an example.

Actually, I realized I should also consider: what if the API requires more configuration, like pagination? The user didn't mention it, so I'll assume the response contains all the products. If pagination is needed, that's a follow-up.

Let me also clean up the imports and make sure everything is consistent.

Final version:

```python
"""
Fetch products priced above a threshold from a Bearer-protected API.

Uses httpx for HTTP, exponential backoff for retries, and a 10-second
per-request timeout. No external dependencies beyond httpx.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)


def get_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    *,
    max_attempts: int = 3,
    timeout: float = 10.0,
    initial_backoff: float = 1.0,
) -> list[dict[str, Any]]:
    """
    Fetch products from `url` and return those priced above `min_price`.
    
    Each request uses Bearer-token authentication. Network errors,
    timeouts, 5xx responses, and 429 (rate-limited) responses are
    retried up to `max_attempts` times with exponential backoff.
    Other 4xx errors are surfaced immediately.
    
    Args:
        token: Bearer token for the Authorization header.
        url: Endpoint to GET.
        min_price: Lower bound (exclusive) for `price`.
        max_attempts: Total attempts before giving up (>=1).
        timeout: Per-request timeout in seconds.
        initial_backoff: Wait time before the second attempt; doubles
            on each subsequent attempt.
    
    Returns:
        A list of dicts with keys ``id``, ``name``, and ``price``.
    
    Raises:
        httpx.HTTPError: On network failure or non-retryable HTTP error
            after all attempts are exhausted.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    last_exc: httpx.HTTPError | None = None
    
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                return _filter_by_price(response.json(), min_price)
        
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            logger.warning(
                "Attempt %d/%d failed (network/timeout): %s",
                attempt, max_attempts, exc,
            )
        
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            last_exc = exc
            # Retry only on 5xx or 429; surface other 4xx immediately.
            if status < 500 and status != 429:
                logger.error("Non-retryable HTTP %d, aborting", status)
                raise
            logger.warning(
                "Attempt %d/%d failed (HTTP %d)",
                attempt, max_attempts, status,
            )
        
        # Don't sleep after the final attempt
        if attempt < max_attempts:
            wait = initial_backoff * (2 ** (attempt - 1))
            logger.info("Sleeping %.1fs before retry", wait)
            time.sleep(wait)
    
    raise RuntimeError(
        f"Exhausted {max_attempts} attempts fetching {url}"
    ) from last_exc


def _filter_by_price(payload: Any, min_price: float) -> list[dict[str, Any]]:
    """
    Normalize the API payload to a list and keep only items with
    ``price > min_price``. Each kept item is reduced to ``id``,
    ``name``, and a numeric ``price``.
    """
    if isinstance(payload, list):
        items = payload
    elif isinstance(payload, dict):
        items = payload.get("products") or payload.get("data") or []
    else:
        items = []
    
    result: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        try:
            price = float(item["price"])
        except (KeyError, TypeError, ValueError):
            continue
        if price > min_price:
            result.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "price": price,
            })
    return result


# Example usage
if __name__ == "__main__":
    # In real code, load the token from a secret manager or env var
    api_token = "your-bearer-token-here"
    
    products = get_expensive_products(api_token)
    for p in products:
        print(f"{p['id']}: {p['name']} - ${p['price']:.2f}")
```

I think this is good. Let me also add a note about the backoff schedule: with `initial_backoff=1.0` and 3 attempts, the wait times are 1s and 2s (no wait after the 3rd).

Let me also think about whether `httpx.HTTPError` is the right base class. It is - it's the base of all httpx exceptions. Good.

One more thing: I use `from __future__ import annotations` so I can use `list[dict[str, Any]]` as type hints even on Python 3.8. The `httpx.HTTPError | None` syntax requires Python 3.10+. Let me use `Optional[httpx.HTTPError]` to be safe, or use the `from __future__ import annotations` (which I have) - actually, with `from __future__ import annotations`, all annotations are strings, so the runtime syntax doesn't matter. So `httpx.HTTPError | None` is fine. Let me verify... yes, with `from __future__ import annotations`, annotations are not evaluated at runtime, so any syntax that works as a string in Python's AST works. So I can use `X | Y` syntax. Good.

Actually wait, the `if __name__ == "__main__"` block will be run as Python code. The `print` and other things work fine. The type hints are not evaluated, so we're good.

Let me finalize and present this solution. I'll structure my response with:
1. Brief explanation of the approach
2. The code
3. Maybe a quick example

I think the code is well-commented and self-explanatory. Let me present it cleanly.
</think>
Aquí tienes una solución completa, documentada y lista para usar. Usa solo `httpx` (que ya debes tener instalada) y la biblioteca estándar.

```python
"""
Fetch products priced above a threshold from a Bearer-protected API.

Usa httpx para HTTP, reintentos con backoff exponencial y timeout
de 10 s por petición. Sin dependencias externas más allá de httpx.
"""

from __future__ import annotations

import logging
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)


def get_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    *,
    max_attempts: int = 3,
    timeout: float = 10.0,
    initial_backoff: float = 1.0,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de `url` y devuelve los que cuestan más de `min_price`.

    Cada petición usa autenticación Bearer. Errores de red, timeouts,
    respuestas 5xx y 429 (rate limit) se reintentan hasta `max_attempts`
    veces con backoff exponencial. Otros errores 4xx se propagan
    inmediatamente.

    Args:
        token:             Bearer token para el header Authorization.
        url:               Endpoint a consultar (GET).
        min_price:         Umbral inferior (estricto) para `price`.
        max_attempts:      Número total de intentos (>= 1).
        timeout:           Timeout por petición, en segundos.
        initial_backoff:   Espera antes del 2º intento; se duplica
                           en cada reintento posterior.

    Returns:
        Lista de dicts con las claves ``id``, ``name`` y ``price``.

    Raises:
        httpx.HTTPError: Si se agotan los intentos o la API devuelve
                         un 4xx no reintentable.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    last_exc: httpx.HTTPError | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                return _filter_by_price(response.json(), min_price)

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            logger.warning(
                "Intento %d/%d falló (red/timeout): %s",
                attempt, max_attempts, exc,
            )

        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            last_exc = exc
            # Reintentar solo en 5xx o 429; otros 4xx son definitivos.
            if status < 500 and status != 429:
                logger.error("HTTP %d no reintentable, abortando", status)
                raise
            logger.warning(
                "Intento %d/%d falló (HTTP %d)",
                attempt, max_attempts, status,
            )

        # No dormir después del último intento.
        if attempt < max_attempts:
            wait = initial_backoff * (2 ** (attempt - 1))
            logger.info("Esperando %.1fs antes de reintentar", wait)
            time.sleep(wait)

    raise RuntimeError(
        f"Agotados los {max_attempts} intentos al llamar a {url}"
    ) from last_exc


def _filter_by_price(payload: Any, min_price: float) -> list[dict[str, Any]]:
    """
    Normaliza el payload de la API a una lista y conserva únicamente
    los elementos con ``price > min_price``. Cada elemento conservado
    se reduce a ``id``, ``name`` y un ``price`` numérico.
    """
    # Acepta tanto una lista cruda como un dict con clave "products"/"data".
    if isinstance(payload, list):
        items = payload
    elif isinstance(payload, dict):
        items = payload.get("products") or payload.get("data") or []
    else:
        items = []

    result: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        try:
            price = float(item["price"])
        except (KeyError, TypeError, ValueError):
            continue
        if price > min_price:
            result.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "price": price,
            })
    return result


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # En código real, carga el token de un secret manager o variable de entorno.
    api_token = "your-bearer-token-here"

    products = get_expensive_products(api_token)
    for p in products:
        print(f"{p['id']}: {p['name']} - ${p['price']:.2f}")
```

### Cómo cubre cada requisito

| Requisito | Implementación |
|---|---|
| **1. GET + Bearer** | `httpx.Client.get(url, headers={"Authorization": f"Bearer {token}"})` |
| **2. Filtro `price > 100`** | `if price > min_price:` en `_filter_by_price` (umbral configurable, por defecto 100) |
| **3. Solo `{id, name, price}`** | Se construye un dict nuevo por cada producto que pasa el filtro |
| **4. Errores de red y timeout (10 s)** | `httpx.Client(timeout=10.0)` + `except (httpx.TimeoutException, httpx.NetworkError)` |
| **5. Reintentos con backoff exponencial (máx. 3)** | Bucle de hasta 3 intentos, espera `1 s`, `2 s` entre ellos; reintenta también en 5xx y 429 |
| **6. Solo `httpx`** | `time` y `logging` son de la stdlib; nada más |

### Notas de diseño que quizás te interesen

- **Política de reintento**: solo se reintenta en errores *transitorios* (red, timeout, 5xx, 429). Los 4xx "duros" (401, 403, 404…) se propagan de inmediato porque reintentarlos no aporta nada.
- **Backoff**: `1 s → 2 s` con `initial_backoff=1.0` y 3 intentos. Si quieres jitter para evitar el "thundering herd" en producción, basta con añadir `random.uniform(0, wait)` antes del `time.sleep`.
- **Tolerancia a payloads variados**: la función auxiliar acepta tanto `[{...}, ...]` como `{"products": [...]}` o `{"data": [...]}`.
- **Defensiva con precios**: si `price` falta, es `None` o no se puede convertir a `float`, el producto simplemente se ignora en lugar de lanzar una excepción.
- **Cliente efímero**: se usa `httpx.Client` dentro de un `with` para que el socket se cierre siempre, incluso si la petición peta.