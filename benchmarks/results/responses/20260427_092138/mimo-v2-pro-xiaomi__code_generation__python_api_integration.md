# MiMo V2-Pro (Xiaomi direct) — code_generation/python_api_integration

- model_id: `mimo-v2-pro`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 20.491s | tokens_per_second: 53.6
- input_tokens: 353 | output_tokens: 1099
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función con httpx: GET + Filtro + Retry

```python
import httpx
import time
from typing import Optional


def get_expensive_products(
    token: str,
    base_url: str = "https://api.example.com",
    min_price: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos con precio > min_price desde la API.

    Args:
        token:      Bearer token de autenticación.
        base_url:   URL base de la API.
        min_price:  Precio mínimo para filtrar (exclusivo).
        max_retries: Número máximo de reintentos.
        timeout:    Timeout por request en segundos.

    Returns:
        Lista de dicts con {id, name, price} de productos filtrados.

    Raises:
        httpx.HTTPStatusError: Si la API responde con error tras agotar reintentos.
        httpx.RequestError:    Si hay error de red tras agotar reintentos.
    """
    url = f"{base_url}/products"
    headers = {"Authorization": f"Bearer {token}"}

    last_exception: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()

                # Filtrar y seleccionar solo los campos requeridos
                expensive_products = [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                    }
                    for product in data
                    if product.get("price", 0) > min_price
                ]

                return expensive_products

        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError) as e:
            last_exception = e

            # No reintentar en el último intento
            if attempt == max_retries:
                break

            # Backoff exponencial: 1s, 2s, 4s...
            wait_time = 2 ** (attempt - 1)
            time.sleep(wait_time)

    # Si llegamos aquí, todos los intentos fallaron
    raise last_exception  # type: ignore[misc]
```

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        productos = get_expensive_products(token="mi_token_secreto_123")
        print(f"Productos caros encontrados: {len(productos)}")
        for p in productos:
            print(f"  - {p['name']}: ${p['price']}")

    except httpx.HTTPStatusError as e:
        print(f"Error HTTP {e.response.status_code}: {e.response.text}")

    except httpx.RequestError as e:
        print(f"Error de red: {e}")
```

## Flujo visual

```
Intento 1 ──GET──► ¿OK? ──Sí──► Filtrar + Retornar
                  │
                  No
                  │
              Espera 1s (backoff)
                  │
Intento 2 ──GET──► ¿OK? ──Sí──► Filtrar + Retornar
                  │
                  No
                  │
              Espera 2s (backoff)
                  │
Intento 3 ──GET──► ¿OK? ──Sí──► Filtrar + Retornar
                  │
                  No
                  │
              Raise última excepción
```

## Puntos clave

| Aspecto | Detalle |
|---|---|
| **Timeout** | 10s por request, configurable |
| **Backoff** | Exponencial: `2^(attempt-1)` → 1s, 2s, 4s |
| **Errores capturados** | `TimeoutException`, `RequestError` (red), `HTTPStatusError` (4xx/5xx) |
| **Filtro** | `product.get("price", 0)` evita `KeyError` si falta el campo |
| **Sin dependencias extra** | Solo `httpx` + librería estándar (`time`) |

> **Nota:** `httpx` ya incluye manejo de timeouts, JSON parsing y códigos de estado, por eso no necesitas `requests` ni `json` por separado.