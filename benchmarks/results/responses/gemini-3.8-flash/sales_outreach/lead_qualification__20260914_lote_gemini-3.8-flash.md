# Gemini 3.8 Flash — sales_outreach/lead_qualification

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 10.273s | tokens_per_second: 128.9
- input_tokens: 243 | output_tokens: 1324

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

[
  {
    "lead": "Lead 1: Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No especificado; probablemente limitado al ser una startup de 5 personas.",
      "authority": "Alta; es el CEO y tomador final de decisiones.",
      "need": "Media; busca automatizar soporte pero en etapa preliminar ('viendo opciones').",
      "timeline": "Baja; sin urgencia explícita, etapa exploratoria."
    },
    "action": "Nurturing automatizado / Invitar a prueba gratuita (Self-serve)",
    "reason": "Aunque tiene la autoridad máxima, el tamaño de la empresa y la falta de urgencia/presupuesto definido no justifican asignar recursos directos de ventas en este momento."
  },
  {
    "lead": "Lead 2: Ana Gomez",
    "score": 10,
    "bant": {
      "budget": "Alta probabilidad; empresa de 200 empleados con reciente levantamiento de Serie B.",
      "authority": "Alta; VP of Operations con poder de decisión y gestión presupuestaria.",
      "need": "Alta; solicitó activamente una demo tras asistir a un webinar.",
      "timeline": "Inmediata/Definida; requieren implementar la solución antes de Q3."
    },
    "action": "Asignar inmediatamente a Account Executive (AE) / Agendar demo prioritaria",
    "reason": "Cumple los 4 criterios de BANT con el perfil ideal de cliente (ICP): autoridad, presupuesto validado, dolor claro y ventana de tiempo definida."
  },
  {
    "lead": "Lead 3: Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "Desconocido; no tiene control sobre partidas presupuestarias.",
      "authority": "Nula; es un pasante (intern) haciendo benchmarking por encargo.",
      "need": "Difusa; investigación genérica de 'herramientas de IA'.",
      "timeline": "Desconocida; solo solicita material informativo."
    },
    "action": "Enviar PDF de precios automatizado y solicitar contacto del decisor (su jefe)",
    "reason": "Falta de autoridad y urgencia. No debe asignarse a ventas, pero se le entrega la información solicitada intentando conseguir el contacto del tomador de decisión."
  }
]