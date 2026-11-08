# GPT-6.1 Sol — code_generation/python_api_integration

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 6.99 | quality: 7.68
- latency_total: 9.21s | tokens_per_second: 58.6
- input_tokens: 102 | output_tokens: 540
- judge_score: 3.8 | justificación: 

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
    """Obtiene productos con precio > 100, con un máximo de 3 intentos."""
    with httpx.Client(
        headers={"Authorization": f"Bearer {token}"},
        timeout=10.0,
    ) as client:
        for intento in range(3):
            try:
                response = client.get("https://api.example.com/products")
                response.raise_for_status()

                productos = response.json()
                return [
                    {
                        "id": producto["id"],
                        "name": producto["name"],
                        "price": producto["price"],
                    }
                    for producto in productos
                    if producto["price"] > 100
                ]

            except httpx.RequestError:
                # Incluye errores de red y timeouts.
                if intento == 2:
                    raise

                time.sleep(2 ** intento)  # Esperas de 1 y 2 segundos.
```

**Consideraciones:**
- Se asume que la API devuelve una lista JSON de productos con campos `id`, `name` y `price`, siendo `price` numérico.
- Realiza como máximo **3 intentos en total**, reintentando errores de red y timeout.
- Los errores HTTP (4xx/5xx) se propagan como `httpx.HTTPStatusError`, sin reintentos.
- El timeout de 10 segundos se aplica a las operaciones de red de HTTPX, no como límite global de toda la función.