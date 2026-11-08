# GLM 5.3 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.56 | quality: 9.08
- latency_total: 148.306s | tokens_per_second: 102.3
- input_tokens: 113 | output_tokens: 15175
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

Aquí tienes la implementación completa:

```python
import logging
import time

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT = 10.0         # segundos
MAX_INTENTOS = 3       # intento inicial + 2 reintentos
BACKOFF_INICIAL = 1.0  # espera entre reintentos: 1s, 2s

STATUS_REINTENTABLES = {429, 500, 502, 503, 504}


def _debe_reintentar(exc: Exception) -> bool:
    """True si el error es transitorio: red, timeout, 429 o 5xx."""
    if isinstance(exc, (httpx.TimeoutException, httpx.NetworkError)):
        return True
    return (
        isinstance(exc, httpx.HTTPStatusError)
        and exc.response.status_code in STATUS_REINTENTABLES
    )


def obtener_productos_caros(token: str) -> list[dict]:
    """
    Obtiene los productos de la API y devuelve solo los de precio > 100.

    Reintenta con backoff exponencial ante errores transitorios
    (máximo 3 intentos en total).

    Returns:
        Lista de dicts con las claves "id", "name" y "price".

    Raises:
        httpx.HTTPError: si se agotan los reintentos o el error no es
            transitorio (p. ej. 401, 404).
        ValueError: si la respuesta no es JSON válido o no es una lista.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=TIMEOUT, headers=headers) as client:
        for intento in range(1, MAX_INTENTOS + 1):
            try:
                respuesta = client.get(API_URL)
                respuesta.raise_for_status()
                productos = respuesta.json()
                break  # éxito: salir del bucle de reintentos
            except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as exc:
                if intento == MAX_INTENTOS or not _debe_reintentar(exc):
                    raise
                espera = BACKOFF_INICIAL * 2 ** (intento - 1)
                logger.warning(
                    "Intento %d/%d falló (%s). Reintentando en %.1fs…",
                    intento, MAX_INTENTOS, exc, espera,
                )
                time.sleep(espera)

    if not isinstance(productos, list):
        raise ValueError(
            f"Se esperaba una lista de productos, llegó {type(productos).__name__}"
        )

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in productos
        if (p.get("price") or 0) > 100  # None o ausente → se descarta
    ]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    try:
        productos = obtener_productos_caros(token="TU_TOKEN")
        print(f"\n{len(productos)} productos con precio > 100:")
        for p in productos:
            print(f"  [{p['id']}] {p['name']} — ${p['price']}")
    except httpx.HTTPError as exc:
        print(f"\nError definitivo tras {MAX_INTENTOS} intentos: {exc}")
    except ValueError as exc:
        print(f"\nRespuesta inválida: {exc}")
```

**Notas de diseño:**

- **`raise` en vez de `return []`**: así no confundes "no hay productos > 100" con "la API está caída". Quien llama decide cómo manejar el fallo.
- **Backoff**: espera 1s tras el primer fallo y 2s tras el segundo (el tercer intento es el último). En producción conviene añadir *jitter*: `time.sleep(espera + random.uniform(0, 0.5))` para evitar reintentos sincronizados.
- **Qué se reintenta**: timeouts, fallos de DNS/conexión (`NetworkError`) y HTTP 429/5xx. Los 4xx no se reintentan porque no son transitorios. Si quieres cubrir todo error de transporte, sustituye la tupla del `except` por `httpx.TransportError` (la clase padre).
- **Cliente reutilizado**: el `httpx.Client` vive fuera del bucle, así los reintentos aprovechan el pool de conexiones.
- La función asume que cada producto trae `id` y `name`; si pueden faltar, cambia `p["id"]` por `p.get("id")`.

Si necesitas la versión asíncrona (`httpx.AsyncClient` + `asyncio.sleep`), dímelo y te la adapto.