# GPT-OSS 20B — multi_turn/debugging_conversation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 25.053s | tokens_per_second: 68.2
- input_tokens: 376 | output_tokens: 1708
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada y estructurada para manejar errores 429, incluyendo estrategias como back-off exponencial y el uso de cabeceras HTTP, lo que la hace altamente útil y clara.

## Respuesta completa

### Solución paso a paso para evitar un *retry infinito* con OpenRouter (DeepSeek V3)

| # | Acción | Por qué |
|---|--------|---------|
| 1 | **Analiza los headers de la respuesta 429** | `Retry-After` (segundos) o `x-ratelimit-reset` indicará exactamente cuántos segundos debes esperar antes de volver a intentar. |
| 2 | **Define un número máximo de reintentos** | Evita ciclos infinitos. 3‑5 reintentos suele ser suficiente. |
| 3 | **Aplica back‑off exponencial + jitter** | Reduce la presión sobre el servidor y evita que varios clientes se sincronicen. |
| 4 | **Respeta la cabecera `Retry-After` cuando esté presente** | Si el servidor indica un tiempo, úsalo. |
| 5 | **Log y alerta** | Registra cada reintento y la razón. Si el número máximo se alcanza, lanza una excepción clara. |
| 6 | **Prueba localmente** | Asegúrate de que la lógica funciona con un mock de la API antes de subirla a producción. |

---

## 1. ¿Qué información extra nos dan los headers?

```text
HTTP/1.1 429 Too Many Requests
Retry-After: 30               # segundos a esperar
x-ratelimit-limit: 300        # límite de requests por minuto
x-ratelimit-remaining: 0      # restantes en este periodo
x-ratelimit-reset: 162753...  # timestamp UTC del reset
```

- **`Retry-After`**: Si está presente, es el valor a usar.
- **`x-ratelimit-reset`**: Si no hay `Retry-After`, puedes usar la diferencia entre ese timestamp y `now`.

---

## 2. Código de ejemplo (Python, sin librerías externas)

```python
import time
import requests
from datetime import datetime

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "sk-..."          # tu clave real
MODEL   = "deepseek-v3"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "OpenRouter-Model": MODEL,
}

MAX_RETRIES = 5            # número máximo de reintentos
BACKOFF_BASE = 1.0         # segundos base para back‑off exponencial
JITTER_RANGE = 0.5         # segundos de jitter aleatorio

def get_retry_after(response: requests.Response) -> float | None:
    """Devuelve el número de segundos que debe esperar el cliente."""
    # 1. Retry-After (segundos)
    if "Retry-After" in response.headers:
        try:
            return float(response.headers["Retry-After"])
        except ValueError:
            pass

    # 2. x-ratelimit-reset (timestamp)
    if "x-ratelimit-reset" in response.headers:
        try:
            reset_ts = int(response.headers["x-ratelimit-reset"])
            now_ts   = int(time.time())
            delay    = reset_ts - now_ts
            return max(delay, 0)
        except ValueError:
            pass

    return None  # no hay sugerencia

def request_with_retries(payload: dict) -> dict:
    attempt = 0
    while attempt <= MAX_RETRIES:
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code < 400:
            return response.json()

        if response.status_code == 429:
            # 1. Intento fallido, calculamos el delay
            delay = get_retry_after(response)
            if delay is None:
                # No hay recomendación, usaremos back‑off exponencial + jitter
                delay = BACKOFF_BASE * (2 ** attempt) + JITTER_RANGE * random.random()

            print(f"[{datetime.utcnow()}] 429 recibido. "
                  f"Reintentando en {delay:.1f}s (intento {attempt+1}/{MAX_RETRIES})")

            time.sleep(delay)
            attempt += 1
            continue

        # Si no es 429, fallamos de inmediato
        response.raise_for_status()

    # Si llegamos aquí, se agotaron los reintentos
    raise RuntimeError(f"Fallo tras {MAX_RETRIES} reintentos: {response.text}")

# Ejemplo de uso
if __name__ == "__main__":
    payload = {
        "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}],
        "max_tokens": 50,
    }
    try:
        result = request_with_retries(payload)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
```

### Detalles importantes

| Concepto | Implementación |
|----------|----------------|
| **Back‑off exponencial** | `BACKOFF_BASE * (2 ** attempt)` |
| **Jitter** | `JITTER_RANGE * random.random()` para evitar que varios clientes se sincronicen. |
| **Retry‑After** | Se consulta antes de usar back‑off. |
| **MAX_RETRIES** | Ajusta según tu tolerancia a fallos. |

---

## 3. Si usas `requests` con **tenacity** (opcional)

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=30),
    retry=retry_if_exception_type(requests.exceptions.HTTPError)
)
def request_with_tenacity(payload: dict) -> dict:
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()
```

Tenacity te permite manejar la lógica de reintentos de forma declarativa, pero tendrás que añadir la lógica de `Retry-After` manualmente si lo deseas.

---

## 4. Buenas prácticas adicionales

| Práctica | Por qué |
|----------|---------|
| **Rate‑limit headers** | Si quieres implementar un *client‑side throttling*, puedes leer `x-ratelimit-remaining` y `x-ratelimit-reset` para pre‑evitar 429. |
| **Batching** | Si tu flujo permite agrupar varias peticiones, reduce el número de llamadas. |
| **Escalado de créditos** | Asegúrate de que tu plan permite el tráfico que necesitas; si no, considera un plan superior. |
| **Logging centralizado** | Guarda cada 429 con timestamp y payload; así puedes identificar patrones de uso. |

---

### Resumen

1. **Detecta** `429` y lee `Retry-After` o `x-ratelimit-reset`.
2. **Aplica** back‑off exponencial + jitter.
3. **Limita** el número de reintentos.
4. **Logea** y alerta si se supera el límite.

Con esto tu aplicación ya no entrará en un bucle infinito y respetará el rate‑limit de OpenRouter. ¡Éxitos!