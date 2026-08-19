# Gemini 3.5 Flash Lite — code_generation/python_api_integration

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.87 | quality: 9.72
- latency_total: 3.501s | tokens_per_second: 293.6
- input_tokens: 105 | output_tokens: 1028
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

Aquí tienes la implementación utilizando la librería `httpx` (que incluye soporte nativo para reintentos mediante su transporte `HTTPTransport` o lógica manual. Para tener un control exacto del backoff exponencial y el manejo de errores específico, implementaremos el bucle de reintentos de forma explícita).

```python
import time
import httpx

# Constantes
API_URL = "https://api.example.com/products"
TOKEN = "tu_token_bearer_aqui"
TIMEOUT_SECONDS = 10.0
MAX_RETRIES = 3


def get_expensive_products() -> list[dict]:
    """Realiza una petición GET a la API de productos, filtra aquellos con precio > 100,

    y retorna una lista con las claves id, name y price.
    Incluye manejo de errores y reintentos con backoff exponencial.
    """
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json",
    }

    delay = 1  .  # Tiempo de espera inicial en segundos para el backoff

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Usamos httpx.Client como context manager con el timeout especificado
            with httpx.Client(timeout=TIMEOUT_SECONDS) as client:
                response = client.get(API_URL, headers=headers)

                # Lanza una excepción para códigos de estado 4xx/5xx
                response.raise_for_status()

                data = response.json()

                # Manejamos el caso de que la API retorne una lista directamente
                # o un diccionario que contenga la lista en una clave (ej. {"products": [...]})
                products = data if isinstance(data, list) else data.get("products", [])

                filtered_products = []
                for product in products:
                    price = product.get("price", 0)
                    if price > 100:
                        filtered_products.append(
                            {
                                "id": product.get("id"),
                                "name": product.get("name"),
                                "price": price,
                            }
                        )

                return filtered_products

        except (httpx.TimeoutException, httpx.NetworkError) as e:
            # Errores de red o timeout, permitimos reintento
            print(f"Intento {attempt}/{MAX_RETRIES} falló por red/timeout: {e}")
            if attempt == MAX_RETRIES:
                print("Se alcanzó el número máximo de reintentos.")
                raise

        except httpx.HTTPStatusError as e:
            # Errores HTTP del servidor (5xx) pueden reintentarse.
            # Errores del cliente (4xx) generalmente no deberían reintentarse.
            print(f"Intento {attempt}/{MAX_RETRIES} - Error HTTP: {e.response.status_code}")
            if 500 <= e.response.status_code < 600 and attempt < MAX_RETRIES:
                pass  # Permitir reintento para errores 5xx
            else:
                raise  # No reintentar errores 4xx o si ya es el último intento

        except Exception as e:
            print(f"Error inesperado: {e}")
            raise

        # Backoff exponencial antes del siguiente intento (ej: 1s, 2s, 4s...)
        if attempt < MAX_RETRIES:
            time.sleep(delay)
            delay *= 2

    return []
```

### Explicación de los puntos clave:
1. **Autenticación Bearer:** Se incluye en el diccionario `headers` usando el formato `"Authorization": "Bearer <TOKEN>"`.
2. **Filtrado:** Recorre la respuesta y filtra los diccionarios donde `price > 100`.
3. **Proyección (id, name, price):** Crea un nuevo diccionario por cada producto filtrado conteniendo únicamente las 3 llaves solicitadas.
4. **Manejo de Errores y Timeout:** Se configura `timeout=10.0` y se capturan excepciones específicas de `httpx` (`TimeoutException`, `NetworkError`, `HTTPStatusError`).
5. **Retry con Backoff Exponencial:** Un bucle `for` controla hasta 3 intentos (`MAX_RETRIES = 3`). En cada fallo de red/timeout, el tiempo de espera se duplica (`time.sleep(delay)` donde `delay` se multiplica por 2 en cada iteración).