# Gemini 3.8 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 4.48 | quality: 4.0
- latency_total: 13.603s | tokens_per_second: 110.3
- input_tokens: 202 | output_tokens: 1500

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

¡Excelente ajuste! Centralizar leads o cotizaciones en Notion y recibir alertas inmediatas en Slack es una combinación ideal para ventas.

Aquí tienes la arquitectura completa del workflow y la configuración paso a paso:

---

### Diagrama del flujo
`Gmail Trigger` ➔ `If (Filtro)` ➔ `Notion (Crear elemento)` ➔ `Slack (Notificación)`

---

### Paso a paso de la configuración

#### 1. Nodo: Gmail Trigger
* **Event**: *Message Received*.
* **Opciones de optimización (Recomendado):**
  * En el campo **Filters** > **Search Query (q)** puedes poner:  
    `subject:(propuesta OR cotizacion OR cotización)`  
  * *Tip técnico:* Al filtrar directamente desde la consulta de Gmail, evitas consumir ejecuciones innecesarias en n8n con correos irrelevantes.

---

#### 2. Nodo: If (Validación de seguridad)
Si prefieres no usar el filtro de la API de Gmail o quieres doble validación:
* **Condición 1**:
  * **Value 1**: `{{ $json.subject.toLowerCase() }}`
  * **Operation**: *Contains*
  * **Value 2**: `propuesta`
* **Combinador lógico**: Cambiar a **OR** (cualquiera de las condiciones debe cumplirse).
* **Condición 2**:
  * **Value 1**: `{{ $json.subject.toLowerCase() }}`
  * **Operation**: *Contains*
  * **Value 2**: `cotiz` *(cubre tanto "cotizacion" como "cotización")*.

*Los siguientes nodos van conectados a la salida **True**.*

---

#### 3. Nodo: Notion
* **Resource**: *Database Page*
* **Operation**: *Create*
* **Database**: Selecciona tu base de datos (asegúrate de haberla compartido previamente con la integración de Notion).
* **Mapeo de propiedades:**
  * **Nombre / Título**: `{{ $json.subject }}`
  * **Email**: `{{ $json.from.value[0].address }}`
  * **Remitente**: `{{ $json.from.value[0].name || $json.from.value[0].address }}`
  * **Fecha**: `{{ $json.date }}`
  * **Cuerpo/Resumen (Opcional)**: `{{ $json.snippet }}`

---

#### 4. Nodo: Slack
Conéctalo a continuación del nodo de Notion para que se ejecute en cadena:
* **Resource**: *Message*
* **Operation**: *Post*
* **Channel**: Selecciona tu canal (ej: `#ventas-leads` o un canal privado).
* **Text**: Puedes formatearlo en Markdown de Slack:
  ```text
  🚨 *Nueva Solicitud Recibida* 🚨
  • *De:* {{ $('Gmail Trigger').item.json.from.value[0].name }} ({{ $('Gmail Trigger').item.json.from.value[0].address }})
  • *Asunto:* {{ $('Gmail Trigger').item.json.subject }}
  • *Resumen:* {{ $('Gmail Trigger').item.json.snippet }}
  • *Notion:* <{{ $json.url }}|Ver en Notion>
  ```
  *(Nota cómo `$json.url` toma directamente el enlace de la página recién creada en el nodo de Notion).*

---

¿Tienes ya creadas las integraciones/credenciales de Notion y Slack en n8n, o necesitas ayuda para configurarlas?