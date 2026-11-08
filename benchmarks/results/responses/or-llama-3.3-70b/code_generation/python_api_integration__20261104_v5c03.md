# Llama 3.3 70B — code_generation/python_api_integration

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 8.91 | quality: 9.52
- latency_total: 6.944s | tokens_per_second: 94.0
- input_tokens: 111 | output_tokens: 653
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

Aquí te dejo una función en Python que realiza lo que solicitas utilizando la biblioteca `httpx`:

```python
import httpx
import time
import random

def obtener_productos(token: str) -> list:
    """
    Obtiene productos de https://api.example.com/products con autenticación Bearer token,
    filtra productos con precio > 100 y retorna una lista de dicts con solo {id, name, price}.
    
    Maneja errores de red y timeout (10 segundos) con retry y backoff exponencial (max 3 intentos).
    """
    
    # Configuración de la solicitud
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10  # Segundos
    
    # Parámetros para el retry
    max_intentos = 3
    delay_inicial = 1  # Segundo
    max_delay = 30  # Segundos
    
    # Lista para almacenar los productos filtrados
    productos_filtrados = []
    
    # Intentos de solicitud
    for intento in range(max_intentos):
        try:
            # Realiza la solicitud GET
            respuesta = httpx.get(url, headers=headers, timeout=timeout)
            respuesta.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
            
            # Procesa la respuesta
            productos = respuesta.json()
            productos_filtrados = [{"id": p["id"], "name": p["name"], "price": p["price"]} for p in productos if p["price"] > 100]
            
            # Si la solicitud fue exitosa, rompe el ciclo
            break
        
        except httpx.HTTPError as e:
            # Maneja errores de red y timeout
            if intento < max_intentos - 1:
                # Calcula el delay para el próximo intento
                delay = min(delay_inicial * 2 ** intento, max_delay)
                delay_con_jitter = delay * (1 + random.random() * 0.1)  # Agrega un poco de jitter para evitar el problema del "thundering herd"
                print(f"Error de red o timeout (intento {intento + 1}/{max_intentos}). Retrying en {delay_con_jitter:.2f} segundos...")
                time.sleep(delay_con_jitter)
            else:
                # Si se agotaron los intentos, re-raise la excepción
                raise e
    
    return productos_filtrados

# Ejemplo de uso
token = "tu_token_de_autenticacion"
productos = obtener_productos(token)
print(productos)
```

Esta función realiza una solicitud GET a la URL especificada con autenticación Bearer token y maneja errores de red y timeout con retry y backoff exponencial. Si la solicitud es exitosa, filtra los productos con precio > 100 y retorna una lista de dicts con solo `{id, name, price}`. Si se agotan los intentos, re-raise la excepción original.