# GLM-5.1 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.0 | quality: 9.52
- latency_total: 64.375s | tokens_per_second: 79.1
- input_tokens: 113 | output_tokens: 5095
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
from typing import Any, Dict, List, Optional

import httpx


def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde https://api.example.com/products.

    - Autenticacion: Bearer token.
    - Timeout: 10 segundos por request.
    - Retry: maximo 3 intentos con backoff exponencial (1s, 2s).
    - Errores 4xx no se reintentan (no recuperables).
    - Errores 5xx, timeouts y errores de red si se reintentan.

    Args:
        token: Bearer token para autenticacion.

    Returns:
        Lista de dicts con {id, name, price} para productos con precio > 100.

    Raises:
        httpx.HTTPStatusError: Si la API retorna un error 4xx.
        RuntimeError: Si todos los intentos fallan por errores recuperables.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3
    base_backoff = 1.0  # segundos
    timeout = httpx.Timeout(10.0)

    last_exc: Optional[Exception] = None

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout, headers=headers) as client:
                response = client.get(url)
                response.raise_for_status()
                products = response.json()

            if not isinstance(products, list):
                raise ValueError(
                    f"Respuesta inesperada: se esperaba lista, "
                    f"se obtuvo {type(products).__name__}"
                )

            # Filtrar precio > 100 y proyectar solo las claves requeridas
            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]

        except httpx.HTTPStatusError as exc:
            # 4xx: error del cliente, no se recuperara con reintentos
            if exc.response.status_code < 500:
                raise
            # 5xx: error del servidor, reintentar
            last_exc = exc

        except httpx.RequestError as exc:
            # Cubre: TimeoutException, ConnectError, ReadError, NetworkError, etc.
            last_exc = exc

        # Backoff exponencial antes del siguiente intento: 1s, 2s
        if attempt < max_attempts:
            time.sleep(base_backoff * (2 ** (attempt - 1)))

    raise RuntimeError(
        f"Request a {url} fallo tras {max_attempts} intentos. "
        f"Ultimo error: {last_exc}"
    ) from last_exc


# --- Ejemplo de uso ---
if __name__ == "__main__":
    try:
        productos = fetch_expensive_products(token="MI_TOKEN_SECRETO")
        print(f"Productos caros ({len(productos)}):")
        for p in productos:
            print(f"  - [{p['id']}] {p['name']}: ${p['price']}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP del cliente: {e.response.status_code}")
    except RuntimeError as e:
        print(f"Error de red persistente: {e}")
```

### Notas de diseño

| Aspecto | Decision |
|---|---|
| **Cliente** | Se crea un `httpx.Client` por intento para garantizar estado limpio tras un fallo (conexiones posiblemente rotas). |
| **Timeout** | `httpx.Timeout(10.0)` cubre connect/read/write/pool en 10s. |
| **Retry selectivo** | Los **4xx** se lanzan de inmediato (no se recuperan con reintentos); los **5xx** y errores de red sí se reintentan. |
| **Backoff** | `1s, 2s` entre intentos (no se espera tras el último intento fallido). Fórmula: `base * 2^(attempt-1)`. |
| **Tipado** | `Optional` en lugar de `X | None` para compatibilidad con Python 3.8+. |
| **Validación** | Se verifica que la respuesta JSON sea una lista y que cada item sea dict antes de acceder a claves. |
| **Sin dependencias extra** | Solo `httpx` + stdlib (`time`, `typing`). No se usa `tenacity` ni similares. |

Si necesitas versión **async** (`httpx.AsyncClient` + `asyncio.sleep`), o agregar **jitter** al backoff para evitar tormentas de reintentos, dime y lo adapto.