# Ling 3.0 Flash VL — multi_turn/debugging_conversation

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 13.064s | tokens_per_second: 124.8
- input_tokens: 396 | output_tokens: 1631

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

¡Bien que lo encontraste! Eso explica perfectamente por qué 5 req/min se convirtieron en miles. Vamos a arreglarlo correctamente:

---

## Principios clave para retries

1. **Nunca retry infinito** - siempre pon un máximo
2. **Backoff exponencial** - espera más tiempo entre cada reintento
3. **Respeta `Retry-After`** - OpenRouter lo incluye en la respuesta 429
4. **No hagas retry de inmediato** - espera al menos 1-2 segundos

---

## Implementación manual (Python)

```python
import time
import requests

def call_openrouter(messages, model="deepseek/deepseek-v3", max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-tu-api-key",
        "HTTP-Referer": "tu-app-url",
        "X-Title": "tu-app-name",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            
            elif response.status_code == 429:
                # Respetar el header Retry-After si existe
                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait = float(retry_after)
                else:
                    # Backoff exponencial: 2s, 4s, 8s, 16s, 32s
                    wait = 2 ** (attempt + 1)
                
                wait = min(wait, 60)  # Tope de 60 segundos
                print(f"429 recibido. Esperando {wait}s (intento {attempt + 1}/{max_retries})")
                time.sleep(wait)
            
            else:
                response.raise_for_status()  # Lanza excepcion para otros errores

        except requests.exceptions.Timeout:
            wait = 2 ** (attempt + 1)
            print(f"Timeout. Reintentando en {wait}s...")
            time.sleep(wait)

    raise Exception(f"Se agotaron {max_retries} reintentos")
```

---

## Alternativa con `tenacity` (más limpio)

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=60),
    retry=retry_if_exception_type(requests.exceptions.HTTPError),
    reraise=True
)
def call_openrouter(messages, model="deepseek/deepseek-v3"):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer sk-tu-api-key",
        "Content-Type": "application/json"
    }
    payload = {"model": model, "messages": messages}
    
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    
    # Convertir 429 en excepcion para que tenacity haga retry
    if response.status_code == 429:
        raise requests.exceptions.HTTPError("Rate limited", response=response)
    
    response.raise_for_status()
    return response.json()
```

---

## Resumen de lo que estaba mal vs lo correcto

| ❌ Tu código actual | ✅ Implementación correcta |
|---|---|
| Retry infinito | Máximo 5-6 intentos |
| Retry inmediato | Espera creciente (2s → 4s → 8s...) |
| Ignora `Retry-After` | Lo respeta si viene en el header |
| Cada 429 genera 100 requests | Cada 429 genera 1 solo reintento |

---

## Extra: circuit breaker (opcional)

Si quieres ir un paso más allá, puedes parar de hacer requests completamente durante X segundos si recibes muchos 429 seguidos:

```python
class CircuitBreaker:
    def __init__(self, max_failures=3, reset_timeout=30):
        self.failures = 0
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.last_failure_time = None
    
    def allow_request(self):
        if self.failures >= self.max_failures:
            if time.time() - self.last_failure_time < self.reset_timeout:
                return False
            self.failures = 0  # Resetear despues del timeout
        return True
    
    def record_failure(self):
        self.failures += 1
        self.last_failure_time = time.time()
    
    def record_success(self):
        self.failures = 0
```

---

Con estos cambios tus 5 req/min van a funcionar perfectamente. Lo primero que te recomiendo es **quitar ya el retry infinito** y luego implementar el backoff exponencial. ¿Tienes el código en algún lenguaje específico? Te puedo adaptar la solución.