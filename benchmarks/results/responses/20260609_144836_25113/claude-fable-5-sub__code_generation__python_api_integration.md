# Claude Fable 5 (suscripción) — code_generation/python_api_integration

- model_id: `claude-fable-5`
- success: True  | final: 7.05 | quality: 9.34
- latency_total: 14.397s | tokens_per_second: 78.8
- input_tokens: 2 | output_tokens: 1134

## Respuesta completa

```python
import time
import httpx


def get_expensive_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    min_price: float = 100,
    max_retries: int = 3,
    timeout: float = 10.0,
) -> list[dict]:
    """
    Obtiene productos con precio > min_price desde la API.

    Args:
        token: Bearer token para autenticación.
        base_url: URL del endpoint de productos.
        min_price: Precio mínimo (exclusivo) para filtrar.
        max_retries: Máximo de intentos (default 3).
        timeout: Timeout total por request en segundos.

    Returns:
        Lista de dicts con {id, name, price}.

    Raises:
        RuntimeError: Si todos los intentos fallan.
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                products = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > min_price
            ]

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Errores transitorios: reintentar con backoff exponencial
            last_error = e
        except httpx.HTTPStatusError as e:
            # 5xx puede ser transitorio; 4xx no tiene sentido reintentar
            if e.response.status_code >= 500:
                last_error = e
            else:
                raise RuntimeError(
                    f"Error HTTP {e.response.status_code}: {e.response.text}"
                ) from e

        # Backoff exponencial: 1s, 2s, 4s... (no esperar tras el último intento)
        if attempt < max_retries - 1:
            time.sleep(2 ** attempt)

    raise RuntimeError(
        f"Falló después de {max_retries} intentos: {last_error}"
    ) from last_error
```

**Uso:**

```python
products = get_expensive_products(token="mi-token-secreto")
# [{"id": 1, "name": "Laptop", "price": 1200.0}, ...]
```

**Puntos clave del diseño:**

- **Timeout de 10s** vía `httpx.Client(timeout=10.0)` — aplica a connect + read + write.
- **Retry solo en errores transitorios**: timeouts, errores de red y HTTP 5xx. Los 4xx (token inválido, 404) fallan inmediato porque reintentar no los arregla.
- **Backoff exponencial**: 1s → 2s → falla (3 intentos totales). Se calcula con `2 ** attempt` y no se espera después del último intento.
- **`raise_for_status()`** convierte respuestas 4xx/5xx en excepción en lugar de procesar JSON de error como si fueran productos.
- **`p.get("price", 0)`** evita `KeyError` si algún producto viene sin precio.

Si manejas muchas llamadas concurrentes, considera la versión async (`httpx.AsyncClient` + `asyncio.sleep`) — la lógica es idéntica.