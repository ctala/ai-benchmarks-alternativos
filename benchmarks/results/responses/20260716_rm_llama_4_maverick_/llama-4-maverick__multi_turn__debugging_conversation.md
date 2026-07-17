# Llama 4 Maverick — multi_turn/debugging_conversation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 10.399s | tokens_per_second: 29.1
- input_tokens: 322 | output_tokens: 303
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en estrategias de manejo de errores de rate limit, ofreciendo un ejemplo práctico útil para un emprendedor.

## Respuesta completa

Un loop infinito de retries es un problema común. Para implementarlo correctamente:

1. Usa un número limitado de retries (3-5 veces)
2. Implementa un backoff exponencial entre retries
   - Espera 1s, luego 2s, luego 4s, etc.
   - Agrega un jitter aleatorio (entre 0 y 1s) para evitar el "thundering herd"
3. Solo haz retry en errores específicos (429, 500, 503)
4. Usa headers de ratelimit para ajustar tu estrategia

Ejemplo en Python:
```python
import time
import random
import requests

def hacer_request(url, params):
    max_retries = 5
    retry_delay = 1
    
    for attempt in range(max_retries):
        response = requests.post(url, json=params)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            if 'Retry-After' in response.headers:
                delay = int(response.headers['Retry-After'])
            else:
                delay = retry_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Rate limit. Reintentando en {delay:.1f}s...")
            time.sleep(delay)
        else:
            break
    
    raise Exception(f"Fallo tras {max_retries} intentos")
```
Esto debería ayudarte a manejar los errores de rate limit de manera más efectiva.