# Kimi K2.5 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.34 | quality: 6.0
- latency_total: 3.398s | tokens_per_second: 67.7
- input_tokens: 267 | output_tokens: 230

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

 Perfecto, mejor flujo. Te detallo los nodos necesarios:

**Nodos del workflow:**

1. **Gmail Trigger** → Modo: "On message received"

2. **IF node** → Condición: `{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}`

3. **Notion node** → Action: "Create a page"
   - Database: seleccionas tu base de contactos/prospectos
   - Mapeas: nombre, email, asunto, fecha, snippet del body

4. **Slack node** → Action: "Post a message"
   - Canal: #leads o el que uses
   - Mensaje: resumen con link al registro en Notion

**Estructura en Notion sugerida:**
| Nombre | Email | Asunto | Fecha | Fuente | Estado |

¿Tienes ya la base de datos en Notion creada o necesitas que te sugiera cómo estructurarla?