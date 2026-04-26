# GPT-OSS 120B (Ollama Cloud) — code_generation/python_api_integration

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 8.08 | quality: 9.52
- latency_total: 20.763s | tokens_per_second: 73.4
- input_tokens: 163 | output_tokens: 1523
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
"""
Módulo: product_api.py
---------------------------------
Implementa una llamada a la API de productos con:
    • autenticación Bearer token,
    • timeout de 10 s,
    • reintentos (máx. 3) con back‑off exponencial,
    • filtrado de productos cuyo precio sea > 100,
    • retorno de una lista de diccionarios con solo los campos
      {id, name, price}.
No se usan dependencias externas fuera de la librería estándar y `httpx`.
"""

import time
from typing import List, Dict, Any

import httpx


def get_expensive_products(
    token: str,
    *,
    url: str = "https://api.example.com/products",
    price_threshold: float = 100.0,
    timeout: float = 10.0,
    max_retries: int = 3,
    backoff_factor: float = 0.5,
) -> List[Dict[str, Any]]:
    """
    Recupera los productos de la API y devuelve solo aquellos cuyo precio
    supera ``price_threshold``.

    Parámetros
    ----------
    token: str
        Token JWT (Bearer) que se envía en el encabezado ``Authorization``.
    url: str, opcional
        Endpoint de la API. Por defecto ``https://api.example.com/products``.
    price_threshold: float, opcional
        Límite mínimo de precio para que un producto sea incluido.
    timeout: float, opcional
        Tiempo máximo (en segundos) que se espera por la respuesta HTTP.
    max_retries: int, opcional
        Número máximo de intentos (el primer intento + reintentos).
    backoff_factor: float, opcional
        Factor de crecimiento del back‑off exponencial.
        El tiempo de espera entre intentos será:
        ``backoff_factor * (2 ** (attempt-1))`` segundos.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de diccionarios con las claves ``id``, ``name`` y ``price``.

    Excepciones
    -----------
    httpx.HTTPStatusError
        Si la respuesta tiene un código de estado HTTP 4xx/5xx después de
        agotar los reintentos.
    httpx.RequestError
        Si ocurre un error de red (p.ej. DNS, conexión rechazada) después de
        agotar los reintentos.
    """
    headers = {"Authorization": f"Bearer {token}"}
    # Configuramos un timeout fijo (10 s) para la petición completa.
    client_timeout = httpx.Timeout(timeout)

    for attempt in range(1, max_retries + 1):
        try:
            # httpx se usa como cliente síncrono para mantener la API simple.
            with httpx.Client(timeout=client_timeout) as client:
                response = client.get(url, headers=headers)
                # Levanta HTTPStatusError para códigos 4xx/5xx
                response.raise_for_status()
                # Se asume que la API devuelve JSON con una lista bajo la clave
                # "products". Si la respuesta es directamente la lista, basta
                # con usar `response.json()`.
                data = response.json()
                # Normalizamos la estructura:
                products = data.get("products", data)   # admite ambos formatos
                # Filtramos y proyectamos los campos requeridos
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > price_threshold
                ]
                return result

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si es el último intento, re‑levantamos la excepción.
            if attempt == max_retries:
                raise
            # Sino, esperamos un tiempo exponencial y reintentamos.
            backoff = backoff_factor * (2 ** (attempt - 1))
            # Opcional: imprimir/loggear información de diagnóstico.
            print(
                f"Intento {attempt} falló ({type(exc).__name__}: {exc}). "
                f"Reintentando en {backoff:.1f}s..."
            )
            time.sleep(backoff)

    # Nunca debería llegar aquí porque el bucle siempre termina con
    # `return` o `raise`.
    return []


# ----------------------------------------------------------------------
# Ejemplo de uso (puedes comentar o eliminar esta sección en producción)
if __name__ == "__main__":
    # Reemplaza con un token válido.
    MY_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

    try:
        productos = get_expensive_products(MY_TOKEN)
        print(f"Se encontraron {len(productos)} productos > $100:")
        for p in productos:
            print(p)
    except httpx.HTTPStatusError as http_err:
        print(f"Error de la API: {http_err.response.status_code} - {http_err}")
    except httpx.RequestError as net_err:
        print(f"Error de red: {net_err}")
```

### Puntos clave del código

| Requisito | Implementación |
|-----------|-----------------|
| **GET con Bearer token** | `headers = {"Authorization": f"Bearer {token}"}` |
| **Timeout 10 s** | `httpx.Timeout(timeout)` (valor por defecto = 10 s) |
| **Filtrar `price > 100`** | List‑comprehension que verifica `p.get("price", 0) > price_threshold` |
| **Retornar `{id, name, price}`** | Se construye un nuevo diccionario con solo esas claves |
| **Manejo de errores de red / timeout** | Captura `httpx.RequestError` (incluye `ConnectTimeout`, `ReadTimeout`, etc.) |
| **Retry con back‑off exponencial** | Bucle `for attempt in range(1, max_retries+1)` con `time.sleep(backoff_factor * 2**(attempt-1))` |
| **Sin dependencias externas** | Sólo `httpx` (ya solicitado) + librería estándar (`time`, `typing`) |

Esta función es totalmente autónoma, tipada y lista para ser importada en cualquier proyecto que necesite consultar la API de productos bajo los requisitos especificados.