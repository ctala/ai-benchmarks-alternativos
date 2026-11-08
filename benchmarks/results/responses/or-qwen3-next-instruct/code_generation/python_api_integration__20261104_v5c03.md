# Qwen 3-Next 80B Instruct — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.89 | quality: 9.52
- latency_total: 4.434s | tokens_per_second: 228.2
- input_tokens: 112 | output_tokens: 1012
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
import logging

def get_expensive_products(bearer_token):
    """
    Obtiene productos de la API, filtra los con precio > 100 y retorna {id, name, price}
    
    Args:
        bearer_token (str): Token de autenticación Bearer
        
    Returns:
        list: Lista de diccionarios con {id, name, price} para productos con precio > 100
        
    Raises:
        Exception: Si todos los intentos fallan
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }
    
    # Configurar logging básico
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Configuración de retry con backoff exponencial
    max_retries = 3
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        try:
            # Realizar la solicitud GET con timeout de 10 segundos
            response = httpx.get(url, headers=headers, timeout=10.0)
            
            # Verificar si la respuesta es exitosa
            response.raise_for_status()
            
            # Parsear la respuesta JSON
            products = response.json()
            
            # Filtrar productos con precio > 100 y extraer solo los campos necesarios
            filtered_products = [
                {"id": product["id"], "name": product["name"], "price": product["price"]}
                for product in products 
                if isinstance(product, dict) and 
                   "price" in product and 
                   product["price"] > 100 and
                   "id" in product and 
                   "name" in product
            ]
            
            return filtered_products
            
        except httpx.RequestError as e:
            logger.warning(f"Intento {attempt + 1} fallido: {str(e)}")
            
            # Si es el último intento, lanzar la excepción
            if attempt == max_retries - 1:
                raise Exception(f"Falló la solicitud después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
            
        except ValueError as e:
            # Error al parsear JSON
            logger.warning(f"Intento {attempt + 1} fallido: Error al parsear JSON - {str(e)}")
            
            if attempt == max_retries - 1:
                raise Exception(f"Falló la solicitud después de {max_retries} intentos: Error al parsear JSON")
            
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
            
        except Exception as e:
            # Otros errores inesperados
            logger.warning(f"Intento {attempt + 1} fallido: {str(e)}")
            
            if attempt == max_retries - 1:
                raise Exception(f"Falló la solicitud después de {max_retries} intentos: {str(e)}")
            
            delay = base_delay * (2 ** attempt)
            logger.info(f"Esperando {delay} segundos antes del próximo intento...")
            time.sleep(delay)
    
    # Este punto nunca debería alcanzarse debido a las excepciones anteriores
    raise Exception("Error inesperado en el proceso de retry")
```

Esta función:

1. Realiza una solicitud GET a la URL especificada con el token Bearer en el header
2. Usa `httpx` con timeout de 10 segundos como requerido
3. Implementa retry con backoff exponencial (1, 2, 4 segundos) hasta un máximo de 3 intentos
4. Maneja errores de red (`httpx.RequestError`), errores de JSON (`ValueError`) y otros errores generales
5. Filtra los productos para devolver solo aquellos con precio > 100 y con los campos `{id, name, price}`
6. Incluye logging para rastrear intentos fallidos y tiempos de espera
7. No usa dependencias externas adicionales a `httpx` (que es la única dependencia requerida)

Nota: `httpx` debe instalarse previamente con `pip install httpx`, pero según la instrucción, no se permiten dependencias adicionales, por lo que esta solución asume que `httpx` está disponible como la única dependencia externa permitida.