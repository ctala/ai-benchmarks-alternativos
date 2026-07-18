# Kimi K3 — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.59 | quality: 7.5
- latency_total: 10.469s | tokens_per_second: 36.2
- input_tokens: 517 | output_tokens: 379
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, abordando el problema de manera efectiva con una implementación adecuada de exponential backoff.

## Respuesta completa

Perfecto, encontramos la causa raiz. Un retry infinito explica perfectamente los 429 constantes.

Aqui esta la implementacion correcta con exponential backoff:

```python
import time
import requests

def call_api_with_retry(prompt, max_retries=5):
    base_delay = 1  # segundo
    
    for attempt in range(max_retries):
        try:
            response = requests.post(
                'https://openrouter.ai/api/v1/chat/completions',
                headers={'Authorization': f'Bearer {api_key}'},
                json={'model': 'deepseek/deepseek-chat', 'messages': prompt}
            )
            
            if response.status_code == 200:
                return response.json()
                
            elif response.status_code == 429:
                # Calcular delay exponencial: 1s, 2s, 4s, 8s, 16s
                delay = base_delay * (2 ** attempt)
                print(f'Rate limited. Esperando {delay}s (intento {attempt + 1}/{max_retries})')
                time.sleep(delay)
                continue
                
            else:
                # Otro error - no reintentar
                response.raise_for_status()
                
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(base_delay * (2 ** attempt))
    
    raise Exception('Max retries alcanzado')
```

Claves importantes:
1. Limite de reintentos (max 5)
2. Exponential backoff (duplicar el delay cada vez)
3. Solo reintentar en 429 y errores de red
4. Logging para debugging

Necesitas ayuda implementando esto en tu stack especifico?