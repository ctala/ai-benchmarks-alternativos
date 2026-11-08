# Mercury 3 — multi_turn/debugging_conversation

- model_id: `inception/mercury-3`
- success: True  | final: 9.41 | quality: 10.0
- latency_total: 2.194s | tokens_per_second: 536.4
- input_tokens: 338 | output_tokens: 1177

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

El problema es claro: tu loop de retry no tiene límite ni espera, así que cada 429 se convierte en una avalancha de requests. La solución es implementar **retry con exponential backoff + jitter**, respetar el header `Retry-After` y limitar el número de intentos.

Te explico cómo hacerlo bien:

---

### 1. Reglas básicas para retries

- **Nunca reintentar inmediatamente** un 429. Espera al menos 1 segundo.
- **Usa exponential backoff**: duplica la espera en cada intento (1s → 2s → 4s → 8s...).
- **Añade jitter** (aleatoriedad) para evitar que muchos clientes reintenten al mismo tiempo (efecto thundering herd).
- **Limita el número máximo de reintentos** (ej: 3-5) y luego falla con un error claro.
- **Respeta el header `Retry-After`** si OpenRouter lo envía. Ese header indica cuántos segundos debes esperar antes del siguiente intento.
- **No reintentes errores 4xx** que no sean 429 (ej: 401, 403, 400). Esos son permanentes y reintentar solo gastará créditos.

---

### 2. Implementación en Python (con `requests`)

Aquí tienes un ejemplo robusto:

```python
import time
import random
import requests

def request_with_retry(url, headers, payload, max_retries=4):
    for attempt in range(max_retries + 1):
        response = requests.post(url, headers=headers, json=payload)

        # Si no es 429, devolvemos la respuesta directamente
        if response.status_code != 429:
            return response

        # Si ya agotamos los intentos, devolvemos el último 429
        if attempt == max_retries:
            return response

        # Calcular espera: respetar Retry-After si existe
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            # Puede venir en segundos o fecha HTTP
            try:
                wait = int(retry_after)
            except ValueError:
                wait = 5  # fallback
        else:
            # Exponential backoff con jitter
            wait = (2 ** attempt) + random.uniform(0, 1)

        print(f"429 recibido. Reintentando en {wait:.2f}s (intento {attempt+1}/{max_retries})")
        time.sleep(wait)

    # Nunca debería llegar aquí, pero por seguridad
    return response
```

**Uso:**

```python
resp = request_with_retry(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={"Authorization": "Bearer TU_API_KEY"},
    payload={"model": "deepseek/deepseek-chat", "messages": [...]}
)
```

---

### 3. Si usas `openai` SDK (OpenRouter es compatible)

Puedes usar el parámetro `max_retries` del cliente:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY",
    max_retries=3,  # reintentos automáticos
)

# El SDK ya maneja backoff y jitter internamente
response = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[{"role": "user", "content": "Hola"}]
)
```

---

### 4. Consejos adicionales

- **Revisa los headers de rate limit** de OpenRouter (`x-ratelimit-remaining`, `x-ratelimit-reset`) para saber cuántas requests te quedan y cuándo se resetea. Puedes usarlos para pausar antes de llegar al límite.
- **Si haces muchas llamadas**, considera usar un **semáforo o cola** para limitar la concurrencia (ej: máximo 2 requests simultáneos).
- **Cachea respuestas** si haces requests repetidas con los mismos parámetros.
- **Monitorea** tus logs para detectar si sigues recibiendo 429. Si es así, puede que necesites reducir la frecuencia o aumentar tu plan.

---

Con esto, tu loop ya no generará 100 requests por cada 429. Si después de implementarlo sigues viendo 429, revisa si tu API key está siendo usada desde varios procesos o si hay algún otro cliente compartiendo la misma key. ¿Quieres que te ayude a revisar el código actual para adaptarlo?