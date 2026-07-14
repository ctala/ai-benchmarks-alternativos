# Claude Opus 4.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 15.55s | tokens_per_second: 31.3
- input_tokens: 124 | output_tokens: 487
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una profundidad significativa con consejos prácticos, está claramente escrita y organizada, y es extremadamente útil para los emprendedores.

## Respuesta completa

# El "success" que miente: workflows que no hacen nada

Tienes un workflow que lleva semanas en verde. Cero errores, cero alertas. Todo perfecto.

Hasta que alguien pregunta por qué no se están actualizando los registros en el CRM.

Revisas. El workflow ejecuta, termina en success... y no procesa ni una sola fila.

**¿Qué pasó?**

El problema es que n8n considera exitosa cualquier ejecución que no lance una excepción. Si tu nodo HTTP recibe un 200 con un array vacío, eso es success. Si tu query a la base de datos no devuelve registros, eso también es success. Si un IF deriva todo por la rama "false" y esa rama no tiene nada conectado, success otra vez.

Success significa "no se rompió". No significa "hizo lo que esperabas".

**Tres formas concretas de cazarlo:**

1. **Nodo IF después de cada fuente de datos.** Evalúa si `$input.all().length === 0`. Por la rama true, lanza un Stop and Error con un mensaje explícito: "El endpoint X devolvió 0 items". Así el workflow falla de verdad y te enteras.

2. **Guarda métricas de cada ejecución.** Un nodo al final que escriba en una tabla o dispare un evento con el conteo de items procesados. Cuando el número sea cero tres ejecuciones seguidas, tienes un problema silencioso.

3. **No confíes solo en el status code.** Valida el body. Un 200 con `{"data": [], "error": null}` es técnicamente correcto y funcionalmente inútil. Parsea y verifica antes de seguir.

**La regla es simple:** si tu workflow no tiene al menos una validación explícita de "¿procesé algo?", no tienes monitoreo. Tienes una luz verde decorativa.