# Granite 4.2 8B — content_verificable/audiencia_que_ya_sabe

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 13.695s | tokens_per_second: 91.4
- input_tokens: 114 | output_tokens: 1252

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

*(~248 palabras)*

¿Alguna vez viste un workflow que aparece como *“success”* en la lista de ejecuciones… pero, en realidad, **no hizo nada visible**? No procesó datos, no envió un mensaje, no actualizó nada—y sin embargo, n8n lo marca como exitoso. Suena contradictorio, pero es más común de lo que crees, y suele pasar sin que notes el problema hasta que algo falla más adelante. Aquí va lo clave, sin vueltas ni repeticiones:

**Por qué ocurre:**  
No es un error de n8n (el motor funciona como esperado). Suele deberse a que **algún nodo en la cadena no emite datos que lleguen al siguiente nodo o a la acción final**, pero *no falla*, por lo que el workflow termina con *success*. Los casos más frecuentes:  
- Un nodo `Function` o `Set` que define variables pero **no devuelve un array/objeto con datos para el siguiente nodo** (ej.: solo `return {}` sin campos necesarios). El workflow avanza, pero nada se pasa adelante.  
- Una condición (`IF`) que evalúa `false` para el dato actual (ej.: `{{$json["status"] == "pending"}}`), por lo que el bloque *“no hago nada”* se ejecuta, pero no hay acción explícita; n8n no marca “error”, solo termina normalmente.  
- Un webhook que recibe datos, pero el primer nodo (ej.: `Function`, `SplitInBatches`, etc.) **no filtra ni procesa el payload**, dejando que el flujo caiga en un nodo que no genera salida (ej.: `Set` sin campos útiles). En este caso, el workflow “termina” sin efecto visible.

**Cómo detectarlo rápido (en menos de 2 minutos):**  
1. **Abre la ejecución en “Debug”** (no el log general). Revisa el *output* de cada nodo, nodo a nodo. Busca nodos donde el *output* sea `[]`, `{}`, o un objeto sin los campos que esperas pasar (ej.: falta `email`, `id`, etc.). Si un nodo devuelve vacío o sin datos relevantes, el siguiente nodo no recibirá nada y no actuará.  
2. **Usa el filtro rápido en el debug:** busca en el panel de salida del nodo la línea que muestra `data: {...}`. Si ves `{}` o `[]` donde debería haber valores (ej.: `{"to": "user@example.com", "text": "Hola"}`), ahí está el corte.  
3. **Verifica la condición del `IF`**: en el debug, revisa el valor real de la expresión (ej.: `{{$json["status"]}}` en el log). Si es `"draft"` y la condición busca `"pending"`, la rama “no hago nada” se ejecuta, pero no hay acción implícita. El workflow no falla; simplemente no avanza con datos.  

**Acción práctica ahora:**  
Al diseñar cualquier workflow que tenga una condición o nodo que procesa datos, **siempre revisa el *output* del primer nodo post-condición en modo Debug antes de probarlo en producción**. Pregunta simple: *“¿Qué datos reales (con valores reales, no solo estructura) llegan al siguiente nodo?”*. Si la respuesta es “nada” o “solo `{}`”, ajusta el `Set`, la función o la condición para que siempre incluya el campo necesario (ej.: `return { email: item.email, text: "Confirmación" }`). Así evitas *success sin acción* y detectas el corte en el mismo paso de prueba.

No necesitas cambiar la lógica compleja; solo confirmar el dato que pasa de un nodo a otro. Prueba esto en tu próximo workflow pequeño (ej.: webhook → IF → Send Email). Verás el output claro en Debug y evitarás perder tiempo buscando “¿por qué no se envió?” después.  

*(¡Prueba el Debug en la ejecución ahora y revisa el output del primer nodo post-condición. Así detectas el “success sin hacer nada” en 60 segundos.)*  

— Tu equipo de n8n rápido.