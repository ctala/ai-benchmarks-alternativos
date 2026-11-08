# GPT-6 Astra — code_generation/python_api_integration

- model_id: `openai/gpt-6-astra`
- success: True  | final: 7.42 | quality: 9.08
- latency_total: 11.521s | tokens_per_second: 48.7
- input_tokens: 102 | output_tokens: 561
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

```python
import time

import httpx


def obtener_productos(token: str) -> list[dict]:
    """Obtiene productos con precio > 100, con hasta 3 intentos."""
    with httpx.Client(
        headers={"Authorization": f"Bearer {token}"},
        timeout=10.0,
    ) as client:
        for intento in range(3):
            try:
                respuesta = client.get("https://api.example.com/products")
            except (httpx.TimeoutException, httpx.NetworkError):
                if intento == 2:
                    raise  # Propaga el error tras agotar los intentos.

                time.sleep(2 ** intento)  # Backoff: 1 s, luego 2 s.
                continue

            respuesta.raise_for_status()
            productos = respuesta.json()

            return [
                {
                    "id": producto["id"],
                    "name": producto["name"],
                    "price": producto["price"],
                }
                for producto in productos
                if producto["price"] > 100
            ]
```

**Supuestos y comportamiento:**
- La API devuelve una lista JSON de productos con `id`, `name` y `price` numérico.
- Realiza como máximo **3 intentos en total**, reintentando solo errores de red y timeout.
- Si se agotan los intentos, propaga la excepción. Los errores HTTP (4xx/5xx) se propagan sin reintentar.
- `timeout=10.0` establece el límite de espera de cada operación de red de `httpx`, no un plazo global para todos los intentos.