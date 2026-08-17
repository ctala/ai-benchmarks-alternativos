# Qwen 3-Next 80B Instruct — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.72 | quality: 9.28
- latency_total: 4.763s | tokens_per_second: 219.8
- input_tokens: 112 | output_tokens: 1047
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import logging

def get_expensive_products(bearer_token):
    """
    Obtiene productos de la API, filtra los con precio > 100 y retorna solo id, name, price.
    Maneja errores de red, timeout y reintentos con backoff exponencial.
    
    Args:
        bearer_token (str): Token de autenticación Bearer
        
    Returns:
        list: Lista de diccionarios con keys {id, name, price} para productos con precio > 100
        
    Raises:
        Exception: Si después de 3 intentos falla la solicitud
    """
    url = "https://api.example.com/products"
    max_retries = 3
    base_delay = 1  # segundos
    
    for attempt in range(max_retries):
        try:
            # Configurar client con timeout de 10 segundos
            client = httpx.Client(timeout=10.0)
            
            # Hacer la solicitud GET con autenticación Bearer
            headers = {
                "Authorization": f"Bearer {bearer_token}",
                "User-Agent": "Python-Product-Filter"
            }
            
            response = client.get(url, headers=headers)
            response.raise_for_status()  # Lanza excepción para códigos de error HTTP
            
            # Parsear la respuesta JSON
            products = response.json()
            
            # Verificar que la respuesta es una lista
            if not isinstance(products, list):
                raise ValueError("La respuesta de la API no es una lista de productos")
            
            # Filtrar productos con precio > 100 y seleccionar solo id, name, price
            filtered_products = [
                {"id": product["id"], "name": product["name"], "price": product["price"]}
                for product in products 
                if isinstance(product, dict) 
                and "id" in product 
                and "name" in product 
                and "price" in product 
                and isinstance(product["price"], (int, float)) 
                and product["price"] > 100
            ]
            
            return filtered_products
            
        except (httpx.RequestError, httpx.TimeoutException) as e:
            # Error de red o timeout
            if attempt == max_retries - 1:
                raise Exception(f"Error después de {max_retries} intentos: {str(e)}")
            
            # Calcular delay con backoff exponencial
            delay = base_delay * (2 ** attempt)
            logging.warning(f"Intento {attempt + 1} falló: {str(e)}. Reintentando en {delay} segundos...")
            time.sleep(delay)
            
        except ValueError as e:
            # Error en el formato de la respuesta
            if attempt == max_retries - 1:
                raise Exception(f"Error en el formato de la respuesta después de {max_retries} intentos: {str(e)}")
            
            delay = base_delay * (2 ** attempt)
            logging.warning(f"Respuesta inválida en intento {attempt + 1}: {str(e)}. Reintentando en {delay} segundos...")
            time.sleep(delay)
            
        except Exception as e:
            # Otros errores inesperados
            if attempt == max_retries - 1:
                raise Exception(f"Error inesperado después de {max_retries} intentos: {str(e)}")
            
            delay = base_delay * (2 ** attempt)
            logging.warning(f"Error inesperado en intento {attempt + 1}: {str(e)}. Reintentando en {delay} segundos...")
            time.sleep(delay)
            
        finally:
            # Asegurar que el cliente se cierre
            try:
                client.close()
            except:
                pass
    
    # Este punto nunca debería alcanzarse debido a las excepciones anteriores
    raise Exception("Error inesperado en el flujo de reintentos")
```

Esta función:

1. Hace una solicitud GET a la URL con autenticación Bearer usando `httpx`
2. Filtra los productos para mantener solo aquellos con precio > 100
3. Retorna una lista de diccionarios con solo las claves `id`, `name`, `price`
4. Maneja errores de red y timeout con un timeout de 10 segundos
5. Implementa reintentos con backoff exponencial (1s, 2s, 4s) hasta un máximo de 3 intentos
6. Usa solo `httpx` y las bibliotecas estándar de Python (time, logging)
7. Incluye validaciones de tipo y estructura de datos para mayor robustez
8. Cierra correctamente el cliente HTTP en todos los casos

Nota: Se incluye `logging` para informar sobre reintentos, pero no es una dependencia externa ya que forma parte de la biblioteca estándar de Python.