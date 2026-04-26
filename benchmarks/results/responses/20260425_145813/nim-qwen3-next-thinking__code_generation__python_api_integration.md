# Qwen 3-Next 80B Thinking (NIM) — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.07 | quality: 8.48
- latency_total: 18.692s | tokens_per_second: 109.6
- input_tokens: 116 | output_tokens: 2048
- judge_score: 4.2 | justificación: 

## Respuesta completa

Okay, let's see. The user wants a Python function that does a GET request to https://api.example.com/products with Bearer token authentication. Then filter products with price over 100, return only id, name, price. Handle network errors and timeouts with 10 seconds, and use exponential backoff retry max 3 times. Using httpx and no extra dependencies.

First, I need to use httpx. The standard way to make HTTP requests with authentication. Bearer token means the Authorization header is "Bearer <token>". So I'll need to pass the token as part of the headers.

Next, handling errors and retries. The user said to use exponential backoff. For that, maybe use the httpx's retry mechanism. Wait, but the question says "no dependencias externas adicionales", so I can't use a separate retry library. So I need to implement the retry logic manually with exponential backoff.

Exponential backoff usually means each retry waits longer, like 2^attempt seconds or something. For example, first retry after 1 second, then 2, then 4, etc. Max 3 attempts total.

So the function should have a loop that tries up to 3 times, with delays between retries. If any exception occurs (like network errors, timeouts), it should retry. But how to handle the timeout for each request? The problem says "maneje errores de red y timeout (10 segundos)", so each request should have a timeout of 10 seconds. So when making the request, set timeout=10.0.

Wait, httpx's timeout parameter can be a float for connect and read timeouts. So maybe timeout=10.0, but perhaps specify connect and read separately. But the user says "timeout (10 segundos)", so maybe just set timeout=10.0.

Now, for retrying on errors. So possible exceptions: httpx.RequestError (which covers network issues), httpx.TimeoutException, maybe others. So in the retry loop, catch exceptions, wait, then retry.

But how to structure the retry. Let's think: max_retries=3, so 0,1,2 attempts. Wait, if max 3 attempts, then initial attempt plus 2 retries. So the loop can run for up to 3 times.

For each attempt, start with a backoff delay. The backoff time could be base * 2 ** attempt. So first retry after 1 second, then 2, then 4. But maybe the first attempt is immediate, then after first failure, wait 1s, then 2s, etc. Wait, the max retries is 3, so the function tries up to 3 times. So for attempt 0 (first try), then if fails, wait, then attempt 1 (second try), then wait, attempt 2 (third try). So total 3 attempts.

The backoff could be calculated as base_delay * (2 ** attempt), but for the first retry (second attempt), attempt count is 1, so base_delay * 2^1. Let's say base_delay is 1 second. So first retry after 1s, second after 2s, third after 4s.

But maybe the initial attempt is attempt 0. So for attempt 0 (first try), no wait. Then if fails, wait for 1s, then attempt 1. Then if fails, wait 2s, attempt 2. Then if fails, max retries reached.

So the code would have a loop from 0 to max_retries (which is 3), but the number of attempts is max_retries +1? Wait, no. If max_retries is 3, then the function tries up to 3 times. Wait, no. The standard is that max_retries is the number of retries. So initial attempt plus max_retries retries. So total attempts = max_retries +1.

So if max_retries=2, then total 3 attempts. So in the code, the loop can run for up to max_retries +1 times. Or perhaps set max_attempts=3, then loop for i in range(max_attempts), and if i>0, then wait.

So for i in range(3): # 0,1,2

if i >0: wait for backoff time.

So base_delay=1, then for i=0: no wait. i=1: wait 1*2^0 =1? Wait, maybe better to have base_delay * (2 ** i). So for i=0 (first attempt), no delay. Wait, no. Let's think: when the first attempt fails, then we wait for the backoff before retrying. So the first retry (second attempt) would wait 1 second, then second retry (third attempt) wait 2 seconds. So for i in 0 to max_retries-1 (since max_retries=3, then i=0,1,2 for retries). Wait, perhaps better to have:

max_retries = 3 (total attempts)

for attempt in range(max_retries):

    try:

        make request

        if response ok, return data

    except Exception as e:

        if attempt == max_retries -1:

            raise e

        else:

            wait for backoff

            backoff = base * 2 ** attempt

But the base could be 1 second. So first attempt (attempt 0), if fails, then wait 1 * 2^0 =1s. Then attempt 1, if fails, wait 2^1=2s. Then attempt 2 (third attempt), if fails, then raise.

Yes. So for attempt 0 (first try), then if fails, wait 1s. Then attempt 1, if fails wait 2s. Attempt 2 (third try), if fails, raise.

So the code for the retry loop would have:

max_retries = 3

base_delay = 1

for attempt in range(max_retries):

    try:

        # make request

        response = client.get(url, headers=headers, timeout=timeout)

        # check if response is ok

        response.raise_for_status()

        # process data

        products = response.json()

        # filter products with price >100

        filtered = [{'id': p['id'], 'name': p['name'], 'price': p['price']} for p in products if p['price'] > 100]

        return filtered

    except Exception as e:

        if attempt == max_retries -1:

            raise e

        else:

            # calculate backoff

            delay = base_delay * (2 ** attempt)

            time.sleep(delay)

But the user said to handle network errors and timeout. So the exceptions to catch would include httpx.RequestError, which includes network issues, timeouts, etc. Because httpx's exceptions are subclasses of httpx.RequestError.

Wait, httpx.TimeoutException is a subclass of httpx.RequestError, so catching httpx.RequestError would cover it. But perhaps better to catch all exceptions, or specifically httpx.RequestError. But to be safe, maybe catch all exceptions, but perhaps better to catch specific ones. However, the problem says "maneje errores de red y timeout", so probably exceptions related to network and timeout. So catching httpx.RequestError.

But in Python, httpx.RequestError is the base exception for all network-related errors. So yes, catching that.

But the code would have to import httpx, and maybe time for sleep.

Wait, the user said "no dependencias externas adicionales", so time is part of standard library, so okay.

So steps:

- Import httpx and time.

- Function takes a token (assuming the token is passed as a parameter, or maybe hardcoded? But the problem doesn't specify. Probably the function needs to take the token as an argument.)

Wait, the problem says "Haga GET a https://api.example.com/products con autenticacion Bearer token". So the function should probably take the token as a parameter.

So the function signature might be something like:

def get_filtered_products(token: str) -> list:

Then inside, set headers with Bearer token.

Then, set timeout=10.0 for the request.

So for the client, when doing get, timeout=10.0.

Wait, httpx timeout parameter can be a float, which sets both connect and read timeouts. Or a tuple for connect and read. But the user says timeout of 10 seconds, so probably just timeout=10.0.

So code:

client = httpx.Client()

But to avoid creating a client each time, but since it's a single request, maybe using httpx.get directly with timeout.

Yes, better to use httpx.get with timeout.

So:

try:

    response = httpx.get(url, headers=headers, timeout=10.0)

except httpx.RequestError as e:

    # handle

But the exception handling.

So putting it all together.

Let me write the code.

First, imports:

import httpx

import time

Then function:

def get_filtered_products(token: str) -> list:

    url = "https://api.example.com/products"

    headers = {"Authorization": f"Bearer {token}"}

    max_retries = 3

    base_delay = 1

    for attempt in range(max_retries):

        try:

            response = httpx.get(url, headers=headers, timeout=10.0)

            response.raise_for_status()

            products = response.json()

            filtered = [{'id': p['id'], 'name': p['name'], 'price': p['price']} for p in products if p['price'] > 100]

            return filtered

        except http