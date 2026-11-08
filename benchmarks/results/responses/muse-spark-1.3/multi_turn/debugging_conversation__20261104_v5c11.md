# Muse Spark 1.3 — multi_turn/debugging_conversation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 12.954s | tokens_per_second: 133.8
- input_tokens: 333 | output_tokens: 1733

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

Perfecto, ¡ya encontraste la causa raíz! Eso es muy común: un 429 inicial + un retry infinito = te auto-bloqueas.

No es solo poner un `while True`, necesitas **retries limitados con backoff exponencial**.

Aquí está cómo arreglarlo bien:

### 1. El anti-patrón que tienes ahora
```python
# MAL - esto te mata
while True:
    response = llamar_api()
    if response.status_code == 429:
        continue  # reintenta inmediatamente, 100 veces por segundo
```

### 2. La forma correcta
```python
import time
import random
import requests

MAX_RETRIES = 5  # nunca infinito
BASE_DELAY = 1   # 1 segundo inicial

def llamar_openrouter(payload, headers):
    for attempt in range(MAX_RETRIES):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers
        )

        if response.status_code == 200:
            return response.json()

        # Solo reintenta 429 y 5xx, NO 400, 401, 402, 404
        if response.status_code == 429 or 500 <= response.status_code < 600:
            # 1. Respeta lo que te dice OpenRouter
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait = float(retry_after)
            else:
                # 2. Backoff exponencial + jitter: 1s, 2s, 4s, 8s...
                wait = (BASE_DELAY * (2 ** attempt)) + random.uniform(0, 1)
            
            print(f"Intento {attempt+1}/{MAX_RETRIES} falló con {response.status_code}. Esperando {wait:.1f}s...")
            time.sleep(wait)
            continue
        else:
            # Error no reintentable, sal inmediatamente
            response.raise_for_status()
    
    raise Exception(f"Falló después de {MAX_RETRIES} intentos")
```

### 3. Las 3 reglas de oro

1.  **Límite máximo:** 3 a 5 intentos, nunca `while True`.
2.  **Backoff exponencial:** No reintentes al instante. Espera 1s -> 2s -> 4s -> 8s.
3.  **Respeta `Retry-After`:** Si OpenRouter te manda ese header, esa es la espera obligatoria.

> Tip pro: Si usas Python, la librería `tenacity` ya hace todo esto por ti y es más limpia que un for manual.

Arregla eso primero, espera unos 60 segundos para que tu rate limit se resetee, y luego prueba con 1 sola llamada. Con tus 5 req/min y saldo pagado, DeepSeek V3 debería ir sobrado.

¿Me quieres pegar tu loop actual y te lo reescribo ya corregido?