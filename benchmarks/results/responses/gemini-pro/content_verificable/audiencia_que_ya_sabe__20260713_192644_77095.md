# Gemini 2.5 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 23.823s | tokens_per_second: 87.5
- input_tokens: 93 | output_tokens: 2085
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, ofreciendo una solución práctica para detectar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

Claro, aquí tienes una propuesta.

**Asunto:** El 'Success' que te está mintiendo

---

Ese momento de pánico. Revisas tus ejecuciones, todo en verde, pero el CRM está vacío y nadie recibió la notificación en Slack. El log dice 'Success', pero sabes que algo no fue como debía. ¿Te suena?

La causa es casi siempre la misma: el workflow finalizó... correctamente. No hubo errores de sistema, ni APIs caídas, ni credenciales incorrectas. La ejecución simplemente siguió una rama lógica (generalmente desde un nodo `IF`) que no tenía ninguna acción al final. Para n8n, un camino que termina sin errores es un éxito, aunque no haya movido ni un solo dato.

Estos "éxitos silenciosos" son peligrosos.

**Cómo detectarlos y convertirlos en información útil:**

La solución no es llenar esas ramas vacías con nodos `NoOp`. La práctica recomendada es usar el nodo `Error` de forma deliberada.

1.  Conecta la salida 'false' de tu `IF` (o cualquier otra rama sin acción) a un nodo `Error`.
2.  Configúralo con un mensaje descriptivo: "No se encontraron nuevos leads para procesar" o "Condición de filtro no cumplida".

Ahora, en lugar de un 'Success' engañoso, obtendrás un 'Failed' explícito que te dirá exactamente por qué no se procesó nada. Podrás filtrar tus ejecuciones por estado 'Failed' y ver de un vistazo solo lo que requiere tu atención.

Este simple cambio transforma fallos silenciosos en alertas accionables, dándote un control real sobre tus automatizaciones y ahorrándote sustos a primera hora de la mañana.

Feliz automatización.