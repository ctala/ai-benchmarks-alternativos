# Mistral Small 4 — multi_turn/requirements_change

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.28 | quality: 6.0
- latency_total: 9.622s | tokens_per_second: 182.6
- input_tokens: 239 | output_tokens: 1757

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico para emprendedores que trabajan con N8N.

**user:**

Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet.

**assistant:**

Perfecto, ese workflow es bastante directo. Te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Extraer datos**: Function node para parsear remitente, asunto, fecha
3. **Guardar**: Google Sheets node para agregar una fila

Los campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?

**user:**

En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno.


## Respuesta completa

¡Perfecto! Vamos a crear un workflow en **n8n** que cumpla con tus nuevos requisitos:

1. **Trigger**: Gmail (solo emails nuevos con "propuesta" o "cotización" en el asunto).
2. **Extraer datos**: Obtener remitente, asunto, fecha y cuerpo del email.
3. **Enviar a Notion**: Crear una nueva entrada en tu base de datos de Notion.
4. **Notificación Slack**: Enviar un mensaje cuando se procese un email.

---

### **Paso a paso para configurar el workflow en n8n**

#### **1. Configurar el nodo "Gmail Trigger"**
- **Tipo de conexión**: `OAuth2` (autoriza tu cuenta de Gmail).
- **Filtro de asunto**: Usaremos una expresión para buscar emails con "propuesta" o "cotización" (sin importar mayúsculas/minúsculas).
  - **Fórmula**:
    ```plaintext
    {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') }}
    ```
- **Opcional**: Si quieres filtrar por un remitente específico o etiquetas de Gmail, configúralo aquí.

---

#### **2. Configurar el nodo "Set" (opcional, para limpieza de datos)**
- Si necesitas extraer el nombre del remitente desde el campo `from` (que suele estar en formato `"Nombre <email@dominio.com>"`), usa una expresión como:
  ```plaintext
  {{ $json.from.match(/[^<]+/)[0].trim() }}
  ```
  Esto extrae solo el nombre del remitente.

---

#### **3. Configurar el nodo "Notion"**
- **Operación**: `Append a row` (o `Create` si prefieres agregar una nueva página).
- **Base de datos**: Selecciona la base de datos de Notion donde quieres guardar los datos.
- **Mapeo de campos**:
  - **Nombre del remitente**: `{{ $json.fromName }}` (o el campo que hayas limpiado).
  - **Email**: `{{ $json.from }}` (puede ser el email directo o el extraído).
  - **Asunto**: `{{ $json.subject }}`
  - **Fecha**: `{{ $json.date }}`
  - **Cuerpo del email**: `{{ $json.text }}` (o `html` si prefieres HTML).

---

#### **4. Configurar el nodo "Slack" (para notificaciones)**
- **Operación**: `Post Message`.
- **Canal**: Selecciona el canal de Slack donde quieres que lleguen las notificaciones.
- **Mensaje**:
  ```plaintext
  📩 *Nuevo email con "propuesta" o "cotización" en el asunto*
  **Asunto**: {{ $json.subject }}
  **De**: {{ $json.from }}
  **Fecha**: {{ $json.date }}
  [Ver en Gmail]({{ $json.gmailUrl }})  // Opcional: enlace directo al email.
  ```
- **Opcional**: Si quieres adjuntar datos específicos como el cuerpo del email, añádelo al mensaje.

---

### **Ejemplo de workflow en JSON (para importar en n8n)**
Si prefieres importar el workflow directamente en n8n, aquí tienes un JSON con la configuración básica:

```json
{
  "name": "Email a Notion + Notificación Slack",
  "nodes": [
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "options": {
          "subjectFilter": {
            "value": "{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') }}",
            "type": "string"
          }
        }
      },
      "id": "gmail-trigger",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "credentials": {
        "gmailApi": "TU_CREDENCIAL_GMAIL"
      }
    },
    {
      "parameters": {
        "functionCode": "// Extraer nombre del remitente si está en formato 'Nombre <email>'\nif ($json.from) {\n  const fromMatch = $json.from.match(/[^<]+/);\n  $json.fromName = fromMatch ? fromMatch[0].trim() : $json.from;\n}\nreturn $json;"
      },
      "id": "set-node",
      "name": "Set (Extraer nombre)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "operation": "append",
        "databaseId": "TU_BASE_DE_DATOS_NOTION",
        "fields": {
          "Nombre": "={{ $json.fromName }}",
          "Email": "={{ $json.from }}",
          "Asunto": "={{ $json.subject }}",
          "Fecha": "={{ $json.date }}",
          "Cuerpo": "={{ $json.text }}"
        }
      },
      "id": "notion-node",
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "notionApi": "TU_CREDENCIAL_NOTION"
      }
    },
    {
      "parameters": {
        "channel": "TU_CANAL_SLACK",
        "text": "📩 *Nuevo email con \"propuesta\" o \"cotización\" en el asunto*\n**Asunto**: {{ $json.subject }}\n**De**: {{ $json.from }}\n**Fecha**: {{ $json.date }}\n[Ver en Gmail]({{ $json.gmailUrl }})"
      },
      "id": "slack-node",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 300],
      "credentials": {
        "slackApi": "TU_CREDENCIAL_SLACK"
      }
    }
  ],
  "connections": {
    "Gmail Trigger": {
      "main": [
        [
          {
            "node": "Set (Extraer nombre)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set (Extraer nombre)": {
      "main": [
        [
          {
            "node": "Notion",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

---

### **Notas importantes**
1. **Credenciales**:
   - Configura las credenciales de Gmail, Notion y Slack en **Credentials** dentro de n8n.
   - Para Notion, necesitas un **token de integración** (generado en [Notion Integrations](https://www.notion.so/my-integrations)).
   - Para Slack, crea un **token de bot** en [Slack API](https://api.slack.com/apps).

2. **Base de datos de Notion**:
   - Asegúrate de que la base de datos tenga los campos correspondientes (Nombre, Email, Asunto, Fecha, Cuerpo).

3. **Pruebas**:
   - Ejecuta el workflow manualmente una vez para verificar que todo funcione.
   - Revisa los logs en n8n si hay errores.

¿Necesitas ayuda con algún paso en específico? 😊