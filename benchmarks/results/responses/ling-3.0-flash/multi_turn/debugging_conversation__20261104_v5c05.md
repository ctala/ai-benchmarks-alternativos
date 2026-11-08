# Ling 3.0 Flash — multi_turn/debugging_conversation

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 15.794s | tokens_per_second: 76.3
- input_tokens: 396 | output_tokens: 1205

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

Perfecto, eso explica todo. Tu loop de retry está convirtiendo 1 request fallida en ~100. Vamos a arreglarlo:

## Principios clave para retries correctos

1. **Max retries finito** - Nunca retry infinito
2. **Backoff exponencial** - Esperar tiempos crecientes entre reintentos (1s → 2s → 4s → 8s...)
3. **Jitter** - Agregar aleatoriedad para evitar que múltiples clientes reboten al mismo tiempo
4. **Respetar `Retry-After`** - Si el servidor envía ese header, usarlo
5. **Solo retry en errores idempotentes** - GET, DELETE. Para POST/PUT, ten cuidado (a menos que tu API sea idempotente)

## Ejemplo en Python (manual)

```python
import time
import random
import requests

def call_openrouter(messages, max_retries=5, base_delay=1.0):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {YOUR_API_KEY}",
        "HTTP-Referer": "https://tu-app.com",
        "X-Title": "Tu App",
        "Content-Type": "application/json",
    }
    payload = {"model": "deepseek/deepseek-v3", "messages": messages}

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    delay = float(retry_after)
                else:
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                
                print(f"429 recibido. Intentando en {delay:.2f}s (intent {attempt + 1}/{max_retries})")
                time.sleep(delay)
                continue
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            if attempt == max_retries:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            print(f"Error: {e}. Reintentando en {delay:.2f}s")
            time.sleep(delay)
    
    raise Exception("Max retries alcanzado")
```

## Alternativa más limpia con `tenacity`

```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type
import requests
from requests.exceptions import HTTPError

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=30),  # 1s a 30s con jitter
    retry=retry_if_exception_type(HTTPError),
    reraise=True
)
def call_openrouter(messages):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={...},
        json={...}
    )
    response.raise_for_status()
    return response.json()
```

## Checklist para tu código

- [ ] Eliminar el loop infinito actual
- [ ] Poner `max_retries = 5` (o menos según tu caso)
- [ ] Implementar backoff exponencial con jitter
- [ ] Verificar si el header `Retry-After` viene en las respuestas 429
- [ ] Considerar si tus requests POST son idempotentes (si no lo son, un retry podría crear duplicados)

Con esto, en lugar de 100 requests por error, harás máximo 5 reintentos con esperas inteligentes. ¿Tu código está en Python o que lenguaje usas? Te puedo adaptar el ejemplo si es otro.