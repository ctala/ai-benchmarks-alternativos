# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — multi_turn/debugging_conversation

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 7.24 | quality: 9.27
- latency_total: 41.742s | tokens_per_second: 65.4
- input_tokens: 357 | output_tokens: 2729
- judge_score: 4.8 | justificación: 

## Respuesta completa

### El problema principal  
Cuando recibes **429 Too Many Requests** tu código está haciendo **reintentos infinitos** sin esperar entre ellos. Cada intento genera otra petición y, como el servidor sigue devolviendo 429, el número de peticiones crece rápidamente (en tu caso 100 × el número de errores).  

Para evitarlo debemos:

1. **Detectar** que la respuesta es 429.  
2. **Leer** el encabezado `Retry-After` (si el servidor lo envía) o usar un **back‑off exponencial**.  
3. **Limitar** el número máximo de reintentos (p.ej. 5‑10).  
4. **Esperar** el tiempo indicado antes de volver a intentar.  

A continuación tienes una guía paso a paso y ejemplos de código en **Python** (con `requests`) y también una alternativa con la librería **`tenacity`**, que simplifica mucho la lógica.

---

## 1️⃣  Detectar 429 y leer `Retry-After`

```python
import time
import requests

def call_api(url, payload, max_retries=5, backoff_factor=1.0):
    """
    Hace la petición y gestiona los reintentos cuando el servidor devuelve 429.
    - max_retries: número máximo de intentos (incluido el original).
    - backoff_factor: factor de crecimiento del tiempo de espera (exponencial).
    """
    for attempt in range(1, max_retries + 1):
        response = requests.post(url, json=payload)   # o el método que uses

        # -------------------------------------------------
        # 1️⃣  ¿Es 429?
        # -------------------------------------------------
        if response.status_code == 429:
            # Intentamos leer el tiempo que el servidor indica esperar
            retry_after = response.headers.get("Retry-After")
            wait_seconds = None

            if retry_after:
                # Puede ser un entero (segundos) o una fecha HTTP‑UTC
                try:
                    wait_seconds = int(retry_after)
                except ValueError:
                    # Si es una fecha, la convertimos a segundos
                    from email.utils import parsedate_to_datetime
                    delta = parsedate_to_datetime(retry_after) - time.time()
                    wait_seconds = max(delta.total_seconds(), 0)

            # Si no hay Retry-After, usamos backoff exponencial
            if wait_seconds is None:
                wait_seconds = backoff_factor * (2 ** (attempt - 1))

            print(f"[Attempt {attempt}] 429 recibido → esperando {wait_seconds:.1f}s")
            time.sleep(wait_seconds)
            continue   # volver a intentar la petición

        # -------------------------------------------------
        # 2️⃣  Caso exitoso (cualquier otro código)
        # -------------------------------------------------
        if response.ok:
            return response.json()   # o .text, .content, lo que necesites

        # -------------------------------------------------
        # 3️⃣  Otros errores (4xx/5xx) que no queremos reintentar
        # -------------------------------------------------
        # Aquí puedes lanzar una excepción o manejar el error según tu lógica
        response.raise_for_status()

    # Si llegamos aquí, agotamos los reintentos
    raise RuntimeError(f"Excedido el número máximo de reintentos ({max_retries}) para {url}")
```

### Qué hace este código

| Paso | Acción |
|------|--------|
| **Loop** | Reintenta hasta `max_retries` veces. |
| **429** | - Lee `Retry-After`. Si está, usa ese valor. <br> - Si no, calcula un **back‑off exponencial** (`base * 2^(n‑1)`). |
| **Sleep** | Espera el tiempo calculado antes de volver a intentar. |
| **Success** | Si la respuesta es `200‑OK`, devuelve el contenido. |
| **Failure** | Cualquier otro código de error (p.ej. 401, 404, 500) lanza `raise_for_status()` para que tu código principal lo maneje. |
| **Fail after max** | Lanza una excepción clara indicando que se agotaron los intentos. |

---

## 2️⃣  Implementación con `tenacity` (biblioteca de retries)

Si prefieres no escribir el bucle manual, la librería **`tenacity`** hace todo el trabajo por ti:

```bash
pip install tenacity
```

```python
import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from requests.exceptions import RequestException

@retry(
    reraise=True,
    stop=stop_after_attempt(6),                     # máximo 6 intentos (1 original + 5 reintentos)
    wait=wait_exponential(multiplier=1, min=1, max=30), # 1s, 2s, 4s, 8s, 16s, 30s (máx)
    retry=retry_if_exception_type((RequestException,)), # reintenta en cualquier excepción de requests
    # También podemos reintentar sólo cuando el código sea 429:
    # retry=lambda retry_state: retry_state.outcome.exception() is not None
)
def call_api(url, payload):
    resp = requests.post(url, json=payload)
    # Si el servidor responde 429, `requests` lanza HTTPError (si usamos response.raise_for_status())
    resp.raise_for_status()
    return resp.json()
```

### Cómo hacer que `tenacity` detecte específicamente 429

`tenacity` trabaja con **excepciones**, así que primero lanzamos una excepción cuando el código es 429:

```python
def call_api(url, payload):
    resp = requests.post(url, json=payload)
    if resp.status_code == 429:
        # Lanzamos una excepción que tenacity capturará para reintentar
        raise requests.HTTPError(f"Rate limit exceeded: {resp.status_code}")
    resp.raise_for_status()
    return resp.json()
```

Con esta configuración, `tenacity` volverá a intentar automáticamente respetando el back‑off exponencial y el número máximo de intentos.

---

## 3️⃣  Buenas prácticas adicionales

| Tema | Qué hacer |
|------|-----------|
| **Limitar el número de reintentos** | No intentes más de 5‑10 veces; después de eso es probable que el problema sea estructural (p.ej. key bloqueada). |
| **Respeto al `Retry-After`** | Si el servidor indica `Retry-After: 60`, respeta exactamente ese tiempo (no uses solo back‑off). |
| **Identificar la causa** | 429 suele deberse a: <br>• Límite de peticiones por minuto (rate limit). <br>• Uso de una API “free” con cuota muy baja. <br>• Key mal configurada o compartida entre varios procesos. |
| **Logging** | Registra cada intento, el código de estado y el tiempo de espera. Facilita el debugging. |
| **Thread / async** | Si tu aplicación hace peticiones concurrentes, asegúrate de que el **semáforo** o **token bucket** que controla el rate‑limit sea compartido entre todos los hilos/corutinas. De lo contrario, cada hilo puede sobrepasar el límite sin que te des cuenta. |
| **Circuit Breaker** | Para casos extremos (p.ej. la API está temporalmente fuera de línea), combina la lógica de retry con un **circuit breaker** (p.ej. `pybreaker`) para dejar de lanzar peticiones cuando el error persiste. |

---

## 4️⃣  Resumen paso a paso para arreglar tu código

1. **Elimina el loop infinito** que genera los reintentos sin pausa.  
2. **Añade una pausa** (sleep) antes de volver a intentar.  
3. **Respeta `Retry-After`** si el servidor lo envía; de lo contrario, usa back‑off exponencial.  
4. **Limita los intentos** (p.ej. 5‑10).  
5. **Maneja errores diferentes a 429** sin reintentar (p.ej. 401 Unauthorized → falla inmediata).  

Con el fragmento de código que te mostré arriba (o con `tenacity`) podrás convertir tu flujo de “reintento infinito” en una estrategia **robusta** y **rate‑limit‑friendly**.

---

### Código completo (ejemplo listo para copiar)

```python
import time
import requests
from requests.exceptions import RequestException

def call_deepseek(url, payload, max_retries=5):
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, json=payload)
            if resp.status_code == 429:
                # ----> 429 → leer Retry-After o hacer back‑off
                retry_after = resp.headers.get("Retry-After")
                wait = None
                if retry_after:
                    try:
                        wait = int(retry_after)
                    except ValueError:
                        from email.utils import parsedate_to_datetime
                        wait = max((parsedate_to_datetime(retry_after) - time.time()).total_seconds(), 0)

                if wait is None:
                    wait = 1.0 * (2 ** (attempt - 1))   # 1s, 2s, 4s, ...

                print(f"[Attempt {attempt}] 429 → waiting {wait:.1f}s")
                time.sleep(wait)
                continue   # reintentar

            # Si llegamos aquí, la respuesta no es 429
            resp.raise_for_status()
            return resp.json()          # <-- devuelve el cuerpo esperado

        except RequestException as exc:
            # Otros errores (conexión, timeout, 5xx, etc.) → reintentar según tu política
            if attempt == max_retries:
                raise RuntimeError(f"Failed after {max_retries} attempts: {exc}") from exc
            print(f"[Attempt {attempt}] Exception {exc} → retry in {attempt}s")
            time.sleep(attempt)   # back‑off simple para errores no 429

    raise RuntimeError("Should never reach here")

# -------------------------------------------------
# Uso:
# -------------------------------------------------
DEEPSEEK_ENDPOINT = "https://api.openrouter.ai/v1/chat/completions"
API_KEY = "sk-..."                     # tu clave con saldo $20
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

payload = {
    "model": "DeepSeek-V3",
    "messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}]
}

try:
    result = call_deepseek(DEEPSEEK_ENDPOINT, payload, max_retries=6)
    print("✅ Respuesta:", result)
except Exception as e:
    print("❌ Error final:", e)
```

Con este patrón:

- **No volverás a saturar** la API porque introduces una espera creciente.  
- **Respetarás** cualquier límite que el propio servidor indique mediante `Retry-After`.  
- **Tendrás** un número máximo de intentos definido, evitando bucles infinitos.  

¡Listo! Ahora tus llamadas a la API de OpenRouter deberían funcionar sin generar el error 429 permanente. 🚀 

Si necesitas adaptar esto a otro lenguaje (Node.js, Go, etc.) o tienes alguna duda adicional, avísame.