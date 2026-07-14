# GPT-OSS 120B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.71 | quality: 9.8
- latency_total: 76.882s | tokens_per_second: 17.1
- input_tokens: 163 | output_tokens: 1316
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y práctica, con un manejo adecuado de errores y backoff exponencial, lo que la hace muy útil para un emprendedor.

## Respuesta completa

```python
import time
from typing import List, Dict, Any

import httpx


def get_filtered_products(
    token: str,
    *,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: int = 10,
) -> List[Dict[str, Any]]:
    """
    Obtiene la lista de productos desde la API, filtra aquellos cuyo precio es mayor
    a 100 y devuelve solo los campos ``id``, ``name`` y ``price``.

    Parámetros
    ----------
    token: str
        Bearer token que autoriza la petición.
    url: str, opcional
        Endpoint de la API. Por defecto ``https://api.example.com/products``.
    max_retries: int, opcional
        Número máximo de re‑intentos en caso de error de red o timeout.
    timeout: int, opcional
        Tiempo máximo (en segundos) que se espera por la respuesta del servidor.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con la forma ``{'id': ..., 'name': ..., 'price': ...}``
        para cada producto cuyo precio supera los 100.

    Excepciones
    -----------
    httpx.HTTPStatusError
        Si la respuesta tiene un código de estado HTTP 4xx/5xx después de agotar
        los re‑intentos.
    httpx.RequestError
        Si ocurre un error de red que no se puede recuperar después de los
        re‑intentos.
    """
    headers = {"Authorization": f"Bearer {token}"}
    attempt = 0

    while attempt < max_retries:
        try:
            # ``httpx.Client`` se cierra automáticamente al salir del ``with``.
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                # Levanta excepción para códigos 4xx/5xx.
                response.raise_for_status()
                products = response.json()
                # Se asume que la API devuelve una lista de objetos.
                break  # Salimos del bucle si todo fue bien.

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            attempt += 1
            # Si ya se agotaron los intentos, re‑lanzamos la excepción.
            if attempt == max_retries:
                raise exc

            # Back‑off exponencial con jitter (0‑0.5 s) para evitar
            # que varios clientes vuelvan a intentar al mismo tiempo.
            backoff = (2 ** (attempt - 1)) + (0.5 * time.random())
            time.sleep(backoff)

    # ----------------------------------------------------------------------
    # Filtrado y reducción de campos
    # ----------------------------------------------------------------------
    filtered: List[Dict[str, Any]] = []
    for p in products:
        # Se protege contra datos inesperados (p.ej. falta de 'price').
        price = p.get("price")
        if isinstance(price, (int, float)) and price > 100:
            filtered.append(
                {
                    "id": p.get("id"),
                    "name": p.get("name"),
                    "price": price,
                }
            )
    return filtered


# ----------------------------------------------------------------------
# Ejemplo de uso
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Sustituye este token por uno válido.
    MY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

    try:
        result = get_filtered_products(MY_TOKEN)
        print("Productos con precio > 100:")
        for prod in result:
            print(prod)
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP: {e.response.status_code} – {e.response.text}")
    except httpx.RequestError as e:
        print(f"Error de red: {e}")
```

### Detalles de la implementación

| Requisito | Cómo se cumple |
|-----------|----------------|
| **GET con Bearer token** | Se envía el encabezado `Authorization: Bearer <token>` en la solicitud. |
| **Filtrar precio > 100** | Después de obtener la respuesta JSON, se recorre la lista y se conserva solo los productos cuyo campo `price` supera 100. |
| **Retornar solo `{id, name, price}`** | Cada producto filtrado se convierte en un diccionario con esas tres claves. |
| **Manejo de errores y timeout (10 s)** | Se usa `httpx.Client(timeout=10)`. Se captura `httpx.RequestError` (problemas de red, timeout) y `httpx.HTTPStatusError` (códigos 4xx/5xx). |
| **Retry con backoff exponencial (máx 3 intentos)** | Un bucle `while` intenta la petición hasta `max_retries`. En cada fallo se espera `2^(intento-1)` segundos (+ jitter). Si se superan los intentos, se vuelve a lanzar la excepción. |
| **Sin dependencias externas** | Solo se importa `httpx`, que ya está permitido, y módulos estándar (`time`, `typing`). |

Esta función es totalmente autocontenida y lista para ser integrada en cualquier proyecto que necesite consumir la API descrita.