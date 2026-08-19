# MiMo-V2.5 Pro — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 7.569s | tokens_per_second: 91.3
- input_tokens: 357 | output_tokens: 691
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando el problema de manera integral con una solución detallada y bien estructurada.

## Respuesta completa

Perfecto, ya tienes el problema identificado. Aquí la solución correcta:

## Retry con Backoff Exponencial + Jitter

```python
import time
import random
import requests

def llamar_api_openrouter(prompt, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    for intento in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        
        if response.status_code == 429:
            # Obtener retry-after del header si existe
            retry_after = response.headers.get("retry-after")
            
            if retry_after:
                wait = float(retry_after)
            else:
                # Backoff exponencial: 2^intento + jitter aleatorio
                base_wait = 2 ** intento  # 1, 2, 4, 8, 16 segundos
                jitter = random.uniform(0, 1)
                wait = base_wait + jitter
            
            print(f"Rate limited. Esperando {wait:.1f}s (intento {intento + 1}/{max_retries})")
            time.sleep(wait)
            continue
        
        # Otros errores (4xx, 5xx) - no reintentar
        response.raise_for_status()
    
    raise Exception(f"API falló después de {max_retries} intentos")
```

## Los puntos clave:

| Concepto | Por qué |
|----------|---------|
| **max_retries limitado** | Evita loops infinitos |
| **Backoff exponencial** | Espera cada vez más: 1s, 2s, 4s, 8s... |
| **Jitter (aleatorio)** | Evita que todos los clientes reintenten al mismo tiempo |
| **Leer retry-after** | Respeta lo que dice el servidor |
| **No reintentar 4xx/5xx** | Solo reintentar rate limits, no errores reales |

## Para requests asíncrono (si usas aiohttp):

```python
import asyncio
import aiohttp

async def llamar_api_async(prompt, max_retries=5):
    for intento in range(max_retries):
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status == 200:
                return await resp.json()
            
            if resp.status == 429:
                wait = (2 ** intento) + random.uniform(0, 1)
                await asyncio.sleep(wait)
                continue
            
            resp.raise_for_status()
```

Con esto, con 5 req/min no deberías ver 429 nunca más. ¿Necesitas adaptarlo a algún framework específico?