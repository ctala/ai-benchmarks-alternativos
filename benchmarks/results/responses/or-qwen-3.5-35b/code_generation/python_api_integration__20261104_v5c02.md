# Qwen 3.5 35B — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.63 | quality: 9.8
- latency_total: 14.656s | tokens_per_second: 201.4
- input_tokens: 113 | output_tokens: 2951
- judge_score: 5.0 | justificación: 

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

Aquí tienes una función completa en Python que cumple con todos los requisitos solicitados:

```python
import httpx
import time
import random
from typing import List, Dict, Any


def fetch_filtered_products(
    token: str,
    base_url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Obtiene productos de la API, filtra aquellos con precio > 100 y devuelve 
    solo los campos id, name y price.

    Args:
        token: Token de autenticación Bearer
        base_url: URL base de la API
        max_retries: Número máximo de intentos
        timeout: Tiempo máximo por solicitud en segundos

    Returns:
        Lista de diccionarios con id, name y price de productos filtrados

    Raises:
        Exception: Si todas las solicitudes fallan
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception: Exception | None = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(base_url, headers=headers)
                response.raise_for_status()
                products = response.json()

                filtered_products = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

                return filtered_products

        except httpx.RequestError as e:
            last_exception = e
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"Intento {attempt + 1} fallido, reintentando en {wait_time:.2f}s...")
                time.sleep(wait_time)
                continue
            break

        except Exception as e:
            # Errores no repetibles (ej. JSON inválido)
            raise

    raise last_exception or ConnectionError("Todas las solicitudes fallaron")
```

### Características principales:

- ✅ Autenticación Bearer mediante cabecera `Authorization`.
- ✅ Filtrado de productos con `precio > 100`.
- ✅ Selección de campos `id`, `name`, `price`.
- ✅ Manejo de errores de red y timeout configurado a 10 segundos.
- ✅ Implementación de retry con backoff exponencial y jitter (máx. 3 intentos).
- ✅ Uso exclusivo de `httpx` sin dependencias externas adicionales.

Esta función es robusta, fácil de integrar y lista para uso en producción o entornos de desarrollo.