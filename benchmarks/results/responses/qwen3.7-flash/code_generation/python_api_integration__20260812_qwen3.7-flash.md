# Qwen 3.7 Flash — code_generation/python_api_integration

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 8.95 | quality: 9.72
- latency_total: 31.836s | tokens_per_second: 129.3
- input_tokens: 113 | output_tokens: 4116
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

Aquí tienes la implementación completa, siguiendo buenas prácticas y cumpliendo exactamente con los requisitos:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100 y retorna
    una lista de diccionarios con solo {id, name, price}.
    Incluye reintento con backoff exponencial para errores de red/timeout.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    base_backoff = 1.0  # segundos

    for attempt in range(1, max_retries + 1):
        try:
            # timeout=10.0 aplica a conexión, lectura y escritura
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

            # Asegurar que trabajamos con una lista (algunas APIs envuelven en un objeto)
            products = data if isinstance(data, list) else data.get("products", [])

            # Filtrar y proyectar solo los campos requeridos
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            return filtered

        except httpx.RequestError as e:
            # httpx.RequestError cubre: ConnectError, ReadError, TimeoutException, NetworkError
            if attempt < max_retries:
                delay = base_backoff * (2 ** (attempt - 1))
                print(f"[Intento {attempt}] Error de red/timeout: {e}. Reintentando en {delay:.1f}s...")
                time.sleep(delay)
            else:
                raise RuntimeError(f"Falló después de {max_retries} intentos: {e}") from e

        except Exception as e:
            # Errores no recuperables (JSON mal formado, campos faltantes, etc.)
            raise RuntimeError(f"Error inesperado al procesar la respuesta: {e}") from e
```

### 🔍 Puntos clave de la implementación:
1. **Autenticación & Timeout**: Se usa `httpx.Client(timeout=10.0)` que configura automáticamente 10 segundos para conexión, lectura y escritura. El token se pasa en el header `Authorization`.
2. **Retry con Backoff Exponencial**: 
   - Intenta hasta 3 veces.
   - Espera `1s → 2s → 4s` entre fallos consecutivos.
   - Solo reintenta en `httpx.RequestError` (cubre red y timeout explícitamente).
3. **Filtrado Seguro**: 
   - Verifica que cada elemento sea un `dict`.
   - Usa `.get("price", 0)` para evitar `KeyError` si falta el campo.
   - Proyecta únicamente `{id, name, price}` como se solicitó.
4. **Ciclo de Vida del Cliente**: `with httpx.Client(...)` garantiza que las conexiones se cierren correctamente tras cada intento, evitando fugas de recursos.
5. **Dependencias**: Solo usa `httpx` (instalable con `pip install httpx`) y `time` del estándar.

### 📦 Ejemplo de uso:
```python
if __name__ == "__main__":
    MY_TOKEN = "tu_bearer_token_aqui"
    try:
        resultado = get_expensive_products(MY_TOKEN)
        print("Productos > $100:", resultado)
    except Exception as e:
        print("Operación fallida:", e)
```