# Muse Wonder — multi_turn/debugging_conversation

- model_id: `meta/muse-wonder`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 12.781s | tokens_per_second: 109.5
- input_tokens: 333 | output_tokens: 1400

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

Perfecto, ya encontramos la causa. Ese loop infinito es el clásico problema: recibes un 429 -> reintentas al instante -> recibes otro 429 -> reintentas... y en segundos te bloqueas solo.

La solución es **Exponential Backoff + Jitter** con un máximo de reintentos. Nunca reintentar al instante ni infinitamente.

Hazlo así:

### 1. Primero, sal del bloqueo actual
Detén tu script por completo y espera 60-120 segundos sin hacer ninguna llamada. Si sigues intentando, el bloqueo se renueva.

### 2. Implementa este patrón de retry (Python)

Este es el estándar que deberías usar:

```python
import requests
import time
import random

def call_openrouter(prompt, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [{"role": "user", "content": prompt}]
    }

    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, json=data)

        # Éxito
        if response.status_code == 200:
            return response.json()

        # Solo reintentamos en 429 y errores de servidor 5xx
        # NO reintentar en 400, 401, 403, 404 (esos nunca se arreglan solos)
        if response.status_code not in [429, 500, 502, 503, 504]:
            print(f"Error no reintentable: {response.status_code} - {response.text}")
            break

        # Último intento, no esperamos más
        if attempt == max_retries - 1:
            print("Se acabaron los reintentos")
            break

        # Respetar el header Retry-After si OpenRouter lo manda
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            wait_time = int(retry_after)
        else:
            # Backoff exponencial: 1s, 2s, 4s, 8s, 16s + jitter aleatorio
            wait_time = (2 ** attempt) + random.uniform(0, 1)

        print(f"Intento {attempt+1} falló con {response.status_code}. Esperando {wait_time:.2f}s...")
        time.sleep(wait_time)

    return None
```

### 3. Las 3 reglas clave

**1. Máximo 5 reintentos:** Nunca `while True:`
**2. Espera creciente:** 1s, 2s, 4s, 8s... no 100 requests por segundo
**3. Jitter (aleatoriedad):** El `random.uniform(0, 1)` evita que si tienes varios procesos, todos reintenten al mismo exacto momento.

Con tus 5 req/min reales, con esto no deberías ver un 429 nunca más.

¿Estás usando Python con `requests` o con el cliente de OpenAI (`from openai import OpenAI`)? Te adapto el código exacto a tu caso si me pegas tu función actual.