# Claude Fable 5 — multi_turn/requirements_change

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 5.31 | quality: 6.0
- latency_total: 15.476s | tokens_per_second: 59.9
- input_tokens: 363 | output_tokens: 927
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en Google Sheets, en su lugar sugiere usar Notion y Slack, lo que la hace irrelevante. Sin embargo, la estructura del workflow es clara y podría ser útil si se ajustara a los requisitos correctos.

## Respuesta completa

Sin problema, el workflow queda asi:

**Estructura del workflow:**

1. **Gmail Trigger** → 2. **Filter/IF node** → 3. **Function node** → 4. **Notion node** → 5. **Slack node**

---

**1. Gmail Trigger**
- Event: Message Received
- Puedes dejar que traiga todos los emails y filtrar despues, o usar el campo "Search" con: `subject:(propuesta OR cotizacion)` para filtrar directo desde Gmail (mas eficiente).

**2. Filter node** (si no filtraste en el trigger)
- Condicion tipo OR:
  - `{{ $json.subject.toLowerCase() }}` contains `propuesta`
  - `{{ $json.subject.toLowerCase() }}` contains `cotizacion`
- Tip: usa `toLowerCase()` para que no importen mayusculas. Considera tambien agregar "cotización" con tilde, porque muchos clientes la escriben asi.

**3. Function/Set node** — extraer datos
- Nombre del remitente: `{{ $json.from.value[0].name }}`
- Email: `{{ $json.from.value[0].address }}`
- Asunto: `{{ $json.subject }}`
- Fecha: `{{ $json.date }}`

(Los paths exactos pueden variar segun la version del nodo de Gmail; revisa el output del trigger en modo test.)

**4. Notion node**
- Operation: Create → Database Page
- Antes necesitas crear en Notion una database con columnas: Nombre, Email, Asunto, Fecha
- Conecta la integracion de Notion y comparte la database con ella (paso que muchos olvidan y da error 404)
- Mapea cada propiedad con los datos del paso anterior

**5. Slack node**
- Operation: Send Message
- Canal: el que prefieras
- Mensaje ejemplo:
```
📩 Nueva propuesta/cotizacion recibida
De: {{ $json.nombre }} ({{ $json.email }})
Asunto: {{ $json.asunto }}
```

---

**Credenciales que necesitas configurar:** Gmail (OAuth2), Notion (Internal Integration Token) y Slack (OAuth2 o webhook).

Quieres que te ayude con la configuracion de alguna credencial en especifico, o con el JSON del workflow para importarlo directo?