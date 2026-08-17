# GPT-5.6 Terra Pro — multi_turn/debugging_conversation

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 24.91s | tokens_per_second: 202.1
- input_tokens: 7381 | output_tokens: 5034

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

El problema es el retry infinito: un `429` debería provocar una espera controlada, no volver a intentar inmediatamente.

Implementa estas reglas:

1. **Máximo de intentos**: por ejemplo 3–5.
2. **Respeta `Retry-After`** si el servidor lo devuelve.
3. Si no existe, usa **backoff exponencial con jitter**.
4. Reintenta solo errores temporales:
   - `429`
   - `408`
   - `500`, `502`, `503`, `504`
   - errores de red/timeouts
5. **No reintentes** errores como `400`, `401`, `403`, `404` o errores de validación.
6. Asegúrate de que no haya retries en dos capas a la vez (por ejemplo, tu código *y* la librería HTTP).

Ejemplo en Python:

```python
import random
import time
import requests

RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}
MAX_RETRIES = 5

def call_openrouter(payload, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=60,
            )

            # Éxito
            if response.ok:
                return response.json()

            # Error no recuperable: no reintentar
            if response.status_code not in RETRYABLE_STATUS:
                response.raise_for_status()

            # Ya agotamos los intentos
            if attempt == MAX_RETRIES:
                response.raise_for_status()

            # Prioridad: usar Retry-After del servidor si existe
            retry_after = response.headers.get("Retry-After")

            if retry_after:
                try:
                    wait_seconds = float(retry_after)
                except ValueError:
                    wait_seconds = 0
            else:
                # 1, 2, 4, 8, 16 segundos + jitter aleatorio
                base_delay = min(2 ** attempt, 30)
                jitter = random.uniform(0, 1)
                wait_seconds = base_delay + jitter

            print(
                f"HTTP {response.status_code}. "
                f"Reintentando en {wait_seconds:.2f}s "
                f"({attempt + 1}/{MAX_RETRIES})"
            )
            time.sleep(wait_seconds)

        except (requests.Timeout, requests.ConnectionError) as exc:
            if attempt == MAX_RETRIES:
                raise

            base_delay = min(2 ** attempt, 30)
            wait_seconds = base_delay + random.uniform(0, 1)

            print(f"Error de red: {exc}. Reintentando en {wait_seconds:.2f}s")
            time.sleep(wait_seconds)

    raise RuntimeError("No debería llegar aquí")
```

Para un `429`, la secuencia sería aproximadamente:

```text
Intento 1 → espera 1–2 s
Intento 2 → espera 2–3 s
Intento 3 → espera 4–5 s
Intento 4 → espera 8–9 s
Intento 5 → falla definitivamente
```

Además, si haces llamadas concurrentes, añade un límite de concurrencia o una cola. Aunque tu promedio sea 5 RPM, podrías estar enviando ráfagas simultáneas que activan límites. Por ejemplo, limita a 1–3 requests concurrentes.

Lo importante: tras agotar los retries, registra el error y devuélvelo al usuario o a tu sistema de colas; **nunca vuelvas a entrar automáticamente en un loop infinito**.