# Kimi K3 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.28 | quality: 9.08
- latency_total: 113.25s | tokens_per_second: 39.4
- input_tokens: 192 | output_tokens: 4466
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

Aquí está la función completa:

```python
import logging
import time

import httpx

logger = logging.getLogger(__name__)

API_URL = "https://api.example.com/products"
TIMEOUT = 10.0       # segundos
MAX_ATTEMPTS = 3
BASE_DELAY = 1.0     # backoff exponencial: 1s, 2s entre intentos


def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos de la API y retorna solo los de precio > 100.

    Args:
        token: Bearer token para autenticación.

    Returns:
        Lista de dicts con las claves: id, name, price.

    Raises:
        httpx.TimeoutException / httpx.NetworkError: si se agotan los reintentos.
        httpx.HTTPStatusError: si la API responde con 4xx/5xx (no se reintenta).
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    with httpx.Client(timeout=TIMEOUT, headers=headers) as client:
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                response = client.get(API_URL)
                response.raise_for_status()  # 4xx/5xx lanza HTTPStatusError

                return [
                    {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                    for p in response.json()
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

            except (httpx.TimeoutException, httpx.NetworkError) as exc:
                if attempt == MAX_ATTEMPTS:
                    logger.error("Agotados %d intentos: %s", MAX_ATTEMPTS, exc)
                    raise
                delay = BASE_DELAY * 2 ** (attempt - 1)  # 1s, 2s, 4s...
                logger.warning(
                    "Intento %d/%d falló (%s). Reintentando en %.0f s...",
                    attempt, MAX_ATTEMPTS, type(exc).__name__, delay,
                )
                time.sleep(delay)
```

**Ejemplo de uso:**

```python
if __name__ == "__main__":
    try:
        productos = fetch_expensive_products("mi-token-secreto")
        for p in productos:
            print(p)
    except httpx.HTTPError as e:
        print(f"No se pudieron obtener los productos: {e}")
```

**Decisiones de diseño:**

- **Backoff exponencial:** los delays son 1s y 2s entre los 3 intentos (`BASE_DELAY * 2^(intento-1)`).
- **Qué se reintenta:** solo errores de red y timeout (`httpx.NetworkError`, `httpx.TimeoutException`). Los errores HTTP 4xx/5xx se propagan inmediatamente, porque reintentar un 401 o 404 no tiene sentido.
- **Cliente reutilizado:** un solo `httpx.Client` para todos los intentos, aprovechando el connection pooling.
- **Filtro robusto:** `isinstance` evita `TypeError` si algún producto viene sin `price` o con `null`.

**Notas:**

- Se asume que la API devuelve un array JSON directo. Si viene envuelto (ej. `{"products": [...]}`), cambia `response.json()` por `response.json()["products"]`.
- Si también quieres reintentar errores 5xx o 429, agrega un `except httpx.HTTPStatusError` que verifique `exc.response.status_code >= 500` antes de decidir reintentar o relanzar.