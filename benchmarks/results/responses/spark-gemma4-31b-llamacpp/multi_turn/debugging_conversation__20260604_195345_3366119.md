# Gemma 4 31B (Spark llama-server Q4_K_M) — multi_turn/debugging_conversation

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 7.59 | quality: 8.99
- latency_total: 79.074s | tokens_per_second: 9.7
- input_tokens: 344 | output_tokens: 766
- judge_score: 4.6 | justificación: 

## Respuesta completa

Exacto, acabas de crear un **ataque de denegación de servicio (DoS)** contra ti mismo. El servidor te da un 429, tu código entra en pánico y lanza 100 peticiones más, lo que hace que el servidor te bloquee aún más tiempo.

Para arreglar esto, debes implementar una estrategia llamada **Exponential Backoff (Retroceso Exponencial)**.

### ¿Qué es el Exponential Backoff?
En lugar de reintentar inmediatamente, el sistema espera un tiempo que aumenta exponencialmente después de cada fallo.
*   Fallo 1 $\rightarrow$ Espera 1 segundo.
*   Fallo 2 $\rightarrow$ Espera 2 segundos.
*   Fallo 3 $\rightarrow$ Espera 4 segundos... y así sucesivamente.

Aquí tienes la implementación profesional recomendada:

#### Ejemplo en Python (Usando la librería `tenacity`)
Esta es la librería estándar de la industria para manejar retries.

```python
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="TU_API_KEY",
)

# Configuración del Retry
@retry(
    # Solo reintenta si el error es de RateLimit (429) o errores de servidor (5xx)
    retry=retry_if_exception_type(openai.RateLimitError), 
    # Espera exponencial: empieza en 1s, máximo 60s
    wait=wait_exponential(multiplier=1, min=1, max=60), 
    # Detente después de 5 intentos para no quedar en loop infinito
    stop=stop_after_attempt(5) 
)
def call_deepseek():
    return client.chat.completions.create(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Hola"}]
    )

try:
    response = call_deepseek()
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error definitivo después de varios reintentos: {e}")
```

### Reglas de oro para tus retries:

1.  **Límite de Intentos (`stop_after_attempt`):** Nunca pongas un loop infinito. Si después de 5 o 10 intentos sigue fallando, el problema no es el tráfico, es el servidor o tu cuenta, y el código debe detenerse y lanzar un error.
2.  **Jitter (Ruido):** Si tienes muchos procesos corriendo en paralelo, añade un "jitter" (un tiempo aleatorio de milisegundos). Esto evita que todos los procesos reintenten exactamente al mismo segundo y vuelvan a colapsar la API.
3.  **Filtro de Errores:** No reintentes errores `400` (Bad Request) o `401` (Unauthorized). Si la API te dice que tu prompt está mal o que tu key no sirve, reintentar 100 veces no cambiará el resultado.

**Siguiente paso sugerido:** Implementa esto y espera unos 5-10 minutos antes de probar, para que OpenRouter limpie tu IP de la "lista negra" temporal de rate limiting.