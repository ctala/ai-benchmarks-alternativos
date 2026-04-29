# Qwen 3-Next 80B Thinking (NIM) — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.87 | quality: 8.2
- latency_total: 20.589s | tokens_per_second: 99.5
- input_tokens: 116 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

## Respuesta completa

Okay, I need to write a Python function that does several things. Let me break down the requirements.

First, it has to make a GET request to https://api.example.com/products with Bearer token authentication. So I'll need to include the Authorization header with 'Bearer <token>'. But wait, the token isn't specified in the problem. Hmm, maybe the function should take the token as a parameter? The problem doesn't mention that, but probably the token is provided externally. So the function should accept a token argument.

Next, filter products where price > 100. Then return a list of dicts with only id, name, price fields. So after getting the data, process each product, check if price is over 100, and extract those three fields.

Handle network errors and timeouts with a 10-second timeout. Also, include retry with exponential backoff, max 3 attempts. Use httpx and no extra dependencies.

So, using httpx for the requests. I remember httpx has a timeout parameter. For retries, maybe I need to implement a retry mechanism manually since httpx doesn't have built-in retry for this. Wait, but the problem says "no dependencias externas adicionales", so I can't use a library like tenacity. So I need to write my own retry logic with exponential backoff.

Exponential backoff means each retry wait time increases exponentially. Like first retry after 1 second, then 2, then 4, etc. Max 3 attempts total.

So steps:

- Function takes token as parameter.

- Use httpx.Client or just httpx.get with retries.

Wait, but httpx.get is synchronous. The problem doesn't specify async, so probably using synchronous code.

But how to handle retries with backoff. So in a loop, up to max retries. For each attempt, try to make the request. If there's an exception (like network error or timeout), wait for a certain time before retrying.

The timeout for each request is 10 seconds. So when making the request, set timeout=10.

So the function structure:

def get_filtered_products(token):
    max_retries = 3
    base_delay = 1  # seconds
    for attempt in range(max_retries):
        try:
            # Make request with timeout=10
            response = httpx.get('https://api.example.com/products', headers={'Authorization': f'Bearer {token}'}, timeout=10)
            response.raise_for_status()  # Raises for 4xx/5xx
            # Process the data
            products = response.json()
            filtered = [{'id': p['id'], 'name': p['name'], 'price': p['price']} for p in products if p['price'] > 100]
            return filtered
        except httpx.RequestError as e:
            # If it's a network error or timeout
            # Check if it's the last attempt, then raise
            if attempt == max_retries -1:
                raise
            # Calculate delay: base_delay * (2 ** attempt)
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
        except httpx.HTTPStatusError as e:
            # Handle other HTTP errors, maybe like 4xx or 5xx
            # But maybe the problem says to handle network and timeout errors, but perhaps other errors should be handled too?
            # The problem says "Maneje errores de red y timeout", so maybe only network-related errors. But HTTPStatusError is for 4xx/5xx. But perhaps the function should not retry on those? Because maybe 401 is authentication error, which won't go away with retry. But the problem says "errors de red y timeout", so perhaps only exceptions like Timeout, ConnectError, etc.

Wait, the problem says "Maneje errores de red y timeout (10 segundos)". So perhaps only network-related errors and timeout should trigger retries. HTTPStatusError (like 404, 500) might not be retried. But maybe the problem is not specific, so perhaps we should retry only on exceptions that are network-related.

In httpx, exceptions like httpx.RequestError includes Timeout, ConnectError, etc. So when catching RequestError, we can retry. But HTTPStatusError is when status code is not successful. So maybe for those, we shouldn't retry. For example, if the API returns 401, that's an authentication error, so retrying won't help.

So in the except block, for RequestError, we retry. For HTTPStatusError, perhaps raise immediately.

So in the code, first catch RequestError (which includes timeouts, network issues), then for HTTPStatusError, handle separately.

But the problem says to handle network errors and timeout, so perhaps those are the ones to retry. So the code would:

In the try block, if there's a RequestError (like Timeout, ConnectError), then retry.

But HTTPStatusError is not a RequestError. So for example, 401 would raise HTTPStatusError, which is a subclass of HTTPError, but RequestError is for connection issues.

So in the except, first check for RequestError, which covers network issues and timeouts. Then if it's an HTTPStatusError, perhaps raise it without retry.

So in the code:

except httpx.RequestError as e:
    # handle retry

except httpx.HTTPStatusError as e:
    # handle this differently, maybe raise immediately

But the problem says "maneje errores de red y timeout", so perhaps only those. So for other errors like HTTPStatusError, maybe we don't retry but still return an error. But the problem doesn't specify how to handle HTTP errors, so maybe for this code, we should raise an exception when HTTPStatusError occurs.

But the problem says to handle network errors and timeouts with retry, so perhaps the code should retry only on network errors and timeouts. For HTTP errors like 4xx or 5xx, maybe we should not retry and just return the error. But the problem says "maneje errores de red y timeout", which implies that other errors may not be handled by the retry mechanism.

So in the code, when a RequestError occurs (which includes timeouts and network errors), we retry. For HTTPStatusError, we raise it immediately.

So in the function:

try:
    response = httpx.get(...)
    response.raise_for_status()
    ... process
except httpx.RequestError as e:
    # retry logic
except httpx.HTTPStatusError as e:
    # raise or handle as needed. Since problem says to handle network errors and timeout, perhaps this is not part of the retry. So we can raise it.

So for the code, let's structure it to catch RequestError for retries, and other exceptions like HTTPStatusError are raised.

Now, implementing the retry with exponential backoff. The max retries is 3. So first attempt (attempt 0), then if fails, wait 1 sec (2^0 * base_delay), then attempt 1, wait 2^1 * base_delay = 2, attempt 2, wait 4. Then if third attempt (attempt 2) fails, since max_retries is 3, the loop runs 3 times (0,1,2). So after 3 attempts, if all fail, raise the exception.

So code structure:

max_retries = 3
base_delay = 1
for attempt in range(max_retries):
    try:
        ... make request
        return filtered products
    except httpx.RequestError as e:
        if attempt == max_retries -1:
            raise
        delay = base_delay * (2 ** attempt)
        time.sleep(delay)
    except httpx.HTTPStatusError as e:
        # Handle this by raising immediately. For example, if the token is invalid, we don't retry.
        raise

So in the code, when there's a RequestError, we wait and retry. For HTTPStatusError, we raise immediately.

But the problem says to handle errors of network and timeout. So HTTPStatusError is not a network error, so we shouldn't retry on that. So for example, if the API returns 401, we raise it and stop.

Now, the code needs to import httpx and time.

So the function should be:

import httpx
import time

def get_filtered_products(token):
    max_retries = 3
    base_delay = 1
    for attempt in range(max_retries):
        try:
            response = httpx.get(
                'https://api.example.com/products',
                headers={'Authorization': f'Bearer {token}'},
                timeout=10
            )
            response.raise_for_status()
            products = response.json()
            filtered = [
                {'id': p['id'], 'name': p['name'], 'price': p['price']}
                for p in products
                if p['price'] > 100
            ]
            return filtered
        except httpx.RequestError as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
        except httpx.HTTPStatusError as e:
            # For HTTP errors, raise immediately as they are not network-related
            raise
        except Exception as e:
            # Maybe catch other exceptions, but perhaps not necessary. But to be safe?
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
But wait, the problem says "maneje errores de red y timeout", which are part of RequestError. So perhaps the only exceptions to handle for retry are RequestError and maybe some others? But the httpx.get could