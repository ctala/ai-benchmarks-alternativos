# Qwen 3.6 35B base (OpenRouter FP8) — code_generation/python_api_integration

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 67.288s | tokens_per_second: 72.2
- input_tokens: 113 | output_tokens: 4857
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



Aquí tienes la implementación completa siguiendo todos los requisitos. Se usa `httpx` exclusivamente, con manejo explícito de timeouts, errores de red y retry con backoff exponencial.

```python
import httpx
import time

def fetch_products_over_100(bearer_token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra los de precio > 100 y retorna 
    una lista de dicts con {id, name, price}.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_retries = 3
    timeout = 10.0

    # Reutilizamos la misma sesión para evitar overhead de reconexión
    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                # Normaliza respuesta: soporta lista directa o objeto con clave estándar
                if isinstance(data, dict):
                    data = data.get("products") or data.get("data") or []

                # Filtrado y proyección a la estructura solicitada
                return [
                    {"id": item.get("id"), "name": item.get("name"), "price": item.get("price")}
                    for item in data
                    if isinstance(item, dict) and item.get("price", 0) > 100
                ]

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                # Si es el último intento, re-lanza el error
                if attempt == max_retries - 1:
                    raise RuntimeError(f"Fallo tras {max_retries} intentos: {exc}") from exc
                
                # Backoff exponencial: 2^0=1s, 2^1=2s, 2^2=4s
                time.sleep(2 ** attempt)

            except httpx.HTTPStatusError as exc:
                # Errores HTTP (4xx, 5xx) no suelen solucionarse con retry
                exc.response.raise_for_status()
```

### 🔍 Puntos clave de la implementación:
1. **Timeout global**: `httpx.Client(timeout=10.0)` configura `connect`, `read`, `write` y `pool` a 10 segundos.
2. **Retry con backoff exponencial**: Loop de 3 intentos. Si falla, espera `2^attempt` segundos (1s, 2s, 4s).
3. **Manejo de errores**: 
   - `httpx.TimeoutException` y `httpx.NetworkError` → reintentan con backoff.
   - `httpx.HTTPStatusError` → se propaga inmediatamente (4xx/5xx no se reintentan por conveniencia).
4. **Filtrado y proyección**: Comprensión de listas que filtra `price > 100` y extrae solo los 3 campos solicitados, con `.get()` seguro para evitar `KeyError`.
5. **Flexibilidad de respuesta**: Soporta tanto `[{...}]` como `{"products": [...]}` o `{"data": [...]}`.

### 📦 Instalación necesaria:
```bash
pip install httpx
```

### 💡 Uso de ejemplo:
```python
token = "tu_bearer_token_aqui"
try:
    result = fetch_products_over_100(token)
    print(result)
except RuntimeError as e:
    print(f"Error crítico: {e}")
```