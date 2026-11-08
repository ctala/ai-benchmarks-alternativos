# Kimi K2.5 — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 51.776s | tokens_per_second: 29.0
- input_tokens: 385 | output_tokens: 1501

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

El problema está claro: **un 429 legítimo (o incluso otro error) activa tu loop de retry sin backoff, lo que genera un ataque DDoS contra tu propia API key**, bloqueándote completamente.

Aquí tienes cómo implementar retries correctamente. Te doy un ejemplo robusto en Python (fácil de adaptar a cualquier lenguaje):

### Principios clave
1. **Límite máximo absoluto** (ej: 3-5 intentos)
2. **Backoff exponencial** (esperar 1s, 2s, 4s, 8s...)
3. **Jitter** (añadir aleatoriedad para no sincronizar picos)
4. **No hacer retry en errores del cliente** (400, 401, 403) — **excepto 429**
5. **Leer los headers de rate limit** de OpenRouter para saber cuándo reintentar

---

### Implementación correcta (Python con `requests`)

```python
import requests
import time
import random
from typing import Optional

def call_openrouter(messages, max_retries=3):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://tu-sitio.com",  # Requerido por OpenRouter
        "X-Title": "Tu App"
    }
    
    for attempt in range(max_retries + 1):  # +1 para el intento inicial
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": "deepseek/deepseek-chat",
                    "messages": messages
                },
                timeout=30
            )
            
            # ÉXITO
            if response.status_code == 200:
                return response.json()
            
            # ERRORES QUE NO DEBEN REINTENTARSE NUNCA
            if response.status_code in (400, 401, 403):
                print(f"Error del cliente {response.status_code}: {response.text}")
                raise Exception(f"Fallo irreparable: {response.status_code}")
            
            # RATE LIMIT (429) - ÚLTIMO intento no reintenta
            if response.status_code == 429:
                if attempt == max_retries:
                    raise Exception("Rate limit persistente tras máximo de reintentos")
                
                # OpenRouter a veces manda 'Retry-After' o info en headers
                retry_after = response.headers.get("Retry-After")
                
                if retry_after:
                    wait = int(retry_after)
                else:
                    # Backoff exponencial + jitter: 2^attempt + random
                    wait = (2 ** attempt) + random.uniform(0, 1)
                
                print(f"429 recibido. Esperando {wait:.2f}s antes de reintentar...")
                time.sleep(wait)
                continue  # Va al siguiente intento
            
            # OTROS 5xx o errores de servidor - reintentar con backoff
            if attempt < max_retries:
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"Error {response.status_code}. Esperando {wait:.2f}s...")
                time.sleep(wait)
                continue
            else:
                raise Exception(f"Error persistente: {response.status_code}")
                
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"Timeout. Reintentando en {wait:.2f}s...")
                time.sleep(wait)
            else:
                raise Exception("Timeout persistente")
                
        except requests.exceptions.RequestException as e:
            # Errores de red (DNS, conexión) - reintentar pocas veces
            if attempt < max_retries:
                wait = (2 ** attempt) + random.uniform(0, 1)
                time.sleep(wait)
            else:
                raise e

# Uso
try:
    result = call_openrouter([{"role": "user", "content": "Hola"}])
except Exception as e:
    print(f"Fallo definitivo: {e}")
```

---

### Qué hacer AHORA para salir del bloqueo

1. **Detén tu script inmediatamente** — cada segundo que siga ejecutándose empeora el bloqueo.
2. **Espera 1-2 minutos** — OpenRouter suele liberar el rate limit rápido si dejas de hacer requests.
3. **Verifica tu dashboard** en OpenRouter para ver si hay algún "limit" adicional activo.
4. **Reinicia con el código nuevo** con `max_retries=2` al principio para probar.

### Consejo adicional para OpenRouter

OpenRouter tiene límites **por modelo** y **por nivel de key**. Aunque tengas $20, si usas modelos "gratuitos" o con alta demanda, el rate limit puede ser más agresivo. DeepSeek V3 generalmente permite **hasta 300 RPM**, pero si estás en una key nueva o compartida, pueden aplicar límites más conservadores temporalmente.

¿Necesitas que adapte el código a otro lenguaje (Node.js, Go, etc.) o que le agregue manejo de circuit breaker para producción?