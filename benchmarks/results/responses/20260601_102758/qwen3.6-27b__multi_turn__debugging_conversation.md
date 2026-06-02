# Qwen 3.6 27B base (OpenRouter FP8) — multi_turn/debugging_conversation

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.39 | quality: 9.1
- latency_total: 27.344s | tokens_per_second: 74.9
- input_tokens: 340 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando directamente el problema de los errores 429 con estrategias de reintento bien fundamentadas.

## Respuesta completa

Perfecto, ya tenemos el diagnóstico: **un retry infinito convierte un 429 momentáneo en un ataque de denegación de servicio contra ti mismo**. Vamos a arreglarlo con una implementación robusta.

### 🔑 Reglas de oro para retries en OpenRouter (y cualquier API moderna)
1. **Máximo de intentos**: 3 a 5 como tope. Nunca infinito.
2. **Backoff exponencial**: `delay = base * 2^attempt`
3. **Jitter aleatorio**: Suma `0-1s` aleatorio para evitar el "thundering herd".
4. **Respeta `Retry-After`**: Si el header existe, úsalo. Es la fuente de verdad del servidor.
5. **Solo retry en errores transitorios**: `429`, `5xx`, timeouts. **NUNCA** en `400`, `401`, `403`, `422` (errores de tu código/llave).

---

### 🐍 Ejemplo Python (requests)
```python
import time
import random
import requests

def call_openrouter(url, headers, payload, max_retries=3, base_delay=1.0):
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            
            # ✅ 42