# Ling 3.0 Flash — multi_turn/debugging_conversation

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.898s | tokens_per_second: 352.8
- input_tokens: 396 | output_tokens: 1375
- judge_score: 5.0 | justificación: 

## Respuesta completa

Perfecto, ya encontraste la causa raíz. Un retry infinito sin espera es la receta para un desastre. Aquí te explico cómo implementar retries correctamente:

---

## Principios clave para un retry inteligente

1. **Exponential Backoff** - Esperar cada vez más entre reintentos (1s → 2s → 4s → 8s...)
2. **Jitter** - Agregar aleatoriedad para evitar que todos los clientes retry al mismo tiempo
3. **Max retries** - Un tope duro para no bucle infinito
4. **Leer `Retry-After`** - Si el servidor te dice "espera X segundos", obedecer
5. **Solo retry en errores transitorios** - 429 y 5xx, NUNCA 400, 401, 404

---

## Ejemplo en Python (con `requests`)

```python
import time
import random
import requests

def call_with_retry(url, headers, payload, max_retries=5):
    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()

        # No reintentar errores de cliente (4xx excepto 429)
        if response.status_code in (400, 401, 403, 404):
            raise Exception(f"Error no reintentable: {response.status_code} - {response.text}")

        # Si es 429, respetar Retry-After si existe
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 0))
            if retry_after == 0:
                # Backoff exponencial + jitter
                base_wait = (2 ** attempt)  # 1, 2, 4, 8, 16...
                jitter = random.uniform(0, base_wait * 0.5)
                wait_time = base_wait + jitter
            else:
                wait_time = retry_after

            print(f"Rate limit (429). Esperando {wait_time:.1f}s... (intento {attempt+1}/{max_retries})")
            time.sleep(wait_time)
            continue

        # 5xx: error del servidor, reintentar con backoff
        if response.status_code >= 500:
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"Error {response.status_code}. Reintentando en {wait_time:.1f}s...")
            time.sleep(wait_time)
            continue

        raise Exception(f"Error inesperado: {response.status_code}")

    raise Exception("Máximo de reintentos alcanzado")
```

---

## Si usas la librería de OpenAI (compatible con OpenRouter)

La librería oficial ya tiene retry integrado. Solo configúrala:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="tu-api-key",
    max_retries=3,  # ← ya incluye backoff exponencial + jitter automáticamente
)
```

Esto es lo más simple y confiable si usas esta librería.

---

## Si usas otro lenguaje o framework

La misma lógica aplica siempre:
- **JavaScript** → usa `backoff` npm package o `p-retry`
- **Node.js** → `retry` o el built-in `fetch` con lógica manual
- **Curl/bash** → un `while` loop con `sleep` creciente

---

## Resumen de lo que debes cambiar en tu código

| ❌ Lo que tienes ahora | ✅ Lo que deberías tener |
|---|---|
| Retry infinito | `max_retries=3` a `5` |
| Sin espera entre retries | Exponential backoff (2^attempt) |
| Sin jitter | `+ random.uniform(0, base_wait * 0.5)` |
| Ignora `Retry-After` | Lee y respeta ese header |
| Retry en TODOS los errores | Solo en 429 y 5xx |

Con eso deberías resolver el loop y los 429 dejan de ser un problema. Si después de esto sigues teniendo 429, el problema es de capacidad real y ahí ajustamos el rate de requests.