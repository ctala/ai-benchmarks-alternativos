# Kimi K2.6 — code_generation/python_api_integration

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.03 | quality: 9.52
- latency_total: 61.975s | tokens_per_second: 63.7
- input_tokens: 115 | output_tokens: 3946
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Aquí tienes una implementación completa, robusta y sin dependencias externas (solo `httpx`):

```python
import httpx
import time
import random
from typing import List, Dict, Any

def fetch_expensive_products(bearer_token: str) -> List[Dict[str, Any]]:
    """
    Consulta productos filtrando los de precio > 100.
    
    Reintentos con backoff exponencial ante errores de red/HTTP.
    Lanza la última excepción si se agotan los 3 intentos.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
    }
    max_retries = 3
    timeout_seconds = 10.0
    last_exception = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                data = response.json()
                # Soporta respuesta directa [ {...} ] o envuelta { "products": [ {...} ] }
                products = data if isinstance(data, list) else data.get("products", [])

                result = []
                for product in products:
                    if not isinstance(product, dict):
                        continue
                    try:
                        price = float(product.get("price", 0))
                    except (TypeError, ValueError):
                        continue  # Ignora productos con precio no numérico

                    if price > 100:
                        result.append({
                            "id": product.get("id"),
                            "name": product.get("name"),
                            "price": price,
                        })
                return result

        except (httpx.RequestError, httpx.HTTPStatusError, httpx.TimeoutException) as exc:
            last_exception = exc
            # Reintenta con backoff exponencial + jitter si no es el último intento
            if attempt < max_retries - 1:
                backoff = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(backoff)

    # Si agotamos los reintentos, propagamos el error al llamador
    if last_exception:
        raise last_exception
    return []


# Ejemplo de uso
if __name__ == "__main__":
    try:
        products = fetch_expensive_products(bearer_token="tu_token_aqui")
        print(f"Encontrados {len(products)} productos premium")
        for p in products[:5]:
            print(p)
    except httpx.RequestError as e:
        print(f"Error de red tras reintentos: {e}")
    except httpx.HTTPStatusError as e:
        print(f"Error HTTP tras reintentos: {e.response.status_code}")
```

### Características incluidas
| Requisito | Implementación |
|---|---|
| **GET con Bearer** | Header `Authorization: Bearer <token>` |
| **Timeout 10s** | `httpx.Client(timeout=10.0)` |
| **Filtro `price > 100`** | Conversión a `float` y comparación |
| **Retorno limitado** | Solo devuelve `id`, `name`, `price` |
| **Retry x3** | Bucle con `max_retries = 3` |
| **Backoff exponencial** | Espera `2^attempto + jitter` segundos |
| **Sin dependencias extra** | Solo librería estándar + `httpx` |