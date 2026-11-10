# GPT-OSS 20B — multi_turn/debugging_conversation

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 14.09s | tokens_per_second: 129.0
- input_tokens: 376 | output_tokens: 1818

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

## ✅ Resumen rápido

- **El 429** no es un “error de tu código”, es el servidor diciendo “¡sólo aceptamos X peticiones por minuto!”  
- Si tu código entra en un bucle infinito de reintentos, cada vez que recibes el 429 se dispara otro 429 → *explosión de peticiones* → tu cuenta se bloquea y la API te sigue diciendo “Too Many Requests”.
- La solución es **reintentar con back‑off exponencial + jitter**, y **detenerse después de un número razonable de intentos** (o cuando el header `Retry-After` indique un tiempo específico).

A continuación tienes un ejemplo completo (Python) que puedes adaptar a tu propio stack. Si usas otro lenguaje, los principios son los mismos; solo cambia la sintaxis.

---

## 🛠️ Implementación práctica (Python)

```python
import time
import random
import requests
from typing import Any, Dict

# ─────────────────────────────────────────────────────────────
# 1️⃣  Configuración
# ─────────────────────────────────────────────────────────────
API_URL   = "https://api.openrouter.ai/v1/chat/completions"
API_KEY   = "sk-..."           # ← tu clave real
MODEL     = "deepseek-coder-v2"  # o el que uses
HEADERS   = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
MAX_RETRIES = 5         # número máximo de reintentos
BASE_DELAY  = 0.5       # 0.5s de base
MAX_DELAY   = 30.0      # no esperes más de 30s entre intentos
JITTER      = 0.1       # 10% de variación
# ─────────────────────────────────────────────────────────────

def make_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Llama a la API con lógica de reintentos.
    Devuelve el JSON de respuesta o levanta una excepción.
    """
    attempt = 0
    while attempt <= MAX_RETRIES:
        try:
            resp = requests.post(API_URL, json=payload, headers=HEADERS, timeout=10)
        except requests.RequestException as exc:
            # Problemas de red, timeout, etc.
            print(f"[{attempt}] Error de red: {exc}")
            # Tratamos como si fuera 429 para dar tiempo al servidor
            status = 429
        else:
            status = resp.status_code

        if status == 200:
            return resp.json()

        if status == 429:
            # 1️⃣  Lee los headers del servidor
            retry_after = resp.headers.get("Retry-After")
            if retry_after is not None:
                # Puede ser un número de segundos o un timestamp
                try:
                    delay = float(retry_after)
                except ValueError:
                    # Si es un timestamp, calculamos la diferencia
                    from datetime import datetime
                    ts = datetime.strptime(retry_after, "%a, %d %b %Y %H:%M:%S GMT")
                    delay = (ts - datetime.utcnow()).total_seconds()
            else:
                # 2️⃣  Back‑off exponencial + jitter
                delay = min(BASE_DELAY * (2 ** attempt), MAX_DELAY)
                jitter = delay * JITTER * (random.uniform(-1, 1))
                delay += jitter

            print(f"[{attempt}] 429 recibido. Esperando {delay:.2f}s antes de reintentar…")
            time.sleep(max(0, delay))
            attempt += 1
            continue

        # Cualquier otro código de error lo consideramos fatal
        print(f"[{attempt}] Código inesperado {status}: {resp.text}")
        resp.raise_for_status()

    # Si llegamos aquí, superamos MAX_RETRIES
    raise RuntimeError(f"Máximo de reintentos ({MAX_RETRIES}) alcanzado sin éxito.")

# ─────────────────────────────────────────────────────────────
# 2️⃣  Uso del helper
# ─────────────────────────────────────────────────────────────
payload = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": "Eres un asistente experto."},
        {"role": "user",   "content": "Hola, ¿cómo estás?"}
    ]
}

try:
    respuesta = make_request(payload)
    print("Respuesta:", respuesta["choices"][0]["message"]["content"])
except Exception as e:
    print("Error final:", e)
```

### ¿Qué hace este código?

| Paso | Qué ocurre | Por qué |
|------|------------|---------|
| **1** | Se define un `MAX_RETRIES` y una política de back‑off exponencial. | Evita que el cliente envíe peticiones repetidas sin pausa. |
| **2** | Si la respuesta es `429`, se comprueba el header `Retry-After`. | Algunas APIs indican explícitamente cuánto tiempo esperar. |
| **3** | Si no hay `Retry-After`, se calcula un `delay` con back‑off exponencial (`BASE_DELAY * 2^attempt`) + jitter (±10%). | El jitter evita que varios clientes se sincronicen y vuelvan a chocar. |
| **4** | Se espera (`time.sleep`) y se vuelve a intentar hasta `MAX_RETRIES`. | Se limita el número total de intentos, protegiendo tu cuota. |
| **5** | Si se supera el número de reintentos, se lanza una excepción. | Tu código puede capturarla y decidir qué hacer (log, notificación, etc.). |

---

## 📚 Buenas prácticas más allá del código

| Tema | Recomendación |
|------|---------------|
| **Rate‑limit headers** | La mayoría de APIs devuelven `x-ratelimit-remaining`, `x-ratelimit-reset`. Si tu SDK lo expone, úsalo para *pre‑ventir* 429. |
| **Batching** | Si tu flujo permite procesar varias peticiones a la vez, agrúbalas y envíalas en menos llamadas. |
| **Cache** | Si la misma consulta se repite, guarda la respuesta localmente (cache LRU, Redis, etc.). |
| **Perfil de uso** | Monitorea cuántas peticiones haces realmente (logs, métricas). A veces el error no se debe a tu código sino a un pico inesperado. |
| **Plan de niveles** | Si tu uso es constante y alto, considera un plan de pago con límites mayores. |
| **Timeouts** | No pongas `timeout=None`. Un timeout corto (ej. 10s) evita que tu cliente quede bloqueado indefinidamente. |

---

## 🔁 Resumen de la estrategia de reintentos

| Estado | Acción |
|--------|--------|
| **200** | Devuelve la respuesta. |
| **429** | Leer `Retry-After`. Si no hay → back‑off exponencial + jitter. Espera y reintenta hasta `MAX_RETRIES`. |
| **4xx/5xx (excl. 429)** | Lanza error inmediatamente (o decide si reintentar según el código). |
| **Timeout / Conexión perdida** | Trata como 429 (espera y reintenta). |
| **Superado `MAX_RETRIES`** | Lanza excepción; tu aplicación decide si vuelve a intentar de forma controlada o si informa al usuario. |

---

## 🚀 Próximos pasos

1. **Reemplaza** tu bucle de reintentos con la función `make_request` (o el equivalente en tu lenguaje).  
2. **Prueba** con un script de prueba y observa los logs: deberías ver algo como `429 recibido. Esperando 2.3s antes de reintentar…`.  
3. **Monitorea** la tasa de peticiones con los headers de rate‑limit que la API devuelve.  
4. Si después de esto sigues recibiendo 429, revisa que no haya *otras* peticiones (por ejemplo, tu propio backend, un script cron, etc.) que estén consumiendo tu cuota.

¡Con esta configuración tu cliente ya no se quedará atrapado en un loop infinito y respetará los límites de OpenRouter! 🚀