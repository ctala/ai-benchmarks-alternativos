# GLM 5.2 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.85 | quality: 9.48
- latency_total: 80.911s | tokens_per_second: 25.9
- input_tokens: 113 | output_tokens: 2099
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la función en Python que cumple con todos los requisitos utilizando `httpx` y la librería estándar de Python:

```python
import httpx
import time
import logging

# Configuración básica de logging para ver los intentos de reintento
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def get_filtered_products(bearer_token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los de precio > 100 y maneja reintentos.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    timeout = 10.0
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            # Usamos un contexto para asegurar el cierre de la conexión
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                
                # Lanza una excepción si el código de estado HTTP es un error (4xx, 5xx)
                response.raise_for_status()
                
                products = response.json()
                
                # Filtramos por precio > 100 y formateamos la salida
                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]
                
                return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as e:
            logger.warning(f"Intento {attempt}/{max_attempts} fallido. Error: {e}")
            
            # Si ya alcanzamos el máximo de intentos, relanzamos la excepción
            if attempt == max_attempts:
                logger.error("Se alcanzó el número máximo de reintentos. Operación abortada.")
                raise
            
            # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s
            wait_time = 2 ** (attempt - 1)
            logger.info(f"Esperando {wait_time} segundos antes de reintentar...")
            time.sleep(wait_time)

    return []  # Return por defecto en caso de que el flujo salga del bucle (aunque no debería)

# Ejemplo de uso:
# try:
#     token = "tu_token_aqui"
#     resultado = get_filtered_products(token)
#     print(resultado)
# except Exception as e:
#     print(f"Error final: {e}")
```

### Detalles de la implementación:
1. **Dependencias**: Solo usa `httpx`, `time` y `logging` (ambos built-in en Python).
2. **Cliente HTTP**: Se utiliza `httpx.Client` de forma síncrona con un bloque `with` para asegurar la correcta gestión de los recursos y la liberación de conexiones.
3. **Timeout**: Configurado a 10 segundos estrictos mediante el parámetro `timeout=10.0`.
4. **Filtrado y Formato**: Se utiliza una *list comprehension* que extrae exactamente las llaves solicitadas y filtra los productos con `price > 100`.
5. **Manejo de errores**: Captura específicamente `httpx.TimeoutException` (para los timeouts), `httpx.NetworkError` (para fallos de conexión/DNS) y `httpx.HTTPStatusError` (por si el servidor responde con un error 500/429).
6. **Backoff exponencial**: Usa la fórmula `2 ** (attempt - 1)` lo que da tiempos de espera de 1, 2 y 4 segundos entre los intentos 1-2 y 2-3. Al llegar al máximo de intentos (3), relanza la excepción para que la maneje la aplicación principal, evitando ocultar el fallo de forma silenciosa.