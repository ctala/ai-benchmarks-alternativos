# Gemini 3.1 Pro — code_generation/python_api_integration

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 7.99 | quality: 9.72
- latency_total: 31.461s | tokens_per_second: 87.2
- input_tokens: 104 | output_tokens: 2743
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

Aquí tienes la implementación de la función cumpliendo con todos tus requisitos. 

Utilizo la librería estándar `time` para el backoff exponencial y capturo `httpx.HTTPError`, que es la clase base en `httpx` para todos los errores (incluyendo timeouts, errores de conexión y respuestas HTTP fallidas).

```python
import time
import httpx
from typing import List, Dict, Any

def obtener_productos_caros(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    max_intentos = 3
    timeout_segundos = 10.0

    for intento in range(max_intentos):
        try:
            # 1 y 4. Petición GET con autenticación y timeout de 10 segundos
            response = httpx.get(url, headers=headers, timeout=timeout_segundos)
            
            # Lanzar excepción si el status code es 4xx o 5xx
            response.raise_for_status()
            
            # Suponemos que la API devuelve una lista de diccionarios en formato JSON
            productos = response.json()
            
            # 2 y 3. Filtrar precio > 100 y extraer solo id, name y price
            productos_filtrados = [
                {
                    "id": producto["id"],
                    "name": producto["name"],
                    "price": producto["price"]
                }
                for producto in productos
                if producto.get("price", 0) > 100
            ]
            
            return productos_filtrados

        except httpx.HTTPError as e:
            # 4. Manejo de errores de red, timeout o HTTP
            if intento == max_intentos - 1:
                # Si es el último intento, lanzamos el error
                raise RuntimeError(f"Fallo al obtener productos tras {max_intentos} intentos. Error final: {e}") from e
            
            # 5. Retry con backoff exponencial (2^0 = 1s, 2^1 = 2s, 2^2 = 4s...)
            tiempo_espera = 2 ** intento
            print(f"Error detectado: {e}. Reintentando en {tiempo_espera} segundos... (Intento {intento + 1}/{max_intentos})")
            time.sleep(tiempo_espera)

# Ejemplo de uso:
# token_jwt = "tu_token_aqui"
# resultado = obtener_productos_caros(token_jwt)
# print(resultado)
```

### Detalles de la implementación:
1. **Petición y Autenticación:** Se envían los headers con `Authorization: Bearer <token>`.
2. **Timeout:** Se pasa `timeout=10.0` a `httpx.get`. En `httpx`, esto cubre tanto el tiempo de conexión como el tiempo de lectura.
3. **Manejo de Errores (`httpx.HTTPError`):** Esta excepción base captura `httpx.TimeoutException`, `httpx.RequestError` (problemas de red/DNS) y `httpx.HTTPStatusError` (generado por el `response.raise_for_status()` si la API devuelve un 500, por ejemplo).
4. **Backoff Exponencial:** Usando `2 ** intento`, el sistema esperará 1 segundo tras el primer fallo, 2 segundos tras el segundo y luego fallará definitivamente en el tercero (máximo 3 intentos).
5. **Filtrado y Mapeo:** Se utiliza una *list comprehension* (comprensión de listas) que es la forma más eficiente y "pitónica" de iterar, filtrar por el precio y construir el nuevo diccionario estructurado simultáneamente. Se usa `.get("price", 0)` por seguridad en caso de que algún producto venga sin la clave precio.