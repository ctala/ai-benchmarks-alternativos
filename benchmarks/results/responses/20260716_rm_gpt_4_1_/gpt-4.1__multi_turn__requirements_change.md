# GPT-4.1 — multi_turn/requirements_change

- model_id: `gpt-4.1`
- success: True  | final: 5.97 | quality: 6.0
- latency_total: 5.326s | tokens_per_second: 113.8
- input_tokens: 225 | output_tokens: 606
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un workflow detallado que cumple con los requisitos actualizados, con una estructura bien organizada y útil para un emprendedor.

## Respuesta completa

¡Perfecto! Te detallo cómo armar ese workflow en N8N, adaptado a tus nuevas necesidades:

---

### **Estructura del Workflow**

1. **Gmail Trigger:** Detecta nuevos emails.
2. **IF Node:** Filtra emails que tengan “propuesta” o “cotización” en el asunto.
3. **Function Node:** Extrae y prepara los datos requeridos.
4. **Notion Node:** Agrega los datos a una base de datos de Notion.
5. **Slack Node:** Envía una notificación a Slack.

---

### **Paso a Paso**

#### 1. **Gmail Trigger**
- **Tipo de Trigger:** New Email
- **Config:** Elige la cuenta y carpeta a monitorear (usualmente “INBOX”).

#### 2. **IF Node** (Filtra por asunto)
- Añade un nodo IF después del trigger.
- **Condición:**
  - Campo: `Subject`
  - Operador: “contains”
  - Valor: `propuesta`
- Añade una segunda condición con “cotización” usando OR.
- **Ejemplo de configuración:**
  - `Subject contains propuesta OR Subject contains cotización`

#### 3. **Function Node** (Prepara los datos)
- Toma el email filtrado y extrae los campos:
    - Remitente (nombre y correo)
    - Asunto
    - Fecha
- **Código de ejemplo:**
```javascript
return [{
  from: item.json.from, // o item.json.sender
  fromEmail: item.json.from.email || item.json.sender,
  subject: item.json.subject,
  date: item.json.date,
}];
```
Ajusta los campos según la salida del nodo anterior.

#### 4. **Notion Node** (Crear página en Notion)
- **Operación:** Create Page
- **Base de datos:** Selecciona tu base de datos de Notion.
- **Mapea los campos:** Relaciona “from”, “fromEmail”, “subject”, “date” a las propiedades de la base.

#### 5. **Slack Node** (Enviar notificación)
- **Operación:** Send Message
- **Canal:** Elige el canal o usuario.
- **Mensaje:** Personaliza con los datos extraídos:
    ```
    📧 Nuevo correo de {{ $json["from"] }} ({{ $json["fromEmail"] }}):
    Asunto: {{ $json["subject"] }}
    Fecha: {{ $json["date"] }}
    ```

---

### **Diagrama del workflow**

```
Gmail Trigger
      ↓
     IF (asunto contiene 'propuesta' o 'cotización')
      ↓
Function (extrae datos)
   ↓           ↓
Notion      Slack
```

---

¿Necesitas el JSON para importarlo a N8N o alguna explicación extra sobre la configuración de algún nodo?