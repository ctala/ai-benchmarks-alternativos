# MiniMax M2.7 (directo) — multi_turn/debugging_conversation

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.04 | quality: 7.5
- latency_total: 13.427s | tokens_per_second: 39.2
- input_tokens: 315 | output_tokens: 526

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

Ahi esta el problema. Un retry infinito en un 429 crea una tormenta de requests. Necesitas backoff exponencial con maximo de intentos:

```python
import time
import random

MAX_RETRIES = 3
BASE_DELAY = 2  # segundos

def call_with_retry(api_func, *args, **kwargs):
    for attempt in range(MAX_RETRIES):
        try:
            response = api_func(*args, **kwargs)
            return response
            
        except Exception as e:
            # Si es 429, esperar y reintentar
            if e.status == 429 and attempt < MAX_RETRIES - 1:
                # Backoff exponencial + jitter aleatorio
                delay = BASE_DELAY * (2 ** attempt) + random.uniform(0, 1)
                print(f"Rate limit. Reintentando en {delay:.1f}s...")
                time.sleep(delay)
            else:
                # Maximo de retries o error diferente
                raise Exception(f"Fallo tras {attempt + 1} intentos: {e}")

# Uso
result = call_with_retry(openrouter.chat.completions.create, 
                          model="deepseek/deepseek-chat-v3-0324",
                          messages=[...])
```

**Reglas basicas:**
- **Maximo 3 retries** - no mas
- **Backoff exponencial**: 2s → 4s → 8s
- **Jitter**: +random para evitar sincronizacion con otros clientes
- **429 = esperar**, no inmediatamente reintentar

Tambien considera usar la libreria `tenacity` si usas Python:

```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def tu_funcion():
    # tu codigo aqui
    pass
```

Con esto deberia dejar de darte 429 constantemente. El problema se resuelve solo ajustando los retries?