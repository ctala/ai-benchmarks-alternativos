# MiMo-V2.5 Pro — multi_turn/debugging_conversation

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.35 | quality: 8.71
- latency_total: 18.823s | tokens_per_second: 75.6
- input_tokens: 357 | output_tokens: 1423
- judge_score: 4.4 | justificación: 

## Respuesta completa

¡Ahí está el problema! Un retry infinito es una receta para el desastre. Aquí tienes la implementación correcta:

## Retry con Backoff Exponencial (Python)

```python
import time
import random
import requests
from typing import Optional

def make_api_call_with_retry(
    url: str,
    headers: dict,
    payload: dict,
    max_retries: int = 3,
    base_delay: float = 1.0
) -> Optional[dict]:
    """
    Implementa retry con backoff exponencial y jitter
    """
    
    for attempt in range(max_retries + 1):  # 0, 1, 2, 3 (4 intentos total)
        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            # Si es exitoso, retorna la respuesta
            if response.status_code == 200:
                return response.json()
            
            # Si es 429, espera según headers o backoff exponencial
            elif response.status_code == 429:
                print(f"Rate limited en intento {attempt + 1}/{max_retries + 1}")
                
                # 1. Primero revisa si hay header Retry-After
                retry_after = response.headers.get('Retry-After')
                
                if retry_after:
                    wait_time = float(retry_after) + 0.5  # Añade un buffer
                    print(f"Esperando {wait_time}s (según header Retry-After)")
                else:
                    # 2. Si no hay header, usa backoff exponencial con jitter
                    wait_time = (base_delay * (2 ** attempt)) + random.uniform(0, 1)
                    print(f"Esperando {wait_time:.2f}s (backoff exponencial)")
                
                # Si es el último intento, no esperes
                if attempt < max_retries:
                    time.sleep(wait_time)
                    continue
            
            # Para otros errores (4xx, 5xx), no reintentar
            else:
                print(f"Error {response.status_code} no reintentable")
                response.raise_for_status()
                
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión en intento {attempt + 1}: {e}")
            if attempt < max_retries:
                wait_time = base_delay * (2 ** attempt)
                time.sleep(wait_time)
            else:
                raise
    
    # Si llegamos aquí, todos los reintentos fallaron
    print(f"Todos los {max_retries + 1} intentos fallaron")
    return None

# Uso
result = make_api_call_with_retry(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer TU_API_KEY",
        "Content-Type": "application/json"
    },
    payload={
        "model": "deepseek/deepseek-chat-v3-0324",
        "messages": [{"role": "user", "content": "Hola"}]
    },
    max_retries=3,
    base_delay=2.0
)
```

## Alternativa con biblioteca `tenacity` (más elegante)

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    stop=stop_after_attempt(4),  # 4 intentos total
    wait=wait_exponential(multiplier=1, min=4, max=60),  # 4s, 8s, 16s, 32s
    retry=retry_if_exception_type((requests.exceptions.HTTPError, 
                                   requests.exceptions.ConnectionError))
)
def call_api(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    
    # Manejar 429 específicamente
    if response.status_code == 429:
        # Podrías lanzar una excepción personalizada
        raise requests.exceptions.HTTPError(response=response)
    
    response.raise_for_status()
    return response.json()
```

## Reglas importantes para retries:

1. **Máximo 3-5 reintentos** - No más
2. **Backoff exponencial**: 1s → 2s → 4s → 8s...
3. **Jitter**: Añade aleatoriedad para evitar "thundering herd"
4. **Respetar `Retry-After`**: Si el servidor lo envía, úsalo
5. **No reintentar errores 4xx** (excepto 429)
6. **Timeout en cada request**: Nunca más de 30 segundos

## Para OpenRouter específicamente:

OpenRouter envía headers útiles en 429:
```python
# Después de un 429, revisa estos headers:
print(response.headers.get('X-RateLimit-Limit'))      # Límite actual
print(response.headers.get('X-RateLimit-Remaining'))   # Requests restantes
print(response.headers.get('X-RateLimit-Reset'))       # Tiempo hasta reset
print(response.headers.get('Retry-After'))             # Segundos a esperar
```

¿En qué lenguaje estás trabajando? Te puedo dar ejemplos más específicos.