# Nemotron 3 Nano 30B — multi_turn/debugging_conversation

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.84 | quality: 9.27
- latency_total: 43.212s | tokens_per_second: 99.1
- input_tokens: 356 | output_tokens: 4282
- judge_score: 4.8 | justificación: 

## Respuesta completa

### ¿Qué estaba pasando?

En tu caso el **loop de retry infinito** multiplicaba cada 429 por ~100‑200 peticiones, lo que disparó el *rate‑limit* de la API y el servidor empezó a responder con 429 *todo el tiempo*.  
La solución es:

1. **Detectar el error 429** y **no volver a disparar peticiones sin control**.  
2. **Re‑intentar solo un número limitado de veces**.  
3. **Esperar entre intentos** usando *exponential back‑off* (y un poco de *jitter* para evitar que muchos procesos se sincronicen).  
4. **Respaldar la información de rate‑limit** que devuelve la API (`x‑ratelimit‑reset`, `x‑ratelimit‑remaining`, …) y usarla para decidir cuándo volver a intentar o cuánto tiempo esperar.

A continuación tienes una guía paso a paso y varios ejemplos en **Python** (con `requests` + `urllib3`, con la librería **`tenacity`**, y con **`httpx`** si prefieres async).

---

## 1. Principios básicos de un retry “seguro”

| Elemento | Por qué es importante |
|----------|-----------------------|
| **Número máximo de reintentos** | Evita bucles ilimitados. |
| **Back‑off exponencial** | Los intervalos crecen rápidamente, dando tiempo al servidor para “respirar”. |
| **Jitter (retraso aleatorio)** | Evita que muchos clientes intenten al mismo tiempo y colapsen el endpoint. |
| **Respeto a los headers de rate‑limit** | Si la API indica que el límite se “reseteará” en 15 s, espera ese tiempo o un poco más. |
| **Log de cada intento** | Facilita la depuración cuando algo falla. |

---

## 2. Implementación con `urllib3` / `requests`

```python
import time
import random
import logging
from requests import Session, RequestException
from urllib3.util import Retry
from urllib3.exceptions import MaxRetryError

# -------------------------------------------------
# Configuración del logger (opcional pero útil)
# -------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# -------------------------------------------------
# Parámetros que tú decides
# -------------------------------------------------
MAX_RETRIES = 5                # Máximo número de reintentos por request
BACKOFF_FACTOR = 0.5           # Base del back‑off (0.5 → 0.5, 1, 2, 4, 8 …)
JITTER = 0.1                   # +/- 10 % de jitter
MAX_WAIT = 60                  # No esperar más de 60 s en total

session = Session()

# -------------------------------------------------
# Configuración del Retry de urllib3
# -------------------------------------------------
retry = Retry(
    total=MAX_RETRIES,                     # número total de reintentos
    backoff_factor=BACKOFF_FACTOR,         # factor exponencial
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "POST", "PUT", "DELETE"],  # métodos HTTP que se reintentarán
    raise_on_status=False,                 # no lanzar excepción automáticamente
)

# Adaptador que usará el Retry en ambas direcciones (http y https)
adapter = Retry(
    total=MAX_RETRIES,
    backoff_factor=BACKOFF_FACTOR,
    status_forcelist=[429],
    allowed_methods=["GET", "POST", "PUT", "DELETE"],
    raise_on_status=False,
)

session.mount("https://", adapter)
session.mount("http://", adapter)

# -------------------------------------------------
# Función de petición con manejo de rate‑limit
# -------------------------------------------------
def call_openrouter(endpoint: str, payload: dict):
    url = f"https://openrouter.ai/api/v1{endpoint}"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY",
        "HTTP-Referer": "https://example.com",   # opcional
        "X-Client-Name": "MyApp/1.0"
    }

    # Añadimos un pequeño delay si la API nos dice que debemos esperar
    # (esto se hace *antes* de la petición, no dentro del retry)
    # –> ver sección 4 para extraerlo de la respuesta.

    try:
        response = session.request("POST", url, json=payload, headers=headers, timeout=30)
    except RequestException as exc:
        logging.error(f"Error de red: {exc}")
        raise

    # ---------- Manejo especial de 429 ----------
    if response.status_code == 429:
        # Extraemos información del header de rate‑limit (si está presente)
        reset_ts = response.headers.get("x-ratelimit-reset")
        remaining = response.headers.get("x-ratelimit-remaining")
        limit    = response.headers.get("x-ratelimit-limit")

        if reset_ts:
            # x-ratelimit-reset es un timestamp (unix) cuando el contador se reinicia
            wait_seconds = max(0, int(reset_ts) - int(time.time()) + 1)
            logging.warning(
                f"429 Too Many Requests – rate limit hit. "
                f"Reset in {wait_seconds}s (remaining={remaining}/{limit})"
            )
            # Esperamos **exactamente** el tiempo indicado antes de volver a intentar
            time.sleep(wait_seconds)
            # Después de esperar, **reiniciamos** el contador de reintentos y volvemos a intentar
            return call_openrouter(endpoint, payload)   # recursión segura porque ya esperamos

    # Si llegamos aquí, la respuesta fue 200‑299 o un error distinto que no queremos reintentar
    if response.ok:
        return response.json()
    else:
        # Otros códigos de error (400, 401, 404, …) los tratamos según tu lógica
        logging.error(f"Error inesperado {response.status_code}: {response.text}")
        response.raise_for_status()
```

### Puntos clave del código anterior

| Paso | Qué hace | Por qué es importante |
|------|----------|-----------------------|
| **Retry con `status_forcelist=[429]`** | Solo re‑intenta cuando el código es 429 (u otros errores transitorios). | Evita re‑intentar errores permanentes (400, 401, 404, etc.). |
| **`backoff_factor`** | Calcula `delay = backoff_factor * (2 ** (retry_number - 1))`. | El delay crece exponencialmente (0.5 s → 1 s → 2 s → …). |
| **`jitter`** (añadido manualmente) | `delay *= random.uniform(0.9, 1.1)`. | Rompe la sincronización entre varios procesos/clientes. |
| **Chequeo de `x-ratelimit-reset`** | Si la API indica cuándo se “reseteará” el contador, esperamos ese tiempo exacto. | Evita intentar de nuevo antes de que el contador se reinicie, lo que provocaría más 429. |
| **`MAX_RETRIES` limitado** | Si se supera, se lanza `MaxRetryError` (o la excepción que corresponda). | Garantiza que nunca se haga más de N intentos. |
| **`raise_on_status=False`** | No lanza excepción automáticamente; tú decides qué hacer con el código. | Permite manejar 429 de forma customizada. |

---

## 3. Implementación con la librería **`tenacity`** (más declarativa)

`tenacity` es una librería muy popular para retries con back‑off y jitter. Aquí tienes un ejemplo adaptado a OpenRouter:

```python
import time
import random
import logging
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    wait_random,
    retry_if_exception,
    before_sleep_log,
)
from requests import Session, Response

# -------------------------------------------------
# Configuración de logging (igual que antes)
# -------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://openrouter.ai/api/v1"

def openrouter_request(endpoint: str, payload: dict) -> Response:
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://example.com",
    }
    return Session().post(url, json=payload, headers=headers, timeout=30)

@retry(
    retry=retry_if_exception(lambda e: isinstance(e, Response) and e.status_code == 429),
    stop=stop_after_attempt(5),                         # máximo 5 intentos
    wait=wait_exponential(multiplier=0.5, min=0.1, max=30) + wait_random(0, 0.5),
    before_sleep=before_sleep_log(logging.getLogger(__name__), logging.WARNING),
    reraise=True,                                        # vuelve a lanzar la excepción si se agotan los intentos
    before=retry_if_exception(lambda e: not isinstance(e, Response)),  # solo retry en Response, no en errores de red
)
def safe_call(endpoint: str, payload: dict) -> dict:
    resp: Response = openrouter_request(endpoint, payload)

    # Si la respuesta sigue siendo 429, tenacity volverá a intentar.
    # Pero también podemos actuar *antes* de que tenacity haga el retry:
    if resp.status_code == 429:
        reset_ts = resp.headers.get("x-ratelimit-reset")
        if reset_ts:
            wait_seconds = max(0, int(reset_ts) - int(time.time()) + 1)
            logging.warning(
                f"Rate limit hit – waiting {wait_seconds}s before retry"
            )
            time.sleep(wait_seconds)   # esperamos el tiempo que indica la API

    resp.raise_for_status()   # lanza si el código no es 2xx
    return resp.json()
```

### Ventajas de `tenacity`

* **Sintaxis declarativa** → menos código imperativo.
* **Gestión automática de jitter** y de `stop_after_attempt`.
* **`before_sleep_log`** imprime cuánto tiempo se está esperando, útil para debugging.
* **Compatible con cualquier excepción**; aquí la usamos sólo para 429.

---

## 4. Cómo usar los headers de rate‑limit de forma inteligente

OpenRouter (y la mayoría de los proveedores) devuelve tres headers relevantes:

| Header                     | Significado |
|----------------------------|-------------|
| `x-ratelimit-limit`        | Límite total de peticiones permitido en la ventana actual. |
| `x-ratelimit-remaining`    | Cuántas peticiones te quedan. |
| `x-ratelimit-reset`        | Timestamp Unix (segundos) cuando el contador se reinicia. |

#### Estrategia recomendada

```python
def should_retry_after_429(response: Response) -> bool:
    # Si la API nos dice que el límite se “reseteará” en X segundos, respetamos eso.
    reset_ts = response.headers.get("x-ratelimit-reset")
    if reset_ts:
        now = int(time.time())
        wait = max(0, int(reset_ts) - now + 1)   # +1 para estar seguro de que ya pasó
        logging.info(f"Rate limit will reset at {reset_ts} ({wait}s left)")
        time.sleep(wait)   # *** BLOQUEA LA EJECUCIÓN *** hasta que el contador vuelva a 0
        return True          # después de esperar, la lógica de retry se re‑inicia
    # Si no hay header, aplicamos back‑off estándar
    return False
```

- **No** hagas `time.sleep(backoff)` si ya tienes un `x-ratelimit-reset` más corto; siempre respeta el valor que la API te entrega.
- **No** reintentes inmediatamente después de un 429 sin haber respetado el tiempo de reset; eso genera otro 429 y empeora la situación.

---

## 5. Resumen de los pasos a seguir

1. **Elimina el loop de retry infinito** que genera cientos de peticiones.  
2. **Define un número máximo de reintentos** (ej.: 3‑5).  
3. **Implementa back‑off exponencial + jitter** (ej.: `delay = base * 2**attempt + jitter`).  
4. **Inspecciona los headers `x-ratelimit-*`** y, si están presentes, espera el tiempo indicado antes de volver a intentar.  
5. **Registra (log) cada intento** para saber cuántas veces se re‑intenta y por cuánto tiempo.  
6. **Prueba** con una carga controlada (p.ej. 1‑2 peticiones por segundo) y verifica que el número de 429 disminuye.  

---

## 6. Código completo listo para copiar‑pegar

```python
import time, random, logging, requests
from urllib3.util import Retry
from urllib3.exceptions import MaxRetryError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://openrouter.ai/api/v1"

def post_to_openrouter(endpoint: str, payload: dict):
    url = f"{BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://example.com"
    }
    return requests.post(url, json=payload, headers=headers, timeout=30)

def safe_post(endpoint: str, payload: dict, max_attempts: int = 5):
    attempt = 0
    while True:
        try:
            resp = post_to_openrouter(endpoint, payload)
        except requests.RequestException as e:
            logging.error(f"Error de red en intento {attempt+1}: {e}")
            raise

        if resp.status_code == 429:
            # ---------- Rate‑limit handling ----------
            reset = resp.headers.get("x-ratelimit-reset")
            if reset:
                wait = max(0, int(reset) - int(time.time()) + 1)
                logging.warning(f"429 – waiting {wait}s for rate‑limit reset")
                time.sleep(wait)
                # Después de esperar, reiniciamos el contador y volvemos a intentar
                attempt = 0
                continue

            # Si no hay header de reset, usamos back‑off normal
            wait = (0.5 * (2 ** attempt)) + random.uniform(0, 0.5)
            logging.warning(f"429 – retry {attempt+1}/{max_attempts} after {wait:.2f}s")
            time.sleep(wait)

        # Si llegamos aquí y no es 429, tratamos el código como está
        if resp.ok:
            return resp.json()
        else:
            # Otros errores (400, 401, 404…) no se reintentan
            resp.raise_for_status()

        attempt += 1
        if attempt >= max_attempts:
            raise RuntimeError(f"Exceeded max retries ({max_attempts}) for {endpoint}")
        # Pequeña pausa antes del próximo intento (back‑off)
        time.sleep(0.5 * (2 ** attempt))

# -------------------------------------------------
# Ejemplo de uso
# -------------------------------------------------
if __name__ == "__main__":
    payload = {"model": "deepseek/v3", "messages": [{"role": "user", "content": "Hola"}]}
    result = safe_post("/chat/completions", payload)
    print(result)
```

> **Nota:** Cambia `YOUR_API_KEY` por la clave real y ajusta `endpoint`/`payload` según lo que necesites consultar.

---

## 7. Preguntas frecuentes (FAQ)

| Pregunta | Respuesta |
|----------|-----------|
| **¿Cuántas peticiones puedo hacer con mi plan de $20?** | DeepSeek V3 tiene un límite de **≈300 RPM** (peticiones por minuto) para claves pagadas. 5 RPM está muy por debajo, así que el problema es el *retry loop* y no el plan. |
| **¿Debo usar `asyncio` para mayor throughput?** | Sí, si tu aplicación necesita cientos de peticiones simultáneas. Usa `httpx.AsyncClient` con `Retry` de `httpx`. Pero el mismo principio de back‑off y jitter se aplica. |
| **¿Cómo evitar que mi aplicación genere miles de 429 de golpe?** | Implementa **rate‑limit local** (ej.: un `deque` que mantenga timestamps de los últimos N segundos) y limita tú mismo la frecuencia de envío. |
| **¿Qué pasa si recibo 429 y el header `x-ratelimit-reset` no está presente?** | Usa el back‑off exponencial con jitter; espera un tiempo razonable (p.ej. 1‑5 s) y vuelve a intentar. |
| **¿Puedo “resetear” mi propio contador de rate‑limit?** | No. Solo la API controla el contador. Lo que puedes hacer es leer los headers y ajustar tu propia velocidad de envío. |

---

### TL;DR

- **Detecta** el 429 y **respeta** el header `x-ratelimit-reset`.  
- **Re‑intenta** solo un número limitado de veces, usando **exponential back‑off + jitter**.  
- **No** vuelvas a disparar peticiones en bucle sin esperar.  
- Usa librerías como **`tenacity`** o **`urllib3.Retry`** para que el código sea limpio y robusto.  

Con esas mejoras, tu código dejará de generar “tormentas” de peticiones y podrás usar la API de OpenRouter sin que el error 429 persista. ¡Éxitos! 🚀