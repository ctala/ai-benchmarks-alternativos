# Kimi K2.7 Code — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.8 | quality: 9.28
- latency_total: 48.96s | tokens_per_second: 49.6
- input_tokens: 114 | output_tokens: 2427
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

Aquí tienes una función sincrónica usando solo `httpx` (estándar en la librería, sin dependencias extras):

```python
import time
import httpx


def get_expensive_products(token: str, min_price: float = 100.0) -> list[dict]:
    """
    Obtiene productos de la API filtrando por precio > min_price.
    
    Retorna una lista de dicts con {id, name, price}.
    Reintenta hasta 3 veces con backoff exponencial y timeout de 10s.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    timeout = httpx.Timeout(10.0)
    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                break  # Éxito: sale del bucle de reintentos
        except httpx.TimeoutException as exc:
            if attempt == max_retries:
                raise RuntimeError("Timeout tras 3 intentos") from exc
        except httpx.NetworkError as exc:
            if attempt == max_retries:
                raise RuntimeError("Error de red tras 3 intentos") from exc
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            # No reintenta errores 4xx; sí reintenta 5xx
            if 400 <= status < 500 or attempt == max_retries:
                raise RuntimeError(f"Error HTTP {status}") from exc

        # Backoff exponencial: 1s, 2s, 4s
        time.sleep(2 ** (attempt - 1))

    data = response.json()
    products = data if isinstance(data, list) else data.get("products", [])

    return [
        {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
        for p in products
        if isinstance(p, dict) and p.get("price", 0) > min_price
    ]
```

### Uso

```python
products = get_expensive_products(token="tu_token_aqui")
print(products)
```

### Detalles

- **Autenticación**: envía `Authorization: Bearer <token>`.
- **Timeout**: 10 segundos totales por request (`httpx.Timeout(10.0)`).
- **Reintentos**: máximo 3 intentos, con esperas de 1s, 2s y 4s.
- **Errores**: maneja timeout, errores de red y HTTP; agrupa 4xx como fallos definitivos.
- **Filtro/mapa**: descarta productos con `price <= 100` y devuelve solo `{id, name, price}`.
- **Flexibilidad**: soporta respuesta como lista directa o como dict con clave `products`.