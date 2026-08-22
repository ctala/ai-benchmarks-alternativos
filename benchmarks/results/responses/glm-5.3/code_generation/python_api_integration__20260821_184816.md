# GLM 5.3 — code_generation/python_api_integration

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.56 | quality: 9.08
- latency_total: 78.097s | tokens_per_second: 89.8
- input_tokens: 113 | output_tokens: 7012
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

Aquí tienes la función:

```python
import time

import httpx


def get_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    min_price: float = 100,
    timeout: float = 10.0,
    max_retries: int = 3,
) -> list[dict]:
    """Obtiene productos con precio > min_price de la API.

    Hace GET con autenticación Bearer y reintenta con backoff
    exponencial ante timeouts, errores de red y errores 5xx.

    Raises:
        httpx.HTTPError: Si se agotan los intentos o hay un error 4xx.
    """
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=timeout, headers=headers) as client:
        for intento in range(1, max_retries + 1):
            try:
                response = client.get(url)
                response.raise_for_status()
                break  # Éxito: salir del bucle de reintentos
            except (httpx.TimeoutException, httpx.NetworkError):
                if intento == max_retries:
                    raise  # Reintenta la excepción original
                time.sleep(2 ** intento)  # Backoff: 2s, 4s
            except httpx.HTTPStatusError as exc:
                # Los 4xx no son transitorios: reintentar no ayuda
                if exc.response.status_code < 500 or intento == max_retries:
                    raise
                time.sleep(2 ** intento)

        # Se asume que la API devuelve una lista JSON de productos
        productos = response.json()

    return [
        {"id": p["id"], "name": p["name"], "price": p["price"]}
        for p in productos
        if p.get("price", 0) > min_price
    ]


if __name__ == "__main__":
    try:
        productos = get_expensive_products(token="TU_TOKEN")
        print(f"{len(productos)} productos con precio > $100")
        for p in productos:
            print(f"  [{p['id']}] {p['name']}: ${p['price']}")
    except httpx.HTTPError as err:
        print(f"Error de la API tras agotar reintentos: {err}")
```

**Decisiones de diseño:**

- **Backoff exponencial:** espera 2 s tras el primer fallo y 4 s tras el segundo (`2 ** intento`). En el tercer fallo relanza la excepción original en vez de envolverla, para que el caller pueda capturar el tipo exacto (`httpx.ReadTimeout`, `httpx.ConnectError`, etc.).
- **Solo se reintentan errores transitorios:** timeouts, errores de red y 5xx. Un `401` o `404` falla inmediatamente porque reintentar no cambiaría el resultado.
- **`p.get("price", 0)`:** los productos sin precio quedan excluidos del filtro en lugar de lanzar `KeyError`.
- **Timeout de 10 s por intento** (no total), lo cual es el comportamiento estándar.

**Notas opcionales:**

- `TimeoutException` y `NetworkError` son subclases de `httpx.TransportError`, así que `except httpx.TransportError:` sería equivalente y más compacto.
- Si la API envuelve la respuesta (p. ej. `{"products": [...]}`), ajusta la línea del `response.json()`.
- Para evitar tormentas de reintentos con múltiples clientes, puedes añadir jitter con stdlib: `time.sleep(2 ** intento + random.uniform(0, 1))`.