# MiMo-V2.5 (omnimodal) — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 4.48 | quality: 4.0
- latency_total: 18.171s | tokens_per_second: 71.2
- input_tokens: 244 | output_tokens: 1293
- judge_score: 3.0 | justificación: La respuesta es precisa y clara, pero no aborda los requisitos originales de guardar datos en Google Sheets, en su lugar introduce un nuevo flujo de trabajo con Notion y Slack, lo que reduce su relevancia y coherencia contextual.

## Respuesta completa

Perfecto, voy a adaptar el workflow con esos cambios. Aquí tienes la estructura paso a paso:

### Workflow: Filtrar emails importantes → Guardar en Notion → Notificar en Slack

---

## **Paso 1: Gmail Trigger**
- **Nodo**: `Gmail Trigger`
- **Evento**: `Message Received`
- **Opciones**:
  - `Poll Times`: Cada 5 minutos (o ajustar según necesidad)
  - `Filters`: Solo emails no leídos (recomendado)

---

## **Paso 2: Filtrar emails (Function Node)**
```javascript
// Node: Filtrar por asunto
const subject = $input.item.json.subject.toLowerCase();
const palabrasClave = ['propuesta', 'cotización', 'cotizacion'];

// Verificar si alguna palabra clave está en el asunto
const contiene = palabrasClave.some(palabra => subject.includes(palabra));

if (!contiene) {
  // Si no contiene, terminamos aquí
  return [];
}
return $input.all();
```

---

## **Paso 3: Extraer datos (Function Node)**
```javascript
// Node: Extraer datos del email
const email = $input.item.json;

return {
  nombre: email.from.name || 'Sin nombre',
  email_remitente: email.from.address,
  asunto: email.subject,
  fecha: email.date,
  preview: email.textPlain ? email.textPlain.substring(0, 200) : ''
};
```

---

## **Paso 4: Guardar en Notion**
- **Nodo**: `Notion`
- **Operación**: `Create Database Item`
- **Configuración**:
  - **Database ID**: El ID de tu base de datos de Notion
  - **Properties** (mapear así):
    ```
    Nombre: {{ $json.nombre }}
    Email: {{ $json.email_remitente }}
    Asunto: {{ $json.asunto }}
    Fecha: {{ $json.fecha }}
    Preview: {{ $json.preview }}
    ```

---

## **Paso 5: Notificar en Slack**
- **Nodo**: `Slack`
- **Operación**: `Send Message`
- **Channel**: `#proyectos` (o el canal que uses)
- **Message Text**:
  ```
  📧 *Nuevo email de propuesta/cotización* 
  
  *De:* {{ $json.nombre }} ({{ $json.email_remitente }})
  *Asunto:* {{ $json.asunto }}
  *Fecha:* {{ $json.fecha }}
  
  _Guardado en Notion. Verificar en la base de datos._
  ```

---

## **Requisitos previos**:
1. **Credenciales en N8N**:
   - Gmail API (OAuth2)
   - Notion API Integration (con permisos de escritura)
   - Slack Bot Token

2. **Base de datos en Notion**:
   - Crear propiedades: Nombre (Title), Email (Email), Asunto (Text), Fecha (Date), Preview (Text)

¿Quieres que te ayude con la configuración de alguna credencial específica o la estructura de la base de datos en Notion?