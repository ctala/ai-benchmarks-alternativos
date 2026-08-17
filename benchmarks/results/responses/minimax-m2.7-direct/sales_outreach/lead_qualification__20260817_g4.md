# MiniMax M2.7 (directo) — sales_outreach/lead_qualification

- model_id: `MiniMax-M2.7`
- success: True  | final: 6.51 | quality: 6.67
- latency_total: 18.046s | tokens_per_second: 50.8
- input_tokens: 247 | output_tokens: 917

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
    "lead": "Juan Perez, CEO",
    "score": 4,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas con recursos limitados.",
      "authority": "Alta. CEO = decisión final.",
      "need": "Media. Quiere explorar automatización de soporte.",
      "timeline": "Baja. 'Viendo opciones' = sin urgencia."
    },
    "action": "Nurturing - Enviar caso de estudio + agendar discovery call para evaluar seriedad.",
    "reason": "Authority alta pero budget y timeline ausentes. Startup pequeña = riesgo de compra baja."
  },
  {
    "lead": "Ana Gomez, VP Operations",
    "score": 9,
    "bant": {
      "budget": "Alta. Empresa 200 empleados, acaba de levantar Serie B.",
      "authority": "Alta. VP Ops típicamente decide en temas operativos como soporte.",
      "need": "Alta. Problema claro con soporte al cliente.",
      "timeline": "Alta. Deadline 'antes de Q3' = urgencia concreta."
    },
    "action": "PRIORIDAD MÁXIMA - Contactar hoy. Agendar demo ASAP.",
    "reason": "Fit perfecto BANT. Todos los indicadores de compra real presentes."
  },
  {
    "lead": "Carlos Ruiz, Intern",
    "score": 2,
    "bant": {
      "budget": "Inexistente. Un intern no maneja presupuesto.",
      "authority": "Ninguna. No es decision maker.",
      "need": "Baja. Necesidad del jefe, no suya.",
      "timeline": "Ninguna. Solo quiere comparar precios."
    },
    "action": "Proporcionar pricing PDF básico + solicitar nombre del jefe para escalar.",
    "reason": "Sin autoridad ni budget. Oportunidad de discovery para encontrar al buyer real."
  }
]
```

**Resumen:**
- 🔴 Ana Gomez: **Hot lead** → Prioridad inmediata
- 🟡 Juan Perez: **Warm lead** → Nutrir con contenido
- 🔵 Carlos Ruiz: **Cold lead** → Usar para escalar al decision maker