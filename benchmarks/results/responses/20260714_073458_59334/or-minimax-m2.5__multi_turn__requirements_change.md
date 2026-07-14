# MiniMax M2.5 — multi_turn/requirements_change

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.79 | quality: 8.0
- latency_total: 5.481s | tokens_per_second: 52.9
- input_tokens: 228 | output_tokens: 290
- judge_score: 3.0 | justificación: La respuesta es clara y bien organizada, pero no cumple con los requisitos originales de guardar datos en Google Sheets, y en su lugar sugiere Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

Perfecto, mucho mejor. Te explico los 4 nodos que necesitas:

## 1. Gmail Trigger
- Configura tu cuenta de Gmail
- Selecciona la bandeja de entrada

## 2. Filter (nodo de N8N)
- Campo: `subject`
- Operation: `contains` (o `matches regex`)
- Value: `propuesta|cotizacion` (puedes usar regex para ambos)

## 3. Notion (Create Page)
- Conecta tu integración de Notion
- Selecciona la database donde quieres guardar
- Mapea los campos: remitente, email, asunto, fecha

## 4. Slack (Send Message)
- Configura tu workspace
- Envía el mensaje a un canal o a ti mismo
- Incluye los datos del email en el mensaje

---

¿Quieres que te pase el JSON del workflow completo para que lo importes directo? Solo dime:
1. Qué campos exactos quieres guardar en Notion
2. A qué canal de Slack quieres la notificación