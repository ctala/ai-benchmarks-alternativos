# GLM 5.3 Flash — code_generation/python_api_integration

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.95 | quality: 9.08
- latency_total: 97.422s | tokens_per_second: 88.3
- input_tokens: 113 | output_tokens: 8599
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

import httpx

API_URL = "https://api.example.com/products"
MAX_ATTEMPTS = 3      # intentos totales (no reintentos adicionales)
TIMEOUT = 10.0        # segundos
BASE_BACKOFF = 1.0    # base del backoff; se duplica en cada reintento


def fetch_expensive_products(token: str, min_price: float = 100) -> list[dict]:
    """
    Descarga los productos de la API y devuelve solo los que cuestan
    más de `min_price`, con el formato {id, name, price}.

    Raises:
        RuntimeError: si fallan los 3 intentos por red/timeout/5xx.
        httpx.HTTPStatusError: si la API devuelve un 4xx (no se reintenta).
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_error = None

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = httpx.get(API_URL, headers=headers, timeout=TIMEOUT)
            response.raise_for_status()
            data = response.json()
            break  # éxito: salimos del bucle de reintentos
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code < 500:
                raise  # 4xx = error del cliente; reintentar no lo arregla
            last_error = exc
        except (httpx.TimeoutException, httpx.RequestError) as exc:
            # TimeoutException cubre los timeouts; RequestError cubre
            # errores de red (DNS, conexión rechazada, etc.)
            last_error = exc

        if attempt == MAX_ATTEMPTS:
            raise RuntimeError(
                f"No se pudo obtener {API_URL} tras {MAX_ATTEMPTS} intentos"
            ) from last_error

        # Backoff exponencial: espera de 1 s, luego 2 s
        time.sleep(BASE_BACKOFF * 2 ** (attempt - 1))

    # La API puede devolver la lista directa o envuelta en una clave
    products = data if isinstance(data, list) else data.get("products", [])

    return [
        {"id": p.get("id"), "name": p.get("name"), "price": p["price"]}
        for p in products
        if isinstance(p.get("price"), (int, float)) and p["price"] > min_price
    ]


if __name__ == "__main__":
    productos = fetch_expensive_products(token="TU_TOKEN")
    print(productos)
```

**Puntos clave:**

- **Timeout**: `timeout=10.0` en httpx aplica 10 s a cada fase (conexión, lectura, escritura, pool).
- **Reintentos**: 3 intentos totales con esperas de 1 s y 2 s (`base * 2^(n-1)`). Solo usa `time.sleep` de la stdlib, sin dependencias extra. En producción conviene añadir *jitter* aleatorio para evitar *thundering herd*.
- **Qué se reintenta**: timeouts, errores de red y respuestas 5xx. Los 4xx (401, 404, etc.) se lanzan de inmediato porque reintentar no cambia el resultado.
- **Robustez del filtro**: `isinstance(...)` descarta precios `None` o como string; acepta tanto una lista directa como una respuesta envuelta tipo `{"products": [...]}`.
- **Token**: se recibe por parámetro (idealmente desde una variable de entorno, nunca hardcodeado).

Si prefieres que al agotar los intentos devuelva `[]` en vez de lanzar `RuntimeError`, cambia el `raise` por `return []`. Y si necesitas la versión async, el mismo esquema funciona con `httpx.AsyncClient` y `asyncio.sleep`.