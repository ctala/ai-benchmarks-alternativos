# Nemotron 3 Nano 30B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 13.331s | tokens_per_second: 92.6
- input_tokens: 118 | output_tokens: 1235
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict

API_URL = "https://api.example.com/products"
TOKEN   = "YOUR_BEARER_TOKEN"          # <-- reemplaza con tu token real
MAX_RETRIES = 3
TIMEOUT_SECONDS = 10                   # timeout de la petición HTTP
BASE_BACKOFF = 0.5                     # segundos (se eleva al cuadrado en cada re‑intento)


def get_expensive_products() -> List[Dict[str, float]]:
    """
    Realiza una petición GET a ``https://api.example.com/products`` con
    autenticación Bearer, filtra los productos cuyo precio sea > 100 y
    devuelve una lista de diccionarios con la forma ``{ "id": ..., "name": ..., "price": ... }``.

    La función incluye:
      * manejo de errores de red y de tiempo de espera,
      * reintentos con back‑off exponencial (máximo 3 intentos).

    Returns
    -------
    List[Dict[str, float]]
        Lista de productos que cumplen la condición de precio.
    """
    headers = {"Authorization": f"Bearer {TOKEN}"}

    # Parámetros de back‑off exponencial
    backoff = BASE_BACKOFF
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # 1️⃣  Petición GET con timeout y autenticación
            response = httpx.get(
                API_URL,
                headers=headers,
                timeout=TIMEOUT_SECONDS,
            )
            # 2️⃣  Si la respuesta no es 2xx lanzamos un error para que sea capturado
            response.raise_for_status()

            # 3️⃣  Filtrado y transformación de la respuesta JSON
            products = response.json()                     # se espera que la API devuelva una lista de dicts
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]
            return filtered

        # 4️⃣  Captura de errores de red / timeout / HTTP no exitoso
        except (httpx.RequestError, httpx.TimeoutException, httpx.HTTPStatusError) as exc:
            # Si es el último intento, volvemos a lanzar la excepción
            if attempt == MAX_RETRIES:
                raise RuntimeError(
                    f"Falló la petición después de {MAX_RETRIES} intentos: {exc}"
                ) from exc

            # Esperamos con back‑off antes del siguiente intento
            print(
                f"Intento {attempt} falló ({exc}). Reintentando en {backoff:.2f}s..."
            )
            time.sleep(backoff)
            backoff *= 2   # exponencial (0.5 → 1 → 2 → 4 …)

    # Esta línea nunca se alcanza porque siempre devolvemos o lanzamos dentro del bucle
    return []


# ----------------------------------------------------------------------
# Ejemplo de uso (descomenta para probar)
# ----------------------------------------------------------------------
# if __name__ == "__main__":
#     try:
#         result = get_expensive_products()
#         print("Productos > 100:", result)
#     except Exception as e:
#         print("Error:", e)
```

### Explicación rápida de los puntos solicitados
| Requisito | Implementación |
|-----------|----------------|
| **1. GET con Bearer token** | `httpx.get(API_URL, headers={"Authorization": f"Bearer {TOKEN}"})` |
| **2. Filtrar precio > 100** | List‑comprehension `if p.get("price", 0) > 100` |
| **3. Retornar solo `{id, name, price}`** | La comprensión construye exactamente esos campos |
| **4. Manejo de errores y timeout (10 s)** | `timeout=TIMEOUT_SECONDS` en `httpx.get` y captura de `httpx.RequestError`, `httpx.TimeoutException`, `httpx.HTTPStatusError` |
| **5. Retry con backoff exponencial (máx 3 intentos)** | Bucle `for attempt in range(1, MAX_RETRIES+1)` con `time.sleep(backoff)` y `backoff *= 2` |

> **Nota:** La función asume que la respuesta JSON contiene una lista de objetos con al menos los campos `id`, `name` y `price`. Si la API devuelve un formato diferente, basta ajustar la extracción dentro de la comprensión. No se usan dependencias externas más allá de `httpx` y la biblioteca estándar.