# Inkling Small — sales_outreach/lead_qualification

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 31.101s | tokens_per_second: 50.7
- input_tokens: 249 | output_tokens: 1576

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
{
  "leads": [
    {
      "name": "Juan Perez",
      "role": "CEO, startup 5 personas",
      "score": 5,
      "bant": {
        "budget": "No confirmado; startup muy pequeña sugiere presupuesto limitado o no asignado aún",
        "authority": "Alta; CEO es decision maker",
        "need": "Medio; menciona automatizar soporte pero es exploratorio y vago",
        "timeline": "No definido; llega vía blog sin urgencia declarada"
      },
      "action": "Calificar (qualify) antes de demo: confirmar presupuesto, alcance del problema y timeline específico",
      "reason": "Autoridad alta, pero falta confirmación de presupuesto, necesidad concreta y urgencia. Es un lead temprano que requiere nurturing calificado."
    },
    {
      "name": "Ana Gomez",
      "role": "VP of Operations, empresa 200 empleados",
      "score": 9,
      "bant": {
        "budget": "Alto; empresa levantó Serie B indica capacidad de inversión y presupuesto disponible",
        "authority": "Alta; VP Operations es decision maker o influenciador clave con poder de compra",
        "need": "Alto; pidió demo tras webinar y tiene problema definido (resolver antes de Q3)",
        "timeline": "Urgente; necesita solución antes de Q3"
      },
      "action": "Priorizar inmediatamente: agendar demo hoy, asignar Account Executive y preparar propuesta personalizada",
      "reason": "Cumple BANT casi completamente: alta autoridad, necesidad clara, timeline urgente y presupuesto probable. Es una oportunidad caliente."
    },
    {
      "name": "Carlos Ruiz",
      "role": "Intern de marketing",
      "score": 2,
      "bant": {
        "budget": "No; intern sin poder de compra ni acceso a presupuesto",
        "authority": "Baja; no es decision maker, solo investigando por orden de su jefe",
        "need": "Bajo/Indirecto; su jefe pidió investigar herramientas de IA, no hay problema propio definido",
        "timeline": "No urgente; solicita PDF con precios como paso inicial"
      },
      "action": "Descalificar como oportunidad activa; enviar contenido educativo/PDF sin dedicar recursos de ventas, y solicitar contacto con el decision maker",
      "reason": "Falta autoridad, presupuesto y necesidad directa. Es un investigador (researcher), no un buyer. Riesgo de perder tiempo si se trata como oportunidad."
    }
  ]
}
```