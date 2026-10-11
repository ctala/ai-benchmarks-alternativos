# MiMo V2.6 Flash — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 85.547s | tokens_per_second: 7.0
- input_tokens: 357 | output_tokens: 600

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

Ahí esta el problema. Ese loop de retry infinito esta amplificando tu tasa de requests y causando mas 429s. Asi se arregla:

## Backoff exponencial con jitter

```python
import time
import random
import requests

def call_api(url, headers, payload, max_retries=5):
    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        
        # Solo reintentar 429, abortar en otros errores
        if response.status_code == 429:
            # Leer el header de retry-after si existe
            retry_after = response.headers.get("Retry-After")
            
            if retry_after:
                wait_time = int(retry_after)
            else:
                # Backoff exponencial: 1, 2, 4, 8, 16 segundos
                wait_time = (2 ** attempt) + random.uniform(0, 1)  # + jitter
            
            print(f"429 recibido. Reintento {attempt+1}/{max_retries} en {wait_time:.1f}s")
            time.sleep(wait_time)
            continue
        
        # Otros errores (401, 500, etc) no se reintentan
        raise Exception(f"Error {response.status_code}: {response.text}")
    
    raise Exception("Maximo de reintentos alcanzado")
```

## Lo clave:

| Concepto | Por qué |
|---|---|
| **Max retries limitado** | Evita loops infinitos |
| **Backoff exponencial** | Espera mas con cada intento en vez de golpear siempre |
| **Jitter (aleatorio)** | Evita que todos tus requests golpeen al mismo tiempo |
| **Respetar `Retry-After`** | Si OpenRouter te dice cuanto esperar, escuchalo |
| **Solo reintentar 429** | Otros errores (401, 500) no se arreglan reintentando |

Podes poner un tope mas alto si queres, pero **nunca** deberias hacer mas de ~5 reintentos con este sistema. Con backoff exponencial, 5 intentos te dan hasta 31 segundos de espera acumulada, que es mas que suficiente para que se resuelva un rate limit.