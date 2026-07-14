# Qwen 3.5 397B — code_generation/python_api_integration

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.08 | quality: 9.32
- latency_total: 30.686s | tokens_per_second: 31.9
- input_tokens: 113 | output_tokens: 978
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any, Optional

def fetch_expensive_products(
    api_url: str = "https://api.example.com/products",
    token: str = "",
    max_retries: int = 3,
    base_delay: float = 1.0,
    timeout_seconds: int = 10
) -> List[Dict[str, Any]]:
    """
    Obtiene productos de una API, filtra por precio > 100 y retorna
    solo los campos id, name y price. Implementa retry con backoff exponencial.

    Args:
        api_url: URL de la API de productos
        token: Token Bearer para autenticación
        max_retries: Número máximo de intentos (default: 3)
        base_delay: Delay base en segundos para backoff (default: 1.0)
        timeout_seconds: Timeout de la petición en segundos (default: 10)

    Returns:
        Lista de diccionarios con {id, name, price} de productos con precio > 100

    Raises:
        httpx.RequestError: Si todos los reintentos fallan
    """
    headers = {"Authorization": f"Bearer {token}"}
    last_exception = None

    for attempt in range(max_retries):
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                response = client.get(api_url, headers=headers)
                response.raise_for_status()
                products = response.json()

                # Filtrar y transformar productos
                filtered = [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in products
                    if isinstance(p, dict) and p.get("price", 0) > 100
                ]
                return filtered

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            last_exception = e
            if attempt < max_retries - 1:
                delay = base_delay * (2 ** attempt)
                time.sleep(delay)
            else:
                raise last_exception

    # Fallback (no debería alcanzarse)
    raise last_exception or httpx.RequestError("Máximo número de reintentos alcanzado")
```

**Ejemplo de uso:**

```python
if __name__ == "__main__":
    try:
        products = fetch_expensive_products(
            api_url="https://api.example.com/products",
            token="tu_token_aqui"
        )
        print(f"Productos encontrados: {len(products)}")
        for p in products:
            print(f"ID: {p['id']}, Nombre: {p['name']}, Precio: ${p['price']}")
    except httpx.RequestError as e:
        print(f"Error al obtener productos: {e}")
```

**Características principales:**
- ✅ Autenticación Bearer token
- ✅ Filtrado por precio > 100
- ✅ Solo retorna {id, name, price}
- ✅ Timeout de 10 segundos
- ✅ Retry con backoff exponencial (1s, 2s, 4s)
- ✅ Manejo de errores de red y HTTP
- ✅ Sin dependencias externas adicionales (solo httpx)