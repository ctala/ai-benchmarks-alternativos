# Mistral Large 4.0 — sales_outreach/lead_qualification

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 20.364s | tokens_per_second: 103.0
- input_tokens: 250 | output_tokens: 2098

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
    "lead": "Juan Perez - CEO Startup 5 personas",
    "score": 6,
    "bant": {
      "budget": "No mencionado. Startup early-stage (5 personas) sugiere presupuesto limitado o aún no definido para esta categoría.",
      "authority": "Alta. Es CEO/Founder, decision maker absoluto con poder de compra directo.",
      "need": "Media-Alta. Está explorando activamente ('viendo opciones'), el problema existe pero no hay urgencia expresada.",
      "timeline": "Baja-Media. Llegó vía blog (inbound orgánico), sin deadline mencionado. Puede moverse rápido si ve ROI claro."
    },
    "action": "Calificar (Discovery Call) - Enviar caso de estudio específico para startups y agendar llamada de 15 min para validar presupuesto y pain point.",
    "reason": "Buena autoridad (CEO) pero falta confirmar presupuesto y urgencia. Las startups pequeñas pueden cerrar rápido si el dolor es agudo, pero ahora está en modo investigación. No es un 'hot lead' todavía."
  },
  {
    "lead": "Ana Gomez - VP Ops Empresa 200 empleados",
    "score": 10,
    "bant": {
      "budget": "Alta. Empresa acaba de levantar Serie B (capital fresco disponible y presión por crecer eficientemente).",
      "authority": "Muy Alta. VP of Operations en empresa mediana-grande (200 empleados), rol ejecutivo con poder de decisión sobre herramientas operativas.",
      "need": "Muy Alta. Solicitó demo proactivamente post-webinar, indicando dolor activo y conciencia del problema.",
      "timeline": "Alta. Deadline explícito: 'antes de Q3' (próximo trimestre), hay presión temporal real."
    },
    "action": "HOT LEAD - Agendar demo esta semana (máxima prioridad), preparar propuesta comercial con ROI específico para operaciones, asignar Account Executive senior inmediatamente.",
    "reason": "BANT perfecto: tiene dinero (Serie B reciente), autoridad (VP), necesidad urgente (Q3) y ya pidió demo. Es un Sales Qualified Lead (SQL) listo para cerrar."
  },
  {
    "lead": "Carlos Ruiz - Intern Marketing",
    "score": 2,
    "bant": {
      "budget": "Nulo/Desconocido. Solo solicita PDF de precios sin indicar poder de compra. Como intern, no maneja presupuesto.",
      "authority": "Nula. Es pasante de marketing, no es decision maker ni influencer clave en el proceso de compra B2B.",
      "need": "Baja. Investigación inicial delegada por su jefe ('investigar herramientas'), sin confirmar dolor real ni urgencia.",
      "timeline": "Baja. Fase de research temprana, sin timeline definido."
    },
    "action": "Nutrir (Nurture) - Enviar contenido educativo (PDF solicitado), agregar a secuencia de email marketing automatizada, NO asignar vendedor. Intentar identificar quién es el decision maker real en su empresa.",
    "reason": "Baja autoridad y etapa muy temprana. No es un lead calificado para ventas directas ahora (MQL no SQL), pero puede convertirse en 'champion' interno si se nutre correctamente. No malgastar tiempo de AE."
  }
]
```