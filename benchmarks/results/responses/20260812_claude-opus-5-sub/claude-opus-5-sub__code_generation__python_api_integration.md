# Claude Opus 5 (suscripción) — code_generation/python_api_integration

- model_id: `claude-opus-5`
- success: True  | final: 7.27 | quality: 8.88
- latency_total: 42.119s | tokens_per_second: 64.0
- input_tokens: 2 | output_tokens: 2696
- judge_score: 4.2 | justificación: 

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
"""Cliente mínimo para obtener productos filtrados desde api.example.com."""

from __future__ import annotations

import logging
import random
import time
from typing import Any, Iterable

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT_S = 10.0
MAX_INTENTOS = 3
BACKOFF_BASE_S = 1.0

# Códigos donde reintentar tiene sentido: rate limit + fallas del servidor.
STATUS_REINTENTABLES = {408, 425, 429, 500, 502, 503, 504}


class ProductsAPIError(RuntimeError):
    """Falla definitiva al consultar el endpoint de productos."""


def obtener_productos_caros(
    token: str,
    precio_minimo: float = 100.0,
    *,
    url: str = API_URL,
    timeout_s: float = TIMEOUT_S,
    max_intentos: int = MAX_INTENTOS,
    client: httpx.Client | None = None,
) -> list[dict[str, Any]]:
    """
    GET a la API de productos y devuelve solo los que superan `precio_minimo`.

    Retorna: [{"id": ..., "name": ..., "price": float}, ...]
    Lanza: ProductsAPIError si se agotan los reintentos o la respuesta es inválida.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    propio = client is None
    client = client or httpx.Client(timeout=httpx.Timeout(timeout_s))

    try:
        payload = _get_con_retry(
            client, url, headers=headers, max_intentos=max_intentos
        )
    finally:
        if propio:
            client.close()

    return [
        producto
        for producto in _normalizar(payload)
        if producto["price"] > precio_minimo
    ]


def _get_con_retry(
    client: httpx.Client,
    url: str,
    *,
    headers: dict[str, str],
    max_intentos: int,
) -> Any:
    ultimo_error: Exception | None = None

    for intento in range(1, max_intentos + 1):
        try:
            respuesta = client.get(url, headers=headers)

            if respuesta.status_code in STATUS_REINTENTABLES:
                respuesta.raise_for_status()

            # 4xx no reintentables (401, 403, 404...): falla inmediata.
            if respuesta.is_error:
                raise ProductsAPIError(
                    f"HTTP {respuesta.status_code} en {url}: {respuesta.text[:200]}"
                )

            return respuesta.json()

        except ProductsAPIError:
            raise  # error definitivo, no reintentar

        except httpx.HTTPStatusError as exc:
            ultimo_error = exc
            espera = _espera(intento, respuesta=exc.response)

        except (httpx.TimeoutException, httpx.TransportError) as exc:
            # Cubre timeouts, DNS, conexión rechazada, TLS, lecturas cortadas.
            ultimo_error = exc
            espera = _espera(intento)

        except ValueError as exc:  # JSON inválido
            raise ProductsAPIError(f"Respuesta no es JSON válido: {exc}") from exc

        if intento == max_intentos:
            break

        logger.warning(
            "Intento %s/%s falló (%s). Reintento en %.2fs",
            intento, max_intentos, type(ultimo_error).__name__, espera,
        )
        time.sleep(espera)

    raise ProductsAPIError(
        f"Falló tras {max_intentos} intentos: {ultimo_error!r}"
    ) from ultimo_error


def _espera(intento: int, respuesta: httpx.Response | None = None) -> float:
    """Backoff exponencial con jitter; respeta Retry-After si el server lo manda."""
    if respuesta is not None:
        retry_after = respuesta.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            return min(float(retry_after), 30.0)

    base = BACKOFF_BASE_S * (2 ** (intento - 1))   # 1s, 2s, 4s
    return base + random.uniform(0, base * 0.25)   # jitter: evita reintentos sincronizados


def _normalizar(payload: Any) -> Iterable[dict[str, Any]]:
    """Acepta lista cruda o {"data": [...]} / {"products": [...]}."""
    if isinstance(payload, dict):
        for clave in ("data", "products", "items", "results"):
            if isinstance(payload.get(clave), list):
                payload = payload[clave]
                break
        else:
            raise ProductsAPIError(f"Formato inesperado: {list(payload)[:5]}")

    if not isinstance(payload, list):
        raise ProductsAPIError(f"Se esperaba una lista, llegó {type(payload).__name__}")

    for item in payload:
        if not isinstance(item, dict):
            continue
        try:
            precio = float(item["price"])
        except (KeyError, TypeError, ValueError):
            logger.debug("Producto descartado, precio inválido: %r", item)
            continue

        yield {"id": item.get("id"), "name": item.get("name"), "price": precio}
```

**Uso:**

```python
productos = obtener_productos_caros(token="tu-token", precio_minimo=100)
for p in productos:
    print(p["id"], p["name"], p["price"])
```

Tres decisiones que vale la pena marcar:

1. **No reintenta 4xx.** Un 401 o un 404 no mejoran esperando 4 segundos; solo reintenta timeouts, errores de transporte, 429 y 5xx. Reintentar un token vencido es quemar tiempo y arriesgar rate limit.
2. **Jitter en el backoff.** Sin él, si tienes N workers fallando a la vez, todos reintentan en el mismo milisegundo y vuelves a tumbar el endpoint. También respeta `Retry-After` si el servidor lo manda, capado a 30s.
3. **`client` inyectable.** Si llamas esto en un loop, pásale un `httpx.Client` reusado — reaprovechas la conexión TCP/TLS y bajas latencia bastante. Además te deja testear con `httpx.MockTransport` sin tocar la red.

Si lo vas a correr dentro de código async, la conversión es directa: `httpx.AsyncClient`, `await client.get(...)` y `await asyncio.sleep(espera)`. El resto de la lógica no cambia.