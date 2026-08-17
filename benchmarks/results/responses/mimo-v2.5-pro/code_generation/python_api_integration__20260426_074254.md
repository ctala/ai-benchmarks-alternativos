# MiMo-V2.5 Pro — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.63 | quality: 9.52
- latency_total: 19.103s | tokens_per_second: 71.0
- input_tokens: 355 | output_tokens: 1356
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función con `httpx`, filtros y retry con backoff exponencial

```python
import httpx
import time
from typing import Any


def get_expensive_products(
    bearer_token: str,
    base_url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout_seconds: float = 10.0,
    min_price: float = 100.0,
) -> list[dict[str, Any]]:
    """
    Obtiene productos de la API y retorna aquellos con precio > min_price.

    Args:
        bearer_token:    Token de autenticación Bearer.
        base_url:        Endpoint de productos.
        max_retries:     Número máximo de reintentos (backoff exponencial).
        timeout_seconds: Timeout por cada request individual.
        min_price:       Precio mínimo para filtrar (exclusivo).

    Returns:
        Lista de dicts con las claves: id, name, price.

    Raises:
        httpx.HTTPStatusError: Si tras todos los reintentos sigue fallando.
        httpx.RequestError:    Si hay un error de red persistente.
    """

    headers = {"Authorization": f"Bearer {bearer_token}"}
    last_exception: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()  # Lanza si status >= 400

                products: list[dict] = response.json()

                # Filtrar y seleccionar solo los campos deseados
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > min_price
                ]

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Errores recuperables → reintentar con backoff
            last_exception = e
            if attempt < max_retries:
                wait = 2 ** (attempt - 1)  # 1s, 2s, 4s ...
                print(f"[Retry {attempt}/{max_retries}] {type(e).__name__}: {e} → esperando {wait}s")
                time.sleep(wait)
                continue
            raise  # Último intento fallido

        except httpx.HTTPStatusError as e:
            # Errores 4xx/5xx → no reintentar (excepto 5xx si se desea)
            status = e.response.status_code
            if status >= 500 and attempt < max_retries:
                last_exception = e
                wait = 2 ** (attempt - 1)
                print(f"[Retry {attempt}/{max_retries}] HTTP {status} → esperando {wait}s")
                time.sleep(wait)
                continue
            raise

    # Seguridad: no debería llegar aquí, pero por si acaso
    raise last_exception  # type: ignore[misc]
```

---

## Cómo funciona paso a paso

```
Intento 1 ──► GET /products
               │
               ├─ ✅ 200 OK → filtrar → retornar
               │
               └─ ❌ Error
                    │
          esperar 2⁰ = 1s
                    │
Intento 2 ──► GET /products
               │
               ├─ ✅ 200 OK → filtrar → retornar
               │
               └─ ❌ Error
                    │
          esperar 2¹ = 2s
                    │
Intento 3 ──► GET /products
               │
               ├─ ✅ 200 OK → filtrar → retornar
               │
               └─ ❌ Error → RAISE excepción
```

---

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        productos = get_expensive_products(
            bearer_token="mi-token-secreto-123",
            min_price=100,
        )
        for p in productos:
            print(f"  #{p['id']}  {p['name']:<30} ${p['price']:.2f}")

        print(f"\nTotal productos caros: {len(productos)}")

    except httpx.HTTPStatusError as e:
        print(f"Error HTTP {e.response.status_code}: {e.response.text}")
    except httpx.RequestError as e:
        print(f"Error de red: {e}")
```

---

## Puntos clave del diseño

| Aspecto | Decisión |
|---|---|
| **Timeout** | 10 s por defecto, configurable |
| **Backoff** | Exponencial: `1s → 2s → 4s` (fórmula: `2^(attempt-1)`) |
| **Reintentos** | Solo en errores **recuperables**: `TimeoutException`, `NetworkError`, `HTTP 5xx` |
| **No reintenta** | `HTTP 4xx` (error del cliente, no tiene sentido reintentar) |
| **Filtrado** | `p.get("price", 0)` para evitar `KeyError` si falta el campo |
| **Context manager** | `with httpx.Client(...)` garantiza que la conexión se cierre |
| **Dependencias** | Solo `httpx` (lo solicitado) + stdlib (`time`, `typing`) |

> **Nota**: `httpx` es la única dependencia externa necesaria (`pip install httpx`). Todo lo demás es parte de la librería estándar de Python.