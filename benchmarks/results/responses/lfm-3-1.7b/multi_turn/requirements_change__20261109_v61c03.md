# LFM-3 1.7B — multi_turn/requirements_change

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 5.08 | quality: 4.0
- latency_total: 6.762s | tokens_per_second: 281.4
- input_tokens: 253 | output_tokens: 1903

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

**Workflow N8N – Emails de Gmail → Notion + Slack**

```
┌─────────────┐
│  Trigger    │  Gmail Trigger (new mail)
└──────┬──────┘
       │
       ▼
┌─────────────┐      ┌───────────────────────┐
│ Filter node │◄─────│  IF ( subject LIKE “%propuesta%” 
│             │      │   OR subject LIKE “%cotizacion%” ) → go to next node else stop
└──────┬──────┘      └───────────┬─────────────┘
       │                         │
       ▼                         ▼
┌─────────────────┐   ┌───────────────────────┐
│  Extract fields │   │  (same output)         │
│  - From (name)  │   │                       │
│  - To (email)   │   │                       │
│  - Subject      │   │                       │
│  - Sent date    │   ▼                       │
└──────┬──────────┘  ┌───────────────────────┐
       │          │  Branch                │
       ▼          │                       │
┌─────────────────┐│  NOTION NODE:           │
│  Notion          ││  • Create/append a row  │
│  - New item     ││  • Database: …          │
└──────┬──────────┘│  • Workspace: …         │
       │          └───────────────┬───────┘
       │                      │
       ▼                     ▼
┌─────────────────┐   ┌───────────────────────┐
│  Slack          │   │  SLACK NODE:           │
│  - Notify (webh)│   │  • POST to channel/webhook │
│  • On each email│   • Message: “New Gmail: <subject>” │
└─────────────────┘   └───────────────────────┘
```

---

### Detalle de cada nodo

| Nodo | Tipo | Configuración clave |
|------|------|---------------------|
| **Gmail Trigger** | Trigger | Evento `new-mail` desde Gmail. Ingresa la cuenta de Gmail en *Settings > Account* y selecciona la carpeta o el flag “All”. |
| **Filter** | Condición | `subject like "%propuesta%" OR subject like "%cotizacion%"` (insensible a mayúsculas/minúsculas). En N8N: `{{ $subject }} contains "propuesta" or {{ $subject }} contains "cotizacion" }`. Solo pasa si es verdadero. |
| **Function (Extraction)** | Función simple | Usa las variables `$from`, `$to`, `$subject`, `$dateReceived` (si está disponible) para extraer campos. Ejemplo: <br>`split($from, "@")[0] AS Name`<br>`$to AS ToEmail`<br>`$subject AS Subject`<br>`formatDateTime($dateReceived, "yyyy-MM-dd") AS SentDate` |
| **Notion – Create Item** | Integration | <br>• **Database**: Crea un nuevo item (tabla de Entrada) o un recurso. <br>• **Title/Key**: Usa el campo `Name` del remitente. <br>• **Fields**: Mapa los valores: `ToEmail`, `Subject`, `SentDate`. <br>• **Workspace**: Insert your workspace ID (`https://app.notion.com/_share/{WSP}`). |
| **Slack – Send Message** | Integration | <br>• **Webhook URL**: Obtenga el URL del canal o app en Slack. <br>• **Payload** (JSON): `{ "text": "📧 Nueva propuesta: ` + $subject + ` (de $to)" }`. <br>• **Channel**: Elimina o usa un nombre específico. |

---

### Flujo resumido

1. **Gmail Trigger** recibe cada nuevo correo.  
2. **Filter** descarta todo que no contenga “propuesta” o “cotizacion”.  
3. Los datos se extraen (Remitente = parte antes del `@`, Email = full address, Asunto, Fecha).  
4. El flujo se divide:  
   - Rama **Notion** crea/agrega un nuevo registro en tu base de datos Notion.  
   - Rama **Slack** envía un mensaje automático cuando llega cualquier correo que cumpla el filtro.  

---

### Próximos pasos

1. **Crea la cuenta/dominio** en Gmail y genera un token webhook en Slack.  
2. **Abre N8N**, crea el nuevo workflow y copia la secuencia de nodos usando la tabla anterior.  
3. En el nodo *Create Item* Notion, pon tus ID de trabajo y nombre de la base de datos.  
4. Prueba ejecutando con **“Run now”** para ver que solo se procesan los emails relevantes.

¿Necesitas ayuda para configurar el filtro de palabras clave o para conectar tu dominio a Gmail/Slack?