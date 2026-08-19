# Sakana Namazu — code_generation/python_api_integration

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.96 | quality: 8.96
- latency_total: 8.896s | tokens_per_second: 230.2
- input_tokens: 190 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

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

El usuario quiere una función Python con requisitos específicos:
1. GET a https://api.example.com/products con Bearer token
2. Filtrar productos con precio > 100
3. Retornar lista de dicts con {id, name, price}
4. Manejar errores de red y timeout (10 segundos)
5. Incluir retry con backoff exponencial (máximo 3 intentos)
6. Usar httpx sin dependencias externas adicionales

Debo escribir código Python limpio y funcional. Como httpx ya tiene capacidades de retry limitadas (o ninguna built-in avanzada), debo implementar el retry manualmente con backoff exponencial. No puedo usar librerías externas como tenacity según las instrucciones.

Aspectos a considerar:
- Usar `httpx` (síncrono o asíncrono? El usuario no especificó, pero por simplicidad y dado que no mencionó async, usaré la versión síncrona, aunque podría ofrecer ambas. Mejor la síncrona para uso general).
- Timeout de 10 segundos: `timeout=10.0` en httpx.
- Bearer token: pasar en headers `Authorization: Bearer <token>`.
- Backoff exponencial: intento 1 (sin espera o espera 0), intento 2 (espera 2^1 * base?), intento 3 (espera 2^2 * base?). Generalmente backoff exponencial entre intentos. Máximo 3 intentos significa que si falla 3 veces, se rinde.
- Errores de red: capturar `httpx.NetworkError`, `httpx.TimeoutException`, `httpx.HTTPStatusError` (si chequeamos status), etc.
- Filtrar: asumir que la respuesta es una lista de dicts o un dict con una clave tipo "products". Debo decidir. Es más robusto asumir que es una lista directa, o manejar ambos casos. Voy a asumir que retorna JSON con una lista. Quizás la respuesta sea `{"products": [...]}` o directamente `[...]`. Mejor hacer la función flexible o asumir que es una lista. Para ser más realista, podría asumir que retorna una lista o un dict con "products". Pero para simplificar, asumiré que la respuesta es una lista de productos o un diccionario con una clave `products`. Mejor aún, verificaré si es lista, si no, buscaré una clave común.
- Retornar lista de dicts: proyectar solo id, name, price.

Estructura del código:
```python
import httpx
import time

def get_expensive_products(token: str, base_url: str = "https://api.example.com") -> list[dict]:
    url = f"{base_url}/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    
    max_retries = 3
    retry_delay = 1  # segundos base para backoff
    
    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                # Manejar posible estructura anidada
                products = data if isinstance(data, list) else data.get("products", [])
                
                result = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if p.get("price", 0) > 100
                ]
                return result
                
        except httpx.TimeoutException:
            if attempt == max_retries:
                raise Exception("Timeout al obtener productos tras 3 intentos")
        except httpx.NetworkError:
            if attempt == max_retries:
                raise Exception("Error de red al obtener productos tras 3 intentos")
        except httpx.HTTPStatusError as e:
            if attempt == max_retries:
                raise Exception(f"Error HTTP {e.response.status_code} tras 3 intentos")
        except Exception as e:
            if attempt == max_retries:
                raise Exception(f"Error inesperado: {e}")
        
        if attempt < max_retries:
            sleep_time = retry_delay * (2 ** (attempt - 1))
            time.sleep(sleep_time)
    
    return []  # nunca debería llegar aquí
```

Espera, el usuario quiere "maneje errores", no necesariamente que relance excepciones al final. Pero es buena práctica. También podría retornar lista vacía en caso de error. Sin embargo, es mejor dejar que la excepción se propague después del último intento, o retornar []. El usuario dice "Maneje errores de red y timeout". Podría interpretarse como que no debe crashear el programa. Quizás retornar lista vacía o relanzar una excepción custom. Voy a hacer que capture las excepciones y tras el último intento retorne una lista vacía o relance. Creo que es más útil que imprima el error y retorne `[]` para no romper el flujo, o mejor aún, dejar que la última excepción se propague para que el llamador sepa qué pasó. Haré que propague la última excepción envuelta en un `RuntimeError` o similar.

Mejor estructura:
- Usar `typing` para type hints.
- Exponer la función claramente.
- Hacerla más robusta: manejar que los campos id/name/price puedan faltar con `.get()` para evitar KeyError, o dejar que falle si el formato es incorrecto? Normalmente si falta un campo es un error del API. Usaré acceso directo pero dentro del bloque try, así que un KeyError sería capturado por el except Exception general si ocurre.

Refinando el código:

```python
import httpx
import time

def fetch_expensive_products(token: str) -> list[dict]:
    """
    Obtiene productos con precio > 100 desde api.example.com.
    Incluye retry con backoff exponencial y manejo de timeouts/red.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    max_attempts = 3
    base_delay = 1  # segundo

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                # Soportar tanto lista directa como {"products": [...]}
                products = data if isinstance(data, list) else data.get("products", [])

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

        except httpx.TimeoutException as exc:
            if attempt == max_attempts:
                raise RuntimeError(f"Timeout tras {max_attempts} intentos: {exc}") from exc
        except httpx.NetworkError as exc:
            if from excattempt == max_attempts:
                raise RuntimeError(f"Error de red tras {max_attempts} intentos: {exc}") from exc
        except httpx.HTTPStatusError as exc:
            if attempt == max_attempts:
                raise RuntimeError(f"Error HTTP tras {max_attempts} intentos: {exc.response.status_code}") from exc
        except Exception as exc:
            # Errores de parsing JSON o de estructura
            if attempt == max_attempts:
                raise RuntimeError(f"Error inesperado tras {max_attempts} intentos: {exc}") from exc

        # Backoff exponencial: 1s, 2s, 4s... pero solo entre intentos
        if attempt < max_attempts:
            backoff = base_delay * (2 ** (attempt - 1))
            time.sleep(backoff)

    # Por seguridad, aunque nunca debería llegar aquí
    return []
```

Hay un error tipográfico en mi borrador: `if from excattempt == max_attempts`. Debo corregir eso.

También podría mejorarse usando un contexto más limpio. Y quizás el usuario prefiere que sea "copiar y pegar" listo.

Otra consideración: `httpx.HTTPStatusError` se lanza solo si llamamos `raise_for_status()`. El usuario pidió manejar errores de red y timeout. Los errores HTTP (4xx/5xx) no son errores de red, pero es bueno manejarlos también. Si quiero ser estricto, podría no hacer raise_for_status()