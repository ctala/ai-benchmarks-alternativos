# Fugu Max — code_generation/python_api_integration

- model_id: `sakana/fugu-max`
- success: True  | final: 7.75 | quality: 9.32
- latency_total: 50.442s | tokens_per_second: 88.0
- input_tokens: 264 | output_tokens: 4437
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

Aquí tienes una implementación con `httpx`, timeout de 10 segundos y retry con backoff exponencial:

```python
import time
import httpx


def obtener_productos(token: str, max_intentos: int = 3) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}

    with httpx.Client(timeout=10.0) as client:
        for intento in range(max_intentos):
            try:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                productos = response.json()

                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in productos
                    if isinstance(p.get("price"), (int, float)) and p["price"] > 100
                ]

            except httpx.RequestError as exc:
                if intento == max_intentos - 1:
                    raise
                time.sleep(2 ** intento)

    return []
```

La excepción `httpx.RequestError` cubre tanto errores de red como timeouts. El backoff espera 1 segundo y luego 2 segundos entre reintentos. Si los 3 intentos fallan, se relanza la última excepción.