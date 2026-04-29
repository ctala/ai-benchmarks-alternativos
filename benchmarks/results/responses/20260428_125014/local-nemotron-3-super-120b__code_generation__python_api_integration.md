# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — code_generation/python_api_integration

- model_id: `nemotron-3-super:120b`
- success: True  | final: 7.33 | quality: 9.24
- latency_total: 67.326s | tokens_per_second: 18.4
- input_tokens: 118 | output_tokens: 1238
- judge_score: 4.6 | justificación: 

## Respuesta completa

```python
import time
from typing import List, Dict, Any

import httpx


def fetch_expensive_products(
    bearer_token: str,
    url: str = "https://api.example.com/products",
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_factor: float = 0.5,
) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos desde una API protegida con token Bearer,
    filtra aquellos cuyo precio es mayor a 100 y devuelve solo los campos
    ``id``, ``name`` y ``price``.

    Parámetros
    ----------
    bearer_token: str
        Token de autorización Bearer.
    url: str, opcional
        Endpoint de la API (por defecto ``https://api.example.com/products``).
    timeout: float, opcional
        Tiempo máximo (en segundos) para cada petición HTTP.
    max_retries: int, opcional
        Número máximo de intentos (incluyendo el primero) antes de fallar.
    backoff_factor: float, opcional
        Factor base para el backoff exponencial (segundos). El retraso entre
        intentos será ``backoff_factor * (2 ** retry_number)``.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price`` de
        los productos cuyo precio > 100.

    Excepciones
    -----------
    httpx.RequestError
        Si después de todos los reintentos persiste un error de red o timeout.
    httpx.HTTPStatusError
        Si la respuesta tiene un código de estado 4xx/5xx y no se puede
        recuperarse con reintentos.
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    attempt = 0

    while attempt < max_retries:
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Lanzará excepción para códigos 4xx/5xx
                response.raise_for_status()
                data = response.json()

                # Asumimos que la API devuelve una lista de productos
                if not isinstance(data, list):
                    raise ValueError("La respuesta esperada era una lista de productos")

                # Filtramos y proyectamos solo los campos requeridos
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in data
                    if isinstance(p, dict)
                    and p.get("price") is not None
                    and float(p["price"]) > 100
                ]
                return result

        except (httpx.TimeoutException, httpx.RequestError) as exc:
            # Error de red o timeout → reintentamos con backoff
            attempt += 1
            if attempt >= max_retries:
                raise  # re‑lanzamos la excepción última
            delay = backoff_factor * (2 ** (attempt - 1))
            time.sleep(delay)

        except httpx.HTTPStatusError as exc:
            # Errores HTTP 4xx/5xx: no reintentamos salvo que sea 5xx y queden intentos
            if 500 <= exc.response.status_code < 600 and attempt < max_retries - 1:
                attempt += 1
                delay = backoff_factor * (2 ** (attempt - 1))
                time.sleep(delay)
                continue
            raise

    # Nunca se llega aquí porque el bucle lanza o retorna antes
    raise RuntimeError("Lógica de reintentos inesperada")
```

### Uso rápido

```python
if __name__ == "__main__":
    TOKEN = "tu_bearer_token_aquí"
    try:
        caros = fetch_expensive_products(TOKEN)
        print("Productos > 100:", caros)
    except Exception as e:
        print(f"Falló la petición: {e}")
```

**Puntos clave**

* **Autenticación Bearer** – se incluye en el header `Authorization`.
* **Timeout de 10 s** – pasado a `httpx.Client(timeout=...)`.
* **Reintentos con backoff exponencial** – hasta 3 intentos, esperando  
  `0.5 s, 1.0 s, 2.0 s` entre ellos (ajustable con `backoff_factor`).
* **Manejo de errores** – captura `httpx.TimeoutException`, `httpx.RequestError` y, para códigos 5xx, también reintenta.
* **Filtrado y proyección** – solo se devuelven los campos `id`, `name` y `price` de los productos cuyo precio supera 100.  

No se requieren dependencias externas além de `httpx`. ¡Listo para usar!