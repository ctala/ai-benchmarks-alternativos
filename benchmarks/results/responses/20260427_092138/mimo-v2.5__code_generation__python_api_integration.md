# MiMo V2.5 (Xiaomi) — code_generation/python_api_integration

- model_id: `mimo-v2.5`
- success: True  | final: 7.71 | quality: 8.88
- latency_total: 19.631s | tokens_per_second: 96.6
- input_tokens: 351 | output_tokens: 1897
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos:

```python
import httpx
import time
from typing import List, Dict, Any


def get_filtered_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100
    y retorna solo los campos id, name y price.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con productos filtrados
        
    Raises:
        Exception: Si falla después de 3 intentos
    """
    
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout_seconds = 10
    
    for attempt in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(
                    url,
                    headers=headers,
                    timeout=timeout_seconds
                )
                response.raise_for_status()
                
                # Parsear la respuesta JSON
                products = response.json()
                
                # Filtrar productos con precio > 100 y extraer solo los campos necesarios
                filtered_products = []
                for product in products:
                    if product.get("price", 0) > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price")
                        })
                
                return filtered_products
                
        except httpx.TimeoutException:
            wait_time = 2 ** (attempt + 1)  # Backoff exponencial: 2, 4, 8 segundos
            print(f"Timeout en intento {attempt + 1}. Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
            
        except httpx.RequestError as e:
            wait_time = 2 ** (attempt + 1)
            print(f"Error de red en intento {attempt + 1}: {e}. Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
            
        except httpx.HTTPStatusError as e:
            if e.response.status_code >= 500:
                # Solo reintentar en errores del servidor
                wait_time = 2 ** (attempt + 1)
                print(f"Error del servidor {e.response.status_code} en intento {attempt + 1}. "
                      f"Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
            else:
                # Para errores 4xx (excepto 408 Timeout), no reintentar
                raise Exception(f"Error HTTP {e.response.status_code}: {e}")
    
    # Si llegamos aquí, todos los intentos fallaron
    raise Exception(f"Todos los {max_retries} intentos fallaron")


# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token = "tu_token_aqui"
        productos = get_filtered_products(token)
        print(f"Se encontraron {len(productos)} productos con precio > 100:")
        for producto in productos:
            print(f"  - {producto['name']}: ${producto['price']} (ID: {producto['id']})")
    except Exception as e:
        print(f"Error: {e}")
```

## Características principales:

1. **Autenticación Bearer**: Usa el token en el header `Authorization: Bearer {token}`

2. **Filtrado**: Solo incluye productos con `price > 100` y retorna `{id, name, price}`

3. **Timeout**: Configurado a 10 segundos por request

4. **Retry con backoff exponencial**:
   - 3 intentos máximo
   - Backoff: 2s → 4s → 8s
   - Solo reintenta en errores de red, timeout, y errores del servidor (5xx)

5. **Manejo de errores**:
   - `TimeoutException`: Timeout de conexión o lectura
   - `RequestError`: Errores de red generales
   - `HTTPStatusError`: Errores HTTP específicos

6. **Context manager**: Usa `httpx.Client()` como context manager para limpieza adecuada

## Notas:
- Asegúrate de tener `httpx` instalado: `pip install httpx`
- La función asume que la API retorna una lista de objetos JSON
- Los campos `id`, `name` y `price` deben existir en la respuesta
- Puedes ajustar el manejo de errores según tus necesidades específicas