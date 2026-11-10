# Qwen 3.7 Flash — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 8.12 | quality: 8.5
- latency_total: 10.08s | tokens_per_second: 74.7
- input_tokens: 655 | output_tokens: 753
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, explicando adecuadamente las limitaciones del sistema y ofreciendo una sugerencia práctica para el usuario.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

Actualmente no dispongo de herramientas que permitan buscar facturas por nombre de cliente, filtrar por estado de pago (como "impagas") ni ordenar resultados por monto. 

Los únicos sistemas disponibles son:
- 🔍 `buscar_cliente`: busca información básica y estado de cuenta de un cliente por nombre o email.
- 📄 `buscar_factura`: solo consulta una factura específica cuando ya conoces su número (formato F-0000).
- 💰 `emitir_factura`: crea nuevas facturas.
- ⏰ `enviar_recordatorio_pago`: envía recordatorios de facturas ya emitidas (requiere el número exacto).

Si tienes el número concreto de alguna factura, puedo consultarla directamente. Si necesitas un listado de facturas impagas ordenadas, te recomendaría revisar esa funcionalidad desde tu panel administrativo o CRM, ya que está fuera del alcance de las herramientas que tengo activas en este momento. ¿Necesitas ayuda con algún otro proceso específico?