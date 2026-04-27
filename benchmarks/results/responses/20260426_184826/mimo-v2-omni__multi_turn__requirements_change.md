# MiMo-V2-Omni (multimodal) — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 6.15 | quality: 5.28
- latency_total: 10.914s | tokens_per_second: 89.8
- input_tokens: 244 | output_tokens: 980
- judge_score: 2.4 | justificación: 

## Respuesta completa

Excelente, ese flujo es más completo. Te detallo el workflow paso a paso:

## **Workflow: Gmail → Filtro → Notion + Slack**

### **Estructura del flujo:**
```
1. Gmail Trigger (Email nuevo)
2. IF Node (Filtro por asunto)
3. └── Si es TRUE:
     ├── Notion Node (Guardar datos)
     └── Slack Node (Notificación)
```

### **Configuración detallada:**

#### **1. Gmail Trigger**
- **Event**: `Message Received`
- **Filters**: Dejar vacío (filtraremos después)
- **Output**: Todos los campos del email

#### **2. IF Node (Filtro)**
```
Condition:
{{ $json.subject.toLowerCase() }} CONTAINS 'propuesta' OR
{{ $json.subject.toLowerCase() }} CONTAINS 'cotizacion' OR
{{ $json.subject.toLowerCase() }} CONTAINS 'cotización'
```
- **True Output**: Continúa al siguiente nodo
- **False Output**: Termina el flujo

#### **3. Notion Node**
- **Operation**: `Create a Database Item`
- **Database**: Seleccionar tu base de datos de Notion
- **Fields mapping**:
  - **Título**: `{{ $json.subject }}`
  - **Email remitente**: `{{ $json.from.value[0].address }}`
  - **Nombre remitente**: `{{ $json.from.value[0].name }}`
  - **Fecha**: `{{ $json.date }}`
  - **Contenido**: `{{ $json.text }}` (primeros 500 caracteres)
  - **Estado**: "Nuevo" (o como tengas configurado)

#### **4. Slack Node**
- **Operation**: `Post Message`
- **Channel**: Tu canal de Slack
- **Message**:
```
📧 Nueva propuesta/cotización recibida:
*De*: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
*Asunto*: {{ $json.subject }}
*Fecha*: {{ $json.date }}
```
- **Attachments**: Opcional, puedes agregar el contenido del email

### **Consideraciones importantes:**

1. **Credenciales**: Necesitas configurar:
   - Gmail OAuth2
   - Notion Integration (con token de acceso)
   - Slack Bot Token

2. **Campos en Notion**: Asegúrate de que tu base de Notion tenga estos campos:
   - Título (Title)
   - Email (Text)
   - Nombre (Text)
   - Fecha (Date)
   - Contenido (Text)

3. **Manejo de errores**: Considera agregar un nodo de Error Trigger para capturar fallos.

4. **Prueba**: Usa emails de prueba con las palabras clave para verificar.

### **Optimización opcional:**
- Agregar un **Function Node** para limpiar datos antes de enviar a Notion
- Usar **Split Out** si un email tiene múltiples destinatarios
- Agregar **Wait Node** si necesitas procesamiento adicional

¿Necesitas ayuda con la configuración específica de alguna de las credenciales (Notion o Slack)?