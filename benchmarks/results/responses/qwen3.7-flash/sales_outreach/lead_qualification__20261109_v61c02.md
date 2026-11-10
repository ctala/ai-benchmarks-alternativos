# Qwen 3.7 Flash — sales_outreach/lead_qualification

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 6.92 | quality: 6.67
- latency_total: 8.15s | tokens_per_second: 69.8
- input_tokens: 262 | output_tokens: 569

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
    "score": 3,
    "bant": {
      "budget": "No mencionado. Al ser una startup pequeña (5 personas), la capacidad de inversión es incierta.",
      "authority": "Alto. Es CEO, por lo que tiene autoridad para decidir, aunque el tamaño de la empresa limita el impacto comercial.",
      "need": "Moderado. Expresa interés en automatizar soporte, pero la frase 'viendo opciones' indica una etapa temprana de exploración sin urgencia clara.",
      "timeline": "Bajo. No hay fecha límite ni urgencia mencionada."
    },
    "action": "Nurturing",
    "reason": "El lead tiene autoridad y un problema potencial, pero carece de presupuesto confirmado, urgencia temporal y está en una fase muy inicial ('viendo opciones'). Requiere educación antes de intentar cerrar una venta."
  },
  {
    "score": 9,
    "bant": {
      "budget": "Alto. La empresa acaba de levantar Serie B, lo que indica disponibilidad de capital reciente para inversiones estratégicas.",
      "authority": "Alto. VP of Operations es un rol directivo clave con poder de decisión sobre procesos operativos.",
      "need": "Alto. Busca resolver un problema operativo específico mediante una solución concreta.",
      "timeline": "Alto. Tiene una fecha límite clara: 'antes de Q3', lo que genera urgencia inmediata."
    },
    "action": "Priorizar / Contactar inmediatamente",
    "reason": "Este lead cumple con todos los criterios BANT de forma sólida. Tiene dinero (Serie B), autoridad (VP), necesidad clara y urgencia (Q3). Es el candidato ideal para avanzar rápidamente al cierre."
  },
  {
    "score": 2,
    "bant": {
      "budget": "Desconocido/Inexistente. Es un intern, probablemente sin poder de gasto.",
      "authority": "Muy bajo. Solo investiga por encargo de su jefe; no es el tomador de decisiones.",
      "need": "Bajo. Es una investigación general ('investigar herramientas'), no una necesidad operativa crítica validada aún.",
      "timeline": "Indefinido. Depende del ritmo de trabajo de su jefe."
    },
    "action": "Descartar o Nurturing pasivo",
    "reason": "El contacto no tiene autoridad ni presupuesto. Aunque puede influir, no decide. Enviar recursos educativos (PDF) puede mantener el contacto, pero no requiere acción de ventas directa."
  }
]
```