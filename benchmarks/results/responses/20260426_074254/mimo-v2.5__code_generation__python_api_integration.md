# MiMo-V2.5 (omnimodal) — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.01 | quality: 8.32
- latency_total: 12.659s | tokens_per_second: 124.6
- input_tokens: 351 | output_tokens: 1577
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes una función completa con todas las solicitudes:

```python
import httpx
from typing import List, Dict, Any, Optional
import time
import logging

# Configurar logging para debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_retries: int = 3
) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100,
    y retorna una lista de diccionarios con solo id, name y price.
    
    Args:
        token: Token de autenticación Bearer
        base_url: URL base de la API
        timeout: Tiempo máximo de espera en segundos
        max_retries: Número máximo de reintentos
    
    Returns:
        Lista de diccionarios con productos filtrados
        
    Raises:
        ValueError: Si el token está vacío
        httpx.HTTPError: Si hay errores de conexión después de los reintentos
    """
    if not token:
        raise ValueError("El token de autenticación no puede estar vacío")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            logger.info(f"Intento {attempt + 1}/{max_retries} - Conectando a {base_url}")
            
            with httpx.Client(
                timeout=timeout,
                follow_redirects=True
            ) as client:
                response = client.get(base_url, headers=headers)
                
                # Verificar si la respuesta es exitosa
                response.raise_for_status()
                
                # Parsear la respuesta JSON
                products_data = response.json()
                
                # Verificar que la respuesta sea una lista
                if not isinstance(products_data, list):
                    raise ValueError(f"Formato de respuesta inesperado: {type(products_data)}")
                
                # Filtrar productos con precio > 100
                filtered_products = []
                for product in products_data:
                    try:
                        if (
                            isinstance(product, dict) and
                            "id" in product and
                            "name" in product and
                            "price" in product and
                            float(product["price"]) > 100
                        ):
                            filtered_products.append({
                                "id": product["id"],
                                "name": product["name"],
                                "price": float(product["price"])
                            })
                    except (ValueError, TypeError) as e:
                        logger.warning(f"Error procesando producto {product.get('id', 'desconocido')}: {e}")
                        continue
                
                logger.info(f"Se encontraron {len(filtered_products)} productos con precio > 100")
                return filtered_products
                
        except httpx.TimeoutException as e:
            last_exception = e
            logger.warning(f"Timeout en intento {attempt + 1}: {e}")
            
        except httpx.NetworkError as e:
            last_exception = e
            logger.warning(f"Error de red en intento {attempt + 1}: {e}")
            
        except httpx.HTTPStatusError as e:
            last_exception = e
            logger.warning(f"Error HTTP {e.response.status_code} en intento {attempt + 1}: {e}")
            
        except Exception as e:
            last_exception = e
            logger.warning(f"Error inesperado en intento {attempt + 1}: {e}")
        
        # Backoff exponencial: 1, 2, 4, 8, 16... segundos
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt  # 2^0=1, 2^1=2, 2^2=4...
            logger.info(f"Esperando {wait_time} segundos antes del siguiente intento...")
            time.sleep(wait_time)
    
    # Si llegamos aquí, todos los reintentos fallaron
    logger.error(f"Todos los {max_retries} intentos fallaron")
    raise last_exception

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con token ficticio
    try:
        products = fetch_products(token="tu_token_aqui")
        print(f"Productos encontrados: {len(products)}")
        for product in products:
            print(f"  ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']}")
            
    except Exception as e:
        print(f"Error al obtener productos: {e}")
```

## Características principales:

1. **Autenticación Bearer**: Usa headers con `Authorization: Bearer {token}`
2. **Filtrado**: Solo productos con precio > 100
3. **Manejo de errores**: Captura timeouts, errores de red, HTTP errors y errores generales
4. **Retry con backoff exponencial**: 
   - Espera 1s en el primer retry
   - 2s en el segundo
   - 4s en el tercero
   - Hasta `max_retries` intentos
5. **Logging**: Incluye logs detallados para debugging
6. **Validación**: Verifica que el token no esté vacío y que la respuesta tenga el formato esperado

## Uso básico:

```python
# Con token
products = fetch_products(token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")

# Con parámetros personalizados
products = fetch_products(
    token="tu_token",
    timeout=15.0,
    max_retries=5
)
```

## Notas importantes:

- **Dependencia**: Solo requiere `httpx` (`pip install httpx`)
- **Tipado**: Usa type hints para mejor documentación
- **Flexibilidad**: Los parámetros tienen valores por defecto pero son configurables
- **Robustez**: Maneja múltiples tipos de errores de forma diferente
- **Logging**: Proporciona información detallada para debugging

La función está lista para producción y maneja todos los requisitos solicitados de manera elegante y robusta.