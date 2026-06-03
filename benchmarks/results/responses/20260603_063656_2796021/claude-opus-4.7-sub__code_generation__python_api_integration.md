# Claude Opus 4.7 (suscripción) — code_generation/python_api_integration

- model_id: `claude-opus-4-7`
- success: True  | final: 7.06 | quality: 9.44
- latency_total: 27.175s | tokens_per_second: 64.6
- input_tokens: 6 | output_tokens: 1755
- judge_score: 4.6 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any


def fetch_expensive_products(
    bearer_token: str,
    url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    base_backoff: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde la API, filtra por precio > threshold y retorna
    una lista normalizada con {id, name, price}.

    Args:
        bearer_token: Token Bearer para autenticación.
        url: Endpoint de la API.
        price_threshold: Precio mínimo (exclusivo) para incluir el producto.
        timeout: Timeout total por request en segundos.
        max_retries: Número máximo de intentos.
        base_backoff: Segundos base para backoff exponencial (1, 2, 4, ...).

    Returns:
        Lista de dicts con keys: id, name, price.

    Raises:
        httpx.HTTPError: Si tras max_retries todos los intentos fallan.
        ValueError: Si la respuesta no tiene el formato esperado.
    """
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    last_exception: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                payload = response.json()
                break  # éxito → salir del loop de retries

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            # Errores transitorios: reintentar con backoff
            last_exception = exc
            if attempt == max_retries:
                raise
            sleep_seconds = base_backoff * (2 ** (attempt - 1))
            time.sleep(sleep_seconds)

        except httpx.HTTPStatusError as exc:
            # 5xx → reintentable; 4xx → no reintentar (error del cliente)
            last_exception = exc
            status = exc.response.status_code
            if 500 <= status < 600 and attempt < max_retries:
                sleep_seconds = base_backoff * (2 ** (attempt - 1))
                time.sleep(sleep_seconds)
                continue
            raise
    else:
        # Defensa: el for-else solo corre si no hubo break (todos fallaron sin raise)
        if last_exception:
            raise last_exception
        raise RuntimeError("Fallo desconocido al obtener productos")

    # Normalizar payload: soportar tanto {"products": [...]} como [...]
    if isinstance(payload, dict):
        products = payload.get("products") or payload.get("data") or []
    elif isinstance(payload, list):
        products = payload
    else:
        raise ValueError(f"Formato de respuesta inesperado: {type(payload).__name__}")

    result: List[Dict[str, Any]] = []
    for product in products:
        if not isinstance(product, dict):
            continue
        price = product.get("price")
        if price is None or not isinstance(price, (int, float)):
            continue
        if price > price_threshold:
            result.append({
                "id": product.get("id"),
                "name": product.get("name"),
                "price": price,
            })

    return result


# Ejemplo de uso
if __name__ == "__main__":
    import os
    token = os.environ["API_TOKEN"]
    expensive = fetch_expensive_products(token)
    for p in expensive:
        print(f"{p['id']}: {p['name']} → ${p['price']}")
```

**Decisiones de diseño:**

1. **Backoff exponencial**: `base_backoff * 2^(attempt-1)` → 1s, 2s, 4s entre reintentos. Configurable vía `base_backoff`.

2. **Qué se reintenta vs qué no**:
   - `TimeoutException` y `NetworkError` → reintentar (transitorios)
   - `5xx` → reintentar (servidor caído)
   - `4xx` → **no reintentar** (auth fallida, recurso no existe — reintentar es gastar tiempo)

3. **Cliente con context manager** (`with httpx.Client(...)`) por intento: evita leak de conexiones si falla en medio del retry.

4. **Filtrado defensivo**: ignora productos sin `price` o con `price` no numérico en vez de crashear (APIs reales son sucias).

5. **Soporta dos formatos de payload**: `{"products": [...]}`, `{"data": [...]}` o lista raíz directa — común en APIs REST.

6. **Type hints explícitos** para que el caller sepa exactamente qué recibe.

Si querés que sea **async** (recomendado si lo llamás desde un agente con otras coroutines), cambiá `httpx.Client` → `httpx.AsyncClient`, agregá `async`/`await` y reemplazá `time.sleep` por `asyncio.sleep`. Avisame si te lo paso.