# KAT Coder Air v2.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.45 | quality: 10.0
- latency_total: 3.353s | tokens_per_second: 169.1
- input_tokens: 110 | output_tokens: 567

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



# El fantasma del "Success" que no hace nada

Te ha pasado: el workflow termina en verde, el log dice "success", y sin embargo… nada. No se envió el email, no se actualizó el CRM, no llegó nada a ningún lado. ¿Qué pasó?

## El problema: el success es de ejecución, no de resultado

n8n marca el nodo como exitoso cuando **no lanzó una excepción**, no cuando **logró el objetivo**. Un GET a una API que responde 200 con un body vacío es un "success" para el motor. Un webhook que recibe datos, los procesa, y luego el siguiente nodo filtra todo con una condición `if`, también termina en verde… aunque el flujo real nunca se ejecutó.

Los casos más comunes:

- **Webhooks con filtros en el primer nodo**: si la condición falla, el workflow termina inmediatamente con success y cero datos procesados.
- **HTTP Request que responde 200/204**: el código de estado es correcto, pero el payload está vacío o el recurso no existe.
- **Cron que dispara un workflow sin datos de entrada**: si no hay triggers condicionales, el flujo corre con valores nulos y los nodos siguientes los ignoran silenciosamente.
- **Nodos de tipo "Switch" o "IF" sin rama else definida**: el workflow cierra sin error, pero tampoco hace nada.

## Cómo detectarlo

1. **Añade un nodo "No Operation" o "Set" al final** que registre los datos de entrada. Si el array de items está vacío, algo filtró todo el camino.
2. **Habilita el log de ejecución paso a paso** en el panel de debug. Revisa cada nodo: si ves un "skipped" en rojo, ahí está el punto de quiebre.
3. **Revisa los webhooks con el endpoint tester** de n8n. Simula la llamada y verifica que los datos llegan al primer nodo, no solo que el webhook responde 200.
4. **Para cron jobs**, añade un condicional al inicio que verifique si hay datos reales antes de continuar. Si no, termina explícitamente con un mensaje en log.

El success de n8n no es una garantía. Es solo la ausencia de error.