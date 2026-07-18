# Kimi K3 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.47 | quality: 9.36
- latency_total: 111.817s | tokens_per_second: 37.3
- input_tokens: 192 | output_tokens: 4168
- judge_score: 5.0 | justificación: 

## Respuesta completa

```python
import logging
import time
from typing import Any

import httpx

logger = logging.getLogger(__name__)

URL = "https://api.example.com/products"
TIMEOUT_SEGUNDOS = 10.0
MAX_INTENTOS = 3


def obtener_productos_caros(token: str) -> list[dict[str, Any]]:
    """
    GET /products con Bearer token; devuelve {id, name, price}
    solo de productos con precio > 100.

    Reintenta ante errores de red, timeout y respuestas 5xx con
    backoff exponencial (1s, 2s). Los errores 4xx no se reintentan.

    Raises:
        httpx.HTTPStatusError: Error HTTP tras agotar reintentos (o 4xx inmediato).
        httpx.TimeoutException / httpx.NetworkError: Fallo de red/timeout persistente.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=TIMEOUT_SEGUNDOS) as cliente:
        for intento in range(1, MAX_INTENTOS + 1):
            try:
                resp = cliente.get(URL, headers=headers)
                resp.raise_for_status()

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in resp.json()
                    if p.get("price", 0) > 100
                ]

            except httpx.HTTPStatusError as e:
                # 4xx = error del cliente (token inválido, etc.): reintentar no ayuda
                if e.response.status_code < 500 or intento == MAX_INTENTOS:
                    raise
                detalle = f"HTTP {e.response.status_code}"

            except (httpx.TimeoutException, httpx.NetworkError) as e:
                if intento == MAX_INTENTOS:
                    raise
                detalle = str(e)

            espera = 2 ** (intento - 1)  # 1s, 2s
            logger.warning(
                "Intento %d/%d falló (%s). Reintentando en %ds...",
                intento, MAX_INTENTOS, detalle, espera,
            )
            time.sleep(espera)

    raise RuntimeError("Inalcanzable")  # satisface al type checker
```

**Uso:**

```python
try:
    productos = obtener_productos_caros("mi_token")
    print(f"{len(productos)} productos con precio > 100")
except httpx.HTTPError as e:
    print(f"La API falló definitivamente: {e}")
```

**Decisiones de diseño:**

- **Reintentos selectivos**: solo se reintentan errores transitorios (red, timeout, 5xx). Un 401/403/404 no se reintenta porque fallaría igual las 3 veces.
- **Backoff**: 1s antes del 2º intento, 2s antes del 3º (`2 ** (intento - 1)`). Si quieres evitar thundering herd, puedes añadir jitter con `random` (stdlib): `espera += random.uniform(0, 0.5)`.
- **Timeout de 10s** aplicado a toda la operación por request (conexión, lectura y pool).
- **Un solo `Client`** reutilizado entre reintentos (mejor que crear uno por intento).

Si tu contexto es async, la versión con `httpx.AsyncClient` y `asyncio.sleep()` es casi idéntica — dímelo y la escribo.