# Mistral Large 3 675B (NIM) — code_generation/python_api_integration

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 7.25 | quality: 9.44
- latency_total: 284.897s | tokens_per_second: 3.7
- input_tokens: 108 | output_tokens: 1060
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos especificados, utilizando `httpx` sin dependencias adicionales:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products(
    token: str,
    min_price: float = 100.0,
    max_retries: int = 3,
    initial_timeout: float = 10.0
) -> Optional[List[Dict[str, str | float]]]:
    """
    Obtiene productos con precio mayor a min_price desde la API.

    Args:
        token: Bearer token para autenticación
        min_price: Precio mínimo para filtrar productos (default: 100.0)
        max_retries: Máximo número de reintentos (default: 3)
        initial_timeout: Timeout inicial en segundos (default: 10.0)

    Returns:
        Lista de diccionarios con {id, name, price} de productos filtrados,
        o None si ocurre un error después de todos los reintentos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(max_retries):
        try:
            # Calcular timeout con backoff exponencial
            timeout = min(initial_timeout * (2 ** attempt), 30.0)  # Máximo 30 segundos

            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)

                # Verificar código de estado
                response.raise_for_status()

                # Procesar respuesta
                products = response.json()
                if not isinstance(products, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtrar productos y seleccionar campos requeridos
                result = []
                for product in products:
                    try:
                        if float(product.get("price", 0)) > min_price:
                            result.append({
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": product.get("price")
                            })
                    except (ValueError, TypeError):
                        continue  # Ignorar productos con precio inválido

                return result

        except httpx.TimeoutException:
            print(f"Timeout en intento {attempt + 1}/{max_retries}")
        except httpx.HTTPStatusError as e:
            print(f"Error HTTP {e.response.status_code} en intento {attempt + 1}/{max_retries}")
            if e.response.status_code >= 500:  # Solo reintentar en errores del servidor
                time.sleep(2 ** attempt)  # Backoff exponencial
            else:
                break  # No reintentar en errores del cliente (4xx)
        except httpx.NetworkError as e:
            print(f"Error de red en intento {attempt + 1}/{max_retries}: {str(e)}")
            time.sleep(2 ** attempt)  # Backoff exponencial
        except ValueError as e:
            print(f"Error en datos de respuesta: {str(e)}")
            break  # No reintentar en errores de parsing
        except Exception as e:
            print(f"Error inesperado en intento {attempt + 1}/{max_retries}: {str(e)}")
            break

    print("Se agotaron todos los intentos o ocurrió un error irrecuperable")
    return None
```

### Características principales:

1. **Autenticación Bearer**: Incluye el token en los headers de la petición
2. **Filtrado de productos**: Solo retorna productos con precio > 100 (configurable)
3. **Formato de salida**: Lista de diccionarios con solo `id`, `name` y `price`
4. **Manejo de errores**:
   - Timeout (configurable)
   - Errores HTTP (4xx, 5xx)
   - Errores de red
   - Errores en parsing de datos
5. **Retry con backoff exponencial**:
   - Hasta 3 intentos (configurable)
   - Tiempo de espera aumenta exponencialmente (1s, 2s, 4s...)
   - Timeout también aumenta exponencialmente (10s, 20s... con máximo de 30s)

### Ejemplo de uso:

```python
token = "tu_token_aqui"
products = get_expensive_products(token)
if products:
    print(f"Productos caros encontrados: {len(products)}")
    for product in products:
        print(product)
else:
    print("No se pudieron obtener los productos")
```

### Notas:
- La función devuelve `None` si fallan todos los intentos o ocurre un error irrecuperable
- Los mensajes de error se imprimen por consola pero puedes modificarlos para usar logging
- El timeout máximo está limitado a 30 segundos para evitar esperas demasiado largas