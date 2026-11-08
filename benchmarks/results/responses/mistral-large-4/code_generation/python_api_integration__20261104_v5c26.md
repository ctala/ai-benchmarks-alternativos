# Mistral Large 4.0 — code_generation/python_api_integration

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.16 | quality: 9.52
- latency_total: 63.464s | tokens_per_second: 111.3
- input_tokens: 108 | output_tokens: 7066
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

Aquí tienes una función completa usando **solo `httpx`** (junto con la librería estándar). Incluye reintentos con *backoff exponencial + jitter*, timeout de 10 s, filtrado por precio y manejo selectivo de errores HTTP (reintenta solo los transitorios: 408, 429 y 5xx).

```python
import re
import time
import random
from typing import Any, Optional

import httpx


def _parse_price(value: Any) -> float:
    """Convierte un precio (número o string como '$1,299.99') a float."""
    if isinstance(value, bool):          # bool hereda de int; lo descartamos
        raise ValueError("Invalid price")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        cleaned = value.strip().replace(",", ".")
        cleaned = re.sub(r"[^\d.\-]", "", cleaned)   # quita $, €, espacios, etc.
        if cleaned in ("", "-", ".", "-."):
            raise ValueError("Invalid price")
        return float(cleaned)
    raise ValueError("Invalid price type")


def _extract_products(payload: Any) -> list:
    """Extrae la lista de productos desde distintas estructuras comunes de API."""
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("products", "data", "items", "results"):
            value = payload.get(key)
            if isinstance(value, list):
                return value
    return []


def get_products_over_100(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    GET a `url` con Bearer token, filtra productos con precio > 100 y
    devuelve solo {id, name, price}.

    - Timeout total: `timeout` segundos (10 por defecto).
    - Reintentos: máx. `max_retries` intentos con backoff exponencial
      (1s, 2s, 4s… con jitter y tope de 8s).
    - Reintenta ante: errores de red, timeout, HTTP 408/429/5xx.
    - Lanza la última excepción si todos los intentos fallan.
    """
    if not token:
        raise ValueError("Se requiere un token Bearer")

    headers = {"Authorization": f"Bearer {token}"}
    last_exc: Optional[Exception] = None

    with httpx.Client(timeout=httpx.Timeout(timeout)) as client:
        for attempt in range(1, max_retries + 1):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                if response.status_code == 204:   # No Content
                    return []

                payload = response.json()
                products = _extract_products(payload)

                result: list[dict] = []
                for product in products:
                    if not isinstance(product, dict):
                        continue
                    try:
                        price = _parse_price(product.get("price"))
                    except (ValueError, TypeError):
                        continue
                    if price > 100:
                        result.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": product.get("price"),
                        })
                return result

            except httpx.HTTPStatusError as exc:
                status = exc.response.status_code
                # Solo reintentamos errores transitorios del servidor / rate-limit
                if status in (408, 429) or status >= 500:
                    last_exc = exc
                else:
                    raise          # 400, 401, 403, 404… no tienen sentido reintentar
            except httpx.RequestError as exc:
                # Errores de red, DNS, conexión rechazada, timeout, etc.
                last_exc = exc
            except httpx.HTTPError as exc:
                # Cualquier otro error HTTP de httpx (ej. decodificación)
                last_exc = exc
            except ValueError as exc:
                # JSON mal formado (json.JSONDecodeError hereda de ValueError)
                last_exc = exc

            # Backoff exponencial con jitter antes del siguiente intento
            if attempt < max_retries:
                backoff = min(2 ** (attempt - 1), 8)   # 1s, 2s, 4s (tope 8s)
                time.sleep(random.uniform(0, backoff))

    # Se agotaron todos los reintentos
    assert last_exc is not None
    raise last_exc


# ---------- Ejemplo de uso ----------
if __name__ == "__main__":
    TOKEN = "tu-token-aqui"
    try:
        productos = get_products_over_100(TOKEN)
        print(productos)
        # Ej: [{'id': 1, 'name': 'Laptop Pro', 'price': 1500.0}, ...]
    except Exception as e:
        print(f"Error tras agotar reintentos: {e}")
```

### Qué cubre cada requisito

| Requisito | Implementación |
|-----------|----------------|
| **GET con Bearer** | `headers={"Authorization": f"Bearer {token}"}` |
| **Filtro precio > 100** | `_parse_price` convierte strings/numéricos y compara `> 100` |
| **Solo {id, name, price}** | Se construye un dict nuevo con esas tres claves |
| **Errores de red / timeout 10s** | `httpx.Timeout(10.0)` + `except httpx.RequestError` |
| **Retry backoff exponencial (máx 3)** | Loop con `time.sleep(random.uniform(0, min(2**(attempt-1), 8)))`; reintenta solo 408/429/5xx y errores de red |

> **Nota:** Si necesitas la versión **asíncrona**, basta con cambiar `httpx.Client` por `httpx.AsyncClient`, `client.get` por `await client.get(...)` y `time.sleep` por `await asyncio.sleep(...)`.