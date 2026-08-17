# GLM 5 — multi_turn/requirements_change

- model_id: `z-ai/glm-5`
- success: True  | final: 4.17 | quality: 4.0
- latency_total: 80.021s | tokens_per_second: 7.6
- input_tokens: 227 | output_tokens: 607
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en Google Sheets, en su lugar introduce Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

Entendido, actualicemos el diseño del workflow. Aquí tienes la estructura completa:

## Flujo de trabajo

```
Gmail Trigger → Filter → Function (parsear datos) → Notion → Slack
```

---

### 1. **Gmail Trigger**
- **Resource**: Message
- **Event**: Message Received
- **Simplify**: Activar

---

### 2. **Filter Node** (IF node)
Condición para filtrar por asunto:

| Campo | Operador | Valor |
|-------|----------|-------|
| `subject` | Contains | `propuesta` |

**Segunda condición (OR):**
| Campo | Operador | Valor |
|-------|----------|-------|
| `subject` | Contains | `cotizacion` |

Configura el nodo para que continúe si **cualquiera** de las dos condiciones se cumple.

---

### 3. **Function Node** - Extraer datos
```javascript
// Extraer nombre y email del remitente
const from = $input.first().json.from;

// Parsear "Nombre <email@dominio.com>"
const emailMatch = from.match(/<([^>]+)>/);
const email = emailMatch ? emailMatch[1] : from;
const nombre = from.replace(/<[^>]+>/, '').trim();

return {
  nombre: nombre,
  email: email,
  asunto: $input.first().json.subject,
  fecha: $input.first().json.internalDate
};
```

---

### 4. **Notion Node**
- **Resource**: Database Page
- **Operation**: Create
- **Database ID**: Selecciona tu base de datos de Notion
- **Properties**: Mapea los campos:
  - `Nombre` ← `nombre`
  - `Email` ← `email`
  - `Asunto` ← `asunto`
  - `Fecha` ← `fecha`

> **Nota**: Necesitas crear una base de datos en Notion con estos campos antes de conectarla.

---

### 5. **Slack Node**
- **Resource**: Message
- **Operation**: Post
- **Channel**: Selecciona el canal
- **Message**:
```
📥 Nuevo email relevante recibido

De: {{nombre}} ({{email}})
Asunto: {{asunto}}
```

---

¿Necesitas ayuda con la configuración de las credenciales de Notion o Slack?