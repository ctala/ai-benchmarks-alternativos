# DeepSeek V4 Flash 0731 — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 12.97s | tokens_per_second: 52.0
- input_tokens: 179 | output_tokens: 674

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El workflow responde `success`. El webhook recibe su 200. Todo parece perfecto… hasta que revisas la base de datos y no hay ni un registro nuevo.

Lo que ocurre es más común de lo que parece: el nodo de respuesta se ejecuta antes de que el resto del flujo haga algo útil. O peor: una condición que creías correcta descarta todos los items en silencio. El workflow termina, pero no procesó nada.

El problema no es la lógica, es la falta de visibilidad.

**Cómo detectarlo antes de que te muerda:**

1. **Mira el execution list, no el status.** Un `success` solo significa que el flujo llegó al final sin errores. Entra en la ejecución y revisa nodo por nodo: ¿cuántos items entraron en cada paso? Si un nodo recibe 5 y emite 0, ahí está tu respuesta.

2. **Pon un nodo `Set` (o `NoOp`) justo antes del nodo de respuesta final.** Ese nodo no hace nada, pero te permite inspeccionar el payload completo en el editor. Si llega vacío, ya sabes que algo se perdió antes.

3. **Activa los logs de ejecución con `executeWorkflow` o añade un nodo `Error Trigger`.** No para errores, sino para avisarte cuando un workflow termina con `success` pero con cero items procesados. Un simple IF al final que compare `$items().length` y te notifique por Telegram o Slack convierte un fallo silencioso en una alerta accionable.

El `success` es una mentira piadosa. Trátalo como lo que es: una señal de que el workflow terminó, no de que hizo su trabajo.