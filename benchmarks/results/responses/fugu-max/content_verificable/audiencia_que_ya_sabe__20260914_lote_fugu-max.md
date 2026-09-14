# Fugu Max — content_verificable/audiencia_que_ya_sabe

- model_id: `sakana/fugu-max`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 14.652s | tokens_per_second: 75.8
- input_tokens: 174 | output_tokens: 1110

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El falso positivo de `success`

En n8n, `success` suele significar algo bastante limitado: ningún nodo lanzó un error no capturado. No significa que se haya procesado algún item, que se haya escrito algo ni que el sistema destino haya aceptado el resultado.

Los falsos positivos más comunes:

- Un `IF`, `Switch` o filtro deja cero items en una rama y el workflow termina limpiamente.
- Una expresión devuelve `undefined`, `null` o una cadena vacía, y el nodo continúa con datos incompletos.
- Un `HTTP Request` recibe un `2xx`, aunque el body indique un rechazo a nivel de negocio.
- `Continue On Fail` oculta errores que luego nadie agrega ni reporta.
- La respuesta del webhook se envía antes de que termine el procesamiento, así que el cliente ve éxito aunque el flujo falle después.
- Un loop no recibe items y, por tanto, no ejecuta ninguna iteración.

La defensa más eficaz es convertir supuestos en invariantes. Después de cada etapa crítica, comprueba explícitamente:

- que el número de items sea mayor que cero;
- que existan los campos obligatorios;
- que el destino confirme la operación, no solo el transporte;
- que el número de entradas y salidas coincida cuando corresponda.

Un `Code` node que lance un error si `items.length === 0` suele ser más útil que diez logs. En operaciones críticas, valida también el body de cada respuesta y acumula los fallos para lanzar un error al final, aunque uses `Continue On Fail`.

Por último, registra métricas de negocio: items recibidos, procesados, descartados y escritos. Añade un `correlationId` y alerta por “cero procesados” o por desvíos anómalos, no solo por ejecuciones fallidas. El gráfico de ejecución ayuda a localizar ramas omitidas; los datos fijados y las ejecuciones manuales, en cambio, pueden dar una falsa sensación de cobertura.