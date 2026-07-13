# MiniMax M3 — persistencia/migracion_api_200_vacio

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.04 | quality: 6.09
- latency_total: 7.714s | tokens_per_second: 13.0
- input_tokens: 409 | output_tokens: 100

## Respuesta completa

Antes de cambiar nada, descartemos causas rápidas: verifica el `post_id` que envías, los headers de auth, y confirma con un GET directo al endpoint del post que existe y es accesible con tus credenciales. Si todo cuadra, prueba con un rango de fechas explícito usando `since` y `until` cubriendo el periodo donde se publicaron los 40 comentarios. Si con eso obtienes datos, la causa raíz es del lado del proveedor y conviene escalar.