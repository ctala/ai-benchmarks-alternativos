# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/python_api_integration

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.01 | quality: 9.44
- latency_total: 9.985s | tokens_per_second: 150.3
- input_tokens: 118 | output_tokens: 1501
- judge_score: 4.6 | justificación: 

## Respuesta completa

```python
import time
from typing import List, Dict, Any

import httpx

# ----------------------------------------------------------------------
# Configuración
# ----------------------------------------------------------------------
API_URL = "https://api.example.com/products"
BEARER_TOKEN = "<YOUR_BEARER_TOKEN>"          # <-- pon aquí tu token
TIMEOUT = 10.0                                 # segundos
MAX_RETRIES = 3
BASE_BACKOFF = 1.0                             # segundos (se duplica en cada intento)


def _request_with_retry(token: str) -> httpx.Response:
    """
    Realiza la petición GET con reintentos exponenciales.
    - token: token Bearer de autenticación.
    - devuelve la respuesta (httpx.Response) si tiene éxito.
    - lanza excepción si después de MAX_RETRIES sigue fallando.
    """
    client = httpx.Client(timeout=TIMEOUT)   # timeout global de 10 s
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.get(API_URL, headers=headers)
            # Si el código HTTP es 2xx consideramos la petición exitosa.
            if response.status_code >= 200 and response.status_code < 300:
                return response
            # Para otros códigos (p.e. 401, 404, 500…) también reintentamos.
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            # Errores de red o timeout → reintentamos.
            pass

        # Si llegamos aquí, la petición no fue exitosa → esperamos antes de reintentar
        if attempt < MAX_RETRIES:
            sleep_time = BASE_BACKOFF * (2 ** (attempt - 1))   # 1, 2, 4 …
            time.sleep(sleep_time)

    # Si después de los intentos no se obtuvo una respuesta válida → error
    raise RuntimeError(
        f"Failed to obtain a successful response after {MAX_RETRIES} attempts."
    )


def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuya precio sea > 100 y devuelve una lista de diccionarios
    con solo los campos `id`, `name` y `price`.

    Parámetros
    ----------
    token: str
        Token de autenticación Bearer.

    Retorna
    -------
    List[Dict[str, Any]]
        Lista de productos filtrados. Cada elemento tiene la forma:
        {"id": <id>, "name": <name>, "price": <price>}.

    Excepciones
    -----------
    RuntimeError
        Si después de los reintentos no se puede obtener la respuesta.
    ValueError
        Si la respuesta JSON no contiene los campos esperados.
    """
    # 1️⃣  Realizamos la petición con reintentos
    response = _request_with_retry(token)

    # 2️⃣  Parseamos el JSON
    try:
        products = response.json()
    except ValueError as exc:
        raise RuntimeError("Respuesta no es JSON válido.") from exc

    # 3️⃣  Filtramos y transformamos
    result = []
    for prod in products:
        # Se asume que cada producto tiene al menos los campos id, name y price.
        if isinstance(prod.get("price"), (int, float)) and prod["price"] > 100:
            result.append(
                {
                    "id": prod["id"],
                    "name": prod["name"],
                    "price": prod["price"],
                }
            )

    return result


# ----------------------------------------------------------------------
# Ejemplo de uso (puedes eliminarlo en producción)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    try:
        expensive = fetch_expensive_products(BEARER_TOKEN)
        print("Productos > 100 €:")
        for p in expensive:
            print(p)
    except Exception as e:
        print(f"Error: {e}")
```

### Explicación rápida
1. **Petición GET** – Se usa `httpx.Client` con un *timeout* de 10 s.  
2. **Retry con backoff exponencial** – Se intentan hasta 3 veces. El tiempo de espera entre intentos es `1 s, 2 s, 4 s`.  
3. **Manejo de errores** – Captura `RequestError` y `TimeoutException`; cualquier otro código HTTP distinto de 2xx también provoca un reintento. Si después de los reintentos falla, se lanza `RuntimeError`.  
4. **Filtrado** – Sólo se conservan los productos cuya clave `price` sea numérica y mayor que 100.  
5. **Salida** – Cada producto se devuelve como `{"id": ..., "name": ..., "price": ...}` dentro de una lista.  

Todo el código usa únicamente la librería estándar (`time`, `typing`) y **httpx**, cumpliendo con la restricción de “no dependencias externas adicionales”.