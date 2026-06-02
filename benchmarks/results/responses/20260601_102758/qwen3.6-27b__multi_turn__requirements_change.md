# Qwen 3.6 27B base (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 5.11 | quality: 4.53
- latency_total: 36.462s | tokens_per_second: 56.2
- input_tokens: 233 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta cambia los requisitos originales sin justificación, introduciendo herramientas y funcionalidades no solicitadas, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

Entendido. Cambiar a **Notion**, añadir **filtrado por palabras clave** y una **notificación a Slack** hace el flujo más útil y profesional. Te dejo la arquitectura exacta y la configuración nodo a nodo para N8N (v1.x+).

---

### 🧱 Estructura del Workflow
```
Gmail Trigger
      ↓
IF (Filtro: "propuesta" o "cotización" en asunto