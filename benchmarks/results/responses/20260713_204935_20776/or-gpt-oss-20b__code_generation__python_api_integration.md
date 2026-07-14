# GPT-OSS 20B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.2 | quality: 9.72
- latency_total: 8.637s | tokens_per_second: 139.3
- input_tokens: 161 | output_tokens: 1203
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import Any, Dict, List, Optional

import httpx


def fetch_expensive_products(
    token: str,
    *,
    url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_attempts: int = 3,
    backoff_factor: float = 1.0,
) -> List[Dict[str, Any]]:
    """
    Obtiene los productos de la API y devuelve solo los que tienen un precio mayor a `price_threshold`.

    Parameters
    ----------
    token : str
        Bearer token de autenticación.
    url : str
        Endpoint de la API. Por defecto es ``https://api.example.com/products``.
    price_threshold : float
        Precio mínimo que un producto debe superar para ser incluido.
    timeout : float
        Timeout (en segundos) de la petición HTTP. Por defecto 10 s.
    max_attempts : int
        Número máximo de intentos en caso de error de red. Por defecto 3.
    backoff_factor : float
        Factor de back‑off exponencial. El tiempo de espera entre intentos será
        ``backoff_factor * 2**(attempt-1)``.
    Returns
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price``.
    Raises
    ------
    httpx.HTTPStatusError
        Si la respuesta HTTP tiene un código de estado distinto de 200.
    httpx.RequestError
        Si todos los intentos fallan por error de red o timeout.
    """
    headers = {"Authorization": f"Bearer {token}"}
    attempt = 0

    while attempt < max_attempts:
        attempt += 1
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                resp.raise_for_status()  # Levanta en 4xx/5xx

            # Suponemos que la respuesta es JSON y es una lista de objetos producto
            products = resp.json()
            if not isinstance(products, list):
                raise ValueError("La respuesta no es una lista de productos")

            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if isinstance(p.get("price"), (int, float)) and p["price"] > price_threshold
            ]
            return filtered

        except (httpx.HTTPError, httpx.RequestError, ValueError) as exc:
            # Si no podemos seguir intentando, abortamos
            if attempt == max_attempts:
                raise

            # Tiempo de espera antes del siguiente intento
            sleep_time = backoff_factor * (2 ** (attempt - 1))
            time.sleep(sleep_time)

            # Continuamos con el siguiente intento
            continue


# ------------------------------------------------------------------
# Ejemplo de uso
# ------------------------------------------------------------------
if __name__ == "__main__":
    API_TOKEN = "tu_token_aquí"

    try:
        productos = fetch_expensive_products(API_TOKEN)
        for p in productos:
            print(f'{p["name"]} ({p["id"]}) - ${p["price"]}')
    except httpx.RequestError as e:
        print(f"Error al conectar con la API: {e}")
    except httpx.HTTPStatusError as e:
        print(f"Respuesta inesperada ({e.response.status_code}): {e}")
```

**Puntos clave del código**

1. **httpx** se usa para hacer la petición GET con un timeout de 10 s.
2. El header `Authorization` lleva el token en formato Bearer.
3. Se filtra la lista de productos recibida, manteniendo solo los con `price > 100`.
4. Se implementa un retry con back‑off exponencial (`1, 2, 4` s entre intentos) y máximo 3 intentos.
5. Se levanta una excepción si todos los intentos fallan o si la respuesta no es la esperada.