# Qwen 3.5 397B — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.13 | quality: 9.72
- latency_total: 78.202s | tokens_per_second: 61.6
- input_tokens: 113 | output_tokens: 4814
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
from typing import List, Dict, Any

def get_filtered_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y maneja retries.
    
    Args:
        token (str): Bearer token para autenticación.
        
    Returns:
        List[Dict]: Lista de diccionarios con {id, name, price}.
        
    Raises:
        ConnectionError: Si fallan todos los intentos por errores de red/timeout.
        httpx.HTTPStatusError: Si la API retorna un error HTTP crítico (ej. 4xx, 5xx persistente).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout_seconds = 10.0
    max_retries = 3
    base_backoff = 1.0  # Segundos iniciales para el backoff

    for attempt in range(max_retries):
        try:
            # Usamos httpx.Client como contexto para asegurar cierre de conexiones
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout_seconds)
                
                # raise_for_status lanza HTTPStatusError para códigos 4xx o 5xx
                response.raise_for_status()
                
                data = response.json()
                
                # Normalizar datos (manejar si viene como lista o dentro de una clave)
                if isinstance(data, dict) and 'products' in data:
                    products = data['products']
                elif isinstance(data, list):
                    products = data
                else:
                    products = []

                result = []
                for product in products:
                    price = product.get('price', 0)
                    # Filtro: precio > 100
                    if price > 100:
                        result.append({
                            'id': product.get('id'),
                            'name': product.get('name'),
                            'price': price
                        })
                
                return result

        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError) as e:
            # Errores de transporte, red o timeout
            if attempt == max_retries - 1:
                raise ConnectionError(f"Falló tras {max_retries} intentos por error de red: {e}") from e
            
            # Backoff exponencial: 1s, 2s, 4s...
            wait_time = base_backoff * (2 ** attempt)
            time.sleep(wait_time)

        except httpx.HTTPStatusError as e:
            # Errores de estado HTTP (4xx, 5xx)
            status_code = e.response.status_code
            
            # Solo reintentamos en errores del servidor (5xx)
            if 500 <= status_code < 600:
                if attempt == max_retries - 1:
                    raise
                wait_time = base_backoff * (2 ** attempt)
                time.sleep(wait_time)
            else:
                # Errores del cliente (4xx) no se reintentan (ej. 401 Unauthorized)
                raise

# Ejemplo de uso (requiere pip install httpx)
if __name__ == "__main__":
    try:
        # token_ejemplo = "tu_token_aqui"
        # productos = get_filtered_products(token_ejemplo)
        # print(productos)
        pass
    except Exception as e:
        print(f"Error: {e}")
```

### Características principales de la implementación:

1.  **Librería `httpx`**: Se utiliza exclusivamente para las peticiones HTTP (síncrono).
2.  **Autenticación**: Se envía el token en el header `Authorization: Bearer`.
3.  **Filtrado**: Se procesa el JSON y se retorna solo si `price > 100`, limitando las claves a `id`, `name`, `price`.
4.  **Timeout**: Configurado a 10 segundos en `client.get`.
5.  **Manejo de Errores**:
    *   Captura excepciones de red y timeout (`TimeoutException`, `ConnectError`, etc.).
    *   Distingue entre errores de servidor (5xx, reintentables) y cliente (4xx, no reintentables).
6.  **Retry con Backoff Exponencial**:
    *   Máximo 3 intentos.
    *   Espera: $1 \times 2^{intentos\_fallidos}$ segundos (1s, 2s...).
    *   No espera después del último fallo, lanza la excepción inmediatamente.