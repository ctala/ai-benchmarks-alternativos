# Ling 3.0 Flash — code_generation/python_api_integration

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.07 | quality: 9.52
- latency_total: 8.359s | tokens_per_second: 384.7
- input_tokens: 140 | output_tokens: 3216
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
import httpx


def fetch_filtered_products(token: str) -> list[dict]:
    """
    Consulta la API de productos, filtra los que tienen precio > 100
    y retorna una lista con solo id, name y price.

    - Autenticación: Bearer token
    - Timeout: 10 segundos
    - Retry: hasta 3 intentos con backoff exponencial (1s, 2s, 4s)
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = httpx.Timeout(10.0)

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

            products = response.json()

            return [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > 100
            ]

        except (
            httpx.TimeoutException,
            httpx.ConnectError,
            httpx.ConnectTimeout,
            httpx.ReadTimeout,
        ) as exc:
            # Errores de red / timeout → reintento con backoff exponencial
            if attempt < max_retries - 1:
                wait = 2 ** attempt  # 1, 2, 4 segundos
                time.sleep(wait)
            else:
                raise RuntimeError(
                    f"Error de red tras {max_retries} intentos: {exc}"
                ) from exc

        except httpx.HTTPStatusError as exc:
            # Errores 5xx → reintento; errores 4xx → no se reintenta
            if exc.response.status_code >= 500 and attempt < max_retries - 1:
                wait = 2 ** attempt
                time.sleep(wait)
            else:
                raise

    # Este punto no debería alcanzarse, pero por seguridad:
    return []


# ── Ejemplo de uso ──────────────────────────────────────────────
if __name__ == "__main__":
    try:
        resultado = fetch_filtered_products("mi_token_aqui")
        print(resultado)
    except Exception as e:
        print(f"Error: {e}")
```

### Resumen de lo que hace cada parte

| Requisito | Implementación |
|---|---|
| **GET + Bearer token** | `headers = {"Authorization": f"Bearer {token}"}` en `client.get()` |
| **Filtro precio > 100** | List comprehension con `p["price"] > 100` |
| **Solo `{id, name, price}`** | Diccionario reducido en el `return` |
| **Timeout 10 s** | `httpx.Timeout(10.0)` pasado al `Client` |
| **Retry con backoff exponencial** | Bucle `for attempt in range(3)` + `time.sleep(2 ** attempt)` |
| **Manejo de errores** | `TimeoutException`, `ConnectError`, `HTTPStatusError` (5xx reintenta, 4xx lanza) |
| **Solo `httpx`** | Sin `requests`, `tenacity`, `backoff`, ni ninguna otra dependencia |