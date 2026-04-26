# Qwen 3.5 (Ollama Cloud default) — multi_turn/debugging_conversation

- model_id: `qwen3.5:cloud`
- success: True  | final: 7.84 | quality: 8.82
- latency_total: 10.923s | tokens_per_second: 90.4
- input_tokens: 340 | output_tokens: 988
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Excelente diagnóstico! Ese es exactamente el problema. Un retry infinito sin control convierte un error temporal en un bloqueo permanente y puede agotar tus créditos rápidamente.

Para manejar errores 429 correctamente, debes implementar un **Backoff Exponencial con Jitter**. Esto significa esperar cada vez más tiempo entre intentos y añadir un poco de aleatoriedad para evitar colisiones.

Aquí tienes la implementación correcta paso a paso:

### 1. Lógica de Reintentos (Python)

Esta función maneja la espera, respeta el tiempo que te indica el servidor (`Retry-After`) y limita los intentos.

```python
import time
import random
import requests

def hacer_request_con_retry(url, headers, data, max_retries=5):
    base_delay = 1  # Segundos iniciales de espera
    
    for intento in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code == 200:
                return response.json()
            
            elif response.status_code == 429:
                # 1. Obtener tiempo de espera del servidor (si existe)
                retry_after = response.headers.get('Retry-After')
                
                if retry_after:
                    delay = int(retry_after)
                    print(f"⏳ 429 detectado. Esperando {delay}s (indicado por servidor)...")
                else:
                    # 2. Backoff exponencial con Jitter
                    delay = (base_delay * (2 ** intento)) + random.uniform(0, 1)
                    print(f"⏳ 429 detectado. Esperando {delay:.2f}s (backoff)...")
                
                time.sleep(delay)
                continue  # Reintentar
            
            else:
                # Errores que NO son 429 no se reintentan
                print(f"❌ Error {response.status_code}: {response.text}")
                response.raise_for_status()
                
        except Exception as e:
            print(f"❌ Excepción: {e}")
            if intento == max_retries - 1:
                raise
            
    raise Exception(f"❌ Máximo de {max_retries} reintentos alcanzado")
```

### 2. Reglas de Oro para tus Retries

| Regla | Por qué |
|-------|---------|
| **Máximo 3-5 retries** | Si después de 5 intentos falla, el problema no es temporal |
| **Backoff exponencial** | 1s → 2s → 4s → 8s → 16s (da tiempo al servidor de recuperarse) |
| **Añadir Jitter** | Suma un valor aleatorio (0-1s) para evitar que muchos clientes reintenten exactamente al mismo tiempo |
| **Leer `Retry-After`** | Si OpenRouter te dice exactamente cuánto esperar, obedece ese valor primero |
| **Solo retry en 429/503** | Nunca reintentar errores 400, 401, 403 (son errores de configuración) |

### 3. Verificación de Seguridad

Antes de volver a ejecutar tu script:

1. **Espera 5-10 minutos** para que el rate limit de tu API key se resetee completamente.
2. **Desactiva el script antiguo** que tiene el loop infinito.
3. **Revisa tu dashboard de OpenRouter** para confirmar que no has gastado créditos inesperadamente durante el bucle.

### 4. ¿Usas alguna librería?

Si no quieres implementar la lógica manual, estas librerías ya lo hacen por ti:

*   **Python:** `tenacity` o `backoff`
*   **Node.js:** `axios-retry` o `p-retry`
*   **OpenAI SDK:** Ya incluye retries automáticos (si usas el SDK oficial compatible)

¿Necesitas que adapte el ejemplo a otro lenguaje o librería específica?