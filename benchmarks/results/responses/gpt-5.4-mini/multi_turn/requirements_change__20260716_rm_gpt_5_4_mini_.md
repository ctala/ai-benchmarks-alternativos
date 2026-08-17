# GPT-5.4 Mini — multi_turn/requirements_change

- model_id: `gpt-5.4-mini`
- success: True  | final: 4.82 | quality: 4.0
- latency_total: 6.713s | tokens_per_second: 138.7
- input_tokens: 226 | output_tokens: 931
- judge_score: 3.0 | justificación: La respuesta es precisa en términos de la estructura del flujo de trabajo, pero no cumple con la instrucción original de guardar los datos en un Google Sheet, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

Claro. Te dejo una estructura de workflow en n8n para:

- leer emails de Gmail
- filtrar solo los que tengan **“propuesta”** o **“cotizacion”** en el asunto
- extraer datos del remitente
- guardarlos en **Notion**
- enviar una notificación a **Slack**

## Flujo del workflow

1. **Gmail Trigger**  
   Detecta nuevos emails.

2. **IF / Filter**  
   Verifica si el asunto contiene:
   - `propuesta`
   - `cotizacion`

3. **Set o Function**  
   Extrae y normaliza:
   - nombre del remitente
   - email del remitente
   - asunto
   - fecha
   - snippet / cuerpo breve

4. **Notion**  
   Crea una página o registro en una base de datos.

5. **Slack**  
   Envía una notificación al canal que elijas.

---

## Configuración sugerida

### 1) Gmail Trigger
- **Node**: `Gmail Trigger`
- **Event**: `New Email`
- Opcional: limitar a inbox si quieres.

---

### 2) IF node para filtrar asunto
Usa una condición tipo **String** sobre el campo del asunto.

**Condición 1**
- Value 1: `{{$json.subject}}`
- Operation: `contains`
- Value 2: `propuesta`

**Condición 2**
- Value 1: `{{$json.subject}}`
- Operation: `contains`
- Value 2: `cotizacion`

Luego configuras el IF para que pase si **cualquiera de las dos** se cumple.

Si prefieres algo más robusto, puedes usar un `Function` con regex:

```javascript
const subject = ($json.subject || '').toLowerCase();

if (subject.includes('propuesta') || subject.includes('cotizacion')) {
  return items;
}

return [];
```

---

### 3) Extraer datos del remitente
En un nodo `Set` o `Function`, puedes dejar algo así:

```javascript
const from = $json.from || '';
const subject = $json.subject || '';
const date = $json.date || '';
const snippet = $json.snippet || '';

let name = '';
let email = '';

const match = from.match(/(.*)<(.+)>/);
if (match) {
  name = match[1].trim().replace(/"/g, '');
  email = match[2].trim();
} else {
  email = from.trim();
}

return [
  {
    json: {
      name,
      email,
      subject,
      date,
      snippet,
    }
  }
];
```

---

### 4) Guardar en Notion
- **Node**: `Notion`
- **Operation**: `Create Page`
- **Database**: selecciona tu base de datos

Mapea campos como:

- **Nombre** → `{{$json.name}}`
- **Email** → `{{$json.email}}`
- **Asunto** → `{{$json.subject}}`
- **Fecha** → `{{$json.date}}`
- **Resumen** → `{{$json.snippet}}`

Asegúrate de que tu base de datos en Notion tenga propiedades compatibles:
- `Title` o `Name` como título
- `Email` tipo email o texto
- `Subject` texto
- `Date` fecha
- `Snippet` texto

---

### 5) Notificación en Slack
- **Node**: `Slack`
- **Operation**: `Post Message`

Ejemplo de mensaje:

```text
Nuevo email de propuesta/cotización recibido:

Remitente: {{$json.name}} <{{$json.email}}>
Asunto: {{$json.subject}}
Fecha: {{$json.date}}
```

Puedes enviarlo a un canal como `#ventas` o `#leads`.

---

## Recomendación de estructura final

**Gmail Trigger**  
→ **IF** (asunto contiene propuesta o cotizacion)  
→ **Function/Set** (extraer remitente)  
→ **Notion** (crear registro)  
→ **Slack** (notificar)

---

## Si quieres, te puedo dejar ahora mismo:
1. el **workflow completo en JSON para importar en n8n**, o  
2. la **configuración nodo por nodo** con capturas lógicas de campos.

Si quieres, te lo preparo en formato listo para importar.