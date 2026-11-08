# Step 3.5 Flash — code_generation/python_api_integration

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.85 | quality: 9.72
- latency_total: 17.935s | tokens_per_second: 74.0
- input_tokens: 118 | output_tokens: 1327
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

```python
import httpx
import time
from typing import List, Dict

def get_filtered_products(bearer_token: str) -> List[Dict[str, any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna lista simplificada.
    
    Args:
        bearer_token: Token de autenticación Bearer
        
    Returns:
        Lista de diccionarios con {id, name, price} de productos con precio > 100
        
    Raises:
        httpx.RequestError: Si fallan todos los reintentos
        ValueError: Si la respuesta no tiene el formato esperado
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza error para códigos 4xx/5xx
                
                products = response.json()
                
                # Validar que la respuesta es una lista
                if not isinstance(products, list):
                    raise ValueError("La respuesta no es una lista de productos")
                
                # Filtrar y mapear productos
                filtered = []
                for product in products:
                    try:
                        price = product.get("price")
                        if price is not None and price > 100:
                            filtered.append({
                                "id": product["id"],
                                "name": product["name"],
                                "price": price
                            })
                    except KeyError as e:
                        # Producto con campos faltantes, lo omitimos
                        continue
                
                return filtered
                
        except (httpx.RequestError, httpx.TimeoutException) as e:
            if attempt == max_retries - 1:
                raise  # Reintentos agotados
            
            # Backoff exponencial: 1, 2, 4 segundos
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
            
        except Exception as e:
            # Otros errores (JSON malformado, etc.) no se reintentan
            raise ValueError(f"Error procesando respuesta: {str(e)}")

# Ejemplo de uso:
# try:
#     products = get_filtered_products("tu_token_aqui")
#     print(products)
# except Exception as e:
#     print(f"Error: {e}")
```

**Características principales:**

1. **Autenticación Bearer**: Token incluido en header `Authorization`
2. **Timeout de 10 segundos**: Configurado en `httpx.Client(timeout=10.0)`
3. **Retry con backoff exponencial**:
   - 3 intentos máximo
   - Esperas: 1s, 2s, 4s entre intentos
   - Solo se reintenta en errores de red/timeout
4. **Manejo robusto de errores**:
   - `httpx.RequestError`: Problemas de conexión
   - `httpx.TimeoutException`: Timeout específico
   - `response.raise_for_status()`: Errores HTTP 4xx/5xx
   - Validación de formato JSON
5. **Filtrado eficiente**:
   - Solo incluye productos con `price > 100`
   - Extrae solo campos requeridos (`id`, `name`, `price`)
   - Omite productos con campos faltantes
6. **Sin dependencias externas**: Solo usa `httpx` (instalable via `pip install httpx`)

**Notas importantes:**
- La función asume que la API devuelve una lista de objetos JSON con al menos `id`, `name` y `price`
- Los productos sin `price` o con `price <= 100` se descartan automáticamente
- Los productos con campos faltantes (`id` o `name`) se omiten silenciosamente
- Los errores de formato JSON o estructura incorrecta se propagan como `ValueError` sin reintento