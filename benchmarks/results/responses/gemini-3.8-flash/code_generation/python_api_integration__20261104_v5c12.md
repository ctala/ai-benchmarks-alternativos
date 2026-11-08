# Gemini 3.8 Flash — code_generation/python_api_integration

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.28 | quality: 9.48
- latency_total: 14.371s | tokens_per_second: 126.1
- input_tokens: 104 | output_tokens: 1812
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

Aquí tienes la solución utilizando **`httpx`** y únicamente la librería estándar de Python (`time`):

```python
import time
from typing import Any, Dict, List
import httpx


def get_expensive_products(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = 10.0  # 10 segundos
    max_retries = 3
    base_delay = 1.0  # Tiempo base en segundos para el backoff

    with httpx.Client(timeout=timeout) as client:
        for attempt in range(max_retries):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()

                products = response.json()

                # Filtrar precio > 100 y mapear solo los campos solicitados
                return [
                    {
                        "id": item["id"],
                        "name": item["name"],
                        "price": item["price"],
                    }
                    for item in products
                    if item.get("price", 0) > 100
                ]

            except (httpx.RequestError, httpx.HTTPStatusError) as exc:
                # Si es el último intento, propagar el error o relanzarlo
                if attempt == max_retries - 1:
                    raise RuntimeError(
                        f"Error al obtener productos tras {max_retries} intentos: {exc}"
                    ) from exc

                # Cálculo de backoff exponencial: 1s, 2s, 4s...
                sleep_time = base_delay * (2**attempt)
                time.sleep(sleep_time)

    return []
```

### Detalles de la implementación:
1. **Autenticación**: Se envía la cabecera estándar `Authorization: Bearer <token>`.
2. **Timeout de 10s**: Configurado a través de `httpx.Client(timeout=10.0)` cubriendo conexión, lectura y escritura.
3. **Manejo de Errores y Reintentos**:
   * Captura tanto fallos a nivel de transporte/timeout (`httpx.RequestError`) como códigos HTTP erróneos devueltos por el servidor (`httpx.HTTPStatusError`).
   * Aplica un cálculo exponencial de espera: `1 * (2 ** attempt)` (espera 1s tras el primer fallo, 2s tras el segundo).
   * Al fallar el 3.er intento, lanza una excepción `RuntimeError` encadenando el error original.
4. **Filtrado y Formato**: Utiliza una *list comprehension* para filtrar los productos con `price > 100` y construye un nuevo diccionario extrayendo exclusivamente `id`, `name` y `price`.