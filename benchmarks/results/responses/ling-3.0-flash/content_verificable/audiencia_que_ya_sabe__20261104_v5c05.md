# Ling 3.0 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 31.791s | tokens_per_second: 29.3
- input_tokens: 123 | output_tokens: 933

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## Tu workflow terminó en "success"… ¿y entonces qué hizo?

Este es el bug que más tiempo me ha robado sin dar señales.

Un workflow en n8n puede devolver **success** sin haber hecho absolutamente nada. No hay error, no hay alerta, la ejecución aparece verde como un Pascua. Y mientras tanto, el proceso que debía ejecutar sigue dormido.

### Por qué pasa

La causa más frecuente es **datos vacíos que atraviesan el flujo sin disparar nada**. Un nodo Output (HTTP Request, Google Sheets, etc.) solo se ejecuta si recibe ítems. Si el nodo anterior le pasa un array vacío, simplemente lo salta. Todo el workflow sigue adelante, termina limpio y te devuelve éxito.

Otro escenario clásico: un nodo **IF** cuyas dos ramas están desconectadas, o un **Switch** que no mapea el caso real. O una sub-ejecución que termina prematuramente porque el trigger no recibió payload.

### Cómo detectarlo antes de que te coste una semana

1. **Inspecciona "Items processed"** en cada nodo de la ejecución. Si un nodo muestra 0 ítems procesados y no hay error, tienes un fantasma.
2. **Añade un nodo Set temprano** que escriba un flag: `hasData: {{$json.length > 0}}`. Si algo downstream lo cambia a `false`, ya tienes tu alerta.
3. **Pon un nodo de logging al inicio** (Telegram, Slack, un simple Set con timestamp) para confirmar que el trigger realmente recibió datos, no solo que se disparó.
4. **Revisa el grafo de ejecución**: si solo el nodo trigger aparece activo, tu workflow hizo exactamente lo que un cron sin eventos — nada.

El éxito sin acción es el silencio más caro que tienes. Apártalo.