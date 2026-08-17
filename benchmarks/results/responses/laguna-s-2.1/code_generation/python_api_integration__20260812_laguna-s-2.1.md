# Poolside Laguna S 2.1 — code_generation/python_api_integration

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 9.05 | quality: 9.72
- latency_total: 9.804s | tokens_per_second: 97.9
- input_tokens: 154 | output_tokens: 960
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import random

def get_filtered_products(bearer_token: str) -> list[dict]:
    """
    Obtiene productos desde la API y filtra los que tienen precio > 100.
    
    Args:
        bearer_token (str): Token de autenticación Bearer.
        
    Returns:
        list[dict]: Lista de productos con {id, name, price} donde price > 100.
        
    Raises:
        Exception: Si ocurre un error después de 3 reintentos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    
    max_retries = 3
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos de error HTTP
                
                products_data = response.json()
                
                # Filtrar productos con precio > 100 y extraer solo los campos necesarios
                filtered_products = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"),
                        "price": product.get("price")
                    }
                    for product in products_data
                    if isinstance(product.get("price"), (int, float)) and product.get("price") > 100
                ]
                
                return filtered_products
                
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            if attempt < max_retries - 1:  # No esperar después del último intento
                delay = base_delay * (2 ** attempt) + random.uniform(0, 1)  # Backoff exponencial con jitter
                time.sleep(delay)
            else:
                raise Exception(f"Error de red después de {max_retries} intentos: {str(e)}")
                
        except httpx.HTTPStatusError as e:
            # Errores HTTP (4xx, 5xx) - no reintentar
            raise Exception(f"Error HTTP {e.response.status_code}: {e.response.text}")
            
        except Exception as e:
            # Otros errores inesperados
            raise Exception(f"Error inesperado: {str(e)}")
    
    # Este return es teóricamente inalcanzable debido al raise en el último intento
    return []
```

### Características implementadas:

1. **Autenticación Bearer**: El token se incluye en el encabezado `Authorization`.
2. **Filtrado por precio**: Solo se retornan productos con `price > 100`.
3. **Estructura de retorno**: Devuelve una lista de diccionarios con `{id, name, price}`.
4. **Manejo de errores**:
   - `httpx.TimeoutException`: Tiempo de espera agotado.
   - `httpx.NetworkError`: Problemas de red.
   - `httpx.HTTPStatusError`: Errores HTTP (códigos 4xx/5xx).
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos.
   - Retardo base de 1 segundo, duplicado en cada reintento (`2^attempt`).
   - Añade jitter aleatorio para evitar sincronización de reintentos.
6. **Timeout de 10 segundos**: Configurado en el cliente HTTP.
7. **Sin dependencias externas**: Solo utiliza `httpx`, `time` y `random` (incluidos en el estándar de Python).

La función maneja correctamente los casos edge como datos faltantes o tipos incorrectos en el campo `price`.