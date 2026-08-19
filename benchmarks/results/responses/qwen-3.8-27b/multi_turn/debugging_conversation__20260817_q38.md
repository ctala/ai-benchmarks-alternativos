# Qwen 3.8 27B — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 19.341s | tokens_per_second: 23.9
- input_tokens: 386 | output_tokens: 463

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



Ese es el problema. El retry infinito convierte un 429 momentáneo en una tormenta.

**Patrón correcto: backoff exponencial con jitter**

```python
import time
import random

def call_with_retry(func, max_retries=5):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError as e:
            if attempt == max_retries - 1:
                raise
            # Backoff: 1s, 2s, 4s, 8s, 16s + jitter aleatorio
            wait = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait)
        except Exception:
            raise  # Otros errores no se reintentan
```

**Reglas clave:**

- **Máximo 5 reintentos**, nunca infinito
- **Solo reintenta 429 y 5xx**, no 4xx (auth, bad request, etc.)
- **Respeta el header `Retry-After`** si la API lo devuelve
- **Jitter aleatorio** para evitar que múltiples clientes reintenten al mismo tiempo

**Si usas la librería oficial de OpenRouter:**

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
    max_retries=3  # Ya incluye backoff exponencial
)
```

La librería ya maneja el backoff internamente. Solo quita tu loop manual.

**Verificación rápida:**
- Revisa los headers `x-ratelimit-remaining-requests` en cada respuesta
- Si llega a 0, espera antes de la siguiente llamada, no espere al 429

¿Estás usando Python, Node, u otro lenguaje? Te doy el ejemplo exacto para tu stack.