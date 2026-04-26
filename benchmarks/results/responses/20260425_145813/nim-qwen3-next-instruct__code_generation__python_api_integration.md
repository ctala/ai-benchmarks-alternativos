# Qwen 3-Next 80B Instruct (NIM) — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.63 | quality: 9.52
- latency_total: 15.382s | tokens_per_second: 80.6
- input_tokens: 114 | output_tokens: 1240
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import logging

def get_expensive_products(bearer_token):
    """
    Obtiene productos de la API, filtra los con precio > 100 y retorna {id, name, price}.
    Maneja errores de red, timeout y retry con backoff exponencial.
    
    Args:
        bearer_token (str): Token de autenticación Bearer
        
    Returns:
        list: Lista de diccionarios con keys {id, name, price} para productos con precio > 100
        
    Raises:
        Exception: Si fallan todos los intentos de retry
    """
    url = "https://api.example.com/products"
    max_retries = 3
    base_delay = 1  # segundos
    
    # Configurar logging básico
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    for attempt in range(max_retries):
        try:
            # Realizar solicitud GET con timeout de 10 segundos y autenticación Bearer
            client = httpx.Client(timeout=10)
            headers = {
                "Authorization": f"Bearer {bearer_token}",
                "User-Agent": "Python-Product-Filter"
            }
            
            response = client.get(url, headers=headers)
            response.raise_for_status()  # Lanza excepción si el código de estado es 4xx/5xx
            
            # Parsear la respuesta JSON
            products_data = response.json()
            
            # Validar que la respuesta es una lista
            if not isinstance(products_data, list):
                raise ValueError("La respuesta de la API no es una lista de productos")
            
            # Filtrar productos con precio > 100 y extraer solo {id, name, price}
            filtered_products = []
            for product in products_data:
                # Verificar que el producto tiene los campos necesarios y price es numérico
                if (isinstance(product, dict) and 
                    'price' in product and 
                    isinstance(product['price'], (int, float)) and 
                    product['price'] > 100):
                    
                    # Extraer solo los campos requeridos
                    filtered_product = {
                        'id': product.get('id'),
                        'name': product.get('name'),
                        'price': product['price']
                    }
                    filtered_products.append(filtered_product)
            
            return filtered_products
            
        except httpx.RequestError as e:
            logger.warning(f"Intento {attempt + 1} fallido: Error de red o timeout - {str(e)}")
            
            if attempt == max_retries - 1:
                logger.error("Todos los intentos fallaron")
                raise Exception(f"Error de red después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
            
        except httpx.HTTPStatusError as e:
            logger.warning(f"Intento {attempt + 1} fallido: Error HTTP {e.response.status_code} - {str(e)}")
            
            if attempt == max_retries - 1:
                logger.error("Todos los intentos fallaron")
                raise Exception(f"Error HTTP después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
            
        except ValueError as e:
            logger.warning(f"Intento {attempt + 1} fallido: Error de formato de respuesta - {str(e)}")
            
            if attempt == max_retries - 1:
                logger.error("Todos los intentos fallaron")
                raise Exception(f"Error de formato de respuesta después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
            
        except Exception as e:
            logger.warning(f"Intento {attempt + 1} fallido: Error inesperado - {str(e)}")
            
            if attempt == max_retries - 1:
                logger.error("Todos los intentos fallaron")
                raise Exception(f"Error inesperado después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
    
    # Este punto nunca debería alcanzarse debido a los raises anteriores
    raise Exception("Error inesperado en el ciclo de retry")
```

Esta función:

1. Realiza una solicitud GET a la URL especificada con autenticación Bearer
2. Usa `httpx` con timeout de 10 segundos
3. Implementa retry con backoff exponencial (1, 2, 4 segundos) hasta 3 intentos
4. Filtra productos con precio > 100 y retorna solo los campos `{id, name, price}`
5. Maneja errores de red, timeout, errores HTTP y errores de formato
6. Usa solo `httpx` y módulos estándar de Python (`time`, `logging`)
7. Incluye logging para rastrear intentos y errores

Nota: `httpx` es una dependencia que debes instalar con `pip install httpx`, pero según tu requerimiento no se usan dependencias adicionales más allá de esta.