# Claude Opus 4.8 (suscripción) — code_generation/python_api_integration

- model_id: `claude-opus-4-8`
- success: True  | final: 7.2 | quality: 9.52
- latency_total: 29.533s | tokens_per_second: 83.8
- input_tokens: 2028 | output_tokens: 2475
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí está la función. (El archivo no se escribió porque falta el permiso; te dejo el código directo.)

```python
"""Cliente para obtener productos desde api.example.com con retry y backoff."""
import time
from typing import Optional

import httpx

API_URL = "https://api.example.com/products"


def fetch_expensive_products(
    token: str,
    *,
    price_threshold: float = 100,
    timeout: float = 10.0,
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> list[dict]:
    """Obtiene productos, filtra por precio > threshold y proyecta {id, name, price}.

    Args:
        token: Bearer token de autenticacion.
        price_threshold: Solo se retornan productos con precio estrictamente mayor.
        timeout: Timeout de red en segundos (connect + read).
        max_retries: Numero maximo de intentos ante errores de red/HTTP transitorios.
        base_delay: Retardo base para el backoff exponencial (segundos).

    Returns:
        Lista de dicts con las claves {id, name, price}.

    Raises:
        httpx.HTTPError: Si se agotan los reintentos sin exito.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exc: Optional[Exception] = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(API_URL, headers=headers)
                response.raise_for_status()
                products = response.json()
            break  # exito: salir del loop de reintentos
        except (httpx.TransportError, httpx.HTTPStatusError) as exc:
            # TransportError cubre timeouts, fallos de conexion, DNS, etc.
            # HTTPStatusError cubre 4xx/5xx; reintentamos solo en 5xx.
            if isinstance(exc, httpx.HTTPStatusError) and exc.response.status_code < 500:
                raise  # errores de cliente (401, 404...) no se reintentan
            last_exc = exc
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)  # 1s, 2s, 4s...
                time.sleep(delay)
            else:
                raise  # se agotaron los intentos
    else:  # pragma: no cover - el break siempre sale antes
        raise last_exc  # type: ignore[misc]

    # Filtrar y proyectar
    result = []
    for p in products:
        price = p.get("price")
        if price is not None and price > price_threshold:
            result.append({"id": p.get("id"), "name": p.get("name"), "price": price})
    return result
```

**Decisiones de diseño:**

1. **Auth Bearer** → header `Authorization: Bearer <token>`.
2. **Filtro** `price > 100` con guarda `is not None` para evitar `TypeError` si la API devuelve `null`.
3. **Proyección** a `{id, name, price}` con `.get()` (tolerante a campos faltantes).
4. **Errores de red + timeout** → `httpx.Client(timeout=10.0)` cubre connect/read; `httpx.TransportError` captura timeouts y fallos de conexión.
5. **Retry con backoff exponencial** → hasta 3 intentos, esperas `1s → 2s → 4s` (`base_delay * 2**attempt`).

**Detalle importante:** distingo errores **4xx vs 5xx**. Un `401`/`404` no se reintenta (el resultado no va a cambiar y solo gastás tiempo); solo reintento en `5xx` y errores de transporte/timeout, que sí suelen ser transitorios.

Solo usa `httpx` + stdlib (`time`, `typing`), sin dependencias extra.

¿Querés que lo guarde como archivo en el repo (necesito que apruebes el permiso de escritura), o preferís una **versión async** con `httpx.AsyncClient`?