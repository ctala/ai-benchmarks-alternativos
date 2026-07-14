# DeepSeek V3 — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.61 | quality: 9.44
- latency_total: 30.793s | tokens_per_second: 51.2
- input_tokens: 110 | output_tokens: 1577
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx`:

```python
import httpx
import asyncio
from typing import List, Dict, Optional
import time
import logging

# Configurar logging para ver los reintentos
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_products_with_retry(
    token: str,
    max_retries: int = 3,
    base_delay: float =)x1.0,
    timeout: float = 10.0
) -> List[Dict[str, any]]:
    """
    Obtiene productos de la API con reintentos exponenciales.
    
    Args:
        token: Token Bearer para autenticación
        max_retries: Número máximo de reintentos (default: 3)
        base_delay: Delay base para backoff exponencial (default: 1.0)
        timeout: Timeout para cada request (default: 10.0)
    
    Returns:
        Lista de diccionarios con productos filtrados {id, name, price}
    
    Raises:
        httpx.RequestError: Si todos los reintentos fallan
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(max_retries):
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrar productos con precio > 100 y extraer campos requeridos
                filtered_products = []
                for product in products:
                    if "price" in product and product["price"] > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price")
                        })
                
                return filtered_products
                
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt == max_retries - 1:
                logger.error(f"Todos los {max_retries} intentos fallaron: {e}")
                raise
            
            # Calcular delay exponencial
            delay = base_delay * (2 ** attempt)
            logger.warning(f"Intento {attempt + 1} fallado. Reintentando en {delay} segundos. Error: {e}")
            
            # Esperar antes del siguiente intento
            await asyncio.sleep(delay)
    
    # Nunca debería llegar aquí, pero por seguridad
    return []

def get_filtered_products_sync(token: str) -> List[Dict[str, any]]:
    """
    Versión síncrona para compatibilidad con código no-asíncrono.
    """
    return asyncio.run(fetch_products_with_retry(token))

# Versión alternativa síncrona usando httpx síncrono
def get_filtered_products_sync_alternative(
    token: str,
    max_retries: int = 3,
    base_delay: float = 1.0,
    timeout: float = 10.0
) -> List[Dict[str, any]]:
    """
    Versión síncrona usando cliente síncrono de httpx.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                
                products = response.json()
                
                # Filtrar productos con precio > 100 y extraer campos requeridos
                filtered_products = []
                for product in products:
                    if "price" in product and product["price"] > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price")
                        })
                
                return filtered_products
                
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if attempt == max_retries - 1:
                logger.error(f"Todos los {max_retries} intentos fallaron: {e}")
                raise
            
            # Calcular delay exponencial
            delay = base_delay * (2 ** attempt)
            logger.warning(f"Intento {attempt + 1} fallado. Reintentando en {delay} segundos. Error: {e}")
            
            # Esperar antes del siguiente intento
            time.sleep(delay)
    
    return []

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con función asíncrona
    async def main_async():
        token = "tu_token_aqui"
        try:
            products = await fetch_products_with_retry(token)
            print(f"Productos obtenidos: {len(products)}")
            for product in products:
                print(product)
        except Exception as e:
            print(f"Error al obtener productos: {e}")
    
    # Ejemplo con función síncrona
    def main_sync():
        token = "tu_token_aqui"
        try:
            products = get_filtered_products_sync_alternative(token)
            print(f"Productos obtenidos: {len(products)}")
            for product in products:
                print(product)
        except Exception as e:
            print(f"Error al obtener productos: {e}")
    
    # Ejecutar ejemplo síncrono
    main_sync()
    
    # Para ejecutar el ejemplo asíncrono:
    # asyncio.run(main_async())
```

## Características principales:

1. **Autenticación Bearer**: Usa el token proporcionado en el header `Authorization`.

2. **Filtrado de productos**: Solo incluye productos con `price > 100` y extrae solo `id`, `name`, `price`.

3. **Manejo de errores**: Captura `httpx.RequestError` (errores de red) y `httpx.HTTPStatusError` (errores HTTP).

4. **Timeout**: Configurable a 10 segundos por defecto.

5. **Retry con backoff exponencial**: 
   - Máximo 3 intentos
   - Delay base: 1 segundo
   - Backoff exponencial: 1s, 2s, 4s (por defecto)

6. **Versiones disponibles**:
   - Asíncrona (`fetch_products_with_retry`): Para uso con async/await
   - Síncrona (`get_filtered_products_sync_alternative`): Para código síncrono tradicional

7. **Logging**: Incluye logging para monitorear los reintentos.

## Instalación requerida:
```bash
pip install httpx
```

La función es robusta y maneja casos como:
- Respuestas HTTP no exitosas
- Timeouts de red
- Errores de conexión
- Datos faltantes en la respuesta JSON
- Reintentos automáticos con espera exponencial