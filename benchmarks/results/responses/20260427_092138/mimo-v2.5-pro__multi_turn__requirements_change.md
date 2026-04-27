# MiMo V2.5-Pro (Xiaomi) — multi_turn/requirements_change

- model_id: `mimo-v2.5-pro`
- success: True  | final: 6.71 | quality: 6.04
- latency_total: 22.731s | tokens_per_second: 53.0
- input_tokens: 244 | output_tokens: 1205
- judge_score: 3.2 | justificación: 

## Respuesta completa

Perfecto, el workflow se adapta a tus nuevas necesidades. Aquí tienes la estructura completa:

## Workflow: Gmail → Filtro → Notion + Slack

### 1. **Gmail Trigger**
- **Tipo**: Gmail Trigger
- **Configuración**:
  - Evento: `messageReceived`
  - Filtro: `subject:('propuesta' OR 'cotización' OR 'cotizacion')`
  - (Nota: Gmail es case-insensitive y maneja acentos)

### 2. **Filtro de Palabras Clave** (Opcional pero recomendado)
- **Tipo**: IF Node
- **Configuración**:
  - Condición: `{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') || $json.subject.toLowerCase().includes('cotizacion') }}`
  - (Doble verificación por si el filtro de Gmail no funciona perfectamente)

### 3. **Function Node** (Para extraer datos)
- **Tipo**: Function Node
- **Código**:
```javascript
const email = $input.item.json;
const from = email.from.value[0];
const subject = email.subject;
const date = new Date(email.date).toISOString().split('T')[0];
const snippet = email.snippet || '';

return {
  json: {
    nombre: from.name || 'Sin nombre',
    email: from.address,
    asunto: subject,
    fecha: date,
    extracto: snippet.substring(0, 200), // Primeros 200 caracteres
    gmail_id: email.id
  }
};
```

### 4. **Notion Node**
- **Tipo**: Notion
- **Acción**: Create Database Item
- **Configuración**:
  - Database ID: (tu ID de base de datos en Notion)
  - Mapeo de propiedades:
    - **Nombre**: `{{ $json.nombre }}`
    - **Email**: `{{ $json.email }}`
    - **Asunto**: `{{ $json.asunto }}`
    - **Fecha**: `{{ $json.fecha }}`
    - **Extracto**: `{{ $json.extracto }}`
    - **Estado**: "Nuevo" (o el que uses)

### 5. **Slack Node**
- **Tipo**: Slack
- **Acción**: Post Message
- **Configuración**:
  - Canal: `#tu-canal` o `@tu-usuario`
  - Mensaje:
```
📧 *Nuevo email comercial*
*De:* {{ $json.nombre }} ({{ $json.email }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
*Extracto:* {{ $json.extracto.substring(0, 100) }}...
```

---

## **Consideraciones importantes:**

1. **Credenciales**: Necesitarás configurar:
   - OAuth de Gmail (con permisos de lectura)
   - API de Notion (con permisos de escritura en la base de datos)
   - Token de Slack (con permisos de escritura en canales)

2. **Base de datos en Notion**: Asegúrate de tener una base de datos con las columnas:
   - Nombre (texto)
   - Email (email)
   - Asunto (texto)
   - Fecha (fecha)
   - Extracto (texto)
   - Estado (selección)

3. **Manejo de errores**: Podrías añadir nodos de error para:
   - Notificar si falla la conexión con Notion
   - Loggear emails que no pasaron el filtro

¿Quieres que te detalle la configuración exacta de las credenciales o el mapeo de propiedades en Notion?