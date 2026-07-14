# Llama 3.3 70B — multi_turn/requirements_change

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 6.3 | quality: 6.0
- latency_total: 6.93s | tokens_per_second: 44.6
- input_tokens: 268 | output_tokens: 309
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en un Google Sheet, en su lugar sugiere usar Notion, lo que la hace irrelevante y poco precisa en el contexto dado.

## Respuesta completa

Entendido, te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
   - Configuración: Filtrar emails que contengan 'propuesta' o 'cotización' en el asunto.

2. **Filtro**: IF node para asegurarnos de que solo emails con 'propuesta' o 'cotización' en el asunto continúen.
   - Condición: `{{ $json.asunto.toLowerCase().includes("propuesta") || $json.asunto.toLowerCase().includes("cotizacion") }}`

3. **Extraer datos**: Function node para parsear remitente, asunto, fecha.
   - Código: Extraer los campos deseados del email y asignarlos a variables.

4. **Guardar en Notion**: Notion node (Create Page) para agregar los datos como una nueva página.
   - Configuración: Seleccionar la base de datos de Notion y el tipo de página. Mapear los campos extraídos con los campos de la página de Notion.

5. **Notificación a Slack**: Slack node (Send Message) para enviar una notificación cuando se reciba un email que coincida con el filtro.
   - Configuración: Seleccionar el canal de Slack y personalizar el mensaje con los datos del email.

Quieres que te proporcione ejemplos de configuración para cada nodo o código de ejemplo para el Function node?