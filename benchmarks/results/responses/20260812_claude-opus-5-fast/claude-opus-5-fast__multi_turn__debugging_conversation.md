# Claude Opus 5 Fast — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 10.096s | tokens_per_second: 202.8
- input_tokens: 539 | output_tokens: 2048

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

Perfecto, encontraste la causa raíz. Ese patrón se llama **retry storm** o *thundering herd* — un error transitorio se amplifica en cascada y termina siendo auto-infligido. Vamos por partes.

## 0. Antes de tocar código: enfría la key

Si estuviste martillando la API, es posible que tu key esté en un estado de penalización temporal más agresivo que el rate limit normal. **Detén el proceso completamente y espera 5-10 minutos** antes de probar de nuevo. Si no, vas a estar debuggeando contra un estado sucio y no vas a saber si tu fix funcionó.

Mientras tanto, verifica tu consumo real en `https://openrouter.ai/api/v1/auth/key` — te dice cuántos créditos y qué límites tienes.

---

## 1. Los cuatro principios de un retry correcto

| Principio | Por qué |
|---|---|
| **Solo reintentar errores transitorios** | Reintentar un 401 nunca va a funcionar, solo quema cuota |
| **Backoff exponencial** | Dar tiempo real a que el servidor se recupere |
| **Jitter (aleatoriedad)** | Evitar que N clientes reintenten en el mismo instante |
| **Límite duro de intentos** | Un retry infinito no es resiliencia, es un DoS a ti mismo |

### Qué reintentar y qué no

```
REINTENTAR:
  429  Too Many Requests    -> respetar Retry-After si viene
  500  Internal Server Error
  502  Bad Gateway
  503  Service Unavailable
  504  Gateway Timeout
  Timeouts / errores de conexión / DNS

NO REINTENTAR (fallar rápido):
  400  Bad Request          -> tu payload está mal
  401  Unauthorized         -> key inválida
  402  Payment Required     -> sin créditos
  403  Forbidden
  404  Not Found            -> modelo mal escrito
  422  Unprocessable Entity
```

Reintentar un 400 mil veces no lo va a convertir en 200.

---

## 2. Implementación manual (para que entiendas la mecánica)

```python
import random
import time
import httpx

RETRYABLE_STATUS = {429, 500, 502, 503, 504}

class RateLimitExceeded(Exception):
    pass

def call_openrouter(
    payload: dict,
    api_key: str,
    max_retries: int = 5,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    total_budget: float = 120.0,
):
    """
    Backoff exponencial con jitter y presupuesto total de tiempo.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    started = time.monotonic()
    last_error = None

    for attempt in range(max_retries + 1):  # intento 0 = primer request
        # Presupuesto global: no seguir si ya gastamos demasiado tiempo
        elapsed = time.monotonic() - started
        if elapsed > total_budget:
            raise RateLimitExceeded(
                f"Presupuesto de {total_budget}s agotado tras {attempt} intentos"
            )

        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(url, headers=headers, json=payload)

            if resp.status_code == 200:
                return resp.json()

            if resp.status_code not in RETRYABLE_STATUS:
                # Error permanente: fallar inmediatamente, sin retry
                resp.raise_for_status()

            last_error = f"HTTP {resp.status_code}: {resp.text[:200]}"

            # El servidor nos dice explícitamente cuánto esperar
            retry_after = resp.headers.get("Retry-After")
            if retry_after:
                try:
                    delay = min(float(retry_after), max_delay)
                except ValueError:
                    delay = _backoff(attempt, base_delay, max_delay)
            else:
                delay = _backoff(attempt, base_delay, max_delay)

        except (httpx.TimeoutException, httpx.ConnectError) as e:
            last_error = f"{type(e).__name__}: {e}"
            delay = _backoff(attempt, base_delay, max_delay)

        if attempt == max_retries:
            break

        print(f"[retry {attempt + 1}/{max_retries}] {last_error} "
              f"-> esperando {delay:.2f}s")
        time.sleep(delay)

    raise RateLimitExceeded(
        