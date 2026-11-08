# MiMo V2.6 Pro — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 19.175s | tokens_per_second: 36.8
- input_tokens: 357 | output_tokens: 705

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

Ahi esta el problema - el retry infinito te pone en una espiral que empeora el rate limit. Vamos a arreglarlo con exponential backoff.

## La estrategia correcta

1. **Maximo de intentos limitado** (ej: 3-5)
2. **Exponencial backoff** - esperar mas en cada retry
3. **Jitter** - agregar aleatoriedad para evitar "thundering herd"
4. **Respetar el header `Retry-After`** si el servidor lo envia

## Ejemplo en Python

```python
import time
import random
import requests

def llamar_con_retry(payload, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 429:
            # Si el servidor dice cuanto esperar, usarlo
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait = float(retry_after)
            else:
                # Exponencial: 2^attempt + jitter aleatorio
                wait = (2 ** attempt) + random.uniform(0, 1)

            print(f"429 recibido. Reintento {attempt + 1}/{max_retries} en {wait:.1f}s")
            time.sleep(wait)
            continue

        if response.status_code >= 500:
            # Error del servidor, tambien vale la pena reintentar
            wait = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait)
            continue

        # 200 u otro error (400, 401...) - no reintentar
        return response.json()

    raise Exception(f"Failed after {max_retries} retries")
```

## Puntos clave

- **Nunca reintentar en errores 4xx** (400, 401, 403) - no van a cambiar
- **Backoff real**: 1s, 2s, 4s, 8s, 16s - no un loop agresivo
- **Logging** - siempre imprimir cuando haces un retry para ver que pasa
- **Circuit breaker** opcional - si llevas varios fallos seguidos, parar de golpe y reportar error

Si usas un framework como `tenacity` o `backoff`, todo esto se simplifica:

```python
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(
    wait=wait_exponential(multiplier=1, max=30),
    stop=stop_after_attempt(5)
)
def llamar_api(payload):
    ...
```

Con esto tu rate limit deberia estabilizarse rapido - una vez que elimines el loop infinito, el 429 probablemente ni aparezca.