# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/python_api_integration

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 72.026s | tokens_per_second: 68.2
- input_tokens: 113 | output_tokens: 4910
- judge_score: 5.0 | justificación: 

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

Aquí tienes una implementación robusta y lista para producción que cumple con todos los requisitos:

```python
import httpx
import time

def fetch_expensive_products(bearer_token: str) -> list[dict]:
    """
    Realiza GET a la API de productos con autenticación Bearer,
    filtra precios > 100, maneja timeouts/errores de red y aplica
    retry con backoff exponencial (máx 3 intentos).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    base_delay = 1.0  # Segundo base para el backoff

    for attempt in range(max_retries):
        try:
            # timeout=10.0 aplica a connect, read, write y pool
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                # Parseo seguro del JSON
                data = response.json()
                products = data if isinstance(data, list) else data.get("products", [])

                # Filtrado y proyección de campos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

        except httpx.HTTPStatusError as e:
            # Solo reintentar en errores del servidor (5xx)
            if e.response.status_code >= 500 and attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
            else:
                raise RuntimeError(f"Error HTTP {e.response.status_code}: {e}") from e

        except httpx.RequestError as e:
            # httpx.RequestError agrupa timeouts y fallos de red
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
            else:
                raise RuntimeError(f"Fallo tras {max_retries} intentos: {e}") from e

        except (httpx.DecodingError, ValueError) as e:
            # Error al parsear JSON (respuesta no válida)
            raise RuntimeError(f"Respuesta JSON inválida: {e}") from e
```

### 🔍 Puntos clave de la implementación:
1. **Timeout de 10s**: `httpx.Client(timeout=10.0)` configura un timeout global que cubre conexión, lectura, escritura y pool de sockets.
2. **Retry + Backoff Exponencial**: 
   - Intento 0 → falla → espera `1.0 * 2^0 = 1s`
   - Intento 1 → falla → espera `1.0 * 2^1 = 2s`
   - Intento 2 → falla → lanza error (máx 3 intentos cumplido)
3. **Manejo inteligente de errores**: 
   - `httpx.RequestError` captura timeouts y cortes de red.
   - `httpx.HTTPStatusError` separa errores 4xx (no reintentables) de 5xx (reintentables).
   - Se incluye captura de errores de decodificación JSON por robustez.
4. **Filtrado seguro**: Verifica que `price` sea numérico antes de comparar, evitando `TypeError` si la API devuelve `null` o strings.
5. **Sin dependencias extra**: Solo usa `httpx` y `time` (stdlib).

### 💡 Ejemplo de uso:
```python
try:
    productos = fetch_expensive_products("tu_token_aqui")
    print(f"Se encontraron {len(productos)} productos caros:")
    for p in productos:
        print(p)
except RuntimeError as e:
    print(f"Operación fallida: {e}")
```

Si prefieres una versión asíncrona (`async def` con `httpx.AsyncClient` y `asyncio.sleep`), avísame y la adapto sin problema.