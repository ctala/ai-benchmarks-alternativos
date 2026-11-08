# Qwen 3.6 Plus — code_generation/python_api_integration

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 90.075s | tokens_per_second: 58.2
- input_tokens: 113 | output_tokens: 5241
- judge_score: 5.0 | justificación: 

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

Aquí tienes una implementación completa, limpia y lista para producción. Cumple con todos los requisitos usando únicamente `httpx` y la librería estándar de Python.

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.
    Incluye autenticación Bearer, timeout de 10s, manejo de errores 
    y reintentos con backoff exponencial (máx 3 intentos).
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_delay = 1.0  # Segundos

    for attempt in range(max_retries):
        try:
            # timeout=10.0 aplica a conexión, lectura y escritura
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza HTTPStatusError si status >= 400
                
                products = response.json()

                # 2. Filtrar y 3. Retornar solo {id, name, price}
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]

        # 4. Manejo de errores de red y timeout
        except httpx.RequestError as e:
            # httpx.RequestError cubre TimeoutException, ConnectError, etc.
            pass  
            
        except httpx.HTTPStatusError as e:
            # Reintentar solo en errores de servidor (5xx)
            if e.response.status_code < 500:
                e.response.raise_for_status()  # 4xx -> fallo inmediato
            pass

        # 5. Backoff exponencial antes del siguiente intento
        if attempt < max_retries - 1:
            delay = base_delay * (2 ** attempt)  # 1s, 2s, 4s
            time.sleep(delay)

    raise RuntimeError("No se pudo obtener los productos después de 3 intentos.")
```

### 🔍 Puntos clave de la implementación:
1. **Autenticación**: Se pasa el header `Authorization: Bearer <token>` en cada intento.
2. **Filtrado & Proyección**: List comprehension que filtra `price > 100` y extrae únicamente las claves solicitadas. `p.get("price", 0)` evita `KeyError` si algún producto viene sin precio.
3. **Timeout**: `httpx.Client(timeout=10.0)` configura un límite estricto de 10 segundos para toda la operación de red.
4. **Manejo de errores**: 
   - `httpx.RequestError` es la clase base que engloba timeouts y fallos de red.
   - `httpx.HTTPStatusError` se maneja diferenciando `4xx` (error del cliente, no se reintenta) de `5xx` (error del servidor, se reintenta).
5. **Retry con Backoff**: Implementado manualmente sin dependencias externas. Usa `time.sleep()` con delays de `1s → 2s → 4s`. Si tras 3 intentos falla, lanza una excepción clara.

### 📦 Instalación requerida:
```bash
pip install httpx
```

### 💡 Uso:
```python
try:
    result = get_expensive_products("tu_token_aqui")
    print(f"Productos encontrados: {len(result)}")
except RuntimeError as e:
    print(f"Error crítico: {e}")
```