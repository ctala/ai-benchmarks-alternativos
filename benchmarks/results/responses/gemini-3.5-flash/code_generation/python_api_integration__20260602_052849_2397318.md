# Gemini 3.5 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 7.01 | quality: 8.6
- latency_total: 11.828s | tokens_per_second: 172.8
- input_tokens: 104 | output_tokens: 2044
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes una solución en Python utilizando la librería `httpx` que cumple con todos los requisitos solicitados. 

Para el reintento con backoff exponencial, implementamos una lógica personalizada utilizando el módulo `time` de la librería estándar, evitando así dependencias adicionales como `tenacity`.

```python
import time
from typing import Any, Dict, List
import httpx


def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    """Hace un GET a la API de productos, filtra los que tienen un precio > 100

    y devuelve una lista simplificada con {id, name, price}.
    Maneja errores de red, timeouts y aplica reintentos con backoff exponencial.
    """
    url = "https://api.example.com/products"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }

    max_attempts = 3
    timeout_seconds = 10.0
    backoff_factor = 2  # Multiplicador para el backoff exponencial

    for attempt in range(max_attempts):
        try:
            # Realizamos la petición con el timeout de 10 segundos
            response = httpx.get(url, headers=headers, timeout=timeout_seconds)

            # Lanza HTTPStatusError si el código de estado es 4xx o 5xx
            response.raise_for_status()

            # Si la petición es exitosa, salimos del bucle de reintentos
            products_data = response.json()
            break

        except httpx.HTTPStatusError as exc:
            # Si es un error de cliente (4xx), no tiene sentido reintentar (ej. 401 Unauthorized)
            if exc.response.status_code < 500:
                print(
                    f"Error de cliente ({exc.response.status_code}). No se reintentará."
                )
                raise exc

            # Si