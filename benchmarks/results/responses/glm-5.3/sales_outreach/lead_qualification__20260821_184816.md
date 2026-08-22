# GLM 5.3 — sales_outreach/lead_qualification

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 31.548s | tokens_per_second: 62.3
- input_tokens: 255 | output_tokens: 1965

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
  "lead_1_juan_perez": {
    "score": 5,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto; startup de 5 personas sugiere presupuesto limitado",
      "authority": "Alta - es CEO y decisor final",
      "need": "Moderado - quiere automatizar soporte, pero en fase exploratoria ('viendo opciones')",
      "timeline": "Desconocido - sin urgencia mencionada"
    },
    "action": "Agendar discovery call para calificar presupuesto y timeline; incluir en secuencia de nurture",
    "reason": "Decisor con necesidad real pero señales débiles: llegó por canal orgánico de baja intención (blog), lenguaje exploratorio, sin presupuesto ni timeline. No pasa directo a ventas pero merece calificación activa."
  },
  "lead_2_ana_gomez": {
    "score": 9,
    "bant": {
      "budget": "Alta probabilidad - Serie B recién levantada indica capital disponible",
      "authority": "Alta - VP of Operations, decisor o influenciador clave en una empresa de 200 empleados",
      "need": "Alta - pidió demo activamente después de un webinar",
      "timeline": "Clara y urgente - 'necesitamos resolver esto antes de Q3'"
    },
    "action": "Fast-track: asignar a un AE y agendar demo en menos de 24-48 horas",
    "reason": "Cumple los 4 criterios BANT: presupuesto (Serie B), autoridad (VP Ops), necesidad explícita (pidió demo) y timeline urgente (Q3). Es el lead más caliente del lote y cada día de demora es riesgo."
  },
  "lead_3_carlos_ruiz": {
    "score": 2,
    "bant": {
      "budget": "No - es intern, sin acceso a presupuesto",
      "authority": "No - no es decisor; su jefe es quien evaluará y decidirá",
      "need": "Vago e indirecto - investigación genérica de 'herramientas de IA', no un problema específico de nuestro producto",
      "timeline": "Desconocido - sin urgencia"
    },
    "action": "Enviar PDF de precios de forma automatizada; intentar identificar al decisor real (su jefe) y moverlo a nurture de bajo toque",
    "reason": "Falla 3 de 4 criterios BANT. Sin autoridad ni presupuesto, y la necesidad es difusa. El único valor es que existe una empresa detrás con interés incipiente. No justifica tiempo del equipo de ventas."
  }
}
```