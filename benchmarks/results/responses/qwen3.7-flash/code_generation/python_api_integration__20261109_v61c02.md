# Qwen 3.7 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.09 | quality: 10.0
- latency_total: 52.762s | tokens_per_second: 106.0
- input_tokens: 113 | output_tokens: 5593
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

Aquí tienes la función completa, cumpliendo todos los requisitos y utilizando únicamente `httpx` y la biblioteca estándar (`time` para los delays):

```python
import httpx
import time

def fetch_filtered_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100
    y retorna una lista de dicts con {id, name, price}.
    Incluye retry con backoff exponencial y manejo de errores.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_delay = 1.0  # Retraso inicial en segundos

    for attempt in range(max_retries):
        try:
            # timeout=10.0 aplica a conexión, lectura y escritura
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()
                # Compatibilidad: la API podría devolver un array o un objeto con clave 'products'
                products = data if isinstance(data, list) else data.get("products", [])

                # Filtrado y proyección solicitada
                return [
                    {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                    for p in products
                    if p.get("price") is not None and float(p["price"]) > 100
                ]

        except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError, Exception) as e:
            delay = base_delay * (2 ** attempt)  # Backoff exponencial: 1s, 2s, 4s
            
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                # Tras agotar intentos, se relanza el error correspondiente
                if isinstance(e, httpx.TimeoutException):
                    raise TimeoutError(f"Timeout tras {max_retries} intentos.")
                elif isinstance(e, httpx.HTTPStatusError):
                    raise RuntimeError(f"HTTP {e.response.status_code} tras {max_retries} intentos.")
                elif isinstance(e, httpx.RequestError):
                    raise ConnectionError(f"Error de red tras {max_retries} intentos.")
                else:
                    raise RuntimeError(f"Error inesperado tras {max_retries} intentos: {e}")
```

### 🔍 Notas de implementación:
1. **Autenticación**: Se pasa vía header `Authorization: Bearer <token>` en cada intento.
2. **Timeout**: `httpx.Client(timeout=10.0)` configura 10 segundos para conexión, lectura y escritura. Captura tanto `TimeoutException` como otros fallos de red.
3. **Retry + Backoff**: La fórmula `base_delay * (2 ** attempt)` genera retardos de `1s → 2s → 4s` antes de los intentos 2 y 3.
4. **Manejo de errores**: Se capturan por separado `TimeoutException`, `HTTPStatusError` (4xx/5xx), `RequestError` (DNS, conexión caída, etc.) y un `Exception` genérico para errores de parseo o estructura inválida.
5. **Flexibilidad de respuesta**: La línea `products = data if isinstance(data, list) else data.get("products", [])` evita crashes si la API envuelve los resultados en un objeto JSON.
6. **Cero dependencias externas**: Solo usa `httpx` y `time` (stdlib).