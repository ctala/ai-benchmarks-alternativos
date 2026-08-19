# KAT Coder Air v2.5 — sales_outreach/lead_qualification

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.07 | quality: 6.67
- latency_total: 4.266s | tokens_per_second: 167.4
- input_tokens: 260 | output_tokens: 714

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
    "score": 4,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas sugiere recursos limitados.",
      "authority": "CEO - tiene autoridad de decisión. Punto fuerte.",
      "need": "Sí tiene necesidad: busca automatizar su soporte. Exploratorio aún.",
      "timeline": "Vago: 'viendo opciones' no indica urgencia ni fecha."
    },
    "action": "Nurture",
    "reason": "Tiene autoridad y necesidad clara, pero falta presupuesto confirmado y urgencia. Lead de etapa temprana que requiere educación y seguimiento progresivo."
  },
  {
    "score": 8,
    "bant": {
      "budget": "Empresa acaba de levantar Serie B. Presupuesto disponible y confirmado.",
      "authority": "VP of Operations. Rol de liderazgo operativo, alta probabilidad de ser decision maker o influencer clave.",
      "need": "Necesidad clara y urgente: resolver antes de Q3. Problema activo que necesita solución.",
      "timeline": "Q3 como deadline. Timeline definido y cercano. Urgencia media-alta."
    },
    "action": "Contacto inmediato - Agendar demo prioritaria",
    "reason": "Lead con mayor calificación. Tiene presupuesto confirmado (Serie B), autoridad, necesidad clara y timeline definido. Priorizar seguimiento rápido para capturar la oportunidad antes de que evalúe competidores."
  },
  {
    "score": 2,
    "bant": {
      "budget": "No mencionado. Intern no tiene acceso a decisiones de compra.",
      "authority": "Intern de marketing. NO es decision maker. Solo recopila información para su jefe.",
      "need": "Necesidad existe pero es indirecta. Su jefe es quien decide, no él.",
      "timeline": "No especificado."
    },
    "action": "Nurture pasivo - No priorizar",
    "reason": "Lead de muy baja calidad. No tiene autoridad de compra ni presupuesto. El contacto real es su jefe. Enviar el PDF y mantenerlo en nurture para futuro contacto indirecto."
  }
]
```