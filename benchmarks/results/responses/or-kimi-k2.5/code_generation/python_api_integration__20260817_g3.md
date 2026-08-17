# Kimi K2.5 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.89 | quality: 9.52
- latency_total: 89.882s | tokens_per_second: 22.8
- input_tokens: 115 | output_tokens: 2048
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

El usuario solicita una función Python con requisitos específicos:

1. Hacer GET a https://api.example.com/products con autenticación Bearer token
2. Filtrar productos con precio > 100
3. Retornar lista de diccionarios con solo {id, name, price}
4. Manejar errores de red y timeout (10 segundos)
5. Incluir retry con backoff exponencial (máximo 3 intentos)

Requisitos técnicos:
- Usar httpx (biblioteca moderna similar a requests pero asíncrona/síncrona)
- Sin dependencias externas adicionales (asumiendo que httpx ya está instalado o es la única dependencia permitida)

Plan de implementación:

1. Importar httpx y time (para backoff)
2. Definir función que acepte token como parámetro
3. Implementar lógica de retry con backoff exponencial:
   - Máximo 3 intentos
   - Backoff exponencial: esperar 2^intento segundos (o similar)
4. Configurar timeout de 10 segundos
5. Headers con Authorization: Bearer {token}
6. Manejo de excepciones:
   - httpx.TimeoutException
   - httpx.NetworkError
   - httpx.HTTPStatusError (para errores 4xx/5xx)
7. Procesamiento de respuesta:
   - Parsear JSON
   - Filtrar productos donde price > 100
   - Mapear a formato {id, name, price}
8. Retornar lista o raise exception después de agotar reintentos

Estructura del código:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para 4xx/5xx
                data = response.json()
                
                # Filtrar y transformar
                result = [
                    {
                        "id": product.get("id"),
                        "name": product.get("name"), 
                        "price": product.get("price")
                    }
                    for product in data
                    if product.get("price", 0) > 100
                ]
                return result
                
        except httpx.TimeoutException:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)  # Backoff exponencial: 1, 2, 4 segundos
            
        except httpx.NetworkError:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
            
        except httpx.HTTPStatusError:
            # No reintentamos errores 4xx/5xx (opcional, podría reintentarse 5xx)
            raise
            
        except Exception:
            # Otros errores (JSON invalid, etc)
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

Consideraciones:
- El backoff exponencial suele ser 2^attempt, pero a veces se usa con jitter. Aquí mantendré simple: 2^attempt segundos (1s, 2s, 4s)
- Debo manejar tanto errores de red (NetworkError) como timeouts (TimeoutException)
- httpx puede lanzar ConnectError, ReadTimeout, etc. Mejor capturar httpx.RequestError como base
- Para errores HTTP (4xx, 5xx), podría decidir si reintentar o no. Normalmente 5xx sí se reintenta, 4xx no. Pero para simplificar, solo reintentaré errores de red/timeout, no errores HTTP 4xx/5xx (a menos sea 503/502 etc). Sin embargo, el prompt pide "manejar errores de red y timeout", así que me enfocaré en esos para el retry.

Refinamiento:
- Usar `httpx.Client` como context manager
- Timeout de 10 segundos en el cliente
- Capturar `httpx.RequestError` como base para errores de red
- Separar `httpx.TimeoutException` si se quiere tratamiento específico, aunque TimeoutException hereda de RequestError

Código final:

```python
import httpx
import time
from typing import List, Dict, Any

def fetch_filtered_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos filtrados con retry y backoff exponencial.
    
    Args:
        token: Bearer token para autenticación
        
    Returns:
        Lista de diccionarios con {id, name, price} para productos > 100
        
    Raises:
        httpx.RequestError: Después de agotar los reintentos por errores de red/timeout
        httpx.HTTPStatusError: Para errores HTTP 4xx/5xx (no se reintentan)
        ValueError: Si la respuesta no es JSON válido
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    max_retries = 3
    base_delay = 1  # Segundos base para backoff
    
    last_exception = None
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError para 4xx/5xx
                
                products = response.json()
                
                # Filtrar productos con precio > 100 y mapear a formato requerido
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
                
        except httpx.TimeoutException as e:
            last_exception = e
            if attempt < max_retries - 1:
                sleep_time = base_delay * (2 ** attempt)  # 1s, 2s, 4s
                time.sleep(sleep_time)
            else:
                break
                
        except httpx.NetworkError as e:
            last_exception = e
            if attempt < max_retries - 1:
                sleep_time = base_delay * (2 ** attempt)
                time.sleep(sleep_time)
            else:
                break
                
        except httpx.HTTPStatusError:
            # No reintentamos errores HTTP (4xx, 5xx)
            raise
            
        except (KeyError, TypeError) as e:
            # Error procesando el JSON (estructura incorrecta)
            raise ValueError(f"Invalid response format: {e}")
    
    # Si salimos del loop, agotamos los reintentos
    raise last_exception or Exception("Max retries exceeded")
```

Esta implementación cubre todos los requisitos:
1. GET con Bearer token ✓
2. Filtra price > 100 ✓
3. Retorna lista de dicts con id, name, price ✓
4. Timeout 10s y manejo de errores de red ✓
5. Retry con backoff exponencial (1s, 2s, 4s) máximo 3 intentos ✓
6. Usa httpx ✓

Podría mejorarse con async, pero el usuario no especificó async vs sync. Usaré sync para simplicidad, aunque httpx soporta ambos. Si el usuario quisiera async, podría usar `httpx.AsyncClient`, pero mantendré sync por defecto.

Una última consideración: el filtrado asume que `products` es una lista. Si la API retorna un dict con clave "products" o similar, necesitaría ajustar. Asumiré que retorna lista directa o que hay que acceder a una clave. Para ser robusto, podría manejar ambos casos, pero mantendré la asunción simple de que es una lista.

También debería manejar el caso donde `price` no existe (usando .get() con default 0 para que no falle el > 100).

Corrección en el list comprehension: usar .get() para evitar KeyError si falta algún campo.

Versión final:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()
