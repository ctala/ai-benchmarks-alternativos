# MiniMax M3.1 Flash — multi_turn/debugging_conversation

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 42.016s | tokens_per_second: 209.6
- input_tokens: 499 | output_tokens: 8806

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

Sí: ese loop explica por qué el 429 “no se va”. Un solo 429 dispara decenas de requests inmediatos, lo que mantiene activo el rate limit y puede consumir más cuota.

El saldo de USD 20 y el rate limit son cosas distintas: tener créditos no elimina las restricciones por requests/minuto.

## Retry recomendado

Debe tener:

1. **Un máximo de intentos**: por ejemplo, 4 requests totales (1 original + 3 retries).
2. **Backoff exponencial**: esperar 5, 10 y 20 segundos, no repetir inmediatamente.
3. **Jitter aleatorio** para evitar que varios workers repitan al mismo tiempo.
4. Respetar `Retry-After` si OpenRouter lo envía.
5. Reintentar solo errores transitorios: `408`, `425`, `429`, `500`, `502`, `503`, `504`.
6. No reintentar errores permanentes como `400`, `401`, `402`, `403` o `404`.

### Ejemplo en Python

```python
import random
import time
from datetime import timezone
from email.utils import parsedate_to_datetime

import requests


RETRYABLE_STATUS = {
    408,  # Request Timeout
    425,  # Too Early
    429,  # Too Many Requests
    500,
    502,
    503,
    504,
}

MAX_BACKOFF_SECONDS = 60


def get_retry_after(response):
    """Retry-After puede ser segundos o una fecha HTTP."""
    value = response.headers.get("Retry-After")
    if not value:
        return None

    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            date = parsedate_to_datetime(value)
            if date.tzinfo is None:
                date = date.replace(tzinfo=timezone.utc)
            return max(0.0, date.timestamp() - time.time())
        except (TypeError, ValueError, OverflowError):
            return None


def calculate_wait(response, attempt):
    # Para 429 comenzamos con una espera más conservadora.
    initial = 5.0 if response and response.status_code == 429 else 1.0

    backoff = min(
        MAX_BACKOFF_SECONDS,
        initial * (2 ** attempt),
    )

    server_delay = get_retry_after(response) if response else None

    # Nunca reintentamos antes de lo que indique el servidor.
    delay = max(backoff, server_delay or 0.0)

    # Jitter: evita que todos los workers reintenten simultáneamente.
    delay += random.uniform(0, min(1.0, delay * 0.25))

    return delay


def call_openrouter(session, payload, max_attempts=4):
    """
    max_attempts incluye la petición original.
    Ejemplo: 4 = 1 original + 3 reintentos.
    """

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # Opcionales:
        # "HTTP-Referer": "https://tu-aplicacion.com",
        # "X-Title": "Mi aplicación",
    }

    for attempt in range(max_attempts):
        try:
            response = session.post(
                url,
                headers=headers,
                json=payload,
                timeout=(10, 180),  # Conexión y lectura
            )
        except (requests.Timeout, requests.ConnectionError) as exc:
            if attempt == max_attempts - 1:
                raise

            delay = calculate_wait(None, attempt)

            print(
                f"Error de red: {exc}; "
                f"intento {attempt + 1}/{max_attempts}; "
                f"espera {delay:.1f}s"
            )

            time.sleep(delay)
            continue

        if response.status_code not in RETRYABLE_STATUS:
            response.raise_for_status()
            return response.json()

        # Se agotaron los intentos: no hay loop infinito.
        if attempt == max_attempts - 1:
            raise RuntimeError(
                f"OpenRouter devolvió {response.status_code}. "
                f"Retry-After={response.headers.get('Retry-After')}; "
                f"request-id={response.headers.get('x-request-id')}; "
                f"body={response.text[:500]}"
            )

        delay = calculate_wait(response, attempt)

        print(
            f"HTTP {response.status_code}; "
            f"intento {attempt + 1}/{max_attempts}; "
            f"Retry-After={response.headers.get('Retry-After')}; "
            f"espera {delay:.1f}s"
        )

        time.sleep(delay)

    raise RuntimeError("No se pudo completar la solicitud")
```

Uso con una sesión reutilizable:

```python
session = requests.Session()

payload = {
    "model": "deepseek/deepseek-v3",
    "messages": [
        {"role": "user", "content": "Hola"}
    ],
}

result = call_openrouter(session, payload)
print(result)
```

## Si usas el cliente de OpenAI contra OpenRouter

Desactiva los retries internos del SDK y deja una sola capa de retry en tu aplicación:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    max_retries=0,
)
```

Si tu SDK, proxy o framework ya reintenta y luego tu código también lo hace, los intentos se multiplican.

## Importante para streaming

No reintentes automáticamente si ya emitiste tokens al usuario. Un stream podría duplicar contenido o generar dos cobros. Solo reintenta si la respuesta falló antes de enviar ningún fragmento.

## Prueba de diagnóstico

1. Detén el loop actual.
2. Espera a que expire la ventana del rate limit, normalmente 60 segundos.
3. Ejecuta una sola llamada con `max_attempts=1`.
4. Si funciona, activa el retry limitado.
5. Registra `Retry-After`, `x-request-id` y el cuerpo del error 429.

Si después de eso sigue apareciendo 429 con solo una llamada, revisa el mensaje de `error.message` y `error.metadata.raw`: podría ser una restricción específica del proveedor o del modelo, no necesariamente del RPM de tu cuenta.