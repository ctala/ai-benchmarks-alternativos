# Nemotron 3 Super — multi_turn/debugging_conversation

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 9.026s | tokens_per_second: 319.0
- input_tokens: 356 | output_tokens: 2879

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

El problema es clásico: un **retry infinito crea una "tormenta de requests"** que te bloquea el rate limit y puede hacer que OpenRouter te ponga en lista negra temporalmente.

Aquí tienes cómo arreglarlo bien, paso a paso.

---

### 1. Detén el código inmediatamente
No ejecutes nada hasta que implementes los límites. Cada 429 que recibas está contando contra tu cupo.

---

### 2. Reglas de oro para reintentos (retries)

| Regla | ¿Por qué? |
|-------|-----------|
| **Máximo de intentos** (ej. 3-5) | Nunca reintentes indefinidamente. |
| **Backoff exponencial** | Esperar 1s, 2s, 4s, 8s... evita saturar el servidor. |
| **Jitter (aleatoriedad)** | Evita que muchos clientes reintenten al mismo tiempo. |
| **Respetar `Retry-After`** | OpenRouter te dice cuánto esperar en los headers. |
| **Solo reintentar errores transitorios** | 429, 500, 502, 503, 504. **No** reintentes 400, 401, 403, 404. |

---

### 3. Ejemplo en Python (sin librerías externas)

Este código usa solo `requests` y `time`:

```python
import requests
import time

API_KEY = "sk-or-..."
URL = "https://openrouter.ai/api/v1/chat/completions"

def llamar_openrouter(payload, max_intentos=5, espera_base=1):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        # Opcional pero recomendado para identificar tu app:
        "HTTP-Referer": "https://tu-app.com",
        "X-Title": "Tu App",
    }

    for intento in range(1, max_intentos + 1):
        try:
            resp = requests.post(URL, headers=headers, json=payload, timeout=30)
        except requests.RequestException as e:
            # Error de red (timeout, DNS, etc.)
            if intento == max_intentos:
                raise
            wait = espera_base * (2 ** (intento - 1))
            print(f"Error de red. Reintentando en {wait}s... ({intento}/{max_intentos})")
            time.sleep(wait)
            continue

        # Éxito
        if resp.status_code == 200:
            return resp.json()

        # Errores permanentes: NO reintentar
        if resp.status_code in (400, 401, 403, 404):
            raise Exception(f"Error permanente {resp.status_code}: {resp.text}")

        # Rate limit o error de servidor: SÍ reintentar
        if resp.status_code in (429, 500, 502, 503, 504):
            # 1. Respetar el header Retry-After si OpenRouter lo envía
            retry_after = resp.headers.get("Retry-After")
            if retry_after:
                wait = int(retry_after)
            else:
                # 2. Backoff exponencial con un poco de jitter
                wait = espera_base * (2 ** (intento - 1)) + (intento * 0.5)

            if intento == max_intentos:
                raise Exception(f"Se agotaron los reintentos. Último error: {resp.status_code} {resp.text}")

            print(f"Rate limit / error servidor ({resp.status_code}). Esperando {wait}s... ({intento}/{max_intentos})")
            time.sleep(wait)
            continue

        # Cualquier otro código inesperado
        raise Exception(f"Error inesperado {resp.status_code}: {resp.text}")

    raise Exception("Se agotaron los reintentos")
```

**Uso:**

```python
payload = {
    "model": "deepseek/deepseek-chat",  # o el ID exacto de DeepSeek V3 en OpenRouter
    "messages": [{"role": "user", "content": "Hola"}],
}

try:
    data = llamar_openrouter(payload)
    print(data)
except Exception as e:
    print(f"Fallo definitivo: {e}")
```

---

### 4. Si usas `tenacity` (recomendado para producción)

Si ya usas o puedes instalar `tenacity`, el código es más limpio:

```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_result
import requests

def es_error_retryable(resp):
    return resp.status_code in (429, 500, 502, 503, 504)

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    retry=retry_if_result(es_error_retryable),
    reraise=True
)
def llamar_openrouter(payload):
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=payload,
        timeout=30,
    )
    # Si es 429 o 5xx, tenacity reintentará automáticamente
    if resp.status_code in (400, 401, 403, 404):
        # Lanzamos excepción para que NO se reintente
        resp.raise_for_status()
    return resp.json()
```

> Nota: `tenacity` por defecto reintenta si la función lanza excepción. Con `retry_if_result` le decimos que reintente según el código de estado del `response`.

---

### 5. ¿Qué hacer ahora para recuperar tu clave?

1. **Apaga el script** con el loop infinito.
2. **Espera 5-10 minutos** sin hacer llamadas. Los límites de OpenRouter se reinician por ventana de tiempo.
3. Revisa tu panel: https://openrouter.ai/settings/limits (o keys) para ver si sigues bloqueado.
4. Si después de esperar sigue dando 429 en la **primera** request, escribe a soporte de OpenRouter mencionando que tuviste un bucle de retry y ya lo corregiste.

---

### 6. Checklist antes de volver a ejecutar

- [ ] El código tiene `max_intentos` definido (máximo 5).
- [ ] No hay `while True` sin condiciones de salida.
- [ ] Se respeta el header `Retry-After` de OpenRouter.
- [ ] No se reintentan errores 401/403 (credenciales malas).
- [ ] Hay un `timeout` en el request (para no dejar conexiones colgadas).

¿Quieres que adapte este ejemplo a otro lenguaje (Node.js, Go, etc.) o a un framework específico (FastAPI, LangChain, etc.)?