# Qwen 3.5 (Ollama Cloud default) — multi_turn/requirements_change

- model_id: `qwen3.5:cloud`
- success: True  | final: 6.29 | quality: 4.4
- latency_total: 31.963s | tokens_per_second: 64.1
- input_tokens: 233 | output_tokens: 2048
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Excelente ajuste! Esa combinación (Gmail + Notion + Slack) es mucho más potente para gestión de leads o oportunidades comerciales. Notion te da una base de datos flexible y Slack te asegura reacción inmediata.

Aquí tienes la estructura optimizada del workflow en N8N.

### 📋 Prerrequisitos (Antes de empezar en N8N)

1.  **Notion:**
    *   Crea una **Base de Datos** en Notion.
    *   Asegúrate de tener las siguientes propiedades (columnas): `Nombre` (Title), `Email` (Email), `Asunto` (Text), `Fecha` (Date), `Estado` (Select - opcional).
    *   Comparte la base de datos con tu integración de Notion (Connection > Add connections > Tu workspace).
    *   Copia el **Database ID** (está en la URL de la base de datos, entre el `/` y el `?`).
2.  **Slack:**
    *   Crea un canal (ej. `#leads-email`) o usa uno existente.
    *   Necesitas un **Webhook URL** (más fácil) o configurar la **Slack App** en N