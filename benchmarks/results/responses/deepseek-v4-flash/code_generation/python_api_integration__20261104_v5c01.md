# DeepSeek V4 Flash (OpenRouter) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.48 | quality: 9.28
- latency_total: 54.808s | tokens_per_second: 58.4
- input_tokens: 110 | output_tokens: 3199
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

Aquí tienes la función solicitada, implementada con `httpx` y manejo de reintentos con backoff exponencial:

```python
import httpx
import time
from typing import List, Dict, Any


def get_filtered_products(token: str) -> List[Dict[str, Any]]:
    """
    Obtiene productos desde https://api.example.com/products usando autenticación Bearer,
    filtra aquellos con precio > 100 y devuelve una lista con los campos id, name y price.

    Args:
        token: Token Bearer para la autenticación.

    Returns:
        Lista de diccionarios con las claves 'id', 'name' y 'price'.

    Raises:
        httpx.HTTPStatusError: Si el servidor devuelve un código de error (4xx o 5xx).
        RuntimeError: Si se agotan los reintentos por fallos de red o timeout.
        ValueError: Si la respuesta no es una lista de productos.
    """
    url = "https://api.example.com/products"
    auth = httpx.BearerAuth(token)
    timeout = httpx.Timeout(10.0)
    max_retries = 3

    for attempt in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(url, auth=auth, timeout=timeout)
                response.raise_for_status()  # Lanza HTTPStatusError si código >= 400
                data = response.json()

                # Validar que la respuesta sea una lista
                if not isinstance(data, list):
                    raise ValueError("La respuesta del servidor no es una lista")

                # Filtrar productos con precio > 100 y quedarse solo con los campos requeridos
                filtered = [
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                    for item in data
                    if item.get("price", 0) > 100
                ]
                return filtered

        except httpx.HTTPStatusError:
            # Errores HTTP (4xx, 5xx) no se reintentan, se relanzan inmediatamente
            raise

        except (httpx.ConnectError, httpx.TimeoutException, httpx.RemoteProtocolError) as e:
            # Errores de red o timeout: se reintenta con backoff exponencial
            if attempt == max_retries - 1:
                raise RuntimeError(f"Fallo después de {max_retries} intentos: {e}")
            wait = 2 ** attempt  # 1, 2, 4 segundos
            time.sleep(wait)

        except Exception as e:
            # Cualquier otro error (JSON inválido, KeyError, etc.) se relanza
            raise e

    # Nunca debería llegar aquí, pero por seguridad se lanza una excepción
    raise RuntimeError("No se pudo completar la solicitud")
```

### Uso de ejemplo:
```python
if __name__ == "__main__":
    try:
        productos = get_filtered_products("mi_token_secreto")
        print(productos)
    except Exception as e:
        print(f"Error: {e}")
```

### Explicación del diseño:
- **Autenticación**: Se usa `httpx.BearerAuth` para mayor claridad.
- **Timeout**: 10 segundos configurado mediante `httpx.Timeout(10.0)`.
- **Reintentos**: Hasta 3 intentos, con espera exponencial de 1, 2 y 4 segundos entre fallos de red o timeout.
- **Manejo de errores**:
  - Errores HTTP (4xx, 5xx) se lanzan inmediatamente sin reintentar.
  - Errores de conexión, timeout o protocolo se reintentan; si se agotan, se lanza `RuntimeError`.
  - Otros errores (JSON inválido, estructura inesperada) se relanzan directamente.
- **Filtrado**: Solo se incluyen productos con `price > 100`, y se devuelve una lista de diccionarios con las claves `id`, `name` y `price`.

La función cumple con todos los requisitos especificados.