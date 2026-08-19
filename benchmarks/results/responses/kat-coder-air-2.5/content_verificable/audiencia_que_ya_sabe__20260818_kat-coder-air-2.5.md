# KAT Coder Air v2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.51 | quality: 10.0
- latency_total: 2.584s | tokens_per_second: 159.5
- input_tokens: 110 | output_tokens: 412

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



# El workflow que dice "exitoso" y no hace nada

Te ha pasado. El workflow corre, la ejecución muestra el check verde, todo luce perfecto… y al final, la acción esperada nunca ocurrió.

Esto suele deberse a uno de estos tres escenarios:

**1. Condiciones que nunca se cumplen**
Un `IF` mal configurado puede hacer que todo el branch posterior se salte silenciosamente. n8n no falla — simplemente no hay datos que procesar. Revisa los nodos previos: ¿realmente están llegando los datos esperados?

**2. Webhooks que no se disparen**
Si tu workflow depende de un webhook externo, la ejecución puede quedar "waiting" eternamente. Cuando se cierra el timeout, marca éxito porque no hubo error técnico… pero tampoco hubo acción real.

**3. Errores en nodos de tipo "Continue On Error"**
Este modo es útil, pero puede enmascarar fallos. El workflow sigue adelante como si nada, y el check verde te da una falsa sensación de seguridad.

## Cómo detectarlo

- **Habilita logs detallados** en cada nodo crítico.
- **Agrega nodos de debug** que escriban en un archivo o canal de Slack para tener evidencia de ejecución.
- **Crea un workflow de monitoreo** que revise ejecuciones recientes y te alerte cuando un workflow haya terminado en "success" pero sin datos de salida.

La automatización sin visibilidad es solo una ilusión de productividad.