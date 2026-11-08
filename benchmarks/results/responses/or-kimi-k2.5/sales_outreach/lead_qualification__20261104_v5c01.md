# Kimi K2.5 — sales_outreach/lead_qualification

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 3.83 | quality: 3.33
- latency_total: 22.683s | tokens_per_second: 27.4
- input_tokens: 280 | output_tokens: 621

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
    "score": 5,
    "bant": {
      "budget": "Desconocido - no mencionó presupuesto, startup pequeña probablemente con recursos limitados",
      "authority": "Alto - es CEO, tiene poder de decisión total",
      "need": "Moderado - está en fase de exploración ('viendo opciones'), no hay urgencia declarada ni problema específico",
      "timeline": "Indefinido - solo está investigando, sin fecha comprometida"
    },
    "action": "NURTURE",
    "reason": "CEO con autoridad pero en etapa muy temprana de investigación. Sin presupuesto visible ni urgencia. Priorizar educación de contenido y seguimiento en 2-3 semanas para detectar avance en decisión. No asignar SDR aún."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto - Serie B reciente indica capital disponible, empresa de 200 empleados con capacidad de inversión",
      "authority": "Alto - VP of Operations, rol con poder de decisión operativa y presupuestaria",
      "need": "Alto - solicitó demo activamente, problema identificado y buscando solución concreta",
      "timeline": "Muy definido - antes de Q3, deadline claro que genera urgencia real"
    },
    "action": "CONTACTAR INMEDIATAMENTE",
    "reason": "Lead caliente con BANT casi perfecto. Timeline comprometido, autoridad confirmada, necesidad validada con acción (demo request), y presupuesto respaldado por financiamiento reciente. Asignar AE senior, contactar en <2 horas, acelerar ciclo de venta."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido - solicita precios pero sin contexto de decisión de compra",
      "authority": "Muy bajo - intern de marketing, sin poder de decisión",
      "need": "Bajo - tarea delegada de 'investigar', no problema propio ni compromiso",
      "timeline": "Indefinido - sin urgencia mencionada, probablemente sin fecha de entrega clara"
    },
    "action": "DESCARTAR o ENVIAR A MARKETING",
    "reason": "Lead de muy baja calidad. No es ICP viable: sin autoridad, sin necesidad real (solo recolectando información), sin timeline. Enviar a marketing para nurturing automatizado. No invertir tiempo de ventas. Si se contacta, pedir hablar con el jefe directo."
  }
]
```