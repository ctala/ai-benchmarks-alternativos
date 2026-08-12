# DeepSeek V4 Flash 0731 — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.76 | quality: 9.36
- latency_total: 18.782s | tokens_per_second: 110.6
- input_tokens: 189 | output_tokens: 2078
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, abordando todos los requisitos con un manejo adecuado de errores y reintentos.

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

Aquí tienes la función Python solicitada. Usa `httpx`, incluye autenticación Bearer, filtrado y reintentos con retroceso exponencial:

```python
import httpx
import time

def fetch_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100
    y devuelve solo {id, name, price}.

    Incluye reintentos con retroceso exponencial (máx. 3 intentos)
    y timeout de 10 segundos.

    Args:
        token: Token Bearer para autenticación.

    Returns:
        Lista de diccionarios con id, name y price.

    Raises:
        httpx.RequestError: Si falla la conexión después de los reintentos.
        httpx.HTTPStatusError: Si la API responde con un código de error HTTP.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3
    backoff_factor = 1.0

    with httpx.Client(headers=headers, timeout=timeout) as client:
        for attempt in range(1, max_attempts + 1):
            try:
                response = client.get(url)
                response.raise_for_status()
                products = response.json()

                # Filtrar productos con precio > 100 y quedarse con los campos deseados
                filtered = [
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                    for item in products
                    if item.get("price", 0) > 100
                ]
                return filtered

            except httpx.RequestError as exc:
                # Si es el último intento, propagamos el error
                if attempt == max_attempts:
                    raise
                # Espera exponencial: 1s, 2s (antes del segundo y tercer intento)
                sleep_time = backoff_factor * (2 ** (attempt - 1))
                time.sleep(sleep_time)
```

La función maneja errores de red y timeouts mediante `httpx.RequestError`, reintentando con pausas de 1 y 2 segundos antes de los reintentos. Si aun así falla, se lanza la última excepción. Los errores HTTP (4xx, 5xx) no se reintentan y se propagan por `raise_for_status()`.