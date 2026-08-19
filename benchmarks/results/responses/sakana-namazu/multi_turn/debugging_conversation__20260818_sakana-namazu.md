# Sakana Namazu — multi_turn/debugging_conversation

- model_id: `sakana/sakana-namazu`
- success: True  | final: 6.93 | quality: 7.5
- latency_total: 8.288s | tokens_per_second: 247.1
- input_tokens: 385 | output_tokens: 2048

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

El problema es clásico: **un 429 sin espera genera una cascada de requests que genera más 429s**. Con 3-5 requests por minuto reales, tu retry infinito los convirtió en cientos. 

Aquí tienes cómo implementar retries correctamente (ejemplo en Python, fácil de adaptar a cualquier lenguaje):

### Las 4 reglas de oro para retries

| Regla | Por qué |
|-------|---------|
| **Máximo 3-5 intentos** | Nunca infinito. Si falla después del 4to, algo grave pasa. |
| **Esperar entre intentos** | Si te rechazaron por "too many requests", ¡pedir otra vez inmediatamente empeora todo! |
| **Backoff exponencial + jitter** | Espera 1s, luego 2s, luego 4s, luego 8s... más una fracción aleatoria para no sincronizarte con otros procesos. |
| **Distinguir errores** | Solo reintentar: `429`, `408`, `500`, `502`, `503`, `504`. **Nunca** reintentar: `400`, `401`, `403`, `422`. |

---

### Opción 1: Código limpio (sin librerías externas)

```python
import time
import random
import requests

def call_openrouter(payload, max_retries=4):
    API_KEY = "tu-key"
    base_delay = 2.0  # segundos base
    
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://tusitio.com",  # OpenRouter lo pide
                    "X-Title": "Tu App"
                },
                json=payload,
                timeout=60  # IMPORTANTE: evita requests colgados
            )

            if resp.status_code == 200:
                return resp.json()

            # Errores de cliente que NO deben reintentarse
            if resp.status_code in (400, 401, 403, 