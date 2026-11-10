# Muse Ember — multi_turn/debugging_conversation

- model_id: `meta/muse-ember`
- success: True  | final: 9.23 | quality: 10.0
- latency_total: 4.592s | tokens_per_second: 474.7
- input_tokens: 333 | output_tokens: 2180

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

Perfecto, encontraste la causa raíz. Eso se llama **retry storm**: un 429 genera otro 429, que genera otro, etc. Y con créditos pagados puede quemarte los $20 rápido.

Primero detén el proceso que está en loop. Luego nunca hagas retry inmediato e infinito.

### Las 3 reglas para un retry correcto

1.  **Máximo de intentos:** Nunca `while True`. Usa `for attempt in range(5)`
2.  **Espera exponencial:** Espera cada vez más: 1s, 2s, 4s, 8s... No reintentes al instante.
3.  **Respeta el `Retry-After` y agrega Jitter:** Si OpenRouter te dice "espera 10s", espera 10s. Y agrégale un poco de aleatoriedad para que no todos tus retries coincidan.

Solo reintenta errores temporales: `429, 500, 502, 503, 504`. Nunca reintentes un `400, 401, 404` porque va a fallar igual.

### Implementación correcta en Python

```python
import time
import random
import requests

MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0  # 1 segundo
MAX_BACKOFF = 60.0     # tope de 60 segundos

session = requests.Session() # Reutiliza la conexión, no crees un cliente nuevo cada vez

def call_openrouter(messages):
    for attempt in range(MAX_RETRIES):
        try:
            response = session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer TU_API_KEY",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek/deepseek-chat-v3-0324", # DeepSeek V3
                    "messages": messages
                },
                timeout=30
            )

            # Éxito
            if response.status_code == 200:
                return response.json()

            # Error temporal: SÍ reintentar, pero esperando
            if response.status_code in [429, 500, 502, 503, 504]:
                # 1. Respetar Retry-After si viene
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                else:
                    # 2. Backoff exponencial: 1, 2, 4, 8...
                    wait = min(MAX_BACKOFF, INITIAL_BACKOFF * (2 ** attempt))
                
                # 3. Jitter: sumar 0 a 1s aleatorio
                wait += random.uniform(0, 1)
                
                print(f"Error {response.status_code}. Reintento {attempt+1}/{MAX_RETRIES} en {wait:.1f}s")
                time.sleep(wait)
                continue

            # Error permanente: NO reintentar
            print(f"Error permanente {response.status_code}: {response.text}")
            response.raise_for_status()

        except requests.RequestException as e:
            # Error de red, también reintentable con espera
            wait = min(MAX_BACKOFF, INITIAL_BACKOFF * (2 ** attempt)) + random.uniform(0, 1)
            print(f"Error de red: {e}. Reintentando en {wait:.1f}s")
            time.sleep(wait)
    
    # Si llega aquí, falló después de todos los intentos
    raise Exception(f"Falló después de {MAX_RETRIES} intentos")
```

### Qué cambió respecto a tu código

**Mal (lo que tenías):**
```python
while True:
    try:
        call_api()
    except:
        continue  # retry inmediato e infinito -> 100 requests en segundos
```

**Bien:**
```python
for attempt in range(5):  # máximo 5 intentos
    ...
    time.sleep(wait)  # espera ANTES de reintentar
```

### Checklist rápido

1.  Detén el loop actual
2.  Revisa en el dashboard de OpenRouter que no se haya drenado tu saldo
3.  Prueba **una sola** llamada manual con curl para confirmar que tu key ya funciona
4.  Reemplaza tu loop por el código de arriba

¿En qué lenguaje estás programando? Si es JavaScript, Java, Go, etc., te adapto el mismo ejemplo.