# Gemini 2.5 Pro — code_generation/python_api_integration

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 8.05 | quality: 9.72
- latency_total: 47.374s | tokens_per_second: 111.3
- input_tokens: 104 | output_tokens: 5271
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes una función en Python que cumple con todos los requisitos, utilizando la librería `httpx` y módulos de la librería estándar de Python.

El código está completamente documentado para explicar cada parte del proceso.

```python
import httpx
import time
from typing import List, Dict, Any, Union

# --- Constantes de configuración ---
API_URL = "https://api.example.com/products"
MAX_RETRIES = 3         # Número máximo de reintentos
BASE_BACKOFF_SECONDS = 1  # Tiempo de espera base para el backoff (1 segundo)
REQUEST_TIMEOUT = 10      # Timeout para la petición en segundos

def fetch_and_filter_products(api_token: str) -> List[Dict[str, Union[str, int, float]]]:
    """
    Obtiene productos de una API, los filtra y formatea.

    Esta función realiza una petición GET a la API de productos con autenticación
    Bearer token. Implementa una lógica de reintentos con backoff exponencial
    para manejar errores de red y timeouts. Finalmente, filtra los productos
    cuyo precio es mayor a 100 y devuelve una lista simplificada de ellos.

    Args:
        api_token: El token de autenticación (Bearer token) para la API.

    Returns:
        Una lista de diccionarios, donde cada diccionario contiene 'id', 'name' y 'price'
        de los productos con precio > 100.
        Retorna una lista vacía si ocurre un error irrecuperable o si no se
        encuentran productos que cumplan el criterio.
    """
    headers = {"Authorization": f"Bearer {api_token}"}
    
    last_exception = None

    # 5. Bucle para reintentos con backoff exponencial
    for attempt in range(MAX_RETRIES):
        try:
            # 1. Hacer la petición GET con autenticación y timeout
            with httpx.Client() as client:
                response = client.get(
                    API_URL, 
                    headers=headers, 
                    timeout=REQUEST_TIMEOUT
                )
                
                # Levantar una excepción para códigos de error HTTP (4xx o 5xx)
                response.raise_for_status()

                # Si la petición es exitosa, procesamos los datos
                all_products = response.json()
                
                # 2. Filtrar productos con precio > 100
                # 3. Retornar una lista de dicts con solo {id, name, price}
                filtered_products = [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": p.get("price")
                    }
                    for p in all_products
                    # Aseguramos que 'price' exista, sea un número y sea > 100
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]
                
                print("Productos obtenidos y filtrados exitosamente.")
                return filtered_products

        # 4. Manejar errores de red y timeout
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            last_exception = e
            print(f"Intento {attempt + 1}/{MAX_RETRIES} fallido: Error de red o timeout ({e}).")
            if attempt < MAX_RETRIES - 1:
                # Calcular el tiempo de espera (backoff exponencial)
                wait_time = BASE_BACKOFF_SECONDS * (2 ** attempt)
                print(f"Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
            else:
                print("Se alcanzó el número máximo de reintentos.")
        
        # Manejar otros errores HTTP (ej: 401 Unauthorized, 404 Not Found)
        except httpx.HTTPStatusError as e:
            print(f"Error HTTP en la petición: {e.response.status_code} {e.response.reason_phrase}")
            print(f"Respuesta del servidor: {e.response.text}")
            # No reintentamos en estos casos, son errores de cliente o servidor
            return []
            
        # Manejar errores inesperados (ej: JSON mal formado)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            return []

    # Si el bucle termina sin éxito, es porque todos los reintentos fallaron
    if last_exception:
        print(f"Error final después de {MAX_RETRIES} intentos: {last_exception}")
        
    return []

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Para este ejemplo, no podemos llamar a la API real.
    # Usaremos `unittest.mock` (de la librería estándar) para simular las respuestas de la API.
    from unittest.mock import patch, MagicMock

    # Caso 1: Petición exitosa a la primera
    print("--- Caso 1: Petición exitosa ---")
    mock_response_success = MagicMock()
    mock_response_success.status_code = 200
    mock_response_success.json.return_value = [
        {"id": 1, "name": "Laptop Básica", "price": 80, "stock": 10},
        {"id": 2, "name": "Monitor 4K", "price": 450, "stock": 5},
        {"id": 3, "name": "Teclado Mecánico", "price": 120, "stock": 20},
        {"id": 4, "name": "Producto sin precio", "name": "Mouse Inalámbrico"},
    ]
    # raise_for_status() no hace nada si el status code es < 400
    mock_response_success.raise_for_status.return_value = None

    with patch('httpx.Client.get', return_value=mock_response_success):
        products = fetch_and_filter_products(api_token="fake-token-123")
        print("Productos filtrados:", products)
        # Salida esperada: [{'id': 2, 'name': 'Monitor 4K', 'price': 450}, {'id': 3, 'name': 'Teclado Mecánico', 'price': 120}]
        assert len(products) == 2
        assert products[0]['price'] == 450

    print("\n" + "="*40 + "\n")

    # Caso 2: Falla por timeout una vez, luego tiene éxito
    print("--- Caso 2: Falla por Timeout y luego éxito ---")
    mock_response_failure = httpx.TimeoutException("El servidor no respondió a tiempo.")
    
    with patch('httpx.Client.get', side_effect=[mock_response_failure, mock_response_success]) as mock_get:
        products = fetch_and_filter_products(api_token="fake-token-123")
        print("Productos filtrados:", products)
        # Verificamos que se llamó a la API 2 veces
        assert mock_get.call_count == 2
        assert len(products) == 2

    print("\n" + "="*40 + "\n")

    # Caso 3: Falla todos los reintentos por error de red
    print("--- Caso 3: Falla todos los reintentos ---")
    mock_response_network_error = httpx.NetworkError("No se pudo conectar al servidor.")
    
    with patch('httpx.Client.get', side_effect=mock_response_network_error) as mock_get:
        products = fetch_and_filter_products(api_token="fake-token-123")
        print("Productos filtrados:", products)
        # Verificamos que se llamó a la API 3 veces (MAX_RETRIES)
        assert mock_get.call_count == MAX_RETRIES
        assert products == []

    print("\n" + "="*40 + "\n")

    # Caso 4: Falla por un error de autenticación (401 Unauthorized)
    print("--- Caso 4: Error de autenticación (401) ---")
    mock_response_auth_error = MagicMock()
    mock_response_auth_error.status_code = 401
    mock_response_auth_error.reason_phrase = "Unauthorized"
    mock_response_auth_error.text = '{"detail": "Token inválido o expirado"}'
    mock_response_auth_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "401 Unauthorized", 
        request=MagicMock(), 
        response=mock_response_auth_error
    )
    
    with patch('httpx.Client.get', return_value=mock_response_auth_error) as mock_get:
        products = fetch_and_filter_products(api_token="token-invalido")
        print("Productos filtrados:", products)
        # Verificamos que se llamó a la API solo 1 vez (no hay reintentos para errores 4xx)
        assert mock_get.call_count == 1
        assert products == []
```

### Desglose de la Solución:

1.  **Petición GET con Autenticación**:
    -   Se crea un diccionario `headers` con la clave `Authorization` y el valor `Bearer {api_token}`.
    -   Se utiliza `httpx.Client().get(url, headers=headers, ...)` para realizar la petición. El uso de `with httpx.Client() as client:` es la práctica recomendada para gestionar la conexión adecuadamente.

2.  **Filtrado de Productos**:
    -   Tras obtener una respuesta exitosa y decodificar el JSON, se usa una *list comprehension* para iterar sobre la lista de productos.
    -   La condición `if isinstance(p.get("price"), (int, float)) and p["price"] > 100` es robusta:
        -   `p.get("price")` evita un `KeyError` si un producto no tiene la clave "price".
        -   `isinstance(...)` se asegura de que el precio sea un número antes de compararlo, evitando un `TypeError`.
        -   `p["price"] > 100` realiza el filtrado numérico.

3.  **Formato de Salida**:
    -   Dentro de la misma *list comprehension*, se crea un nuevo diccionario `{ "id": p.get("id"), "name": p.get("name"), "price": p.get("price") }` para cada producto que pasa el filtro, asegurando que solo se incluyan los campos solicitados.

4.  **Manejo de Errores de Red y Timeout**:
    -   La petición se envuelve en un bloque `try...except`.
    -   Se captura la tupla `(httpx.TimeoutException, httpx.NetworkError)`. Estas son las excepciones que `httpx` lanza para timeouts y problemas de conectividad (DNS, conexión rechazada, etc.).
    -   El argumento `timeout=REQUEST_TIMEOUT` en la llamada a `get` le indica a `httpx` que lance una `TimeoutException` si la petición tarda más de 10 segundos.

5.  **Retry con Backoff Exponencial**:
    -   Un bucle `for attempt in range(MAX_RETRIES)` controla el número de intentos.
    -   Si se captura un error de red o timeout, se verifica si aún quedan intentos (`attempt < MAX_RETRIES - 1`).
    -   Si es así, se calcula el tiempo de espera con la fórmula `BASE_BACKOFF_SECONDS * (2 ** attempt)`. Esto resulta en esperas de 1, 2, 4, ... segundos.
    -   Se usa `time.sleep()` para pausar la ejecución antes del siguiente intento.
    -   Si se agotan los reintentos, se imprime un mensaje final y la función retorna una lista vacía.