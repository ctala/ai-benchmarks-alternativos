# Gemma 4 31B — code_generation/python_api_integration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.91 | quality: 9.72
- latency_total: 16.657s | tokens_per_second: 51.9
- input_tokens: 117 | output_tokens: 865
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

Para implementar esta funcionalidad siguiendo todas tus especificaciones, utilizaremos `httpx` y el módulo `time` para gestionar el backoff exponencial.

Aquí tienes el código completo y documentado:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los mayores a 100 
    y retorna solo id, name y price.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout_seconds = 10.0
    
    # Usamos un cliente para optimizar conexiones (Connection Pooling)
    with httpx.Client(timeout=timeout_seconds) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # Filtrado y transformación de datos
                # Solo incluimos id, name, price si el precio es > 100
                return [
                    {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                    for p in products 
                    if p.get("price", 0) > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                # Si es el último intento, lanzamos la excepción
                if attempt == max_retries - 1:
                    print(f"Error final tras {max_retries} intentos: {e}")
                    raise e
                
                # Backoff exponencial: 2^attempt (1s, 2s, 4s...)
                wait_time = 2 ** attempt
                print(f"Error detectado: {e}. Reintentando en {wait_time}s...")
                time.sleep(wait_time)

# Ejemplo de uso:
if __name__ == "__main__":
    TOKEN = "tu_token_aqui"
    try:
        resultado = get_expensive_products(TOKEN)
        print(resultado)
    except Exception as e:
        print(f"La función falló: {e}")
```

### Explicación de los puntos clave:

1.  **Autenticación**: Se pasa el token en el header `Authorization` siguiendo el estándar `Bearer {token}`.
2.  **Filtrado y Transformación**: He utilizado una *list comprehension* que realiza ambas tareas en un solo paso: verifica que el precio sea mayor a 100 y construye un nuevo diccionario solo con las llaves requeridas (`id`, `name`, `price`).
3.  **Manejo de Errores y Timeout**: 
    *   `timeout=10.0` en el cliente asegura que la petición no quede colgada indefinidamente.
    *   `response.raise_for_status()` convierte códigos de error HTTP (como 500 o 404) en excepciones capturables.
4.  **Retry con Backoff Exponencial**: 
    *   El bucle `for attempt in range(max_retries)` controla los intentos.
    *   `time.sleep(2 ** attempt)` implementa el crecimiento exponencial del tiempo de espera entre reintentos.
5.  **Eficiencia**: El uso de `with httpx.Client()` es la práctica recomendada para evitar abrir y cerrar sockets TCP en cada llamada si se hicieran múltiples peticiones.