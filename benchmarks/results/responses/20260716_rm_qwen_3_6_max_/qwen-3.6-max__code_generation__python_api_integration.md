# Qwen 3.6 Max — code_generation/python_api_integration

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 81.881s | tokens_per_second: 48.9
- input_tokens: 113 | output_tokens: 4004
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una implementación limpia, robusta y que cumple exactamente con los 5 requisitos solicitados:

```python
import httpx
import time

def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100 y retorna
    solo id, name y price. Incluye retry con backoff exponencial y manejo de errores.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)  # 10 segundos para connect, read, write y pool
    max_retries = 3
    last_exc = None

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza error para 4xx/5xx
                products = response.json()

                if not isinstance(products, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtrado y proyección de campos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]

            except httpx.RequestError as e:
                # Captura timeouts, errores de conexión, DNS, SSL, etc.
                last_exc = e
                if attempt < max_retries - 1:
                    # Backoff exponencial: 1s, 2s, 4s
                    time.sleep(2 ** attempt)
                else:
                    raise RuntimeError(
                        f"Fallo tras {max_retries} intentos por error de red/timeout"
                    ) from e

            except httpx.HTTPStatusError as e:
                # Errores HTTP (4xx/5xx) no se reintentan según el enunciado
                raise RuntimeError(
                    f"Error HTTP {e.response.status_code}: {e.response.text}"
                ) from e
```

### 🔍 Puntos clave de la implementación:
1. **Autenticación Bearer**: Se inyecta en `headers` con el formato estándar `Authorization: Bearer <token>`.
2. **Timeout de 10s**: `httpx.Timeout(10.0)` aplica el límite a todas las fases de la petición (conexión, lectura, escritura, pool).
3. **Filtrado y proyección**: List comprehension que valida `price > 100` y extrae únicamente `id`, `name`, `price`. Usa `.get("price", 0)` para evitar `KeyError` si algún item no trae el campo.
4. **Manejo de errores**: 
   - `httpx.RequestError` agrupa timeouts, fallos de red, DNS, SSL, etc.
   - `httpx.HTTPStatusError` captura respuestas 4xx/5xx y falla rápido (sin retry, ya que son errores del servidor/cliente, no de red).
5. **Retry con backoff exponencial**: Bucle de 3 intentos con `time.sleep(2 ** attempt)` → esperas de `1s`, `2s`, `4s`. No requiere librerías externas como `tenacity`.

### 📦 Uso:
```python
try:
    expensive_items = fetch_expensive_products("tu_token_aqui")
    print(f"Productos encontrados: {len(expensive_items)}")
    print(expensive_items)
except RuntimeError as e:
    print(f"No se pudieron obtener los productos: {e}")
```

### ⚠️ Notas:
- Se asume que la API retorna un JSON con una **lista de objetos** en el cuerpo. Si la respuesta viene envuelta (ej. `{"data": [...]}`), solo ajusta `products = response.json()["data"]`.
- `httpx` y `time` son las únicas dependencias (`time` es parte de la stdlib de Python).
- Si necesitas jitter para evitar thundering herd en producción, puedes añadir `import random` y usar `time.sleep((2 ** attempt) + random.uniform(0, 1))`.