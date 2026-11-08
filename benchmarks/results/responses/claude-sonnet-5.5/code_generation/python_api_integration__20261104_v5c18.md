# Claude Sonnet 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.91 | quality: 9.32
- latency_total: 16.3s | tokens_per_second: 156.6
- input_tokens: 156 | output_tokens: 2552
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
import logging
import time

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class ProductsAPIError(Exception):
    """Error al obtener productos de la API."""


def get_expensive_products(
    token: str,
    min_price: float = 100,
    max_attempts: int = 3,
    base_delay: float = 1.0,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos con precio > min_price.

    Retorna una lista de dicts con solo {id, name, price}.
    Reintenta con backoff exponencial (1s, 2s, ...) ante errores de red,
    timeouts y respuestas 429/5xx. Lanza ProductsAPIError si falla.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    data = None
    last_exc: Exception | None = None

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                data = response.json()
                break

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                if status not in RETRYABLE_STATUS:
                    # 400, 401, 403, 404...: reintentar no sirve
                    raise ProductsAPIError(
                        f"Error HTTP no recuperable: {status}"
                    ) from exc
                last_exc = exc

            except httpx.TransportError as exc:
                # Incluye TimeoutException, ConnectError, ReadError, etc.
                last_exc = exc

            except ValueError as exc:
                # La respuesta no es JSON válido
                raise ProductsAPIError("La respuesta no es JSON válido") from exc

            if attempt < max_attempts:
                delay = base_delay * 2 ** (attempt - 1)
                logger.warning(
                    "Intento %d/%d falló (%r). Reintentando en %.1fs",
                    attempt, max_attempts, last_exc, delay,
                )
                time.sleep(delay)
        else:
            raise ProductsAPIError(
                f"Falló tras {max_attempts} intentos: {last_exc!r}"
            ) from last_exc

    # Acepta tanto una lista directa como {"products": [...]}
    items = data.get("products", []) if isinstance(data, dict) else data
    if not isinstance(items, list):
        raise ProductsAPIError("Formato de respuesta inesperado")

    result = []
    for item in items:
        try:
            if float(item["price"]) > min_price:
                result.append(
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                )
        except (KeyError, TypeError, ValueError):
            logger.debug("Producto ignorado por datos inválidos: %r", item)

    return result
```

**Ejemplo de uso:**

```python
try:
    products = get_expensive_products("mi_token_secreto")
    print(products)
except ProductsAPIError as e:
    print(f"No se pudieron obtener los productos: {e}")
```

**Decisiones de diseño:**

- **Timeout:** `httpx.Client(timeout=10.0)` aplica 10 s a conexión, lectura, escritura y pool.
- **Qué se reintenta:** errores de transporte (`httpx.TransportError`, que incluye timeouts y fallos de conexión) y códigos 429/500/502/503/504. Los errores 4xx como 401 o 404 fallan de inmediato, porque reintentarlos no los arregla.
- **Backoff:** espera 1 s tras el primer fallo y 2 s tras el segundo, y no duerme después del último intento. Si quieres evitar que varios clientes reintenten sincronizados, puedes añadir jitter con `random.uniform` (de la biblioteca estándar).
- **Errores:** todo se unifica en `ProductsAPIError`, con la excepción original encadenada (`from exc`) para depurar.
- **Datos malformados:** los productos sin `price`, `id` o `name`, o con un precio no numérico, se ignoran en lugar de romper toda la función.
- **Supuesto:** la API devuelve una lista de productos o un objeto `{"products": [...]}`. Si el formato real es otro, ajusta la parte de `items`.

Si lo necesitas asíncrono, la estructura es igual: `httpx.AsyncClient`, `await client.get(...)` y `await asyncio.sleep(delay)`.