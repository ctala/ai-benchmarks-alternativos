# DeepSeek V4 Pro (0813) — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 36.035s | tokens_per_second: 51.1
- input_tokens: 179 | output_tokens: 1841

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Success ≠ trabajo hecho: tu workflow pudo no haber hecho nada**

Un workflow en n8n puede terminar en verde y no haber movido un solo dato. El estado `success` solo confirma que no hubo errores no capturados, no que tu lógica de negocio se ejecutó.

Causas típicas:

- Un nodo anterior devolvió 0 ítems. Los nodos siguientes se omiten (skipped). El flujo termina `success` aunque no se hizo nada.
- Un IF o Filter eliminó todos los ítems y no construiste la rama vacía.
- Un error quedó atrapado con “Continue”: el fallo se traga y el workflow sigue como si nada.
- Un HTTP Request devolvió 204 o vacío, o un webhook llegó sin payload y no validaste.
- Un nodo está desactivado, o “Execute Node” manual no refleja la ejecución real.

Cómo detectarlo:

1. No mires solo el check verde; abre la ejecución y revisa los datos de salida de cada nodo. Busca nodos en gris/omitidos.
2. Instrumenta puntos críticos: después de cualquier filtro, agrega un IF que cuente ítems. Si `count === 0`, lanza un Stop and Error con mensaje claro.
3. Valida respuestas de HTTP/Webhook: comprueba que el body tenga campos esperados antes de continuar.
4. Si usas Continue en errores, registra con un nodo de log o incrementa un contador; así sabrás que ocurrió.

Regla: si un workflow puede terminar sin producir el efecto esperado, haz que falle explícitamente. Un success vacío es un bug en silencio.