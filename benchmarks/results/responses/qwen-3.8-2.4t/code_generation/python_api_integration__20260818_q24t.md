# Qwen 3.8 2.4T (A95B) — code_generation/python_api_integration

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 7.47 | quality: 8.48
- latency_total: 20.252s | tokens_per_second: 101.1
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

We need answer in Spanish likely. User asks: "Escribe una funcion Python que: ... Usa httpx y no dependencias externas adicionales." Need provide code. Need think through requirements.

Need produce final answer with Python function using httpx. No extra dependencies. Should implement GET https://api.example.com/products with Bearer token. Filter price > 100. Return list of dicts with only id,name,price. Handle network errors and timeout 10 seconds. Retry with exponential backoff max 3 attempts. Use httpx only. Could use time.sleep (stdlib). Need maybe typing. Need robust: raise_for_status? HTTP errors? The requirement says errores de red y timeout. But probably also handle HTTP status? Retry maybe for network errors and timeouts, maybe 5xx? Could include httpx.HTTPStatusError? "no dependencias externas adicionales" means only httpx and stdlib. Could implement:

import time
import httpx

def get_expensive_products(token: str) -> list[dict]:
    url = "https://api.example.com/products"
    headers = {"Authorization": f"Bearer {token}"}
    timeout = httpx.Timeout(10.0)
    max_attempts = 3
    base_delay = 1.0
    last_exc = None
    for attempt in range(max_attempts):
        try:
            with httpx.Client(timeout=timeout, headers=headers) as client:
                response = client.get(url)
                response.raise_for_status()
                data = response.json()
                # Maybe data could be list or dict with results? Requirement simple. Assume list. Could handle if dict? Maybe not.
                products = data if isinstance(data, list) else data.get("products", [])? But to be safe? It says filtre productos. Could assume JSON list. But robust: if response JSON is list. If not, raise ValueError.
                return [
                   {"id": p["id"], "name": p["name"], "price": p["price"]}
                   for p in products
                   if isinstance(p, dict) and p.get("price") is not None and float(p["price"]) > 100
                ]
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
             last_exc = exc
             if attempt < max_attempts -1:
                 time.sleep(base_delay * (2 ** attempt))
                 continue
             raise RuntimeError... from exc? Or raise last_exc.
        except httpx.HTTPStatusError as exc:
             # For 5xx maybe retry? 4xx not? Requirement network and timeout. But could retry 5xx. Need not overcomplicate. If include HTTPStatusError, need backoff for 5xx maybe. But user only asked network y timeout. Could keep simple: catch httpx.HTTPError? But HTTPStatusError is HTTPError. If catch all httpx.HTTPError and retry, 401 will retry unnecessarily. Better catch TimeoutException, NetworkError. For HTTPStatusError maybe raise immediately or retry if >=500. But requirement "Maneje errores de red y timeout" not necessarily HTTP. But robust.
Need ensure max 3 intentos. Exponential backoff. Could delay 1,2 seconds. Use attempt number.

Potential issue: "no dependencias externas adicionales" httpx is external but allowed. Use only httpx and standard library.

Could include type hints: list[dict[str, object]] maybe. Python 3.9+? If want compatibility, from typing import List, Dict? But stdlib. Could use list[dict] (3.9). Fine.

Need maybe pass token as argument. Could also environment variable? The prompt says with authentication Bearer token, likely function receives token. Could define def fetch_products(token: str):.

Need consider missing fields: Should we include only products with id,name,price present? Use if all(k in p for k in ("id","name","price")) and price > 100. If price string? Could convert to float. But if price is Decimal? JSON numeric. Use float(p["price"]) > 100. If conversion fails, skip? Could raise? Better robust: skip invalid? But requirement just filter. Could do:

result = []
for product in products:
    try:
       price = float(product.get("price"))
    except (TypeError, ValueError):
       continue
    if price > 100:
       result.append({"id": product.get("id"), "name": product.get("name"), "price": price})

But if id/name missing, maybe include None? "con solo {id, name, price}". Could require keys. Maybe:
if all(key in product for key in ("id", "name", "price")):
...

Need return list of dicts exactly keys. If price was int, returning float maybe changes type. Could preserve original price if numeric. But filter compare. Could use price_value = product["price"]; if isinstance(price_value, (int, float)) and price_value > 100. But JSON may have Decimal? httpx returns JSON as Python int/float/str. Could do price = product["price"]; if isinstance(price, (int,float)) and price > 100. But if price is string "101", skip. Maybe acceptable. Could convert to float but return original or float? The requirement says price. To avoid type changes, use:
price = product["price"]
if isinstance(price, (int, float)) and price > 100:
   ... price: price
But booleans are int subclass; True > 100 false. Fine. If price is string, maybe not. Could convert and return float. Usually APIs price numeric. Simpler:
filtered = [
    {"id": p["id"], "name": p["name"], "price": p["price"]}
    for p in payload
    if p.get("price", 0) > 100
]
But if missing price, KeyError? p.get. If price None, comparison error. Use try.

Need handle response payload not list. Could raise ValueError. If API returns {"products": [...]} maybe not specified. We can write helper:
payload = response.json()
if isinstance(payload, dict):
    products = payload.get("products", [])
elif isinstance(payload, list):
    products = payload
else: products = []
But this may be beyond. Could include to be robust. But if dict with other key, no. Maybe keep simple: products = response.json(); if not isinstance(products, list): raise ValueError("..."). That is clear.

Retry: Need ensure with httpx.Client inside loop? Could create once outside. But if network error, client maybe still ok. Simpler:

def get_high_value_products(token: str) -> list[dict]:
    url=...
    headers=...
    timeout = httpx.Timeout(10.0)
    max_attempts=3
    last_exception: Exception | None = None
    for attempt in range(max_attempts):
       try:
          response = httpx.get(url, headers=headers, timeout=timeout)
          response.raise_for_status()
          products = response.json()
          if not isinstance(products, list): raise ValueError(...)
          result=[]
          for p in products:
             if not isinstance(p, dict): continue
             try:
                price = float(p.get("price"))
             except (TypeError, ValueError):
                continue
             if price > 100:
                result.append({"id": p.get("id"), "name": p.get("name"), "price": price})
          return result
       except (httpx.TimeoutException, httpx.NetworkError) as exc:
          last_exception = exc
       except httpx.HTTPStatusError as exc:
          # Retry only 5xx? Could include. But if 4xx, raise. If 5xx, retry. But user only network/timeout. If we catch HTTPStatusError and retry 5xx, need last_exception. Could implement:
          if exc.response.status_code >= 500 and attempt < max_attempts -1:
             last_exception=exc
          else: raise
       # after catch, if attempt < max_attempts - 1: sleep(...); else raise RuntimeError... from last_exception

But careful: If HTTPStatusError 5xx on last attempt, code after except? We can structure:

for attempt in range(max_attempts):
   try: ...
   except (httpx.TimeoutException, httpx.NetworkError) as exc:
       last_exc = exc
   except httpx.HTTPStatusError as exc:
       if exc.response.status_code < 500:
           raise
       last_exc = exc
   if attempt < max_attempts - 1:
       time.sleep(2 ** attempt)
       continue
   raise RuntimeError("...") from last_exc

But if ValueError due invalid JSON or not list, not retried, raises. Good.

Need maybe catch httpx.InvalidURL? Not needed. Could catch httpx.HTTPError? But no.

Potential problem: If HTTPStatusError 5xx caught and attempt is last, after except we go to if attempt < ... false then raise RuntimeError. Good.

Should backoff be exponential: delay = 2 ** attempt (1,2) or 0.5 * 2**attempt? Max 3 intentos means 2 retries after first. Could use delay = min(2 ** attempt, 8). Maybe.

Need ensure function returns if success.