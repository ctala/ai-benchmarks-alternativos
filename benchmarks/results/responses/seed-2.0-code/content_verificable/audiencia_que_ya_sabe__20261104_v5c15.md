# Seed 2.0 Code — content_verificable/audiencia_que_ya_sabe

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 29.266s | tokens_per_second: 84.4
- input_tokens: 133 | output_tokens: 2469

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

### Asunto: Tu workflow de n8n marcó SUCCESS? No confíes (aún)
( ~245 palabras )

Ayer pasaste 20 minutos revisando tu workflow de sincronización de leads de Shopify a HubSpot: marcó 12 ejecuciones SUCCESS en las últimas 2h, pero HubSpot no tenía ni un registro nuevo. Te suena? Es el fallo más silencioso de n8n, y afecta a workflows sin errores explícitos.

Las causas son específicas (no son fallos de lógica básica):
1. Split en modo «Pass All» sin condiciones coincidentes: pasa 0 items, n8n no tira error (porque no hubo excepción).
2. Nodo HTTP con «Ignore Response Status Code» activado: un 404/403 por límite de API no se registra como fallo.
3. Filtro de items (en nodo Filter o en el trigger de Cron con filtros de fecha) que devuelve 0 resultados: n8n marca success por defecto.

Cómo detectarlo (sin revisar logs manualmente):
- Pon un nodo Code DESPUÉS del filtro/split principal: `if ($input.all().length === 0) throw new Error("Sin items procesados");` (forza un fallo visible en el panel de ejecuciones).
- Activa «Fail Workflow on Empty Items» en nodos con filtros (está en Opciones Avanzadas, pero no es global: el Code es solución universal).
- Usa el Error Trigger + Slack/email para alertarte de estos fallos forzados.

Hoy revisa tus 2 workflows más críticos (ej: sincronización de pagos, envío de facturas): ¿tienen validación de items procesados?