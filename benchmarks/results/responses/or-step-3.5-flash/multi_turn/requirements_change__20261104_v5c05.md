# Step 3.5 Flash — multi_turn/requirements_change

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 4.71 | quality: 4.0
- latency_total: 28.03s | tokens_per_second: 98.5
- input_tokens: 264 | output_tokens: 2761

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

Excelente ajuste. Aquí tienes el workflow actualizado:

## **Workflow: Gmail → Notion + Slack**

### **1. Gmail Trigger**
- **Tipo**: "On new email"
- **Configuración**: 
  - Conecta tu cuenta Gmail
  - Opcional: Puedes especificar etiqueta/carpeta si solo quieres monitorear emails específicos

### **2. Filtro (IF Node)**
**Condición** (case-insensitive):
```javascript
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') }}
```
*(Ajusta "cotización" si usas "cotizacion" sin tilde)*

### **3. Function Node (Extracción y formateo)**
```javascript
// Parsear remitente
const from = $input.first().json.from;
let nombre = '';
let email = '';

if (from) {
  const match = from.match(/^(.*)<(.*)>$/);
  if (match) {
    nombre = match[1].trim();
    email = match[2].trim();
  } else {
    email = from.trim();
  }
}

// Formatear fecha para Notion (ISO 8601)
const fecha = new Date().toISOString();

return {
  json: {
    nombre: nombre || 'Sin nombre',
    email: email,
    asunto: $input.first().json.subject,
    fecha: fecha,
    body: $input.first().json.text || $input.first().json.body || ''
  }
};
```

### **4. Notion Node**
- **Conexión**: Conecta tu cuenta Notion
- **Acción**: "Create" en tu base de datos
- **Mapeo de propiedades** (ajusta según tus columnas en Notion):
  ```
  Nombre → {{ $json.nombre }}
  Email → {{ $json.email }}
  Asunto → {{ $json.asunto }}
  Fecha → {{ $json.fecha }}
  Contenido → {{ $json.body }}
  ```

### **5. Slack Node**
- **Conexión**: Tu cuenta Slack
- **Acción**: "Send Message"
- **Canal**: #notificaciones o el que prefieras
- **Mensaje**:
  ```
  🚀 Nueva propuesta/cotización recibida:
  
  *Remitente*: {{ $json.nombre }} ({{ $json.email }})
  *Asunto*: {{ $json.asunto }}
  *Fecha*: {{ $json.fecha }}
  
  _Revisar en Notion para detalles completos_
  ```

---

## **Configuraciones clave:**

### **Para Notion:**
1. Crea una base de datos en Notion con estas propiedades:
   - `Nombre` (Título o Texto)
   - `Email` (Email o Texto)
   - `Asunto` (Texto)
   - `Fecha` (Fecha)
   - `Contenido` (Texto largo)

2. En el nodo Notion de n8n:
   - Selecciona tu base de datos
   - Elige "Create" como acción
   - Mapea cada propiedad con los datos del Function node

### **Para Slack:**
- Asegúrate que el bot de n8n esté añadido al canal
- Puedes usar emojis y formato Markdown en el mensaje

---

## **Flujo completo:**
```
Gmail Trigger → IF (filtro) → Function → [Notion] → [Slack]
                                 ↖___________↙
```

### **Notas importantes:**
1. **Pruebas**: Activa "Test workflow" con emails reales de prueba
2. **Rate limits**: Gmail y Notion tienen límites de API (verifica cuotas)
3. **Errores**: Considera agregar un nodo "Error Trigger" para notificar fallos
4. **Filtro adicional**: Si necesitas filtrar por remitente específico, ajusta el IF node

¿Necesitas ayuda con alguna configuración específica de credenciales o propiedades en Notion?