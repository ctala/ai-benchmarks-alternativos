# Tencent Hy4 preview — code_generation/python_api_integration

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.27 | quality: 9.72
- latency_total: 52.339s | tokens_per_second: 61.3
- input_tokens: 129 | output_tokens: 3209
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

Aquí tienes la función en Python que cumple con todos los requisitos utilizando únicamente `httpx` y la biblioteca estándar (`time` para el backoff):

```python
import httpx
import time

def obtener_productos_filtrados(bearer_token: str) -> list[dict]:
    """
    Realiza una petición GET a la API de productos, filtra aquellos con precio > 100
    y retorna una lista de diccionarios con las claves id, name y price.
    
    Incluye reintentos con backoff exponencial (máximo 3 intentos) y manejo de errores
    de red y timeouts.
    
    Args:
        bearer_token: Token de autenticación para el header Authorization.
        
    Returns:
        Lista de diccionarios con la información de los productos filtrados.
        
    Raises:
        httpx.HTTPError: Si después de todos los intentos la petición sigue fallando.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_intentos = 3
    timeout_segundos = 10.0
    
    for intento in range(max_intentos):
        try:
            # 1. Realizar la petición GET con autenticación y timeout
            response = httpx.get(url, headers=headers, timeout=timeout_segundos)
            response.raise_for_status()  # Lanza excepción si la respuesta es 4xx o 5xx
            
            # 2. Procesar la respuesta JSON
            productos = response.json()
            
            # 3. Filtrar productos con precio > 100 y mapear solo las claves requeridas
            productos_filtrados = [
                {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                for p in productos
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]
            
            return productos_filtrados
            
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            # 4. Manejo de errores de red, timeout y errores HTTP
            if intento == max_intentos - 1:
                # Si es el último intento, relanzamos la excepción
                raise e
            
            # 5. Retry con backoff exponencial (espera 1s, luego 2s)
            tiempo_espera = 2 ** intento
            time.sleep(tiempo_espera)
    
    return []  # Fallback por seguridad (inaccesible en la práctica)
```

### Explicación de los puntos clave:

1. **Autenticación Bearer**: Se incluye el token en el header `Authorization` con el formato `Bearer <token>`.
2. **Timeout**: Se pasa el parámetro `timeout=10.0` a `httpx.get()` para limitar el tiempo de espera a 10 segundos.
3. **Manejo de errores**: Se capturan `httpx.RequestError` (que cubre errores de red y timeouts) y `httpx.HTTPStatusError` (para respuestas HTTP fallidas como 500 o 404).
4. **Retry con backoff exponencial**: Se utiliza un bucle `for` con un máximo de 3 intentos. Si ocurre un error, se espera $2^n$ segundos (1s, 2s) antes del siguiente intento.
5. **Filtrado y mapeo**: Usando una list comprehension, se filtran los productos por precio y se construye un nuevo diccionario solo con las claves `id`, `name` y `price`.
6. **Sin dependencias externas adicionales**: Solo se importa `httpx` y `time` (biblioteca estándar de Python), cumpliendo con la restricción.

### Ejemplo de uso:

```python
try:
    productos = obtener_productos_filtrados("mi_token_secreto")
    print(productos)
except httpx.HTTPError as e:
    print(f"No se pudieron obtener los productos después de varios intentos: {e}")
```