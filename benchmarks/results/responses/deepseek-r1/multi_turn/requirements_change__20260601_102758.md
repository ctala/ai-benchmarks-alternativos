# DeepSeek R1 (reasoning) — multi_turn/requirements_change

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 4.66 | quality: 4.64
- latency_total: 214.656s | tokens_per_second: 25.6
- input_tokens: 244 | output_tokens: 5487
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en un Google Sheet, sino que cambia a Notion y Slack, lo que la hace irrelevante. Aunque la estructura del workflow es correcta, no se ajusta a la instrucción original.

## Respuesta completa

Perfecto, aquí está el workflow modificado para N8N con Gmail → Filtro → Notion + Slack:

```json
{
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "resource": "message",
        "operation": "getAll",
        "format": "resolved",
        "options": {
          "labelIDs": ["INBOX"]
        },
        "returnAll": false,
        "limit": 5
      },
      "name": "Gmail",
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "gmailOAuth2Api": "TU_CREDENCIAL_GMAIL"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{$json[\"subject\"]}}",
              "operation": "contains",
              "value2": "propuesta"
            },
            {
              "value1": "{{$json[\"subject\"]}}",
              "operation": "contains",
              "value2": "cotizacion"
            }
          ],
          "options": {
            "caseSensitive": false
          }
        }
      },
      "name": "Filtro de Asunto",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [700, 300]
    },
    {
      "parameters": {
        "functionCode": "// Extraer datos del remitente\nconst from = $item.json.from.value[0];\nreturn {\n  json: {\n    nombre: from.name || '',\n    email: from.address || '',\n    asunto: $item.json.subject || '',\n    fecha: $item.json.date || ''\n  }\n};"
      },
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [950, 200]
    },
    {
      "parameters": {
        "operation": "create",
        "databaseId": "TU_ID_DE_BASE_DE_DATOS_NOTION",
        "properties": {
          "properties": {
            "Nombre": {
              "title": [
                {
                  "text": {
                    "content": "{{$json[\"nombre\"]}}"
                  }
                }
              ]
            },
            "Email": {
              "email": "{{$json[\"email\"]}}"
            },
            "Asunto": {
              "rich_text": [
                {
                  "text": {
                    "content": "{{$json[\"asunto\"]}}"
                  }
                }
              ]
            },
            "Fecha": {
              "date": {
                "start": "{{$json[\"fecha\"]}}"
              }
            }
          }
        }
      },
      "name": "Guardar en Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [1200, 200],
      "credentials": {
        "notionApi": "TU_CREDENCIAL_NOTION"
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "operation": "post",
        "text": "Nuevo email importante recibido:\n*De*: {{$json[\"nombre\"]}} ({{$json[\"email\"]}})\n*Asunto*: {{$json[\"asunto\"]}}\n*Fecha*: {{$json[\"fecha\"]}}",
        "channel": "CANAL_SLACK",
        "options": {}
      },
      "name": "Notificar en Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1200, 400],
      "credentials": {
        "slackApi": "TU_CREDENCIAL_SLACK"
      }
    }
  ],
  "connections": {
    "Start": {
      "main": [[{ "node": "Gmail", "type": "main", "index": 0 }]]
    },
    "Gmail": {
      "main": [[{ "node": "Filtro de Asunto", "type": "main", "index": 0 }]]
    },
    "Filtro de Asunto": {
      "main": [
        [
          { "node": "Extraer Datos", "type": "main", "index": 0 },
          { "node": "Notificar en Slack", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [[{ "node": "Guardar en Notion", "type": "main", "index": 0 }]]
    }
  }
}
```

**Pasos de configuración esenciales:**

1. **Credenciales:**
   - Gmail: Configura OAuth2 en N8N
   - Notion: Crea una integración y comparte tu base de datos con ella
   - Slack: Genera token de acceso en api.slack.com

2. **Preparar base de datos en Notion:**
   - Crea una base de datos con estas propiedades:
     - `Nombre` (title)
     - `Email` (email)
     - `Asunto` (rich text)
     - `Fecha` (date)
   - Copia el ID de la base de datos de la URL

3. **Filtro mejorado:**
   - Busca "propuesta" o "cotizacion" en el asunto (case-insensitive)
   - Los emails sin estas palabras serán descartados automáticamente

4. **Función personalizada:**
   - Extrae nombre y email del remitente
   - Captura asunto y fecha del mensaje

5. **Notificación en Slack:**
   - Mensaje formateado con los datos clave
   - Incluye emojis para mejor visualización (opcional)

**Recomendaciones:**
1. Prueba primero con modo "Manual" en el nodo Gmail
2. Verifica los permisos de la integración de Notion
3. Ajusta el formato de fecha si es necesario en el nodo de Notion
4. Para mayor seguridad, agrega un nodo de delay después de Gmail

¿Necesitas ayuda con la configuración de las credenciales o ajustar algún detalle específico?