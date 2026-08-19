# Claude Sonnet 5 — code_generation/python_api_integration

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.1 | quality: 9.52
- latency_total: 18.103s | tokens_per_second: 110.9
- input_tokens: 154 | output_tokens: 2008
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
from typing import List, Dict, Any, Optional

import httpx

logger = logging.getLogger(__name__)


def get_expensive_products(
    api_url: str = "https://api.example.com/products",
    token: str = "",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_base: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde una API REST, filtra los que tienen precio > price_threshold
    y retorna una lista de diccionarios con {id, name, price}.

    Implementa:
    - Autenticación Bearer token
    - Timeout de red (default 10s)
    - Retry con backoff exponencial (max 3 intentos por defecto)
    - Manejo de errores de red / timeout / HTTP

    Args:
        api_url: URL del endpoint de productos.
        token: Bearer token para autenticación.
        price_threshold: Precio mínimo (exclusivo) para filtrar.
        timeout: Timeout en segundos para la petición HTTP.
        max_retries: Número máximo de intentos.
        backoff_base: Segundos base para el cálculo de backoff exponencial.

    Returns:
        Lista de dicts con las claves 'id', 'name', 'price' de productos
        cuyo precio es mayor a price_threshold. Retorna lista vacía si
        todos los intentos fallan.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(api_url, headers=headers)
                response.raise_for_status()
                data = response.json()

            # Se asume que la respuesta es una lista de productos,
            # o un dict con clave "products" que contiene la lista.
            products = data if isinstance(data, list) else data.get("products", [])

            result = [
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": product.get("price"),
                }
                for product in products
                if isinstance(product.get("price"), (int, float))
                and product["price"] > price_threshold
            ]
            return result

        except httpx.TimeoutException as exc:
            last_exception = exc
            logger.warning(
                "Intento %d/%d: timeout tras %.1fs al llamar a %s",
                attempt, max_retries, timeout, api_url
            )

        except httpx.HTTPStatusError as exc:
            # Errores 4xx/5xx: no siempre tiene sentido reintentar 4xx,
            # pero aquí se reintenta igual salvo que sea un error de cliente claro (401/403/404).
            status = exc.response.status_code
            last_exception = exc
            if status in (401, 403, 404):
                logger.error(
                    "Error HTTP %d no recuperable al llamar a %s: %s",
                    status, api_url, exc
                )
                break
            logger.warning(
                "Intento %d/%d: error HTTP %d al llamar a %s",
                attempt, max_retries, status, api_url
            )

        except httpx.RequestError as exc:
            # Cubre errores de conexión, DNS, etc.
            last_exception = exc
            logger.warning(
                "Intento %d/%d: error de red al llamar a %s: %s",
                attempt, max_retries, api_url, exc
            )

        except (ValueError, KeyError) as exc:
            # Error al parsear JSON o estructura inesperada
            last_exception = exc
            logger.error(
                "Error al procesar la respuesta de %s: %s",
                api_url, exc
            )
            break

        # Backoff exponencial antes del siguiente intento (si no es el último)
        if attempt < max_retries:
            sleep_time = backoff_base * (2 ** (attempt - 1))
            logger.info("Esperando %.1fs antes de reintentar...", sleep_time)
            time.sleep(sleep_time)

    if last_exception:
        logger.error(
            "No se pudo obtener productos tras %d intentos. Último error: %s",
            max_retries, last_exception
        )

    return []


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    products = get_expensive_products(
        api_url="https://api.example.com/products",
        token="tu_token_aqui",
        price_threshold=100,
    )
    print(products)
```

### Notas de diseño

- **`httpx.Client`** se usa dentro de un `with` para asegurar el cierre correcto de la conexión en cada intento.
- **Errores manejados por separado**:
  - `httpx.TimeoutException` → timeout de red.
  - `httpx.HTTPStatusError` → códigos 4xx/5xx (con lógica para no reintentar en 401/403/404).
  - `httpx.RequestError` → errores generales de conexión (DNS, conexión rechazada, etc.).
  - `ValueError`/`KeyError` → problemas al parsear el JSON.
- **Backoff exponencial**: `backoff_base * 2^(intento-1)` → 1s, 2s, 4s (con `backoff_base=1.0`).
- Si todos los intentos fallan, retorna `[]` en lugar de lanzar excepción, pero registra el error vía `logging`. Si prefieres que la función **lance** la excepción en vez de retornar `[]`, puedes reemplazar el `return []` final por `raise last_exception`.