# GPT-4.1 — content_verificable/audiencia_que_ya_sabe

- model_id: `gpt-4.1`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 5.216s | tokens_per_second: 68.3
- input_tokens: 102 | output_tokens: 356
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en soluciones prácticas, siendo altamente útil para la audiencia experta.

## Respuesta completa

Seguro, aquí tienes un texto de unas 250 palabras para tu newsletter, adaptado a tu audiencia experta en n8n:

---

¿Tu workflow devuelve “success” pero no hizo nada? Te pasa más de lo que crees. n8n, como sabes, considera que un workflow es exitoso si no hay errores explícitos lanzados, sin importar si procesó datos o no. Esto es especialmente común en workflows disparados por cron o webhooks sin payload relevante, donde a veces la lógica de entrada filtra todo y el workflow termina “limpio”... pero vacío.

El problema: si solo te fías del status, crees que todo va bien cuando, en realidad, hay workflows que llevan días sin procesar un solo item. Tus reportes muestran “0 fallos”, pero los datos nunca llegaron a destino. Un clásico: trigger de webhook esperando cierto campo, pero los requests llegan sin él, pasan por el IF y se van por la rama muerta.

Soluciones. Un truco rápido: al final del workflow, añade un nodo Function que valide si realmente hubo datos procesados (ejemplo: input.length > 0). Si no, lanza un error personalizado con throw new Error('No data processed'). Así, el workflow solo será “success” cuando realmente hizo algo útil.

Si prefieres no romper el workflow, loguéalo: usa un HTTP Request o un Send Email para avisarte cuando se ejecutó sin procesar datos. O mejor aún, envía la métrica a una base de datos o a tu sistema de monitoreo favorito.

Detectar estos “false positives” evita que tus automatizaciones se duerman en los laureles. Revisa tus workflows, ¡seguro alguno necesita este ajuste!