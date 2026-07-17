# DeepSeek R1 (reasoning) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 254.247s | tokens_per_second: 12.7
- input_tokens: 109 | output_tokens: 3234
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos especificados utilizando `httpx`:

```python
import httpx
import time
import random

def get_high_priced_products(token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 de una API
    Args:
        token: Token de autenticación Bearer
    Returns:
        Lista de diccionarios con {id, name, price} o lista vacía en caso de error
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)  # Timeout de 10 segundos
    max_retries = 3
    base_delay = 1  # Segundos base para el backoff

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
                
                # Procesar respuesta
                data = response.json()
                products = data.get("products", [])
                
                # Filtrar y formatear productos
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return filtered_products

        except (httpx.NetworkError, httpx.TimeoutException) as e:
            # Backoff exponencial con jitter
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                return []  # Máximo de reintentos alcanzado

        except (httpx.HTTPStatusError, KeyError, TypeError) as e:
            # Errores que no se reintentan (respuesta HTTP no exitosa o estructura de datos inválida)
            return []
    
    return []  # Fallback por si acaso
```

### Explicación:
1. **Autenticación Bearer**: Usa el token proporcionado en el header `Authorization`.
2. **Filtrado de productos**: Selecciona solo productos con `price > 100`.
3. **Formato de salida**: Retorna diccionarios con solo `id`, `name`, y `price`.
4. **Manejo de errores**:
   - `NetworkError` y `TimeoutException`: Se reintentan con backoff exponencial.
   - `HTTPStatusError` (códigos 4xx/5xx): No se reintenta, retorna lista vacía.
   - `KeyError`/`TypeError` (estructura de datos inválida): No se reintenta.
5. **Retry con backoff**:
   - Máximo 3 intentos.
   - Backoff exponencial: `1s`, `~2s`, `~4s` con jitter aleatorio.
6. **Timeout**: 10 segundos por solicitud.

### Características:
- Usa context manager (`with`) para asegurar que el cliente HTTP se cierre correctamente.
- `raise_for_status()` verifica códigos HTTP de error (400-599).
- Maneja errores de estructura de datos (campos faltantes o tipos incorrectos).
- Incluye jitter aleatorio para evitar el "efecto tormenta" en reintentos.

Esta función retornará una lista de productos filtrados o una lista vacía en caso de:
- Error de red/timeout después de 3 intentos
- Respuesta HTTP no exitosa (4xx/5xx)
- Estructura de datos inesperada en la respuesta
- Cualquier otro error no recuperable