# Qwen 3.6 Max — agent_capabilities/agent_team_delegation

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.86 | quality: 9.6
- latency_total: 76.807s | tokens_per_second: 39.6
- input_tokens: 1152 | output_tokens: 3045
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría implementar directamente.

## Respuesta completa

📋 **Plan de Ejecución Coordinado**

Antes de delegar, te presento el flujo de trabajo estructurado para garantizar calidad y respetar dependencias:

| Fase | Agente | Tarea | Dependencia | Prioridad |
|------|--------|-------|-------------|-----------|
| 🔍 1 | `researcher` | Análisis de 3 competidores + insights de diferenciación | Ninguna (punto de partida) | High |
| ✍️ 2 | `writer` | Copy completo (Hero, Features, Pricing, CTA) | Requiere entregable del researcher | High |
| 🎨 3 | `designer` | Assets visuales (Hero + Features) | Requiere insights del researcher + tono del writer | High |
| 💻 4 | `coder` | HTML/CSS responsive e integración de contenido | Requiere copy + assets finales | High |
| ✅ 5 | `reviewer` | QA integral (copy, código, diseño, responsive, SEO básico) | Requiere entregables de writer, designer y coder | High |

🔗 **Gestión de dependencias:** Cada agente recibirá en su contexto instrucciones explícitas sobre qué entregables debe esperar y cómo integrarlos. Coordinaré la entrega secuencial y validaré los handoffs antes de avanzar a la siguiente fase.

---

🚀 **Delegando tareas al Agent Team:**

