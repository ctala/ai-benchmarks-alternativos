# GPT-6 Luna Pro — multi_turn/debugging_conversation

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 21.972s | tokens_per_second: 165.5
- input_tokens: 4991 | output_tokens: 3637

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

Implementa **reintentos limitados**, con espera exponencial y variación aleatoria (*jitter*). Para un 429, respeta `Retry-After` si OpenRouter lo devuelve; no vuelvas a llamar inmediatamente.

Ejemplo en Python con `requests` —hasta **5 intentos en total**, no 5 reintentos adicionales:

```python
import random
import time
import requests

RETRYABLE = {429, 500, 502, 503, 504}

def llamar_openrouter(payload, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    max_intentos = 5
    base = 1       # segundos
    tope = 30      # segundos

    for intento in range(max_intentos):
        respuesta = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=(5, 60),
        )

        if respuesta.status_code not in RETRYABLE:
            respuesta.raise_for_status()
            return respuesta.json()

        # No hay más intentos: devuelve el error para poder inspeccionarlo.
        if intento == max_intentos - 1:
            respuesta.raise_for_status()

        # Retry-After suele indicar segundos. Si no está, usa backoff exponencial
        # con jitter para que varios clientes no reintenten a la vez.
        retry_after = respuesta.headers.get("Retry-After")
        backoff = random.uniform(0, min(tope, base * (2 ** intento)))

        try:
            espera = max(float(retry_after), backoff) if retry_after else backoff
        except ValueError:
            espera = backoff

        time.sleep(espera)
```

Con esta configuración, las esperas aumentan progresivamente y tienen un máximo. Ajusta `max_intentos` y `tope` según cuánto tiempo estés dispuesto a esperar. Si `Retry-After` viene como fecha HTTP en lugar de segundos, tendrás que convertir esa fecha a una duración.

Algunas recomendaciones:

- No reintentes errores como **400, 401, 403 o 402**: suelen requerir corregir la solicitud, la autenticación o el pago.
- Limita también la **concurrencia** y usa una cola si tu aplicación puede enviar varias solicitudes a la vez.
- Un timeout de red puede ocurrir aunque el servidor haya procesado la solicitud. Reintentar un `POST` en ese caso podría generar una respuesta duplicada o un coste adicional.
- Si el 429 persiste tras unos pocos reintentos, no lo ocultes: registra el cuerpo del error y los headers de la respuesta y revisa los límites aplicables a tu cuenta, modelo o proveedor. Tener saldo no elimina necesariamente todos los límites.