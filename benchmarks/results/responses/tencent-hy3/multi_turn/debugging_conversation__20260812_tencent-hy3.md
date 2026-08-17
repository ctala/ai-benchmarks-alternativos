# Tencent Hy3 — multi_turn/debugging_conversation

- model_id: `tencent/hy3`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 13.487s | tokens_per_second: 97.4
- input_tokens: 374 | output_tokens: 1313

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

Exacto, encontramos la raiz del problema. Tu loop de retry infinito crea una **"tormenta de reintentos"** (retry storm): cada vez que el servidor dice "espera" (429), tu codigo le grita 100 veces mas fuerte, lo que hace que el servidor te bloquee aun mas tiempo.

Para arreglarlo correctamente, necesitas implementar **reintentos con retroceso exponencial (exponential backoff) y limite maximo de intentos**.

### Los 4 principios de un buen retry:
1. **Limite maximo de intentos** (ej: 3 o 5 veces, nunca infinito).
2. **Backoff exponencial**: esperar 1s, luego 2s, luego 4s, luego 8s.
3. **Jitter (aleatoriedad)**: sumar ruido aleatorio para que varios procesos no se sincronicen.
4. **Respetar `Retry-After`**: OpenRouter envia en el header cuantos segundos debes esperar.

---

### Ejemplo en Python (vanilla, sin librerias):

```python
import requests
import time
import random

API_KEY = "tu_api_key"
URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek/deepseek-chat",  # DeepSeek V3
    "messages": [{"role": "user", "content": "Hola"}]
}

max_retries = 5

for intento in range(max_retries):
    response = requests.post(URL, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Exito:", response.json())
        break
    elif response.status_code == 429:
        # 1. Revisar si el server manda 'Retry-After'
        retry_after = response.headers.get('Retry-After')
        
        if retry_after:
            espera = float(retry_after)
        else:
            # 2. Backoff exponencial: 2^intento (1, 2, 4, 8...)
            espera = (2 ** intento) 
        
        # 3. Jitter: sumar hasta 1 segundo de ruido
        espera += random.uniform(0, 1)
        
        print(f"429 recibido. Esperando {espera:.2f}s antes del intento {intento+1}")
        time.sleep(espera)
    else:
        print(f"Error {response.status_code}: {response.text}")
        break
else:
    print("Se agotaron los reintentos. Abortando.")
```

---

### Alternativa pro (usando `tenacity`):
Si usas Python, la libreria `tenacity` hace esto solo:

```bash
pip install tenacity
```

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_status
import requests

@retry(
    stop=stop_after_attempt(5),  # Max 5 intentos
    wait=wait_exponential(multiplier=1, min=1, max=30),  # 1s, 2s, 4s... max 30s
    retry=retry_if_status(429)  # Solo reintenta en 429
)
def llamar_api():
    r = requests.post(URL, headers=headers, json=data)
    r.raise_for_status()
    return r.json()
```

---

### Recomendacion extra (Rate Limiting del lado del cliente):
Aunque el limite es 300 RPM, si tu logica es sensible, agrega un pequeño `time.sleep(0.2)` entre llamadas normales para no llegar nunca al borde.

¿Quieres que veamos como adaptar esto a tu lenguaje específico (JS/Node, Go, etc.)?