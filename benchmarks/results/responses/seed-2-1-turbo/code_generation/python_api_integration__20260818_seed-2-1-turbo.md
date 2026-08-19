# Seed 2.1 Turbo — code_generation/python_api_integration

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.49 | quality: 8.48
- latency_total: 39.313s | tokens_per_second: 52.1
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


El usuario pide una función Python con httpx, la función debe cumplir 5 requisitos claros: usar Bearer token sin hardcodearlo, filtrar productos con precio > 100, retornar lista de dicts con campos id/name/price, manejar errores y timeouts de red, y implementar retry exponencial manual con 3 intentos máximo sin dependencias externas adicionales.

He definido los detalles del reintento exponencial: se implementará de forma manual sin dependencias externas, con un máximo de 3 intentos en total y un retardo exponencial base de 1 segundo entre cada reintento. También he confirmado que estableceré un límite de tiempo total de 10 segundos para cada solicitud.

Para la autenticación Bearer, el token se pasará como parámetro de la función y se incluirá en el encabezado de autorización. En cuanto al manejo de errores, se capturarán excepciones de red y de respuesta, reintentando solo errores de servidor (5xx) y el código 429, no los errores de cliente (4xx) en general.

Transient errors eligible for retry have been expanded to include network errors, timeouts, 5xx HTTP responses and 429 status codes. After 3 failed retries, a descriptive exception will be raised instead of returning empty content or None.

Default response parsing will assume the API returns a direct list of product dictionaries with id, name and price fields. Only these three fields will be retained in the final output. The function will be named get_filtered_products, with bearer token as a required parameter and optional custom API endpoint.

The retry loop logic has been finalized: it will run up to 3 times, with exception handling covering both HTTP errors and invalid JSON responses. Only unrecoverable errors will trigger an exception after all retries are exhausted.

I confirm json.JSONDecodeError (a standard library exception) can be caught without extra dependencies. I’ll add comments to handle cases where the parsed JSON is not a list, and the exponential backoff delay will be calculated as base * (2 ** attempt) with a 1-second base delay.

The retry delay calculation logic has been verified to fit the 3-attempt workflow, and adding jitter is optional as a future improvement. Since the user didn't specify requirements, I'll use the synchronous httpx client by default, with support for async adaptation.

I’m confirming the specific implementation details for the core logic: I can either use httpx.get directly or create an httpx client instance, with the latter being more efficient and allowing one-time timeout configuration. I’ve finalized the 10-second timeout setting and the construction logic for the authentication header. For product filtering, I’ll use the get method to avoid KeyError when the price field is missing, and I can add optional validation for non-numeric price values as an extra improvement. I’m now working on the field extraction logic for the final output.
