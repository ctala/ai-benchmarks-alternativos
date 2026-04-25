# Gemini 2.5 Pro — multi_turn/debugging_conversation

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 7.34 | quality: 9.27
- latency_total: 18.892s | tokens_per_second: 107.7
- input_tokens: 312 | output_tokens: 2035
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Excelente! Has encontrado la causa raíz del problema. Ese es el paso más importante. Un bucle de reintentos sin control es una causa muy común de "avalanchas" de requests que provocan bloqueos por rate limit.

Lo que estás describiendo se conoce como una "tormenta de reintentos" (retry storm). La solución estándar y recomendada para esto es implementar un **"Exponential Backoff con Jitter"**.

Suena complicado, pero la idea es simple:

1.  **Exponential Backoff (Espera Exponencial):** En lugar de reintentar inmediatamente, esperas un poco. Si vuelve a fallar, duplicas el tiempo de espera antes del siguiente intento. (Ej: 1s, 2s, 4s, 8s...). Esto le da al servidor tiempo para recuperarse.
2.  **Jitter (Aleatoriedad):** Si muchos clientes empiezan a reintentar al mismo tiempo con la misma espera exponencial, podrían volver a hacer las peticiones todos a la vez. Para evitarlo, se añade un pequeño tiempo aleatorio (jitter) a cada espera.

---

### Cómo implementarlo: Paso a Paso

Aquí tienes una estrategia completa y un ejemplo en Python (el concepto es aplicable a cualquier lenguaje).

#### Lógica del Proceso

1.  **Define un número máximo de reintentos:** Nunca reintentes infinitamente. 3 a 5 reintentos suele ser un buen punto de partida.
2.  **Define una espera inicial:** Por ejemplo, 1 segundo.
3.  **Crea un bucle:** Que se ejecute hasta el número máximo de reintentos.
4.  **Dentro del bucle:**
    *   Haz la llamada a la API dentro de un bloque `try/except`.
    *   **Si la llamada tiene éxito (código 200):** ¡Perfecto! Sal del bucle y devuelve el resultado.
    *   **Si la llamada falla con un error 429 (u otro error transitorio como 500, 503):**
        *   Calcula el tiempo de espera: `espera_actual = espera_inicial * (2 ** numero_de_intento) + random.uniform(0, 1)`
        *   Espera esa cantidad de tiempo (ej. `time.sleep(espera_actual)`).
        *   Incrementa el contador de intentos y continúa con la siguiente iteración del bucle.
    *   **Si la llamada falla con otro error (como 400 o 401):** No reintentes. Es un error permanente en tu petición. Lanza una excepción y detén el proceso.
5.  **Si el bucle termina sin éxito:** Lanza una excepción final indicando que la llamada falló después de todos los reintentos.

---

### Ejemplo Práctico en Python (Implementación Manual)

Este es un ejemplo de cómo se vería la lógica en una función.

```python
import openai
import time
import random
import os

# Configura tu cliente de OpenRouter
# Es mejor crear el cliente UNA VEZ y reutilizarlo
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def realizar_llamada_con_reintentos(prompt, max_retries=5, initial_wait=1):
    """
    Realiza una llamada a la API de OpenRouter con una estrategia
    de exponential backoff con jitter.
    """
    wait_time = initial_wait
    for attempt in range(max_retries):
        try:
            print(f"Intento #{attempt + 1}...")
            completion = client.chat.completions.create(
                model="deepseek/