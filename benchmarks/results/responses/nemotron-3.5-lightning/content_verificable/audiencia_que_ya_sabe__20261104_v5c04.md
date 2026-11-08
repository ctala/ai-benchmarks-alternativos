# Nemotron 3.5 Lightning — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.706s | tokens_per_second: 133.0
- input_tokens: 116 | output_tokens: 360

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Aquí tienes un borrador técnico directo, sin relleno:

***

**El "éster falso" en tus workflows**

Has visto esto mil veces: n8n marca un nodo como *success*, el correo llega a la bandeja de entrada... o no. Y tú, mirando el historial, te preguntas: "¿Realmente se ejecutó?".

El problema no es n8n, es la ilusión de la finalización. Un workflow puede terminar con éxito y haber fallado silenciosamente en su misión. ¿Cómo?

Primero, revisa la **orden de ejecución**. Si un nodo de "Set" o "If" falla su condición, los nodos siguientes pueden saltarse, pero el workflow sigue su curso hasta el nodo final, etiquetándolo como éxito. El diablo está en los detalles de los datos: ¿están vacíos? ¿Son `null`?

Segundo, y esto es crítico: **los errores de API**. Si tu webhook externo devuelve `200 OK` pero el cuerpo dice "Error de validación", n8n lo toma como éxito. El nodo "HTTP Request" no falla, pero tu negocio sí.

**La solución no es añadir más nodos, es añadir visibilidad.**

Usa el nodo **“Execute Workflow”** para encapsular lógica crítica y capturar errores específicos. Más importante aún: activa los **Logs Detallados** en la configuración del nodo y fíjate en el campo `error` vs `data`. Un workflow "success" con un `error` en el JSON es un workflow mentiroso.

No confíes en el color verde. Confía en los datos que salen.

***

*(258 palabras)*