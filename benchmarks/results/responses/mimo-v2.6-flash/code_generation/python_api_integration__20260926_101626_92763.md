# MiMo V2.6 Flash — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.72 | quality: 9.52
- latency_total: 25.794s | tokens_per_second: 53.8
- input_tokens: 111 | output_tokens: 1389
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
from typing import List, Dict, Any

import httpx


def get_expensive_products(
    api_key: str,
    *,
    base_url: str = "https://api.example.com",
    timeout: float = 10.0,
    max_retries: int = 3,
    price_threshold: float = 100.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde la API.

    Args:
        api_key:       Bearer token para autenticación.
        base_url:      URL base del endpoint.
        timeout:       Timeout en segundos por request.
        max_retries:   Número máximo de intentos (incluye el primero).
        price_threshold: Precio mínimo para filtrar.

    Returns:
        Lista de dicts con claves {id, name, price}.

    Raises:
        httpx.HTTPStatusError: Si la API devuelve un error 4xx/5xx tras agotar reintentos.
        httpx.HTTPError:       Si todos los intentos fallan por red/timeout.
    """

    url = f"{base_url}/products"
    headers = {"Authorization": f"Bearer {api_key}"}
    last_exception: httpx.HTTPError | None = None

    for attempt in range(max_retries):
        # ── Backoff exponencial: 1 s, 2 s, 4 s … ──
        if attempt > 0:
            backoff = 2 ** (attempt - 1)  # 1, 2, 4, ...
            time.sleep(backoff)

        try:
            # ── Requisito 1: GET con Bearer token ──
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()          # 4xx/5xx → HTTPStatusError

            # ── Requisito 2-3: filtrar y proyectar ──
            products: List[Dict[str, Any]] = response.json()
            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > price_threshold
            ]

        # ── Requisito 4: errores de red / timeout ──
        except httpx.TimeoutException as exc:
            last_exception = exc
            print(f"[intent {attempt + 1}/{max_retries}] Timeout: {exc}")

        except httpx.ConnectError as exc:
            last_exception = exc
            print(f"[intent {attempt + 1}/{max_retries}] Error de conexión: {exc}")

        except httpx.HTTPStatusError as exc:
            # Errores 4xx no se reintentan (p. ej. 401, 403, 404)
            if exc.response.status_code >= 500 and attempt < max_retries - 1:
                last_exception = exc
                print(
                    f"[intent {attempt + 1}/{max_retries}] "
                    f"HTTP {exc.response.status_code} — reintentando…"
                )
                continue
            raise  # 4xx o último intento con 5xx → propagar

        except httpx.HTTPError as exc:
            last_exception = exc
            print(f"[intent {attempt + 1}/{max_retries}] Error HTTP: {exc}")

    # ── Si llegamos aquí, se agotaron todos los reintentos ──
    raise last_exception  # type: ignore[misc]


# ─────────────────────────── demo / ejemplo de uso ───────────────────────────
if __name__ == "__main__":
    try:
        resultados = get_expensive_products(api_key="tu-bearer-token-aqui")
        for producto in resultados:
            print(producto)
    except httpx.HTTPError as e:
        print(f"Fallo definitivo: {e}")
```

---

### Cómo funciona paso a paso

```
Intento 1 ──► GET /products ──► ¿OK? ──► filtrar >100 ──► retornar
                  │
                  ▼ (error de red / timeout / 5xx)
            esperar 1 s (2⁰)
                  │
Intento 2 ──► GET /products ──► ¿OK? ──► filtrar >100 ──► retornar
                  │
                  ▼ (error)
            esperar 2 s (2¹)
                  │
Intento 3 ──► GET /products ──► ¿OK? ──► filtrar >100 ──► retornar
                  │
                  ▼ (error)
            lanzar excepción  ✗
```

| Requisito | Dónde se resuelve |
|---|---|
| **Bearer token** | `headers = {"Authorization": f"Bearer {api_key}"}` |
| **Filtro precio > 100** | Comprensión con `if p["price"] > price_threshold` |
| **Solo `{id, name, price}`** | Proyección manual en la comprensión |
| **Timeout 10 s** | `httpx.Client(timeout=timeout)` |
| **Retry + backoff exponencial** | Bucle `for attempt` con `time.sleep(2 ** (attempt - 1))` |
| **Errores de red** | Captura de `TimeoutException`, `ConnectError`, `HTTPError` |

> **Nota:** los errores **4xx** (401, 403, 404…) **no se reintentan** porque son problemas de configuración/permisos, no transitorios. Solo los **5xx** y errores de red/timeout entran en el ciclo de reintentos.