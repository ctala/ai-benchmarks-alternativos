# Tencent Hy4 preview — multi_turn/debugging_conversation

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 167.035s | tokens_per_second: 59.7
- input_tokens: 371 | output_tokens: 9965

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

¡Ese hallazgo lo explica todo! Un `while True` que reintenta al instante convierte **un solo 429 en una avalancha de cientos de requests**. Aunque tú solo quieras hacer 5 RPM, el loop las dispara todas en milisegundos, agotas el bucket de rate limit al instante y OpenRouter te bloquea temporalmente (por eso “no puedes hacer ni una llamada”).

Vamos a arreglarlo en dos partes: **parar el sangrado** y **reintentar correctamente**.

---

## 1. Acción inmediata (antes de cambiar código)

1. **Detén el proceso/script** que tiene el loop infinito (mata el contenedor, el script de Python/Node, etc.).
2. **Espera a que se resetee el rate limit**. Normalmente la ventana es de 1 minuto. Si puedes, revisa el header `Retry-After` de uno de los 429: ese es el tiempo exacto que debes esperar sin hacer ninguna llamada.
3. Después de esperar, haz **una sola llamada manual** (por ejemplo con `curl` o un script de 1 request). Debería devolver `200`.

---

## 2. Reglas para implementar retries “bien”

Nunca hagas esto:

```python
while True:          # ❌ infinito
    try:
        r = call()
        if r.ok: break
    except:
        continue     # ❌ reintenta sin esperar
```

Haz esto:

1. **Reintentos acotados:** máximo 3 a 5 intentos. Usa un `for intento in range(max_retries)`, no un `while True`.
2. **Solo reintentar errores transitorios:** `429` y `5xx` (500, 502, 503, 504) o timeouts de red. **No** reintentes `400`, `401`, `403`, `404`.
3. **Respetar `Retry-After`:** si la respuesta trae ese header, espera exactamente esos segundos. Es la forma correcta de no pelearte con el servidor.
4. **Si no hay `Retry-After`, usa backoff exponencial con jitter:**
   - `espera = min(base * 2**intento, max_espera)`
   - Añade un `random` (jitter) para que, si tienes varios workers, no todos reintenten al mismo tiempo.
5. **Limita la tasa en tu cliente:** si solo necesitas 5 RPM, no dispares requests en paralelo. Secuencia: 1 request cada 12 segundos (`60/5`), o usa un token bucket/semaphore.
6. **Después de agotar los reintentos, falla y loguea.** No vuelvas a enciclarte.

---

## 3. Ejemplos de implementación

### Opción A: Python + `requests` (sin dependencias raras)

```python
import requests
import time
import random

API_KEY = "sk-or-..."
URL = "https://openrouter.ai/api/v1/chat/completions"
MAX_RETRIES = 5

def calcular_espera(resp, intento):
    # 1) Prioridad: header Retry-After (segundos)
    ra = resp.headers.get("Retry-After")
    if ra:
        try:
            return float(ra)
        except ValueError:
            pass  # podría ser fecha HTTP, lo ignoramos por simplicidad

    # 2) Headers de rate limit de OpenRouter
    reset = resp.headers.get("X-RateLimit-Reset") or resp.headers.get("x-ratelimit-reset")
    if reset:
        try:
            ts = float(reset)
            if ts > 1_000_000_000_000:      # epoch en milisegundos
                return max(ts / 1000 - time.time(), 0)
            if ts > 1_000_000_000:          # epoch en segundos
                return max(ts - time.time(), 0)
            return max(ts, 0)               # segundos restantes
        except ValueError:
            pass

    # 3) Fallback: backoff exponencial + jitter
    return min(2 ** intento, 60) + random.uniform(0, 1)


def llamar_openrouter(payload):
    headers = {"Authorization": f"Bearer {API_KEY}"}

    for intento in range(MAX_RETRIES):
        r = requests.post(URL, json=payload, headers=headers, timeout=30)

        if r.status_code == 200:
            return r.json()

        # ¿Es un error transitorio?
        if r.status_code == 429 or 500 <= r.status_code < 600:
            espera = calcular_espera(r, intento)
            print(f"[retry {intento+1}/{MAX_RETRIES}] {r.status_code}, esperando {espera:.1f}s")
            time.sleep(espera)
            continue

        # Error de cliente (400, 401, etc.) -> no reintentar
        r.raise_for_status()

    raise RuntimeError("Se agotaron los reintentos (429 persistente)")


# --- Throttle cliente para 5 RPM (1 cada 12s) ---
_ultimo_request = 0
MIN_INTERVAL = 12  # 60s / 5 requests

def llamar_throttled(payload):
    global _ultimo_request
    delta = time.time() - _ultimo_request
    if delta < MIN_INTERVAL:
        time.sleep(MIN_INTERVAL - delta)
    _ultimo_request = time.time()
    return llamar_openrouter(payload)
```

Uso:

```python
resp = llamar_throttled({
    "model": "deepseek/deepseek-chat",  # DeepSeek V3
    "messages": [{"role": "user", "content": "Hola"}]
})
print(resp["choices"][0]["message"]["content"])
```

---

### Opción B: Python con el SDK de OpenAI (recomendado si ya lo usas)

OpenRouter es compatible con el SDK de OpenAI, y este ya trae reintentos con backoff y jitter, y respeta `Retry-After`. Solo tienes que activarlos:

```python
from openai import OpenAI, RateLimitError

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-...",
    max_retries=5,   # <- importante: por defecto son 2
    timeout=30,
)

try:
    resp = client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Hola"}],
    )
    print(resp.choices[0].message.content)
except RateLimitError as e:
    print("Sigue limitado después de 5 reintentos. Espera 1 min y reintenta manualmente.")
```

> Nota: el SDK **no** hace throttle de tasa (solo reintentos). Si disparas 100 requests en paralelo, igual te va a limitar. Para 5 RPM, sigue secuenciando las llamadas como en el ejemplo de `llamar_throttled`.

---

### Opción C: Node.js / TypeScript (usando `fetch`)

```js
const API_KEY = "sk-or-...";
const URL = "https://openrouter.ai/api/v1/chat/completions";
const MAX_RETRIES = 5;

async function llamarOpenRouter(payload) {
  for (let intento = 0; intento < MAX_RETRIES; intento++) {
    const res = await fetch(URL, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (res.ok) return await res.json();

    if (res.status === 429 || res.status >= 500) {
      let waitMs;

      const ra = res.headers.get("retry-after");
      if (ra) waitMs = parseFloat(ra) * 1000;

      const reset = res.headers.get("x-ratelimit-reset");
      if (!waitMs && reset) {
        const ts = Number(reset);
        waitMs = ts > 1e12 ? ts - Date.now() : ts * 1000;
      }

      if (!waitMs) {
        waitMs = Math.min(1000 * 2 ** intento, 60000) + Math.random() * 1000;
      }

      console.log(`[retry ${intento + 1}] esperando ${waitMs}ms`);
      await new Promise((r) => setTimeout(r, waitMs));
      continue;
    }

    // Error no reintentable
    throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  }
  throw new Error("Máximo de reintentos alcanzado");
}
```

Para limitar a 5 RPM en Node, simplemente haz `await new Promise(r => setTimeout(r, 12000))` entre llamadas secuenciales, o usa una librería tipo `bottleneck`:

```js
import Bottleneck from "bottleneck";
const limiter = new Bottleneck({ maxConcurrent: 1, minTime: 12000 }); // 1 cada 12s = 5 RPM
const llamarLimitado = limiter.wrap(llamarOpenRouter);
```

---

## 4. Verifica tu límite real en OpenRouter

Para no volar a ciegas, consulta tu key:

```bash
curl https://openrouter.ai/api/v1/key \
  -H "Authorization: Bearer $OPENROUTER_API_KEY"
```

Fíjate en el campo `data.rate_limit` (algo como `{"requests": 300, "interval": "1m"}`). Ese es tu límite real según tu saldo. Configura tu throttle cliente para quedarte por debajo (por ejemplo, al 50-80% del límite).

Además, en cada respuesta revisa:

- `X-RateLimit-Remaining`: cuántas requests te quedan en la ventana.
- `X-RateLimit-Reset` / `x-ratelimit-reset`: cuándo se resetea.
- `Retry-After`: cuánto esperar si te dieron 429.

---

## 5. Checklist final para que no te vuelva a pasar

- [ ] Reemplazaste el `while True` por un bucle `for` con máximo 3-5 intentos.
- [ ] Solo reintentas `429` y `5xx`.
- [ ] Esperas el tiempo que diga `Retry-After` (o backoff exponencial con jitter si no viene).
- [ ] Agregaste un **throttle en el cliente** a ~5 RPM (1 cada 12s) o según el límite que te devuelva `/key`.
- [ ] Si usas el SDK de OpenAI, configuraste `max_retries=5` y **no** lo envolviste en otro loop infinito.
- [ ] Logueas cada reintento para tener visibilidad.

Con esto, tu script de 5 RPM debería funcionar sin problemas y, si alguna vez vuelve a aparecer un 429 aislado, el cliente esperará educadamente y reintentará un par de veces en lugar de multiplicar el tráfico por 100.

¿En qué lenguaje estás trabajando (Python, Node, otro)? Si me pasas un fragmento de tu loop actual te ayudo a refactorizarlo directamente.