# Kimi K2.6 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.78 | quality: 9.08
- latency_total: 99.947s | tokens_per_second: 30.7
- input_tokens: 115 | output_tokens: 3068
- judge_score: 4.8 | justificación: 

## Respuesta completa

 ```python
import time
import httpx


def get_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos desde la API, filtra los de precio > 100 y retorna
    una lista simplificada con id, name y price.

    Incluye reintentos con backoff exponencial (máx. 3 intentos) para errores
    transitorios de red, timeout o HTTP 5xx. Timeout de petición: 10 s.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_retries = 3

    last_error = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                break  # Éxito, salimos del bucle de reintentos

        except (httpx.TimeoutException, httpx.NetworkError, httpx.ConnectError) as exc:
            # Errores de red / timeout → reintentar si quedan intentos
            last_error = exc
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Backoff exponencial: 1s, 2s, 4s
            continue

        except httpx.HTTPStatusError as exc:
            # Reintentar solo errores 5xx; 4xx se propagan de inmediato
            if exc.response.status_code >= 500 and attempt < max_retries - 1:
                last_error = exc
                time.sleep(2 ** attempt)
                continue
            raise

    else:
        # Se agotaron los reintentos sin éxito
        if last_error:
            raise last_error
        return []

    # Normalizar la respuesta: soporta lista directa o dict envolvente
    if isinstance(data, dict):
        products = data.get("products") or data.get("data") or []
    elif isinstance(data, list):
        products = data
    else:
        products = []

    # Filtrar y proyectar los campos solicitados
    result = []
    for product in products:
        if not isinstance(product, dict):
            continue
        try:
            price = product.get("price")
            if price is not None and price > 100:
                result.append({
                    "id": product["id"],
                    "name": product["name"],
                    "price": price,
                })
        except (KeyError, TypeError):
            # Omite productos mal formados
            continue

    return result
```

**Notas:**
*   Requiere únicamente `httpx` (`pip install httpx`).
*   El backoff exponencial espera `2^attempt` segundos entre reintentos (`1s`, `2s`, `4s`).
*   Errores de cliente HTTP (`4xx`) no se reintentan; se lanzan inmediatamente.
*   El timeout total de cada petición es de **10 segundos**.
*   La función es tolerante a estructuras envolventes (`{"products": [...]}`) o listas directas.