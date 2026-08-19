# Qwen 3.7 Flash — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 4.52 | quality: 3.33
- latency_total: 26.145s | tokens_per_second: 125.8
- input_tokens: 260 | output_tokens: 3288

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
      "budget": "No mencionado / Incierto (startup temprana)",
      "authority": "Alto (CEO)",
      "need": "Claro (explorando automatización de soporte)",
      "timeline": "Indefinido / Etapa de exploración"
    },
    "action": "Nurturing cualificado / Email de seguimiento personalizado",
    "reason": "Posee alta autoridad y necesidad evidente, pero carece de confirmación presupuestaria y urgencia temporal. Requiere educación comercial y calificación progresiva antes de intervención directa."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto (empresa con ronda Serie B reciente)",
      "authority": "Alto (VP of Operations, decisor operativo)",
      "need": "Alto (solicitó demo tras webinar)",
      "timeline": "Alto (plazo definido: antes de Q3)"
    },
    "action": "Asignar a AE / Agendar demo prioritaria",
    "reason": "Score alto por cumplir BANT en todos los frentes. Cuenta con fondos disponibles, autoridad directa, necesidad concreta y ventana de tiempo clara. Listo para avanzar a fase de negociación y cierre."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Muy bajo (sin atribución presupuestal)",
      "authority": "Muy bajo (intern, rol ejecutor/investigador)",
      "need": "Bajo (tarea delegada de scouting)",
      "timeline": "No definido / Fase de descubrimiento"
    },
    "action": "Automatización / Enviar PDF solicitado + secuencia de nurturance",
    "reason": "Perfil junior sin poder de decisión ni presupuesto. Solo en etapa de reconocimiento técnico. Ideal para nutrición automatizada hasta que el contacto escale internamente, cambie de rol o el stakeholder tome la batuta."
  }
]
```