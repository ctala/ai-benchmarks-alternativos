# MiMo-V2.5 (omnimodal) — content_verificable/audiencia_que_ya_sabe

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 11.866s | tokens_per_second: 49.3
- input_tokens: 107 | output_tokens: 585
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, abordando directamente el problema con soluciones prácticas y detalladas para una audiencia experta.

## Respuesta completa

**Tu workflow dice "success" y no ha hecho nada. ¿Por qué?**

Es el bug que más duele: el workflow termina verde, el webhook responde 200, tus logs dicen "completed"... pero los datos no llegaron, el email no se envió, la API externa nunca se tocó.

**Las causas más frecuentes:**

**1. El nodo anterior se saltó sin error.** El `if` no matcheó y no había rama de fallback. El `Split In Batches` terminó con un array vacío. El `Set` devolvió un objeto con las mismas claves pero valores `null`. Todo "correcto", nada procesado.

**2. El nodo de error está desactivado.** Si tienes un `Error Trigger` o un bloque `try/catch` manual, un error real se traga silenciosamente y el flujo principal reporta éxito porque técnicamente el nodo de error *sí ejecutó*.

**3. La condición del `IF` está invertida.** Pasas a la rama "false" que está vacía. El workflow "termina" sin hacer nada. Verde.

**4. La query de base de datos no falla, solo devuelve 0 filas.** Un `INSERT` con conflicto que no lanza excepción. Un `UPDATE` que afecta 0 registros. Tu nodo reporta éxito porque SQL no tiró error.

**Cómo detectarlo sin adivinar:**

- Activa **"Always Output Data"** en cada nodo crítico. Si el payload sale vacío o con estructura inesperada, lo ves al instante al inspeccionar el output.
- Añade un nodo `Noop` con un expression check al final: `{{ $json.someField }}`. Si lanza error en ejecución, tu flujo realmente no procesó nada.
- En la ejecución, revisa el **panel de outputs de cada nodo**, no solo el nodo final. El verde engaña: es el estado del nodo individual, no del propósito de tu workflow.

El fix más barato que puedes aplicar hoy: un nodo `Respond to Webhook` al final con un `{{ JSON.stringify({ processed: items.length }) }}` en el body. Si `processed` es 0, lo sabes antes de que alguien se dé cuenta.