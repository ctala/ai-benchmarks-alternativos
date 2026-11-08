# Llama 4 Maverick — multi_turn/debugging_conversation

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.56 | quality: 7.5
- latency_total: 4.347s | tokens_per_second: 90.2
- input_tokens: 322 | output_tokens: 392

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

Un loop infinito de retries es un problema común. Para implementarlo correctamente, debes seguir estas pautas:

1. **Limita el número de retries**: No más de 3-5 intentos.
2. **Implementa un backoff exponencial**: Aumenta el tiempo de espera entre retries.
3. **Detecta errores recuperables**: Solo haz retry para errores como 429, 503, timeouts.

Ejemplo en Python:
```python
import time
import random
import requests

def hacer_request(url, params):
    max_retries = 3
    retry_delay = 1  # segundos

    for intento in range(max_retries + 1):
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()  # Lanza excepción para 4xx/5xx
            return response.json()
        except requests.HTTPError as e:
            if e.response.status_code == 429:
                # Backoff exponencial con jitter
                retry_delay *= 2
                retry_delay_with_jitter = retry_delay * (1 + random.random())
                print(f"Retry {intento+1}/{max_retries} en {retry_delay_with_jitter:.2f}s")
                time.sleep(retry_delay_with_jitter)
            else:
                raise  # No retry para otros errores
        except requests.RequestException as e:
            # Otros errores de request (timeout, conexión, etc.)
            if intento < max_retries:
                retry_delay *= 2
                time.sleep(retry_delay)
            else:
                raise

    # Si llegamos aquí, se agotaron los retries
    raise Exception("Max retries exceeded")
```
Esto te permite:
- Limitar el número de intentos
- Esperar más tiempo entre retries
- Manejar específicamente el error 429

Ajusta `max_retries` y los tiempos de espera según tus necesidades.