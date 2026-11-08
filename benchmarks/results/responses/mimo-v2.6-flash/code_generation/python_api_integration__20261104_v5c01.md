# MiMo V2.6 Flash — code_generation/python_api_integration

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.46 | quality: 9.52
- latency_total: 48.605s | tokens_per_second: 22.7
- input_tokens: 111 | output_tokens: 1105
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
import httpx

MAX_RETRIES = 3
BASE_DELAY = 1        # segundos para backoff: 1, 2, 4
TIMEOUT_SECONDS = 10
API_URL = "https://api.example.com/products"


def fetch_filtered_products(token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 y retorna solo {id, name, price}.

    Reintenta con backoff exponencial (1s, 2s, 4s) ante errores de red,
    timeout o respuestas 5xx.
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(API_URL, headers=headers)

                # 5xx → reintenta; 4xx → error irrecuperable
                if response.status_code >= 500:
                    response.raise_for_status()

                response.raise_for_status()          # 4xx lanza HTTPStatusError
                products = response.json()           # ya sabemos que es 2xx

            # --- filtrar y normalizar ---
            result = [
                {
                    "id": p.get("id"),
                    "name": p.get("name"),
                    "price": p.get("price"),
                }
                for p in products
                if isinstance(p, dict) and p.get("price", 0) > 100
            ]
            return result

        except (httpx.TimeoutException, httpx.ConnectError, httpx.HTTPStatusError) as exc:
            is_retryable = (
                isinstance(exc, httpx.HTTPStatusError)
                and exc.response.status_code >= 500
            ) or isinstance(exc, (httpx.TimeoutException, httpx.ConnectError))

            if is_retryable and attempt < MAX_RETRIES:
                delay = BASE_DELAY * (2 ** (attempt - 1))       # 1, 2, 4
                print(f"[retry] intento {attempt}/{MAX_RETRIES} "
                      f"falló ({exc!r}); reintentando en {delay}s…")
                time.sleep(delay)
                continue

            # Se agotaron los reintentos o es un error no reintentable
            raise

        except (ValueError, KeyError, TypeError) as exc:
            # JSON malformado o estructura inesperada
            raise ValueError(f"Respuesta con formato inválido: {exc}") from exc
```

## Flujo de la función

```
┌──────────────────────────────────────────────────────┐
│  GET /products  (Bearer token, timeout=10s)          │
│                                                      │
│  ¿Éxito (2xx)?                                       │
│   ├─ SÍ  → filtrar price > 100 → retornar lista      │
│   └─ NO                                           │
│        ├─ 5xx / timeout / connect error              │
│        │    ├─ intento < 3 → sleep(1s → 2s → 4s)     │
│        │    └─ intento = 3 → lanzar excepción         │
│        └─ 4xx (401, 403, 404…) → lanzar directo      │
└──────────────────────────────────────────────────────┘
```

### Decisiones clave

| Aspecto | Implementación |
|---|---|
| **Backoff exponencial** | `1·2⁰`, `1·2¹`, `1·2²` → **1s, 2s, 4s** |
| **Errores reintentables** | `ConnectError`, `TimeoutException`, `5xx` |
| **Errores no reintentables** | `4xx` (401, 403, 404…) se lanzan inmediatamente |
| **JSON inválido** | Se envuelve en `ValueError` con mensaje claro |
| **Context manager** | `httpx.Client` garantiza cierre de conexiones |