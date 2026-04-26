# Llama 3.3 70B (Groq) — code_generation/python_api_integration

- model_id: `llama-3.3-70b-versatile`
- success: True  | final: 7.99 | quality: 8.68
- latency_total: 1.952s | tokens_per_second: 339.7
- input_tokens: 136 | output_tokens: 663
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí te dejo una función Python que cumple con los requisitos que mencionaste:
```python
import httpx
import time
import random

def obtener_productos(token):
    """
    Obtiene productos con precio > 100 desde https://api.example.com/products
    con autenticación Bearer token.

    Args:
        token (str): Token de autenticación Bearer

    Returns:
        list: Lista de dicts con {id, name, price} de productos con precio > 100
    """
    # Configuración de retry con backoff exponencial
    max_intentos = 3
    timeout = 10
    backoff_factor = 1

    for intento in range(max_intentos):
        try:
            # Hacer GET a https://api.example.com/products con autenticación Bearer token
            respuesta = httpx.get(
                "https://api.example.com/products",
                headers={"Authorization": f"Bearer {token}"},
                timeout=timeout
            )
            respuesta.raise_for_status()  # Lanzar excepción si la respuesta no es 200

            # Filtar productos con precio > 100
            productos = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in respuesta.json()
                if p["price"] > 100
            ]

            return productos

        except (httpx.NetworkError, httpx.TimeoutException) as e:
            # Manejar errores de red y timeout
            if intento < max_intentos - 1:
                # Esperar un tiempo antes de volver a intentar
                espera = backoff_factor * (2 ** intento)
                espera += random.uniform(0, 1)  # Agregar un poco de aleatoriedad
                print(f"Error {e}, esperando {espera:.2f} segundos antes de volver a intentar")
                time.sleep(espera)
                backoff_factor += 1
            else:
                # Si se han agotado los intentos, lanzar la excepción
                raise

    # Si se han agotado los intentos, lanzar una excepción
    raise Exception("No se pudo obtener la lista de productos después de {} intentos".format(max_intentos))
```
Aquí hay una explicación de cómo funciona la función:

1. La función `obtener_productos` toma un token de autenticación Bearer como argumento.
2. La función hace un GET a `https://api.example.com/products` con autenticación Bearer token usando `httpx`.
3. La función filtra los productos con precio > 100 y devuelve una lista de dicts con solo `{id, name, price}`.
4. La función maneja errores de red y timeout (10 segundos) con un retry con backoff exponencial (max 3 intentos).
5. Si se han agotado los intentos, la función lanza una excepción.

Espero que esto te sea útil. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!