# Seed 2.1 Turbo — code_generation/python_api_integration

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.14 | quality: 9.72
- latency_total: 90.706s | tokens_per_second: 69.4
- input_tokens: 155 | output_tokens: 6298
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

Aquí tienes la función cumpliendo todos los requisitos, usando solo `httpx` y librerías estándar de Python, con manejo de errores robusto y buenas prácticas:

```python
import httpx
import time
from typing import List, Dict


def get_filtered_products(
    bearer_token: str,
    max_retries: int = 3,
    base_backoff_seconds: float = 1.0,
    request_timeout_seconds: float = 10.0
) -> List[Dict]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100 y retorna solo los campos id, name y price.
    
    Args:
        bearer_token: Token de autenticación Bearer para la API.
        max_retries: Cantidad máxima de intentos de solicitud (default: 3).
        base_backoff_seconds: Tiempo base para el cálculo de backoff exponencial entre reintentos (default: 1s).
        request_timeout_seconds: Tiempo máximo de espera por cada solicitud (default: 10s).
    
    Returns:
        Lista de diccionarios con las claves `id`, `name` y `price` de los productos filtrados.
    
    Raises:
        httpx.HTTPStatusError: Si la API devuelve un error 4xx (no reintentable) o se agotan los reintentos para 5xx.
        httpx.NetworkError: Si hay fallos de conexión después de agotar todos los reintentos.
        httpx.TimeoutException: Si se supera el tiempo de espera en todos los intentos.
        ValueError: Si la respuesta de la API no tiene el formato de lista esperado.
    """
    API_URL = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }

    # Configuramos el timeout una sola vez para el cliente
    timeout_config = httpx.Timeout(request_timeout_seconds)

    # Reutilizamos el cliente HTTP para aprovechar conexiones persistentes
    with httpx.Client(timeout=timeout_config) as client:
        for attempt in range(max_retries):
            try:
                # Realizamos la solicitud GET
                response = client.get(API_URL, headers=headers)
                # Levantamos excepción automáticamente para códigos de estado 4xx/5xx
                response.raise_for_status()

                # Parseamos la respuesta JSON
                products = response.json()

                # Validamos que la respuesta sea una lista (ajusta si la API devuelve un objeto con clave "products")
                if not isinstance(products, list):
                    raise ValueError("La respuesta de la API no es una lista de productos")

                # Filtramos y transformamos los productos
                filtered_products = []
                for product in products:
                    price = product.get("price")
                    # Solo consideramos productos con precio numérico y mayor a 100
                    if isinstance(price, (int, float)) and price > 100:
                        filtered_products.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price
                        })

                return filtered_products

            # Errores reintentables: fallos de red y timeout
            except (httpx.NetworkError, httpx.TimeoutException) as error:
                # Si es el último intento, propagamos el error
                if attempt == max_retries - 1:
                    raise
                # Calculamos tiempo de espera con backoff exponencial: 1s, 2s, 4s...
                wait_time = base_backoff_seconds * (2 ** attempt)
                time.sleep(wait_time)

            # Errores de estado HTTP: solo reintentamos si son 5xx (errores de servidor transitorios)
            except httpx.HTTPStatusError as error:
                is_server_error = error.response.status_code >= 500
                has_more_attempts = attempt < max_retries - 1

                if is_server_error and has_more_attempts:
                    wait_time = base_backoff_seconds * (2 ** attempt)
                    time.sleep(wait_time)
                else:
                    # Errores 4xx o sin más intentos: propagamos el error
                    raise

    # Punto inalcanzable, pero por seguridad
    return []
```

---

### Ejemplo de uso:
```python
if __name__ == "__main__":
    token = "tu_token_de_autenticacion"
    try:
        productos = get_filtered_products(bearer_token=token)
        print(f"Productos filtrados: {len(productos)}")
        for p in productos:
            print(p)
    except httpx.TimeoutException:
        print("Error: Se agotó el tiempo de espera después de 3 intentos")
    except httpx.NetworkError:
        print("Error: Fallo de conexión a la API")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP: {e.response.status_code} - {e.response.text}")
    except ValueError as e:
        print(f"Error en formato de respuesta: {e}")
```

---

### Características y decisiones de diseño:
1. **Autenticación**: Se envía el token en el header `Authorization` en formato Bearer, como estándar.
2. **Timeout de 10s**: Configurado a nivel de cliente `httpx` para cubrir todo el ciclo de la solicitud (conexión + lectura).
3. **Retry con backoff exponencial**: Implementado sin dependencias externas, con 3 intentos totales. Los tiempos de espera entre intentos son `1s → 2s` (para 3 intentos hay 2 esperas).
4. **Reintentos inteligentes**: Solo se reintenta para errores transitorios:
   - Fallos de red (`NetworkError`)
   - Timeouts (`TimeoutException`)
   - Errores de servidor 5xx (ej: 500, 502, 503)
   - No se reintenta errores 4xx (ej: 401 token inválido, 404 no encontrado) ya que son fallos del cliente que no se resuelven reintentando.
5. **Validación de datos**: Se verifica que el precio sea numérico para evitar errores de comparación, y se usa `.get()` para extraer campos sin generar `KeyError` si faltan en la respuesta.
6. **Cliente reutilizado**: Se usa un solo `httpx.Client` para todos los intentos, aprovechando conexiones HTTP persistentes.

---

### Ajustes comunes:
- Si la API devuelve los productos dentro de una clave (ej: `{"products": [...]}`), cambia la línea `products = response.json()` por `products = response.json()["products"]`.
- Para agregar **jitter** (variación aleatoria) al backoff y evitar el efecto "thundering herd", agrega `import random` y modifica el cálculo de `wait_time`:
  ```python
  wait_time = base_backoff_seconds * (2 ** attempt) + random.uniform(0, 0.5)
  ```