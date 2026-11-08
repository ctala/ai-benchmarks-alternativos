# Nemotron 3 Ultra 550B — multi_turn/debugging_conversation

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 3.699s | tokens_per_second: 210.9
- input_tokens: 356 | output_tokens: 780

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico experto en APIs y automatizacion. Ayuda a diagnosticar problemas paso a paso.

**user:**

Mi API de OpenRouter me da error 429 todo el tiempo. No puedo hacer ni una llamada.

**assistant:**

Error 429 es 'Too Many Requests' - significa que estas excediendo el rate limit. Vamos a diagnosticarlo:

1. Cuantas requests/minuto estas haciendo aproximadamente?
2. Que modelo estas usando? (algunos tienen limites mas bajos)
3. Estas usando la API key correcta? (las keys gratuitas tienen limites muy bajos)

**user:**

Estoy haciendo como 5 requests por minuto, usando DeepSeek V3. Tengo una API key con creditos pagados, unos $20 de saldo.

**assistant:**

5 req/min con DeepSeek deberia funcionar sin problemas - el limite es 300 RPM. Algo mas esta pasando. Vamos a verificar:

1. Estas reutilizando la misma instancia del cliente o creando una nueva por cada request?
2. Tienes algun retry automatico que podria estar multiplicando los requests?
3. Me puedes mostrar el header completo de la respuesta 429? Especificamente los headers `x-ratelimit-*`

**user:**

Acabo de revisar y resulta que tengo un loop en mi codigo que hace retry infinito cuando recibe un error. Asi que cada 429 genera como 100 requests mas. Pero no se como arreglarlo bien, como deberia implementar los retries?


## Respuesta completa

Ahi esta el problema. El retry infinito en 429 es el peor caso: cada 429 genera mas 429s.

**Regla de oro:** Nunca reintentar 429 sin `Retry-After` y backoff exponencial.

## Implementación correcta

```python
import time
import random
from openai import OpenAI, RateLimitError

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu_key"
)

def call_with_retry(messages, model="deepseek/deepseek-chat", max_retries=3):
    for attempt in range(max_retries + 1):
        try:
            return client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7
            )
        except RateLimitError as e:
            if attempt == max_retries:
                raise  # Se acabaron los retries, lanza el error
            
            # 1. Leer Retry-After del header (segundos)
            retry_after = 1
            if hasattr(e, 'response') and e.response is not None:
                retry_after = int(e.response.headers.get('Retry-After', 1))
            
            # 2. Backoff exponencial + jitter
            backoff = (2 ** attempt) + random.uniform(0, 1)
            wait_time = max(retry_after, backoff)
            
            print(f"Rate limited. Esperando {wait_time:.1f}s (intento {attempt + 1}/{max_retries})")
            time.sleep(wait_time)
        except Exception as e:
            # Otros errores no se reintentan automaticamente
            raise

# Uso
response = call_with_retry([{"role": "user", "content": "Hola"}])
print(response.choices[0].message.content)
```

## Puntos clave

| Concepto | Por que |
|----------|---------|
| `max_retries=3` | Evita loop infinito |
| `Retry-After` header | El servidor te dice exactamente cuanto esperar |
| Backoff exponencial (`2^attempt`) | Da tiempo al rate limit a recuperarse |
| Jitter (`random.uniform`) | Evita thundering herd si hay multiples clientes |

## Si usas `httpx`/`requests` directo

```python
import httpx

def call_openrouter(messages):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"model": "deepseek/deepseek-chat", "messages": messages}
    
    with httpx.Client(timeout=30) as client:
        for attempt in range(4):
            r = client.post("https://openrouter.ai/api/v1/chat/completions", 
                           json=payload, headers=headers)
            
            if r.status_code == 429:
                wait = int(r.headers.get('Retry-After', 2 ** attempt))
                time.sleep(wait + random.uniform(0, 0.5))
                continue
            
            r.raise_for_status()
            return r.json()
        
        raise Exception("Max retries exceeded")
```

**Test rapido:** Cambia tu codigo, haz una sola llamada y confirma que no explota. Despues escala.