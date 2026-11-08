# Gemma 4 31B — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 7.197s | tokens_per_second: 51.1
- input_tokens: 111 | output_tokens: 368

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Aquí tienes una propuesta directa, técnica y al grano.

***

**Título: El peligro del "Success" vacío**

Si trabajas con n8n a diario, sabes que un check verde al final de la ejecución es tranquilizador. Pero hay un escenario peligroso: el workflow que termina en `success` sin haber procesado un solo dato.

Esto ocurre principalmente por la naturaleza de los nodos de n8n: **si un nodo recibe un array vacío, el flujo se detiene ahí.** 

Para n8n, esto no es un error. El nodo no falló; simplemente no tenía ítems que procesar. El resultado es una ejecución exitosa en el historial, pero un proceso de negocio incompleto en la realidad. Es el "silencio administrativo" de la automatización.

**Cómo detectarlo y solucionarlo:**

1.  **El nodo Filter/If:** Si filtras datos y el resultado es cero, el flujo muere. Para evitarlo, no confíes en el flujo lineal.
2.  **Wait / Merge:** Si esperas datos de un webhook que nunca llega o de un nodo que devuelve un array vacío, el resto de la cadena nunca se disparará.
3.  **La solución: El nodo "Code" de validación.** Inserta un nodo de código inmediatamente después de tu fuente de datos. Valida la longitud del array:
    `if (items.length === 0) throw new Error('No data found');`
    
Al forzar un error explícito cuando no hay datos, transformas ese `success` engañoso en un `failed`. Solo así saltarán tus alertas de monitorización y sabrás que algo falló en el origen antes de que el cliente te avise.