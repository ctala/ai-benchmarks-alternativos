# Claude Haiku 5.5 — code_generation/python_api_integration

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.32 | quality: 9.08
- latency_total: 10.691s | tokens_per_second: 248.2
- input_tokens: 156 | output_tokens: 2654
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

API_URL = "https://api.example.com/products"
TIMEOUT_SEGUNDOS = 10.0
MAX_INTENTOS = 3
BACKOFF_BASE = 1.0  # espera inicial en segundos: 1s, 2s, 4s...
CODIGOS_REINTENTABLES = {429, 500, 502, 503, 504}


class ProductsAPIError(Exception):
    """Error al obtener productos de la API."""


def _get_con_reintentos(client: httpx.Client, url: str, headers: dict) -> list:
    """Hace GET con reintentos y backoff exponencial. Devuelve el JSON parseado."""
    ultimo_error: Exception | None = None

    for intento in range(1, MAX_INTENTOS + 1):
        try:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

        except httpx.TimeoutException as e:
            ultimo_error = e  # timeout: reintentable

        except httpx.TransportError as e:
            ultimo_error = e  # error de red (DNS, conexión rechazada, etc.): reintentable

        except httpx.HTTPStatusError as e:
            if e.response.status_code not in CODIGOS_REINTENTABLES:
                # 4xx como 401/403/404 no se reintentan
                raise ProductsAPIError(
                    f"Error HTTP {e.response.status_code}: {e.response.text[:200]}"
                ) from e
            ultimo_error = e  # 429 o 5xx: reintentable

        except ValueError as e:
            # Respuesta no es JSON válido (json.JSONDecodeError hereda de ValueError)
            raise ProductsAPIError("La respuesta de la API no es JSON válido") from e

        if intento < MAX_INTENTOS:
            espera = BACKOFF_BASE * (2 ** (intento - 1))
            time.sleep(espera)

    raise ProductsAPIError(
        f"No se pudo obtener los productos tras {MAX_INTENTOS} intentos"
    ) from ultimo_error


def obtener_productos_caros(token: str, precio_minimo: float = 100.0) -> list[dict]:
    """
    Obtiene productos de la API y devuelve solo los de precio > precio_minimo,
    con los campos id, name y price.

    Raises:
        ProductsAPIError: si falla la petición tras los reintentos o la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(timeout=TIMEOUT_SEGUNDOS) as client:
        productos = _get_con_reintentos(client, API_URL, headers)

    if not isinstance(productos, list):
        raise ProductsAPIError("Se esperaba una lista de productos en la respuesta")

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in productos
        if isinstance(p, dict) and p.get("price") is not None and p["price"] > precio_minimo
    ]


if __name__ == "__main__":
    try:
        resultado = obtener_productos_caros(token="TU_TOKEN_AQUI")
        for producto in resultado:
            print(producto)
    except ProductsAPIError as e:
        print(f"Error: {e}")
```

**Notas:**

- **Timeout:** 10 segundos en el cliente de `httpx`, aplicado a cada intento.
- **Reintentos:** hasta 3 intentos en timeouts, errores de red, 429 y 5xx, con esperas de 1s y 2s entre intentos. Los errores 4xx (como 401 o 404) no se reintentan, porque repetir la petición no los va a corregir.
- **Filtro:** se aplica con `price > precio_minimo` (100 por defecto). Si un producto no tiene precio, se descarta.
- **Supuesto:** la función asume que la API devuelve directamente una lista JSON de productos con las claves `id`, `name` y `price`. Si la respuesta viene envuelta (por ejemplo, `{"data": [...]}`), hay que ajustar la línea donde se asigna `productos`.