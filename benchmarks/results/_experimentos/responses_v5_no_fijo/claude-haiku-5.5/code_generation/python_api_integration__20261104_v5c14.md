# Claude Haiku 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.3 | quality: 9.08
- latency_total: 11.52s | tokens_per_second: 254.4
- input_tokens: 156 | output_tokens: 2931
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

```python
import time

import httpx

URL = "https://api.example.com/products"
TIMEOUT_SEGUNDOS = 10.0
MAX_INTENTOS = 3
BACKOFF_BASE = 1.0  # espera: 1s, 2s, 4s...
UMBRAL_PRECIO = 100


class ProductsAPIError(Exception):
    """Error al obtener productos de la API."""


def obtener_productos_caros(token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 usando un Bearer token.

    Retorna una lista de dicts con las claves: id, name, price.
    Reintenta con backoff exponencial (máximo 3 intentos) ante
    errores de red, timeouts, 429 y 5xx.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    ultimo_error = None
    data = None

    with httpx.Client(timeout=TIMEOUT_SEGUNDOS) as client:
        for intento in range(MAX_INTENTOS):
            try:
                response = client.get(URL, headers=headers)
            except httpx.TransportError as e:
                # Incluye TimeoutException, ConnectError, ReadError, etc.
                ultimo_error = f"{type(e).__name__}: {e}"
            else:
                status = response.status_code
                if status == 429 or status >= 500:
                    # Errores temporales: se reintenta
                    ultimo_error = f"HTTP {status}"
                elif status >= 400:
                    # Errores del cliente (401, 403, 404...): no tiene sentido reintentar
                    raise ProductsAPIError(f"HTTP {status}: {response.text[:200]}")
                else:
                    try:
                        data = response.json()
                    except ValueError as e:
                        raise ProductsAPIError("La respuesta no es JSON válido") from e
                    break

            # Backoff exponencial antes del siguiente intento
            if intento < MAX_INTENTOS - 1:
                time.sleep(BACKOFF_BASE * (2 ** intento))
        else:
            raise ProductsAPIError(
                f"Fallaron {MAX_INTENTOS} intentos. Último error: {ultimo_error}"
            )

    if not isinstance(data, list):
        raise ProductsAPIError("Se esperaba una lista de productos en la respuesta")

    resultado = []
    for producto in data:
        try:
            precio = float(producto.get("price"))
        except (TypeError, ValueError):
            continue  # ignora productos sin precio válido

        if precio > UMBRAL_PRECIO:
            resultado.append({
                "id": producto.get("id"),
                "name": producto.get("name"),
                "price": precio,
            })

    return resultado


if __name__ == "__main__":
    try:
        productos = obtener_productos_caros("MI_TOKEN")
        for p in productos:
            print(p)
    except ProductsAPIError as e:
        print(f"Error: {e}")
```

**Notas:**

- **Timeout:** `httpx.Client(timeout=10.0)` aplica 10 segundos a cada intento.
- **Errores de red:** `httpx.TransportError` es la clase base de `TimeoutException`, `ConnectError`, `ReadError`, etc., así que se capturan todos con un solo `except`.
- **Reintentos:** se reintenta solo ante errores temporales (red, timeout, 429, 5xx). Los 4xx como 401 o 403 se lanzan de inmediato, porque reintentarlos no cambia el resultado.
- **Backoff:** las esperas son 1s y 2s entre los 3 intentos. Si quieres evitar que varios clientes reintenten sincronizados, puedes añadir jitter con `random.uniform`.
- **Supuesto:** la API devuelve una lista JSON directamente. Si la respuesta viene envuelta (por ejemplo `{"data": [...]}`), ajusta la línea donde se asigna `data`.