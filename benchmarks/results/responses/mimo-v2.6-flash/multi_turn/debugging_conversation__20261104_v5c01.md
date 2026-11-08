# MiMo V2.6 Flash — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.26 | quality: 7.5
- latency_total: 17.827s | tokens_per_second: 35.5
- input_tokens: 357 | output_tokens: 633

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

Ahi esta el problema. El retry infinito genera mas requests, lo que genera mas 429, en un ciclo vicioso. Aca te dejo una implementacion correcta:

```python
import time
import openai

client = openai.OpenAI(
    api_key="tu-api-key",
    base_url="https://openrouter.ai/api/v1"
)

def llamar_con_retry(messages, max_reintentos=5):
    reintentos = 0
    delay = 1  # segundos iniciales

    while reintentos < max_reintentos:
        try:
            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=messages
            )
            return response

        except openai.RateLimitError as e:
            reintentos += 1
            if reintentos >= max_reintentos:
                raise Exception(f"Rate limit despues de {max_reintentos} reintentos")

            # Exponential backoff: 1, 2, 4, 8, 16...
            print(f"429 - esperando {delay}s (intento {reintentos}/{max_reintentos})")
            time.sleep(delay)
            delay *= 2

        except Exception as e:
            raise  # otros errores no reintentar
```

**Los 3 errores comunes que estabas cometiendo:**

1. **Sin max_reintentos** → loop infinito
2. **Sin delay entre reintentos** → martilleas el servidor
3. **Delay fijo** → deberia ser exponential backoff

**Si quieres algo mas robusto** sin escribir todo manualmente, usa el `tenacity`:

```python
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
import openai

@retry(
    retry=retry_if_exception_type(openai.RateLimitError),
    wait=wait_exponential(min=1, max=30),  # 1s, 2s, 4s... max 30s
    stop=stop_after_attempt(5)             # max 5 reintentos
)
def llamar_api(messages):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=messages
    )
    return response
```

**Checklist rapido:**
- ✅ Maximo de reintentos (5 es razonable)
- ✅ Espera creciente entre intentos (exponential backoff)
- ✅ Solo reintentar el 429, no otros errores
- ✅ Loggear cada reintento para debuggear

Borra primero tu loop infinito, implementa esto, y prueba de nuevo.