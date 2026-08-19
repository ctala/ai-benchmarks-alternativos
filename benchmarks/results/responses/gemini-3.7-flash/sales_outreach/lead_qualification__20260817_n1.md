# Gemini 3.7 Flash — sales_outreach/lead_qualification

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 8.546s | tokens_per_second: 136.9
- input_tokens: 243 | output_tokens: 1170

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
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "Desconocido / Probablemente bajo (startup de 5 personas)",
      "authority": "Alta (CEO / Tomador de decisiones directo)",
      "need": "Media (explorando opciones de automatización de soporte)",
      "timeline": "Baja / No definida (etapa exploratoria temprana)"
    },
    "action": "Nurturing automatizado y email de discovery",
    "reason": "Tiene la autoridad directa, pero está en etapa exploratoria sin urgencia ni presupuesto validado. No requiere atención inmediata de un ejecutivo senior."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alto (reciente Serie B, empresa de 200 empleados)",
      "authority": "Alta (VP of Operations)",
      "need": "Alta (solicitó demo activamente tras webinar)",
      "timeline": "Alta / Crítica (necesita implementar antes de Q3)"
    },
    "action": "Asignar de inmediato a Account Executive (AE) y agendar demo",
    "reason": "Lead ideal (SQL). Cumple con los 4 pilares de BANT: presupuesto respaldado por ronda de inversión, poder de decisión, necesidad clara y fecha límite definida."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido",
      "authority": "Nula (pasante de marketing, solo recopila información)",
      "need": "Baja / Indefinida (investigación genérica de herramientas)",
      "timeline": "Desconocida / Sin urgencia"
    },
    "action": "Enviar PDF de precios automatizado e incluir en secuencia de marketing",
    "reason": "Sin autoridad ni dolor de negocio claro. Enviar material solicitado por vía automatizada para no consumir tiempo de ventas directas."
  }
]
```