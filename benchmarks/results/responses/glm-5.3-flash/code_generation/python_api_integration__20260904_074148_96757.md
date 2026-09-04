# GLM 5.3 Flash — code_generation/python_api_integration

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.67 | quality: 9.28
- latency_total: 10.595s | tokens_per_second: 76.2
- input_tokens: 113 | output_tokens: 807
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

# Función de obtención y filtrado de productos

```python
import httpx
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT = 10.0
MAX_RETRIES = 3


def get_expensive_products(token: str, min_price: float = 100.0) -> list[dict]:
    """
    Obtiene productos de la API y filtra los que cuestan más de min_price.

    Args:
        token: Bearer token para autenticación.
        min_price: Precio mínimo de filtro (default: 100).

    Returns:
        Lista de dicts con {id, name, price} de productos filtrados.
        Lista vacía si falla la petición tras todos los reintentos.
    """
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = httpx.get(
                API_URL,
                headers=headers,
                timeout=TIMEOUT,
            )
            response.raise_for_status()
            products = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > min_price
            ]

        except httpx.TimeoutException:
            logger.warning("Intento %d/%d: timeout tras %.0fs", attempt, MAX_RETRIES, TIMEOUT)
        except httpx.HTTPStatusError as e:
            logger.warning("Intento %d/%d: HTTP %d - %s", attempt, MAX_RETRIES, e.response.status_code, e)
        except httpx.RequestError as e:
            logger.warning("Intento %d/%d: error de red - %s", attempt, MAX_RETRIES, e)
        except (KeyError, ValueError) as e:
            # Error de formato de respuesta: no tiene sentido reintentar
            logger.error("Respuesta con formato inesperado: %s", e)
            return []

        # Backoff exponencial: 1s, 2s, 4s... (no esperar tras el último intento)
        if attempt < MAX_RETRIES:
            delay = 2 ** (attempt - 1)
            logger.info("Reintentando en %ds...", delay)
            time.sleep(delay)

    logger.error("Falló tras %d intentos", MAX_RETRIES)
    return []


if __name__ == "__main__":
    resultado = get_expensive_products(token="mi_token_secreto")
    print(resultado)
```

## Puntos clave

- **Backoff exponencial**: `2 ** (attempt - 1)` produce esperas de 1s, 2s antes de los reintentos 2 y 3.
- **Timeout de 10s**: pasado directamente a `httpx.get`.
- **Errores manejados**:
  - `httpx.TimeoutException` — timeout
  - `httpx.HTTPStatusError` — códigos 4xx/5xx (via `raise_for_status`)
  - `httpx.RequestError` — errores de conexión/DNS
  - `KeyError`/`ValueError` — JSON malformado (no reintenta, es un error permanente)
- **Type hints y fallback**: retorna `[]` si todo falla, en lugar de lanzar excepción.

Si prefieres que los errores permanentes (4xx como 401/403) no se reintenten, se puede añadir esa lógica fácilmente:

```python
if 400 <= e.response.status_code < 500:
    logger.error("Error del cliente (%d), no se reintenta", e.response.status_code)
    return []
```