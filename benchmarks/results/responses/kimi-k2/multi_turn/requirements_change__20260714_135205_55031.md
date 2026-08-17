# Kimi K2 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 4.88 | quality: 4.0
- latency_total: 7.862s | tokens_per_second: 30.4
- input_tokens: 267 | output_tokens: 239
- judge_score: 3.0 | justificación: La respuesta es clara y bien estructurada, pero no cumple con el requisito original de guardar datos en Google Sheets, y añade herramientas no solicitadas como Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

Perfecto, ajusto el workflow:

**Nodos:**

1. **Gmail Trigger** → activa con emails nuevos
2. **IF node** → filtra asunto que contenga "propuesta" O "cotizacion" (case insensitive)
3. **Function o Set node** → extrae: nombre remitente, email, asunto, fecha, snippet del cuerpo
4. **Notion node** → crea página en base de datos específica
5. **Slack node** → notificación al canal que elijas

**Configuración clave:**

- En el IF: condition = string, operation = contains, value = propuesta | cotizacion (con OR)
- Notion: necesitas la database ID y mapear propiedades (título, email, fecha, etc.)
- Slack: mensaje breve tipo "Nueva propuesta de [email] - [asunto]"

¿Tienes ya la base de datos en Notion creada con las propiedades que necesitas? Eso define cómo mapeamos los campos.