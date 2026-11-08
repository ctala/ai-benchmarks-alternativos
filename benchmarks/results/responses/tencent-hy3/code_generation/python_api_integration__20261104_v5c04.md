# Tencent Hy3 — code_generation/python_api_integration

- model_id: `tencent/hy3`
- success: True  | final: 8.55 | quality: 9.72
- latency_total: 47.217s | tokens_per_second: 77.3
- input_tokens: 126 | output_tokens: 3649
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

Aquí tienes una implementación en Python que cumple con todos los requisitos utilizando únicamente `httpx` (y el módulo estándar `time` para el backoff):

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde la API, filtra los de precio > 100 y 
    retorna una lista de diccionarios con {id, name, price}.
    
    Args:
        token: Token de autenticación Bearer.
    
    Returns:
        Lista de productos filtrados y formateados.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0  # 10 segundos
    
    for attempt in range(max_retries):
        try:
            # 1. GET con autenticación Bearer y timeout de 10s
            response = httpx.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Lanza error en respuestas 4xx/5xx
            
            # Parsear JSON (asumiendo que la API devuelve una lista o un dict con 'products')
            data = response.json()
            products = data if isinstance(data, list) else data.get("products", [])
            
            # 2 y 3. Filtrar precio > 100 y mapear a {id, name, price}
            filtered_products = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            
            return filtered_products
        
        except httpx.RequestError as e:
            # 4. Manejo de errores de red y timeout (httpx.RequestError incluye TimeoutException)
            print(f"Intento {attempt + 1} fallido por error de red/timeout: {e}")
            
            if attempt < max_retries - 1:
                # 5. Retry con backoff exponencial (1s, 2s antes del siguiente intento)
                wait_time = 2 ** attempt
                print(f"Reintentando en {wait_time} segundo(s)...")
                time.sleep(wait_time)
            else:
                print("Se agotaron los 3 intentos. No se pudieron obtener los productos.")
                return []  # Retorna lista vacía si fallan todos los intentos
    
    return []

# Ejemplo de uso:
# products = get_expensive_products("mi_token_secreto")
# print(products)
```

### Explicación de los puntos clave:
1. **GET con Bearer token**: Se envía el header `Authorization: Bearer <token>` usando el parámetro `headers` de `httpx.get`.
2. **Filtro de precio**: Se usa una *list comprehension* para quedarse solo con los productos donde `price > 100`.
3. **Formato de salida**: Solo se construyen dicts con las llaves `id`, `name` y `price`.
4. **Errores de red y timeout**: `httpx.RequestError` captura tanto fallos de conexión como timeouts (ya que `TimeoutException` hereda de esta). El `timeout=10.0` garantiza que la petición no se cuelgue más de 10 segundos.
5. **Retry con backoff exponencial**: El bucle `for` permite hasta 3 intentos. Si hay un error, espera `2 ** attempt` segundos (1s, luego 2s) antes de reintentar.
6. **Sin dependencias extra**: Solo se usa `httpx` y `time` (módulo estándar de Python).