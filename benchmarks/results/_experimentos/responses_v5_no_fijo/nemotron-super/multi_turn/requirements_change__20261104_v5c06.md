# Nemotron 3 Super — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.02 | quality: 6.0
- latency_total: 35.718s | tokens_per_second: 90.8
- input_tokens: 248 | output_tokens: 3242

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

¡Entendido! Aquí tienes el workflow optimizado para N8N con tus nuevos requisitos: **filtrar emails por asunto ("propuesta" o "cotizacion"), extraer datos del remitente, guardarlos en Notion y enviar notificación a Slack**. Incluyo detalles críticos para evitar errores comunes.

---

### 📋 **Workflow Completo (5 Nodos)**
*(Orden de ejecución: 1 → 2 → 3 → 4 → 5)*

#### **1. Trigger: Gmail**  
*(Lee emails nuevos con filtro previo en el asunto)*  
- **Evento**: `Watch Emails`  
- **Configuración clave**:  
  - `Search Query`: `subject:(propuesta OR cotizacion)`  
    *(Nota: Usa sintaxis de búsqueda de Gmail. Esto filtra **antes** de procesar, ahorrando ejecuciones innecesarias)*  
  - `Label`: `INBOX` (o deja vacío para todas las carpetas)  
  - `Mark as Read`: `No` (opcional, según tu preferencia)  
  - `Include Spam & Trash`: `No`  
- **Salida**: Solo emails cuyo asunto contenga "propuesta" **o** "cotizacion" (case-insensitive).

#### **2. Function: Parsear Remitente**  
*(Extrae nombre y email limpio del campo "from" de Gmail)*  
- **Nombre del nodo**: `Parse Sender`  
- **Código**:  
  ```javascript
  const from = $json["from"]; // Ej: "Juan Pérez <juan@email.com>"
  
  // Extraer email entre < >
  const emailMatch = from.match(/<([^>]+)>/);
  const email = emailMatch ? emailMatch[1] : from; // Si no hay <>, asume que todo es email
  
  // Extraer nombre (todo antes del < )
  const nameMatch = from.match(/^([^<]+)</);
  const name = nameMatch ? nameMatch[1].trim() : email; // Si no hay nombre, usa email
  
  return [
    {
      json: {
        senderName: name,
        senderEmail: email,
        subject: $json["subject"],
        receivedAt: $json["date"] // ISO 8601 (ej: "2024-06-15T10:30:00Z")
      }
    }
  ];
  ```
- **Por qué Function y no Set?**  
  Gmail devuelve el remitente en formato `"Nombre <email@domain.com>"`. Este nodo lo separa limpiamente para Notion.

#### **3. Notion: Crear Página en Base de Datos**  
*(Guarda los datos en tu base de datos de Notion)*  
- **Nombre del nodo**: `Save to Notion`  
- **Configuración crítica**:  
  - `Resource`: `Page`  
  - `Operation`: `Create`  
  - `Database ID`: **[TU_ID_DE_BASE_DE_DATOS_AQUÍ]**  
    *(¡Debes crearla primero en Notion! Ver notas abajo)*  
  - `Fields to Map`:  
    | Notion Property | Tipo en Notion | Valor desde N8N |  
    |-----------------|----------------|-----------------|  
    | `Nombre`        | Título         | `{{$json["senderName"]}}` |  
    | `Email`         | Texto          | `{{$json["senderEmail"]}}` |  
    | `Asunto`        | Texto          | `{{$json["subject"]}}` |  
    | `Fecha`         | Fecha          | `{{$json["receivedAt"]}}` |  
    | `Origen`        | Seleccionar    | `"Gmail"` (valor fijo) |  

> ⚠️ **Requisitos previos en Notion**:  
> 1. Crea una base de datos tipo *"Table"* (o "Base de datos") en Notion.  
> 2. Añade estas propiedades **exactamente** con estos nombres y tipos:  
>    - `Nombre` (Título)  
>    - `Email` (Texto)  
>    - `Asunto` (Texto)  
>    - `Fecha` (Fecha)  
>    - `Origen` (Seleccionar, con opción "Gmail")  
> 3. Copia el **ID de la base de datos** de la URL:  
>    `https://www.notion.so/tu-espacio/[AQUI_VA_TU_ID]?v=...`  
>    *(El ID es una cadena de 32 caracteres hexadecimales, ej: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)*  
> 4. En N8N, crea credenciales de Notion (Integration Token con permiso `read_write` en tu workspace).

#### **4. Slack: Enviar Notificación**  
*(Alerta en Slack solo cuando se guarda exitosamente en Notion)*  
- **Nombre del nodo**: `Notify Slack`  
- **Configuración**:  
  - `Resource`: `Message`  
  - `Operation`: `Post`  
  - `Channel`: `#tus-propuestas` (o el canal que uses)  
  - `Text`:  
    ```text
    :memo: Nueva propuesta/cotización recibida
    • De: {{$json["senderName"]}} (<{{$json["senderEmail"]}}>)
    • Asunto: {{$json["subject"]}}
    • Hora: {{$json["receivedAt"] | formatDate("DD/MM/YYYY HH:mm")}}
    :mag: Ver en Notion: [Enlace a la página] 
    ```  
    *(Nota: Para el enlace a Notion, necesitarías el ID de la página creada en el nodo anterior. Si no lo necesitas, elimina esa línea)*  
  - **Importante**: Activa `Only Execute On Success` en el nodo de Notion (ver paso 5).

#### **5. Manejo de Errores (Opcional pero Recomendado)**  
*(Para no perder datos si falla Notion/Slack)*  
- **Conecta el nodo de Notion** → `Error Trigger` → `Function` (para loggear) o `Email` (para alertarte a ti).  
- **¿Por qué?** Si Notion falla (ej: límite de rate, propiedad faltante), el workflow se detiene y no llega a Slack. Con esto, sabes qué falló.

---

### 🔑 **Pasos Críticos para que Funcione**
1. **Notion primero**:  
   - Crea la base de datos con las propiedades exactas (nombres y tipos como en la tabla arriba).  
   - Copia su ID y pégalo en el nodo de Notion.  
   - Genera un [Integration Token](https://www.notion.so/my-integrations) en Notion con permisos `read_write` para tu workspace.  
   - En N8N: `Credentials → New Credential → Notion → Pega el token`.

2. **Gmail Search Query**:  
   - `subject:(propuesta OR cotizacion)` busca **cualquiera** de las dos palabras (no requiere ambas).  
   - Si quieres coincidencia exacta de frases (ej: "cotización de servicios"), usa:  
     `subject:"cotizacion de servicios" OR subject:"propuesta de proyecto"`  
   - **Prueba primero** en Gmail web con esa búsqueda para confirmar que filtra como esperas.

3. **Evita duplicados**:  
   - Si el mismo email llega múltiples veces (ej: reenvíos), Notion creará páginas duplicadas.  
   - **Solución avanzada**: Agrega un nodo `HTTP Request` antes de Notion para verificar si el `senderEmail` + `subject` ya existe en tu base de datos (usando la API de Notion). Pero para empezar, lo simple es mejor.

4. **Zona horaria en Slack**:  
   - El `formatDate` en el mensaje de Slack ajusta la hora a tu zona local (ej: `DD/MM/YYYY HH:mm`). Ajusta el formato si necesitas otro.

5. **Prueba con un email de prueba**:  
   - Envía un email a tu Gmail con asunto: `"Prueba: propuesta de servicios"`  
   - Verifica que:  
     a) El workflow se active  
     b) Notion cree la página con datos limpios  
     c) Slack reciba la notificación  

---

### 💡 **¿Por qué este enfoque es eficiente?**
- **Filtro temprano**: El `Search Query` en Gmail evita procesar emails irrelevantes (ahorra ejecuciones y límites de N8N).  
- **Datos limpios**: El nodo `Function` asegura que Notion reciba formato consistente (sin `< >` ni espacios extra).  
- **Separación de responsabilidades**: Notion solo guarda; Slack solo notifica (más fácil de depurar).  
- **Escalable**: Si mañana quieres agregar más filtros (ej: solo de cierto dominio), solo modifica el `Search Query`.

---

### ⚠️ **Posibles Problemas y Soluciones**
| Problema                          | Solución                                                                 |
|-----------------------------------|--------------------------------------------------------------------------|
| **Notion da error 400**           | Revisa que los nombres de propiedades en Notion coincidan exactamente con los mapeados en N8N (case-sensitive). |
| **Slack no recibe mensaje**       | Verifica que el nodo de Notion tenga activado `Only Execute On Success` (en ajustes del nodo). |
| **Remitente sin nombre** (ej: `<no-reply@empresa.com>`) | La función ya maneja esto: usa el email como nombre si no encuentra `<Nombre >`. |
| **Workflow se dispara demasiado** | Ajusta el `Search Query` en Gmail para ser más específico (ej: añadir `from:cliente@empresa.com`). |

---

¿Necesitas que te ayude a:  
1. Generar el JSON para importar este workflow directamente a N8N?  
2. Explicar cómo crear la Integration Token de Notion paso a paso?  
3. Ajustar el filtro para incluir/excluir remitentes específicos?  

¡Avísame y te doy los detalles exactos! 😊