# Qwen 3.6 Max — code_generation/python_api_integration

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.19 | quality: 9.72
- latency_total: 89.844s | tokens_per_second: 45.9
- input_tokens: 113 | output_tokens: 4125
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una implementación limpia y robusta que cumple con todos los requisitos solicitados:

```python
import httpx
import time
from typing import List, Dict, Any

def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100,
    y retorna solo id, name y price.
    Incluye manejo de errores, timeout y retry con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout = 10.0  # Requisito 4: timeout de 10 segundos

    last_exc = None

    # Requisito 5: Retry con backoff exponencial (máx 3 intentos)
    for attempt in range(max_retries):
        try:
            # Requisito 1: GET con autenticación Bearer y timeout
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza error para 4xx/5xx
                data = response.json()
                break  # Éxito: salimos del bucle de reintentos
                
        except (httpx.RequestError, httpx.HTTPStatusError, httpx.DecodingError) as e:
            # Requisito 4: Manejo de errores de red, timeout y HTTP
            last_exc = e
            if attempt < max_retries - 1:
                # Backoff exponencial: 1s, 2s, 4s
                time.sleep(2 ** attempt)
                continue
            # Si es el último intento, continuamos para lanzar el error final
        except Exception as e:
            raise RuntimeError(f"Error inesperado durante la petición: {e}") from e
    else:
        raise RuntimeError(f"Fallo tras {max_retries} intentos: {last_exc}") from last_exc

    # Validación básica de estructura
    if not isinstance(data, list):
        raise ValueError("La respuesta de la API no es una lista de productos")

    # Requisito 2 y 3: Filtrar precio > 100 y retornar solo {id, name, price}
    filtered_products = []
    for product in data:
        price = product.get("price")
        if isinstance(price, (int, float)) and price > 100:
            filtered_products.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price
            })

    return filtered_products
```

### 🔍 Mapeo de requisitos:
1. **GET + Bearer**: Se usa `httpx.Client().get()` con el header `Authorization: Bearer <token>`.
2. **Filtro `price > 100`**: Se valida con `isinstance(price, (int, float)) and price > 100` para evitar errores con tipos inesperados.
3. **Formato de retorno**: Se construye explícitamente `{"id": ..., "name": ..., "price": ...}` ignorando el resto de campos.
4. **Errores y timeout**: `timeout=10.0` aplica a conexión, lectura y escritura. Se capturan `httpx.RequestError` (red/timeout), `httpx.HTTPStatusError` (4xx/5xx) y `httpx.DecodingError` (JSON inválido).
5. **Retry + backoff exponencial**: Bucle de 3 intentos con `time.sleep(2 ** attempt)` → esperas de 1s, 2s y 4s entre reintentos.

### 💡 Notas para producción:
- `httpx` es la única dependencia externa requerida (`pip install httpx`).
- En entornos críticos, se recomienda añadir *jitter* al backoff para evitar thundering herd: `time.sleep((2 ** attempt) + random.uniform(0, 1))`.
- Si tu aplicación es asíncrona, la misma lógica puede adaptarse fácilmente usando `httpx.AsyncClient` y `await asyncio.sleep()`.

¿Necesitas que la adapte a un contexto asíncrono o que incluya logging estructurado?