# MiMo V2.5 (Xiaomi) — multi_turn/requirements_change

- model_id: `mimo-v2.5`
- success: True  | final: 6.84 | quality: 6.4
- latency_total: 11.928s | tokens_per_second: 84.8
- input_tokens: 244 | output_tokens: 1011
- judge_score: 3.2 | justificación: 

## Respuesta completa

Perfecto, entendido. Aquí tienes el workflow actualizado con todos los requisitos:

## **Workflow N8N: Emails → Notion + Slack**

### **Pasos del workflow:**

1. **Gmail Trigger** → Se activa con cada email nuevo
2. **Filtro IF** → Solo emails con "propuesta" o "cotización" en el asunto
3. **Function** → Extrae y formatea datos del remitente
4. **Notion** → Crea una página en tu base de datos
5. **Slack** → Envía notificación al canal designado

---

### **Configuración detallada:**

#### **1. Gmail Trigger**
- **Poll Times**: Every 5 minutes
- **Filters**: No aplicar filtros aquí (los haremos en el siguiente nodo)

#### **2. Filtro IF**
- **Condition**: Text contains "propuesta" O "cotización"
- **Field**: `{{ $json.subject }}`
- **Operator**: Contains (case insensitive)
- **Value 1**: `propuesta`
- **Value 2**: `cotización`
- **Combinar**: Any (OR)

#### **3. Function Node (Extraer datos)**
```javascript
return {
  nombre: $json.from.value[0].name,
  email: $json.from.value[0].address,
  asunto: $json.subject,
  fecha: $json.date,
  snippet: $json.snippet,
  messageId: $json.id
};
```

#### **4. Notion Node**
- **Operation**: Create Page
- **Database**: Seleccionar tu base de datos
- **Properties** (ejemplo):
  - **Nombre** (Title): `{{ $json.nombre }}`
  - **Email** (Email): `{{ $json.email }}`
  - **Asunto** (Rich Text): `{{ $json.asunto }}`
  - **Fecha** (Date): `{{ $json.fecha }}`
  - **Snippet** (Rich Text): `{{ $json.snippet }}`
  - **Estado** (Select): "Nuevo"

#### **5. Slack Node**
- **Channel**: #ventas-leads (o el que prefieras)
- **Text**: 
```
🎯 *Nuevo lead importante:*
*De:* {{ $json.nombre }} ({{ $json.email }})
*Asunto:* {{ $json.asunto }}
*Preview:* {{ $json.snippet }}...
```

---

### **Notas importantes:**

1. **Credenciales**: Necesitarás configurar:
   - Gmail OAuth2
   - Notion Integration Token
   - Slack Bot Token

2. **Base de datos Notion**: Asegúrate de crear una base con las propiedades mencionadas antes de activar el workflow.

3. **Filtros avanzados**: Si quieres agregar más palabras clave, solo modifica el nodo IF agregando más condiciones.

¿Quieres que te ayude con:
- La configuración específica de credenciales?
- Crear la estructura exacta en Notion?
- Ajustar el formato del mensaje de Slack?
- Agregar más campos o filtros?