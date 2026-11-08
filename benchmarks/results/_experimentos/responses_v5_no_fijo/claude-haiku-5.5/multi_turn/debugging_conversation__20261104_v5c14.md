# Claude Haiku 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 8.01s | tokens_per_second: 218.0
- input_tokens: 541 | output_tokens: 1746

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

Encontraste la causa. Un retry infinito sin pausa convierte un 429 aislado en una avalancha de requests, y eso casi siempre mantiene el error activo. Tambien debo corregir algo: antes te dije que el limite es 300 RPM, pero los limites de OpenRouter y de cada proveedor cambian y dependen del modelo y de tu cuenta. Revisa los headers `x-ratelimit-*` o la documentacion actual en lugar de confiar en ese numero.

**Primero, detén el loop** para que deje de consumir requests.

## Como implementar retries correctamente

Un retry bien hecho necesita cinco cosas:

1. **Un limite maximo de intentos**
2. **Espera exponencial** entre intentos (cada espera mas larga que la anterior)
3. **Jitter** (un poco de aleatoriedad) para que varios clientes no reintenten al mismo tiempo
4. **Respetar `Retry-After`** si el servidor lo envia
5. **Reintentar solo errores temporales** (429, 500, 502, 503, 504), no errores como 400 o 401

Ejemplo en Python:

```python
import os
import time
import random
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ["OPENROUTER_API_KEY"]

RETRYABLE = {429, 500, 502, 503, 504}
MAX_RETRIES = 5
BASE_DELAY = 1.0   # segundos
MAX_DELAY = 60.0   # tope de espera

def call_openrouter(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        except requests.RequestException as e:
            if attempt == MAX_RETRIES:
                raise
            wait = min(MAX_DELAY, BASE_DELAY * 2 ** attempt) + random.uniform(0, 1)
            print(f"Error de red ({e}). Reintento en {wait:.1f}s...")
            time.sleep(wait)
            continue

        if resp.status_code == 200:
            return resp.json()

        if resp.status_code not in RETRYABLE or attempt == MAX_RETRIES:
            # Error no recuperable o se agotaron los intentos
            resp.raise_for_status()

        # Prioridad 1: Retry-After si el servidor lo envia
        retry_after = resp.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            wait = float(retry_after)
        else:
            # Prioridad 2: backoff exponencial con jitter
            wait = min(MAX_DELAY, BASE_DELAY * 2 ** attempt) + random.uniform(0, 1)

        print(f"HTTP {resp.status_code}. Intento {attempt + 1}/{MAX_RETRIES}. Espero {wait:.1f}s")
        time.sleep(wait)
```

## Puntos clave

- **El `for` tiene un techo fijo.** Nunca uses `while True` sin una salida.
- **Un 429 no es un error de tu codigo, es una señal de "ve mas lento".** Por eso el retry debe esperar, no reenviar de inmediato.
- **Si el 429 persiste tras varios intentos**, no sigas reintentando: registra el error, reduce la concurrencia o pon la tarea en una cola para mas tarde.

## Para verificar despues

- Si usas concurrencia (threads, asyncio, workers), limita cuantas requests pueden estar en vuelo al mismo tiempo. Un semaforo o cola suele bastar.
- Imprime los headers `x-ratelimit-*` de una respuesta exitosa para ver tus limites reales.
- Revisa el cuerpo del 429. OpenRouter a veces devuelve un mensaje que indica si el limite viene de tu cuenta o del proveedor upstream de DeepSeek, lo cual cambia la solucion.

Si me dices en que lenguaje estas programando (Python, JavaScript, etc.) y como hacias los retries antes, te ayudo a adaptar el codigo a tu caso.