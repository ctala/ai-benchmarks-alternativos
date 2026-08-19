# Claude Fable 5 — code_generation/python_api_integration

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.41 | quality: 9.08
- latency_total: 16.852s | tokens_per_second: 79.5
- input_tokens: 154 | output_tokens: 1339
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import logging

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT = 10.0
MAX_RETRIES = 3
BACKOFF_BASE = 1.0  # segundos: 1s, 2s, 4s


def get_expensive_products(token: str, min_price: float = 100.0) -> list[dict]:
    """
    Obtiene productos de la API y retorna los que tienen precio > min_price.

    Args:
        token: Bearer token para autenticación.
        min_price: Precio mínimo para filtrar (exclusivo).

    Returns:
        Lista de dicts con las claves: id, name, price.

    Raises:
        httpx.HTTPStatusError: Si la API responde con error 4xx/5xx tras los reintentos.
        httpx.RequestError: Si falla la conexión tras agotar los reintentos.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with httpx.Client(timeout=TIMEOUT) as client:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                products = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > min_price
            ]

        except httpx.HTTPStatusError as exc:
            # Errores 4xx no se reintentan (el problema no es transitorio)
            if exc.response.status_code < 500:
                logger.error("Error del cliente %s: %s", exc.response.status_code, exc)
                raise
            last_exception = exc
            logger.warning(
                "Intento %d/%d falló con status %d",
                attempt, MAX_RETRIES, exc.response.status_code,
            )

        except (httpx.TimeoutException, httpx.RequestError) as exc:
            last_exception = exc
            logger.warning("Intento %d/%d falló: %s", attempt, MAX_RETRIES, exc)

        # Backoff exponencial antes del siguiente intento
        if attempt < MAX_RETRIES:
            wait = BACKOFF_BASE * (2 ** (attempt - 1))
            logger.info("Reintentando en %.1f segundos...", wait)
            time.sleep(wait)

    raise last_exception
```

**Ejemplo de uso:**

```python
try:
    products = get_expensive_products("mi_token_secreto")
    for p in products:
        print(f"{p['id']}: {p['name']} - ${p['price']}")
except httpx.HTTPStatusError as e:
    print(f"Error de la API: {e.response.status_code}")
except httpx.RequestError as e:
    print(f"Error de red: {e}")
```

**Detalles de diseño:**

- **Timeout de 10s**: aplicado globalmente al cliente (conexión + lectura).
- **Backoff exponencial**: espera 1s → 2s antes de los reintentos 2 y 3.
- **Errores 4xx no se reintentan**: si el token es inválido (401) o la ruta no existe (404), reintentar es inútil. Solo se reintentan errores 5xx, timeouts y fallos de red.
- **Filtrado seguro**: `p.get("price", 0)` evita `KeyError` si algún producto no tiene precio.
- **Excepción final**: si se agotan los intentos, se relanza la última excepción para que el llamador decida qué hacer.

Si necesitas una versión **async** (con `httpx.AsyncClient` y `asyncio.sleep`), avísame y te la preparo.