# GPT-OSS 120B (Ollama Cloud) — multi_turn/debugging_conversation

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.85 | quality: 8.86
- latency_total: 23.917s | tokens_per_second: 85.6
- input_tokens: 377 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

## 🚦 Por qué tu “retry infinito” explota el límite

Cuando recibes **429 Too Many Requests** la API te está diciendo *“¡Alto! ya superaste el número permitido en este intervalo”*.  
Si tu código vuelve a intentar **de inmediato** (y sin contar cuántas veces ya lo hizo), cada 429 genera **otra petición** que vuelve a ser 429 → se convierte en una bola de nieve que rápidamente supera los límites (100 req ≈ cada 429, como viste).

Para que el retry sea útil debe:

| Paso | Qué hacer | Por qué |
|------|-----------|--------|
| 1️⃣ | **Detectar 429** y leer el header `Retry‑After` (si está presente). | La API te indica cuánto tiempo esperar antes de volver a intentar. |
| 2️⃣ | **Esperar** al menos ese tiempo (o un tiempo razonable si el header falta). | Evita volver a golpear el límite antes de que se “resetee”. |
| 3️⃣ | **Aplicar back‑off exponencial** (y jitter). | Cada intento fallido espera más, evitando que varios procesos simultáneos vuelvan a saturar el endpoint. |
| 4️⃣ | **Limitar el número máximo de intentos** (p.ej. 3‑5). | Si sigue fallando, es mejor que el cliente falle y el operador lo revisa. |
| 5️⃣ | **Registrar** cada intento y el motivo del fallo. | Facilita el debugging y la observabilidad. |
| 6️⃣ | (Opcional) **Circuit‑breaker**: si se supera un umbral de fallos en X segundos, pausa los intentos por un período mayor. | Protege tu aplicación de “cascadas” cuando la API está realmente saturada. |

---

## 📦 Implementación práctica (Python)

A continuación tienes una plantilla reutilizable usando **`httpx`** (pero funciona igual con `requests`, `aiohttp`, etc.) y la librería **`tenacity`** para el back‑off.  

```python
import time
import logging
from typing import Optional

import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    wait_random,
    retry_if_exception_type,
    before_sleep_log,
)

# -------------------------------------------------
# Configuración básica
# -------------------------------------------------
API_KEY = "sk-..."                     # tu clave pagada
BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "deepseek/deepseek-v3"          # modelo que usas
MAX_RETRIES = 5                        # número máximo de reintentos
logger = logging.getLogger("openrouter")
logging.basicConfig(level=logging.INFO)

# -------------------------------------------------
# Helper: extrae el header Retry-After (segundos)
# -------------------------------------------------
def _get_retry_after(response: httpx.Response) -> Optional[int]:
    """Devuelve el número de segundos indicado en `Retry-After` o None."""
    ra = response.headers.get("Retry-After")
    if ra is None:
        return None
    try:
        # Puede ser un número entero (segundos) o una fecha HTTP‑date
        return int(ra)
    except ValueError:
        # Si es una fecha, conviértela a segundos restantes
        from email.utils import parsedate_to_datetime
        dt = parsedate_to_datetime(ra)
        return max(0, int((dt - datetime.datetime.now(datetime.timezone.utc)).total_seconds()))


# -------------------------------------------------
# Decorador de retry con Tenacity
# -------------------------------------------------
def _is_retryable_exception(exc: Exception) -> bool:
    """Solo reintentamos si la respuesta fue 429."""
    if isinstance(exc, httpx.HTTPStatusError):
        return exc.response.status_code == 429
    return False


def retry_on_429(fn):
    """Aplica retry con back‑off exponencial + jitter y respeta Retry-After."""
    @retry(
        retry=retry_if_exception_type(httpx.HTTPStatusError).filter(_is_retryable_exception),
        stop=stop_after_attempt(MAX_RETRIES),
        wait=wait_exponential(multiplier=1, min=1, max=60) + wait_random(0, 1),  # 1‑2‑4‑8‑… s + jitter
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True,
    )
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


# -------------------------------------------------
# Función que hace la llamada real
# -------------------------------------------------
@retry_on_429
def call_openrouter(messages: list[dict]) -> dict:
    """Ejecuta una petición a /chat/completions y maneja 429."""
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        # (opcional) puedes limitar tokens, temperature, etc.
    }

    with httpx.Client(timeout=30) as client:
        response = client.post(url, json=payload, headers=headers)

        # Si la respuesta es 429, lanzamos una excepción que Tenacity atrapará
        if response.status_code == 429:
            # Si la API envía Retry-After, esperemos *exactamente* ese tiempo antes de fallar
            ra_seconds = _get_retry_after(response)
            if ra_seconds:
                logger.warning(f"429 recibido – respetando Retry-After={ra_seconds}s")
                time.sleep(ra_seconds)
            # Levantamos la excepción para que el decorador vuelva a intentar
            response.raise_for_status()

        # Para cualquier otro error HTTP (5xx, 4xx distinto de 429) lanzamos excepción normal
        response.raise_for_status()
        return response.json()


# -------------------------------------------------
# Uso de la función
# -------------------------------------------------
if __name__ == "__main__":
    prueba = [
        {"role": "system", "content": "Eres un asistente amable."},
        {"role": "user", "content": "Dime una curiosidad sobre el ajedrez."},
    ]

    try:
        result = call_openrouter(prueba)
        print("Respuesta:", result["choices"][0]["message"]["content"])
    except httpx.HTTPStatusError as e:
        logger.error(f"Falló la petición después de reintentos: {e}")
```

### Qué hace este código paso a paso

1. **`retry_on_429`**: decorador que solo vuelve a intentar cuando la excepción tiene status 429.  
2. **Back‑off exponencial** (`wait_exponential`) → 1 s, 2 s, 4 s, 8 s … con un **jitter aleatorio** de 0‑1 s para que varios procesos concurrentes no se sincronicen.  
3. **`MAX_RETRIES = 5`** → si después de 5 intentos sigue 429, la excepción se propaga y tu aplicación puede decidir qué hacer (por ejemplo, registrar un error crítico y notificar al operador).  
4. **`Retry-After`**: si el servidor indica cuántos segundos esperar, el cliente duerme exactamente ese tiempo **antes** de lanzar la excepción, de modo que el próximo intento llegue después del “reset”.  
5. **Registro** (`logging`) en cada pausa, para que tengas trazas claras en tus logs.

---

## 🛠️ Si prefieres no usar una librería externa (solo `requests`)

```python
import time, logging, requests

MAX_RETRIES = 5
BASE_DELAY = 1      # segundos
MAX_DELAY  = 60

def call(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"model": MODEL, "messages": messages}

    for attempt in range(1, MAX_RETRIES + 1):
        r = requests.post(url, json=payload, headers=headers)

        if r.status_code == 200:
            return r.json()                     # éxito

        if r.status_code != 429:
            r.raise_for_status()               # otro error → no reintentamos

        # ----- 429 -------------------------------------------------
        retry_after = r.headers.get("Retry-After")
        if retry_after:
            wait = int(retry_after)
        else:
            # back‑off exponencial + jitter
            wait = min(BASE_DELAY * (2 ** (attempt - 1)), MAX_DELAY)
            wait += random.random()            # jitter 0‑1 s

        logging.warning(
            f"[{attempt}/{MAX_RETRIES}] 429 recibido. Esperando {wait:.2f}s..."
        )
        time.sleep(wait)

    # Si llegamos aquí, agotamos los reintentos
    raise RuntimeError("Excedido número máximo de reintentos (429).")
```

### Puntos clave de este fragmento

| Elemento | Detalle |
|----------|---------|
| `MAX_RETRIES` | Evita bucles infinitos. |
| `Retry-After` | Respeta la