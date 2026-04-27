# MiMo V2-Pro (Xiaomi direct) — agent_capabilities/skill_execution_complex

- model_id: `mimo-v2-pro`
- success: True  | final: 5.2 | quality: 7.28
- latency_total: 19.215s | tokens_per_second: 17.6
- input_tokens: 1309 | output_tokens: 339
- judge_score: 3.2 | justificación: 

## Respuesta completa

Voy a ayudarte con eso. Sin embargo, necesito algunos datos antes de ejecutar:

1. **Para publicar el artículo**: ¿Cuál es el link del doc compartido donde está el artículo? (Necesito la URL para usarla en el skill de publicación)

2. **Para la reunión del jueves**: 
   - ¿A qué fecha exacta te refieres con "el jueves"? (por ejemplo: 2025-01-16)
   - ¿Cuánto tiempo quieres que dure la reunión? (30 min, 1 hora, etc.)

Una vez que me des esta información, ejecutaré en secuencia:
- `publish_blog_post` para publicar el artículo
- `send_message` por Slack a @maria y @carlos con el link
- `create_calendar_event` para agendar la reunión de review