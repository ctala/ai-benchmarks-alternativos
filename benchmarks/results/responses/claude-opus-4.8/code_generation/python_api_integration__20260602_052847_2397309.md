# Claude Opus 4.8 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.08 | quality: 9.52
- latency_total: 19.259s | tokens_per_second: 97.1
- input_tokens: 154 | output_tokens: 1871
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función para obtener productos filtrados

```python
import httpx
import time


def fetch_filtered_products(
    token: str,
    *,
    min_price: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0,
    base_backoff: float = 1.0,
) -> list[dict]:
    """
    Obtiene productos desde la API, filtra por precio y retorna campos seleccionados.

    Args:
        token: Bearer token para autenticación.
        min_price: Precio mínimo (exclusivo) para filtrar productos.
        max_retries: Número máximo de intentos.
        timeout: Timeout en segundos para la petición.
        base_backoff: Tiempo base (segundos) para el backoff exponencial.

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        httpx.HTTPError: Si todos los intentos fallan.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    last_exception: Exception | None = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

            products = response.json()

            return [
                {
                    "id": p["id"],
                    "name": p["name"],
                    "price": p["price"],
                }
                for p in products
                if p.get("price", 0) > min_price
            ]

        except (httpx.TransportError, httpx.TimeoutException, httpx.HTTPStatusError) as exc:
            last_exception = exc

            # No reintentar errores de cliente 4xx (excepto 429)
            if isinstance(exc, httpx.HTTPStatusError):
                status = exc.response.status_code
                if 400 <= status < 500 and status != 429:
                    raise

            # Si fue el último intento, propagar el error
            if attempt == max_retries - 1:
                break

            # Backoff exponencial: 1s, 2s, 4s...
            wait = base_backoff * (2 ** attempt)
            time.sleep(wait)

    # Si llegamos aquí, todos los intentos fallaron
    raise httpx.HTTPError(
        f"Falló tras {max_retries} intentos: {last_exception}"
    )
```

## Versión asíncrona

Si prefieres usar `async`/`await`:

```python
import httpx
import asyncio


async def fetch_filtered_products_async(
    token: str,
    *,
    min_price: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0,
    base_backoff: float = 1.0,
) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Exception | None = None

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                products = response.json()

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > min_price
                ]

            except (httpx.TransportError, httpx.TimeoutException, httpx.HTTPStatusError) as exc:
                last_exception = exc

                if isinstance(exc, httpx.HTTPStatusError):
                    status = exc.response.status_code
                    if 400 <= status < 500 and status != 429:
                        raise

                if attempt == max_retries - 1:
                    break

                await asyncio.sleep(base_backoff * (2 ** attempt))

    raise httpx.HTTPError(f"Falló tras {max_retries} intentos: {last_exception}")
```

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        products = fetch_filtered_products("mi-token-secreto")
        for product in products:
            print(f"{product['id']}: {product['name']} - ${product['price']}")
    except httpx.HTTPError as e:
        print(f"Error al obtener productos: {e}")
```

## Notas sobre las decisiones de diseño

| Requisito | Implementación |
|-----------|----------------|
| **Timeout 10s** | `httpx.Client(timeout=timeout)` con valor por defecto `10.0` |
| **Retry x3** | Bucle `for attempt in range(max_retries)` |
| **Backoff exponencial** | `base_backoff * (2 ** attempt)` → 1s, 2s, 4s |
| **Errores de red** | Captura `TransportError` y `TimeoutException` |
| **Filtrado** | List comprehension con `if p.get("price", 0) > min_price` |

**Consideraciones adicionales:**

- **No se reintentan errores 4xx** (salvo `429 Too Many Requests`), porque un error de autenticación o petición mal formada no se solucionará reintentando.
- Uso de `p.get("price", 0)` para evitar `KeyError` si algún producto no trae el campo `price`.
- Si necesitas validar que existan `id` y `name` antes de incluirlos, puedes agregar una condición extra al filtro.

¿Quieres que agregue **jitter** al backoff para evitar el efecto "thundering herd" en escenarios de alta concurrencia?