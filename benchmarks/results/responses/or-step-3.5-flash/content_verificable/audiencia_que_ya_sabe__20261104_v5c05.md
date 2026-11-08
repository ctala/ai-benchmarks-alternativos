# Step 3.5 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 9.08 | quality: 10.0
- latency_total: 14.207s | tokens_per_second: 77.7
- input_tokens: 113 | output_tokens: 1104

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**¿Tu workflow de n8n dice "Success" pero no pasó nada? No estás solo.**

Es uno de los comportamientos más confusos (y comunes) en automatizaciones: ves el check verde, revisas la ejecución y… el output está vacío, no se creó el registro, no se envió el email. El workflow técicamente *terminó sin errores*, pero su efecto real fue nulo. ¿Por qué?

**Los culpables más frecuentes:**

1.  **Condiciones que nunca se cumplen:** Tu nodo `IF` o `Switch` evaluó una expresión que, con los datos reales que llegaron, siempre fue `false`. El workflow siguió la rama "no" (o ninguna), que a menudo no tiene salida visible. **Éxito = 0 acciones ejecutadas en la rama activa.**
2.  **Webhook/Trigger "silencioso":** Un webhook recibió una petición, pero el payload venía vacío o con una estructura inesperada. Los nodos posteriores procesaron "nada" sin lanzar errores.
3.  **Nodes deshabilitados o con errores capturados:** Un nodo está desactivado, o un error en un nodo fue capturado por un `Catch Error` y manejado con una simple notificación, sin detener el flujo.
4.  **Filtros previos agresivos:** Un `Filter` o `Set` modificó los datos de forma que el siguiente nodo no tenía nada que hacer (ej.: una lista quedó vacía).

**Cómo detectar estas "ejecuciones fantasma":**

*   **Revisa la pestaña "Executions" con lupa:** No te fíes solo del estado. Haz clic en la ejecución y **examina cada nodo**. ¿El `IF` tomó la rama "false"? ¿Un nodo `HTTP Request` devolvió un array vacío? El output de cada nodo es tu evidencia.
*   **Añade un "nodo centinela":** Al final de cada rama lógica importante (especialmente las `false`), añade un nodo `Set` o `Function` que **fuerce un output reconocible** (ej.: `{ "ram": "no_action", "reason": "condition_failed" }`). Así, en la ejecución verás siempre un rastro.
*   **Logea las decisiones clave:** Usa el nodo `No Operation` (solo para logging) o un `Telegram/Slack` en las ramas críticas. Un mensaje como "`[Workflow X] Rama principal: condición false. Payload: {…}`" te salvará horas.
*   **Prueba con datos reales:** El editor de n8n es engañoso. Prueba tus webhooks/crons con payloads y schedules reales. Lo que funciona con datos de ejemplo puede fallar con datos reales.

**Conclusión:** Un "Success" solo garantiza que *n8n no se cayó*. No garantiza que *tu negocio* avanzara. Tu responsable es el **output de los nodos finales**, no el estado global. Vigila esos datos, y si una ejecución no produce un output modificado (un registro, un archivo, un mensaje), es una ejecución vacía. Añade notificaciones para esos casos.

¿Has pillado ya alguna "ejecución fantasma" esta semana?