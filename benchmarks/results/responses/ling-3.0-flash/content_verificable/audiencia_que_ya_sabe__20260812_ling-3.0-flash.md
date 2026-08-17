# Ling 3.0 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.3s | tokens_per_second: 264.2
- input_tokens: 123 | output_tokens: 872
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando directamente el problema y proporcionando soluciones prácticas.

## Respuesta completa

## Tu workflow terminó con éxito. ¿Y luego qué?

Te ha pasado: miras la ejecución, todo verde, `Success`, y… no pasó nada. No se envió ningún email, no se creó ningún registro, no se tocó ninguna API externa. El workflow hizo exactamente lo que no querías que hiciera: nada.

Esto no es un error. Es un vacío lógico, y en n8n es más común de lo que sugiere la interfaz limpia.

**Tres causas frecuentes:**

**Ramas muertas.** Un Switch o un IF evalúa una condición y la ruta "falsa" no tiene ningún nodo conectado. La ejecución fluye, no choca con nada, y termina limpia. El workflow funcionó perfectamente… por el camino que no importaba.

**Cero items.** Un Code node filtra todos los elementos, o un nodo upstream devuelve un array vacío porque el webhook recibió un payload inesperado. Todo downstream procesa cero elementos. Cero errores. Cero acciones. Éxito total.

**Continue On Fail silencioso.** Un nodo crítico falla, pero tiene "Continue On Fail" activado, y el error se traga sin que nadie lo sepa. El flujo sigue y termina en green como si nada.

**Cómo detectarlo:**

- Mete un nodo Code después de cada punto crítico que logue `items.length`. Si es cero, algo se perdió.
- Usa el Execution Data Viewer para rastrear qué rama tomó realmente la ejecución. No confíes solo en el grafo simplificado.
- Añade un nodo de validación explícito: si el dataset está vacío, lanza un error o un webhook a un canal de alertas (Telegram, Slack, lo que sea).
- Si usas webhooks, loggea el payload crudo en un nodo antes de procesarlo. Los formatos cambian sin aviso.

El problema no es que falle. Es que *parece* que no falló.