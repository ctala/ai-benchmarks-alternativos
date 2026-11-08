# Seed 2.1 Turbo — multi_turn/requirements_change

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 4.14 | quality: 4.0
- latency_total: 85.003s | tokens_per_second: 71.3
- input_tokens: 279 | output_tokens: 6061

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

### 📋 Resumen del Workflow Final
Flujo completo: `Gmail (nuevos correos) → Filtro de asunto → Limpieza de datos → Guardar en Notion → Notificación en Slack`

---

### ✅ Prerrequisitos antes de empezar
1. Tener tus cuentas de **Gmail, Notion y Slack conectadas en n8n** (ve a *Credenciales → Agregar credencial* y busca cada servicio, sigue los pasos de autorización).
2. Crear una **base de datos en Notion** para guardar las propuestas/cotizaciones (te doy una plantilla de propiedades abajo).
3. *Paso que se olvida 90% de las veces*: Comparte la base de datos de Notion con la integración de n8n (abre la base de datos → Botón *Compartir* → Invita a la app de n8n que agregaste en las credenciales).

---

### 🛠️ Configuración paso a paso de cada nodo

---

#### Nodo 1: Gmail Trigger (activador del flujo)
Se ejecuta cada vez que llega un correo nuevo:
1. Selecciona tu credencial de Gmail.
2. En **Evento**, elige `Nuevo correo electrónico recibido`.
3. En **Carpeta**, selecciona `INBOX` (o la carpeta que quieras escanear, ej: una carpeta filtrada de clientes).
4. Opcional: Activa `Marcar como leído` para no procesar correos repetidos.
5. Si usas n8n self-hosted: configura el **Tiempo de sondeo** (ej: cada 5 minutos). Si usas n8n Cloud, funciona en tiempo real por webhook.

---

#### Nodo 2: IF Node (filtro de asunto)
Solo deja pasar los correos que tengan "propuesta" o "cotización" en el asunto (ignora mayúsculas/minúsculas y tildes):
1. Agrega un nodo `IF` después del Gmail Trigger.
2. En **Condición 1**, cambia el modo de valor fijo a **Expresión** (botón `{ }` al lado del campo de valor).
3. Pega esta expresión en el campo de valor:
   ```javascript
   {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') || $json.subject.toLowerCase().includes('cotización') }}
   ```
   *Nota: Agregué "cotización" con tilde para capturar ambas variantes, puedes borrarla si no la necesitas.*
4. En el operador, selecciona `Es verdadero` (booleano).
5. Usa la rama **Verdadero** (correos que cumplen el filtro) para los siguientes nodos. La rama Falso se detendrá sola si no agregas nada.

---

#### Nodo 3: Set Node (limpiar y organizar datos)
Extrae solo los datos que necesitas para Notion y Slack, sin código (ideal para principiantes):
1. Agrega un nodo `Set` en la rama Verdadero del IF.
2. Activa la opción `Solo incluir los campos definidos abajo` para no llevar datos innecesarios.
3. Agrega estos campos con sus expresiones (copia y pega cada una en modo Expresión):
   | Nombre del campo | Expresión | Descripción |
   |------------------|-----------|-------------|
   | `nombre_remitente` | `{{ $json.from.name }}` | Nombre de quien envía el correo |
   | `email_remitente` | `{{ $json.from.address }}` | Email del remitente |
   | `asunto` | `{{ $json.subject }}` | Asunto completo del correo |
   | `fecha_recepcion` | `{{ new Date($json.date).toISOString() }}` | Fecha formateada para que Notion la lea como fecha |
   | `link_gmail` | `{{ "https://mail.google.com/mail/u/0/#inbox/" + $json.id }}` | Link directo al correo en Gmail |
   | `cuerpo_resumido` | `{{ $json.textSnippet }}` | Resumen corto del cuerpo del correo (primeras líneas) |

---

#### Nodo 4: Notion - Create Page (guardar datos)
Guarda cada correo que pasa el filtro como una página nueva en tu base de datos de Notion:
1. Primero, crea la base de datos en Notion con estas propiedades (coinciden con los campos del Set):
   - `Nombre Remitente` (tipo: Texto)
   - `Email` (tipo: Email)
   - `Asunto` (tipo: Texto)
   - `Fecha Recepción` (tipo: Fecha)
   - `Link Gmail` (tipo: URL)
   - `Estado` (tipo: Select, con opciones como `Nuevo`, `En revisión`, `Enviada`, `Cerrada` → para hacer seguimiento comercial)
2. En el nodo de Notion, selecciona tu credencial.
3. En **Operación**, elige `Crear página`.
4. En **Base de datos**, selecciona la base que creaste (si no aparece, revisa que la hayas compartido con la integración de n8n).
5. En **Propiedades**, mapea cada campo del Set con la propiedad correspondiente de Notion:
   - Nombre Remitente → `{{ $json.nombre_remitente }}`
   - Email → `{{ $json.email_remitente }}`
   - Asunto → `{{ $json.asunto }}`
   - Fecha Recepción → `{{ $json.fecha_recepcion }}`
   - Link Gmail → `{{ $json.link_gmail }}`
   - Estado → Valor fijo `Nuevo` (para que todas las entradas empiecen con ese estado)
6. Opcional: En **Contenido de la página**, agrega el cuerpo completo del correo: usa `{{ $json.text }}` para texto plano o `{{ $json.body }}` para formato HTML.

---

#### Nodo 5: Slack - Send Message (notificación)
Te avisa en Slack cada vez que se guarda una nueva propuesta/cotización en Notion (solo se ejecuta si el guardado en Notion fue exitoso):
1. Agrega el nodo de Slack **después del nodo de Notion**.
2. Selecciona tu credencial de Slack.
3. En **Canal**, elige el canal de trabajo donde quieres recibir la notificación, o selecciona tu propio usuario para que te llegue como mensaje directo.
4. En **Texto del mensaje**, pega este texto personalizado:
   ```
   🔔 Nueva solicitud de propuesta/cotización recibida
   👤 Remitente: {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
   📩 Asunto: {{ $json.asunto }}
   📝 Resumen: {{ $json.cuerpo_resumido }}
   🔗 Ver en Notion: {{ $json.url }}
   📧 Ver en Gmail: {{ $json.link_gmail }}
   ```
   *Nota: `{{ $json.url }}` es el link directo a la página de Notion que acabamos de crear, lo trae automáticamente el nodo de Notion.*
5. Opcional: Activa `Enviar como bot` y personaliza el nombre del bot (ej: "Alertas de Propuestas") para que se vea más ordenado.

---

### 💡 Mejoras opcionales para emprendedores
1. **Evitar duplicados**: Agrega un nodo `Notion - Database Query` antes de crear la página, para buscar si ya existe una entrada con el mismo ID de Gmail, y solo crearla si no existe.
2. **Resumen automático con IA**: Si recibes correos muy largos, agrega un nodo de OpenAI antes del Set para resumir el cuerpo en 3 puntos clave y guardarlo en Notion.
3. **Botones en Slack**: Agrega botones en la notificación para cambiar el estado de la página de Notion directamente (ej: "Marcar como en revisión") sin entrar a Notion.
4. **Filtrar por dominio**: Agrega una condición extra en el IF para excluir correos internos de tu equipo, o para solo aceptar correos de clientes potenciales.

---

### 🚨 Errores comunes y soluciones
- **No aparece la base de datos de Notion**: Asegúrate de haber compartido la base de datos con la integración de n8n (paso de prerrequisitos).
- **El filtro no captura correos que sí tienen la palabra**: Revisa que la expresión use `toLowerCase()` para ignorar mayúsculas, y agrega variantes de la palabra si es necesario (ej: "presupuesto").
- **La fecha en Notion no se ve bien**: Asegúrate de que la expresión de fecha use `.toISOString()`, el formato que Notion reconoce como fecha válida.

¿Necesitas que te explique alguna parte en más detalle, o quieres agregar alguna funcionalidad extra?