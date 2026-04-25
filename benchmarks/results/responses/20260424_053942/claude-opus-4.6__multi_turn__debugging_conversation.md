# Claude Opus 4.6 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.36 | quality: 8.74
- latency_total: 16.111s | tokens_per_second: 58.0
- input_tokens: 394 | output_tokens: 935
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Ahí está el problema! Tu retry infinito está creando una **avalancha de requests** que empeora el 429 en cada ciclo. Vamos a arreglarlo correctamente:

## La solución: Exponential Backoff con límites

```python
import time
import requests

def call_openrouter(prompt, max_retries=5):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer tu-api-key",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    for attempt in range(max_retries):
        response = requests.post(url, headers=headers, json=payload)

        # --- Éxito ---
        if response.status_code == 200:
            return response.json()

        # --- Rate limit (429) ---
        if response.status_code == 429:
            # 1. Respetar el header Retry-After si existe
            wait = response.headers.get("Retry-After")

            if wait:
                wait = int(wait)
            else:
                # 2. Exponential backoff: 1s, 2s, 4s, 8s, 16s
                wait = 2 ** attempt

            print(f"⚠️  429 recibido. Intento {attempt + 1}/{max_retries}. "
                  f"Esperando {wait}s...")
            time.sleep(wait)
            continue

        # --- Otros errores (500, 503, etc.) ---
        if response.status_code >= 500:
            wait = 2 ** attempt
            print(f"⚠️  Error {response.status_code}. Reintentando en {wait}s...")
            time.sleep(wait)
            continue

        # --- Errores del cliente (400, 401, 403) - NO reintentar ---
        print(f"❌ Error {response.status_code}: {response.text}")
        return None

    print(f"❌ Falló después de {max_retries} intentos.")
    return None
```

## ¿Por qué funciona?

```
Tu código actual (retry infinito):
  429 → retry → 429 → retry → 429 → retry → 429...  💀
  (100+ requests en segundos)

Con exponential backoff:
  429 → espera 1s → 429 → espera 2s → 429 → espera 4s → ✅
  (3 requests en 7 segundos)
```

## Las 3 reglas clave del retry

| Regla | Por qué |
|---|---|
| **Límite de reintentos** (`max_retries=5`) | Evita loops infinitos |
| **Backoff exponencial** (`2 ** attempt`) | Cada espera es más larga, le da tiempo al servidor |
| **Respetar `Retry-After`** | El servidor te dice exactamente cuánto esperar |

## Paso inmediato

Busca en tu código el retry actual y reemplázalo. Probablemente se ve algo así:

```python
# ❌ TU CÓDIGO ACTUAL - ELIMINAR ESTO
while True:
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    # Sin espera, sin límite = avalancha
```

¿Puedes mostrarme tu loop actual para confirmar que lo reemplazamos correctamente?