# GPT-OSS 120B — multi_turn/debugging_conversation

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.91 | quality: 10.0
- latency_total: 42.273s | tokens_per_second: 48.4
- input_tokens: 371 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la implementación de una política de retry robusta, ofreciendo una solución práctica y detallada que un emprendedor podría aplicar directamente.

## Respuesta completa

### ✅ Qué está pasando
- Cuando recibes **429 Too Many Requests** tu código entra en un *retry* inmediato.  
- Cada retry vuelve a lanzar otro **429**, lo que dispara otro retry, y así sucesivamente → **infinite loop** que dispara cientos de peticiones en segundos y vuelve a saturar el límite.

### 🎯 Qué debe hacer un buen “retry policy”

| Paso | Qué hacer | Por qué |
|------|-----------|----------|
| 1️⃣ Detectar el error correcto | Sólo volver a intentar **429** (y opcionalmente **5xx** temporales). | Otros errores (4xx, 401, 404…) son definitivos. |
| 2️⃣ Leer `Retry-After` (si existe) | Si el servidor envía `Retry-After: <seconds>` o una fecha HTTP, espera ese tiempo antes de re‑intentar. | El propio OpenRouter te está indicando cuánto tiempo debes esperar. |
| 3️⃣ Aplicar **exponential backoff** con **jitter** | `delay = base * 2**attempt` (ej. base = 1 s) + un pequeño ruido aleatorio (±30 %). | Evita “thundering herd” y da tiempo al servidor para recuperarse. |
| 4️⃣ Limitar **máximo de intentos** | Por ejemplo `max_attempts = 5`. | Evita bucles infinitos y permite que tu aplicación falle de forma controlada. |
| 5️⃣ Registrar/monitorizar | Loggear cada intento, código de respuesta y tiempo de espera. | Te ayuda a detectar patrones y a ajustar los límites. |
| 6️⃣ (Opcional) **Circuit‑breaker** | Después de varios fallos consecutivos, “abrir” el circuito y detener retries por un tiempo mayor (p.ej. 1 min). | Previene que una caída del servicio consuma todos tus recursos. |

---

## 📦 Implementación práctica (Python)

A continuación tienes una función genérica que puedes reutilizar en cualquier proyecto que use `requests`.  
Si usas otro lenguaje (Node, Go, etc.) la lógica es la misma; al final del mensaje incluyo ejemplos breves para JavaScript.

```python
import time
import random
import logging
import requests
from typing import Any, Dict

# -------------------------------------------------
# Configurable retry policy
# -------------------------------------------------
BASE_DELAY = 1.0            # segundos (primer retry)
MAX_DELAY = 60.0            # límite superior del backoff
MAX_ATTEMPTS = 5            # número máximo de reintentos
JITTER_FACTOR = 0.3         # ±30 % de jitter

log = logging.getLogger(__name__)

def _sleep_with_jitter(delay: float) -> None:
    """Aplica jitter aleatorio al delay y duerme."""
    jitter = delay * JITTER_FACTOR
    delay = random.uniform(delay - jitter, delay + jitter)
    log.debug(f"Sleeping {delay:.2f}s before next retry")
    time.sleep(delay)

def openrouter_chat(
    api_key: str,
    model: str,
    messages: list,
    **extra_payload: Any,
) -> Dict[str, Any]:
    """
    Llama a la API de OpenRouter con política de retry robusta.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # Opcional: identifica tu aplicación
        "X-OpenAI-Client-User-Agent": "my‑app/1.0",
    }
    payload = {
        "model": model,
        "messages": messages,
        **extra_payload,
    }

    attempt = 0
    while True:
        attempt += 1
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=30)
        except requests.RequestException as exc:
            # Errores de red (timeout, DNS, etc.) → consideramos retry
            log.warning(f"Network error on attempt {attempt}: {exc}")
            if attempt >= MAX_ATTEMPTS:
                raise
            _sleep_with_jitter(min(BASE_DELAY * 2 ** (attempt - 1), MAX_DELAY))
            continue

        # -------------------------------------------------
        # 1️⃣ 429 → Too Many Requests
        # -------------------------------------------------
        if response.status_code == 429:
            log.warning(f"429 received (attempt {attempt})")
            # 1️⃣ leer Retry-After si está presente
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    # Si es una fecha HTTP, conviértela a segundos
                    from email.utils import parsedate_to_datetime
                    retry_dt = parsedate_to_datetime(retry_after)
                    delay = max(0, (retry_dt - datetime.datetime.utcnow()).total_seconds())
            else:
                # 2️⃣ backoff exponencial + jitter
                delay = min(BASE_DELAY * 2 ** (attempt - 1), MAX_DELAY)

            if attempt >= MAX_ATTEMPTS:
                log.error("Max retries reached after 429")
                response.raise_for_status()   # lanza HTTPError 429
            _sleep_with_jitter(delay)
            continue   # reintenta

        # -------------------------------------------------
        # 5xx (p.ej. 502, 503, 504) → errores temporales del servidor
        # -------------------------------------------------
        if 500 <= response.status_code < 600:
            log.warning(f"{response.status_code} server error (attempt {attempt})")
            if attempt >= MAX_ATTEMPTS:
                response.raise_for_status()
            _sleep_with_jitter(min(BASE_DELAY * 2 ** (attempt - 1), MAX_DELAY))
            continue

        # -------------------------------------------------
        # 2xx → éxito
        # -------------------------------------------------
        if response.ok:
            return response.json()

        # -------------------------------------------------
        # Otros 4xx (p.ej. 401, 403, 404) → no deben reintentarse
        # -------------------------------------------------
        log.error(
            f"Non‑retriable error {response.status_code}: {response.text}"
        )
        response.raise_for_status()
```

### Cómo usarla

```python
api_key = "sk-...."
model   = "deepseek/deepseek-v3"
messages = [
    {"role": "system", "content": "Eres un asistente útil."},
    {"role": "user",   "content": "¿Cuál es la capital de Francia?"}
]

try:
    result = openrouter_chat(api_key, model, messages)
    print(result["choices"][0]["message"]["content"])
except requests.HTTPError as e:
    print(f"Fallo definitivo: {e}")
```

---

## 📦 Variante rápida (si ya usas `httpx` o `aiohttp`)

```python
import httpx, asyncio, random, time

async def chat_async(api_key, model, messages):
    async with httpx.AsyncClient(timeout=30) as client:
        attempt = 0
        while True:
            attempt += 1
            try:
                r = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    json={"model": model, "messages": messages},
                    headers={"Authorization": f"Bearer {api_key}"}
                )
            except httpx.RequestError as exc:
                if attempt >= 5: raise
                await asyncio.sleep(min(1 * 2 ** (attempt-1), 60) *
                                   random.uniform(0.7, 1.3))
                continue

            if r.status_code == 429:
                retry_after = r.headers.get("Retry-After")
                delay = float(retry_after) if retry_after else min(1 * 2 ** (attempt-1), 60)
                if attempt >= 5: r.raise_for_status()
                await asyncio.sleep(delay * random.uniform(0.7, 1.3))
                continue

            if 500 <= r.status_code < 600:
                if attempt >= 5: r.raise_for_status()
                await asyncio.sleep(min(1 * 2 ** (attempt-1), 60) *
                                   random.uniform(0.7, 1.3))
                continue

            r.raise_for_status()
            return r.json()
```

---

## 🛠️ Pasos concretos para **arreglar tu código actual**

1. **Identifica el bucle de retry**  
   Busca algo como:

   ```python
   while True:
       resp = requests.post(...)
       if resp.status_code == 429:
           continue          # <-- aquí está el bucle infinito
   ```

2. **Reemplázalo** por la lógica anterior (o por tu propia variante con backoff).  
   Lo esencial es:
   ```python
   if resp.status_code == 429:
       retry_after = resp.headers.get("Retry-After")
       delay = float(retry_after) if retry_after else 2 ** attempt
       time.sleep(delay + random jitter)
       attempt += 1
       if attempt > MAX_ATTEMPTS: raise
   ```

3. **Añade un contador de intentos** (`attempt`) y una condición de salida (`if attempt > MAX_ATTEMPTS`).