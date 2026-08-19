# Inkling Small — code_generation/python_api_integration

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.02 | quality: 9.8
- latency_total: 237.693s | tokens_per_second: 13.8
- input_tokens: 111 | output_tokens: 3284
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, cubriendo todos los requisitos con una implementación sólida.

## Respuesta completa

Aquí tienes la función usando solo `httpx` y la librería estándar (`time`):

```python
import time
import httpx


def fetch_products(token: str, url: str = "https://api.example.com/products") -> list[dict]:
    """
    Obtiene productos, filtra por precio > 100 y retorna {id, name, price}.
    Reintenta hasta 3 veces con backoff exponencial ante errores de red/timeout.
    """
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    timeout = 10.0  # segundos

    for attempt in range(1, max_attempts + 1):
        try:
            # Cliente con timeout de 10 s para todo el request
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()  # lanza HTTPStatusError si es 4xx/5xx
                data = resp.json()

            # Adaptación: la API puede devolver una lista directa o un dict con clave
            if isinstance(data, list):
                products = data
            elif isinstance(data, dict):
                products = data.get("products") or data.get("data") or data.get("items") or []
            else:
                products = []

            result = []
            for p in products:
                if not isinstance(p, dict):
                    continue
                price = p.get("price")
                # Solo incluir si el precio es numérico y mayor a 100
                if isinstance(price, (int, float)) and price > 100:
                    result.append({
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": price,
                    })

            return result

        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError) as exc:
            # Errores de red, timeout o HTTP fallido: reintentar si quedan intentos
            if attempt == max_attempts:
                raise exc  # Último intento fallido: propagar el error
            
            # Backoff exponencial: 1 s, 2 s (2^(intento-1))
            time.sleep(2 ** (attempt - 1))

    # No debería alcanzarse, pero por seguridad
    return []
```

### Puntos clave de la implementación
| Requisito | Cómo se cubre |
|---|---|
| **GET con Bearer** | `headers={"Authorization": f"Bearer {token}"}` |
| **Timeout 10 s** | `httpx.Client(timeout=10.0)` y `client.get(...)` |
| **Filtrado `price > 100`** | Comprobación `isinstance(price, (int, float)) and price > 100` |
| **Retorno `{id, name, price}`** | Se construye la lista de diccionarios con solo esas 3 claves |
| **Retry + backoff exponencial** | Bucle `for` con `max_attempts = 3`; `time.sleep(2 ** (attempt - 1))` |
| **Errores de red / timeout** | `except (httpx.RequestError, httpx.TimeoutException, ...)`; se reintenta o se lanza al final |
| **Sin dependencias extra** | Solo `httpx` (y `time` de la stdlib) |

> **Nota:** Si tu API devuelve siempre una lista directa (`[{...}, {...}]`), la parte de `isinstance(data, dict)` es opcional pero hace la función más robusta ante estructuras anidadas (`{"products": [...]}`).