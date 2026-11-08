# GPT-6.1 Sol — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 9.819s | tokens_per_second: 39.4
- input_tokens: 101 | output_tokens: 387

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## «Success» no significa «trabajo hecho»

El workflow termina en verde. No hay excepciones. Pero el CRM sigue igual y el mensaje nunca llegó. En n8n, **una ejecución sin errores no demuestra que se haya cumplido el objetivo**: solo indica que no se registró un fallo técnico.

El falso positivo suele aparecer en cuatro sitios:

- **Cero ítems donde esperabas datos.** Una consulta no devuelve resultados y los nodos posteriores no tienen nada que procesar. Si ese vacío era inesperado, el verde está ocultando un problema.
- **Ramas que no se recorren.** Un IF o Switch desvía todos los ítems. La ejecución termina, pero nunca alcanza la acción que justificaba el workflow.
- **Errores absorbidos.** Configuraciones para continuar ante errores, respuestas de fallback o capturas demasiado amplias convierten un fallo en una salida aparentemente normal.
- **APIs que aceptan sin completar.** Un `200` puede incluir un error de negocio; un `202` puede confirmar únicamente la recepción. Ninguno garantiza por sí solo el resultado final.

Para detectarlo, deja de monitorizar únicamente el estado de ejecución y **define condiciones de éxito de negocio**.

¿Cuántos registros debían actualizarse? ¿Cuántos se actualizaron realmente? ¿Qué identificador devuelve la operación? ¿Puedes consultar después el estado persistido?

Añade comprobaciones en los puntos críticos: volumen mínimo esperado, campos obligatorios, rama alcanzada y confirmación del cambio. Si una condición imprescindible no se cumple, genera un fallo explícito —por ejemplo, con Stop And Error— o una alerta con contexto suficiente para investigar.

No conviertas cualquier vacío en error: distingue «no había trabajo» de «el trabajo desapareció».

**El verde describe la ejecución. La verificación demuestra el resultado.**