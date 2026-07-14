# DeepSeek V4 Pro — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 12.405s | tokens_per_second: 29.2
- input_tokens: 333 | output_tokens: 362
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, abordando directamente el problema de la tasa de error 429 con una solución práctica y detallada, incluyendo un enfoque de backoff exponencial para mayor robustez.

## Respuesta completa

Ahi esta el problema - retry infinito en 429 causa un loop mortal. Aqui tienes la implementacion correcta:

```python
import time
import requests

def call_openrouter(prompt, max_retries=3):
    for intento in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "model": "deepseek/deepseek-chat",
                "messages": [{"role": "user", "content": prompt}]
            }
        )
        
        if response.status_code == 429:
            # Leer el tiempo de espera sugerido
            retry_after = int(response.headers.get('Retry-After', 60))
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            
            wait_time = max(retry_after, 5)  # minimo 5 segundos
            
            if intento < max_retries - 1:
                print(f"Rate limited. Esperando {wait_time}s...")
                time.sleep(wait_time)
                continue
            
        return response.json()
```

**Puntos clave:**
- **Maximo 3 retries** - nunca infinito
- **Respeta Retry-After** - OpenRouter te dice cuanto esperar
- **Usa exponential backoff** si quieres ser mas robusto:

```python
wait_time = min(retry_after * (2 ** intento), 120)  # max 2 min
```

Arregla ese loop infinito y tus 5 RPM funcionaran perfecto.