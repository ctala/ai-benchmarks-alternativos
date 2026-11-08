# Mistral Small 4 — code_generation/python_api_integration

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.18 | quality: 9.72
- latency_total: 4.869s | tokens_per_second: 170.3
- input_tokens: 117 | output_tokens: 829
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

Aquí tienes una función en Python que cumple con todos los requisitos usando `httpx` para las peticiones HTTP y manejando los casos solicitados:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products(bearer_token: str) -> Optional[List[Dict]]:
    """
    Obtiene productos con precio > 100 desde la API, con manejo de errores y retry.

    Args:
        bearer_token: Token para autenticación Bearer

    Returns:
        Lista de diccionarios con productos {id, name, price} o None si falla
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}

    max_retries = 3
    base_delay = 1.0  # segundos

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4XX/5XX

                products = response.json()
                expensive_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]

                return expensive_products

        except httpx.HTTPStatusError as e:
            print(f"Intento {attempt + 1}: Error HTTP {e.response.status_code}")
        except httpx.NetworkError as e:
            print(f"Intento {attempt + 1}: Error de red - {str(e)}")
        except httpx.TimeoutException as e:
            print(f"Intento {attempt + 1}: Timeout - {str(e)}")
        except Exception as e:
            print(f"Intento {attempt + 1}: Error inesperado - {str(e)}")

        if attempt < max_retries - 1:
            delay = base_delay * (2 ** attempt)  # Backoff exponencial
            print(f"Reintentando en {delay:.1f} segundos...")
            time.sleep(delay)

    print("Máximo número de reintentos alcanzado")
    return None
```

### Características implementadas:

1. **Autenticación Bearer**: Usa el token proporcionado en los headers
2. **Filtrado de productos**: Solo incluye productos con precio > 100
3. **Formato de salida**: Retorna lista de dicts con solo {id, name, price}
4. **Manejo de errores**:
   - Errores de red (NetworkError)
   - Timeouts (TimeoutException)
   - Errores HTTP (HTTPStatusError)
   - Otros errores inesperados
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Tiempo de espera inicial de 1 segundo
   - Cada retry duplica el tiempo de espera (1s, 2s, 4s)
6. **Timeout**: 10 segundos por petición

### Uso de ejemplo:

```python
token = "tu_token_aqui"
products = get_expensive_products(token)
if products is not None:
    print(f"Encontrados {len(products)} productos caros:")
    for p in products:
        print(p)
else:
    print("No se pudieron obtener los productos")
```

### Notas:
- El código asume que la respuesta de la API es un JSON con una lista de productos donde cada producto tiene al menos "id", "name" y "price"
- Si la estructura de los datos es diferente, se debe ajustar el filtrado y la selección de campos
- El timeout de 10 segundos se aplica tanto a la conexión como a la lectura de la respuesta