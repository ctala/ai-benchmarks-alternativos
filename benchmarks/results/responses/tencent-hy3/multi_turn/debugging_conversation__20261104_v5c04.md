# Tencent Hy3 — multi_turn/debugging_conversation

- model_id: `tencent/hy3`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 49.384s | tokens_per_second: 51.3
- input_tokens: 374 | output_tokens: 2533

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

Perfecto, ya encontramos la raíz del problema. Lo que te está pasando se conoce como **"Retry Storm" (tormenta de reintentos)**: un bucle infinito que, al recibir un 429, dispara inmediatamente otra petición, la cual vuelve a fallar, generando así un crecimiento exponencial de tráfico (tus 5 reales se vuelven 500 ficticios).

Para arreglarlo correctamente, debes implementar una estrategia de **Reintentos con Backoff Exponencial (Exponential Backoff)**.

### Los 4 pilares de un buen sistema de reintentos:

1. **Límite máximo de intentos**: Nunca reintentes infinitamente. Usa 3 a 5 intentos como máximo.
2. **Espera creciente (Backoff)**: No reintentes al instante. Espera 1s, luego 2s, luego 4s, etc.
3. **Jitter (ruido aleatorio)**: Suma unos milisegundos aleatorios para evitar que muchos procesos fallen y reintenten exactamente a la vez.
4. **Respetar `Retry-After`**: OpenRouter (y la mayoría de APIs) envía una cabecera que te dice exactamente cuántos segundos debes esperar.

---

### Ejemplo de implementación en Python

Aquí tienes un código seguro que puedes usar para reemplazar tu bucle actual:

```python
import time
import random
import requests

def llamar_openrouter(mensaje_usuario):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek/deepseek-v3",
        "messages": [{"role": "user", "content": mensaje_usuario}]
    }
    
    max_intentos = 4  # Pilar 1: Límite de intentos
    
    for intento in range(max_intentos):
        resp = requests.post(url, headers=headers, json=data)
        
        # Si recibimos 429 (Rate Limit)
        if resp.status_code == 429:
            # Pilar 4: Respetar cabecera Retry-After si existe
            retry_after = resp.headers.get('Retry-After')
            
            if retry_after:
                espera = float(retry_after)
            else:
                # Pilar 2 y 3: Backoff exponencial + jitter aleatorio
                espera = (2 ** intento) + random.uniform(0, 1)
            
            print(f"⚠️ 429 recibido. Esperando {espera:.1f}s antes de reintentar...")
            time.sleep(espera)
            continue # Vuelve al inicio del bucle para el siguiente intento
            
        # Pilar extra: No reintentar errores 4xx distintos de 429 (ej. 401 key mala, 400 JSON malo)
        if resp.status_code >= 400 and resp.status_code < 500:
            print("❌ Error de cliente (no reintentable):", resp.text)
            return None
            
        # Si llegamos aquí con 200 o 2xx, éxito
        return resp.json()
        
    print("🛑 Se agotaron los reintentos. Abortando.")
    return None

# Uso:
# resultado = llamar_openrouter("Explícame qué es una API")
```

---

### Recomendaciones adicionales

1. **Mata el proceso actual**: Asegúrate de detener tu script actual que está en bucle para que dejes de mandar tráfico basura (aunque el 429 no te cobra créditos, satura tu conexión y la de ellos).
2. **Usa librerías especializadas**: Si usas Python, te recomiendo la librería **`tenacity`**. Permite hacer esto con solo un decorador:
   ```python
   from tenacity import retry, wait_exponential, stop_after_attempt
   
   @retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(5))
   def mi_funcion_api():
       # tu código requests.post aquí
       # tenacity automáticamente captura excepciones y hace backoff
       pass
   ```
3. **Rate Limiting del lado del cliente**: Como buena práctica de automatización, implementa un "limitador" en tu propio código (ej. usando `time.sleep(0.5)` entre tus 5 llamadas reales) para nunca ni siquiera acercarte al límite de OpenRouter.

¿Quieres que adapte el código a otro lenguaje (JavaScript/Node, PHP) o necesitas ayuda para integrar `tenacity`?