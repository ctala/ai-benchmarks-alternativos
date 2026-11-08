# GLM 5 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 31.607s | tokens_per_second: 62.0
- input_tokens: 331 | output_tokens: 1961

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

¡Bingo! Ese es exactamente el problema. Un loop de retry infinito ante un error 429 crea un efecto avalancha: la API te bloquea temporalmente, tu código intenta arreglarlo haciendo *más* peticiones, la API ve más tráfico malicioso y te bloquea por más tiempo. 

Para arreglar esto, necesitas implementar una estrategia de **Backoff Exponencial con Límite Máximo**. Aquí tienes las 4 reglas de oro para los retries:

1. **Límite máximo de intentos:** Nunca hagas retries infinitos. Un máximo de 3 a 5 intentos es el estándar.
2. **Backoff exponencial:** Si el primer intento falla, espera 1 segundo. Si el segundo falla, espera 2 segundos. Luego 4, luego 8. Esto le da tiempo al servidor de OpenRouter a recuperarse.
3. **Respeta el header `Retry-After`:** Las respuestas 429 suelen incluir un header llamado `Retry-After` que te dice exactamente cuántos segundos debes esperar. Siempre debe tener prioridad sobre tu backoff calculado.
4. **Solo reintentar en errores transitorios:** Haz retry en 429 (Rate limit), 500, 502, 503 o 504. **Nunca** hagas retry en 400 (Bad Request), 401 (Unauthorized) o 404 (Not Found), porque por más que lo intentes, siempre van a fallar.

Aquí tienes un ejemplo en **Python** de cómo deberías estructurarlo:

```python
import time
import requests

def llamar_openrouter(url, headers, payload, max_retries=3):
    for intento in range(max_retries + 1):
        response = requests.post(url, headers=headers, json=payload)
        
        # Si todo sale bien, devolvemos la respuesta
        if response.status_code == 200:
            return response.json()
            
        # Si es un error que NO se debe reintentar (ej. API key incorrecta o prompt malformado)
        if response.status_code in [400, 401, 403, 404]:
            print(f"Error fatal {response.status_code}: No se reintentará.")
            response.raise_for_status()
            
        # Si es un error transitorio (429, 500, etc.) y aún nos quedan intentos
        if intento < max_retries:
            # Calculamos el tiempo de espera (Backoff exponencial: 1s, 2s, 4s...)
            wait_time = 2 ** intento 
            
            # ¡Importante! Revisamos si OpenRouter nos dijo cuánto esperar
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                try:
                    wait_time = int(retry_after)
                except ValueError:
                    pass # Si no es un número, usamos el backoff exponencial
                
            print(f"Error {response.status_code}. Esperando {wait_time}s antes del intento {intento + 2}/{max_retries + 1}...")
            time.sleep(wait_time)
        else:
            # Se agotaron los intentos
            print("Se alcanzó el máximo de reintentos.")
            response.raise_for_status()

# Uso:
# llamar_openrouter("https://openrouter.ai/api/v1/chat/completions", headers, payload)
```

**Pro-tip:** Si estás usando el SDK oficial de OpenAI en Python (que es 100% compatible con OpenRouter solo cambiando la URL base), el SDK ya trae esto configurado por defecto. Solo tienes que instanciarlo así:

```python
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="tu-key",
  max_retries=3 # Esto maneja el backoff exponencial automáticamente
)
```

¿Qué lenguaje o librería estás usando actualmente en tu código para hacer las llamadas? Así te puedo dar la solución exacta para tu stack.