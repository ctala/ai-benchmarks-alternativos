# Muse Spark 1.3 — multi_turn/debugging_conversation

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 9.78s | tokens_per_second: 176.9
- input_tokens: 332 | output_tokens: 1730

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

¡Perfecto, encontraste la causa raíz! Eso es clásico: un 429 ocasional + retry infinito = te auto-bloqueas.

No es que 5 req/min sea mucho, es que cuando falla 1 vez, tu código genera 100 más en segundos y OpenRouter te castiga más tiempo.

Aquí cómo arreglarlo bien:

### 1. La regla de oro para retries

Nunca hagas `while True` sin límite. Usa esto:

1.  **Máximo 3-5 intentos**, no infinito
2.  **Exponential backoff + jitter** (esperar cada vez más tiempo)
3.  **Respeta el header `Retry-After`** si OpenRouter te lo manda
4.  **Solo reintenta 429 y 5xx**, no 400, 401, 402, 404

### 2. Implementación correcta en Python

Si usas Python con `requests` / cliente OpenAI:

```python
import time
import random
import requests

MAX_RETRIES = 4

def llamar_openrouter(payload, headers):
    for intento in range(MAX_RETRIES):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            json=payload,
            headers=headers
        )
        
        # Éxito, salimos
        if response.status_code == 200:
            return response.json()
        
        # Errores que NO se deben reintentar
        if response.status_code in [400, 401, 402, 404]:
            print(f"Error fatal {response.status_code}: {response.text}")
            break
        
        # Errores que SÍ se reintentan: 429 y 5xx
        if response.status_code == 429 or 500 <= response.status_code < 600:
            # 1. Revisa si OpenRouter te dice cuánto esperar
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                espera = float(retry_after)
            else:
                # 2. Exponential backoff: 1s, 2s, 4s, 8s... + jitter aleatorio
                espera = (2 ** intento) + random.uniform(0, 1)
            
            print(f"429 recibido. Intento {intento+1}/{MAX_RETRIES}. Esperando {espera:.1f}s...")
            time.sleep(espera)
            continue
    
    raise Exception(f"Falló después de {MAX_RETRIES} intentos")
```

Si usas la librería `tenacity` es aún más limpio:
`pip install tenacity`

### 3. Qué buscar en tu código actual

Seguro tienes algo así:
```python
# MAL
while error:
    reintentar() # sin sleep, sin contador
```

Cámbialo por un `for intento in range(3)` + `time.sleep()`.

> Tip extra: Agrega un log cada vez que recibas 429. Así verás si fue solo 1 evento aislado que tu loop convirtió en 100.

¿En qué lenguaje / librería tienes tu loop? Pégame ese pedacito de código y te lo reescribo ya corregido.