# Claude Opus 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 21.172s | tokens_per_second: 103.2
- input_tokens: 541 | output_tokens: 2185

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

Ese loop multiplica tu tráfico justo cuando el servidor te pide que bajes el ritmo, así que el rate limit nunca se libera.

**Una corrección:** antes te dije que el límite era 300 RPM, pero no debí darlo como cifra exacta. Los límites de OpenRouter dependen del modelo, del tipo de cuenta y del proveedor que sirve el modelo. Un 429 también puede venir del proveedor (por ejemplo, DeepSeek saturado) y no de tu cuenta. Revisa la documentación actual de OpenRouter y los headers de la respuesta para ver tus límites reales.

## Principios de un retry correcto

1. **Límite de intentos**: nunca infinito. Entre 3 y 5 suele bastar.
2. **Backoff exponencial**: esperar 1s, 2s, 4s, 8s... entre intentos.
3. **Jitter**: añadir aleatoriedad a la espera para que varios procesos no reintenten al mismo tiempo.
4. **Respetar `Retry-After`**: si el servidor indica cuánto esperar, usar ese valor.
5. **Reintentar solo errores transitorios**:
   - ✅ Reintentar: `429`, `500`, `502`, `503`, `504`, timeouts y errores de red
   - ❌ No reintentar: `400` (request mal formado), `401` (key inválida), `402` (sin créditos), `404`. Reintentarlos no cambia nada.

## Implementación en Python

```python
import time
import random
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def call_openrouter(payload, api_key, max_retries=5, base_delay=1.0, max_delay=60.0):
    headers = {"Authorization": f"Bearer {api_key}"}

    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=60)
        except (requests.Timeout, requests.ConnectionError) as e:
            if attempt == max_retries:
                raise
            wait = min(max_delay, base_delay * 2 ** attempt) * random.uniform(0.5, 1.5)
            print(f"Error de red ({e}), reintento {attempt + 1} en {wait:.1f}s")
            time.sleep(wait)
            continue

        if resp.ok:
            return resp.json()

        # Errores no reintentables: fallar de inmediato
        if resp.status_code not in RETRYABLE_STATUS:
            raise RuntimeError(f"Error {resp.status_code}: {resp.text}")

        if attempt == max_retries:
            raise RuntimeError(f"Agotados {max_retries} reintentos. Último: {resp.status_code} {resp.text}")

        # Respetar Retry-After si viene; si no, backoff exponencial con jitter
        retry_after = resp.headers.get("Retry-After")
        if retry_after and retry_after.isdigit():
            wait = float(retry_after)
        else:
            wait = min(max_delay, base_delay * 2 ** attempt) * random.uniform(0.5, 1.5)

        print(f"{resp.status_code} recibido, reintento {attempt + 1}/{max_retries} en {wait:.1f}s")
        time.sleep(wait)
```

Uso:

```python
result = call_openrouter(
    {"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "Hola"}]},
    api_key="sk-or-...",
)
```

## Alternativas más simples

**Si usas el SDK de OpenAI** (compatible con OpenRouter), ya trae retries con backoff incluidos:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
    max_retries=5,   # backoff automático en 429 y 5xx
    timeout=60,
)
```

**La librería `tenacity`** permite hacer lo mismo con decoradores, si prefieres no escribir el loop a mano.

## Recomendaciones extra

- **Espera unos minutos antes de probar.** Si el loop estuvo generando cientos de requests, puede que sigas limitado un rato.
- **Si el 429 viene del proveedor**, OpenRouter permite definir modelos de respaldo para que, si DeepSeek está saturado, use otro:
  ```python
  {"models": ["deepseek/deepseek-chat", "otro/modelo-respaldo"], "messages": [...]}
  ```
- **Registra cada reintento** (como hacen los `print` del ejemplo). Así habrías detectado el loop infinito enseguida.

¿Qué librería estás usando para las llamadas? Si me muestras tu código actual, te ayudo a adaptarlo.