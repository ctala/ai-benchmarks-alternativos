# North Mini Code — code_generation/python_api_integration

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 7.53 | quality: 7.87
- latency_total: 26.558s | tokens_per_second: 35.6
- input_tokens: 94 | output_tokens: 946

## Respuesta completa

```python
import time
from typing import List, Dict, Any
import httpx

def fetch_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos desde la API, filtra aquellos con precio > 100
    y devuelve solo id, name y price.

    Args:
        bearer_token (str): Token de autenticación Bearer.

    Returns:
        List[Dict[str, Any]]: Una lista de productos filtrados.

    Raises:
        httpx.HTTPStatusError: Si el servidor devuelve un código de error (4xx/5xx).
        httpx.RequestError: Si falla la solicitud tras todos los reintentos
            (error de red, timeout, etc.).
    """
    URL = "https://api.example.com/products"
    MAX_ATTEMPTS = 3
    TIMEOUT = 10  # segundos

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with httpx.Client(timeout=TIMEOUT) as client:
                response = client.get(URL, headers=headers)
                response.raise_for_status()          # raise for 4xx/5xx
                products = response.json()

                # Validar que sea una lista (la API debería devolver una)
                if not isinstance(products, list):
                    raise ValueError("Respuesta inesperada: se esperaba una lista")

                # Filtrar y seleccionar solo los campos necesarios
                filtered = [
                    {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]

                return filtered

        except (httpx.NetworkError, httpx.TimeoutException) as exc:
            # Errores recuperables: reintentar con backoff exponencial
            if attempt == MAX_ATTEMPTS:
                raise httpx.RequestError(
                    f"Fallo tras {MAX_ATTEMPTS} intentos: {exc}"
                ) from exc

            delay = 2 ** (attempt - 1)  # 1 s, 2 s, 4 s
            time.sleep(delay)

    # El bucle siempre termina en raise, pero lo mantenemos para el linter
    raise httpx.RequestError("Se agotaron los intentos")
```