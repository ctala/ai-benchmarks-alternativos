# Claude Haiku 5.5 — sales_outreach/lead_qualification

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.22 | quality: 10.0
- latency_total: 5.186s | tokens_per_second: 192.6
- input_tokens: 411 | output_tokens: 999

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
    "lead": "Juan Perez",
    "score": 5,
    "bant": {
      "budget": "No mencionado. Startup de 5 personas sugiere presupuesto limitado, pero no confirmado.",
      "authority": "Alta. Es CEO, decide directamente.",
      "need": "Parcial. Esta 'viendo opciones' para automatizar soporte, lo que indica un problema, pero no sabemos si es urgente o severo.",
      "timeline": "Desconocido. No indico urgencia."
    },
    "action": "Nurturing: enviar contenido relevante del blog y preguntar por volumen de soporte y costo actual del proceso. Escalar a ventas si responde con urgencia o presupuesto definido.",
    "reason": "Decision maker con interes real, pero sin senales de presupuesto ni urgencia. Empresa pequena probablemente implica ticket bajo. Vale la pena calificar mas antes de invertir tiempo de ventas."
  },
  {
    "lead": "Ana Gomez",
    "score": 9,
    "bant": {
      "budget": "Alto. Empresa de 200 empleados recien financiada con Serie B.",
      "authority": "Alta. VP of Operations es decision maker o influencer principal.",
      "need": "Alto. Asistio a webinar y pidio demo, senal clara de interes activo en el problema.",
      "timeline": "Urgente. Quiere resolverlo antes de Q3, con fecha concreta."
    },
    "action": "Prioridad maxima: agendar demo en las proximas 48 horas con un ejecutivo de cuentas senior. Preparar caso de uso especifico para operaciones y confirmar quien mas participa en la decision.",
    "reason": "Cumple los cuatro criterios BANT con fuerza. Combinacion de presupuesto recien levantado, autoridad, necesidad expresada y plazo definido es el perfil ideal."
  },
  {
    "lead": "Carlos Ruiz",
    "score": 2,
    "bant": {
      "budget": "No es quien decide el presupuesto. Solo investiga por encargo.",
      "authority": "Muy baja. Es intern y no toma decisiones de compra.",
      "need": "Indirecto. Su jefe pidio investigar herramientas de IA, no necesariamente este producto.",
      "timeline": "Sin urgencia propia. Depende de la agenda de su jefe."
    },
    "action": "Enviar el PDF con precios como recurso general y pedirle que comparta el contacto de su jefe o que lo ponga en copia. No dedicar tiempo de ventas directo.",
    "reason": "Sin autoridad de compra ni necesidad propia. Valor principal es llegar al decision maker a traves de el. Puede ser util como influencer interno, pero no es prospecto calificado."
  }
]
```