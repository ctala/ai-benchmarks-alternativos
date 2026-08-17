# MiMo V2.5-Pro (Xiaomi) — multi_turn/debugging_conversation

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.82 | quality: 9.19
- latency_total: 12.895s | tokens_per_second: 56.8
- input_tokens: 357 | output_tokens: 733
- judge_score: 4.8 | justificación: 

## Respuesta completa

Encontramos el problema! El retry infinito esta empeorando el rate limit. Aqui la solucion correcta:

```python
import time
import random
import requests

def call_openrouter_with_retry(api_key, payload, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code == 200:
                return response.json()
            
            if response.status_code == 429:
                # Leer header Retry-After si existe
                retry_after = response.headers.get('Retry-After')
                
                if retry_after:
                    wait_time = float(retry_after)
                else:
                    # Exponential backoff con jitter
                    wait_time = (2 ** attempt) + random.uniform(0, 1)
                
                print(f"Rate limited. Esperando {wait_time:.1f}s (intento {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue
            
            # Otros errores - no reintentar
            response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(1)
    
    raise Exception(f"Max retries ({max_retries}) excedido")
```

**Cambios clave:**

1. **Maximo 3 reintentos** - no infinito
2. **Exponential backoff** - 1s, 2s, 4s
3. **Jitter** - variacion aleatoria para evitar sincronizacion
4. **Respeta header `Retry-After`** - OpenRouter te dice cuanto esperar
5. **No reintenta errores 4xx/5xx** - solo 429

**Uso:**
```python
result = call_openrouter_with_retry(
    api_key="tu-key",
    payload={
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [{"role": "user", "content": "Hola"}]
    }
)
```

Que lenguaje estas usando? Si no es Python te adapto el ejemplo.