# GLM-5.1 — multi_turn/debugging_conversation

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 29.739s | tokens_per_second: 66.7
- input_tokens: 331 | output_tokens: 1983

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

¡Excelente detective! Ese loop infinito es exactamente la causa raíz. Al recibir un 429, tu código lanza 100 peticiones más instantáneamente, lo que genera más 429s y crea un efecto avalancha. OpenRouter termina bloqueando tu IP o tu clave temporalmente para proteger el sistema.

Para arreglar esto, un buen sistema de reintentos (retries) debe tener 4 reglas básicas:

1. **Límite máximo de intentos:** Nunca hacer reintentos infinitos. Usa un máximo (ej. 3 o 5).
2. **Backoff exponencial (Exponential Backoff):** No reintentar inmediatamente. Si el primer intento falla, espera 2 segundos. Si el segundo falla, espera 4. Si el tercero falla, espera 8.
3. **Respetar el header `Retry-After`:** Las APIs suelen enviar este header indicando exactamente cuántos segundos debes esperar.
4. **Solo reintentar en errores recuperables:** Solo debes reintentar en códigos `429` (Rate limit) y `5xx` (errores del servidor). Si es un `400` (Bad Request) o `401` (Unauthorized), reintentar no sirve de nada y solo gastará recursos.

Aquí tienes un ejemplo en **Python** usando la librería `requests` que implementa estas reglas:

```python
import requests
import time

def llamar_openrouter(prompt, max_retries=3):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    for intento in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)
        
        # Si todo va bien, devolvemos el resultado
        if response.status_code == 200:
            return response.json()
            
        # Si es 429 o un error del servidor (5xx), entramos al retry
        elif response.status_code == 429 or response.status_code >= 500:
            # Revisamos si la API nos dice cuánto esperar
            retry_after = response.headers.get("Retry-After")
            
            if retry_after:
                # Si el header existe, esperamos ese tiempo + un pequeño margen
                wait_time = int(retry_after) + 1
            else:
                # Si no, usamos backoff exponencial: 2s, 4s, 8s...
                wait_time = 2 ** intento
                
            print(f"Error {response.status_code}. Esperando {wait_time} segundos... (Intento {intento + 1}/{max_retries})")
            time.sleep(wait_time)
            
        # Si es un error 4xx (ej: 400, 401), no tiene sentido reintentar
        else:
            print(f"Error fatal {response.status_code}: {response.text}")
            response.raise_for_status() # Lanza la excepción y detiene el loop

    # Si se acaban los intentos, lanzamos error
    raise Exception(f"Falló después de {max_retries} intentos.")
```

### Alternativa mucho más simple (si usas el SDK de OpenAI)
Si estás usando Python y el SDK oficial de OpenAI (que es compatible con OpenRouter solo cambiando la `base_url`), ¡no necesitas programar esto! El SDK ya tiene un sistema de reintentos incorporado que hace exactamente esto por debajo.

Solo debes instanciar el cliente así:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY",
    max_retries=3,  # <--- Esto maneja el 429 automáticamente con backoff exponencial
)
```

**¿Qué lenguaje o librería estás usando para hacer las llamadas?** Si no es Python, te puedo dar el snippet exacto para tu stack (Node.js, Go, etc.).