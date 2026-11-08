# Gemini 3.5 Flash Lite — code_generation/python_api_integration

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.93 | quality: 9.72
- latency_total: 2.785s | tokens_per_second: 271.5
- input_tokens: 104 | output_tokens: 756
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

Aquí tienes la función en Python utilizando la librería `httpx`. Cumple con todos los requisitos especificados, incluyendo el manejo de errores, timeout y la lógica de reintentos con backoff exponencial.

```python
import time
import httpx


def get_expensive_products(token: str) -> list[dict]:
    """Realiza una petición GET a la API de productos, filtra aquellos con precio > 100,

    y retorna una lista con los campos {id, name, price}.
    Incluye reintentos con backoff exponencial y manejo de errores.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0
    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()  # Lanza excepción para códigos 4xx/5xx

                products = response.json()

                # Filtrar y transformar los datos
                filtered_products = [
                    {
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": p.get("price"),
                    }
                    for p in products
                    if p.get("price", 0) > 100
                ]

                return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Si es el último intento, propagamos el error
            if attempt == max_retries:
                raise RuntimeError(
                    f"Error de red o timeout tras {max_retries} intentos: {e}"
                )

            # Backoff exponencial: 2^attempt segundos (2s, 4s, 8s...)
            sleep_time = 2**attempt
            time.sleep(sleep_time)

        except httpx.HTTPStatusError as e:
            # Los errores HTTP (como 401, 404, 500) generalmente no se reintentan igual,
            # pero para errores 5xx podría aplicarse. Aquí lanzamos directamente.
            raise RuntimeError(
                f"Error HTTP {e.response.status_code}: {e.response.text}"
            )

        except Exception as e:
            raise RuntimeError(f inesperado: {e}")
```

### Explicación de los puntos clave:
1. **Autenticación Bearer**: Se pasa en el diccionario `headers` con `Authorization: Bearer <token>`.
2. **Filtrado y proyección**: Se usa una *list comprehension* para filtrar `price > 100` y construir nuevos diccionarios solo con las llaves `id`, `name` y `price`.
3. **Timeout**: Configurado a `10.0` segundos tanto a nivel de cliente como en la petición.
4. **Manejo de errores**: Captura excepciones específicas de `httpx` (`TimeoutException`, `NetworkError`, `HTTPStatusError`).
5. **Retry con backoff exponencial**: Un ciclo `for` que intenta hasta 3 veces. Si falla por red o timeout, espera $2^{attempt}$ segundos antes de reintentar.