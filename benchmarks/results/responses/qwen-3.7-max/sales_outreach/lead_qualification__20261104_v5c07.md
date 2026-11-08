# Qwen 3.7 Max — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 3.86 | quality: 3.33
- latency_total: 11.716s | tokens_per_second: 46.9
- input_tokens: 262 | output_tokens: 549

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
      "budget": "Desconocido. Startup de 5 personas sugiere presupuesto limitado o no asignado.",
      "authority": "Alta. Es CEO y tiene poder de decisión total.",
      "need": "Media. Tiene un problema claro (automatizar soporte) pero está en fase de exploración ('viendo opciones').",
      "timeline": "Bajo. No hay urgencia declarada; llegada vía blog indica etapa temprana de investigación."
    },
    "action": "Nurturing automatizado",
    "reason": "Aunque es el decision maker, la falta de presupuesto confirmado, el tamaño reducido de la empresa y la ausencia de urgencia lo hacen un lead de baja prioridad comercial inmediata. Requiere educación hasta que madure."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. Recién levantaron Serie B, lo que indica liquidez para inversión en herramientas.",
      "authority": "Alta. VP of Operations en empresa de 200 empleados suele tener autoridad de compra o influencia decisiva directa.",
      "need": "Alto. Necesidad explícita de resolver un problema operativo específico.",
      "timeline": "Alto. Deadline claro definido ('antes de Q3')."
    },
    "action": "Asignar a Account Executive para demo prioritaria",
    "reason": "Cumple con los 4 criterios BANT de forma sólida. Tiene fondos, autoridad, necesidad urgente y un timeline definido. Es un oportunidad de cierre inminente."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido. Solo solicita lista de precios, sin confirmación de disponibilidad real.",
      "authority": "Nula. Es un intern realizando investigación delegada por su jefe.",
      "need": "Indefinido. La necesidad es de su jefe, no propia; aún están en fase de mapeo de mercado.",
      "timeline": "Desconocido. No se ha mencionado ninguna fecha ni urgencia."
    },
    "action": "Enviar PDF solicitado y calificar como MQL en nurturing",
    "reason": "No es decision maker ni influenciador directo. Es un contacto informativo en etapa muy temprana. Se debe proveer la información solicitada pero no dedicar recursos de ventas hasta identificar al verdadero comprador."
  }
]
```