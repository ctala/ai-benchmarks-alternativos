# Gemini 3.6 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.44 | quality: 9.76
- latency_total: 10.753s | tokens_per_second: 204.2
- input_tokens: 104 | output_tokens: 2196
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, con una implementación detallada que incluye manejo de errores y backoff exponencial.

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

Aquí tienes la función en Python utilizando únicamente **`httpx`** (y el módulo nativo `time` para el *backoff*):

```python
import time
import httpx


def get_filtered_products(token: str) -> list[dict]:
    """Realiza una petición GET a la API de productos con autenticación Bearer,

    aplica reintentos con backoff exponencial en caso de fallo y filtra
    los productos con precio mayor a 100.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0  # Timeout de 10 segundos
    max_retries = 3
    base_delay = 1  # Tiempo base en segundos para el backoff exponencial

    for attempt in range(1, max_retries + 1):
        try:
            # Petición GET con timeout de 10s
            response = httpx.get(url, headers=headers, timeout=timeout)

            # Lanza excepción si hay un error HTTP (ej. 500, 502, 503, etc.)
            response.raise_for_status()

            products = response.json()

            # Filtrar productos con precio > 100 y mapear a {id, name, price}
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in products
                if p.get("price", 0) > 100
            ]

            return filtered

        except (httpx.RequestError, httpx.HTTPStatusError) as exc:
            # Si se alcanzaron los 3 intentos, se lanza el error final
            if attempt == max_retries:
                print(
                    f"[ERROR] Se superó el límite de {max_retries} intentos. Detalle: {exc}"
                )
                raise

            # Cálculo de backoff exponencial: 1s, 2s, 4s...
            sleep_time = base_delay * (2 ** (attempt - 1))
            print(
                f"[INFO] Intento {attempt} fallido. Reintentando en {sleep_time}s..."
            )
            time.sleep(sleep_time)


# Ejemplo de uso:
# token_api = "tu_token_aqui"
# productos = get_filtered_products(token_api)
# print(productos)
```

### Detalles de la implementación:
1. **Autenticación Bearer**: Se pasa la cabecera `Authorization: Bearer <token>`.
2. **Timeout**: Configurado explícitamente a `10.0` segundos (`httpx.get(..., timeout=10.0)`).
3. **Manejo de Errores**: Se capturan `httpx.RequestError` (para timeouts y errores de red/conexión) y `httpx.HTTPStatusError` (para códigos de estado HTTP 4xx/5xx).
4. **Backoff Exponencial**:
   * Intento 1: Espera $1 \times 2^0 = 1$ segundo.
   * Intento 2: Espera $1 \times 2^1 = 2$ segundos.
   * Intento 3: Falla y lanza la excepción final.
5. **Filtrado y Mapeo**: Se usó una comprensión de listas para seleccionar únicamente las llaves `id`, `name`, y `price` de los elementos que cumplen la condición `price > 100`.