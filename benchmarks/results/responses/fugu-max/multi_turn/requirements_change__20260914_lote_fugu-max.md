# Fugu Max — multi_turn/requirements_change

- model_id: `sakana/fugu-max`
- success: True  | final: 5.51 | quality: 6.0
- latency_total: 40.386s | tokens_per_second: 70.1
- input_tokens: 398 | output_tokens: 2831

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

Aquí tienes el flujo actualizado con Gmail → filtro → Notion → Slack.

**1. Nodo Gmail Trigger**  
- Evento: **New Email**  
- Activa la opción **Simplify** (así `subject`, `from` y `date` vienen como campos directos).  
- Configura el intervalo de polling (por ejemplo, cada 1 minuto).

**2. Nodo Function (para separar nombre y email del remitente)**  
Agrega un nodo Function y pega este código:

```javascript
const from = $json.from; // Ej: "Juan Pérez <juan@empresa.com>"
const match = from.match(/^(.*)<(.+)>$/);

let name = from;
let email = from;
if (match) {
  name = match[1].trim();
  email = match[2];
}

return {
  json: {
    name,
    email,
    subject: $json.subject,
    date: $json.date,
    raw_from: from
  }
};
```

**3. Nodo IF (filtrar asuntos)**  
- Modo: **Match Any (OR)**  
- Condición 1: `{{ $json.subject.toLowerCase() }}` → **Contains** → `propuesta`  
- Condición 2: `{{ $json.subject.toLowerCase() }}` → **Contains** → `cotizacion`  
*(Usamos `toLowerCase()` para ignorar mayúsculas/minúsculas)*

**4. Nodo Notion (guardar datos)**  
- Operación: **Create Page**  
- Database ID: tu base de datos de Notion  
- Mapea las propiedades según tu esquema, por ejemplo:  
  - Título (Title) = `{{ $json.subject }}`  
  - Remitente (Rich Text) = `{{ $json.name }}`  
  - Email (Email) = `{{ $json.email }}`  
  - Fecha (Date) = `{{ $json.date }}`

**5. Nodo Slack (notificación)**  
- Operación: **Send Message**  
- Canal: el que prefieras (ej: `#ventas`)  
- Mensaje:  
  ```
  📩 Nuevo correo relevante de {{ $json.name }} ({{ $json.email }})
  Asunto: {{ $json.subject }}
  ```

**Consejos finales**  
- Guarda y activa el workflow.  
- Prueba con un correo de prueba que tenga "propuesta" en el asunto y verifica que llegue a Notion y Slack.  
- Si quieres evitar duplicados en Notion, añade una propiedad única (ej: Email ID) y valida antes de insertar.

¿Quieres que te detalle alguna parte, como el mapeo de propiedades en Notion o el filtro con múltiples palabras?