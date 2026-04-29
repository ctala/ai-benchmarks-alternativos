# Devstral 2 123B (NIM) — code_generation/python_api_integration

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 7.5 | quality: 9.72
- latency_total: 30.224s | tokens_per_second: 29.6
- input_tokens: 105 | output_tokens: 895
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos utilizando `httpx` y manejo de errores con retry exponencial:

```python
import httpx
import time
from typing import List, Dict

def get_expensive_products(bearer_token: str) -> List[Dict]:
    """
    Obtiene productos con precio > 100 de la API con autenticación Bearer.

    Args:
        bearer_token: Token de autenticación Bearer

    Returns:
        Lista de diccionarios con {id, name, price} de productos caros

    Raises:
        Exception: Si fallan todos los intentos de conexión
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }
    max_retries = 3
    timeout = 10.0  # segundos

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)

                # Verificar código de estado
                response.raise_for_status()

                products = response.json()

                # Filtrar productos con precio > 100 y seleccionar campos
                expensive_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]

                return expensive_products

        except httpx.TimeoutException as e:
            if attempt == max_retries - 1:
                raise Exception(f"Timeout después de {max_retries} intentos: {str(e)}")
            wait_time = (2 ** attempt)  # Backoff exponencial
            print(f"Timeout en intento {attempt + 1}. Reintento en {wait_time}s...")
            time.sleep(wait_time)

        except httpx.HTTPStatusError as e:
            if attempt == max_retries - 1:
                raise Exception(f"Error HTTP después de {max_retries} intentos: {str(e)}")
            wait_time = (2 ** attempt)
            print(f"Error HTTP {e.response.status_code} en intento {attempt + 1}. Reintento en {wait_time}s...")
            time.sleep(wait_time)

        except httpx.NetworkError as e:
            if attempt == max_retries - 1:
                raise Exception(f"Error de red después de {max_retries} intentos: {str(e)}")
            wait_time = (2 ** attempt)
            print(f"Error de red en intento {attempt + 1}. Reintento en {wait_time}s...")
            time.sleep(wait_time)

        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Error inesperado después de {max_retries} intentos: {str(e)}")
            wait_time = (2 ** attempt)
            print(f"Error inesperado en intento {attempt + 1}. Reintento en {wait_time}s...")
            time.sleep(wait_time)

    raise Exception("Se agotaron todos los intentos sin éxito")
```

### Características implementadas:
1. **GET con autenticación Bearer**: Usa el token en los headers
2. **Filtro de productos**: Solo incluye productos con precio > 100
3. **Formato de salida**: Lista de diccionarios con solo id, name y price
4. **Manejo de errores**:
   - Timeout (10 segundos)
   - Errores HTTP (4xx, 5xx)
   - Errores de red
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Espera de 1s, 2s, 4s entre intentos (2^attempt)
6. **Solo httpx**: Sin dependencias adicionales

### Uso ejemplo:
```python
try:
    token = "tu_token_aqui"
    expensive_products = get_expensive_products(token)
    print(expensive_products)
except Exception as e:
    print(f"Error: {str(e)}")
```