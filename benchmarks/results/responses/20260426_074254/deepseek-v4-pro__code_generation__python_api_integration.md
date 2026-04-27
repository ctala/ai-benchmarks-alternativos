# DeepSeek V4 Pro — code_generation/python_api_integration

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.98 | quality: 9.08
- latency_total: 75.212s | tokens_per_second: 29.2
- input_tokens: 110 | output_tokens: 2193
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import time
import httpx
from httpx import RequestError, HTTPStatusError, TimeoutException

def filtrar_productos_caros(token: str) -> list[dict]:
    """
    Obtiene productos de la API y retorna aquellos con precio > 100.

    Realiza una petición GET a https://api.example.com/products con autenticación
    Bearer. Implementa reintentos con backoff exponencial (máximo 3 intentos) y
    maneja errores de red y timeouts de 10 segundos.

    Args:
        token: Token de autenticación Bearer.

    Returns:
        Lista de diccionarios con las claves 'id', 'name' y 'price' de los productos
        cuyo precio sea estrictamente mayor que 100.

    Raises:
        RequestError, HTTPStatusError, TimeoutException: Si después de los 3 intentos
            la petición sigue fallando.
    """
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0          # segundos
    max_attempts = 3
    backoff_base = 1.0      # segundos para el primer reintento (luego 2, 4)

    for intento in range(max_attempts):
        try:
            respuesta = httpx.get(url, headers=headers, timeout=timeout)
            respuesta.raise_for_status()  # lanza excepción si el código no es 2xx

            productos = respuesta.json()
            # Filtrar productos con precio > 100 y conservar solo id, name, price
            resultado = [
                {"id": p["id"], "name": p["name"], "price": p["price"]}
                for p in productos
                if p.get("price", 0) > 100
            ]
            return resultado

        except (RequestError, HTTPStatusError, TimeoutException) as e:
            # Error de red, timeout o código de estado no exitoso
            if intento == max_attempts - 1:
                raise  # Último intento: relanzar la excepción
            # Calcular tiempo de espera con backoff exponencial
            espera = backoff_base * (2 ** intento)
            time.sleep(espera)
```