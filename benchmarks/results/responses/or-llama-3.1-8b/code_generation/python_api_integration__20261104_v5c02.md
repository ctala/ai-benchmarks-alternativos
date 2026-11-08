# Llama 3.1 8B Instant — code_generation/python_api_integration

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 9.07 | quality: 9.32
- latency_total: 4.701s | tokens_per_second: 145.3
- input_tokens: 112 | output_tokens: 683
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

Aquí te muestro una posible implementación de la función que cumplen con los requisitos que se te han especificado:
```python
import httpx
import json
import time
import random

def obtener_productos():
    # Configuración de la API
    url = "https://api.example.com/products"
    bearer_token = "TU_BEARER_TOKEN_AQUI"  # reemplaza con tu token de autenticación
    headers = {"Authorization": f"Bearer {bearer_token}"}

    # Configuración de retry con backoff exponencial
    max_intentos = 3
    backoff_factor = 0.5
    intentos = 0

    while intentos < max_intentos:
        try:
            # Intento de GET a la API
            response = httpx.get(url, headers=headers, timeout=10)

            # Verificar si la respuesta fue exitosa
            if response.status_code == 200:
                # Parsear la respuesta como JSON
                productos = json.loads(response.text)

                # Filtrar productos con precio > 100
                productos_filtrados = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in productos
                    if p["price"] > 100
                ]

                return productos_filtrados
            else:
                # Si la respuesta no es 200, reintentar
                print(f"Error {response.status_code}")
                intentos += 1
                time.sleep(backoff_factor * (2 ** intentos))
        except httpx.RequestError as e:
            # Manejo de errores de red
            print(f"Error de red: {e}")
            intentos += 1
            time.sleep(backoff_factor * (2 ** intentos))
        except httpx.TimeoutException as e:
            # Manejo de timeout
            print(f"Timeout: {e}")
            intentos += 1
            time.sleep(backoff_factor * (2 ** intentos))
    return None
```
La función `obtener_productos` intenta hacer un GET a la API de productos con autenticación Bearer token. Si la respuesta no es exitosa (es decir, si el código de estado no es 200), se reintentará hasta un máximo de 3 intentos con un backoff exponencial (es decir, el tiempo de espera entre intentos se duplica después de cada intento). Si se produce un error de red o un timeout, se maneja y se reintentará.

Ten en cuenta que debes reemplazar `TU_BEARER_TOKEN_AQUI` con tu token de autenticación real.

Recuerda que esta implementación asume que la API devuelve una lista de JSON con la siguiente estructura:
```json
[
  {"id": 1, "name": "Producto 1", "price": 50},
  {"id": 2, "name": "Producto 2", "price": 150},
  {"id": 3, "name": "Producto 3", "price": 250},
  ...
]
```
Si la estructura de la API es diferente, debes ajustar la función correspondientemente.