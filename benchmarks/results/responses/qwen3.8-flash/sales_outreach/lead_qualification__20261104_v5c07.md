# Qwen 3.8 Flash — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 4.3 | quality: 3.33
- latency_total: 16.017s | tokens_per_second: 34.3
- input_tokens: 262 | output_tokens: 550

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente de calificacion de leads. Evalua cada lead con un score 1-10 y decide la accion.

Framework BANT:
- Budget: tiene presupuesto?
- Authority: es decision maker?
- Need: tiene el problema que resolvemos?
- Timeline: necesita solucion pronto?

Responde en JSON: {"score": N, "bant": {"budget": "...", "authority": "...", "need": "...", "timeline": "..."}, "action": "...", "reason": "..."}

**user:**

Lead 1: Juan Perez, CEO de una startup de 5 personas. Dice que "estamos viendo opciones para automatizar nuestro soporte". No menciono presupuesto. Llego via el blog.

Lead 2: Ana Gomez, VP of Operations en empresa de 200 empleados. Pidio una demo despues de un webinar. Dijo que "necesitamos resolver esto antes de Q3". Su empresa acaba de levantar Serie B.

Lead 3: Carlos Ruiz, intern de marketing. Dice que su jefe le pidio "investigar herramientas de IA". Quiere un PDF con precios.

Califica los 3 leads.


## Respuesta completa

```json
[
  {
    "score": 5,
    "bant": {
      "budget": "Desconocido. No mencionó presupuesto.",
      "authority": "Alta. Es CEO y toma decisiones finales.",
      "need": "Media/Exploratoria. Está 'viendo opciones', lo que indica interés pero no urgencia crítica confirmada.",
      "timeline": "Indefinido. No hay fecha límite clara."
    },
    "action": "Nurturing / Calificación",
    "reason": "Tiene la autoridad (CEO) pero falta información clave sobre presupuesto y urgencia. El canal de origen (blog) sugiere una etapa temprana del embudo. Requiere seguimiento para validar BANT antes de asignar a ventas."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Acaba de levantar Serie B, tiene capital disponible.",
      "authority": "Alta. VP of Operations suele tener poder de decisión o influencia directa en la compra operativa.",
      "need": "Alta. Participación activa en webinar y solicitud de demo específica.",
      "timeline": "Urgente. Necesita resolverlo antes de Q3."
    },
    "action": "Prioridad Alta / Asignar a Ventas Inmediato",
    "reason": "Lead caliente con todos los elementos BANT presentes: dinero (Serie B), autoridad (VP), necesidad demostrada (demo request) y urgencia temporal (Q3 deadline). Máxima probabilidad de cierre rápido."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Inexistente. Un intern no gestiona presupuestos.",
      "authority": "Baja. Solo es un investigador, no el decisor.",
      "need": "Baja/Indirecta. Cumple una tarea de su jefe, no tiene dolor propio validado.",
      "timeline": "Desconocido/Irrelevante. Su timeline depende de cuando su jefe revise la investigación."
    },
    "action": "Descartar o Enviar a Base de Datos de Nurturing",
    "reason": "No cumple con Authority ni Budget. Es un lead de baja calidad para ventas directas. La mejor acción es enviarle recursos educativos (PDFs) y esperar a que el decisor real contacte, o marcar como 'no cualificado' para evitar desperdiciar tiempo del equipo comercial."
  }
]
```