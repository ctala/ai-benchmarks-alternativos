# Gemma 4 26B MoE (3.8B activos) — multi_turn/debugging_conversation

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.34 | quality: 7.5
- latency_total: 15.754s | tokens_per_second: 64.0
- input_tokens: 345 | output_tokens: 1009

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

¡Bingo! Has encontrado el clásico **"Retry Storm"** (Tormenta de reintentos). Lo que está pasando es que tu código entra en un bucle de retroalimentación positiva: el error causa un reintento, el reintento causa más errores, y eso genera una avalancha de peticiones que bloquea tu cuenta.

Para arreglarlo como un experto, no puedes simplemente hacer un `while True`. Necesitas implementar una estrategia de **Exponential Backoff con Jitter**.

Aquí tienes los 3 pilares para solucionar esto:

### 1. Exponential Backoff (Retroceso Exponencial)
En lugar de reintentar inmediatamente, debes esperar un tiempo que crezca exponencialmente con cada fallo. 
*   Fallo 1: Espera 1s
*   Fallo 2: Espera 2s
*   Fallo 3: Espera 4s
*   Fallo 4: Espera 8s...

### 2. Jitter (Ruido aleatorio)
Si tienes varios procesos corriendo, y todos usan exactamente el mismo tiempo de espera, todos volverán a atacar la API al mismo milisegundo exacto. El **Jitter** añade un pequeño componente aleatorio (ej. entre 0.5s y 1.5s) para "desincronizar" las peticiones.

### 3. Max Retries (Límite de intentos)
**Nunca** permitas un reintento infinito. Debes establecer un límite (ej. 5 intentos) y, si después de eso sigue fallando, lanzar una excepción o registrar el error para que un humano lo vea.

---

### Implementación sugerida (Python)

Si estás usando Python, la librería `tenacity` es el estándar de la industria para esto. Es limpia y robusta.

```python
import time
import random
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Simulamos una excepción de error de API
class RateLimitError(Exception):
    pass

# Configuración profesional de reintentos:
# 1. stop_after_attempt(5): Deja de intentar tras 5 fallos.
# 2. wait_exponential(multiplier=1, min=2, max=10): 
#    Espera 2s, luego 4s, 8s... hasta un máximo de 10s.
# 3. retry_if_exception_type: Solo reintenta si es un error de Rate Limit (429), 
#    no si es un error de código (401 o 404).

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(RateLimitError),
    reraise=True
)
def call_openrouter_api(prompt):
    print(f"Intentando llamada a la API... {time.strftime('%X')}")
    
    # --- SIMULACIÓN DE TU LÓGICA ---
    # Aquí iría tu petición con requests o openai client
    # Si recibes un status_code == 429:
    #    raise RateLimitError("Exceso de peticiones")
    # -------------------------------
    
    # Simulando que falla por ahora para que veas el comportamiento
    raise RateLimitError("Error 429 detectado")

# Ejecución
try:
    call_openrouter_api("Hola DeepSeek")
except Exception as e:
    print(f"❌ Falló definitivamente después de varios intentos: {e}")
```

### Checklist de depuración final:
1.  **Filtra los errores:** Asegúrate de que tu código **SOLO** haga retry si el error es `429` (Rate Limit) o `5xx` (Error de servidor). Si el error es `401` (API Key inválida) o `400` (Bad Request), el retry no servirá de nada y solo gastarás recursos.
2.  **Logs:** Agrega un `print` o un log que diga: *"Error 429 recibido. Reintentando en X segundos..."*. Esto te dará visibilidad de qué está pasando en tiempo real.
3.  **Límite de intentos:** Pon un `max_retries` estricto. Es mejor que la aplicación falle y te avise, a que se quede en un bucle infinito consumiendo tu saldo o bloqueando tu IP.