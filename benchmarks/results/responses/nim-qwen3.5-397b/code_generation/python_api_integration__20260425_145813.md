# Qwen 3.5 397B (NIM) — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.42 | quality: 9.48
- latency_total: 59.276s | tokens_per_second: 19.7
- input_tokens: 113 | output_tokens: 1168
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una implementación completa que cumple con todos los requisitos utilizando la librería `httpx`.

La función incluye:
1.  **Autenticación Bearer**: Usando los headers adecuados.
2.  **Filtrado**: Selecciona productos con precio mayor a 100.
3.  **Proyección de datos**: Devuelve solo las claves `id`, `name` y `price`.
4.  **Manejo de errores**: Captura excepciones de red y timeouts de `httpx`.
5.  **Reintentos con Backoff Exponencial**: Implementa una lógica de reintento (max 3 intentos) esperando $2^{\text{intento}}$ segundos entre cada fallo.

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str, base_url: str = "https://api.example.com") -> List[Dict[str, Any]]:
    """
    Obtiene productos, filtra por precio > 100 y retorna una lista limitada de campos.
    Incluye reintentos con backoff exponencial y manejo de errores de red.
    """
    url = f"{base_url}/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    products_data = []

    for attempt in range(max_retries):
        try:
            # Usamos httpx.Client para una solicitud síncrona eficiente
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                
                # Levantar excepción para códigos de estado HTTP no exitosos (4xx, 5xx)
                response.raise_for_status()
                
                data = response.json()
                
                # Asumimos que la API devuelve una lista en la raíz o en una clave 'results'/'data'
                # Ajustar según la estructura real de la API. Aquí asumimos lista directa.
                if isinstance(data, list):
                    items = data
                elif isinstance(data, dict) and 'products' in data:
                    items = data['products']
                elif isinstance(data, dict) and 'data' in data:
                    items = data['data']
                else:
                    items = []

                # 2. Filtrar productos con precio > 100
                # 3. Retornar solo {id, name, price}
                filtered_products = [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": p.get("price")
                    }
                    for p in items
                    if isinstance(p.get("price"), (int, float)) and p.get("price") > 100
                ]
                
                return filtered_products

        except (httpx.RequestError, httpx.TimeoutException) as e:
            print(f"Intento {attempt + 1} fallido debido a error de red/timeout: {e}")
            
            if attempt == max_retries - 1:
                # Último intento fallido
                raise RuntimeError(f"No se pudo conectar después de {max_retries} intentos.") from e
            
            # 5. Backoff exponencial: esperar 2^attempt segundos (1s, 2s, 4s...)
            wait_time = 2 ** attempt
            print(f"Reintentando en {wait_time} segundos...")
            time.sleep(wait_time)
            
        except httpx.HTTPStatusError as e:
            # Errores HTTP (4xx, 5xx) que no son de red pura, pero indican fallo de la petición
            if e.response.status_code >= 500 and attempt < max_retries - 1:
                # Si es error 5xx, podemos intentar de nuevo
                wait_time = 2 ** attempt
                print(f"Error del servidor ({e.response.status_code}). Reintentando en {wait_time} segundos...")
                time.sleep(wait_time)
                continue
            
            # Para errores 4xx o si ya no hay reintentos, lanzamos el error
            raise RuntimeError(f"Error HTTP {e.response.status_code}: {e}") from e

    return []
```

### Puntos clave de la implementación:

*   **Dependencias**: Solo usa `httpx`, `time` y `typing` (estándar).
*   **Timeout**: Se configura explícitamente en `httpx.Client(timeout=10.0)`.
*   **Lógica de Reintento**:
    *   El bucle `for attempt in range(max_retries)` controla los 3 intentos.
    *   Si ocurre un `RequestError` o `TimeoutException`, calcula el tiempo de espera como $2^{\text{attempt}}$ (1s, 2s, 4s) antes de volver a intentar.
    *   También maneja errores 500 del servidor como candidatos a reintento.
*   **Filtrado y Limpieza**: Usa una *list comprehension* para filtrar por precio y construir el diccionario reducido `{id, name, price}` de forma eficiente.
*   **Robustez**: Verifica que el precio sea numérico antes de compararlo para evitar errores de tipo si la API devuelve datos inconsistentes.