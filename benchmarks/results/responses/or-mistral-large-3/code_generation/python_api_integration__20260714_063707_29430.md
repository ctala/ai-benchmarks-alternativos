# Mistral Large 3 675B — code_generation/python_api_integration

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.59 | quality: 9.72
- latency_total: 14.831s | tokens_per_second: 69.0
- input_tokens: 105 | output_tokens: 1023
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos solicitados, utilizando `httpx` para las peticiones HTTP y manejo de errores con retry y backoff exponencial:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    min_price: float = 100.0,
    timeout: int = 10,
    max_retries: int = 3
) -> List[Dict[str, Optional[object]]]:
    """
    Obtiene productos con precio mayor a min_price desde una API con autenticación Bearer.

    Args:
        token: Token de autenticación Bearer
        base_url: URL base de la API (default: "https://api.example.com/products")
        min_price: Precio mínimo para filtrar productos (default: 100.0)
        timeout: Timeout en segundos para la petición (default: 10)
        max_retries: Número máximo de intentos (default: 3)

    Returns:
        Lista de diccionarios con {id, name, price} de productos que cumplen el filtro.
        En caso de error, retorna una lista vacía.
    """
    headers = {"Authorization": f"Bearer {token}"}
    products = []

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx

                data = response.json()
                if not isinstance(data, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtrar y transformar los productos
                products = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price")
                    }
                    for product in data
                    if isinstance(product.get("price"), (int, float)) and product.get("price") > min_price
                ]
                return products

        except httpx.TimeoutException:
            if attempt == max_retries - 1:
                print(f"Timeout después de {max_retries} intentos")
                return []
            wait_time = (2 ** attempt)  # Backoff exponencial (1, 2, 4 segundos...)
            print(f"Timeout. Reintentando en {wait_time} segundos... (Intento {attempt + 1}/{max_retries})")
            time.sleep(wait_time)

        except httpx.HTTPStatusError as e:
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            return []

        except httpx.RequestError as e:
            print(f"Error de red: {str(e)}")
            if attempt == max_retries - 1:
                return []
            wait_time = (2 ** attempt)
            print(f"Reintentando en {wait_time} segundos... (Intento {attempt + 1}/{max_retries})")
            time.sleep(wait_time)

        except ValueError as e:
            print(f"Error en la respuesta de la API: {str(e)}")
            return []

        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return []

    return products
```

### Características de la función:

1. **Autenticación Bearer**: Incluye el token en los headers de la petición.
2. **Filtrado de productos**: Solo retorna productos con precio > 100 (configurable).
3. **Formato de salida**: Lista de diccionarios con solo `id`, `name` y `price`.
4. **Manejo de errores**:
   - Timeout (10 segundos)
   - Errores HTTP (4xx, 5xx)
   - Errores de red
   - Validación de la respuesta de la API
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Espera exponencial (1s, 2s, 4s) entre intentos
6. **Sin dependencias externas**: Solo usa `httpx` (y la librería estándar de Python).

### Ejemplo de uso:

```python
token = "tu_token_aqui"
products = get_expensive_products(token)
print(products)
```

### Notas adicionales:

- La función retorna una lista vacía en caso de error.
- Los mensajes de error se imprimen por consola (puedes modificarlos para usar logging si lo prefieres).
- El timeout se aplica tanto a la conexión como a la lectura de la respuesta.
- La función es tipada con `typing` para mejor claridad.