# Inkling Small — code_generation/python_api_integration

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.38 | quality: 9.52
- latency_total: 12.853s | tokens_per_second: 306.5
- input_tokens: 110 | output_tokens: 3939
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

Aquí tienes una función completa con `httpx`, sin dependencias extra. Usa `timeout=10.0`, captura errores de red/timeout, hace **3 intentos totales** con backoff exponencial (`1s`, `2s`) y filtra por `price > 100`.

```python
import time
import httpx


def fetch_filtered_products(token: str, url: str = "https://api.example.com/products") -> list[dict]:
    """
    Realiza GET con Bearer token, filtra productos con precio > 100 y retorna
    lista de dicts con solo {id, name, price}.
    """
    headers = {"Authorization": f"Bearer {token}"}
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            # 1. Request con timeout de 10 segundos
            with httpx.Client(timeout=10.0) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()
                payload = resp.json()

            # 2. Normalizar respuesta (lista directa o envuelto en dict)
            if isinstance(payload, list):
                products = payload
            elif isinstance(payload, dict):
                products = (
                    payload.get("products")
                    or payload.get("data")
                    or payload.get("items")
                    or []
                )
            else:
                products = []

            # 3. Filtrar y proyectar
            result = []
            for p in products:
                if not isinstance(p, dict):
                    continue

                raw_price = p.get("price")
                # Intentar interpretar precio como número (int o float)
                if isinstance(raw_price, bool):
                    price = None  # evitar que bool cuente como int
                elif isinstance(raw_price, (int, float)):
                    price = raw_price
                else:
                    try:
                        price = float(raw_price)
                        if isinstance(price, float) and price.is_integer():
                            price = int(price)
                    except (ValueError, TypeError):
                        price = None

                if price is not None and price > 100:
                    result.append({
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": price,
                    })

            return result

        except (httpx.NetworkError, httpx.TimeoutException, httpx.ConnectError) as exc:
            # 4. Manejo de errores de red / timeout + retry con backoff exponencial
            if attempt == max_attempts:
                raise exc  # relanzar si ya no hay más intentos
            
            # Backoff exponencial: 1s (intento 1→2), 2s (intento 2→3)
            time.sleep(2 ** (attempt - 1))

        except httpx.HTTPStatusError:
            # Errores HTTP (4xx/5xx) no se retiran; se propagan inmediatamente
            raise
        except Exception:
            # Otros errores (JSON malformado, etc.) se propagan
            raise

    # Si llegamos aquí, todos los intentos fallaron (por seguridad)
    raise RuntimeError("No se pudo obtener productos tras el máximo de intentos.")
```

### Puntos clave
- **Autenticación**: header `Authorization: Bearer <token>`.
- **Timeout**: `httpx.Client(timeout=10.0)` aplica a conexión + lectura.
- **Retry / Backoff**: 3 intentos con esperas de `1` y `2` segundos (`2 ** (attempt - 1)`).
- **Errores cubiertos**: `NetworkError`, `TimeoutException`, `ConnectError`; si persisten tras 3 intentos se relanzan.
- **Filtrado y proyección**: solo conserva `id`, `name`, `price` y descarta precios `<= 100` o no numéricos.