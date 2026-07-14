# DeepSeek V3 — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 4.64 | quality: 4.0
- latency_total: 25.136s | tokens_per_second: 25.9
- input_tokens: 244 | output_tokens: 652
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, adaptándose a los requisitos modificados al incluir Notion y Slack, además de proporcionar una estructura clara y detallada que un emprendedor podría usar directamente, aunque el cambio de Google Sheet a Notion no se explicó en detalle.

## Respuesta completa

Excelente, mejor aún. Este workflow será más completo y automatizado. Te detallo la estructura:

## Workflow con 5 nodos:

### **1. Trigger - Gmail Trigger**
- Configura la conexión con Gmail
- Se activa cada X tiempo (ej: 15 minutos)
- Captura emails nuevos

### **2. Filter - IF Node** (para filtrar por asunto)
- Condición: `{{ $json.subject.toLowerCase().includes("propuesta") || $json.subject.toLowerCase().includes("cotización") || $json.subject.toLowerCase().includes("cotizacion") }}`
- Solo pasa los emails que contengan esas palabras

### **3. Function Node** (extraer y formatear datos)
```javascript
// Extraer información del remitente
const from = $input.first().from;
const subject = $input.first().subject;
const date = $input.first().date;
const body = $input.first().plainText || '';

// Parsear remitente (ej: "Juan Perez <juan@email.com>")
let name = '';
let email = '';

if (from.includes('<')) {
  name = from.split('<')[0].trim();
  email = from.split('<')[1].replace('>', '').trim();
} else {
  email = from.trim();
  name = email.split('@')[0];
}

// Preparar para Notion
const notionData = {
  properties: {
    "Nombre": {
      "title": [
        {
          "text": {
            "content": name
          }
        }
      ]
    },
    "Email": {
      "email": email
    },
    "Asunto": {
      "rich_text": [
        {
          "text": {
            "content": subject
          }
        }
      ]
    },
    "Fecha": {
      "date": {
        "start": new Date(date).toISOString()
      }
    },
    "Contenido": {
      "rich_text": [
        {
          "text": {
            "content": body.substring(0, 2000) // Limitar tamaño
          }
        }
      ]
    }
  }
};

return notionData;
```

### **4. Notion Node** (Create Page)
- Conexión: Tu cuenta de Notion
- Database: Seleccionas la base de datos donde quieres guardar
- Properties: Los mapeas desde el Function node

### **5. Slack Node** (Send Message)
- Conexión: Tu workspace de Slack
- Channel: #notificaciones o DM
- Mensaje personalizable: `📧 Nueva propuesta/cotización de {{ $json.properties.Nombre.title[0].text.content }}`

## Configuraciones necesarias:
1. **Credenciales Gmail** en N8N (OAuth2)
2. **Integración de Notion** (crear internal integration y compartir DB)
3. **App de Slack** en tu workspace

¿Quieres que te explique algún paso específico o la configuración de las conexiones?