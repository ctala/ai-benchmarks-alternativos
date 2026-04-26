# DeepSeek V4 Flash (NIM) — code_generation/python_api_integration

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.06 | quality: 8.88
- latency_total: 273.386s | tokens_per_second: 3.8
- input_tokens: 110 | output_tokens: 1029
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí tienes la función Python que cumple con todos los requisitos usando `httpx`:

```python
import httpx
import asyncio
from typing import List, Dict, Optional
import time

async def get_filtered_products(token: str) -> List[Dict]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna solo id, name, price.
    
    Args:
        token: Bearer token para autenticación
        
    Returns:
        Lista de diccionarios con {id, name, price} de productos con precio > 100
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    max_retries = 3
    base_delay = 1  # segundo
    
    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrar productos con precio > 100
                filtered_products = [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"]
                    }
                    for product in products
                    if product.get("price", 0) > 100
                ]
                
                return filtered_products
                
        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError) as e:
            # Error de red o timeout
            if attempt < max_retries - 1:  # No esperar en el último intento
                delay = base_delay * (2 ** attempt)  # Backoff exponencial
                print(f"Intento {attempt + 1} falló: {e}. Reintentando en {delay} segundos...")
                await asyncio.sleep(delay)
            else:
                print(f"Todos los {max_retries} intentos fallaron. Último error: {e}")
                raise
                
        except httpx.HTTPStatusError as e:
            # Error HTTP (4xx, 5xx) - no reintentar para errores del cliente
            print(f"Error HTTP {e.response.status_code}: {e}")
            raise
            
        except Exception as e:
            # Otros errores inesperados
            print(f"Error inesperado: {e}")
            raise
    
    return []  # En caso de que todos los intentos fallen y no se haya levantado excepción

# Versión síncrona (wrapper)
def get_filtered_products_sync(token: str) -> List[Dict]:
    """
    Versión síncrona de la función asíncrona.
    """
    return asyncio.run(get_filtered_products(token))

# Ejemplo de uso:
if __name__ == "__main__":
    # Uso asíncrono
    async def main():
        try:
            token = "tu_token_aqui"
            products = await get_filtered_products(token)
            print(f"Productos filtrados: {products}")
        except Exception as e:
            print(f"Error al obtener productos: {e}")
    
    asyncio.run(main())
    
    # O versión síncrona
    # products = get_filtered_products_sync("tu_token_aqui")
```

**Características de la implementación:**

1. **Autenticación Bearer**: Se incluye el token en el header `Authorization`
2. **Filtrado**: Filtra productos donde `price > 100`
3. **Formato de retorno**: Solo incluye `id`, `name`, `price`
4. **Manejo de errores**:
   - Timeout de 10 segundos configurado en el cliente
   - Captura específica de errores de red y timeout
   - Errores HTTP (4xx, 5xx) se manejan por separado
5. **Retry con backoff exponencial**:
   - Máximo 3 intentos
   - Delay inicial de 1 segundo
   - Multiplicador exponencial: 1s, 2s, 4s entre intentos
   - Solo reintenta en errores de red/timeout, no en errores HTTP

**Notas adicionales:**
- La función es asíncrona por defecto usando `async/await`
- Se incluye una versión síncrona como wrapper
- Los errores HTTP (como 401 Unauthorized) no se reintentan automáticamente
- Se imprime información sobre los reintentos para debugging