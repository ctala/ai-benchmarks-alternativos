# Seed 2.0 Code — multi_turn/debugging_conversation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 84.193s | tokens_per_second: 59.8
- input_tokens: 389 | output_tokens: 5031

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

¡Genial que encontraste la causa raíz! El problema es que tus reintentos no tienen control: un solo error 429 se convierte en una tormenta de requests que agotan tus límites de OpenRouter.

Para arreglarlo, debes implementar **reintentos inteligentes con estos 5 principios clave** (nunca más loops infinitos):
1. Límite máximo de reintentos (máx 3-5, nunca infinito)
2. **Exponential Backoff**: Espera creciente entre reintentos (1s → 2s → 4s → ...)
3. **Jitter**: Aleatoriedad en la espera para evitar "tormentas de reintentos" entre múltiples clientes
4. Respetar el header `Retry-After` (si OpenRouter te dice cuánto esperar, usa ese valor)
5. **Solo reintentar errores transitorios**: 429 (rate limit) y 5xx (errores del servidor) → NO reintentar 400/401/403 (son errores tuyos, no se solucionan con reintentos)

---

### Ejemplo práctico (Python, recomendado)
Usamos la librería `tenacity` (estándar para reintentos) + el cliente de OpenAI (compatible con OpenRouter, ya que OpenRouter imita la API de OpenAI):

#### Paso 1: Instalar dependencias
```bash
pip install tenacity openai
```

#### Paso 2: Código con reintentos seguros
```python
import openai
from tenacity import (
    retry,
    stop_after_attempt,  # Límite de reintentos (NO INFINITO)
    wait_exponential_jitter,  # Backoff + jitter (evita tormentas)
    retry_if_exception_type,  # Solo reintentar errores válidos
    before_sleep_log,  # Loguear qué pasa en cada retry
)
import logging

# Configurar logging para ver reintentos
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Configurar cliente de OpenAI para OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY_DE_OPENROUTER",
)

# --------------------------
# Definir errores TRANSITORIOS (se solucionan con reintentos)
# OpenRouter usa errores compatibles con OpenAI:
# - RateLimitError: 429
# - InternalServerError/APIError: 500, 502, 503, etc.
# --------------------------
ERRORES_TRANSITORIOS = (
    openai.RateLimitError,
    openai.InternalServerError,
    openai.APIError,
)

# --------------------------
# Decorador de reintentos INTELIGENTES
# --------------------------
@retry(
    stop=stop_after_attempt(5),  # Máx 5 reintentos (ajusta según tu necesidad)
    wait=wait_exponential_jitter(
        multiplier=1,  # Tiempo base: 1s → 2s → 4s → ...
        max=10  # Tiempo máximo de espera entre reintentos: 10s
    ),
    retry=retry_if_exception_type(ERRORES_TRANSITORIOS),  # Solo reintentar estos
    before_sleep=before_sleep_log(logger, logging.WARNING),  # Loguear cada retry
)
def hacer_request_openrouter(prompt: str):
    """Hace una request segura a DeepSeek V3 en OpenRouter"""
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat",  # DeepSeek V3 en OpenRouter
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        # Requerido por OpenRouter para estadísticas (opcional pero recomendado)
        extra_headers={"HTTP-Referer": "https://tu-app.com", "X-Title": "Tu App"}
    )
    return response.choices[0].message.content

# --------------------------
# Uso SEGURO
# --------------------------
if __name__ == "__main__":
    try:
        respuesta = hacer_request_openrouter("¿Qué es Python?")
        print(f"Respuesta: {respuesta}")
    except ERRORES_TRANSITORIOS as e:
        # Si después de 5 reintentos sigue fallando: manejar error
        logger.error(f"Error transitorio después de reintentos: {e}")
    except Exception as e:
        # Otros errores (400, 401, 403) NO reintentables:
        # - 400: Prompt muy largo, parámetros inválidos
        # - 401: API key incorrecta
        # - 403: Sin permisos para el modelo
        logger.error(f"Error NO reintentable: {e}")
```

---

### Tip extra: Evita el 429 en primer lugar
OpenRouter devuelve **headers de rate limit** en cada respuesta. Puedes monitorearlos para esperar antes de llegar al límite:
```python
# Modifica la función hacer_request_openrouter para extraer headers:
def hacer_request_openrouter(prompt: str):
    response = client.chat.completions.create(...)
    
    # Extraer límites de rate (cliente OpenAI v1+ usa response.response.headers)
    remaining = int(response.response.headers.get("x-ratelimit-remaining", 0))
    reset_timestamp = int(response.response.headers.get("x-ratelimit-reset", 0))  # Unix timestamp

    # Si quedan menos de 5 requests, esperar hasta que se resetee el límite
    if remaining < 5:
        import time
        tiempo_espera = reset_timestamp - int(time.time())
        if tiempo_espera > 0:
            logger.warning(f"Quedan pocas requests: esperando {tiempo_espera}s...")
            time.sleep(tiempo_espera)
    
    return response.choices[0].message.content
```

---

### Lo que NUNCA debes hacer (lo que tenías antes):
❌ Reintentos infinitos  
❌ Reintentar inmediatamente sin espera  
❌ Reintentar errores no transitorios (400, 401, 403)  
❌ No respetar headers del servidor (`Retry-After`, rate limits)

Con esto, tus reintentos no causarán más 429, y solucionarás errores transitorios de forma segura. Si sigues teniendo problemas, revisa los headers `x-ratelimit-*` de OpenRouter para ver si tu modelo tiene un límite más bajo de lo que crees (DeepSeek V3 para usuarios pagos es **300 RPM**, así que 5 req/min es totalmente seguro sin reintentos descontrolados).