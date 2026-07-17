# Grok 4.3 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.15 | quality: 9.08
- latency_total: 10.995s | tokens_per_second: 107.7
- input_tokens: 286 | output_tokens: 1184
- judge_score: 4.8 | justificación: 

## Respuesta completa

```python
import httpx
import time
from typing import List, Dict, Any

def obtener_productos_caros(token: str) -> List[Dict[str, Any]]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_intentos = 3

    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()

                return [
                    {"id": item["id"], "name": item["name"], "price": item["price"]}
                    for item in data
                    if item.get("price", 0) > 100
                ]

        except (httpx.TimeoutException, httpx.RequestError, httpx.HTTPStatusError) as e:
            if intento == max_intentos - 1:
                raise
            time.sleep(2 ** intento)  # Backoff: 1s, 2s, 4s

    return []
```