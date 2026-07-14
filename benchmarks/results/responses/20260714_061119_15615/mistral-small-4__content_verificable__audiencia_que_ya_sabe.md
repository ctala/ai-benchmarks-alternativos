# Mistral Small 4 — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.35 | quality: 10.0
- latency_total: 4.926s | tokens_per_second: 88.3
- input_tokens: 117 | output_tokens: 435
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando el problema específico con soluciones prácticas.

## Respuesta completa

**¿Por qué tu workflow dice *success* pero no hizo nada?**

Si trabajas con n8n a diario, seguro te has topado con este escenario: el workflow termina con estado *success*, pero al revisar los logs… nada. No hubo errores, no se procesaron datos, pero tampoco saltó ninguna alerta. ¿Qué está pasando?

El problema suele estar en **tres causas comunes** que n8n no siempre reporta con claridad:

1. **Webhooks que no llegaron**
   Un webhook puede marcarse como recibido (*"webhook received"*) incluso si el payload está vacío o corrupto. Si tu workflow depende de datos externos (ej: una API que falló silenciosamente), n8n no generará error si no hay validación explícita. *Solución:* Añade un nodo de *Set* para verificar el payload antes de procesarlo.

2. **Nodos "sin salida" que no fallan**
   Algunos nodos (como *HTTP Request* o *Function*) pueden devolver *success* aunque no ejecuten la acción. Ejemplo: Si un *IF* evalúa una condición que nunca se cumple, n8n no lo marca como error. *Solución:* Usa *Assert* o *Error Trigger* para forzar fallos controlados.

3. **Cron o triggers que no dispararon**
   Si un workflow se ejecuta por cron pero la condición de tiempo no se cumple (ej: zona horaria mal configurada), n8n no generará error. *Solución:* Loguea el timestamp de inicio en un nodo *Set* y compáralo con el esperado.

**Bonus:** Activa el *Execution Log* detallado en n8n (ajusta en *Settings > Execution Log*) para ver qué nodos realmente se ejecutaron. La diferencia entre *"ejecutado"* y *"procesado"* suele ser la clave.

¿Te ha pasado? Comparte tus casos en los comentarios—seguro no eres el único frustrado con estos falsos positivos. 🚀