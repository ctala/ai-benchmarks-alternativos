# Claude Fable 5.1 — code_generation/python_api_integration

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.5 | quality: 9.32
- latency_total: 20.244s | tokens_per_second: 98.6
- input_tokens: 156 | output_tokens: 1996
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
BASE_BACKOFF_SECONDS = 1.0


class ProductsFetchError(Exception):
    """Error al obtener productos tras agotar los reintentos."""


def fetch_expensive_products(
    token: str,
    min_price: float = 100.0,
    url: str = API_URL,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y devuelve solo aquellos con precio > min_price.

    Retorna una lista de dicts con las claves: id, name, price.
    Reintenta hasta MAX_ATTEMPTS veces con backoff exponencial ante errores
    de red, timeout o respuestas 5xx.

    Raises:
        ProductsFetchError: si no se pudo obtener una respuesta válida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    last_error: Exception | None = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(url, headers=headers)

            # 5xx: error del servidor, vale la pena reintentar
            if response.status_code >= 500:
                raise httpx.HTTPStatusError(
                    f"Error del servidor: {response.status_code}",
                    request=response.request,
                    response=response,
                )

            # 4xx: error del cliente (token inválido, etc.), no reintentar
            response.raise_for_status()

            data = response.json()
            return _filter_products(data, min_price)

        except httpx.TimeoutException as exc:
            last_error = exc
            logger.warning("Timeout en intento %d/%d", attempt, MAX_ATTEMPTS)

        except httpx.HTTPStatusError as exc:
            if exc.response.status_code < 500:
                # Errores 4xx no se reintentan
                raise ProductsFetchError(
                    f"Error HTTP {exc.response.status_code}: {exc.response.text}"
                ) from exc
            last_error = exc
            logger.warning(
                "Error 5xx (%d) en intento %d/%d",
                exc.response.status_code, attempt, MAX_ATTEMPTS,
            )

        except httpx.RequestError as exc:
            # Errores de red: DNS, conexión rechazada, etc.
            last_error = exc
            logger.warning(
                "Error de red en intento %d/%d: %s", attempt, MAX_ATTEMPTS, exc
            )

        except ValueError as exc:
            # JSON inválido: no tiene sentido reintentar
            raise ProductsFetchError("La respuesta no es JSON válido") from exc

        # Backoff exponencial: 1s, 2s, 4s...
        if attempt < MAX_ATTEMPTS:
            wait = BASE_BACKOFF_SECONDS * (2 ** (attempt - 1))
            logger.info("Reintentando en %.1f segundos...", wait)
            time.sleep(wait)

    raise ProductsFetchError(
        f"No se pudo obtener productos tras {MAX_ATTEMPTS} intentos"
    ) from last_error


def _filter_products(data: Any, min_price: float) -> list[dict[str, Any]]:
    """Filtra productos con precio > min_price y proyecta solo id, name, price."""
    # Soporta tanto una lista directa como un objeto {"products": [...]}
    products = data.get("products", data) if isinstance(data, dict) else data

    if not isinstance(products, list):
        raise ProductsFetchError("Formato de respuesta inesperado")

    result = []
    for p in products:
        try:
            price = float(p["price"])
        except (KeyError, TypeError, ValueError):
            continue  # Ignorar productos sin precio válido

        if price > min_price:
            result.append({
                "id": p.get("id"),
                "name": p.get("name"),
                "price": price,
            })

    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        productos = fetch_expensive_products(token="mi_token_secreto")
        for prod in productos:
            print(prod)
    except ProductsFetchError as e:
        print(f"Error: {e}")
```

**Puntos clave de la implementación:**

- **Timeout**: `httpx.Client(timeout=10.0)` aplica 10 s a conexión, lectura y escritura.
- **Retry con backoff exponencial**: espera 1 s, 2 s y 4 s entre intentos (máximo 3). Solo se reintenta ante timeouts, errores de red (`httpx.RequestError`) y respuestas 5xx.
- **Errores no recuperables**: los 4xx (token inválido, 404, etc.) y el JSON malformado fallan de inmediato sin reintentar.
- **Filtrado**: ignora productos sin precio válido y devuelve solo `{id, name, price}` para los que superan el umbral.
- **Sin dependencias extra**: solo `httpx` y la biblioteca estándar.