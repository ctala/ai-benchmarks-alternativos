# North Mini Code — code_generation/python_api_integration

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 7.68 | quality: 7.87
- latency_total: 24.775s | tokens_per_second: 59.1
- input_tokens: 94 | output_tokens: 1465

## Respuesta completa

```python
import time
from typing import List, Dict, Any
import httpx


def fetch_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_retries: int = 3,
) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos del API, filtra aquellos con precio > 100,
    y devuelve una lista de diccionarios con solo las claves id, name y price.

    Parámetros:
        token (str): Token de acceso Bearer.
        url (str): URL del endpoint de productos (por defecto el API dado).
        timeout (float): Tiempo máximo de espera para la solicitud en segundos.
        max_retries (int): Número máximo de reintentos tras fallos.

    Retorna:
        List[Dict[str, Any]]: Lista de productos filtrados.

    Levanta:
        httpx.RequestError: Si falla la solicitud después de todos los reintentos.
        httpx.HTTPStatusError: Si la respuesta del servidor indica un error (4xx/5xx).
        httpx.TimeoutException: Si la solicitud excede el tiempo de espera.
        ValueError: Si la respuesta no es un JSON válido o falta alguna clave necesaria.
    """
    for attempt in range(max_retries):
        try:
            # Se usa un cliente sincrónico; se podría cambiar a AsyncClient si se prefiere async
            with httpx.Client(timeout=timeout) as client:
                response = client.get(
                    url,
                    headers={"Authorization": f"Bearer {token}"},
                )
                response.raise_for_status()          # Levanta HTTPStatusError para códigos de error
                data = response.json()                # Puede levantar JSONDecodeError

                filtered = []
                for item in data:
                    # Aseguramos que item sea un diccionario y tenga las claves necesarias
                    if not isinstance(item, dict):
                        continue
                    price = item.get("price")
                    # Filtramos solo aquellos con precio > 100
                    if price is not None and price > 100:
                        filtered.append(
                            {
                                "id": item.get("id"),
                                "name": item.get("name"),
                                "price": price,
                            }
                        )
                return filtered

        except (httpx.RequestError, httpx.HTTPStatusError, httpx.TimeoutException) as e:
            # Si este es el último intento, propagamos el error
            if attempt == max_retries - 1:
                raise

            # Backoff exponencial: 2^attempt segundos
            backoff = 2 ** attempt
            time.sleep(backoff)

    # Nunca se alcanza aquí, pero por claridad
    raise RuntimeError("Se alcanzó el máximo número de reintentos sin éxito.")
```