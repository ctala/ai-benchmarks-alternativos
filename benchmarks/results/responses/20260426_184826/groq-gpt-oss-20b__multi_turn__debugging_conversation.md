# GPT-OSS 20B (Groq) — multi_turn/debugging_conversation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.94 | quality: 8.54
- latency_total: 1.886s | tokens_per_second: 792.0
- input_tokens: 376 | output_tokens: 1494
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Perfecto! Ahora que ya sabemos que el problema viene del **retry infinito**, vamos a estructurar una estrategia de reintentos que:

1. **Evite saturar la API**  
2. **Sea robusta** (mantenga el flujo de datos)  
3. **Respetar los límites de rate‑limit** que la API devuelve en los headers.

---

## 1. Entendiendo los headers de rate‑limit

OpenRouter (y la mayoría de APIs) devuelven algo parecido a:

| Header | Significado |
|--------|-------------|
| `x-ratelimit-limit` | Límite total de requests (ej. 300) |
| `x-ratelimit-remaining` | Requests que aún puedes hacer |
| `x-ratelimit-reset` | Timestamp (en segundos) cuando se reinicia el contador |

**Tip**: Si ves `429` y `Retry-After: 60`, espera 60 s antes de reintentar.

---

## 2. Estrategia de reintentos recomendada

| Paso | Acción | Por qué |
|------|--------|---------|
| 1 | **Captura solo 429** (y opcionalmente 5xx) | Otros errores no se deben reintentar automáticamente. |
| 2 | **Limita el número máximo de reintentos** (p. ej. 5) | Evita loops infinitos. |
| 3 | **Backoff exponencial + jitter** | Reduce la probabilidad de que varios clientes golpeen la API al mismo tiempo. |
| 4 | **Respeta `Retry-After`** | Si la API lo envía, úsalo. |
| 5 | **Revisa `x-ratelimit-remaining`** | Si llega a 0, espera hasta `x-ratelimit-reset`. |

---

## 3. Código de ejemplo (Python)

```python
import time
import random
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "TU_API_KEY"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

MAX_RETRIES = 5
BASE_BACKOFF = 1.0      # segundos
JITTER = 0.5            # segundos

def call_openrouter(payload):
    attempt = 0
    while attempt <= MAX_RETRIES:
        try:
            resp = requests.post(API_URL, json=payload, headers=HEADERS, timeout=10)

            # Si todo sale bien, devuelve el JSON
            if resp.status_code == 200:
                return resp.json()

            # 429 → reintentar
            if resp.status_code == 429:
                attempt += 1
                # 1. Si hay Retry-After, úsalo
                retry_after = resp.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                    print(f"[WARN] 429 recibido. Esperando {wait}s (Retry-After).")
                    time.sleep(wait)
                else:
                    # 2. Si no hay header, usar backoff exponencial + jitter
                    backoff = BASE_BACKOFF * (2 ** (attempt - 1))
                    backoff += random.uniform(0, JITTER)
                    print(f"[WARN] 429 recibido. Esperando {backoff:.2f}s (backoff).")
                    time.sleep(backoff)

                # 3. Si el límite se agotó, esperar hasta reset
                if resp.headers.get("x-ratelimit-remaining") == "0":
                    reset_ts = int(resp.headers.get("x-ratelimit-reset", time.time() + 60))
                    wait_until = reset_ts - time.time()
                    if wait_until > 0:
                        print(f"[INFO] Límite alcanzado. Esperando {wait_until:.0f}s hasta reset.")
                        time.sleep(wait_until)

                continue  # vuelve al bucle

            # 5xx → reintentar (opcional)
            if 500 <= resp.status_code < 600:
                attempt += 1
                backoff = BASE_BACKOFF * (2 ** (attempt - 1))
                backoff += random.uniform(0, JITTER)
                print(f"[WARN] Error {resp.status_code}. Esperando {backoff:.2f}s.")
                time.sleep(backoff)
                continue

            # Otros códigos → lanzar excepción
            resp.raise_for_status()

        except requests.exceptions.RequestException as e:
            # Timeout, DNS, etc. -> reintentar
            attempt += 1
            backoff = BASE_BACKOFF * (2 ** (attempt - 1))
            backoff += random.uniform(0, JITTER)
            print(f"[ERROR] {e}. Esperando {backoff:.2f}s.")
            time.sleep(backoff)

    raise RuntimeError(f"No se pudo completar la llamada después de {MAX_RETRIES} reintentos.")
```

### Cómo usarlo

```python
payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "Hola, ¿cómo estás?"}
    ]
}

try:
    result = call_openrouter(payload)
    print(result)
except RuntimeError as err:
    print(f"Error final: {err}")
```

---

## 4. Buenas prácticas adicionales

| Tema | Recomendación |
|------|---------------|
| **Batching** | Si necesitas varias respuestas, considera usar `messages` con varios prompts en una sola llamada (si el modelo lo permite). |
| **Cache** | Guarda respuestas ya obtenidas (por ejemplo, en Redis) y reutilízalas si el prompt es idéntico. |
| **Rate‑limit monitoring** | Almacena en un log `x-ratelimit-remaining` y `x-ratelimit-reset` para alertas tempranas. |
| **Parallelism** | Si tu aplicación hace muchas llamadas simultáneas, limita el número de hilos/async tasks (p. ej. 10 concurrentes). |
| **Testing** | Usa un mock de la API con los mismos headers para probar tu lógica de reintentos antes de ir a producción. |

---

## 5. Resumen rápido

1. **No reintentes indefinidamente**. Limita a 5–10 intentos.  
2. **Respeta `Retry-After`** si está presente.  
3. **Backoff exponencial + jitter** reduce la congestión.  
4. **Observa los headers de rate‑limit** y espera al reset cuando sea necesario.  
5. **Registra** cada reintento para poder depurar si el problema persiste.

Con esta implementación deberías dejar de recibir 429s y mantener tu flujo de datos estable. ¡Éxitos! 🚀