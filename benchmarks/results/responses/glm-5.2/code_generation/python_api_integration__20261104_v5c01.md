# GLM 5.2 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.26 | quality: 9.48
- latency_total: 17.12s | tokens_per_second: 94.5
- input_tokens: 113 | output_tokens: 1618
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

Aquí tienes la función en Python que cumple con todos tus requisitos usando `httpx` y la biblioteca estándar `time` para el backoff:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra los que tienen precio > 100 y retorna
    una lista de diccionarios con {id, name, price}.
    
    Incluye manejo de errores, timeout de 10s y reintento con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }
    
    max_attempts = 3
    
    for attempt in range(max_attempts):
        try:
            # Realizamos la petición GET con un timeout de 10 segundos
            response = httpx.get(url, headers=headers, timeout=10.0)
            
            # Lanza una excepción si el código de estado HTTP es un error (4xx o 5xx)
            response.raise_for_status()
            
            # Parseamos la respuesta JSON
            products = response.json()
            
            # Filtramos productos con precio > 100 y mapeamos al formato requerido
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            
            return filtered_products
            
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si es el último intento, relanzamos la excepción
            if attempt == max_attempts - 1:
                print(f"Error final tras {max_attempts} intentos: {exc}")
                raise
            
            # Calculamos el tiempo de espera (backoff exponencial: 1s, 2s, 4s...)
            wait_time = 2 ** attempt
            print(f"Intento {attempt + 1} fallido. Reintentando en {wait_time} segundos... Error: {exc}")
            time.sleep(wait_time)

# Ejemplo de uso (descomenta para probar):
# if __name__ == "__main__":
#     token = "tu_token_aqui"
#     try:
#         productos = get_expensive_products(token)
#         print(productos)
#     except Exception as e:
#         print(f"No se pudo completar la solicitud: {e}")
```

### Detalles de la implementación:
1. **Autenticación Bearer**: Se añade la cabecera `Authorization: Bearer <token>` a la petición.
2. **Timeout**: Se configura explícitamente `timeout=10.0` en `httpx.get`.
3. **Filtrado y mapeo**: Se usa una *list comprehension* para iterar sobre el JSON, asegurarse de que el diccionario tenga la clave `price` (usando `.get` para evitar `KeyError`), filtrar los mayores a 100 y extraer exactamente `id`, `name` y `price`.
4. **Manejo de errores**: Captura `httpx.RequestError` (que cubre problemas de red, timeouts, fallos de conexión) y `httpx.HTTPStatusError` (errores HTTP 4xx/5xx).
5. **Backoff exponencial**: El bucle `for` corre hasta 3 veces. Si falla, espera `2 ** attempt` segundos (1s en el intento 0, 2s en el intento 1). En el tercer intento (índice 2), si falla, relanza la excepción original para que el llamador la maneje.