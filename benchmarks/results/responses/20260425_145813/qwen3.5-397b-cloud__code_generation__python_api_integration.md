# Qwen 3.5 397B (Ollama Cloud) — code_generation/python_api_integration

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 8.05 | quality: 9.72
- latency_total: 104.475s | tokens_per_second: 42.5
- input_tokens: 113 | output_tokens: 4441
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str, url: str = "https://api.example.com/products") -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra por precio > 100 y retorna id, name, price.
    Incluye retry con backoff exponencial y manejo de errores de red/timeout.
    """
    max_retries = 3
    timeout_seconds = 10.0
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    last_exception = None

    for attempt in range(max_retries):
        try:
            # Usamos Client como context manager para gestionar conexiones
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout_seconds)
                
                # Lanza HTTPStatusError para códigos 4xx o 5xx
                response.raise_for_status()
                
                data = response.json()
                
                # Asumimos que la API retorna una lista de productos directamente.
                # Si envuelve los datos (ej: {"products": [...]}), ajustar el acceso aquí.
                if not isinstance(data, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtrado y transformación
                filtered_products = [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"]
                    }
                    for product in data
                    if product.get("price", 0) > 100
                ]
                
                return filtered_products

        except (httpx.RequestError, httpx.TimeoutException) as e:
            # Errores de red o timeout son reintentables
            last_exception = e
            print(f"Intento {attempt + 1} fallido (Red/Timeout): {e}")
            
        except httpx.HTTPStatusError as e:
            # Solo reintentamos si es error 5xx (Servidor). 4xx (Cliente) no se reintentan.
            if 500 <= e.response.status_code < 600:
                last_exception = e
                print(f"Intento {attempt + 1} fallido (Error Servidor {e.response.status_code}): {e}")
            else:
                # Error 4xx (ej: 401 Unauthorized), no reintentar
                raise e
        
        # Lógica de Backoff Exponencial si no es el último intento
        if attempt < max_retries - 1:
            wait_time = 2 ** attempt  # 1s, 2s, 4s...
            time.sleep(wait_time)
        else:
            # Se agotaron los intentos
            break

    # Si salimos del loop sin retornar, lanzamos el último error capturado
    raise RuntimeError(f"Falló después de {max_retries} intentos") from last_exception
```

### Puntos clave de la implementación:

1.  **Librería `httpx`**: Se usa el cliente síncrono (`httpx.Client`) para mantener el código simple y compatible.
2.  **Timeout**: Configurado explícitamente en `10.0` segundos en la petición.
3.  **Retry con Backoff**:
    *   Bucle `for` de 3 intentos.
    *   Si falla, espera `2 ** attempt` segundos (1s, luego 2s).
    *   Solo reintentamos errores de red (`RequestError`) o errores de servidor (`5xx`). Los errores de cliente (`4xx`, como token inválido) se lanzan inmediatamente.
4.  **Filtrado**: Se usa list comprehension para filtrar `price > 100` y construir el diccionario limpio `{id, name, price}`.
5.  **Gestión de Errores**: Si los 3 intentos fallan, se lanza un `RuntimeError` con la excepción original adjunta (`from last_exception`) para facilitar el debug.

### Instalación necesaria:
Solo necesitas instalar `httpx`:
```bash
pip install httpx
```