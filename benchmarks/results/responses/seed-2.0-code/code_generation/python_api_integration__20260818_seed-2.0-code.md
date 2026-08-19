# Seed 2.0 Code — code_generation/python_api_integration

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.45 | quality: 8.48
- latency_total: 33.206s | tokens_per_second: 61.7
- input_tokens: 140 | output_tokens: 2048
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


El usuario pide una función Python con httpx, cumpla 5 puntos. Primero, voy a estructurar paso a paso.

Primero, las importaciones: necesitamos httpx, y para el backoff exponencial... Wait, el usuario dice NO dependencias externas adicionales. Oh, right, no puedo usar tenacity o algo así, tengo que implementar el backoff exponencial manualmente. También, para manejar tiempos, tal vez time.sleep.

Primero, la autenticación Bearer: el token debería ser un parámetro de la función, ¿verdad? Porque no lo hardcodees.

Punto 1: GET a la URL, Bearer token, timeout 10s. Httpx maneja timeout, se puede pasar como parámetro, o en el cliente.

Punto 2: Filtrar precio > 100. Ojo, ¿el precio es número? Tal vez haya que validar que sea int o float, por si la API devuelve string? Pero bueno, suponer que es numérico, pero tal vez manejar TypeError?

Punto 3: Lista de dicts solo con id, name, price. Así que para cada producto filtrado, extraer solo esas claves. Ojo, ¿qué pasa si alguna clave falta? Tal vez manejar KeyError? Pero el usuario no lo especifica, pero tal vez incluir un chequeo o usar get con None? Wait, el usuario dice retornar esos campos, así que suponer que la API los devuelve, pero tal vez manejar excepciones por clave faltante?

Punto 4: Manejar errores de red y timeout. Httpx tiene excepciones específicas: httpx.NetworkError, httpx.TimeoutException, también httpx.HTTPStatusError por códigos 4xx/5xx? El usuario dice errores de red y timeout, pero tal vez manejar también errores HTTP? Wait, el punto 4 dice "errores de red y timeout (10 segundos)", pero el retry debería aplicar a cuáles?

Punto 5: Retry con backoff exponencial, max 3 intentos. Backoff exponencial: usualmente 2^intento * algo, por ejemplo 1s, 2s, 4s para 3 intentos (porque 3 intentos: primer intento sin espera, segundo después de 1s, tercero después de 2s? Wait, no: max 3 intentos = 1er intento, si falla reintento 2 con backoff, luego reintento 3 con más backoff. El backoff exponencial: base 2, por ejemplo, delay = (2 ** (intento_actual - 1)) * 0.5? O base 1, pero mejor que sea exponencial. También, hay que decidir en qué excepciones reintentar: errores de red, timeout, tal vez 5xx (errores de servidor) pero no 4xx (errores de cliente, como token inválido).

Ahora, implementar el retry SIN dependencias externas: usar un bucle for que corra hasta max_retries (3), y en cada iteración, intentar la petición, si es exitosa romper el bucle, si es una excepción que se puede reintentar, esperar el backoff, sino lanzar la excepción.

Primero, las excepciones de httpx que queremos reintentar: httpx.NetworkError (problemas de red: DNS, conexión rechazada, etc.), httpx.TimeoutException (timeout), httpx.HTTPStatusError con código 5xx (porque 4xx es error del cliente, como token malo, no se reintenta).

Ahora, la estructura de la función:

- Nombre: tal vez obtener_productos_filtrados, o algo así.
- Parámetros: bearer_token (obligatorio, porque es la autenticación), max_retries=3 (por defecto 3), timeout=10 (por defecto 10s).
- Pasos:
  1. Configurar el encabezado Authorization: Bearer {token}
  2. Implementar el bucle de retry:
     - Para cada intento en range(1, max_retries + 1):
       - Intentar crear un cliente httpx (o usar un contexto with httpx.Client() para manejar conexiones)
       - Hacer el GET: url, headers=headers, timeout=timeout
       - Levantar excepción si status code es 4xx/5xx: response.raise_for_status()
       - Parsear el JSON: response.json()
       - Validar que la respuesta sea una lista (porque la API devuelve lista de productos)
       - Filtrar productos donde price > 100 (ojo, validar que price sea numérico, porque si la API devuelve string como "150.50" habría que convertirlo? Tal vez intentar convertir a float, si falla, omitir el producto? O lanzar error? El usuario no lo dice, pero mejor manejar para que no rompa: por ejemplo, para cada producto, obtener el precio como float, si no se puede, saltarlo)
       - Extraer solo id, name, price: para cada producto filtrado, crear un dict con esas claves. Otra vez, validar que las claves existan? Si no, tal vez omitir el producto o poner None? Mejor usar get() para evitar KeyError: {'id': producto.get('id'), 'name': producto.get('name'), 'price': producto.get('price')}
       - Si todo sale bien, retornar la lista.
     - Si hay excepción:
       - Verificar si es una excepción que se puede reintentar (NetworkError, TimeoutException, o HTTPStatusError con 5xx)
       - Si es el último intento, lanzar la excepción
       - Si no, calcular el backoff exponencial: por ejemplo, delay = 2 ** (intento - 1) * 0.5? Wait, el primer intento no hay espera, el segundo intento (intento=2) espera 2^(1) * 0.5 = 1s, el tercero (intento=3) espera 2^(2)*0.5=2s. Eso es backoff exponencial.
       - Esperar el delay con time.sleep(delay)
- Manejo de errores:
  - Errores de red: httpx.NetworkError
  - Timeout: httpx.TimeoutException
  - Errores HTTP: httpx.HTTPStatusError (por ejemplo, 401 Unauthorized si el token es malo, no se reintenta)
  - Errores al parsear JSON: ValueError? Porque response.json() lanza json.JSONDecodeError, que es subclase de ValueError.
  - También, si la respuesta no es una lista: TypeError?

Wait, el usuario dice "no dependencias externas adicionales" más httpx, así que usamos la librería estándar: time, json (aunque httpx parsea json por su cuenta).

Ahora, detalles importantes:

- Autenticación Bearer: el encabezado es {'Authorization': f'Bearer {bearer_token}'}
- Timeout: en httpx, el timeout se puede pasar como un número float (segundos) o como un objeto httpx.Timeout para más control, pero el usuario dice timeout 10 segundos, así que pasar timeout=10.0 al método get o al cliente.
- Retry: max 3 intentos. Ojo: el primer intento es el intento 1, luego reintento 2, luego reintento 3. Si los 3 fallan, se lanza la excepción.
- Backoff exponencial: ¿qué base? Usualmente base 2, sin jitter? El usuario no menciona jitter, así que no lo agregamos, pero tal vez comentarlo? Pero el usuario pide exactamente lo que dice, así que backoff exponencial simple: delay = 2 ** (current_attempt - 1) * 1? Wait, por ejemplo, intento 1: no espera, intento 2: 2^(1) = 2s, intento 3: 2^(2) =4s. Eso es exponencial. O tal vez 1s, 2s, 4s para 3 intentos (porque 3 intentos: 1er sin espera, 2do 1s, 3ro 2s: 2^(0), 2^(1)). Depende de cómo se cuente. Mejor definir que para el reintento N (después del primer fallo), el delay es 2^(N-1) segundos. Por ejemplo:
  - Intento 1: falla, es el primer fallo, reintento 2 después de 2^(0) = 1s
  - Intento 2: falla, segundo fallo, reintento 3 después de 2^(1) = 2s
  -