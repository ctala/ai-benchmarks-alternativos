# Qwen 3.8 27B — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.44 | quality: 8.48
- latency_total: 29.931s | tokens_per_second: 68.4
- input_tokens: 155 | output_tokens: 2048
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

We need answer in Spanish. User asks: Escribe una funcion Python que: 1. GET https://api.example.com/products con autenticacion Bearer token 2. Filtre productos con precio > 100 3. Retorne lista de dicts con solo {id, name, price} 4. Maneje errores de red y timeout (10 segundos) 5. Incluya retry con backoff exponencial (max 3 intentos). Usa httpx y no dependencias externas adicionales.

Need produce code. Need likely include import httpx, time, maybe exceptions. Function signature fetch_products(token: str). Need retry max 3 attempts, backoff exponential. Timeout 10 seconds. Handle network errors and timeout. Maybe raise custom or return? "Maneje errores" likely catch and raise meaningful exception or return []? Better: after retries raise RuntimeError/ConnectionError. But maybe handle by logging? No external dependencies. Could use built-in logging? Standard library ok. But no external deps besides httpx. We can include try/except httpx.HTTPError, TimeoutException? httpx.TimeoutException subclass of HTTPError? In httpx, TimeoutException is subclass of HTTPError? Let's recall: httpx.HTTPError base? There are httpx.TimeoutException, httpx.TransportError, httpx.HTTPStatusError. Network errors: httpx.TransportError includes ConnectError, ReadTimeout? Actually httpx.TimeoutException is subclass of TransportError? In httpx exceptions: HTTPError base, RequestError (TransportError), HTTPStatusError. TimeoutException subclass of RequestError? I think httpx.TimeoutException inherits from RequestError? Let's verify mentally: httpx.HTTPError -> RequestError -> TransportError -> NetworkError? Hmm. To be safe catch (httpx.TimeoutException, httpx.TransportError) or httpx.HTTPError? HTTPError includes HTTPStatusError for status codes. We want network and timeout, not HTTP status errors? Could catch httpx.RequestError? If request not completed due network/timeout. But if server returns 401/404, raise_for_status raises HTTPStatusError, which is HTTPError not RequestError? In httpx, HTTPStatusError inherits HTTPError, not RequestError? Actually response.raise_for_status raises HTTPStatusError. We can catch httpx.HTTPError broadly. But user specifically network and timeout. Could catch httpx.TimeoutException and httpx.ConnectError etc. But broad httpx.HTTPError okay? It would also catch status errors, which may not be retryable? If 4xx/5xx maybe retry? Requirement only network/timeout. Better catch (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError, httpx.WriteError, httpx.PoolTimeout, httpx.RemoteProtocolError?) Too verbose. Use httpx.TransportError? Let's check httpx exception hierarchy: httpx.HTTPError
- RequestError
  - TransportError
    - TimeoutException
      - ConnectTimeout
      - ReadTimeout
      - WriteTimeout
      - PoolTimeout
    - NetworkError
      - ConnectError
      - ReadError
      - WriteError
      - CloseError
    - ProtocolError
      - LocalProtocolError
      - RemoteProtocolError
    - ProxyError
    - UnsupportedProtocol
- HTTPStatusError
Maybe TimeoutException and TransportError. If catch httpx.TransportError, includes timeouts and network. Good.

Need backoff exponential max 3 attempts. Use for attempt in range(max_retries): try ... except httpx.TransportError: if attempt == max_retries -1 raise; delay = base_delay * (2 ** attempt); time.sleep(delay). Base delay maybe 1 second. Need avoid blocking? Fine.

Bearer token: headers={"Authorization": f"Bearer {token}"}. timeout=10. Could use httpx.Client(timeout=10) with context manager, or httpx.get(url, headers=..., timeout=10). For retries, create client once? If using client, connection pooling. Need no additional deps. Code:

import time
import httpx

def obtener_productos(token: str, base_url: str = "https://api.example.com/products", max_retries: int = 3, timeout: float = 10.0) -> list[dict]:
    headers = {"Authorization": f"Bearer {token}"}
    last_error = None
    for attempt in range(max_retries):
        try:
            response = httpx.get(base_url, headers=headers, timeout=timeout)
            response.raise_for_status()
            products = response.json()
            # maybe if not list? handle
            if not isinstance(products, list): raise ValueError("La respuesta no es una lista")
            return [
                {"id": p.get("id"), "name": p.get("name"), "price": p.get("price")}
                for p in products
                if isinstance(p, dict) and p.get("price") is not None and float(p["price"]) > 100
            ]
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            last_error = exc
            if attempt == max_retries - 1:
                break
            time.sleep(2 ** attempt) # 1,2? base 1. Could use 1 * 2**attempt.
        # What about JSONDecodeError? httpx.JSONDecodeError? If invalid JSON, maybe not network. Could raise or retry? Not required. Could catch ValueError and raise RuntimeError.
    raise RuntimeError(f"No se pudo obtener productos después de {max_retries} intentos") from last_error

But if response.raise_for_status() raises HTTPStatusError (not TransportError), not caught; maybe should handle? Requirement network/timeout. But "maneje errores de red y timeout" not HTTP status. Could catch httpx.HTTPError broadly to handle status as errors. But then 401 would retry unnecessarily. Could catch httpx.HTTPStatusError and raise immediately? Better:
try:
 response = ...
 response.raise_for_status()
 ...
except httpx.HTTPStatusError as exc:
 raise RuntimeError(...) from exc
except (httpx.TimeoutException, httpx.TransportError) as exc:
 retry.
But httpx.TimeoutException is TransportError, so except httpx.TransportError catches it. But order: HTTPStatusError not subclass TransportError, so fine.

Need maybe use httpx.Client to reuse connection. Example:

def fetch_products(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    max_retries = 3
    timeout = 10.0
    for attempt in range(max_retries):
       try:
           with httpx.Client(timeout=timeout, headers=headers) as client:
               response = client.get(url)
               response.raise_for_status()
               data = response.json()
           return [ ...]
       except httpx.HTTPStatusError:
           raise
       except httpx.TransportError as exc:
           if attempt == max_retries - 1:
               raise RuntimeError(...) from exc
           time.sleep(1 * (2 ** attempt))
    # unreachable

Potential issue: httpx.TimeoutException is subclass of httpx.TransportError? If yes, catch TransportError enough. But if not? Let's be explicit: except (httpx.TimeoutException, httpx.TransportError). But if TimeoutException subclass, duplicate ok.

Need type hints? Python 3.9? list[dict] requires 3.9. Could use List from typing? No external, standard. To be safe use list[dict] if modern. Could include from __future__? Not needed.

Need ensure price numeric. If price string? Use Decimal? No external. float. If price not numeric, ValueError. Could skip or raise. Maybe robust: try: price = float(p.get("price")) except (TypeError, ValueError): continue. But requirement filter price > 100. If invalid, skip. Return price original or float? It says {id,name,price}; likely keep original price. Could return float? Better preserve original? But for comparison convert. Return p["price"] original. If price is string "120", returning string maybe okay? But probably numeric. Could return float(price) to ensure numeric. But if original int, float changes. Could return p["price"] after validation. If price is string, returning string might be undesirable. Could normalize to float? The spec only says price. I'd return float(price) for consistent numeric. But if price is Decimal? no. Simpler: if p.get("price", 0) > 100. But if None error. Use isinstance(price, (int, float)) and not bool. But price might be string. Could robust:

def _as_price(value):
    try:
       return float(value)
    except (TypeError, ValueError): return None

Then filtered = []
for item in products:
   if not isinstance(item, dict): continue
   price = _as_price(item.get("price"))
   if price is None or price <= 100: continue
   filtered.append({"id": item.get("id"), "name": item.get("name"), "price": price})
return filtered

This returns float. Good.

Need maybe handle response.json() invalid. httpx raises json.JSONDecodeError? It uses json library, raises httpx.DecodingError? Actually response.json() raises json.JSONDecodeError (ValueError) if invalid. Could catch ValueError and raise RuntimeError? Not network. Maybe include:
except ValueError as exc:
    raise RuntimeError