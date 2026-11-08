# Gemma 4 31B — multi_turn/debugging_conversation

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.34 | quality: 7.5
- latency_total: 13.166s | tokens_per_second: 65.7
- input_tokens: 344 | output_tokens: 865

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

Ahí tienes el culpable. Has creado un **ataque de denegación de servicio (DoS) accidental** contra tu propia cuenta. El servidor te da un 429, tu código entra en pánico y lanza 100 peticiones más, lo que hace que el servidor te bloquee aún más agresivamente.

Para solucionar esto, debes implementar una estrategia llamada **Exponential Backoff (Retroceso Exponencial)**.

### La Regla de Oro: No reintentes inmediatamente

En lugar de un loop infinito, el flujo debe ser:
`Error 429` $\rightarrow$ `Esperar X segundos` $\rightarrow$ `Reintentar` $\rightarrow$ `Si falla, esperar 2X segundos` $\rightarrow$ `Reintentar`.

Aquí tienes cómo implementarlo correctamente en Python (usando la librería `tenacity`, que es el estándar de la industria para esto):

#### 1. Instalación
```bash
pip install tenacity
```

#### 2. Implementación Profesional
```python
import openai # OpenRouter usa el formato de OpenAI
from tenacity import (
    retry, 
    stop_after_attempt, 
    wait_random_exponential, 
    retry_if_exception_type
)

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY",
)

# Esta es la magia:
@retry(
    # 1. Espera exponencial: empieza con 1s, luego 2s, 4s, etc. 
    # El "random" evita que miles de clientes reintenten al mismo milisegundo (Thundering Herd)
    wait=wait_random_exponential(min=1, max=60), 
    # 2. No reintentar infinitamente. Después de 5 veces, ríndete y lanza el error.
    stop=stop_after_attempt(5), 
    # 3. Solo reintentar si el error es de RateLimit (429)
    retry=retry_if_exception_type(openai.RateLimitError) 
)
def call_openrouter_safe():
    return client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Hola"}]
    )

try:
    response = call_openrouter_safe()
    print(response.choices[0].message.content)
except openai.RateLimitError:
    print("Límite excedido incluso después de 5 reintentos. Deteniendo proceso.")
except Exception as e:
    print(f"Error no relacionado con RateLimit: {e}")
```

### ¿Por qué este enfoque soluciona tu problema?

1.  **`wait_random_exponential`**: Si el servidor está saturado, darle un respiro es la única forma de que te deje entrar. Al aumentar el tiempo de espera, permites que tu "cuota" de requests se resetee.
2.  **`stop_after_attempt(5)`**: Evita el loop infinito. Si después de 5 intentos (que habrán tomado varios minutos) sigues recibiendo 429, significa que hay un problema mayor (ej. saldo agotado o caída global del modelo) y el programa debe detenerse.
3.  **`retry_if_exception_type`**: Muy importante. **No** debes reintentar si el error es un `400` (Bad Request) o `401` (API Key inválida), porque esos errores nunca se arreglarán reintentando; solo gastarías recursos.

**Consejo final:** Antes de ejecutar el código corregido, espera unos 5-10 minutos sin hacer ninguna petición para que el sistema de seguridad de OpenRouter "limpie" tu IP del estado de bloqueo.