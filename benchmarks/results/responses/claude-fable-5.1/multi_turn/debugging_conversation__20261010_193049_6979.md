# Claude Fable 5.1 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 19.134s | tokens_per_second: 68.4
- input_tokens: 541 | output_tokens: 1308

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

Ahi esta el problema. Un retry infinito contra un 429 es un circulo vicioso: cada reintento inmediato cuenta contra el limite, lo que genera mas 429s, lo que genera mas reintentos. Terminas auto-bloqueandote.

Un retry bien hecho necesita 4 cosas:

1. **Limite de intentos** (3-5 maximo, nunca infinito)
2. **Exponential backoff** - esperar cada vez mas entre intentos (1s, 2s, 4s, 8s...)
3. **Jitter** - un poco de aleatoriedad para no sincronizar reintentos
4. **Respetar `Retry-After`** - si el servidor te dice cuanto esperar, hazle caso

Ejemplo en Python (adaptable a cualquier lenguaje):

```python
import time
import random
import requests

def call_openrouter(payload, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)

        # Exito
        if response.status_code == 200:
            return response.json()

        # Errores que NO vale la pena reintentar (tu culpa, no del servidor)
        if response.status_code in (400, 401, 403, 404):
            raise Exception(f"Error no recuperable: {response.status_code} - {response.text}")

        # Errores reintentables: 429, 500, 502, 503, 504
        if response.status_code == 429 or response.status_code >= 500:
            # Si el servidor dice cuanto esperar, obedecer
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait = float(retry_after)
            else:
                # Backoff exponencial: 1, 2, 4, 8, 16 segundos...
                wait = (2 ** attempt) + random.uniform(0, 1)  # jitter

            print(f"Intento {attempt + 1}/{max_retries} fallo ({response.status_code}). Esperando {wait:.1f}s...")
            time.sleep(wait)
            continue

        # Cualquier otro codigo inesperado
        raise Exception(f"Error inesperado: {response.status_code}")

    raise Exception(f"Fallo despues de {max_retries} intentos")
```

Puntos clave:

- **No reintentes 4xx excepto 429.** Un 400 o 401 va a fallar igual 100 veces; reintentar solo quema tiempo y creditos.
- **El `Retry-After` tiene prioridad.** OpenRouter a veces lo manda y es la fuente mas confiable.
- **Loggea cada intento.** Asi la proxima vez ves el patron en segundos, no horas.
- **Considera un circuit breaker** si esto corre en produccion: si fallan N requests seguidas, para todo por un minuto en vez de seguir golpeando.

Si prefieres no escribir esto a mano, librerias como `tenacity` (Python) o `p-retry` (Node) lo hacen en 3 lineas y estan bien probadas.

Una vez que arregles el loop, espera unos minutos antes de probar - probablemente tienes un rate limit temporal acumulado por la avalancha de requests. En que lenguaje esta tu codigo? Si no es Python te lo adapto.