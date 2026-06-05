# Qwen 3.7 Max — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.14 | quality: 7.48
- latency_total: 50.513s | tokens_per_second: 68.4
- input_tokens: 125 | output_tokens: 3455
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el workflow completo de n8n en JSON. Para importarlo: en n8n ve a **Workflows → Add workflow → menú (⋮) → Import from File** (o pega el JSON directamente con Ctrl+V en el canvas).

```json
{
  "name": "Clasificador de Mensajes con IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y responde ÚNICAMENTE con una de estas tres palabras exactas (en minúsculas, sin comillas, sin puntuación, sin texto adicional): soporte, ventas, otro.\n\n- 'soporte': preguntas técnicas, reportes de errores, problemas con el producto, solicitudes de ayuda.\n- 'ventas': interés en comprar, precios, planes, demos, contrataciones.\n- 'otro': cualquier cosa que no encaje en las dos categorías anteriores."
            },
            {
              "role": "user",
              "content": "=Email del remitente: {{ $json.email }}\n\nMensaje:\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL_OPENAI",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Normalizamos la respuesta de la IA a una categoría válida\nconst raw = ($input.first().json.message?.content || $input.first().json.text || '').toString().trim().toLowerCase();\n\nlet categoria = 'otro';\nif (raw.includes('soporte') || raw.includes('support')) categoria = 'soporte';\nelse if (raw.includes('ventas') || raw.includes('sales')) categoria = 'ventas';\n\nconst prev = $('Extraer email y message').first().json;\n\nreturn [{\n  json: {\n    email: prev.email,\n    message: prev.message,\n    categoria: categoria,\n    respuestaIA: raw\n  }\n}];"
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Parsear clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": { "caseSensitive": true, "typeValidation": "strict" },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "soporte",
                    "operator": { "type": "string", "operation": "equals" }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": { "caseSensitive": true, "typeValidation": "strict" },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "ventas",
                    "operator": { "type": "string", "operation": "equals" }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": { "caseSensitive": true, "typeValidation": "strict" },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "otro",
                    "operator": { "type": "string", "operation": "equals" }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": { "fallbackOutput": "extra", "fallbackOutputKey": "otro" }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Router por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🛠️ *Nuevo ticket de SOPORTE*\n*De:* {{ $json.email }}\n*Categoría detectada:* {{ $json.categoria }}\n\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 140],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva oportunidad de VENTAS*\n*De:* {{ $json.email }}\n*Categoría detectada:* {{ $json.categoria }}\n\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📩 *Mensaje GENERAL*\n*De:* {{ $json.email }}\n*Categoría detectada:* {{ $json.categoria }}\n\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 460],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [{ "node": "Extraer email y message", "type": "main", "index": 0 }]
      ]
    },
    "Extraer email y message": {
      "main": [
        [{ "node": "Clasificar con OpenAI", "type": "main", "index": 0 }]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [{ "node": "Parsear clasificación", "type": "main", "index": 0 }]
      ]
    },
    "Parsear clasificación": {
      "main": [
        [{ "node": "Router por categoría", "type": "main", "index": 0 }]
      ]
    },
    "Router por categoría": {
      "main": [
        [{ "node": "Enviar a #support", "type": "main", "index": 0 }],
        [{ "node": "Enviar a #sales", "type": "main", "index": 0 }],
        [{ "node": "Enviar a #general", "type": "main", "index": 0 }]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "tags": []
}
```

---

### 🔧 Pasos para ponerlo en producción

1. **Credenciales**: Reemplaza los dos `REEMPLAZA_CON_TU_CREDENCIAL_...` con tus credenciales reales de **OpenAI** y **Slack** en n8n (menú Credentials → Add credential).
2. **Canales de Slack**: Asegúrate de que existan los canales `#support`, `#sales` y `#general` en tu workspace, y de que la app de Slack tenga permisos `chat:write` y esté invitada a cada canal.
3. **Activar webhook**: Activa el workflow (toggle superior derecho) y copia la **Production URL** del nodo Webhook. Será algo como:
   ```
   https://tu-n8n.com/webhook/clasificar-mensaje
   ```
4. **Probar con curl**:
   ```bash
   curl -X POST https://tu-n8n.com/webhook/clasificar-mensaje \
     -H "Content-Type: application/json" \
     -d '{
       "email": "cliente@ejemplo.com",
       "message": "Hola, me interesa conocer los precios del plan empresarial."
     }'
   ```

### 🧠 Notas de diseño

- **Prompt restrictivo**: el system prompt fuerza a la IA a responder *solo* con una de las tres palabras clave, lo que hace el parsing posterior trivial y robusto.
- **Parsing tolerante**: el nodo `Parsear clasificación` usa `includes()` en lugar de `===`, así que aunque la IA devuelva `"soporte."` o `"Soporte"` seguirá funcionando.
- **Fallback**: el Switch está configurado con `fallbackOutput: "extra"` apuntando a `otro`, por lo que cualquier categoría inesperada termina en `#general` en lugar de perderse.
- **Temperature 0**: garantiza respuestas deterministas para la misma entrada.