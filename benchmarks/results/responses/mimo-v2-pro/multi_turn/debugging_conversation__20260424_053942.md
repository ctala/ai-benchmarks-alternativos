# MiMo-V2-Pro — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.39 | quality: 8.82
- latency_total: 14.206s | tokens_per_second: 56.3
- input_tokens: 357 | output_tokens: 800
- judge_score: 4.8 | justificación: 

## Respuesta completa

Esa es la causa raiz. Un retry infinito es una bomba de requests. Aca te dejo un patron correcto:

## Retry con Exponential Backoff

```python
import time
import random

def call_api_with_retry(payload, max_retries=5):
    for attempt in range(max_retries):
        response = openrouter.chat.completions.create(**payload)
        
        if response.status_code == 429:
            # Leer el header que dice cuando reintentar
            retry_after = response.headers.get("Retry-After")
            
            if retry_after:
                wait = int(retry_after)
            else:
                # Exponential backoff: 1s, 2s, 4s, 8s, 16s + jitter random
                wait = (2 ** attempt) + random.uniform(0, 1)
            
            print(f"429 recibido. Esperando {wait:.1f}s (intento {attempt+1}/{max_retries})")
            time.sleep(wait)
            continue
        
        response.raise_for_status()
        return response.json()
    
    raise Exception("Max retries alcanzado")
```

## Las 3 reglas clave

```
1. LEE Retry-After    → El servidor te dice cuanto esperar
2. EXPONENCIAL        → 1s → 2s → 4s → 8s (no reintentar al toque)
3. LIMITE FIJO        → Max 3-5 retries, despues para
```

## Ejemplo completo con tu caso

```python
import httpx
import time
import random

client = httpx.Client(
    base_url="https://openrouter.ai/api/v1",
    headers={"Authorization": f"Bearer {API_KEY}"}
)

def chat(messages, model="deepseek/deepseek-chat-v3-0324"):
    max_retries = 5
    
    for attempt in range(max_retries):
        try:
            response = client.post("/chat/completions", json={
                "model": model,
                "messages": messages
            })
            
            if response.status_code == 200:
                return response.json()
            
            elif response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                wait = float(retry_after) if retry_after else (2 ** attempt) + random.random()
                print(f"Rate limited. Esperando {wait:.1f}s...")
                time.sleep(wait)
            
            else:
                response.raise_for_status()
                
        except httpx.RequestError as e:
            print(f"Error de red: {e}")
            time.sleep(2 ** attempt)
    
    raise Exception("No se pudo completar despues de {max_retries} intentos")

# Uso normal
result = chat([{"role": "user", "content": "Hola"}])
```

## Lo que NO hacer

```python
# MAL - loop infinito sin espera
while True:
    response = client.post(...)
    if response.status_code != 200:
        continue  # 💥 BOMBA DE REQUESTS

# MAL - retry sin backoff
for i in range(100):
    response = client.post(...)
    if response.status_code == 429:
        continue  # 💥 Sigues bombardeando
```

Con esto deberias resolverlo. Si te sigue dando 429 incluso con el retry correcto, ahi si podemos investigar si hay otro problema.