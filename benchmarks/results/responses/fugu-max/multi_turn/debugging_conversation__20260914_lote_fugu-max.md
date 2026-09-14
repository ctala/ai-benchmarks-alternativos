# Fugu Max — multi_turn/debugging_conversation

- model_id: `sakana/fugu-max`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 25.945s | tokens_per_second: 117.0
- input_tokens: 385 | output_tokens: 3036

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

La solución es **limitar los reintentos**, aplicar **backoff exponencial con jitter** y respetar `Retry-After`. Además, una cuenta con saldo no implica necesariamente un límite de requests ilimitado: puede haber límites por clave, modelo, proveedor, tokens/minuto o concurrencia.

Un esquema razonable:

- Máximo **4–6 intentos totales**, no reintentos infinitos.
- Reintentar solo `429`, `408`, `500`, `502`, `503` y `504`.
- No reintentar `401`, `402`, `403`, `404` o `422`.
- Usar `Retry-After` si OpenRouter lo envía.
- Si no existe, esperar aproximadamente `1, 2, 4, 8...` segundos con variación aleatoria.
- Añadir un tiempo máximo total, por ejemplo 90 segundos.
- Limitar también la concurrencia; un límite de 5 requests/minuto no evita 20 requests simultáneas.

Ejemplo en Python con `requests`:

```python
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import requests


RETRYABLE_STATUS = {408, 429, 500, 502, 503, 504}

MAX_ATTEMPTS = 5          # Incluye el primer intento
MAX_TOTAL_TIME = 90       # Segundos
MAX_BACKOFF = 30          # Solo se usa si no existe Retry-After


def retry_after_seconds(response):
    value = response.headers.get("Retry-After")

    if not value:
        return None

    # Retry-After puede ser un número de segundos
    try:
        return max(0, float(value))
    except ValueError:
        pass

    # O una fecha HTTP
    try:
        date = parsedate_to_datetime(value)
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)

        return max(
            0,
            (date - datetime.now(timezone.utc)).total_seconds()
        )
    except Exception:
        return None


def call_openrouter(api_key, payload):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # Opcional:
        # "HTTP-Referer": "https://tu-sitio.example",
        # "X-Title": "Mi aplicación",
    }

    session = requests.Session()
    started_at = time.monotonic()

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            response = session.post(
                url,
                headers=headers,
                json=payload,
                timeout=(10, 120),
            )

        except (requests.Timeout, requests.ConnectionError) as error:
            if attempt >= MAX_ATTEMPTS:
                raise RuntimeError(
                    "La solicitud falló después de agotar los reintentos"
                ) from error

            # Backoff con jitter para errores de red
            delay = random.uniform(
                0,
                min(MAX_BACKOFF, 2 ** (attempt - 1))
            )

            if time.monotonic() - started_at + delay > MAX_TOTAL_TIME:
                raise RuntimeError(
                    "Se alcanzó el tiempo máximo de reintentos"
                ) from error

            print(
                f"Error de red. Reintento {attempt + 1}/{MAX_ATTEMPTS} "
                f"en {delay:.2f}s"
            )
            time.sleep(delay)
            continue

        if 200 <= response.status_code < 300:
            return response.json()

        status = response.status_code

        # Errores permanentes: no tiene sentido repetirlos
        if status not in RETRYABLE_STATUS:
            raise RuntimeError(
                f"OpenRouter devolvió HTTP {status}: "
                f"{response.text[:1000]}"
            )

        # Ya no quedan intentos
        if attempt >= MAX_ATTEMPTS:
            raise RuntimeError(
                f"OpenRouter devolvió HTTP {status} tras "
                f"{MAX_ATTEMPTS} intentos: {response.text[:1000]}"
            )

        server_delay = retry_after_seconds(response)

        if server_delay is not None:
            # Respetar la indicación del servidor
            delay = server_delay
        else:
            # Full jitter: reduce sincronización entre workers
            delay = random.uniform(
                0,
                min(MAX_BACKOFF, 2 ** (attempt - 1))
            )

        elapsed = time.monotonic() - started_at
        if elapsed + delay > MAX_TOTAL_TIME:
            raise RuntimeError(
                f"HTTP {status}; el siguiente reintento excedería "
                f"el tiempo máximo permitido"
            )

        print(
            f"HTTP {status}. Reintento {attempt + 1}/{MAX_ATTEMPTS} "
            f"en {delay:.2f}s"
        )

        # Cerrar la respuesta antes de esperar
        response.close()
        time.sleep(delay)

    raise RuntimeError("No se pudo completar la solicitud")
```

Payload de ejemplo:

```python
result = call_openrouter(
    api_key="TU_API_KEY",
    payload={
        "model": "deepseek/deepseek-chat",
        "messages": [
            {"role": "user", "content": "Hola"}
        ],
        "temperature": 0.2,
    },
)

print(result)
```

También conviene registrar, sin mostrar la API key, estos datos de la respuesta:

```python
print(response.status_code)
print(response.headers.get("Retry-After"))
print(response.headers.get("x-ratelimit-limit"))
print(response.headers.get("x-ratelimit-remaining"))
print(response.headers.get("x-ratelimit-reset"))
print(response.text[:1000])
```

Puntos importantes:

1. **Detén ahora el proceso que está haciendo retries infinitos.** Es posible que el límite temporal siga activo durante un rato.
2. **No crees un cliente nuevo en cada llamada** si tu librería usa pools o conexiones reutilizables.
3. **Limita la concurrencia**, por ejemplo con un semáforo de 1–3 solicitudes simultáneas.
4. Los límites pueden ser por **tokens**, no solo por requests. Cinco prompts grandes por minuto pueden superar un límite aunque el número de llamadas parezca bajo.
5. En respuestas en streaming, reintenta solo si el error ocurre **antes de recibir el primer token**. Si el stream se corta después, reintentar puede generar una respuesta duplicada y cobrar otra generación.
6. Si el cuerpo del `429` indica un problema de créditos, cuenta, modelo o proveedor, el backoff no lo solucionará: habrá que corregir esa causa o seleccionar otro proveedor/modelo.

La cifra de “300 RPM” no debe asumirse como garantizada; el límite efectivo depende de la configuración de OpenRouter y del proveedor que atienda ese modelo.