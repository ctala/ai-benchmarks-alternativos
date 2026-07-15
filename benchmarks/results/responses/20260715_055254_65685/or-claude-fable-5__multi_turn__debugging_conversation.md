# Claude Fable 5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 14.231s | tokens_per_second: 60.5
- input_tokens: 539 | output_tokens: 861
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución detallada con buenas prácticas como el backoff exponencial y el jitter, lo que la hace altamente útil y clara para un emprendedor.

## Respuesta completa

Ahi esta el problema. El retry infinito crea un efecto cascada: cada 429 genera mas requests, que generan mas 429s. Asi es como se implementa correctamente con **exponential backoff**:

```python
import time
import requests

def llamar_api(payload, max_retries=5):
    for intento in range(max_retries):
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json=payload
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 429:
            # Respetar el header Retry-After si existe
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                espera = int(retry_after)
            else:
                # Backoff exponencial: 1s, 2s, 4s, 8s, 16s
                espera = 2 ** intento

            print(f"Rate limit. Esperando {espera}s (intento {intento + 1}/{max_retries})")
            time.sleep(espera)
            continue

        # Otros errores: no reintentar ciegamente
        response.raise_for_status()

    raise Exception(f"Fallo despues de {max_retries} intentos")
```

Los puntos clave:

1. **Limite maximo de retries** (5 es razonable) - nunca infinito
2. **Backoff exponencial**: cada retry espera el doble que el anterior
3. **Respetar `Retry-After`**: si el servidor te dice cuanto esperar, hazle caso
4. **Solo reintentar en 429/5xx** - un 400 o 401 nunca se va a arreglar reintentando

Mejora opcional: agrega *jitter* (aleatoriedad) para evitar que multiples clientes reintenten al mismo tiempo:

```python
import random
espera = (2 ** intento) + random.uniform(0, 1)
```

Con esto, tus 5 req/min reales van a funcionar sin problema. El loop infinito era lo que te estaba saturando el limite.