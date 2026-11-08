# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/python_api_integration

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.66 | quality: 9.56
- latency_total: 12.523s | tokens_per_second: 61.6
- input_tokens: 112 | output_tokens: 772
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

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx`, sin dependencias externas adicionales:

```python
import httpx
import time
import random

def get_expensive_products(token: str, base_url: str = "https://api.example.com/products") -> list:
    """
    Obtiene productos filtrados con precio > 100 desde una API con autenticación Bearer.
    
    Args:
        token (str): Token Bearer para autenticación.
        base_url (str): URL del endpoint de productos.
        
    Returns:
        list: Lista de diccionarios con las claves 'id', 'name', y 'price' para productos > 100.
        
    Raises:
        httpx.RequestError: Si todos los reintentos fallan.
    """
    max_retries = 3
    timeout = 10.0  # segundos
    base_delay = 1.0  # segundo
    backoff_multiplier = 2.0
    jitter_range = 0.1  # ±10% para evitar thundering herd

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=httpx.Timeout(timeout)) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                products = response.json()

                # Filtrar productos con precio > 100
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]
                return filtered

        except (httpx.TimeoutException, httpx.RequestError) as e:
            if attempt == max_retries:
                # Último intento fallido: lanzar excepción
                raise e

            # Calcular delay con backoff exponencial y jitter
            delay = base_delay * (backoff_multiplier ** (attempt - 1))
            jitter = delay * jitter_range * (2 * random.random() - 1)  # ±jitter_range * delay
            delay = max(0.1, delay + jitter)
            time.sleep(delay)

    # No debería llegar aquí, pero por seguridad
    raise httpx.RequestError("Todos los reintentos fallaron sin excepción previa")
```

### Notas importantes:
- **Autenticación**: Usa el header `Authorization: Bearer <token>`.
- **Timeout**: 10 segundos totales por solicitud (`httpx.Timeout(timeout)`).
- **Reintentos**: Máximo 3 intentos con *exponential backoff* (`1s`, `2s`, `4s` + jitter).
- **Jitter**: Pequeña aleatoriedad (±10%) para evitar que múltiples clientes se sincronicen en reintentos.
- **Filtrado**: Asegura que `price` sea numérico y > 100 antes de incluir.
- **Manejo de errores**: Captura `TimeoutException` y otros `RequestError` (como `ConnectError`, `HTTPStatusError`, etc.). `HTTPStatusError` se lanza si `raise_for_status()` detecta código 4xx/5xx.

✅ Funciona con `httpx` (disponible en Python estándar con `pip install httpx`, pero **sin otras dependencias externas**).