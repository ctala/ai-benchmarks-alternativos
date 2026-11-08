# Nemotron 3 Super — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 4.97 | quality: 4.0
- latency_total: 5.899s | tokens_per_second: 286.5
- input_tokens: 248 | output_tokens: 1690

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

Aquí tienes el flujo actualizado para **N8N** con Gmail → Filtro → Notion → Slack.

---

### 1. Nodos del Workflow

| Nodo | Propósito |
|------|-----------|
| **Gmail Trigger** | Detecta emails nuevos en tu bandeja de entrada |
| **IF** | Filtra solo si el asunto contiene "propuesta" o "cotización" |
| **Notion** | Crea una página en tu base de datos con los datos del email |
| **Slack** | Envía una notificación al canal que elijas |

---

### 2. Configuración paso a paso

#### Nodo 1: Gmail Trigger
- **Evento:** `Messages`
- **Cambios:** `New message`
- **Filtro (opcional pero recomendado):** En el campo *Filter* de Gmail puedes poner:
  ```
  subject:(propuesta OR cotización)
  ```
  Esto hace que n8n solo procadre emails que ya cumplan el criterio, ahorrando ejecuciones.  
  *Si lo dejas vacío, el filtro lo hacemos en el siguiente nodo.*

#### Nodo 2: IF (Filtro por asunto)
Si no usaste el filtro de Gmail, agrega un nodo **IF** con esta condición:

- **Valor 1:** `{{ $json["subject"]?.toLowerCase() }}`
- **Operación:** `includes`
- **Valor 2:** `propuesta`  
  *(O agrega una segunda condición con `cotización` usando "OR")*

> Solo la rama **True** continúa hacia Notion y Slack.

#### Nodo 3: Notion (Create Page)
- **Resource:** `Page`
- **Operation:** `Create`
- **Database ID:** selecciona tu base de datos de Notion (debes haber creado la integración en Notion y compartido la DB con ella)
- **Properties:** mapea los campos del email. Ejemplo:

| Propiedad Notion | Valor (expresión n8n) |
|------------------|----------------------|
| Nombre (Title) | `{{ $json["fromName"] }}` |
| Email | `{{ $json["fromEmail"] }}` |
| Asunto | `{{ $json["subject"] }}` |
| Fecha | `{{ $json["receivedAt"] }}` |
| Remitente | `{{ $json["fromName"] }} <{{ $json["fromEmail"] }}>` |

> **Importante:** En Notion necesitas un *Integration Token* interno y haber compartido la base de datos con esa integración desde la interfaz de Notion.

#### Nodo 4: Slack (Send Message)
- **Channel:** selecciona el canal (ej. `#ventas` o `#alertas`)
- **Text:**
  ```
  📧 Nuevo email de propuesta/cotización
  
  *De:* {{ $json["fromName"] }} ({{ $json["fromEmail"] }})
  *Asunto:* {{ $json["subject"] }}
  *Fecha:* {{ $json["receivedAt"] }}
  ```

---

### 3. Conexiones (orden de ejecución)

```
Gmail Trigger ──▶ IF ──▶ Notion ──▶ Slack
                      │
                      └── (False: no hace nada)
```

---

### 4. Requisitos previos

1. **Gmail:** Credenciales OAuth2 configuradas en n8n.
2. **Notion:** 
   - Crear una integración en [notion.so/my-integrations](https://www.notion.so/my-integrations)
   - Copiar el *Internal Integration Token*
   - Crear una base de datos y compartirla con la integración (menú ⋯ → Add connections)
3. **Slack:** Crear una app en [api.slack.com](https://api.slack.com) con permisos `chat:write` y conectarla en n8n.

---

¿Quieres que te pase el JSON del workflow para importarlo directamente en tu n8n, o prefieres que te ayude a configurar las credenciales de alguna plataforma en particular?