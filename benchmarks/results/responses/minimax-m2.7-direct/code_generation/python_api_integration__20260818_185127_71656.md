# MiniMax M2.7 (directo) — code_generation/python_api_integration

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.36 | quality: 9.52
- latency_total: 27.367s | tokens_per_second: 74.8
- input_tokens: 133 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

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

The user asks: "Escribe una funcion Python que:

1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales."

We need to write a Python function using httpx library. Should include GET request with Bearer token in Authorization header. Filter for price > 100. Return list of dicts with keys id, name, price. Handle network errors and timeout of 10 seconds. Include retry with exponential backoff, max 3 attempts.

We should provide a code block. Should be thorough and include docstring, optional usage example, perhaps handle httpx exceptions: httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError etc.

Also incorporate exponential backoff: sleeping between retries, maybe using time.sleep. Should be careful to include jitter optional. We need to not import any external dependencies besides httpx.

We need to consider that the token is passed as parameter, maybe as a string. Provide function signature: def fetch_filtered_products(token: str) -> list[dict].

Potentially handle a response JSON format: expecting list of product objects with fields id, name, price. But maybe it's a dict with 'products' key. We'll assume it's a list directly. Provide robust parsing: if response is dict, check if 'products' present.

Also use httpx timeout configuration: httpx timeout=10.0. Use a client context manager to ensure connection pooling.

Also handle errors: raise custom exception or re-raise after retries.

Let's design the function:

- Import httpx, time, typing.
- Define custom exception classes: NetworkError, APIError, maybe.

- Define function fetch_filtered_products(bearer_token: str, url: str = "https://api.example.com/products", max_retries: int = 3, base_delay: float = 1.0) -> list[dict].

- Inside, set up a loop for attempts.

- Use try/except httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError, etc.

- After each failure (except maybe 4xx client errors?), we should retry for server errors (5xx) and network errors.

- Exponential backoff: delay = base_delay * (2 ** (attempt - 1)), plus random jitter.

- After max retries exhausted, raise exception.

- Once successful, parse JSON: data = response.json().

- If data is dict with key 'products', then data = data['products'].

- Then filter: [product for product in data if product.get('price', 0) > 100].

- Return list of dicts: [{'id': p['id'], 'name': p['name'], 'price': p['price']} for p in filtered].

- Optionally include type hints.

- Add docstring.

- Provide a usage example with try/except.

- Mention that token is not logged.

- Use time.sleep.

- Use the default httpx Client with timeout.

Potential nuance: Should we use a context manager to reuse client across retries? Yes, create client outside loop, reuse across retries. But we need to close it after all attempts.

Better: Create a client outside loop, and in each iteration, perform request.

But the client might hold connection pool; that's okay.

Potential network errors: ConnectError, ConnectTimeout, ReadTimeout, etc.

Simplify: In httpx we have httpx.ConnectError, httpx.TimeoutException, httpx.HTTPError (base). Use try/except httpx.HTTPError to catch any HTTP errors. But for clarity, catch specific ones.

Implement with try: response = client.get(url, headers={'Authorization': f'Bearer {bearer_token}'}, timeout=10.0). If response status >= 500, treat as retriable. For 4xx, not retriable. So we need to differentiate. If status code 401, maybe not retriable. So we can raise APIError with status code and stop.

Thus:

```
if response.status_code >= 500:
    # retry
elif response.status_code >= 400:
    raise APIError(f"Client error: {response.status_code}", status_code=response.status_code)
```

But we also need to handle httpx request errors: ConnectError, TimeoutException, etc.

If network error: treat as retriable.

We'll need to implement a loop for attempts.

Also include base_delay and max_delay.

Implementation details:

```
def fetch_filtered_products(
    token: str,
    url: str = "https://api.example.com/products",
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> list[dict]:
    """
    Fetch products from the API, filter those with price > 100,
    and return a list of dictionaries containing `id`, `name`, and `price`.
    Implements retry with exponential backoff on transient failures.
    """
    client = httpx.Client(timeout=10.0)
    try:
        for attempt in range(1, max_retries + 1):
            try:
                response = client.get(url, headers={"Authorization": f"Bearer {token}"})
                # Check for HTTP errors
                if response.status_code >= 500:
                    # Server error, retry
                    response.raise_for_status()  # This will raise HTTPStatusError for logging
                elif response.status_code >= 400:
                    # Client error, do not retry
                    response.raise_for_status()
                else:
                    # Success
                    break
            except (httpx.ConnectError, httpx.TimeoutException, httpx.HTTPStatusError) as exc:
                # Network or server error, will retry if attempts left
                if attempt == max_retries:
                    raise
                # Exponential backoff
                delay = base_delay * (2 ** (attempt - 1))
                # Add jitter to avoid thundering herd
                import random
                delay += random.uniform(0, 0.5 * delay)
                time.sleep(delay)
                continue
        else:
            # If loop finishes without break, raise generic error
            raise NetworkError("Request failed after exhausting retries")
    finally:
        client.close()
```

But need to handle that after successful response we break out of loop. However we need to break after success but before the try/except block finishes. Could restructure as:

```
for attempt in range(1, max_retries+1):
    try:
        response = client.get(...)
        if response.is_success:
            # success
            break
        elif response.status_code >= 500:
            # retry
            pass
        else:
            response.raise_for_status()
    except httpx.TimeoutException, etc:
        pass
    else:
        # no exception but not success
        pass
    if attempt < max_retries:
        delay = ...
        time.sleep(delay)
else:
    raise NetworkError...
```

Simplify: we can use a while loop with attempt count.

Better: incorporate retry logic in a separate inner function.

I think it's straightforward.

We need to define custom exceptions.

We'll also include docstring with example usage.

Edge Cases:

- The JSON response might not be a list but a dict with 'products' key. We'll try to detect.

- In case of missing fields, handle gracefully: use .get.

- For price field, ensure numeric.

Implementation:

```
def fetch_filtered_products(token: str, url: str = "https://api.example.com/products", max_retries: int = 3, base_delay: float = 1.0) -> list[dict]:
    """
    ...
    """
    class APIError(Exception):
        """Custom exception for API errors."""
        def __init__(self, message: str, status_code: int = None):
            super().__init__(message)
            self.status_code = status_code

    class NetworkError(Exception):
        """Custom exception for network errors after retries."""
        pass

    client = httpx.Client(timeout=10.0)
    try:
        for attempt in range(1, max_retries + 1):
            try:
                response = client.get(url, headers={"Authorization": f"Bearer {token}"})
                # Raise for 4xx and 5xx
                try:
                    response.raise_for_status()
                except httpx.HTTPStatusError as exc:
                    # If server error (5xx), we want to retry; for client error we raise directly
                    if exc.response.status_code >= 500:
                        # Server error, will retry
                        pass
                    else:
                        # Client error, raise APIError
                        raise APIError(f"API returned {exc.response.status_code}", status_code=exc.response.status_code)
                # If we reach here, request succeeded (2xx)
                break
            except (httpx.ConnectError, httpx.TimeoutException) as exc:
                # Network error, will retry
                pass
            except APIError:
                # Client error, re-raise immediately
                raise

            # If we are here, we need to retry
            if attempt < max_retries:
                delay = base_delay * (2 ** (attempt - 1))
                # Add jitter
                import random
                delay += random.uniform(0, 0.5 * delay)
                time.sleep(delay)
            else:
                raise NetworkError("Request failed after exhausting retries")
        else:
            # If loop ends without break (shouldn't happen)
            raise NetworkError("Request failed after exhausting retries")
    finally:
        client.close()

    # Parse response
    try: