# Seed 2.1 Turbo — multi_turn/debugging_conversation

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 59.677s | tokens_per_second: 47.9
- input_tokens: 389 | output_tokens: 2856

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

Perfecto, ya encontraste la causa raíz: el **retry inmediato e infinito genera un efecto cascada**: 1 error 429 → 100 reintentos en segundos → más 429 → más reintentos, hasta que te quedas sin cupo de rate limit por completo.

La solución es implementar **retries inteligentes** que cumplan estas reglas obligatorias:
1. Número máximo de reintentos (nunca infinito)
2. Espera progresiva entre reintentos (exponential backoff)
3. Respetar el header `Retry-After` que envía OpenRouter (te dice exactamente cuántos segundos esperar)
4. Solo reintentar errores transitorios (429, 5xx, timeouts), no errores de cliente (400, 401, etc.)

---

## Ejemplo práctico (más común: SDK de OpenAI compatible con OpenRouter)
Si usas el SDK oficial de OpenAI (el estándar para conectarse a OpenRouter, ya que es compatible con su API), ya trae retries inteligentes integrados, solo tienes que configurarlos bien:

```python
from openai import OpenAI

# Configura el cliente con OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="TU_API_KEY_DE_OPENROUTER",
  # Configuración de retries CORRECTA:
  max_retries=5,  # Máximo 5 reintentos (nunca infinito)
  timeout=30,
)

# Tu llamada normal
response = client.chat.completions.create(
  model="deepseek/deepseek-chat-v3:free", # O el modelo que uses
  messages=[{"role": "user", "content": "Hola"}],
)
```

### ¿Qué hace el SDK por ti automáticamente?
- Usa **exponential backoff con jitter**: espera 1s, 2s, 4s, 8s, 16s... (con un valor aleatorio para evitar picos)
- Respeta el header `Retry-After` que envía OpenRouter (si el servidor te dice que esperes 10s, usa ese valor en vez del backoff)
- Solo reintenta errores transitorios: 429, 500, 502, 503, 504 y timeouts
- No reintenta errores de cliente (400, 401, 403) que no se solucionan reintentando

---

## Si haces llamadas manuales (sin SDK, con `requests` en Python)
Implementa el backoff manualmente, leyendo el header `Retry-After` para ser más preciso:

```python
import requests
import time
import random

MAX_RETRIES = 5
BASE_WAIT = 1  # Segundo base de espera

def llamar_openrouter(mensaje):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-chat-v3:free",
        "messages": [{"role": "user", "content": mensaje}]
    }

    for intento in range(MAX_RETRIES):
        response = requests.post(url, headers=headers, json=data)
        
        # Si la respuesta es exitosa, devuélvela
        if response.status_code == 200:
            return response.json()
        
        # Si es un error que NO se reintenta, lanza excepción inmediatamente
        if response.status_code in [400, 401, 403, 404, 422]:
            raise Exception(f"Error no transitorio: {response.status_code} - {response.text}")
        
        # Si es 429 o error de servidor, esperamos antes de reintentar
        if response.status_code in [429, 500, 502, 503, 504]:
            # Primero intentamos usar el valor de Retry-After que envía OpenRouter
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                wait_time = float(retry_after)
            else:
                # Si no hay Retry-After, usamos exponential backoff con jitter
                wait_time = BASE_WAIT * (2 ** intento) + random.uniform(0, 1)
            
            print(f"Intento {intento+1} fallido (status {response.status_code}). Esperando {wait_time:.1f}s...")
            time.sleep(wait_time)
            continue
    
    # Si se acabaron los reintentos
    raise Exception(f"Se agotaron los {MAX_RETRIES} reintentos. Último error: {response.status_code} - {response.text}")

# Uso
respuesta = llamar_openrouter("Hola")
print(respuesta)
```

---

## Buenas prácticas adicionales para evitar 429 con OpenRouter
1. **Monitorea los límites restantes antes de llegar al error**:
   OpenRouter envía headers en cada respuesta con tu estado de rate limit:
   - `x-ratelimit-remaining-requests`: cuántas requests te quedan en la ventana actual
   - `x-ratelimit-reset-requests`: cuántos segundos faltan para que se restablezca el límite
   
   Puedes leerlos para pausar tus llamadas antes de recibir un 429.

2. **Si usas múltiples threads/workers**:
   El rate limit es por API key, no por instancia de código. Usa un **rate limiter compartido** (ej: algoritmo de Token Bucket) para no superar el límite global.

3. **Verifica tu límite exacto**:
   Para DeepSeek V3 con cuenta pagada, el límite estándar es 300 requests/minuto y 1000 tokens/segundo. Puedes comprobar tus límites específicos en el [dashboard de OpenRouter](https://openrouter.ai/keys) seleccionando tu API key.

---

## ¿Cómo verificar que funciona?
Después de implementar los retries:
1. Ejecuta tu código y revisa los logs: no deberías ver más de 5 reintentos por error
2. Si recibes un 429, verás que el código espera el tiempo indicado antes de reintentar
3. Revisa el header `x-ratelimit-remaining-requests` en las respuestas exitosas para confirmar que no te acercas al límite

Si sigues teniendo problemas después de esto, revisa si tienes otras instancias del código corriendo al mismo tiempo (ej: en producción + pruebas locales) que estén consumiendo el rate limit de la misma key.