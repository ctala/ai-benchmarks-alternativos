# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — code_generation/python_api_integration

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 7.63 | quality: 9.52
- latency_total: 22.058s | tokens_per_second: 65.4
- input_tokens: 119 | output_tokens: 1443
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
from typing import List, Dict, Any
import httpx

def get_expensive_products(
    url: str = "https://api.example.com/products",
    bearer_token: str = "",
    *,
    timeout: float = 10.0,
    max_retries: int = 3,
) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuya precio sea mayor a 100.

    1️⃣  Hace un GET a ``url`` con autenticación por token Bearer.  
    2️⃣  Filtra los productos cuyo campo ``price`` sea > 100.  
    3️⃣  Devuelve una lista de diccionarios con solo ``id``, ``name`` y ``price``.  
    4️⃣  Captura errores de red, timeout y códigos de respuesta no‑OK.  
    5️⃣  Reintenta la petición con back‑off exponencial (máximo 3 intentos).

    Parámetros
    ----------
    url : str
        Endpoint a consultar.
    bearer_token : str
        Token de autorización (Bearer <token>).
    timeout : float, opcional
        Tiempo máximo de espera por petición (segundos). Por defecto 10 s.
    max_retries : int, opcional
        Número máximo de reintentos. Por defecto 3.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista con los campos ``id``, ``name`` y ``price`` de los productos
        que cumplen el criterio de precio.
    """
    # Cabeceras que necesita la API
    headers = {"Authorization": f"Bearer {bearer_token}"}

    # Cliente HTTP con timeout global
    client = httpx.Client(timeout=timeout)

    for attempt in range(1, max_retries + 1):
        try:
            response = client.get(url, headers=headers)
            # Si llegamos aquí, la petición se completó (aunque el código HTTP pueda ser 4xx/5xx)
            response.raise_for_status()                     # lanza HTTPError para códigos >=400
            # Suponemos que la respuesta es JSON con una lista de productos
            products = response.json()
        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Error de red, timeout o código de estado no válido
            if attempt == max_retries:
                # Último intento: propagamos la excepción para que el llamador la maneje
                raise RuntimeError(f"Failed to fetch products after {max_retries} attempts") from exc
            # Esperamos antes del reintento (back‑off exponencial + pequeño jitter)
            sleep_time = (2 ** (attempt - 1)) + (time.time() % 0.5)   # jitter < 0.5 s
            print(f"[Retry {attempt}/{max_retries}] Error: {exc}. Reintentando en {sleep_time:.2f}s...")
            time.sleep(sleep_time)
            continue

        # Si llegamos aquí, la respuesta es válida (200 OK)
        # Filtramos y transformamos
        result = [
            {"id": p["id"], "name": p["name"], "price": p["price"]}
            for p in products
            if isinstance(p, dict) and p.get("price", 0) > 100
        ]
        return result

    # Nunca debería llegar aquí, pero por completitud:
    raise RuntimeError("Unexpected exit from retry loop")
```

### Explicación rápida de los puntos solicitados

| # | Requisito | Cómo se implementa |
|---|-----------|--------------------|
| 1 | GET a `https://api.example.com/products` con token Bearer | `client.get(url, headers={"Authorization": f"Bearer {bearer_token}"})` |
| 2 | Filtrar productos con `price > 100` | List‑comprehension con `if p.get("price", 0) > 100` |
| 3 | Devolver lista de dicts `{id, name, price}` | Cada elemento de la lista resultante contiene exactamente esos tres campos |
| 4 | Manejo de errores de red y timeout (10 s) | `httpx.RequestError` y `httpx.HTTPStatusError` se capturan; el cliente se crea con `timeout=10.0` |
| 5 | Retry con back‑off exponencial (máx 3 intentos) | Bucle `for attempt in range(1, max_retries+1)`, espera `2**(attempt-1)` segundos + jitter; si se agotan los intentos se lanza una excepción |

**Uso de ejemplo**

```python
if __name__ == "__main__":
    try:
        productos_caros = get_expensive_products(
            bearer_token="mi-token-secreto",
            timeout=10,
            max_retries=3,
        )
        print("Productos > 100:", productos_caros)
    except Exception as e:
        print("Error al obtener los datos:", e)
```

La función solo depende de **httpx** (sin librerías externas adicionales) y cumple con todos los requisitos especificados.