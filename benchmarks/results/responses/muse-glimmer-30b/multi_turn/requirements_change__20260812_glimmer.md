# Muse Glimmer 30B — multi_turn/requirements_change

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 5.33 | quality: 4.0
- latency_total: 1.871s | tokens_per_second: 55.6
- input_tokens: 242 | output_tokens: 104
- judge_score: 2.0 | justificación: La respuesta no sigue los requisitos especificados, cambiando el almacenamiento de datos a Notion y agregando notificaciones a Slack, lo que no se solicitó.

## Respuesta completa

Entendido. Entonces el flujo seria:

1. **Gmail Trigger** con filtro en el asunto para 'propuesta' o 'cotizacion'
2. **Function node** para extraer los datos del remitente
3. **Notion node** para crear una pagina con esos datos
4. **Slack node** para enviarte la notificacion

Los filtros se pueden hacer directamente en el Gmail Trigger o en un If node despues. Prefieres que te muestre la configuracion completa?