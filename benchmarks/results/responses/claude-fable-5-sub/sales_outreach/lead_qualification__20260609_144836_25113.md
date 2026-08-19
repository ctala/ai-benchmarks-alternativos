# Claude Fable 5 (suscripción) — sales_outreach/lead_qualification

- model_id: `claude-fable-5`
- success: True  | final: 6.1 | quality: 7.2
- latency_total: 15.588s | tokens_per_second: 64.5
- input_tokens: 2 | output_tokens: 1006

## Respuesta completa

```json
[
  {
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido. No mencionó presupuesto; startup de 5 personas sugiere presupuesto limitado.",
      "authority": "Alta. Es CEO, decision maker directo.",
      "need": "Media. 'Viendo opciones' indica exploración temprana, no dolor urgente.",
      "timeline": "Indefinido. Sin fecha ni urgencia declarada."
    },
    "action": "Nurture + descubrimiento ligero",
    "reason": "Tiene autoridad total pero está en fase exploratoria sin budget ni timeline confirmados. Vale una llamada corta de descubrimiento o secuencia de email educativa. No priorizar sobre leads con urgencia, pero no descartar: en startups chicas el ciclo de decisión es rápido si el dolor se confirma."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa de 200 empleados que acaba de levantar Serie B = capital fresco disponible.",
      "authority": "Alta. VP of Operations, decisora o influencer clave del área dueña del problema.",
      "need": "Alta. Pidió demo proactivamente después del webinar; necesidad explícita.",
      "timeline": "Concreto. 'Antes de Q3' = ventana de ~3 semanas a 3 meses con deadline claro."
    },
    "action": "Agendar demo inmediata con AE senior",
    "reason": "Cumple los 4 criterios BANT con señales fuertes en cada uno. Timeline explícito + Serie B reciente = momento ideal de compra. Prioridad máxima: responder en menos de 24 horas, idealmente el mismo día."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido. El intern no controla ni conoce el presupuesto.",
      "authority": "Nula. Es intern; el decision maker es su jefe, que no está en la conversación.",
      "need": "Posible pero difusa. 'Investigar herramientas de IA' es un encargo genérico, no un problema definido.",
      "timeline": "Indefinido. Fase de research sin fecha."
    },
    "action": "Enviar material self-service y pedir intro al jefe",
    "reason": "Score bajo por falta total de autoridad y señales débiles. Pero no ignorar: enviarle el PDF de precios + un one-pager fácil de reenviar, y preguntar directamente si puede conectar con su jefe para una llamada de 15 min. El intern es un canal, no el lead real. Cero tiempo de ventas hasta que aparezca el decision maker."
  }
]
```