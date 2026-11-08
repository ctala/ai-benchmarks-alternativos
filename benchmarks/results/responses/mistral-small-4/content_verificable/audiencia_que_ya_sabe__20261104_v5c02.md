# Mistral Small 4 — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.49 | quality: 10.0
- latency_total: 2.847s | tokens_per_second: 162.6
- input_tokens: 117 | output_tokens: 463

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**¿Por qué tu workflow en n8n dice "success" pero no hizo nada?**

Si trabajas con n8n a diario, seguro te ha pasado: un workflow termina con estado *Success*, pero al revisar los logs o los datos, no hay rastro de lo que debería haberse ejecutado. **¿Magia?** No. Aquí te explico por qué pasa y cómo detectarlo antes de que te vuelva loco.

1. **Nodes que no disparan nada (pero no fallan)**
   Algunos nodos, como *HTTP Request* con método HEAD o *Webhook* sin payload, pueden devolver 200/204 sin procesar datos. Revisa que los nodos *tengan* datos de entrada y salida (usa *Debug* o *Set* para forzar valores).

2. **Condicionales que no se cumplen**
   Un *IF* con una condición mal escrita (ej: `{{ $json.value }} == "true"` en lugar de `{{ $json.value == "true" }}`) siempre devolverá falso, pero no generará error. **Solución:** Usa *Expression* en el campo de condición y valida con *Function* o *Code* si la lógica es compleja.

3. **Cron o Webhook sin payload**
   Si tu workflow depende de un *trigger* externo y no recibe datos (ej: webhook sin cuerpo), los nodos aguas abajo no se ejecutarán. **Verifica:** Añade un *Set* al principio para forzar datos de prueba o revisa los headers en el *Webhook*.

4. **Errores silenciosos en nodos**
   Nodos como *Read Binary File* o *Google Sheets* pueden devolver *Success* incluso si no encontraron el archivo o la fila. **Debug:** Usa *Item Lists* para ver el estado de cada nodo en detalle.

**Bonus:** Activa *Log Streaming* en tu instancia de n8n para ver en tiempo real qué nodos procesan datos (o no). Si ningún nodo muestra *Processed Item*, tu workflow no hizo nada.

¿Te ha pasado? Comparte tu caso en los comentarios. 👇