# Kimi K2 Thinking (NIM) — multi_turn/debugging_conversation

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 6.79 | quality: 8.54
- latency_total: 66.879s | tokens_per_second: 29.7
- input_tokens: 390 | output_tokens: 1986
- judge_score: 4.6 | justificación: 

## Respuesta completa

 ¡Excelente diagnóstico! El retry infinito es un error común que convierte un pequeño problema en un desastre. Aquí te muestro la forma correcta de implementar retries con backoff exponencial y respeto a los límites de OpenRouter.

## Solución Básica (Backoff Exponencial)

```python
import time
import random
import openai

def call_openrouter_with_retry(client, **kwargs):
    """Implementa backoff exponencial con jitter"""
    max_retries = 5
    base_delay = 1  # segundo inicial
    
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
            
        except openai.RateLimitError as e:
            if attempt == max_retries - 1:
                raise  # Re-lanzar si agotamos los intentos
            
            # Calcular delay con backoff exponencial + jitter
            delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), 60)
            
            print(f"⚠️ Rate limit alcanzado (intento {attempt + 1}/{max_retries}). "
                  f"Esperando {delay:.2f}s...")
            time.sleep(delay)
            
        except openai.APIError as e:
            # Solo retry en errores 5xx o 429, no en errores 4xx del cliente
            if e.status_code and e.status_code >= 500:
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)
            else:
                raise  # No retry en errores 4xx (400, 401, 403, etc)
```

## Solución Avanzada (Respetando Headers de OpenRouter)

OpenRouter envía headers específicos que debes usar:

```python
import time
import random
import openai
from openai import OpenAI

class OpenRouterClient:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )
        self.max_retries = 5
        
    def _extract_wait_time(self, response_headers=None, error=None):
        """Determina cuánto esperar basado en headers o error"""
        
        # 1. Primero: si hay un header Retry-After (en segundos)
        if response_headers and 'retry-after' in response_headers:
            try:
                return float(response_headers['retry-after'])
            except:
                pass
        
        # 2. Segundo: usar x-ratelimit-reset (timestamp Unix)
        if response_headers and 'x-ratelimit-reset' in response_headers:
            try:
                reset_time = float(response_headers['x-ratelimit-reset'])
                current_time = time.time()
                wait_time = reset_time - current_time
                return max(wait_time, 1)  # Mínimo 1 segundo
            except:
                pass
        
        # 3. Tercero: usar x-ratelimit-remaining
        if response_headers and 'x-ratelimit-remaining' in response_headers:
            try:
                remaining = int(response_headers['x-ratelimit-remaining'])
                if remaining == 0:
                    # Si no quedan requests, esperar 60s por defecto
                    return 60
            except:
                pass
        
        # 4. Default: backoff exponencial
        return None
    
    def create_completion(self, **kwargs):
        """Crea una completion con retry inteligente"""
        
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(**kwargs)
                
                # Log para monitorear límites
                print(f"✅ Request exitoso. Remaining: "
                      f"{response.headers.get('x-ratelimit-remaining', 'N/A')} requests")
                return response
                
            except openai.RateLimitError as e:
                if attempt == self.max_retries - 1:
                    print(f"❌ Rate limit agotado después de {self.max_retries} intentos")
                    raise
                
                # Intentar extraer tiempo de espera de los headers
                wait_time = self._extract_wait_time(
                    response_headers=getattr(e, 'response', {}).get('headers'),
                    error=e
                )
                
                if wait_time is None:
                    # Fallback a backoff exponencial
                    wait_time = min(2 ** attempt + random.uniform(0, 1), 60)
                
                print(f"⚠️ Rate limit (intento {attempt + 1}/{self.max_retries}). "
                      f"Esperando {wait_time:.2f}s...")
                time.sleep(wait_time)
                
            except openai.APIError as e:
                # Solo retry en errores 5xx y 429
                status_code = getattr(e, 'status_code', 0)
                if status_code in [502, 503, 504, 529]:  # Errores temporales
                    if attempt == self.max_retries - 1:
                        raise
                    
                    wait_time = min(2 ** attempt + random.uniform(0, 1), 30)
                    print(f"⚠️ Error temporal {status_code}. Esperando {wait_time:.2f}s...")
                    time.sleep(wait_time)
                else:
                    # No retry en errores 4xx (400, 401, 403, etc)
                    raise

# Uso:
client = OpenRouterClient(api_key="sk-or-xxxx")

try:
    response = client.create_completion(
        model="deepseek/deepseek-chat",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=100
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error final: {e}")
```

## Recomendaciones Clave

1. **Nunca hagas retry inmediato**: Siempre espera al menos 1 segundo
2. **Máximo 3-5 intentos**: Más que eso es señal de un problema mayor
3. **Usa jitter**: Evita que todos tus retries se sincronicen
4. **Lee los headers**: OpenRouter envía `x-ratelimit-*` que son tu mejor guía
5. **Loguea todo**: Para debuggear cuántos retries estás haciendo
6. **Considera un rate limiter local**: Para no depender solo del servidor

Ejemplo de rate limiter local (opcional pero recomendado):

```python
from threading import Semaphore
import time

class LocalRateLimiter:
    def __init__(self, max_calls, period):
        self.semaphore = Semaphore(max_calls)
        self.period = period
        
    def __enter__(self):
        self.semaphore.acquire()
        # Programar la liberación del semáforo
        timer = threading.Timer(self.period, self.semaphore.release)
        timer.start()
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Limita a 300 requests por minuto (OpenRouter default)
limiter = LocalRateLimiter(max_calls=300, period=60)

# Uso:
with limiter:
    response = client.create_completion(...)
```

Con esta implementación, tus 5 requests/minuto funcionarán perfectamente y el sistema será robusto ante fallos temporales.