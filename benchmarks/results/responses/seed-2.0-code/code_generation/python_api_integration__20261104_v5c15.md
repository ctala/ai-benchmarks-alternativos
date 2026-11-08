# Seed 2.0 Code — code_generation/python_api_integration

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.15 | quality: 8.56
- latency_total: 4.205s | tokens_per_second: 52.3
- input_tokens: 140 | output_tokens: 220
- judge_score: 4.6 | justificación: 

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


El usuario pide una función Python con httpx, cumpliendo varios puntos. Vamos a estructurarla paso a paso.

Primero, los requisitos:
1. GET a la URL con Bearer token: Necesitamos recibir el token como parámetro, o lo pasamos? Mejor como parámetro para que sea flexible.
2. Filtrar precio >100: Después de obtener la respuesta, parsear JSON, iterar y filtrar.
3. Retornar lista de dicts con id, name, price: Extraer solo esas claves. Ojo, hay que manejar si alguna clave falta? Tal vez lanzar un error o filtrar? Mejor manejar con un try-except al extraer, o usar .get()?
4. Manejar errores de red, timeout (10s): Httpx tiene Timeout configuración, y excepciones como ConnectError, ReadTimeout, etc. También status codes HTTP (4xx