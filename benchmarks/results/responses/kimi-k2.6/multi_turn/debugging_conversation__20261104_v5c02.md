# Kimi K2.6 — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 16.858s | tokens_per_second: 76.3
- input_tokens: 385 | output_tokens: 1286

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

 Ese es el problema clásico: **un retry agresivo sin backoff convierte un pequeño rate limit en un ataque DDoS accidental**. OpenRouter te está bloqueando porque ese loop genera cientos de requests por segundo.

Aquí tienes cómo implementarlo correctamente:

## Reglas de oro para retries seguros

1. **Máximo fijo**: Nunca más de 3-5 intentos
2. **Backoff exponencial**: Esperar 2s, luego 4s, luego 8s (no instantáneo)
3. **No retryar todo**: Solo 408, 429, 500, 502, 503. **Nunca** 400, 401, 403, 404
4. **Leer los headers**: Si la API te dice `Retry-After`, úsalo
5. **Jitter**: Añadir aleatoriedad para evitar "thundering herd"

---

## Opción A: Con `tenacity` (recomendado)

```python
import openai
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-..."
)

# Configuración segura
@retry(
    stop=stop_after_attempt(3),                    # Máximo 3 intentos
    wait=wait_exponential_jitter(initial=2, max=60), # 2s, 4s, 8s + jitter
    retry=retry_if_exception_type(openai.RateLimitError),
    reraise=True
)
def call_api(messages):
    try:
        return client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=messages
        )
    except openai.RateLimitError as e:
        # Opcional: leer Retry-After si existe
        retry_after = e.response.headers.get('retry-after')
        if retry_after:
            print(f"Rate limit. Esperar {retry_after}s")
        raise
```

---

## Opción B: Implementación manual (sin librerías)

```python
import time
import random

def call_with_retry(client, messages, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=messages
            )
        except Exception as e:
            status = getattr(e, 'status_code', None) or getattr(e.response, 'status_code', 0)
            
            # Solo retryar estos códigos
            if status not in (408, 429, 500, 502, 503):
                raise  # Error del cliente, no retryar
            
            if attempt == max_retries - 1:
                raise  # Último intento fallido
            
            # Backoff exponencial con jitter
            wait = (2 ** attempt) + random.uniform(0, 1)
            
            # Si OpenRouter envía Retry-After, respetarlo
            retry_after = getattr(e.response, 'headers', {}).get('retry-after')
            if retry_after:
                wait = int(retry_after) + random.uniform(0, 1)
            
            print(f"Error {status}. Reintentando en {wait:.1f}s... (intento {attempt + 1}/{max_retries})")
            time.sleep(wait)
```

---

## Qué hacer AHORA para salir del loop

Tu IP/API key probablemente está en cooldown temporal por el spam:

1. **Para tu código inmediatamente**
2. **Espera 1-2 minutos** sin hacer requests
3. **Cambia la lógica** antes de volver a correr
4. **Prueba con 1 solo request** manualmente para verificar que ya no estás baneado

---

## Truco extra: Headers de OpenRouter

OpenRouter envía headers útiles. Lee siempre:
- `x-ratelimit-limit`: Tu límite (ej: 300)
- `x-ratelimit-remaining`: Cuántas te quedan
- `x-ratelimit-reset`: Timestamp de reset

```python
response = client.chat.completions.create(...)
print(response.response.headers)  # En algunos clientes está en response._response
```

**Resumen**: Tu retry anterior era "instantáneo e infinito". El correcto es **"3 intentos máximo, con esperas crecientes"**. Con eso, 5 requests/minuto nunca te darán problemas.

¿Necesitas que adapte el código a otro lenguaje (JS, Go, etc.)?