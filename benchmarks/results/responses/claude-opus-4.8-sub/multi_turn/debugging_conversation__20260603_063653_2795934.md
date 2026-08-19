# Claude Opus 4.8 (suscripción) — multi_turn/debugging_conversation

- model_id: `claude-opus-4-8`
- success: True  | final: 7.32 | quality: 9.55
- latency_total: 22.145s | tokens_per_second: 67.6
- input_tokens: 2026 | output_tokens: 1496
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profundiza en la solución del problema de rate limiting con buenas prácticas de implementación, incluyendo ejemplos de código claros y útiles, manteniendo la coherencia con el contexto de la conversación.

## Respuesta completa

Buenísimo que lo encontraste — ese loop de retry infinito es exactamente lo que te tiraba el 429. Cada error generaba 100 requests, esos 100 fallaban, y la bola de nieve te dejaba permanentemente sobre el rate limit. Por eso "ni una llamada" funcionaba.

Acá está cómo implementar retries bien:

## Las 4 reglas de oro

1. **Límite de reintentos** — nunca infinito. 3-5 intentos máximo, después fallás de verdad.
2. **Backoff exponencial** — esperá más tiempo entre cada reintento (1s, 2s, 4s, 8s...).
3. **Jitter** — agregá aleatoriedad a la espera para no sincronizar reintentos.
4. **Respetá `Retry-After`** — si el server te dice cuánto esperar, hacele caso.

## Implementación en Python

```python
import time
import random
import httpx

def request_with_retry(client, payload, max_retries=5):
    for attempt in range(max_retries):
        try:
            resp = client.post("/chat/completions", json=payload)

            # Si NO es un error de rate limit, devolvé o fallá inmediato
            if resp.status_code != 429:
                resp.raise_for_status()
                return resp.json()

            # Es 429: calcular cuánto esperar
            retry_after = resp.headers.get("retry-after")
            if retry_after:
                wait = float(retry_after)            # el server manda
            else:
                wait = (2 ** attempt) + random.uniform(0, 1)  # backoff + jitter

            # NO esperar si es el último intento (no tiene sentido)
            if attempt < max_retries - 1:
                print(f"429 recibido, esperando {wait:.1f}s (intento {attempt+1}/{max_retries})")
                time.sleep(wait)

        except httpx.RequestError as e:
            # errores de red: mismo backoff
            wait = (2 ** attempt) + random.uniform(0, 1)
            if attempt < max_retries - 1:
                time.sleep(wait)
            else:
                raise

    raise RuntimeError(f"Falló tras {max_retries} intentos")
```

## Lo crítico que tenías mal

Tu loop seguramente hacía algo así:

```python
# ❌ MAL — esto es lo que te rompió todo
while True:
    try:
        return hacer_request()
    except:
        continue   # reintenta YA, sin esperar, sin límite
```

Tres problemas fatales:
- **Sin límite** → reintentos infinitos
- **Sin espera** → bombardea el server instantáneamente
- **`except:` pelado** → reintenta hasta errores que nunca se van a arreglar (auth, payload inválido)

## Sugerencia práctica

Para producción, mejor no reinventar la rueda. La librería **`tenacity`** te da todo esto declarativo:

```python
from tenacity import retry, stop_after_attempt, wait_exponential_jitter, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential_jitter(initial=1, max=30),
    retry=retry_if_exception_type(httpx.HTTPStatusError),
)
def hacer_request(client, payload):
    resp = client.post("/chat/completions", json=payload)
    resp.raise_for_status()
    return resp.json()
```

Y si usás el SDK de OpenAI (compatible con OpenRouter), ya trae retries con backoff incorporados — solo configurás `max_retries=5` al crear el cliente y te olvidás.

---

**Antes de seguir:** ahora mismo podrías seguir rate-limited por unos minutos aunque arregles el código, porque OpenRouter a veces aplica un cooldown tras un burst así. Esperá ~5 min antes de probar de nuevo.

¿Querés que veamos qué tipo de cliente estás usando (SDK de OpenAI, httpx directo, requests) para darte la versión exacta que te calza?