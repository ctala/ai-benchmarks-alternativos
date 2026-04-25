# Claude Opus 4.6 — code_generation/python_api_integration

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.33 | quality: 9.52
- latency_total: 33.162s | tokens_per_second: 61.8
- input_tokens: 123 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa



# Función Python para consumir API de productos con `httpx`

## Código completo

```python
import httpx
import time
from typing import Optional


def fetch_expensive_products(
    token: str,
    min_price: float = 100.0,
    base_url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos de la API cuyo precio supera el umbral indicado.

    Args:
        token:       Bearer token para autenticación.
        min_price:   Precio mínimo para filtrar (exclusivo). Default 100.
        base_url:    URL del endpoint de productos.
        max_retries: Número máximo de intentos (incluye el primero).
        timeout:     Segundos máximos de espera por request.

    Returns:
        Lista de dicts con claves {id, name, price}.

    Raises:
        httpx.HTTPStatusError: Si la respuesta tiene código 4xx/5xx
                               tras agotar reintentos.
        httpx.RequestError:    Si falla la conexión tras agotar reintentos.
    """

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    # ── Retry con backoff exponencial ──────────────────────────────
    last_exception: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            # Un client nuevo por intento evita reutilizar sockets rotos
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)

                # Lanza httpx.HTTPStatusError si status >= 400
                response.raise_for_status()

            # ── Filtrado y proyección ──────────────────────────────
            products: list[dict] = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > min_price
            ]

        # Errores de red / DNS / conexión rechazada
        except httpx.RequestError as exc:
            last_exception = exc
            print(
                f"[intento {attempt}/{max_retries}] "
                f"Error de red: {exc}"
            )

        # Errores HTTP (5xx son reintentables, 4xx no)
        except httpx.HTTPStatusError as exc:
            last_exception = exc
            status = exc.response.status_code

            # No reintentar errores del cliente (400-499)
            if 400 <= status < 500:
                print(f"Error del cliente ({status}): no se reintenta.")
                raise

            print(
                f"[intento {attempt}/{max_retries}] "
                f"Error del servidor ({status})"
            )

        # ── Backoff exponencial: 1s → 2s → (no duerme en último) ──
        if attempt < max_retries:
            wait = 2 ** (attempt - 1)          # 1, 2, 4 …
            print(f"    Reintentando en {wait}s …")
            time.sleep(wait)

    # Agotados los reintentos → propagar la última excepción
    raise last_exception  # type: ignore[misc]


# ── Ejemplo de uso ────────────────────────────────────────────────
if __name__ == "__main__":
    API_TOKEN = "tu_token_aqui"

    try:
        products = fetch_expensive_products(token=API_TOKEN)
        print(f"\n✅ {len(products)} productos con precio > 100:\n")
        for p in products:
            print(f"  • [{p['id']}] {p['name']} — ${p['price']:.2f}")

    except httpx.HTTPStatusError as e:
        print(f"\n❌ Error HTTP {e.response.status_code}: {e}")
    except httpx.RequestError as e:
        print(f"\n❌ Error de conexión tras reintentos: {e}")
```

---

## Flujo visual del retry

```
Intento 1 ──► ¿Éxito? ──► SÍ ──► Filtrar y retornar
                │
                NO (error red / 5xx)
                │
          sleep(1s)  ← 2⁰
                │
Intento 2 ──► ¿Éxito? ──► SÍ ──► Filtrar y retornar
                │
                NO
                │
          sleep(2s)  ← 2¹
                │
Intento 3 ──► ¿Éxito? ──► SÍ ──► Filtrar y retornar
                │
                NO
                │
          raise última excepción
```

---

## Decisiones de diseño clave

| Aspecto | Detalle |
|---|---|
| **Timeout** | `httpx.Client(timeout=10.0)` aplica a **connect + read + write + pool** |
| **Backoff** | Exponencial `2^(n-1)` → esperas de **1s, 2s** (3 intentos) |
| **4xx vs 5xx** | Los errores **4xx se propagan inmediatamente** (no tiene sentido reintentar un 401/404); los **5xx sí se reintentan** |
| **Proyección** | Se extraen **solo** `id`, `name`, `price` → menor huella de memoria |
| **Sin dependencias extra** | Solo `httpx` + stdlib (`time`, `typing`) |

---

## Tests unitarios (ejemplo con `pytest`)

```python
import httpx
import pytest
from unittest.mock import patch

from products import fetch_expensive_products


# ── Datos de prueba ───────────────────────────────────────────────
MOCK_PRODUCTS = [
    {"id": 1, "name": "Laptop",    "price": 999.99, "category": "tech"},
    {"id": 2, "name": "Cable USB", "price": 5.50,   "category": "tech"},
    {"id": 3, "name": "Monitor",   "price": 350.00, "category": "tech"},
]


def _mock_response(status=200, json_data=None):
    """Crea un httpx.Response falso."""
    resp = httpx.Response(
        status_code=status,
        json=json_data or [],
        request=httpx.Request("GET", "https://api.example.com/products"),
    )
    return resp


# ── Tests ─────────────────────────────────────────────────────────
class TestFetchExpensiveProducts:

    @patch("products.httpx.Client")
    def test_filters_by_price(self, MockClient):
        """Solo retorna productos con precio > 100."""
        instance = MockClient.return_value.__enter__.return_value
        instance.get.return_value = _mock_response(200, MOCK_PRODUCTS)

        result = fetch_expensive_products(token="fake-token")

        assert len(result) == 2
        assert all(p["price"] > 100 for p in result)
        assert set(result[0].keys()) == {"id", "name", "price"}

    @patch("products.httpx.Client")
    def test_retry_on_server_error(self, MockClient):
        """Reintenta en 5xx y finalmente tiene éxito."""
        instance = MockClient.return_value.__enter__.return_value
        error_resp = _mock_response(503)
        ok_resp    = _mock_response(200, MOCK_PRODUCTS)

        instance.get.side_effect = [
            httpx.HTTPStatusError("503", request=error_resp.request, response=error_resp),
            ok_resp,
        ]

        