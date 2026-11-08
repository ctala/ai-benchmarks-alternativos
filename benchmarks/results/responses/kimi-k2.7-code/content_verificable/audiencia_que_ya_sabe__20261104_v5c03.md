# Kimi K2.7 Code — content_verificable/audiencia_que_ya_sabe

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 14.089s | tokens_per_second: 44.4
- input_tokens: 119 | output_tokens: 626

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow que termina en verde no siempre está vivo. En n8n, *success* solo significa que ningún nodo explotó, no que tu lógica haya corrido. Y ese detalle es el agujero negro que traga horas de debugging.

El escenario clásico: tu webhook recibe un payload, un IF evalúa una condición, todos los items van por la rama "false" y el workflow acaba sin tocar nada más. O una query de Airtable/Notion/SQL devuelve cero registros, pero como no hay error, la ejecución aparece como *successful*. O peor: un Code node filtra a mano, pierde items en silencio y tú crees que todo salió bien.

Para detectarlo, no mires el estado de la ejecución; mira el volumen de datos. Al final del flujo, añade un Set node que cuente items (`items.length`) y un IF que verifique si el resultado esperado es cero. Si lo es, dispara una alerta o un Stop and Error para forzar el fallo. En workflows de sincronización, compara siempre el count de origen contra el de destino: si entraron 120 y salieron 0, algo va mal aunque el nodo esté sonriente.

Otra táctica útil: nunca dejes una rama vacía. Si un IF divide el flujo, conecta ambas ramas a algo que registre qué pasó, aunque sea un No Operation node con un nombre descriptivo como `skipped_empty_payload`.

En resumen: trata el *success* como un mínimo, no como una garantía. Diseña tus workflows para que fallen cuando no hagan lo que deben.