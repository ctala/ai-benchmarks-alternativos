# Claude Opus 5.5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 21.787s | tokens_per_second: 110.8
- input_tokens: 541 | output_tokens: 2414

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

Encontraste la causa. Un retry infinito sin espera convierte cada 429 en una avalancha de requests, lo que genera más 429 y te mantiene bloqueado.

## Principios de un retry bien hecho

1. **Límite de intentos**: nunca infinito; entre 3 y 5 suele bastar.
2. **Backoff exponencial**: esperar 1s, 2s, 4s, 8s... entre intentos.
3. **Jitter (aleatoriedad)**: evita que varios procesos reintenten al mismo tiempo.
4. **Respetar `Retry-After`**: si el servidor indica cuánto esperar, haz caso.
5. **Reintentar solo errores transitorios**:
   - Sí: `429`, `500`, `502`, `503`, `504`, timeouts y errores de conexión.
   - No: `400` (request mal formado), `401` (key inválida), `402` (sin créditos). Reintentarlos nunca va a funcionar.

## Implementación en Python

```python
import time
import random
import requests

URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": "Bearer TU_API_KEY",
    "Content-Type": "application/json",
}
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def calcular_espera(intento, base=1.0, maximo=60.0, retry_after=None):
    if retry_after:
        try:
            return min(float(retry_after), maximo)
        except ValueError:
            pass
    # Exponencial con "full jitter": aleatorio entre 0 y base * 2^intento
    return random.uniform(0, min(maximo, base * (2 ** intento)))

def llamar_openrouter(payload, max_reintentos=5):
    for intento in range(max_reintentos + 1):
        try:
            resp = requests.post(URL, headers=HEADERS, json=payload, timeout=60)
        except (requests.Timeout, requests.ConnectionError):
            if intento == max_reintentos:
                raise
            espera = calcular_espera(intento)
            print(f"Error de conexión, reintento {intento + 1} en {espera:.1f}s")
            time.sleep(espera)
            continue

        if resp.ok:
            return resp.json()

        # Error no recuperable o último intento: fallar de inmediato
        if resp.status_code not in RETRYABLE_STATUS or intento == max_reintentos:
            print(f"Error {resp.status_code}: {resp.text}")
            resp.raise_for_status()

        espera = calcular_espera(intento, retry_after=resp.headers.get("Retry-After"))
        print(f"HTTP {resp.status_code}, reintento {intento + 1} en {espera:.1f}s")
        time.sleep(espera)

# Uso
resultado = llamar_openrouter({
    "model": "deepseek/deepseek-chat",
    "messages": [{"role": "user", "content": "Hola"}],
})
```

## Alternativas más simples

**Si usas el SDK de OpenAI** apuntando a OpenRouter, ya trae retries con backoff incluidos:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY",
    max_retries=5,  # backoff automático
    timeout=60,
)
```

**Con la librería `tenacity`**:

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential

@retry(stop=stop_after_attempt(5), wait=wait_random_exponential(min=1, max=60))
def llamar(payload):
    ...
```

## Dos aclaraciones importantes

**1. Una corrección sobre lo que te dije antes.** Afirmé que el límite era de 300 RPM, y no debí darlo como dato fijo. Los límites de OpenRouter cambian según el tipo de cuenta y su política vigente, así que conviene revisar su documentación. Además, con DeepSeek muchos 429 no vienen de OpenRouter, sino del **proveedor upstream** cuando está saturado. Puedes distinguirlo leyendo el cuerpo del error. Si es del proveedor, ayuda configurar modelos de respaldo con el campo `models`, para que OpenRouter cambie a otro si el primero falla.

**2. Después de arreglar el código**, espera unos minutos antes de probar. Es posible que sigas temporalmente limitado por la ráfaga de requests anterior.

¿Usas `requests`, el SDK de OpenAI u otra librería? Si me muestras tu loop actual, te ayudo a adaptarlo.