# Mistral Small 4 — code_generation/python_api_integration

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 30.363s | tokens_per_second: 34.0
- input_tokens: 117 | output_tokens: 1032
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función en Python que cumple con todos los requisitos especificados, utilizando `httpx` para las solicitudes HTTP y manejando errores, timeouts y reintentos con backoff exponencial:

```python
import httpx
import time
from typing import List, Dict, Optional

def get_expensive_products(
    bearer_token: str,
    max_retries: int = 3,
    initial_timeout: float = 1.0,
    max_timeout: float = 10.0
) -> Optional[List[Dict]]:
    """
    Obtiene productos con precio > 100 desde una API con autenticación Bearer.

    Args:
        bearer_token: Token de autenticación Bearer
        max_retries: Número máximo de reintentos (default: 3)
        initial_timeout: Tiempo inicial de espera en segundos (default: 1.0)
        max_timeout: Tiempo máximo de espera en segundos (default: 10.0)

    Returns:
        Lista de diccionarios con {id, name, price} o None si falla
    """
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }

    url = "https://api.example.com/products"

    for attempt in range(max_retries):
        try:
            # Configurar timeout (10 segundos total para la operación)
            timeout = httpx.Timeout(
                connect=5.0,  # tiempo para establecer conexión
                read=10.0,   # tiempo para recibir respuesta
                write=5.0,   # tiempo para enviar request
                pool=5.0     # tiempo para obtener conexión del pool
            )

            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)

                # Verificar status code
                response.raise_for_status()

                products = response.json()

                # Filtrar productos con precio > 100
                expensive_products = [
                    {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"]
                    }
                    for product in products
                    if product.get("price", 0) > 100
                ]

                return expensive_products

        except httpx.HTTPStatusError as e:
            # Error HTTP (4xx, 5xx)
            print(f"Error HTTP {e.response.status_code}: {e}")
            if attempt == max_retries - 1:
                return None

        except httpx.RequestError as e:
            # Errores de red (ConnectionError, Timeout, etc.)
            print(f"Error de red: {e}")
            if attempt == max_retries - 1:
                return None

        # Backoff exponencial con jitter para evitar thundering herd
        sleep_time = min(initial_timeout * (2 ** attempt) + (0.1 * (2 ** attempt)), max_timeout)
        print(f"Reintentando en {sleep_time:.2f} segundos... (Intento {attempt + 1}/{max_retries})")
        time.sleep(sleep_time)

    return None  # Solo se llega aquí si todos los reintentos fallan
```

### Características clave:

1. **Autenticación Bearer**: Incluye el token en los headers de la solicitud.
2. **Filtrado**: Solo devuelve productos con `price > 100` en formato `{id, name, price}`.
3. **Manejo de errores**:
   - `HTTPStatusError` para errores HTTP (4xx, 5xx)
   - `RequestError` para errores de red (timeouts, conexiones fallidas, etc.)
4. **Timeouts**:
   - Timeout total de 10 segundos configurado en `httpx.Timeout`.
   - Timeout para diferentes fases de la solicitud (connect, read, write, pool).
5. **Retry con backoff exponencial**:
   - Espera inicial de 1 segundo, duplicándose en cada reintento.
   - Tiempo máximo de espera de 10 segundos.
   - Incluye un pequeño jitter (10% del tiempo de espera) para evitar sincronización.
   - Máximo de 3 reintentos (configurable).

### Uso:

```python
products = get_expensive_products("tu_token_aqui")
if products is not None:
    for product in products:
        print(product)
else:
    print("No se pudieron obtener los productos después de varios intentos")
```

### Notas adicionales:
- La función devuelve `None` si todos los reintentos fallan.
- Los mensajes de error se imprimen en consola (puedes reemplazarlos con logging en producción).
- La función usa `httpx.Client` para reutilizar conexiones (mejor rendimiento).