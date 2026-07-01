# Nemotron 3 Ultra 550B — multi_turn/debugging_conversation

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 5.99 | quality: 6.47
- latency_total: 37.08s | tokens_per_second: 19.4
- input_tokens: 356 | output_tokens: 719

## Respuesta completa

Ese es el problema clasico. Un loop infinito en 429 te auto-DDoSea. Implementa **exponential backoff con jitter** y respeta el header `Retry-After`.

Ejemplo robusto en Python:

```python
import time
import random
import httpx

async def call_with_retry(client, url, headers, json, max_retries=5):
    for attempt in range(max_retries):
        resp = await client.post(url, headers=headers, json=json)
        
        if resp.status_code == 429:
            # 1. Leer Retry-After (segundos o fecha HTTP)
            retry_after = resp.headers.get("Retry-After")
            if retry_after:
                try:
                    wait = int(retry_after)
                except ValueError:
                    # Es una fecha HTTP, parsearla
                    wait = max(0, int(time.mktime(time.strptime(retry_after, "%a, %d %b %Y %H:%M:%S GMT"))) - time.time())
            else:
                # 2. Backoff exponencial + jitter si no hay header
                wait = (2 ** attempt) + random.uniform(0, 1)
            
            print(f"429 - Esperando {wait:.1f}s (intento {attempt + 1}/{max_retries})")
            await asyncio.sleep(wait)
            continue
        
        if 500 <= resp.status_code < 600:
            # Errores de servidor: retry con backoff
            wait = (2 ** attempt) + random.uniform(0, 1)
            await asyncio.sleep(wait)
            continue
            
        return resp  # 2xx, 4xx (excepto 429)
    
    raise Exception(f"Max retries ({max_retries}) exceeded")
```

**Puntos clave:**
| Regla | Por que |
|-------|---------|
| `Retry-After` tiene prioridad | El servidor te dice exactamente cuando volver |
| Max 5-6 retries | Despues de ~32-64s ya no vale la pena |
| Jitter (`random.uniform`) | Evita thundering herd si hay muchos clientes |
| Solo retry en 429 y 5xx | 400/401/403/404 no se arreglan reintentando |

**Si usas OpenAI SDK / `openai` python client:** ya trae esto built-in:

```python
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key="sk-or-...",
    base_url="https://openrouter.ai/api/v1",
    max_retries=5,  # default: 2
    timeout=30.0
)
```

El SDK respeta `Retry-After` y hace exponential backoff automaticamente.

---

**Verifica tambien:** que no estes creando `AsyncClient`/`httpx.Client` nuevo por request. Usa **uno solo** (connection pooling) y compartelo.