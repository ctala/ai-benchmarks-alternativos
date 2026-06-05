# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/python_api_integration

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 8.19 | quality: 9.48
- latency_total: 34.865s | tokens_per_second: 25.6
- input_tokens: 117 | output_tokens: 892
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver este problema, utilizaremos la librería `httpx` junto con una lógica de manejo de errores manual para el **backoff exponencial**, ya que solicitaste no usar dependencias externas adicionales (como `tenacity`).

Aquí tienes la solución:

```python
import httpx
import time
import logging

# Configuración básica de logging para ver los reintentos
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_expensive_products(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    max_retries = 3
    base_delay = 1  # Segundos iniciales para el backoff

    with httpx.Client(timeout=10.0) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                products_data = response.json()
                
                # Filtrado y mapeo de datos
                # Asumimos que la API devuelve una lista de objetos
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products_data
                    if p.get("price", 0) > 100
                ]
                
                return filtered_products

            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                # Si es el último intento, lanzamos la excepción
                if attempt == max_retries - 1:
                    logger.error(f"Fallo final tras {max_retries} intentos: {e}")
                    raise
                
                # Cálculo de backoff exponencial: 1s, 2s, 4s...
                delay = base_delay * (2 ** attempt)
                logger.warning(f"Error en intento {attempt + 1}: {e}. Reintentando en {delay}s...")
                time.sleep(delay)

    return []

# Ejemplo de uso:
if __name__ == "__main__":
    try:
        token_ejemplo = "tu_token_aqui"
        resultado = get_expensive_products(token_ejemplo)
        print(resultado)
    except Exception as err:
        print(f"Error final: {err}")
```

### Explicación de la implementación:

1.  **`httpx.Client(timeout=10.0)`**: Se utiliza el cliente de `httpx` para gestionar la conexión. El parámetro `timeout` asegura que la petición no se quede colgada más de 10 segundos.
2.  **Autenticación Bearer**: Se incluye en el diccionario de headers como `Authorization: Bearer <token>`.
3.  **Manejo de Errores**: 
    *   `httpx.RequestError`: Captura problemas de red (DNS, conexión perdida, etc.).
    *   `response.raise_for_status()`: Captura errores de HTTP (como 404, 500, 401) y los convierte en excepciones.
4.  **Backoff Exponencial**:
    *   Se usa un bucle `for` para los intentos.
    *   La fórmula `base_delay * (2 ** attempt)` genera esperas progresivas (ej. 1s, 2s, 4s).
    *   `time.sleep(delay)` pausa la ejecución antes del siguiente intento.
5.  **List Comprehension**: Se utiliza para filtrar los productos con precio > 100 y proyectar únicamente los campos `id`, `name` y `price` en una sola línea limpia.