# DeepSeek V3 — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 7.59 | quality: 8.32
- latency_total: 41.681s | tokens_per_second: 46.7
- input_tokens: 110 | output_tokens: 1948
- judge_score: 3.8 | justificación: 

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

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx`:

```python
import httpx
import asyncio
from typing import List, Dict, Any, Optional
import time

async def fetch_products_with_retry(
    token: str,
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna datos específicos.
    
    Args:
        token: Token de autenticación Bearer
        max_retries: Número máximo de reintentos (default: 3)
        timeout: Timeout en segundos (default: 10)
    
    Returns:
        Lista de diccionarios con {id, name, price} de productos con precio > 100
    
    Raises:
        httpx.RequestError: Si fallan todos los reintentos
        httpx.HTTPStatusError: Si la respuesta HTTP tiene código de error
    """
    base_delay = 1.0  # Retardo inicial en segundos
    max_delay = 30.0  # Retardo máximo en segundos
    
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    last_error = None
    
    for attempt in range(max_retries):
        try:
            # Configurar timeout
            timeout_config = httpx.Timeout(timeout)
            
            async with httpx.AsyncClient(timeout=timeout_config) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx
                
                data = response.json()
                
                # Filtrar y transformar productos
                filtered_products = []
                for product in data.get("products", []):
                    price = product.get("price", 0)
                    
                    # Filtrar productos con precio > 100
                    if price > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price
                        })
                
                return filtered_products
                
        except httpx.TimeoutException as e:
            last_error = e
            print(f"Timeout en intento {attempt + 1}/{max_retries}: {e}")
            
        except httpx.HTTPStatusError as e:
            # No reintentar para errores del cliente (4xx) excepto 429 (Too Many Requests)
            if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                raise e
            last_error = e
            print(f"Error HTTP {e.response.status_code} en intento {attempt + 1}/{max_retries}")
            
        except httpx.RequestError as e:
            last_error = e
            print(f"Error de red en intento {attempt + 1}/{max_retries}: {e}")
            
        except Exception as e:
            last_error = e
            print(f"Error inesperado en intento {attempt + 1}/{max_retries}: {e}")
        
        # Calcular retardo exponencial con jitter
        if attempt < max_retries - 1:
            delay = min(base_delay * (2 ** attempt), max_delay)
            # Añadir jitter aleatorio para evitar thundering herd
            jitter = delay * 0.1  # 10% de jitter
            delay_with_jitter = delay + (time.time() % jitter)
            
            print(f"Reintentando en {delay_with_jitter:.2f} segundos...")
            await asyncio.sleep(delay_with_jitter)
    
    # Si llegamos aquí, todos los intentos fallaron
    raise httpx.RequestError(f"Todos los {max_retries} intentos fallaron. Último error: {last_error}")


# Versión síncrona si prefieres no usar async/await
def fetch_products_sync(
    token: str,
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Versión síncrona de fetch_products_with_retry.
    """
    base_delay = 1.0
    max_delay = 30.0
    
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    last_error = None
    
    for attempt in range(max_retries):
        try:
            timeout_config = httpx.Timeout(timeout)
            
            with httpx.Client(timeout=timeout_config) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                data = response.json()
                
                filtered_products = []
                for product in data.get("products", []):
                    price = product.get("price", 0)
                    
                    if price > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price
                        })
                
                return filtered_products
                
        except httpx.TimeoutException as e:
            last_error = e
            print(f"Timeout en intento {attempt + 1}/{max_retries}: {e}")
            
        except httpx.HTTPStatusError as e:
            if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                raise e
            last_error = e
            print(f"Error HTTP {e.response.status_code} en intento {attempt + 1}/{max_retries}")
            
        except httpx.RequestError as e:
            last_error = e
            print(f"Error de red en intento {attempt + 1}/{max_retries}: {e}")
            
        except Exception as e:
            last_error = e
            print(f"Error inesperado en intento {attempt + 1}/{max_retries}: {e}")
        
        if attempt < max_retries - 1:
            delay = min(base_delay * (2 ** attempt), max_delay)
            jitter = delay * 0.1
            delay_with_jitter = delay + (time.time() % jitter)
            
            print(f"Reintentando en {delay_with_jitter:.2f} segundos...")
            time.sleep(delay_with_jitter)
    
    raise httpx.RequestError(f"Todos los {max_retries} intentos fallaron. Último error: {last_error}")


# Ejemplo de uso
async def main():
    # Tu token de autenticación
    token = "tu_token_aqui"
    
    try:
        # Usando la versión asíncrona (recomendada)
        products = await fetch_products_with_retry(token)
        print(f"Productos encontrados: {len(products)}")
        for product in products:
            print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: {product['price']}")
            
    except Exception as e:
        print(f"Error al obtener productos: {e}")


# Para ejecutar el ejemplo asíncrono
if __name__ == "__main__":
    # Ejecutar versión asíncrona
    asyncio.run(main())
    
    # O usar versión síncrona
    # token = "tu_token_aqui"
    # products = fetch_products_sync(token)
    # print(products)
```

**Características principales:**

1. **Autenticación Bearer**: Incluye el token en los headers
2. **Filtrado por precio**: Solo productos con `price > 100`
3. **Estructura de salida**: Lista de diccionarios con `{id, name, price}`
4. **Manejo de errores**:
   - Timeout configurable (10 segundos por defecto)
   - Errores de red (conexión, DNS, etc.)
   - Errores HTTP (4xx, 5xx)
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Delay exponencial: 1s, 2s, 4s (con máximo de 30s)
   - Jitter aleatorio para evitar sincronización
   - No reintenta errores 4xx (excepto 429 - Too Many Requests)

**Notas importantes:**
- La función asume que la API retorna un JSON con una clave `"products"` que contiene la lista
- Ajusta el parsing según la estructura real de la API
- La versión asíncrona es más eficiente para múltiples peticiones
- Instala httpx si no lo tienes: `pip install httpx`