# GPT-OSS 120B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.66 | quality: 9.52
- latency_total: 29.824s | tokens_per_second: 46.3
- input_tokens: 165 | output_tokens: 1380
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import List, Dict, Any

import httpx


def get_expensive_products(
    token: str,
    *,
    url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_factor: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Fetches the product list from ``url`` using a Bearer token, filters the
    products whose ``price`` is greater than ``price_threshold`` and returns a
    simplified list containing only ``id``, ``name`` and ``price`` fields.

    Features
    --------
    * **Timeout** – each request is limited to ``timeout`` seconds.
    * **Retry with exponential back‑off** – on network errors or timeouts the
      request is retried up to ``max_retries`` times.  The delay between attempts
      follows ``backoff_factor * (2 ** attempt)`` seconds (1 s, 2 s, 4 s …).
    * **Error handling** – network‑related errors (connection problems,
      DNS failures, timeouts) and non‑2xx HTTP responses are caught and logged.
      After the last retry an empty list is returned (you may raise an exception
      instead if that fits your use‑case).

    Parameters
    ----------
    token: str
        Bearer token used for authentication.
    url: str, optional
        API endpoint that returns a JSON array of products.
    price_threshold: float, optional
        Minimum price a product must have to be kept.
    timeout: float, optional
        Request timeout in seconds (passed to ``httpx``).
    max_retries: int, optional
        Maximum number of attempts (the first try + ``max_retries-1`` retries).
    backoff_factor: float, optional
        Base factor for exponential back‑off (in seconds).

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries, each with keys ``id``, ``name`` and ``price``.
    """
    headers = {"Authorization": f"Bearer {token}"}
    attempt = 0

    while attempt < max_retries:
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Raise for HTTP errors (e.g. 4xx/5xx)
                response.raise_for_status()
                products = response.json()            # expecting a list of dicts

            # ------------------------------------------------------------------
            # Filter & reshape
            # ------------------------------------------------------------------
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > price_threshold
            ]
            return filtered

        # ----------------------------------------------------------------------
        # Network‑related errors (including timeout) and HTTP status errors
        # ----------------------------------------------------------------------
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            attempt += 1
            # If we exhausted retries, log and break
            if attempt >= max_retries:
                print(f"[ERROR] Request failed after {attempt} attempts: {exc}")
                break

            # Exponential back‑off before the next try
            backoff = backoff_factor * (2 ** (attempt - 1))
            print(
                f"[WARN] Attempt {attempt}/{max_retries} failed ({exc}). "
                f"Retrying in {backoff:.1f}s..."
            )
            time.sleep(backoff)

    # If we reach this point all attempts failed → return empty list
    return []


# --------------------------------------------------------------------------
# Example usage
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # Replace with a real token
    MY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

    expensive_products = get_expensive_products(MY_TOKEN)
    print(f"Found {len(expensive_products)} expensive products:")
    for p in expensive_products:
        print(p)
```

### Qué hace el código

| Paso | Acción |
|------|--------|
| **1** | Prepara los encabezados con `Authorization: Bearer <token>`. |
| **2** | Abre un cliente `httpx` con timeout de 10 s (configurable). |
| **3** | Intenta la petición `GET`. Si la respuesta no es 2xx, `raise_for_status()` lanza `HTTPStatusError`. |
| **4** | Convierte la respuesta JSON (se asume que es una lista de objetos). |
| **5** | Filtra los productos cuyo campo `price` supera `price_threshold` (100 por defecto) y crea una lista de diccionarios con solo `id`, `name` y `price`. |
| **6** | Captura cualquier `httpx.RequestError` (incluye timeout) o `HTTPStatusError`, aplica un back‑off exponencial y vuelve a intentar hasta `max_retries`. |
| **7** | Si después de los reintentos sigue fallando, devuelve `[]` y muestra un mensaje de error. |

Todo está implementado solo con la biblioteca estándar de Python y `httpx`, sin dependencias externas adicionales.