# Kimi K2.6 — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.2 | quality: 9.72
- latency_total: 71.939s | tokens_per_second: 26.5
- input_tokens: 385 | output_tokens: 1909
- judge_score: 4.8 | justificación: 

## Respuesta completa

 El problema está claro: **un 429 con retry inmediato e infinito es una bomba de requests**. Cada error genera más tráfico, lo que genera más 429s, y así hasta que te banean temporalmente.

Aquí tienes cómo implementarlo correctamente:

## La regla de oro para 429s

1. **Nunca retries inmediatos**
2. **Backoff exponencial + jitter** (espera creciente con aleatoriedad)
3. **Máximo 3-5 reintentos** y luego fallar graceful
4. **Leer el header `Retry-After`** si viene en la respuesta
5. **No reintentar errores 4xx que no sean 429** (400, 401, 403, etc.)

---

## Implementación en Python (con `tenacity`)

```python
import openai
import random
import time
from tenacity import (
    retry, 
    stop_after_attempt, 
    wait_exponential_jitter, 
    retry_if_exception_type,
    before_sleep_log
)
import logging

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-..."
)

# Configurar logging para ver qué pasa
logger = logging.getLogger(__name__)

@retry(
    # Máximo 4 intentos (1 original + 3 reintentos)
    stop=stop_after_attempt(4),
    
    # Espera exponencial: 2s, 4s, 8s... + jitter de 0-2s extra
    wait=wait_exponential_jitter(initial=2, exp_base=2, jitter=2, max=60),
    
    # Solo reintentar en errores de rate limit o server errors
    retry=retry_if_exception_type((openai.RateLimitError, openai.APIError, openai.APITimeoutError)),
    
    before_sleep=before_sleep_log(logger, logging.WARNING)
)
def call_openrouter(messages, model="deepseek/deepseek-chat"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            extra_headers={
                "HTTP-Referer": "https://tusitio.com",
                "X-Title": "TuApp"
            }
        )
        return response
    except openai.RateLimitError as e:
        # Si OpenRouter manda Retry-After, respetarlo
        retry_after = e.response.headers.get('retry-after')
        if retry_after:
            logger.warning(f"Rate limit. Esperando {retry_after}s...")
            time.sleep(float(retry_after))
        raise  # Dejar que tenacity maneje el backoff
    except openai.AuthenticationError:
        # NO reintentar 401 - la key es inválida
        raise
    except openai.BadRequestError:
        # NO reintentar 400 - el prompt es inválido
        raise

# Uso
try:
    result = call_openrouter([{"role": "user", "content": "Hola"}])
except Exception as e:
    print(f"Falló definitivamente después de retries: {e}")
```

---

## Implementación manual (sin librerías)

Si no puedes instalar `tenacity`:

```python
import time
import random
import openai

def call_with_retry(messages, max_retries=4):
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=messages
            )
            
        except openai.RateLimitError as e:
            if attempt == max_retries - 1:
                raise  # Último intento fallido, propagar error
            
            # Calcular espera: 2^attempt + random(0, 2)
            wait_time = (2 ** attempt) + random.uniform(0, 2)
            
            # Si el header dice cuánto esperar, usar ese valor + buffer
            retry_after = e.response.headers.get('retry-after')
            if retry_after:
                wait_time = float(retry_after) + random.uniform(0, 1)
            
            print(f"429 en intento {attempt + 1}. Esperando {wait_time:.1f}s...")
            time.sleep(wait_time)
            
        except (openai.AuthenticationError, openai.BadRequestError, openai.PermissionDeniedError):
            # Errores del cliente: no reintentar nunca
            raise
        except Exception as e:
            # Otros errores (timeout, connection): reintentar con menos agresividad
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

---

## Headers importantes a monitorear

OpenRouter a veces devuelve info útil en los headers. Logéalos:

```python
response = client.chat.completions.create(...)
# o en el error: e.response.headers

# Revisa estos:
# x-ratelimit-limit: límite total
# x-ratelimit-remaining: cuántas te quedan
# x-ratelimit-reset: timestamp de cuándo se resetea
# retry-after: segundos a esperar (cuando es 429)
```

---

## Cambios inmediatos que debes hacer en tu código

1. **Busca el `while True` o `for` infinito** y reemplázalo por un contador máximo.
2. **Agrega un `sleep` obligatorio** antes de CADA retry, aunque sea de 1 segundo.
3. **Diferencia el tipo de error**: si es 401/400/403, sal inmediatamente.
4. **Considera una cola**: si necesitas >300 RPM, implementa una cola con consumidor controlado en lugar de spawneadores descontrolados.

---

## Si sigues teniendo 429 después de arreglar esto

Es posible que el límite no sea tuyo, sino del **provider upstream** (DeepSeek puede estar saturado). En ese caso:
- Prueba con `model="openai/gpt-4o-mini"` temporalmente para verificar que tu código funciona
- Revisa el [status de OpenRouter](https://status.openrouter.ai/)
- Considera activar el **Provider Fallback** en tu dashboard de OpenRouter

¿Quieres que revise tu código actual para encontrar el loop infinito específico? Pégalo aquí (sin tu API key) y te digo exactamente qué cambiar.