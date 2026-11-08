# GPT-6 Astra — multi_turn/debugging_conversation

- model_id: `openai/gpt-6-astra`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 22.706s | tokens_per_second: 47.6
- input_tokens: 312 | output_tokens: 1081

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

Sí: ese bucle convierte un error puntual en una **tormenta de reintentos**. Primero detén el proceso y deja pasar el período de bloqueo antes de probar de nuevo.

También corrijo algo de mi respuesta anterior: **no debía haber afirmado un límite fijo de 300 RPM**. Los límites pueden depender del modelo, del proveedor y de tu cuenta; tener saldo no garantiza que no haya un 429.

### Cómo implementar los reintentos

- **Máximo de intentos:** por ejemplo, 4 en total —la llamada original y 3 reintentos—.
- **Backoff exponencial con jitter:** esperar cada vez más, con una variación aleatoria para evitar que todos los procesos reintenten a la vez.
- **Respetar `Retry-After`:** si el servidor indica cuánto esperar, no reintentar antes.
- **Reintentar solo errores transitorios:** normalmente `429`, `502`, `503` y `504`. No reintentar automáticamente `400`, `401` o `403`.
- **Evitar capas duplicadas:** si usas tus propios reintentos, desactiva los del SDK, o viceversa.

### Ejemplo en Python

Este ejemplo usa `requests`, sin reintentos internos por defecto:

```python
import random
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

import requests


def retry_after_seconds(value):
    if not value:
        return 0.0

    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            date = parsedate_to_datetime(value)
            return max(
                0.0,
                (date - datetime.now(timezone.utc)).total_seconds()
            )
        except (ValueError, TypeError, OverflowError):
            return 0.0


def llamar_openrouter(api_key, payload, max_intentos=4):
    if max_intentos < 1:
        raise ValueError("max_intentos debe ser al menos 1")

    with requests.Session() as session:
        for intento in range(max_intentos):
            response = session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json=payload,
                timeout=(10, 60),  # conexión y lectura
            )

            if response.ok:
                return response.json()

            transitorio = response.status_code in {429, 502, 503, 504}
            ultimo_intento = intento == max_intentos - 1

            if not transitorio or ultimo_intento:
                response.raise_for_status()

            # Esperas crecientes con variación aleatoria.
            base = min(30, 2 ** (intento + 1))
            espera = max(
                random.uniform(base / 2, base),
                retry_after_seconds(response.headers.get("Retry-After")),
            )

            # No mantener este proceso bloqueado indefinidamente.
            # Si el servidor pide más tiempo, abortar en vez de
            # reintentar antes de lo permitido.
            if espera > 120:
                response.raise_for_status()

            print(
                f"HTTP {response.status_code}: "
                f"reintento {intento + 1}/{max_intentos - 1} "
                f"en {espera:.1f}s"
            )
            time.sleep(espera)
```

**Importante:**
- No rodees esta función con otro bucle infinito que la vuelva a ejecutar si falla: eso anularía el límite.
- Si tienes varios workers, limita también la concurrencia y la tasa de llamadas **entre todos**, no solo por worker.
- Este ejemplo deja que los errores de conexión y timeout se propaguen. Reintentarlos requiere cuidado: si el servidor ya procesó la generación, podrías duplicar trabajo y coste.

Después de detener el bucle y esperar, prueba **una sola llamada**. Si sigue devolviendo `429`, revisa el cuerpo del error y `Retry-After`: puede ser una cuota agotada o saturación del proveedor, algo que los reintentos por sí solos no solucionan.