# Ministral 14B — multi_turn/debugging_conversation

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 19.947s | tokens_per_second: 64.1
- input_tokens: 325 | output_tokens: 1278

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

¡Perfecto que hayas identificado el problema! El **retry infinito** es común en APIs con rate limits, pero se puede implementar correctamente con estas reglas:

---

### **Solución recomendada para retries con OpenRouter (y APIs en general)**
1. **Usa un exponencial backoff** (esperar cada vez más tiempo entre retries).
2. **Respetar los headers de rate limit** (`Retry-After` o `x-ratelimit-*`).
3. **Limitar el número máximo de retries** (ej: 3-5 intentos).
4. **No hacer retries en errores definitivos** (ej: 401, 404, 500 sin retry).

---

### **Ejemplo en Python (con `requests` y `tenacity`)**
```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    RetryError,
) from requests.exceptions import RequestException

# Configuración del retry
@retry(
    stop=stop_after_attempt(5),  # Máximo 5 retries
    wait=wait_exponential(multiplier=1, min=2, max=10),  # Espera 2s, 4s, 8s, etc.
    retry=retry_if_exception_type(RequestException),  # Retry solo en errores de red/API
    reraise=True,  # Re-lanza la última excepción si falla todo
)
def call_openrouter_api(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        json={"model": "deepseek-v3", "messages": [{"role": "user", "content": prompt}]},
        headers=headers,
    )
    response.raise_for_status()  # Lanza error si HTTP != 200
    return response.json()

# Ejemplo de uso
try:
    result = call_openrouter_api("Hola, ¿cómo estás?")
    print(result)
except RetryError as e:
    print(f"Fallo después de {e.last_attempt.attempt_number} intentos. Último error: {str(e.last_attempt.exception())}")
```

---

### **Claves para tu caso específico (DeepSeek/OpenRouter)**
1. **Revisa los headers de respuesta**:
   - Si el servidor devuelve `Retry-After: 10`, espera **exactamente 10 segundos** (no uses backoff exponencial en este caso).
   - Ejemplo:
     ```python
     if response.status_code == 429:
         retry_after = int(response.headers.get("Retry-After", 5))  # Default: 5s
         time.sleep(retry_after)
         return call_openrouter_api(prompt)  # Retry manual
     ```

2. **Evita retries en errores 429 con `Retry-After`**:
   Si el servidor ya te dice cuándo puedes retry, **no uses backoff exponencial** (puede ser contraproducente).

3. **Monitoriza tus requests**:
   Usa herramientas como [Postman](https://www.postman.com/) o [curl](https://curl.se/) para probar manualmente y ver los headers de rate limit.

---

### **Alternativa sin librerías (solo `requests`)**
```python
import time
import requests

def call_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                json={"model": "deepseek-v3", "messages": [{"role": "user", "content": prompt}]},
                headers={"Authorization": f"Bearer {API_KEY}"},
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 2 ** attempt))  # Espera 1s, 2s, 4s...
                print(f"Rate limit. Retrying en {retry_after}s (intento {attempt + 1}/{max_retries})...")
                time.sleep(retry_after)
            else:
                raise  # Error no retryable (ej: 401, 500)
    raise Exception("Máximo retries alcanzado")

# Uso
result = call_with_retry("¿Cómo está el clima?")
```

---

### **Recomendaciones adicionales**
1. **Ajusta el `max_retries`**:
   - Para APIs con rate limits, **3-5 retries suelen ser suficientes**.
   - Si usas backoff exponencial, el tiempo total de espera puede ser largo (ej: 2s + 4s + 8s = 14s).

2. **Límites de OpenRouter**:
   - DeepSeek V3 tiene un **rate limit de 300 RPM por clave** (verifica en [su documentación](https://openrouter.ai/docs)).
   - Si pagaste créditos, asegúrate de que la clave esté asociada a un plan con límites adecuados.

3. **Logging**:
   Añade logs para depurar:
   ```python
   print(f"Intentando request {attempt + 1}/{max_retries}. Status: {response.status_code}")
   ```

---
### **¿Qué hacer si sigue fallando?**
- **Contacta a soporte de OpenRouter**: A veces hay límites ocultos o problemas temporales en el servidor.
- **Reducir la frecuencia**: Prueba con 2-3 requests/minuto para ver si el problema persiste.
- **Usar una clave nueva**: Si la clave antigua tiene un histórico de errores, crea una nueva.