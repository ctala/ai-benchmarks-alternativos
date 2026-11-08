# Inkling Small — multi_turn/debugging_conversation

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 34.75s | tokens_per_second: 38.8
- input_tokens: 313 | output_tokens: 1348

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

Exacto: ese es el problema. Un loop infinito de retry convierte **una** llamada fallida en **cientos**, y el 429 se auto-perpetúa. Vamos a arreglarlo con una política de retries segura.

### Reglas de oro para retries en APIs (especialmente OpenRouter):

1. **Máximo de intentos** (ej: 3 o 5), nunca infinito.
2. **Backoff exponencial**: espera 1s, luego 2s, 4s, 8s... para no saturar.
3. **Solo reintentar códigos específicos**: 429, 500, 502, 503, 504. **Nunca** reintentar 401/403 (gastarías créditos sin sentido).
4. **Respetar `Retry-After`**: si el 429 trae ese header, usa ese tiempo mínimo.
5. **No lanzar requests en paralelo** sin control: si haces 5/min pero con 10 hilos, rompes el límite.

### Implementación correcta (Python, con `requests`):

```python
import time
import requests

def call_openrouter(prompt, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            
            # Éxito
            if resp.status_code == 200:
                return resp.json()
            
            # Si es 429, intenta reintentar con backoff
            if resp.status_code == 429:
                # Leer header de espera si existe
                retry_after = resp.headers.get("Retry-After")
                if retry_after:
                    wait = int(retry_after)
                else:
                    wait = 2 ** attempt  # 2, 4, 8...
                
                print(f"429 en intento {attempt}. Esperando {wait}s...")
                time.sleep(wait)
                continue  # va al siguiente intento
            
            # Errores que NO se deben reintentar (401, 403, 400, etc.)
            resp.raise_for_status()
            return resp.json()

        except requests.exceptions.RequestException as e:
            if attempt == max_retries:
                raise e
            wait = 2 ** attempt
            print(f"Error en intento {attempt}: {e}. Esperando {wait}s...")
            time.sleep(wait)

    raise Exception("Máximo de reintentos alcanzado")
```

### ¿Qué cambia respecto a tu loop anterior?

- **`for attempt in range(...)`**: límite estricto. No hay `while True`.
- **`continue` solo en 429**: si es otro error, lanza o sale.
- **`time.sleep()`**: evita la tormenta de requests.
- **`2 ** attempt`**: backoff exponencial.

### Extra para tu caso específico:

Como usas **DeepSeek V3** y tienes créditos pagados:
- El límite de OpenRouter es ~300 RPM por clave, pero si usas un modelo con alta demanda, puede haber throttling temporal.
- Si haces 5/min, con esta implementación deberías pasar sin problemas.
- **No uses `while True` ni `recursión` sin límite** para retries.

Si quieres algo más robusto sin escribirlo a mano, usa la librería `tenacity`:

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(requests.HTTPError)  # puedes filtrar por status
)
def call(...):
    ...
```

**Prueba con `max_retries=3` y `wait=2**attempt` primero.** ¿Quieres que revisemos cómo estás lanzando esas 5 requests (¿en paralelo con `threading`?) para asegurarnos de que no se acumulen?