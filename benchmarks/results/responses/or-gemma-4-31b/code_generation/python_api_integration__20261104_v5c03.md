# Gemma 4 31B — code_generation/python_api_integration

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.61 | quality: 9.72
- latency_total: 29.665s | tokens_per_second: 29.2
- input_tokens: 117 | output_tokens: 866
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

Para implementar esta funcionalidad con `httpx`, la mejor práctica es utilizar un `Client` para gestionar la conexión y un bucle `for` con `time.sleep` para manejar el backoff exponencial.

Aquí tienes el código completo:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0
    
    # Usamos un cliente para optimizar el manejo de conexiones
    with httpx.Client() as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers, timeout=timeout)
                
                # Lanza excepción si el status code es 4xx o 5xx
                response.raise_for_status()
                
                # Si llegamos aquí, la petición fue exitosa
                products = response.json()
                
                # Filtrado y transformación:
                # Solo precio > 100 y solo campos id, name, price
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products 
                    if p.get("price", 0) > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as e:
                # Si es el último intento, lanzamos la excepción
                if attempt == max_retries - 1:
                    print(f"Error final después de {max_retries} intentos: {e}")
                    raise e
                
                # Backoff exponencial: 2^0 = 1s, 2^1 = 2s, etc.
                wait_time = 2 ** attempt
                print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time}s...")
                time.sleep(wait_time)

# Ejemplo de uso
if __name__ == "__main__":
    try:
        my_token = "tu_token_aqui"
        result = get_expensive_products(my_token)
        print(result)
    except Exception as e:
        print(f"La función falló: {e}")
```

### Explicación de los puntos clave:

1.  **Autenticación Bearer**: Se implementa pasando el token en el diccionario de `headers` como `Authorization: Bearer <token>`.
2.  **Filtrado y Proyección**: Utilizo una *list comprehension* que hace dos cosas a la vez: filtra los productos cuyo precio es mayor a 100 y crea un nuevo diccionario solo con las llaves requeridas (`id`, `name`, `price`).
3.  **Manejo de Errores y Timeout**: 
    *   `timeout=10.0` asegura que la petición no se quede colgada.
    *   `response.raise_for_status()` convierte errores HTTP (como 500 o 404) en excepciones capturables.
    *   Se capturan tanto `RequestError` (problemas de red/DNS) como `HTTPStatusError` (respuestas de error del servidor).
4.  **Retry con Backoff Exponencial**: 
    *   El bucle `for` controla el número de intentos.
    *   `time.sleep(2 ** attempt)` implementa el crecimiento exponencial del tiempo de espera entre reintentos.
5.  **Eficiencia**: El uso de `httpx.Client()` es más eficiente que llamar a `httpx.get()` repetidamente, ya que reutiliza el pool de conexiones.