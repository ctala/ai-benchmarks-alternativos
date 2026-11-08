# Nemotron 3 Nano 30B — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.8 | quality: 9.52
- latency_total: 14.045s | tokens_per_second: 94.4
- input_tokens: 118 | output_tokens: 1326
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


```python
import httpx
import time
from typing import List, Dict

API_URL = "https://api.example.com/products"
BEARER_TOKEN = "TU_BEARER_TOKEN_AQUI"          # <-- pon aquí tu token
MAX_RETRIES = 3
BASE_BACKOFF = 1.0                            # segundos (se duplica en cada reintento)
TIMEOUT = 10.0                                # segundos


def get_expensive_products() -> List[Dict]:
    """
    Obtiene de la API todos los productos cuyo precio sea > 100
    y devuelve una lista de diccionarios con solo los campos
    ``id``, ``name`` y ``price``.

    La función:
    * Usa autenticación Bearer.
    * Aplica un timeout de 10 s.
    * Reintenta hasta 3 veces con back‑off exponencial (1 s, 2 s, 4 s).
    * Captura errores de red y los devuelve como lista vacía
      (puedes modificar el comportamiento a tu gusto).

    Returns
    -------
    List[Dict]
        Lista de productos filtrados, por ejemplo:
        [
            {"id": "p123", "name": "Widget Pro", "price": 150.0},
            ...
        ]
    """
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    params = {}                                   # si la API necesita query‑string, añádelo aquí

    # ----------  Retry con back‑off exponencial ----------
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = httpx.get(
                API_URL,
                headers=headers,
                params=params,
                timeout=TIMEOUT,
            )
            response.raise_for_status()          # lanza excepción si el código >=400
            data = response.json()               # se asume que la respuesta es JSON

            # ----------  Filtrado ----------
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if p.get("price", 0) > 100
            ]

            return filtered

        # ----------  Manejo de errores ----------
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            # Errores de red / timeout
            if attempt == MAX_RETRIES:
                # Último intento → devolvemos lista vacía y opcionalmente loggeamos
                print(f"[get_expensive_products] Error de red o timeout después de {attempt} intentos: {exc}")
                return []
            else:
                # Esperamos antes del siguiente reintento
                backoff = BASE_BACKOFF * (2 ** (attempt - 1))
                print(f"[get_expensive_products] Intento {attempt} falló ({exc}). Reintentando en {backoff:.1f}s...")
                time.sleep(backoff)

        except httpx.HTTPStatusError as exc:
            # Errores HTTP (p.ej. 500, 404) – normalmente no se reintentan,
            # pero se puede decidir según el código.
            print(f"[get_expensive_products] Error HTTP {exc.response.status_code}: {exc}")
            return []

    # Si llegamos aquí, todos los reintentos fallaron
    return []


# ----------------------------------------------------------------------
# Ejemplo de uso (descomenta si lo ejecutas como script independiente)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    productos = get_expensive_products()
    if productos:
        for p in productos:
            print(p)
    else:
        print("No se obtuvieron productos o hubo un error.")
```

### Detalles clave

| Requisito | Implementación |
|-----------|----------------|
| **GET a `https://api.example.com/products` con Bearer** | `headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}` y `httpx.get(API_URL, headers=headers, ...)` |
| **Filtrar precio > 100** | List‑comprehension con `if p.get("price", 0) > 100` |
| **Retornar `{id, name, price}`** | Cada elemento del list‑comprehension contiene exactamente esos tres campos |
| **Manejo de errores de red y timeout (10 s)** | `httpx.get(..., timeout=TIMEOUT)` y captura `httpx.RequestError` / `httpx.TimeoutException` |
| **Retry con backoff exponencial (máx 3 intentos)** | Bucle `for attempt in range(1, MAX_RETRIES + 1)` con `backoff = BASE_BACKOFF * (2 ** (attempt - 1))` |
| **Solo `httpx`** | No se usan otras librerías externas; todo está basado en la API estándar de `httpx` |

Puedes copiar esta función tal cual en tu proyecto. Sólo reemplaza `TU_BEARER_TOKEN_AQUI` por el token real y, si la API requiere parámetros de consulta, añádelos en `params`. ¡Listo! 🚀