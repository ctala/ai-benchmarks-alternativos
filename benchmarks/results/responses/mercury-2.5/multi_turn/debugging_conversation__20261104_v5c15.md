# Mercury 2.5 — multi_turn/debugging_conversation

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.52 | quality: 10.0
- latency_total: 3.759s | tokens_per_second: 413.4
- input_tokens: 339 | output_tokens: 1554

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



Exactamente, el loop infinito convierte un límite temporal en un bloqueo permanente. Cuando el servidor ve miles de requests de tu parte en segundos, bloquea tu IP o API key inmediatamente.

Aquí tienes la estructura correcta para implementar retries en OpenRouter (o cualquier API REST):

### 1. Reglas clave
*   **Máximo de intentos:** Nunca más de 3-5 intentos.
*   **Backoff exponencial:** Espera tiempo más largo entre intentos (1s, 2s, 4s, 8s...).
*   **Respeta `Retry-After`:** Si el servidor envía este header en el 429, usa ese valor exacto en lugar de calcular el tuyo.
*   **Jitter:** Agrega una pequeña variación aleatoria para evitar que muchos clientes intenten al mismo tiempo.

### 2. Ejemplo en Python (`requests`)

```python
import time
import requests

def make_request_with_retry(url, headers, max_retries=5):
    for attempt in range(max_retries):
        response = requests.post(url, headers=headers)
        
        # Si no es 429, procesamos o lanzamos error
        if response.status_code != 429:
            return response
        
        # Si es 429, verificamos el header de espera
        retry_after = response.headers.get('Retry-After')
        if retry_after:
            wait = int(retry_after)
        else:
            # Backoff exponencial base 2, con tope de 60s
            wait = min(2 ** attempt, 60)
        
        # Jitter aleatorio (+-10%)
        wait *= 1 + (random.random() - 0.5) * 0.2
        
        print(f"429 detectado. Reintentando en {wait:.1f}s...")
        time.sleep(wait)
    
    raise Exception("Se agotaron los reintentos tras el 429")
```

### 3. Pasos para arreglar tu caso
1.  **Detén el loop actual:** Busca la estructura `while True` o `retry=True` en tu código y elimínala.
2.  **Añade el límite:** Configura un `max_retries` fijo (ej. 3).
3.  **Verifica headers:** En la respuesta 429, imprime `response.headers` para ver si OpenRouter te está dando tiempo específico para reintentar.

¿Qué lenguaje de programación estás usando actualmente? Puedo ajustarte el snippet si no es Python.