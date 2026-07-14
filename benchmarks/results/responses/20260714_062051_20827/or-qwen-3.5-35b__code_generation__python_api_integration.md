# Qwen 3.5 35B — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.9 | quality: 9.72
- latency_total: 6.35s | tokens_per_second: 161.1
- input_tokens: 113 | output_tokens: 1023
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
import random
from typing import List, Dict, Any

def fetch_products_with_retry(
    token: str,
    base_url: str = "https://api.example.com",
    endpoint: str = "/products",
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Hace una petición GET a la API de productos con autenticación Bearer,
    filtra por precio > 100 y aplica retry con backoff exponencial.

    Args:
        token: Bearer token para autenticación
        base_url: URL base de la API
        endpoint: Endpoint de productos
        max_retries: Máximo número de intentos
        timeout: Tiempo de espera en segundos

    Returns:
        Lista de dicts con {id, name, price} para productos con price > 100
    """
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{base_url}{endpoint}"

    for attempt in range(1, max_retries + 1):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()  # Lanza excepción si hay error HTTP
                data = response.json()

            # Asumimos que la respuesta es una lista de productos
            if not isinstance(data, list):
                raise ValueError("La respuesta de la API no es una lista")

            # Filtrar productos con precio > 100
            filtered = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in data
                if isinstance(p, dict) and "price" in p and p["price"] > 100
            ]

            return filtered

        except httpx.TimeoutException:
            if attempt == max_retries:
                raise
            wait_time = (2 ** (attempt - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)

        except httpx.HTTPError as e:
            if attempt == max_retries:
                raise
            wait_time = (2 ** (attempt - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)

        except Exception as e:
            if attempt == max_retries:
                raise
            wait_time = (2 ** (attempt - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)

    return []
```

### Características implementadas:
1. ✅ Autenticación Bearer Token en cabeceras
2. ✅ Filtrado de productos con precio > 100
3. ✅ Retorno de campos {id, name, price}
4. ✅ Manejo de errores de red y timeout (10 segundos)
5. ✅ Retry con backoff exponencial (máximo 3 intentos)
6. ✅ Uso exclusivo de `httpx`, sin dependencias adicionales

### Ejemplo de uso:
```python
if __name__ == "__main__":
    try:
        products = fetch_products_with_retry(
            token="TU_BEARER_TOKEN",
            timeout=10
        )
        print(f"Productos encontrados: {len(products)}")
        for p in products:
            print(p)
    except Exception as e:
        print(f"Error: {e}")
```

### Notas:
- El backoff exponencial se calcula como: `2^(attempt-1) + random(0,1)`
- Se incluyen validaciones básicas de estructura de datos
- Puedes ajustar el `base_url` y `endpoint` si es necesario