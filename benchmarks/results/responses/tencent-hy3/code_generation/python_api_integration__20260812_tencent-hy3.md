# Tencent Hy3 — code_generation/python_api_integration

- model_id: `tencent/hy3`
- success: True  | final: 8.37 | quality: 9.72
- latency_total: 102.181s | tokens_per_second: 41.7
- input_tokens: 126 | output_tokens: 4258
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
    Obtiene productos desde la API, filtra los de precio > 100 y retorna
    una lista de diccionarios con {id, name, price}.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    
    max_retries = 3
    timeout = 10.0  # 4. Timeout de 10 segundos
    
    for attempt in range(max_retries):
        try:
            # 1. GET con autenticación Bearer y timeout
            response = httpx.get(url, headers=headers, timeout=timeout)
            
            # Lanza httpx.HTTPStatusError si la respuesta es 4xx o 5xx
            response.raise_for_status()
            
            # Parsear el JSON de la respuesta
            data = response.json()
            
            # Soporte flexible por si la API devuelve un dict con una lista adentro
            if isinstance(data, dict):
                products = data.get("products", data.get("data", []))
            else:
                products = data
            
            # 2 y 3. Filtrar (precio > 100) y mapear a {id, name, price}
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            return filtered
        
        # 4. Manejo de errores de red y timeout
        except (httpx.NetworkError, httpx.TimeoutException) as e:
            # 5. Retry con backoff exponencial (max 3 intentos)
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 1s, 2s, 4s...
                print(f"Intento {attempt + 1} fallido ({e}). Reintentando en {wait_time}s...")
                time.sleep(wait_time)
            else:
                # Si agotamos los reintentos, manejamos el error retornando lista vacía
                print(f"Error de red/timeout tras {max_retries} intentos: {e}")
                return []
        
        except httpx.HTTPStatusError as e:
            # Errores HTTP (como 401 token inválido) no se reintentan, se manejan directamente
            print(f"Error de respuesta HTTP (no reintentable): {e}")
            return []
    
    return []

# Ejemplo de uso:
# productos = get_expensive_products("mi_token_secreto")
# print(productos)
```

### Explicación de cómo cumple los requisitos:
1. **GET con Bearer token**: Se usa `httpx.get` con el header `Authorization: Bearer <token>`.
2. **Filtro de precio > 100**: Se usa una *list comprehension* que verifica `p.get("price", 0) > 100`.
3. **Retorno de campos específicos**: Solo se construyen dicts con las llaves `id`, `name` y `price`.
4. **Manejo de errores de red y timeout**: Se capturan `httpx.NetworkError` y `httpx.TimeoutException`, y se define `timeout=10.0` en la petición.
5. **Retry con backoff exponencial**: Un bucle `for` con máximo 3 iteraciones; si falla, espera `2 ** attempt` segundos (1s, luego 2s) antes de reintentar.
6. **Sin dependencias adicionales**: Solo usa `httpx` (permitido) y `time` (módulo estándar de Python).