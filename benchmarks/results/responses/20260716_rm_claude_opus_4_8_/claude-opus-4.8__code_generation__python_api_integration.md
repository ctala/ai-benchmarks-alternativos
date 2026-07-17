# Claude Opus 4.8 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.79 | quality: 9.52
- latency_total: 21.484s | tokens_per_second: 86.4
- input_tokens: 154 | output_tokens: 1856
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función para obtener productos filtrados

```python
import httpx
import time


def fetch_products(token: str) -> list[dict]:
    """
    Obtiene productos desde la API, filtra por precio > 100 y retorna
    una lista de dicts con {id, name, price}.

    Args:
        token: Bearer token para autenticación.

    Returns:
        Lista de dicts con las claves 'id', 'name' y 'price'.

    Raises:
        httpx.HTTPError: Si todos los reintentos fallan.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)

    max_retries = 3
    base_delay = 1.0  # segundos

    last_exception: Exception | None = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # lanza HTTPStatusError si 4xx/5xx

            products = response.json()

            # Filtrar y proyectar solo los campos requeridos
            return [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "price": p["price"],
                }
                for p in products
                if p.get("price", 0) > 100
            ]

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            # Errores transitorios: reintentar con backoff
            last_exception = exc
            _log_retry(attempt, max_retries, exc)

        except httpx.HTTPStatusError as exc:
            # Reintentar solo en errores del servidor (5xx)
            last_exception = exc
            if exc.response.status_code < 500:
                # 4xx: error del cliente, no tiene sentido reintentar
                raise
            _log_retry(attempt, max_retries, exc)

        # Backoff exponencial: 1s, 2s, 4s... (no dormir tras el último intento)
        if attempt < max_retries - 1:
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)

    # Se agotaron los reintentos
    raise httpx.HTTPError(
        f"No se pudo obtener productos tras {max_retries} intentos"
    ) from last_exception


def _log_retry(attempt: int, max_retries: int, exc: Exception) -> None:
    print(f"Intento {attempt + 1}/{max_retries} falló: {exc!r}")
```

## Uso

```python
if __name__ == "__main__":
    try:
        productos = fetch_products("mi_token_secreto")
        for p in productos:
            print(p)
    except httpx.HTTPError as e:
        print(f"Error al obtener productos: {e}")
```

## Notas de diseño

| Requisito | Implementación |
|-----------|----------------|
| **GET + Bearer** | `client.get()` con header `Authorization: Bearer <token>` |
| **Filtro precio > 100** | List comprehension con `if p.get("price", 0) > 100` |
| **Proyección de campos** | Se construye un dict nuevo con solo `id`, `name`, `price` |
| **Timeout 10s** | `httpx.Timeout(10.0)` |
| **Retry (max 3)** | Bucle `for attempt in range(3)` |
| **Backoff exponencial** | `base_delay * (2 ** attempt)` → 1s, 2s, 4s |

**Decisiones clave:**

- **No reintentar en errores 4xx**: un `401` (token inválido) o `404` no se resuelven reintentando, así que se propaga inmediatamente. Solo reintenta en errores de red, timeouts y `5xx`.
- **`raise ... from last_exception`**: preserva la cadena de excepciones para debugging.
- **`.get("price", 0)`**: evita `KeyError` si algún producto viene sin precio.

## Variante asíncrona (opcional)

Si trabajas en un contexto async:

```python
import asyncio
import httpx


async def fetch_products_async(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_retries, base_delay = 3, 1.0
    last_exc = None

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                resp = await client.get(url, headers=headers)
                resp.raise_for_status()
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in resp.json()
                    if p.get("price", 0) > 100
                ]
            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                last_exc = exc
            except httpx.HTTPStatusError as exc:
                last_exc = exc
                if exc.response.status_code < 500:
                    raise

            if attempt < max_retries - 1:
                await asyncio.sleep(base_delay * (2 ** attempt))

    raise httpx.HTTPError(f"Fallo tras {max_retries} intentos") from last_exc
```

¿Necesitas que agregue **jitter** al backoff (para evitar thundering herd) o soporte para paginación de la API?