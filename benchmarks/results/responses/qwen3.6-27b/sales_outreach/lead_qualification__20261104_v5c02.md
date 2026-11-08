# Qwen 3.6 27B base (OpenRouter FP8) — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 10.094s | tokens_per_second: 55.3
- input_tokens: 262 | output_tokens: 558

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

{
  "leads": [
    {
      "name": "Juan Perez",
      "score": 4,
      "bant": {
        "budget": "Desconocido. No se mencionó presupuesto explícito.",
        "authority": "Alta. Es el CEO y tomador de decisiones final.",
        "need": "Media/Alta. Expresa interés en automatizar soporte, pero está en fase exploratoria.",
        "timeline": "Baja/Desconocida. Llegó vía blog, sin urgencia aparente."
      },
      "action": "Nurturing / Educación",
      "reason": "Aunque tiene autoridad máxima (CEO), la falta de mención de presupuesto y la fuente de entrada (blog) sugieren que está en etapa temprana de investigación. Requiere contenido educativo para madurar el lead antes de una venta directa."
    },
    {
      "name": "Ana Gomez",
      "score": 9,
      "bant": {
        "budget": "Alta probabilidad. La empresa levantó Serie B, lo que indica fondos disponibles.",
        "authority": "Alta. VP of Operations es un rol clave con poder de decisión o fuerte influencia.",
        "need": "Alta. Solicitó demo activa tras webinar.",
        "timeline": "Alta. Urgencia clara: 'resolver esto antes de Q3'."
      },
      "action": "Venta Inmediata / Demo Prioritaria",
      "reason": "Cumple casi todos los criterios BANT. Tiene autoridad, necesidad clara, timeline urgente y señal fuerte de presupuesto (Serie B). Es un lead calificado listo para cerrar."
    },
    {
      "name": "Carlos Ruiz",
      "score": 2,
      "bant": {
        "budget": "Desconocido/Bajo impacto. Un intern no maneja presupuestos.",
        "authority": "Muy Baja. Es un intern; solo investiga por orden de su jefe.",
        "need": "Media. Hay necesidad en la empresa, pero él no la siente directamente.",
        "timeline": "Desconocida. Depende de las instrucciones de su jefe."
      },
      "action": "Descalificar / Derivar a Marketing Automation",
      "reason": "No es el tomador de decisiones. Enviarle precios puede generar ruido. Lo ideal es ofrecer recursos educativos y tratar de contactar al jefe (decision maker) si es posible, o dejarlo en campañas de nurturing automáticas."
    }
  ]
}