# Devstral 2 (Dic 2025) — multi_turn/requirements_change

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.23 | quality: 8.36
- latency_total: 10.747s | tokens_per_second: 77.7
- input_tokens: 227 | output_tokens: 835
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Perfecto! Vamos a ajustar el workflow para que:

1. **Filtre emails** con "propuesta" o "cotización" en el asunto.
2. **Guarde los datos en Notion** (creando una entrada en una base de datos).
3. **Envíe una notificación a Slack** cuando se procese un email válido.

---

### **Workflow en n8n**
#### **1. Nodo: Gmail Trigger (IMAP)**
- **Operación**: `Receive Emails` (IMAP).
- **Configuración**:
  - Conecta tu cuenta de Gmail (OAuth2).
  - Filtra por `UNSEEN` (emails no leídos).
  - **Opcional**: Si quieres procesar solo emails nuevos, marca `Mark as Read` después de procesarlos.

#### **2. Nodo: IF (Filtro por asunto)**
- **Condición**:
  ```javascript
  // Busca "propuesta" o "cotización" (case-insensitive)
  const subject = $input.item(0).json.subject.toLowerCase();
  return subject.includes("propuesta") || subject.includes("cotizacion");
  ```
- **Salidas**:
  - **True**: Continúa al siguiente nodo (Notion + Slack).
  - **False**: Termina el flujo para ese email.

#### **3. Nodo: Notion (Crear entrada en base de datos)**
- **Operación**: `Create a Database Item`.
- **Configuración**:
  - Conecta tu cuenta de Notion (API Key + Database ID).
  - **Campos a mapear** (ejemplo):
    | Campo en Notion | Valor (desde Gmail)       |
    |-----------------|---------------------------|
    | Nombre          | `{{$node["Gmail"].json[0].from.name}}` |
    | Email           | `{{$node["Gmail"].json[0].from.email}}` |
    | Asunto          | `{{$node["Gmail"].json[0].subject}}`    |
    | Fecha           | `{{$node["Gmail"].json[0].date}}`      |
    | Contenido       | `{{$node["Gmail"].json[0].textBody}}`  |

#### **4. Nodo: Slack (Notificación)**
- **Operación**: `Send Message`.
- **Configuración**:
  - Conecta tu cuenta de Slack (Webhook o OAuth).
  - **Mensaje**:
    ```
    📧 *Nuevo email con propuesta/cotización*
    - **De**: {{ $node["Gmail"].json[0].from.name }} ({{ $node["Gmail"].json[0].from.email }})
    - **Asunto**: {{ $node["Gmail"].json[0].subject }}
    - **Fecha**: {{ $node["Gmail"].json[0].date }}
    - *Guardado en Notion*.
    ```

---

### **Ejemplo visual del flujo**:
```
Gmail Trigger → IF (filtro) → Notion (guardar) → Slack (notificar)
```

### **Notas importantes**:
1. **Notion API**:
   - Necesitas una **base de datos en Notion** con los campos mencionados.
   - La API de Notion usa un **Database ID** (lo encuentras en la URL de tu base de datos).

2. **Slack**:
   - Si usas un **Webhook**, configúralo en tu canal de Slack.
   - Si usas OAuth, asegúrate de tener permisos para enviar mensajes.

3. **Pruebas**:
   - Ejecuta el workflow en modo **test** con un email de prueba que incluya "propuesta" o "cotización".

¿Quieres que te ayude con la configuración específica de algún nodo? 😊