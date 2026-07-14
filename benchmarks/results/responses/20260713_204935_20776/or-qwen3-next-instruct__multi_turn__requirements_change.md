# Qwen 3-Next 80B Instruct — multi_turn/requirements_change

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.17 | quality: 6.0
- latency_total: 9.129s | tokens_per_second: 188.2
- input_tokens: 246 | output_tokens: 1718
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, ajustándose a los requisitos actualizados del usuario, y ofrece una estructura clara y detallada que un emprendedor podría usar directamente, aunque no profundiza en aspectos como la gestión de errores o la escalabilidad.

## Respuesta completa

¡Perfecto! Tu nuevo workflow es más inteligente y útil. Aquí te dejo el **workflow completo en N8N** con los siguientes pasos:

---

### ✅ **Objetivo final:**
- **Monitorear Gmail** en busca de emails nuevos
- **Filtrar** solo los que contengan `"propuesta"` o `"cotización"` (o variants) en el **asunto**
- **Extraer**: Nombre del remitente, email, asunto, fecha
- **Guardar en Notion** (como una nueva página en una base de datos)
- **Enviar notificación a Slack**

---

## 🛠️ **Workflow en N8N (pasos detallados)**

### **1. Gmail Trigger — `New Email`**
> Se activa cuando llega un nuevo email en la bandeja de entrada.

- **Credenciales**: Conecta tu cuenta de Gmail (usa OAuth)
- **Opciones avanzadas**:
  - ✅ `Only unread emails` → **Sí** (evita repetidos)
  - ✅ `Include email body` → **No** (no lo necesitas aún)
  - ✅ `Include email headers` → **Sí**

> ⚠️ **Importante**: Si usas 2FA, genera una contraseña de app de Google y usa eso en N8N.

---

### **2. Filter Node — Filtrar por palabras clave en el asunto**
> Solo deja pasar emails con `"propuesta"` o `"cotización"` (en español o inglés)

- **Condición**:
  ```
  {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') || $json.subject.toLowerCase().includes('cotización') }}
  ```

- **Opción**: `Keep if true`

> ✅ Esto filtra:  
> - "Propuesta de servicio"  
> - "Cotización para tu proyecto"  
> - "Proposal for..." (si quieres incluir inglés, añade `'proposal'` o `'quote'`)

💡 *Consejo*: Si quieres incluir inglés, usa:
```js
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') || $json.subject.toLowerCase().includes('cotización') || $json.subject.toLowerCase().includes('proposal') || $json.subject.toLowerCase().includes('quote') }}
```

---

### **3. Function Node — Extraer y formatear datos**
> Transforma los datos para que Notion los entienda

**Nombre**: `Extract Sender & Format for Notion`

```javascript
// Extrae el remitente y formatea datos limpios
const subject = items[0].json.subject;
const from = items[0].json.from;

// Extrae nombre y email desde el formato "Nombre <email@dominio.com>"
const emailRegex = /<([^>]+)>/;
const match = from.match(emailRegex);
const email = match ? match[1] : from;
const name = match ? from.replace(emailRegex, '').trim().replace(/"/g, '') : from;

// Fecha en formato ISO (Notion lo acepta como "date")
const date = new Date(items[0].json.date).toISOString().split('T')[0];

return [
  {
    json: {
      name: name,
      email: email,
      subject: subject,
      date: date,
      source: "Gmail - Propuesta/Cotización"
    },
    binary: {},
    metadata: {}
  }
];
```

👉 Esto te da:  
- `name`: "Juan Pérez"  
- `email`: "juan@empresa.com"  
- `subject`: "Cotización para sitio web"  
- `date`: "2025-04-05"  
- `source`: texto descriptivo

---

### **4. Notion Node — Crear página en base de datos**
> Necesitas una base de datos en Notion con las propiedades adecuadas.

#### 🔧 Configuración de Notion:
1. En Notion, crea una **Base de Datos** (ej: "Propuestas Entrantes")
2. Añade las siguientes propiedades:
   - **Nombre** (Title)
   - **Email** (Email)
   - **Asunto** (Title o Rich Text)
   - **Fecha** (Date)
   - **Origen** (Select o Rich Text)

#### ➤ Configura el nodo en N8N:
- **Action**: `Create a page`
- **Database ID**: Pega el ID de tu base de datos (lo obtienes del URL de la página: `https://www.notion.so/.../abc123...?v=...` → el ID es `abc123...`)
- **Properties**:
  - **Nombre**: `={{ $json.name }}`
  - **Email**: `={{ $json.email }}`
  - **Asunto**: `={{ $json.subject }}`
  - **Fecha**: `={{ $json.date }}`
  - **Origen**: `={{ $json.source }}`

> ✅ ¡Necesitas un **token de integración de Notion** y **compartir la base de datos** con esa integración!  
> [Guía rápida: Cómo generar token de Notion](https://docs.n8n.io/integrations/builtin/activators/n8n-nodes-notion/)

---

### **5. Slack Node — Enviar notificación**
> Notifica en un canal de Slack cuando llega una nueva propuesta

- **Action**: `Send a message`
- **Channel**: `#notificaciones-propuestas` (o el canal que prefieras)
- **Message**:
  ```
  📩 Nueva propuesta recibida!

  👤 *Remitente:* {{ $json.name }}
  ✉️ *Email:* {{ $json.email }}
  📌 *Asunto:* {{ $json.subject }}
  📅 *Fecha:* {{ $json.date }}

  🚀 Revisa en Notion: https://www.notion.so/...[tu-base-de-datos]
  ```

> ✅ Necesitas un **token de Slack** (OAuth App + token de bot) y tener el canal accesible.  
> [Guía: Cómo conectar Slack a N8N](https://docs.n8n.io/integrations/builtin/activators/n8n-nodes-slack/)

---

## 🧩 **Workflow Resumido (Flujo)**

```
Gmail Trigger (New Email)
        ↓
    Filter (propuesta/cotización)
        ↓
Function (Extraer nombre/email/fecha)
        ↓
   Notion (Crear página en DB)
        ↓
     Slack (Enviar notificación)
```

---

## ✅ Recomendaciones Finales

| Tarea | Recomendación |
|-------|----------------|
| ✅ Pruebas | Usa el botón "Execute Workflow" en N8N para probar con un email de prueba |
| ✅ Logs | Activa el nodo "Debug" después de cada paso si algo falla |
| ✅ Email duplicados | El trigger con "Only unread" evita duplicados |
| ✅ Notion | Usa `Date` como tipo de campo en Notion, no texto |
| ✅ Slack | Usa emojis para que la notificación sea más visible |
| ✅ Seguridad | No compartas tokens de Gmail/Notion/Slack en GitHub o chats públicos |

---

## 💡 Bonus: ¿Quieres que se guarde el cuerpo del email también?

Si más adelante quieres guardar el contenido del email (para búsqueda), activa `Include email body` en el Trigger y usa un `Function` para extraer solo las primeras 200 palabras.

---

¿Quieres que te genere el **JSON exportable del workflow** para copiarlo directamente en N8N?  
¡Solo dime y te lo doy listo para pegar! 🚀