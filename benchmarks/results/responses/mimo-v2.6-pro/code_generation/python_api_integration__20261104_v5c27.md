# MiMo V2.6 Pro — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 7.48 | quality: 8.12
- latency_total: 25.031s | tokens_per_second: 66.6
- input_tokens: 111 | output_tokens: 1668
- judge_score: 3.8 | justificación: 

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

# Función con httpx: GET, filtro, retry y manejo de errores

```python
import httpx
import time


def get_expensive_products(
    base_url: str = "https://api.example.com/products",
    bearer_token: str = "",
    min_price: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_base: float = 1.0,   # segundo base del backoff
) -> list[dict]:
    """
    Obtiene productos desde una API REST, filtra por precio mínimo
    y devuelve solo los campos {id, name, price}.

    Args:
        base_url:    URL del endpoint de productos.
        bearer_token: Token de autenticación (Bearer).
        min_price:   Precio mínimo (exclusivo) para filtrar.
        timeout:     Timeout de cada petición en segundos.
        max_retries: Número máximo de intentos (incluye el primero).
        backoff_base: Base del backoff exponencial en segundos.

    Returns:
        Lista de dicts con las claves "id", "name" y "price".

    Raises:
        httpx.HTTPStatusError: Si la API responde con error HTTP definitivo
                               (4xx o 5xx tras agotar los reintentos).
        httpx.RequestError:    Si hay un error de red tras agotar los reintentos.
    """
    if not bearer_token:
        raise ValueError("bearer_token no puede estar vacío")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    last_exception: Exception | None = None

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)

                # Errores HTTP 4xx/5xx → retry para 5xx, fallo directo para 4xx
                response.raise_for_status()

                data = response.json()  # Se espera una lista de productos

            # ── Filtrado y proyección ──────────────────────────────
            result = [
                {
                    "id": product.get("id"),
                    "name": product.get("name"),
                    "price": product.get("price"),
                }
                for product in data
                if isinstance(product.get("price"), (int, float))
                and product["price"] > min_price
            ]

            return result

        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code

            # 4xx: error del cliente → NO tiene sentido reintentar
            if 400 <= status < 500:
                raise

            # 5xx: error del servidor → reintentable
            last_exception = exc

        except (httpx.ConnectError, httpx.ReadTimeout,
                httpx.ConnectTimeout, httpx.WriteTimeout,
                httpx.PoolTimeout, httpx.RemoteProtocolError) as exc:
            # Errores de red / timeout → reintentables
            last_exception = exc

        # ── Backoff exponencial antes del siguiente intento ────────
        if attempt < max_retries:
            sleep_time = backoff_base * (2 ** (attempt - 1))  # 1s, 2s, 4s…
            time.sleep(sleep_time)

    # Se agotaron los reintentos
    raise last_exception
```

---

## Desglose de cada requisito

| Requisito | Cómo se resuelve |
|---|---|
| **1. GET con Bearer** | `httpx.Client().get(url, headers={"Authorization": f"Bearer {token}"})` |
| **2. Filtro precio > 100** | List comprehension: `if product["price"] > min_price` |
| **3. Solo {id, name, price}** | Proyección en el dict dentro de la comprensión |
| **4. Errores de red y timeout (10 s)** | `httpx.Client(timeout=10.0)` + captura de `ConnectError`, `ReadTimeout`, etc. |
| **5. Retry con backoff exponencial (3 intentos)** | Bucle `for attempt in range(1, 4)` con `time.sleep(backoff_base * 2**(attempt-1))` → 1 s, 2 s |
| **Solo httpx** | No se usa `requests`, `urllib3`, ni ningún otro paquete externo |

---

## Uso rápido

```python
# Uso mínimo
products = get_expensive_products(bearer_token="mi_token_aqui")

for p in products:
    print(p)
# {'id': 42, 'name': 'Laptop Pro', 'price': 1299.99}
# {'id': 87, 'name': 'Monitor 4K', 'price': 549.00}
```

```python
# Uso personalizado
products = get_expensive_products(
    base_url="https://api.myshop.com/v2/products",
    bearer_token="eyJhbGciOi...",
    min_price=200.0,
    timeout=5.0,
    max_retries=3,
    backoff_base=2.0,   # 2s, 4s entre reintentos
)
```

---

## Diagrama del flujo

```
┌─────────────────────────────────────────────────┐
│              get_expensive_products()            │
│                                                 │
│  attempt = 1                                    │
│  ┌──────────────────────────────┐               │
│  │  GET /products (timeout 10s) │               │
│  └──────────┬───────────────────┘               │
│             │                                   │
│     ┌───────▼────────┐                          │
│     │  ¿Éxito HTTP?  │                          │
│     └───┬───────┬────┘                          │
│      Sí │       │ No                            │
│         │   ┌───▼──────────────┐                │
│         │   │ ¿4xx? → raise    │                │
│         │   │ ¿5xx? → retry    │                │
│         │   │ ¿Red?  → retry   │                │
│         │   └───┬──────────────┘                │
│         │       │ attempt < 3?                  │
│         │     Sí│  sleep(1s, 2s) → retry        │
│         │     No│  raise last_exception         │
│         │       │                               │
│  ┌──────▼───────▼──────────────┐                │
│  │ Filtrar price > min_price   │                │
│  │ Proyectar {id, name, price} │                │
│  └──────────────┬──────────────┘                │
│                 │                               │
│          return result                          │
└─────────────────────────────────────────────────┘
```