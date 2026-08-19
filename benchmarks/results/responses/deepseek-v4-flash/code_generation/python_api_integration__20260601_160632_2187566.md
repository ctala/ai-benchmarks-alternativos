# DeepSeek V4 Flash (OpenRouter) — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.4 | quality: 9.72
- latency_total: 29.574s | tokens_per_second: 72.5
- input_tokens: 110 | output_tokens: 2144
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes una función Python que cumple con todos los requisitos usando `httpx`:

```python
import httpx
import time
from typing import List, Dict, Any

def get_expensive_products(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    timeout: float = 10.0
) -> List[Dict[str, Any]]:
    """
    Obtiene productos con precio > 100 desde una API protegida con Bearer token.

    Args:
        token: Token de autenticación Bearer.
        url: Endpoint de productos.
        max_retries: Número máximo de reintentos (por defecto 3).
        timeout: Timeout en segundos para la petición (por defecto 10).

    Returns:
        Lista de diccionarios con {id, name, price} para productos con price > 100.

    Raises:
        httpx.RequestError: Si falla la conexión o hay timeout después de reintentos.
        httpx.HTTPStatusError: Si la API devuelve un código de error (4xx/5xx) tras reintentos.
        KeyError: Si un producto no contiene los campos esperados.
    """
    headers = {"Authorization": f"Bearer {token}"}

    for attempt in range(max_retries):
        try:
            with httpx.Client() as client:
                response = client.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()  # Lanza excepción si el código no es 2xx

                products = response.json()  # Se espera una lista de productos
                filtered = []
                for product in products:
                    if product.get("price", 0) > 100:
                        filtered.append({
                            "id": product["id"],
                            "name": product["name"],
                            "price": product["price"]
                        })
                return filtered

        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            # Si es el último intento, relanzamos la excepción
            if attempt == max_retries - 1:
                raise
            # Backoff exponencial: espera 2^attempt segundos (1, 2, 4...)
            time.sleep(2 ** attempt)

# Ejemplo de uso:
# try:
#     result = get_expensive_products("tu_token_aquí")
#     print(result)
# except Exception as e:
#     print(f"Error: {e}")
```

### Explicación de cómo cumple los requisitos:

1. **GET con autenticación Bearer**: Se incluye el header `Authorization: Bearer {token}` en cada petición.
2. **Filtro por precio > 100**: Después de obtener la respuesta JSON, se itera sobre la lista de productos y se seleccionan aquellos con `price > 100`.
3. **Retorno de solo {id, name, price}**: Se construye un diccionario con esas tres claves para cada producto filtrado.
4. **Manejo de errores de red y timeout**: Se capturan `httpx.RequestError` (cubre timeout, conexión rechazada, etc.) y `httpx.HTTPStatusError` (códigos HTTP 4xx/5xx) mediante `response.raise_for_status()`.
5. **Retry con backoff exponencial**: Hasta 3 intentos (configurable). Entre intentos se espera un tiempo que crece exponencialmente: 1s, 2s, 4s... (2^attempt). Si todos los intentos fallan, se relanza la última excepción.

La función es flexible: acepta el token como parámetro obligatorio, y permite personalizar la URL, el número de reintentos y el timeout.