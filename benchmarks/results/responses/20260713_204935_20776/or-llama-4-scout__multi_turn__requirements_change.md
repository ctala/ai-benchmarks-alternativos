# Llama 4 Scout 17B — multi_turn/requirements_change

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 6.18 | quality: 6.0
- latency_total: 23.505s | tokens_per_second: 34.5
- input_tokens: 230 | output_tokens: 812
- judge_score: 3.0 | justificación: La respuesta es correcta en términos de configuración de un flujo de trabajo en N8N, pero no cumple con los requisitos originales de guardar datos en Google Sheets, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

Genial, podemos adaptar el workflow para que se ajuste a tus necesidades. Aquí te explico los pasos:

**Workflow:**

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtrar**: Function node para verificar si el asunto contiene las palabras 'propuesta' o 'cotización'
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha y contenido del email
4. **Notificación a Slack**: Slack node para enviar una notificación cuando llegue un email que cumpla con los criterios
5. **Guardar en Notion**: Notion node para crear una nueva página con los datos extraídos

**Configuración de cada nodo:**

### 1. Gmail Trigger

* Configura la cuenta de Gmail que deseas utilizar
* Selecciona el tipo de trigger que deseas (por ejemplo, "Nuevo email")
* Configura los parámetros de búsqueda (por ejemplo, carpeta de entrada, etiquetas, etc.)

### 2. Filtrar

* Agrega un Function node después del trigger de Gmail
* En el código, puedes utilizar algo como:
```javascript
const asunto = items[0].json.asunto;
const palabrasClave = ['propuesta', 'cotización'];
const contienePalabraClave = palabrasClave.some(palabra => asunto.toLowerCase().includes(palabra.toLowerCase()));

if (!contienePalabraClave) {
  return [];
}

return items;
```
* Esto verificará si el asunto contiene alguna de las palabras clave y solo pasará el email si la condición se cumple.

### 3. Extraer datos

* Agrega un Function node después del nodo de filtrado
* En el código, puedes utilizar algo como:
```javascript
const remitente = items[0].json.from;
const asunto = items[0].json.asunto;
const fecha = items[0].json.date;
const contenido = items[0].json.body;

items[0].json.remitente = remitente;
items[0].json.asunto = asunto;
items[0].json.fecha = fecha;
items[0].json.contenido = contenido;

return items;
```
* Esto extraerá los datos que necesitas y los agregará al objeto `json` de cada item.

### 4. Notificación a Slack

* Agrega un Slack node después del nodo de extracción de datos
* Configura la cuenta de Slack que deseas utilizar
* Selecciona el tipo de mensaje que deseas enviar (por ejemplo, "Mensaje de texto")
* En el texto del mensaje, puedes utilizar algo como:
```markdown
Nuevo email de ${items[0].json.remitente} con asunto: ${items[0].json.asunto}
```
* Esto enviará una notificación a Slack con la información del remitente y el asunto.

### 5. Guardar en Notion

* Agrega un Notion node después del nodo de notificación a Slack
* Configura la cuenta de Notion que deseas utilizar
* Selecciona el tipo de página que deseas crear (por ejemplo, "Página básica")
* En el contenido de la página, puedes utilizar algo como:
```json
{
  "properties": {
    "Remitente": {
      "text": [
        {
          "text": items[0].json.remitente
        }
      ]
    },
    "Asunto": {
      "text": [
        {
          "text": items[0].json.asunto
        }
      ]
    },
    "Fecha": {
      "date": items[0].json.fecha
    },
    "Contenido": {
      "text": [
        {
          "text": items[0].json.contenido
        }
      ]
    }
  }
}
```
* Esto creará una nueva página en Notion con los datos extraídos.

Recuerda configurar cada nodo con tus credenciales y preferencias. ¡Espero que esto te ayude!