# Qwen 3-Next 80B Thinking — code_generation/python_api_integration

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.52 | quality: 8.2
- latency_total: 21.145s | tokens_per_second: 96.9
- input_tokens: 114 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

## Respuesta completa

Okay, let's see. I need to write a Python function that does a GET request to a specific API endpoint with Bearer token auth, filters products priced over 100, returns a list of dicts with id, name, price, handles network errors and timeouts with a 10-second timeout, and includes exponential backoff retry up to 3 times. Using httpx and no extra dependencies.

First, I remember that httpx is a good library for making HTTP requests. It's async by default but can be used sync. But the problem doesn't specify async, so maybe I should use the sync version to keep it simple. Wait, but httpx has bothsync and async. The question says "no dependencies external additional", so httpx is allowed since it's the only one mentioned. So I need to import httpx.

Authentication: Bearer token. So in the headers, Authorization:Bearer <token>. But the token is not given in the problem. Wait, the problem says "with Bearer token" but doesn't specify where the token is coming from. Maybe the function should take the token as a parameter? Or is the token hardcoded? The problem statement doesn't specify, but in real code, the token would probably be passed as an argument. But the problem says "Escribe una funcion Python que..." so the function should probably take the token as a parameter. Wait, the problem doesn't explicitly say, but in the description, it's mentioned "autenticacion Bearer token", so the function should accept the token as a parameter. But the problem statement doesn't specify the parameters. Hmm. Let me check again.

The problem says: "1. Haga GET a https://api.example.com/products con autenticacion Bearer token". So the function must include the Bearer token in the headers. But where does the token come from? The function probably needs to take the token as a parameter. So the function signature would be something like def get_products(token: str) -> list. Or maybe the token is stored in an environment variable, but the problem doesn't specify. But the problem statement doesn't mention any specific parameter, so perhaps the function is supposed to handle the token in some way. Wait, but in the absence of specific instructions, the function should probably take the token as an argument. Otherwise, how would it get the token? So I'll assume the function has a parameter for the token.

Next, the function needs to make the GET request. Using httpx, so something like response = httpx.get(url, headers={'Authorization': fBearer {token}'}), but with error handling and retries.

Handling errors: network errors and timeout. The timeout is 10 seconds. So in httpx, the timeout parameter can be set to 10.0. But also, the function needs to retry with exponential backoff up to 3 times. So in case of any exceptions (like network errors, timeouts, etc.), it should retry with backoff.

httpx has built-in retry mechanisms? Or do I need to implement it manually. Since the problem says "no dependencies externas adicionales", so I can't use something like tenacity or retrying. So I have to implement the retry logic myself.

Exponential backoff: typically, for each retry, wait 2^retry_attempt seconds, plus some jitter. but max 3 attempts. So first try, then if fails, wait 2^1=2 seconds, then 4, then 8, but since max 3 attempts, the first try is attempt 0, then first retry is 1, second retry is 2. Wait, 3 total attempts:  initial, then two retries. So max 3 attempts. So the backoff would be 2^0, 2^1, 2^2? No, usually the first retry is 2^1, then 2^2, etc. But the standard is to start with 0.5 or 1, then double each time.

But the problem says "retry with backoff exponential (max 3 intentos)". So 3 attempts total. So initial request, then two retries. So for the first retry (second attempt), wait 2 seconds, then 4, then 8? But max 3 attempts, so the wait times would be 2, 4, but perhaps with a base. Let's see: for the nth retry (starting at 0 for the first attempt), the sleep time is 2^n * base. But max 3 attempts, so n can be 0,1,2. But for the first attempt (n=0), no wait. Then first retry (second attempt, n=1) wait 2^1 * base. Second retry (third attempt, n=2) wait 2^2 * base. But the base could be 1 second. So 2, 4 seconds. but perhaps with some jitter. But the problem doesn't specify, so maybe just 2^ (attempt number -1) * 1 second. Let's say for the first retry (2nd attempt), wait 2^0 * 1 = 1 second. Then 2^1 * 1 = 2, then 4. But max 3 attempts total (1 initial, 2 retries). So the code would have a loop for up to 3 times, with a wait time between retry attempts.

So in code, I can use a for loop from 0 to 2 (3 attempts). For each attempt, try the request. If it fails, wait a certain time. For the first attempt (i=0), no wait. For i=1, wait 2^0 *1 second. i=2, 2^1 *1. So total 3 attempts. But the standard exponential backoff is 2^i where i is the number of retries. So for the first retry ( second attempt), 2^1, but sometimes starting at 1. Let's see. For example, in some implementations, the first retry is 1 second, then 2, then 4. So for 3 attempts, the first is 1, then 2, then 4. But the max 3 attempts, so 1, 2, 4. But the problem says "backoff exponential (max 3 intentos)", so 3 attempts total.

So in code, for i in range(3):
    try:
        make request with timeout 10s
        break
    except exceptions:
        if i < 2:
            sleep(2**i * 0.5) or something. But the exact formula can vary. Maybe 2^i * base. Let's say base is 1 second. So for the first retry (i=1, since the first attempt is 0, then first retry is 1), sleep 2^1 * 1 = 2. But no, usually the number of retries is the count. Let's say for 3 attempts, the first attempt is 0, then if it fails, first retry (1st retry, second attempt), wait 2^1, then second retry (third attempt), wait 2^2. But 2^1 is 2, 2^2 is 4. But sometimes starting at 1. For example, in some implementations, the initial wait is 1 second, then 2, then 4. So for 3 attempts, the first retry (second attempt) wait 1 second, then 2, then 4. But the exact numbers might not matter as long as it's exponential. Let's use 2**i * 1 second for i starting at 0. So for the first retry (i=0), 1 second. second retry (i=1), 2 seconds. third attempt (i=2), 4 seconds. But the total 3 attempts, so the first attempt is 0, then two retries. Wait, no. If the function is to try up to 3 times, then the loop runs 3 times. For the first iteration (i=0), no wait. then if it fails, wait 2^0 = 1. then second iteration (i=1), if fails, wait 2^1=2. then third iteration (i=2), if fails, no more. But the max 3, so 3 attempts.

Wait, for example:

for attempt in range(3):
    try:
        ... do request ...
        break
    except Exception as e:
        if attempt < 2:
            wait time = 2 ** attempt * 0.5  # or 1 second base
            time.sleep(wait time)
        else:
            raise

But in this case, for the first attempt (0), no sleep. if fails, then for the second attempt (1st retry), sleep 2^0 * 0.5 = 0.5. Then third attempt (2nd retry), sleep 2^1 * 0.5 = 1.0. But the exact values can vary. The problem says "backoff exponential", so the key is that the wait time increases exponentially with each retry. So using 2**attempt * base is standard. Let's choose base 1 second. So for first retry (attempt 1, since first attempt is 0, then when it fails, for the next attempt, which is the first retry), the sleep time is 2^0 * 1 = 1 second. Then for the second retry (second attempt), sleep 2^1 *1 = 2. Then for the third attempt ( third try), sleep 2^2 *1 =4. but the max 3, so 3 attempts total. So