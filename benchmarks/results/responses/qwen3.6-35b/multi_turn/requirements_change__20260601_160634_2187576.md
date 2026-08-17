# Qwen 3.6 35B base (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.66 | quality: 7.16
- latency_total: 9.715s | tokens_per_second: 201.6
- input_tokens: 233 | output_tokens: 1959
- judge_score: 4.0 | justificación: La respuesta es precisa y clara, proporcionando una guía detallada para implementar el flujo de trabajo modificado, aunque no responde directamente a la instrucción original, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

Excelente cambio. Integrar **Gmail → Notion → Slack** es un flujo muy potente para gestión de leads o seguimiento comercial. Aquí tienes la estructura exacta y la configuración paso a paso para n8n:

### 🔹 Estructura del Workflow
```
[Gmail Trigger] → [Filter] → [Notion (Crear página)] → [Slack (Enviar mensaje)]
```
*(Nota: Slack solo se ejecutará si el email pasa el filtro, ya que n8n maneja el flujo secuencialmente)*

---

### 📥 1. Nodo: `Gmail Trigger`
- **Trigger**: `On New Email`
- **Authentication**: Conecta tu cuenta de Gmail (OAuth2)
- **Options**: 
  - ✅ `Include Raw Data` (opcional, si necesitas el cuerpo completo)
  - `Return All`: `False` (solo el último email nuevo)
- **Output útil**: `subject`, `from`, `from.name`, `date`, `messageId`

---

### 🔍 2. Nodo: `Filter`
Configura **una sola condición** usando una expresión JS (n8n lo evalúa como booleano):
```js
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') }}
```
✅ Esto garantiza que funcione con mayúsculas, minúsculas o acentos/diacríticos.

---

### 📊 3. Nodo: `Notion → Create Database Item`
**Requisitos previos:**
1. Crea una base de datos en Notion con estas propiedades (ejemplo):
   - `Remitente` (Text)
   - `Email` (Text)
   - `Asunto` (Text)
   - `Fecha Recepción` (Date)
   - `Estado` (Status, opcional)
2. Obtén el `Database ID` (de la URL: `notion.so/tu-empresa/XXXXXXXXXXXXXXXXXXXXXXXXXX`)
3. Crea una Integration en Notion con permisos `Read & Write` y copia el `Secret` (Bearer token).

**Configuración en n8n:**
- **Database ID**: Pega el ID de tu base de datos
- **Properties** (mapeo dinámico):
  | Propiedad Notion | Valor |
  |------------------|-------|
  | `Remitente`      | `{{ $json.from.name || $json.from }}` |
  | `Email`          | `{{ $json.from }}` |
  | `Asunto`         | `{{ $json.subject }}` |
  | `Fecha Recepción`| `{{ $json.date }}` |

⚠️ Asegúrate de que los tipos de propiedad en Notion coincidan con los valores que envías (texto → texto, fecha → ISO string, etc.).

---

### 💬 4. Nodo: `Slack → Send Message`
- **Authentication**: Conecta tu Slack Workspace (OAuth)
- **Channel**: Selecciona el canal destino (ej: `#leads`, `#ventas`)
- **Text** (usa formato Slack o Markdown):
```
📩 Nuevo email filtrado
👤 Remitente: {{ $json.from.name || $json.from }}
📧 Email: {{ $json.from }}
📌 Asunto: {{ $json.subject }}
🕒 Fecha: {{ $json.date }}
🔗 Ver en Notion: {{ $json.id }}
```
*(Nota: `$json.id` será el `page_id` que devuelve el nodo Notion)*

---

### 🔧 Consejos Pro
1. **Manejo de errores**: Añade un nodo `Error Trigger` o usa `Continue On Fail` en los nodos externos si quieres que un fallo en Notion/Slack no detenga el workflow.
2. **Duplicados**: Si un email se reenvía o se marca como leído, el trigger puede duplicarse. Puedes añadir un nodo `Function` antes de Notion para guardar `messageId` en un `Set` o usar `Notion → Get Page` para verificar si ya existe.
3. **Prueba local**: Usa `Execute Node` en el filtro y `Debug` en Slack para validar el flujo sin ejecutarlo en producción.
4. **Variables de entorno**: Guarda el `NOTION_DB_ID` y `SLACK_CHANNEL` en `Settings > Credentials/Variables` para mantener el workflow limpio.

¿Quieres que te genere el **JSON exportable** del workflow para importarlo directamente en tu n8n, o necesitas ayuda con la configuración de las credenciales/APIs?