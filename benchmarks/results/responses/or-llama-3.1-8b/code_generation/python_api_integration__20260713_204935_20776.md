# Llama 3.1 8B Instant — code_generation/python_api_integration

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 7.0 | quality: 6.36
- latency_total: 2.964s | tokens_per_second: 129.9
- input_tokens: 112 | output_tokens: 385
- judge_score: 3.0 | justificación: 

## Respuesta completa

Aquí te muestro un ejemplo de cómo podrías implementar la función utilizando `httpx` y `backoff`:

```python
import httpx
from backoff import on_exception, expo

def obtener_productos_con_precio_superior_a_100():
    # Configuración de la autenticación
    token = "TU_TOKEN_AQUI"
    headers = {"Authorization": f"Bearer {token}"}

    # Configuración de la petición
    url = "https://api.example.com/products"
    params = {"price": "gt:100"}

    @on_exception(backoff.expo, httpx.RequestError, max_tries=3)
    async def obtener_productos():
        async with httpx.AsyncClient() as client:
            # Configuración del timeout
            timeout = httpx.Timeout(10.0)
            try:
                response = await client.get(url, headers=headers, params=params, timeout=timeout)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                raise

    productos = obtener_productos()
    # Procesar productos
    productos = [{d["id"], d["name"], d["price"]} for d in productos]

    return productos
```
Ten en cuenta que debes reemplazar `TU_TOKEN_AQUI` con tu token de autenticación real. 

Recuerda que `httpx` es asincrónico, así que la función `obtener_productos_con_precio_superior_a_100` devuelve una `async` corutina. 

También ten en cuenta que el significado de `backoff.expo` es que si una petición falla, esperaré 2^1 segundos, 2^2 segundos, 2^3 segundos, etc., como máximo 10 segundos.