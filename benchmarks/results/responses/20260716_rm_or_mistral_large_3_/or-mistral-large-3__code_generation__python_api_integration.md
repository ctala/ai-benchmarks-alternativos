# Mistral Large 3 675B — code_generation/python_api_integration

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.61 | quality: 9.72
- latency_total: 12.857s | tokens_per_second: 72.6
- input_tokens: 105 | output_tokens: 933
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos solicitados, utilizando `httpx` para las peticiones HTTP y manejando los errores, timeouts y reintentos con backoff exponencial:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products(token: str) -> Optional[List[Dict[str, str | float]]]:
    """
    Obtiene productos con precio > 100 desde la API, retornando solo id, name y price.

    Args:
        token: Bearer token para autenticación.

    Returns:
        Lista de diccionarios con {id, name, price} de productos caros, o None si falla.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0  # 10 segundos de timeout
    max_retries = 3
    base_delay = 1  # 1 segundo de delay inicial

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx

                products = response.json()
                if not isinstance(products, list):
                    print("Error: La respuesta no es una lista de productos")
                    return None

                # Filtrar y transformar los productos
                expensive_products = [
                    {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p.get("price") > 100
                ]

                return expensive_products

        except httpx.TimeoutException:
            print(f"Timeout en intento {attempt + 1}/{max_retries}")
        except httpx.HTTPStatusError as e:
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            break  # No reintentar en errores 4xx (excepto 429)
        except httpx.RequestError as e:
            print(f"Error de red en intento {attempt + 1}: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            break  # No reintentar en errores desconocidos

        # Calcular delay con backoff exponencial (1, 2, 4 segundos)
        if attempt < max_retries - 1:
            delay = base_delay * (2 ** attempt)
            print(f"Reintentando en {delay} segundos...")
            time.sleep(delay)

    print("Se agotaron los intentos o ocurrió un error irrecuperable")
    return None
```

### Características clave:
1. **Autenticación Bearer**: Usa el token proporcionado en los headers.
2. **Filtrado**: Solo incluye productos con `price > 100` y verifica que el precio sea numérico.
3. **Formato de salida**: Retorna una lista de diccionarios con solo `id`, `name` y `price`.
4. **Manejo de errores**:
   - Timeout (10 segundos)
   - Errores de red (`httpx.RequestError`)
   - Errores HTTP (`httpx.HTTPStatusError`)
   - Errores inesperados
5. **Retry con backoff exponencial**:
   - 3 intentos máximos
   - Delay inicial de 1 segundo, duplicándose en cada intento (1s, 2s, 4s)
   - No reintenta en errores 4xx (excepto 429 que sería manejado automáticamente por httpx)

### Ejemplo de uso:
```python
token = "tu_token_aqui"
products = get_expensive_products(token)
if products:
    print("Productos caros encontrados:")
    for p in products:
        print(p)
else:
    print("No se pudieron obtener los productos")
```

### Notas:
- La función retorna `None` en caso de fallo después de todos los reintentos.
- Usa `httpx.Client` para mejor manejo de conexiones persistentes.
- El timeout se aplica tanto a la conexión como a la lectura de la respuesta.