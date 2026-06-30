# Grok 4.3 — code_generation/python_api_integration

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.36 | quality: 7.87
- latency_total: 9.859s | tokens_per_second: 134.0
- input_tokens: 225 | output_tokens: 1321

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
    backoff_base = 1  # segundos
    
    for intento in range(max_intentos):
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(url, headers=headers)
                
                # Reintentar solo en errores 5xx
                if 500 <= resp.status_code < 600:
                    if intento < max_intentos - 1:
                        time.sleep(backoff_base * (2 ** intento))
                        continue
                    resp.raise_for_status()
                
                resp.raise_for_status()
                productos = resp.json()
                
                return [
                    {"id": p["id"], "name": p["name"], "price": p["price"]}
                    for p in productos
                    if p.get("price", 0) > 100
                ]
                
        except (httpx.TimeoutException, httpx.NetworkError) as e:
            if intento == max_intentos - 1:
                raise
            time.sleep(backoff_base * (2 ** intento))
    
    return []
```