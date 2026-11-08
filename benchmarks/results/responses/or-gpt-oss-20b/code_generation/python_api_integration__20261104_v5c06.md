# GPT-OSS 20B — code_generation/python_api_integration

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.89 | quality: 9.48
- latency_total: 9.177s | tokens_per_second: 98.5
- input_tokens: 150 | output_tokens: 904
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
from typing import List, Dict, Any

def fetch_expensive_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene los productos cuyo precio es mayor a 100 desde la API
    https://api.example.com/products.

    Parámetros
    ----------
    token: str
        Token de autenticación Bearer.

    Retorna
    -------
    List[Dict[str, Any]]
        Una lista de diccionarios con las claves ``id``, ``name`` y ``price``.

    Excepciones
    -----------
    RuntimeError
        Si después de 3 intentos la petición sigue fallando (red, timeout,
        o cualquier error de httpx) se levanta un RuntimeError con el mensaje
        correspondiente.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)          # 10 s de timeout
    max_attempts = 3                       # máximo de intentos
    backoff_factor = 1.0                   # segundos de base

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()          # lanza si código 4xx/5xx

                data = response.json()
                # Se espera que la respuesta sea un iterable de objetos producto.
                # Cada objeto debe contener al menos las claves id, name y price.
                results = []
                for product in data:
                    try:
                        price = product.get("price")
                        if price is not None and price > 100:
                            results.append({
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price
                            })
                    except Exception:
                        # Si alguna clave falta o el valor no es numérico, se ignora el producto.
                        continue
                return results

        except (httpx.RequestError, httpx.HTTPError) as exc:
            # Si no es el último intento, esperar antes de reintentar
            if attempt == max_attempts:
                raise RuntimeError(
                    f"No se pudo obtener los productos después de "
                    f"{max_attempts} intentos: {exc}"
                ) from exc
            else:
                sleep_time = backoff_factor * (2 ** (attempt - 1))
                time.sleep(sleep_time)
                continue  # reintentar
```

### Cómo usar

```python
if __name__ == "__main__":
    TOKEN = "tu_token_aquí"
    try:
        productos = fetch_expensive_products(TOKEN)
        print(productos)
    except RuntimeError as err:
        print(f"Error: {err}")
```

**Notas importantes**

1. **httpx** es la única librería externa que se importa, cumpliendo con la restricción.
2. Se manejan tanto errores de red (`RequestError`) como problemas HTTP (`HTTPError`), y se aplica un `timeout` de 10 s.
3. Se implementa reintento con *exponential backoff*: 1 s, 2 s, 4 s entre intentos.
4. Si después de 3 intentos sigue fallando, se lanza un `RuntimeError` con la causa original para que el llamador pueda decidir qué hacer.