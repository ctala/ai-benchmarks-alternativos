# MiMo-V2.5 Pro — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.27 | quality: 9.52
- latency_total: 16.793s | tokens_per_second: 70.3
- input_tokens: 355 | output_tokens: 1180
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Función con `httpx`: GET, filtrado y retry con backoff exponencial

```python
import httpx
import time


def get_expensive_products(
    bearer_token: str,
    base_url: str = "https://api.example.com/products",
    price_threshold: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos de la API, filtra los que superan un precio
    y devuelve solo {id, name, price}.

    Args:
        bearer_token:    Token de autorización Bearer.
        base_url:        Endpoint de productos.
        price_threshold: Precio mínimo para filtrar (exclusivo).
        max_retries:     Número máximo de intentos.
        timeout:         Timeout de la petición en segundos.

    Returns:
        Lista de dicts con {id, name, price} de productos con precio > threshold.
    """

    headers = {"Authorization": f"Bearer {bearer_token}"}
    last_exception: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()          # Lanza excepción si 4xx/5xx

                products = response.json()

                # Filtrar y seleccionar solo los campos deseados
                expensive = [
                    {
                        "id":    product["id"],
                        "name":  product["name"],
                        "price": product["price"],
                    }
                    for product in products
                    if product.get("price", 0) > price_threshold
                ]

                return expensive

        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as exc:
            last_exception = exc
            print(f"  ⚠ Intento {attempt}/{max_retries} fallido: {type(exc).__name__}: {exc}")

            if attempt < max_retries:
                # Backoff exponencial: 1s → 2s → 4s ...
                wait = 2 ** (attempt - 1)
                print(f"    ⏳ Reintentando en {wait}s ...")
                time.sleep(wait)

    # Si se agotaron todos los intentos
    raise RuntimeError(
        f"No se pudo completar la petición tras {max_retries} intentos."
    ) from last_exception
```

---

## Cómo funciona paso a paso

```
Intento 1  ──→  falla  ──→  espera 1 s   (2⁰)
Intento 2  ──→  falla  ──→  espera 2 s   (2¹)
Intento 3  ──→  falla  ──→  RuntimeError propagado
```

| Aspecto | Detalle |
|---|---|
| **Autenticación** | Header `Authorization: Bearer <token>` en cada intento |
| **Timeout** | 10 s por defecto (conecta + lectura + escritura) |
| **Excepciones capturadas** | `TimeoutException`, `NetworkError`, `HTTPStatusError` (4xx/5xx) |
| **Backoff** | `2^(attempt-1)` segundos entre reintentos |
| **Salida** | `list[dict]` con solo `id`, `name`, `price` filtrados |

---

## Ejemplo de uso

```python
if __name__ == "__main__":
    try:
        products = get_expensive_products(
            bearer_token="mi_token_secreto_aqui",
            price_threshold=100,
        )
        print(f"Productos encontrados: {len(products)}")
        for p in products:
            print(f"  - {p['name']}: ${p['price']}")
    except RuntimeError as e:
        print(f"Error final: {e}")
```

**Salida esperada (éxito):**
```
Productos encontrados: 3
  - Laptop Pro: $1299.99
  - Monitor 4K: $599.00
  - Teclado mecánico: $150.00
```

**Salida en caso de fallo persistente:**
```
  ⚠ Intento 1/3 fallado: TimeoutException: ...
    ⏳ Reintentando en 1s ...
  ⚠ Intento 2/3 fallado: TimeoutException: ...
    ⏳ Reintentando en 2s ...
  ⚠ Intento 3/3 fallado: TimeoutException: ...
Error final: No se pudo completar la petición tras 3 intentos.
```

> **Nota:** `httpx` es la única dependencia externa requerida (`pip install httpx`). `time` es parte de la librería estándar de Python.