# Claude Haiku 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 10.958s | tokens_per_second: 203.9
- input_tokens: 161 | output_tokens: 2234

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Tu workflow dice "success". Eso no significa que haya hecho algo.**

En n8n, una ejecución se marca como exitosa cuando ningún nodo lanza un error. Pero "sin error" y "con trabajo hecho" no son lo mismo. Estas son las trampas más comunes:

**1. Cero items que desaparecen en silencio.** Si un nodo devuelve una lista vacía, los nodos siguientes no se ejecutan. Un IF que nunca matchea, un Filter demasiado estricto o un Google Sheets que no encontró filas terminan en verde sin haber procesado nada.

**2. "Continue On Fail" tragándose errores.** Con esta opción activa, el error viaja como item y el flujo sigue. Si nadie lo revisa después, la ejecución queda en success.

**3. HTTP 200 con payload fallido.** Muchas APIs responden 200 con `{"ok": false}` o con un array vacío. El nodo HTTP no tiene motivo para fallar.

**4. Webhooks que responden antes de procesar.** Con "Respond Immediately", la respuesta sale bien aunque el procesamiento posterior falle.

**5. Expresiones que resuelven a undefined.** Un Set o un Code node con una referencia mal escrita produce items vacíos de contenido útil, y nada lo marca.

**Cómo detectarlo**

- **Assertions explícitas:** tras cada paso crítico, un IF que valide `items.length > 0` y, si no se cumple, un nodo Stop and Error con un mensaje descriptivo.
- **Verifica el efecto, no el paso:** al final del flujo, comprueba que la fila existe, el archivo se subió o el mensaje salió. El éxito real se mide por el side effect.
- **Monitorea el volumen:** registra cuántos items procesa cada ejecución y alerta cuando caiga a cero en un flujo que históricamente tiene datos. Puedes hacerlo consultando la API de ejecuciones.
- **Error Workflow global:** conecta un Error Trigger a un flujo que notifique. Y trata cada "Continue On Fail" activo como deuda técnica que hay que justificar.

Un workflow en verde no es necesariamente un workflow correcto. Muchas veces solo es uno que no tropezó con nada que supiera reportar.