# Muse Glimmer 30B — code_generation/python_api_integration

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.72 | quality: 9.72
- latency_total: 9.582s | tokens_per_second: 170.9
- input_tokens: 148 | output_tokens: 1638
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función síncrona con `httpx` que cumple todos los requisitos: autenticación Bearer, timeout de 10s, retry con backoff exponencial y filtrado.

```python
import time
import httpx
from typing import List, Dict

def fetch_expensive_products(bearer_token: str, url: str = "https://api.example.com/products") -> List[Dict]:
    """
    Obtiene productos desde la API y devuelve solo los con precio > 100.

    Args:
        bearer_token: Token para el header Authorization: Bearer ...
        url: Endpoint de productos

    Returns:
        Lista de dicts con {id, name, price}
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    max_attempts = 3
    timeout = 10.0

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()
                data = resp.json()

            # Validación básica
            if not isinstance(data, list):
                raise ValueError("Respuesta inesperada: se esperaba una lista")

            productos = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                and "id" in p and "name" in p
            ]
            return productos

        except httpx.TimeoutException as e:
            # Timeout de red
            last_err = f"Timeout en intento {attempt}: {e}"
        except httpx.RequestError as e:
            # Errores de red, DNS, conexión
            last_err = f"Error de red en intento {attempt}: {e}"
        except httpx.HTTPStatusError as e:
            # Error 4xx/5xx
            last_err = f"HTTP {e.response.status_code} en intento {attempt}"
            # No tiene sentido reintentar 4xx cliente, pero seguimos la política
        except Exception as e:
            last_err = f"Error inesperado en intento {attempt}: {e}"

        # Backoff exponencial antes del siguiente intento
        if attempt < max_attempts:
            sleep_time = 2 ** (attempt - 1)  # 1s, 2s, 4s
            time.sleep(sleep_time)

    # Si llegamos aquí, agotamos reintentos
    raise RuntimeError(f"No se pudo obtener productos tras {max_attempts} intentos. Último error: {last_err}")


# Ejemplo de uso
if __name__ == "__main__":
    TOKEN = "tu_token_aqui"
    try:
        productos = fetch_expensive_products(TOKEN)
        print(productos)
    except RuntimeError as err:
        print(err)
```

**Qué hace:**

1. **GET con Bearer**: `Authorization: Bearer {token}`.
2. **Timeout 10s**: `httpx.Client(timeout=10.0)`.
3. **Retry con backoff exponencial**: 3 intentos con espera 1s → 2s → 4s.
4. **Manejo de errores**: `TimeoutException`, `RequestError`, `HTTPStatusError` y errores de parsing.
5. **Filtrado**: solo productos con `price > 100` y devuelve dicts con `id`, `name` y `price`.

No requiere dependencias externas además de `httpx`.