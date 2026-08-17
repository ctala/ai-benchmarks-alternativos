# Gemini 2.5 Pro — multi_turn/requirements_change

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 6.61 | quality: 7.16
- latency_total: 18.467s | tokens_per_second: 110.4
- input_tokens: 206 | output_tokens: 2038
- judge_score: 4.0 | justificación: 

## Respuesta completa

¡Excelente cambio! Este workflow es mucho más potente y es un caso de uso muy común para automatizar la gestión de leads o clientes.

Me encanta la idea. Aquí tienes el desglose completo, nodo por nodo, para que lo construyas.

### **Visión General del Workflow**

El flujo se verá así:

`Gmail Trigger` → `IF Node` → `Notion Node` → `Slack Node`

1.  **Gmail Trigger**: Se activa cuando llega un email nuevo.
2.  **IF Node**: Revisa si el asunto contiene "propuesta" o "cotización". Si no, el workflow se detiene.
3.  **Notion Node**: Si el filtro se cumple, crea una nueva entrada en tu base de datos de Notion.
4.  **Slack Node**: Envía un mensaje a un canal específico para avisarte.

---

### **Configuración Detallada de Cada Nodo**

Aquí tienes el paso a paso.

#### **1. Nodo: Gmail Trigger (El Vigilante)**

Este nodo inicia todo el