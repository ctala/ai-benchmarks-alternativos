# DeepSeek V4 Pro — multi_turn/debugging_conversation

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 7.675s | tokens_per_second: 69.1
- input_tokens: 335 | output_tokens: 530

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

Ahí está el problema. Un retry infinito crea un efecto cascada que satura el rate limit. Aquí tienes la forma correcta de implementarlo:

**Con backoff exponencial + jitter (recomendado):**

```python
import time
import random
import requests

MAX_RETRIES = 5
BASE_DELAY = 1  # segundo

for attempt in range(MAX_RETRIES):
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code != 429:
        break
    
    # Respetar el Retry-After si el servidor lo envía
    retry_after = response.headers.get("Retry-After")
    if retry_after:
        wait = int(retry_after)
    else:
        # Backoff exponencial con jitter
        wait = BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
    
    print(f"Rate limit alcanzado. Reintentando en {wait:.1f}s (intento {attempt+1}/{MAX_RETRIES})")
    time.sleep(wait)
```

**Si usas la librería oficial de OpenAI/OpenRouter:**

```python
from openai import OpenAI
from tenacity import retry, wait_exponential_jitter, stop_after_attempt

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-api-key"
)

@retry(
    wait=wait_exponential_jitter(initial=1, max=60, jitter=2),
    stop=stop_after_attempt(5),
)
def hacer_request():
    return client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Hola"}],
    )
```

Además, revisa que no estés creando múltiples instancias o hilos que cada uno haga sus propios retries. Eso también multiplicaría las llamadas.