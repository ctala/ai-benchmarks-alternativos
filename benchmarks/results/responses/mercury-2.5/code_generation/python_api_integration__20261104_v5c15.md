# Mercury 2.5 — code_generation/python_api_integration

- model_id: `inception/mercury-2.5`
- success: True  | final: 8.87 | quality: 9.08
- latency_total: 3.259s | tokens_per_second: 515.0
- input_tokens: 100 | output_tokens: 1678
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



Aquí tienes una implementación utilizando `httpx`:

```python
import httpx
import time
from typing import List, Dict, Any

def obtener_productos_caros(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = httpx.Timeout(10.0)

    for intento in range(max_retries):
        try:
            with httpx.Client(timeout=timeout) as client:
                respuesta = client.get(url, headers=headers)
                respuesta.raise_for_status()
                productos = respuesta.json()

                # Filtrar y mapear campos
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in productos
                    if p.get("price", 0) > 100
                ]
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            if intento == max_retries - 1:
                raise
            # Backoff exponencial simple
            tiempo_espera = 2 ** intento
            time.sleep(tiempo_espera)
```

**Características:**
- Usa `httpx.Client` con timeout de 10s.
- Implementa 3 intentos con backoff (1s, 2s, 4s).
- Filtra donde `precio > 100`.
- Retorna solo `id`, `name` y `price`.
- Maneja errores de red y HTTP.