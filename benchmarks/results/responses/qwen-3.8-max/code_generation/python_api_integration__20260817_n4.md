# Qwen 3.8 Max — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.31 | quality: 8.68
- latency_total: 43.922s | tokens_per_second: 46.7
- input_tokens: 151 | output_tokens: 2050
- judge_score: 4.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales.


## Respuesta completa

We need answer in Spanish. User asks: "Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales."

Need provide code only? Probably explanation too. Need satisfy: use httpx, no extra deps. Need function. Need handle network errors and timeout 10s. Retry exponential backoff max 3 attempts. Bearer token. Filter price > 100. Return list dicts with id, name, price. Need consider response JSON shape maybe list of products or maybe data key? We can assume list, but robust maybe support list or {"products": [...]}? The prompt says GET to /products; likely response list. Could write function fetch_expensive_products(token: str) -> list[dict]. Use httpx.Client(timeout=10.0). Retry loop attempts max 3. Backoff exponential: sleep 1,2? max 3 intentos means attempts=3. Use time.sleep from stdlib. Catch httpx.TimeoutException, httpx.NetworkError maybe httpx.HTTPStatusError? Retry on network/timeout and maybe 5xx? Requirement network and timeout. Could include raise_for_status and retry on HTTPStatusError for 5xx/429? But no additional dependencies. Need not use tenacity. Need Bearer header.

Potential implementation:

import time
import httpx

def get_expensive_products(token: str, *, min_price: float = 100.0) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3
    last_exc: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.get(url, headers=headers)
                response.raise_for_status()
                payload = response.json()
                products = payload if isinstance(payload, list) else payload.get("products", []) maybe if dict. But if dict with no products? Could return [] or raise. Better assume list; but robust.
                result=[]
                for product in products:
                    try:
                       price = float(product.get("price"))
                    except (TypeError, ValueError): continue? Maybe skip invalid.
                    if price > 100:
                       result.append({"id": product.get("id"), "name": product.get("name"), "price": price})
                return result
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_exc = exc
            if attempt == max_attempts: break
            time.sleep(2 ** (attempt - 1)) # 1,2? Actually 2**(attempt-1) =1,2. If max attempts 3, sleep after 1 and 2.
        except httpx.HTTPStatusError as exc:
            # maybe retry only 5xx/429; else raise? Requirement handle network/timeout; but robust.
            if exc.response.status_code in (429,500,502,503,504) and attempt < max_attempts:
                last_exc=exc; time.sleep(2**(attempt-1)); continue
            raise
    raise RuntimeError("...") from last_exc

Need be careful if HTTPStatusError caught and attempt max? If non-retryable raise. If retryable and attempt max break then raise RuntimeError. Could simpler: retry only TimeoutException, NetworkError. But maybe include HTTPStatusError? It says maneje errores de red y timeout. Could not need HTTP status. But raise_for_status will raise HTTPStatusError for 4xx; if not caught, it propagates. Is that okay? It says handle network errors and timeout. Could wrap and raise custom? Need maybe return []? "Maneje errores" could mean catch and raise controlled exception or return empty? Usually handle by retry and if fails raise. We can define exception? No external. Could return []? But hiding errors. Better after retries raise RuntimeError or re-raise last exception. But function should return list. Could raise last_exc. If last_exc is None? Could.

Need use only httpx and standard library. time is standard. typing optional.

Need maybe Python 3.10 type hints. Could use list[dict[str, object]].

Need ensure no extra dependencies. httpx is allowed.

Could include docstring and usage.

Need maybe mention that if API returns dict with products key, adapt. But final answer likely code.

Let's craft final in Spanish. Include function. Maybe include notes. Need ensure max 3 intentos: if first fails sleep 1s, second fails sleep 2s, third fails raise. Exponential backoff: base 1s factor 2. Could use time.sleep(min(2 ** attempt, 10)) but simple.

Consider HTTPStatusError: If response 200 but invalid JSON? Should handle? Not required. Could catch httpx.HTTPError? But HTTPStatusError is subclass of HTTPError. If catch broad httpx.HTTPError, retry on all HTTP errors including 400, not ideal. Requirement network and timeout. Could catch httpx.TransportError? In httpx, NetworkError subclass TransportError; TimeoutException also HTTPError? Let's recall httpx exceptions: HTTPError base; TransportError(TimeoutException? Actually TimeoutException inherits TransportError? In httpx, TimeoutException(HTTPError)? Need check. NetworkError(TransportError). Could catch httpx.TransportError and httpx.TimeoutException? TimeoutException maybe TransportError? I think httpx.TimeoutException inherits TransportError? Let's recall: httpx.HTTPError; TransportError(HTTPError); TimeoutException(TransportError); ConnectTimeout(TimeoutException); ReadTimeout etc; NetworkError(TransportError). So catch httpx.TransportError covers timeout and network? But maybe too broad includes protocol errors. Fine. But explicit better: (httpx.TimeoutException, httpx.NetworkError). For HTTP status 5xx we might retry. Need catch after raise_for_status. If 4xx, not retry. Could implement.

Potential issue: If response is not JSON, response.json() raises maybe json.JSONDecodeError (stdlib). Not dependency. Should we handle as error? Could raise ValueError. Not required. Could catch and raise RuntimeError. But not necessary.

Need ensure product price maybe Decimal? float conversion. If price is string "101" works. If missing skip? Maybe skip invalid products. But if id/name missing? Include None. Could require. Maybe if product doesn't have id/name? Could still include. Better to only include if has required fields? The prompt says return dicts with only {id,name,price}. If missing, maybe skip? But could be unexpected. I'd include if price valid; id/name get None. But more robust: if product is dict and all keys? Could skip invalid. But filter price >100. If price missing skip.

Let's design final code:

"""Obtiene productos > 100 con retry/backoff usando httpx."""
import time
from typing import Any
import httpx

URL = "https://api.example.com/products"

def fetch_products_over_100(token: str) -> list[dict[str, Any]]:
    """..."""
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3
    backoff_base = 1.0
    last_error: Exception | None = None

    for attempt in range(1, max_attempts + 1):
        try:
            with httpx.Client(timeout=timeout) as client:
                resp = client.get(URL, headers=headers)
                resp.raise_for_status()
                data = resp.json()

            # Soporta respuesta lista o {"products": [...]}
            if isinstance(data, list):
                products = data
            elif isinstance(data, dict) and isinstance(data.get("products"), list):
                products = data["products"]
            else:
                raise ValueError("Formato de respuesta inesperado")

            filtered = []
            for p in products:
                if not isinstance(p, dict):
                    continue
                try:
                    price = float(p.get("price"))
                except (TypeError, ValueError):
                    continue
                if price > 100:
                    filtered.append({
                        "id": p.get("id"),
                        "name": p.get("name"),
                        "price": price,
                    })
            return filtered

        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_error = exc
        except httpx.HTTPStatusError as exc:
            # Retry solo errores transitorios HTTP; 4xx no se reintentan.
            if exc.response.status_code in {429, 500, 502, 503, 504}:
                last_error = exc
            else:
                raise
        except ValueError:
            # JSON invalido/formato inesperado: no reintentar? Could maybe