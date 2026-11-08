# Seed 2.0 Code — multi_turn/debugging_conversation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 76.024s | tokens_per_second: 74.6
- input_tokens: 389 | output_tokens: 5671

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

¡Genial que encontraste la causa raíz! El loop infinito de retries es el problema típico que convierte un 429 ocasional en un bloqueo total (cada retry genera más requests, que generan más 429, y así sucesivamente).

Para arreglarlo, debes implementar **retries inteligentes que no empeoren el rate limit**. Aquí te explico los principios obligatorios y ejemplos listos para usar (asumimos Python, que es el más común para OpenRouter):

---

### 📌 Principios OBLIGATORIOS para retries en APIs
1. **Límite máximo de retries**: Nunca reintentar infinitamente (ej: max 5 intentos)
2. **Exponential Backoff + Jitter**: Esperar más tiempo cada retry (1s → 2s → 4s...) con un valor aleatorio para evitar colisiones de múltiples clientes
3. **Respetar el header `Retry-After`**: OpenRouter te dice EXACTAMENTE cuánto esperar en sus headers (`retry-after` o `x-ratelimit-retry-after`), usa ese valor si está disponible
4. **Solo reintentar errores recuperables**: No reintentar errores como 400 (Bad Request) o 401 (Key inválida), solo 429 (Rate Limit) o errores 5xx del servidor

---

### ✅ Ejemplo RECOMENDADO (con `tenacity` + cliente OpenAI compatible)
Usamos la librería `tenacity` (robusta para retries) y el cliente oficial de OpenAI (OpenRouter es 100% compatible con su API):

#### Paso 1: Instalar dependencias
```bash
pip install tenacity openai python-dotenv
```

#### Paso 2: Código listo para usar
```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential_jitter,
    retry_if_exception_type,
    wait_combine,
)
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os

# Cargar API key desde archivo .env (NUNCA hardcodees tu key!)
load_dotenv()

# Configurar cliente de OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Función para extraer el header `Retry-After` de la respuesta de OpenRouter
def wait_retry_after(retry_state):
    """Usa el tiempo de espera que te indica OpenRouter, si está disponible"""
    exception = retry_state.outcome.exception()
    if isinstance(exception, RateLimitError):
        # OpenRouter devuelve estos headers con el tiempo de espera en segundos
        headers = exception.response.headers
        retry_after = headers.get("retry-after") or headers.get("x-ratelimit-retry-after")
        if retry_after:
            return float(retry_after) + 0.5  # +0.5s de margen
    return 0  # Si no hay header, usa el Exponential Backoff

# Decorador que configura los retries INTELIGENTES
@retry(
    # 1. Límite de retries: Máximo 5 intentos (evita loops infinitos)
    stop=stop_after_attempt(5),
    # 2. Estrategia de espera: Combina el Retry-After de OpenRouter + Backoff con Jitter
    wait=wait_combine(
        wait_retry_after,  # Primero intenta usar el tiempo que te dice OpenRouter
        wait_exponential_jitter(multiplier=1, min=1, max=10)  # Sino: 1s → 2s → 4s → max 10s + jitter
    ),
    # 3. Solo reintentar Rate Limit errors (no reintentar 400, 401, etc.)
    retry=retry_if_exception_type(RateLimitError),
    # Opcional: Mostrar logs de retries para debuggear
    before_sleep=lambda state: print(
        f"⚠️  Rate Limit alcanzado. Reintentando en {state.next_action.sleep:.2f}s. Intento {state.attempt_number}/5"
    )
)
def llamar_openrouter(prompt: str):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",  # DeepSeek V3
        messages=[{"role": "user", "content": prompt}],
        # Headers RECOMENDADOS por OpenRouter para evitar bloqueos accidentales
        extra_headers={
            "HTTP-Referer": "https://tu-app.com",  # Opcional, pero recomendado
            "X-Title": "Mi App de Prueba"
        }
    )
    # Opcional: Ver tus límites de Rate Limit en tiempo real (devueltos por OpenRouter)
    # print(f"Requests restantes este minuto: {response.usage.x_ratelimit_remaining_requests}")
    return response.choices[0].message.content

# Uso
if __name__ == "__main__":
    try:
        respuesta = llamar_openrouter("Dime un chiste corto sobre programadores")
        print(f"✅ Respuesta: {respuesta}")
    except Exception as e:
        print(f"❌ Error después de todos los retries: {str(e)}")
```

---

### 🧪 Ejemplo SIN LIBRERÍAS (si no quieres instalar `tenacity`)
Si prefieres no usar librerías externas, aquí tienes una versión manual con los mismos principios:
```python
import time
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY"))

def llamar_openrouter_simple(prompt: str, max_retries: int = 5):
    intento = 0
    while intento < max_retries:
        try:
            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError as e:
            intento += 1
            # Extraer header Retry-After de OpenRouter
            retry_after = None
            if e.response:
                retry_after = e.response.headers.get("retry-after") or e.response.headers.get("x-ratelimit-retry-after")
            
            # Calcular tiempo de espera
            if retry_after:
                espera = float(retry_after) + 0.5
            else:
                # Exponential Backoff + Jitter simple: 1s → 2s → 4s...
                espera = (2 ** (intento - 1)) + (0.5 * (intento / max_retries))
            
            print(f"⚠️  Intento {intento}/{max_retries} fallido. Esperando {espera:.2f}s...")
            
            # Si es el último intento, salir del loop
            if intento == max_retries:
                break
            time.sleep(espera)
    
    raise Exception(f"Se agotaron los {max_retries} retries por Rate Limit")

# Uso
if __name__ == "__main__":
    try:
        print(llamar_openrouter_simple("Dime un chiste corto"))
    except Exception as e:
        print(f"Error: {e}")
```

---

### 📌 Notas ESPECÍFICAS para OpenRouter + DeepSeek V3
Con tu uso (5 requests por minuto, $20 de saldo) **nunca deberías tener un 429 sin el loop infinito de retries**, porque:
- DeepSeek V3 tiene un límite por defecto de **300 RPM (requests por minuto)** y **100,000 TPM (tokens por minuto)** para usuarios pagos.
- Puedes ver tus límites en tiempo real en los headers de cualquier respuesta: `x-ratelimit-limit-requests`, `x-ratelimit-remaining-requests`, etc.

Si después de arreglar los retries todavía tienes problemas, revisa:
1. Que no estés compartiendo la API key con otras apps/usuarios (los límites son por key)
2. Que no estés enviando demasiados tokens por request (los límites también son por tokens, no solo requests)
3. Revisa tu panel de OpenRouter para ver tu uso real: https://openrouter.ai/settings/keys