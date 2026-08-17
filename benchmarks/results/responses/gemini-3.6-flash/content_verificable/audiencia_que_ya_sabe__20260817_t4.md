# Gemini 3.6 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 11.051s | tokens_per_second: 148.8
- input_tokens: 93 | output_tokens: 1644

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Asunto:** El engaño del tick verde en n8n 🟩

Llegas al panel de ejecuciones, ves todo en verde y te vas a tomar un café. Sin embargo, a los diez minutos te cae un ticket: *"Los leads de hoy no están entrando al CRM"*.

¿Te suena? Has caído en el clásico falso positivo. En n8n, que una ejecución termine en *success* solo significa que ningún nodo lanzó una excepción no controlada, no que el workflow haya hecho su trabajo.

**¿Por qué ocurre esto?**

1. **Arrays vacíos (`[]`):** Si un *HTTP Request* o un nodo de base de datos no encuentra datos, devuelve un array de longitud 0. En n8n, 0 ítems significa que los nodos posteriores no tienen nada que iterar y se omiten. El workflow finaliza en verde sin haber procesado nada.
2. **APIs con "falso 200":** Servicios (como GraphQL o APIs legacy) que devuelven un código `HTTP 200 OK`, pero con un payload tipo `{"success": false, "data": null}`. Para n8n la petición fue correcta.
3. **Ramas muertas:** Nodos *If* o *Switch* que envían los datos a una salida sin nodos conectados, finalizando la ejecución silenciosamente.

**Cómo detectarlo y evitarlo:**

* **Data Guards:** Coloca un nodo *If* tras tus fuentes de datos y valida la longitud del payload: `$input.all().length > 0`. 
* **Forzar el fallo:** Si recibir 0 ítems es un comportamiento anómalo, redirige la falsa salida a un nodo *Stop and Error*. Esto pintará la ejecución de rojo y disparará tu *Error Trigger* global.
* **Validación de Schema:** No te fíes del status HTTP. Usa nodos *Filter* o *Code* para comprobar la presencia de claves críticas en el JSON antes de mutar datos aguas abajo.

No confíes en el verde por defecto. En automatización avanzada, la ausencia de datos debe tratarse con la misma rigurosidad que un error de sintaxis.