# Claude Opus 5.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 10.873s | tokens_per_second: 82.4
- input_tokens: 161 | output_tokens: 896

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El verde que miente

Lo has visto: ejecución en verde, cero errores y, al día siguiente, alguien pregunta por qué no llegó nada al CRM. n8n no mintió. Reportó exactamente lo que pasó: nada falló. El problema es que **nada falló porque nada se ejecutó**.

**Las causas habituales:**

- **Cero items.** Si un nodo devuelve una lista vacía, los nodos siguientes simplemente no corren. Para n8n eso es un final válido, no un error. Una API con credenciales a medio caducar que responde `[]` te deja exactamente así.
- **200 con error dentro.** Muchas APIs devuelven `{"status":"error"}` con código 200. El nodo HTTP lo da por bueno.
- **Un IF que manda todo a la rama equivocada.** Si cambió un campo upstream (`email` pasa a ser `Email`), la condición evalúa a false para todo y el flujo termina limpio por la rama muerta.
- **On Error → Continue.** Lo activaste para un caso concreto y ahora se traga fallos que sí importaban.

**Cómo detectarlo:**

1. **Valida volumen.** Tras los nodos críticos, añade un IF que compruebe `{{ $input.all().length }}`. Si es 0 cuando no debería, conéctalo a un **Stop and Error**. Así conviertes el silencio en un fallo real y tu Error Workflow lo captura.
2. **Valida el contenido, no el status code.** Revisa el body de la respuesta antes de continuar.
3. **Dead man's switch.** Al final del flujo, haz un ping a un servicio tipo Healthchecks. Si el ping no llega, te avisa ese servicio, no n8n. Es la única forma de cazar el workflow que ni siquiera arrancó.
4. **Audita cada `Continue`.** Si no sabes por qué está activado, desactívalo.

Un success sin evidencia del trabajo hecho no demuestra nada.