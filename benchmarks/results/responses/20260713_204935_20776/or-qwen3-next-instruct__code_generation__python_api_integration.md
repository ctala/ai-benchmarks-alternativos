# Qwen 3-Next 80B Instruct — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.51 | quality: 9.52
- latency_total: 11.706s | tokens_per_second: 88.6
- input_tokens: 112 | output_tokens: 1037
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import logging

def get_expensive_products(token):
    """
    Obtiene productos de la API, filtra los con precio > 100 y retorna {id, name, price}.
    
    Args:
        token (str): Token de autenticación Bearer
        
    Returns:
        list: Lista de diccionarios con keys {id, name, price} para productos con precio > 100
        
    Raises:
        Exception: Si fallan todos los intentos de retry
    """
    url = "https://api.example.com/products"
    max_retries = 3
    base_delay = 1  # segundos
    
    # Configurar logging opcional (opcional, pero útil para depuración)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    for attempt in range(max_retries):
        try:
            # Realizar la solicitud GET con autenticación Bearer y timeout de 10 segundos
            response = httpx.get(
                url,
                headers={
                    "Authorization": f"Bearer {token}"
                },
                timeout=10.0
            )
            
            # Verificar si la respuesta es exitosa
            response.raise_for_status()
            
            # Parsear la respuesta JSON
            products = response.json()
            
            # Filtrar productos con precio > 100 y seleccionar solo los campos requeridos
            filtered_products = [
                {"id": product["id"], "name": product["name"], "price": product["price"]}
                for product in products
                if isinstance(product, dict) and "price" in product and product["price"] > 100
            ]
            
            return filtered_products
            
        except httpx.TimeoutException:
            logger.warning(f"Intento {attempt + 1}: Timeout al conectar con la API")
            if attempt == max_retries - 1:
                raise Exception("Fallo en todos los intentos: Timeout persistente")
                
        except httpx.RequestError as e:
            logger.warning(f"Intento {attempt + 1}: Error de red - {str(e)}")
            if attempt == max_retries - 1:
                raise Exception(f"Fallo en todos los intentos: Error de red - {str(e)}")
                
        except httpx.HTTPStatusError as e:
            logger.warning(f"Intento {attempt + 1}: Error HTTP - {e.response.status_code} {e.response.reason_phrase}")
            if attempt == max_retries - 1:
                raise Exception(f"Fallo en todos los intentos: Error HTTP - {e.response.status_code}")
                
        except ValueError as e:  # Error al parsear JSON
            logger.warning(f"Intento {attempt + 1}: Error al parsear JSON - {str(e)}")
            if attempt == max_retries - 1:
                raise Exception(f"Fallo en todos los intentos: Error al parsear JSON - {str(e)}")
                
        except KeyError as e:  # Si algún producto no tiene los campos esperados
            logger.warning(f"Intento {attempt + 1}: Estructura de datos inesperada - {str(e)}")
            if attempt == max_retries - 1:
                raise Exception(f"Fallo en todos los intentos: Estructura de datos inesperada - {str(e)}")
        
        # Aplicar backoff exponencial antes del siguiente intento
        if attempt < max_retries - 1:
            delay = base_delay * (2 ** attempt)  # 1, 2, 4 segundos
            logger.info(f"Esperando {delay} segundos antes del siguiente intento...")
            time.sleep(delay)
    
    # Este punto nunca debería alcanzarse debido a las raises anteriores
    raise Exception("Error inesperado: todos los intentos fallaron")
```

Esta función:

1. Realiza una solicitud GET a la URL especificada con el token Bearer en el encabezado
2. Usa un timeout de 10 segundos como requerido
3. Implementa retry con backoff exponencial (1, 2, 4 segundos entre intentos) hasta un máximo de 3 intentos
4. Maneja errores de red, timeout, errores HTTP, y errores de parsing JSON
5. Filtra los productos para retornar solo aquellos con precio > 100
6. Retorna una lista de diccionarios con solo las claves `id`, `name` y `price`
7. Usa únicamente `httpx` como dependencia externa (la única requerida, como se pidió)
8. Incluye logging para rastrear intentos y errores (útil para depuración)

La función lanza una excepción si todos los intentos fallan, lo que permite al llamador manejar el error según sea necesario.