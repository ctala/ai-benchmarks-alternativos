# Claude Opus 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.92 | quality: 10.0
- latency_total: 129.135s | tokens_per_second: 107.2
- input_tokens: 390 | output_tokens: 13837
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3: Automatización con IA. De la idea al flujo de trabajo

> **Curso:** IA Práctica para Emprendedores
> **Duración estimada:** 3 a 4 horas (1,5 h de teoría y ejemplos, 2 h de ejercicio práctico)
> **Nivel:** Emprendedor no técnico (no necesitas saber programar)
> **Requisitos previos:** Módulos 1 y 2 (fundamentos de IA y prompts efectivos), una cuenta de Gmail y ganas de experimentar

---

## 📌 1. Objetivo del módulo

Al terminar este módulo podrás identificar qué tareas repetitivas de tu emprendimiento conviene automatizar y diseñar flujos de trabajo que combinen tus herramientas actuales (formularios, correo, hojas de cálculo, WhatsApp) con la inteligencia artificial, sin escribir código. Conocerás la lógica detrás de cualquier automatización (disparador → procesamiento → acción), analizarás tres casos reales aplicables a startups latinoamericanas y construirás tu primer flujo funcional en **n8n**: un formulario de contacto inteligente que clasifica cada consulta, redacta una respuesta personalizada y la registra en tu base de datos. El objetivo final es que recuperes horas de tu semana para dedicarlas a lo que solo tú puedes hacer: hacer crecer tu negocio.

---

## 📚 2. Contenido teórico

### 2.1 ¿Qué es la automatización y en qué cambia con la IA?

**Automatizar** es lograr que una tarea se ejecute sola cada vez que ocurre algo, sin que tengas que intervenir.

Hasta hace poco, las automatizaciones solo seguían **reglas rígidas**:

> *"Si llega un correo con la palabra 'factura', muévelo a la carpeta Contabilidad."*

El problema es que los clientes no escriben siguiendo reglas. Uno escribe "factura", otro "comprobante", otro "¿me mandas lo de mi pago?". La regla falla.

Con la IA, la automatización puede **entender, decidir y crear**:

> *"Lee este correo, identifica si es una solicitud de factura (aunque no use esa palabra), extrae el número de pedido y redacta una respuesta amable."*

| Automatización tradicional | Automatización con IA |
|---|---|
| Sigue reglas exactas | Interpreta el contexto |
| Funciona con datos ordenados | Funciona con texto libre, audios o imágenes |
| Mueve información | Entiende, resume, clasifica y redacta |
| "Si dice X, haz Y" | "Analiza esto y decide qué hacer" |

### 2.2 La anatomía de cualquier automatización

Todo flujo de trabajo, desde el más simple hasta el más complejo, tiene tres partes:

```
┌──────────────┐      ┌──────────────────┐      ┌──────────────┐
│  DISPARADOR  │ ───► │  PROCESAMIENTO   │ ───► │    ACCIÓN    │
│  (Trigger)   │      │  (IA + lógica)   │      │   (Output)   │
└──────────────┘      └──────────────────┘      └──────────────┘
  ¿Qué lo inicia?       ¿Qué se hace con         ¿Qué resultado
                         la información?          se produce?
```

**Ejemplo cotidiano:**
- **Disparador:** un cliente llena el formulario de tu web.
- **Procesamiento:** la IA lee el mensaje y determina si es una venta, una queja o soporte.
- **Acción:** se envía una respuesta, se guarda en Google Sheets y se te avisa por Telegram si es urgente.

💡 **Regla de oro:** si puedes describir una tarea con la frase *"Cada vez que pasa ___, yo hago ___"*, probablemente se puede automatizar.

### 2.3 ¿Qué tareas conviene automatizar?

Usa esta matriz para decidir:

| | **Poco frecuente** | **Muy frecuente** |
|---|---|---|
| **Requiere mucho criterio humano** | ❌ Hazla tú | ⚠️ Automatiza parcialmente (la IA prepara, tú apruebas) |
| **Requiere poco criterio** | 🤷 No vale la pena | ✅ **¡Automatiza ya!** |

**Fórmula rápida de retorno:**
> Minutos que toma la tarea × veces por semana × 4 = minutos al mes que recuperas

*Ejemplo:* responder consultas de precio toma 5 min × 40 veces por semana × 4 = **800 minutos al mes (más de 13 horas)**.

### 2.4 Las herramientas: n8n, Make y Zapier

Existen plataformas "no-code" (sin código) que conectan tus aplicaciones como si fueran piezas de LEGO.

| Herramienta | Ventajas | Consideraciones | Ideal para |
|---|---|---|---|
| **n8n** | Muy flexible, nodos de IA avanzados, versión gratuita autoalojada, cobra por ejecución completa y no por cada paso | Curva de aprendizaje algo mayor | Emprendedores que quieren escalar sin que los costos se disparen |
| **Make** | Visual e intuitiva, buen plan gratuito | Cobra por operación (cada paso cuenta) | Flujos medianos |
| **Zapier** | La más fácil, miles de integraciones | Puede volverse costosa al crecer | Flujos simples y rápidos |

> 💰 Los precios y planes cambian con frecuencia. Revisa siempre la página oficial de cada herramienta antes de decidir.

### 2.5 Conociendo n8n

**n8n** (se pronuncia "n-eight-n" o "nodemation") es una plataforma de automatización de código abierto. Tienes dos formas de usarla:

1. **n8n Cloud:** creas una cuenta en n8n.io y lo usas desde el navegador. Tiene una prueba gratuita. **Es la opción recomendada para este curso.**
2. **Autoalojado (self-hosted):** lo instalas en tu propio servidor. La edición comunitaria es gratuita, pero requiere conocimientos técnicos.

#### Conceptos clave de n8n

| Concepto | Qué es | Analogía |
|---|---|---|
| **Workflow** | El flujo completo de automatización | La receta completa |
| **Nodo** | Cada paso o bloque del flujo | Cada paso de la receta |
| **Trigger** | El nodo que inicia todo | "Cuando el agua hierva…" |
| **Credenciales** | Los permisos para conectar tus apps | Las llaves de tu casa |
| **Ejecución** | Cada vez que el flujo corre | Cada vez que cocinas la receta |
| **Expresión** | Un dato dinámico que viene de un paso anterior, por ejemplo `{{ $json.nombre }}` | "Usa el ingrediente que preparaste antes" |

#### Los nodos de IA en n8n

n8n tiene nodos para conectarse con modelos como **OpenAI (ChatGPT), Google Gemini, Anthropic (Claude)** y otros. Los más útiles para empezar:

- **Nodo de OpenAI / Gemini:** envía un prompt y recibe una respuesta. Es el más simple.
- **Basic LLM Chain:** permite usar cualquier modelo con un prompt estructurado.
- **AI Agent:** un "asistente" que puede usar herramientas, como consultar tu inventario o buscar en tu base de datos, y tomar decisiones.
- **Text Classifier:** clasifica texto en categorías que tú defines y envía cada caso por un camino distinto.

### 2.6 Principios para automatizar con IA de forma responsable

1. **Humano en el circuito:** en temas sensibles (reembolsos, quejas graves, salud, dinero), la IA prepara y una persona aprueba.
2. **La IA puede equivocarse:** dale instrucciones claras y la información correcta. No le pidas inventar precios ni políticas.
3. **Protege los datos:** no envíes información sensible de clientes (números de tarjeta, documentos de identidad) a la IA sin necesidad. Revisa la ley de protección de datos de tu país, como la Ley 1581 en Colombia, la LFPDPPP en México o la LGPD en Brasil.
4. **Empieza pequeño:** automatiza un proceso, mídelo, mejóralo y después pasa al siguiente.
5. **Sé transparente:** si un cliente habla con un bot, es buena práctica que lo sepa.

---

## 🛠️ 3. Ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada 💬

**🏪 Caso:** *"Café de Altura"*, una tienda online de café de especialidad en Colombia, recibe más de 60 mensajes diarios por WhatsApp. El 70 % son las mismas preguntas: horarios, costos de envío, métodos de pago y estado del pedido.

**❌ Antes:** la fundadora respondía mensajes hasta las 11 p.m. y muchos clientes esperaban horas.

**✅ Después:** un asistente con IA responde al instante las preguntas frecuentes y deriva a una persona los casos complejos.

#### Flujo de trabajo

```
📱 Mensaje de WhatsApp entrante
        │
        ▼
🤖 AI Agent (con la base de conocimiento: precios, envíos, políticas)
        │
        ▼
❓ ¿La IA puede resolverlo con seguridad?
   │                          │
  SÍ                          NO (queja, reembolso, caso raro)
   │                          │
   ▼                          ▼
💬 Responde al cliente     🔔 Notifica al equipo por Telegram/Slack
   │                          + responde "Te contactará una persona"
   ▼
📊 Registra la conversación en Google Sheets
```

#### Nodos en n8n
- **WhatsApp Trigger** (requiere la API de WhatsApp Business de Meta)
- **AI Agent** + modelo de chat (OpenAI o Gemini) + **memoria** para recordar la conversación
- **IF** para decidir si se escala a un humano
- **WhatsApp** para enviar la respuesta
- **Telegram** o **Slack** para la alerta al equipo
- **Google Sheets** para el registro

#### Prompt del sistema sugerido
```
Eres el asistente virtual de Café de Altura, tienda de café de especialidad en Colombia.
Tono: cálido, cercano, usa "tú". Respuestas breves (máximo 3 líneas).

INFORMACIÓN DEL NEGOCIO:
- Envíos: Bogotá 1-2 días, resto del país 3-5 días.
- Envío gratis en compras superiores a $120.000 COP.
- Pagos: PSE, tarjeta, Nequi, contraentrega en Bogotá.
- Horario de atención humana: lunes a sábado, 8 a.m. a 6 p.m.

REGLAS:
- Si no sabes algo, NO lo inventes. Di que un asesor responderá pronto.
- Si el cliente está molesto, pide un reembolso o reporta un problema con su pedido,
  marca la conversación como ESCALAR.
```

**📈 Resultado esperado:** responder al instante a la mayoría de las consultas frecuentes y recuperar varias horas diarias de trabajo.

> 💡 **Tip para empezar:** configurar la API oficial de WhatsApp toma tiempo. Puedes practicar primero con **Telegram**, que es gratis y se conecta a n8n en minutos.

---

### Ejemplo 2: Generación de contenido para redes sociales 📱

**🏪 Caso:** *"Sonrisa Clara"*, una clínica dental en Guadalajara (México), sabe que debe publicar en Instagram y LinkedIn, pero nadie del equipo tiene tiempo para redactar.

**❌ Antes:** publicaban de forma irregular, una o dos veces al mes.

**✅ Después:** cada lunes reciben borradores de publicaciones para toda la semana, listos para revisar y programar.

#### Flujo de trabajo

```
⏰ Disparador programado (todos los lunes, 8:00 a.m.)
        │
        ▼
📋 Lee de Google Sheets la lista de temas pendientes
   (ej.: "blanqueamiento", "miedo al dentista", "cuidado infantil")
        │
        ▼
🤖 IA genera para cada tema:
   • Post de Instagram (gancho + texto + hashtags)
   • Post de LinkedIn (tono profesional)
   • Idea de imagen o guion de reel
        │
        ▼
📊 Guarda los borradores en Google Sheets con estado "Por revisar"
        │
        ▼
📧 Envía un email al equipo: "Tus 5 posts de la semana están listos"
        │
        ▼
👤 Humano revisa, ajusta y aprueba → (opcional) se programa la publicación
```

#### Nodos en n8n
- **Schedule Trigger** para ejecutar el flujo cada semana
- **Google Sheets** para leer los temas y guardar los borradores
- **OpenAI** o **Gemini** para generar el contenido
- **Gmail** para la notificación

#### Prompt sugerido
```
Eres el community manager de Sonrisa Clara, clínica dental familiar en Guadalajara.
Público: familias y profesionales de 25-50 años.
Tono: cercano, educativo, que quite el miedo al dentista. Nada de tecnicismos.

Tema de hoy: {{ tema }}

Genera:
1. INSTAGRAM: un gancho en la primera línea, máximo 120 palabras, 1 llamado a la acción,
   5 hashtags relevantes (incluye #Guadalajara).
2. LINKEDIN: versión profesional de 150 palabras.
3. IDEA VISUAL: describe en 2 líneas la imagen o el reel ideal.

No hagas promesas médicas ni garantices resultados.
```

**📈 Resultado esperado:** publicar de forma constante dedicando unos 30 minutos semanales a revisar, en lugar de horas a redactar desde cero.

> ⚠️ **Importante:** mantén siempre la revisión humana. En sectores regulados (salud, finanzas, alimentos), el contenido debe cumplir las normas publicitarias de tu país.

---

### Ejemplo 3: Calificación automática de leads 🎯

**🏪 Caso:** *"Nube Contable"*, un software de facturación para pymes en Perú, recibe más de 200 registros al mes desde su web. El equipo comercial (dos personas) pierde tiempo llamando a curiosos mientras los clientes potentes esperan.

**❌ Antes:** se llamaba a los leads por orden de llegada.

**✅ Después:** la IA evalúa cada lead en segundos y el equipo atiende primero a los más prometedores.

#### Flujo de trabajo

```
📝 Nuevo registro en el formulario (Typeform, Google Forms, web)
        │
        ▼
🤖 IA analiza y asigna una puntuación del 1 al 10 según:
   • Tamaño de empresa  • Urgencia  • Presupuesto  • Encaje con el producto
        │
        ▼
🔀 Clasificación
   │              │                │
 🔥 CALIENTE    🌤️ TIBIO         ❄️ FRÍO
  (8-10)        (5-7)            (1-4)
   │              │                │
   ▼              ▼                ▼
Alerta inmediata  Secuencia de     Newsletter
a ventas +        emails           educativa
agenda llamada    automáticos
        │
        ▼
📊 Todo se registra en el CRM (HubSpot, Pipedrive) o en Google Sheets
```

#### Nodos en n8n
- **Form Trigger**, **Typeform Trigger** o **Webhook**
- **OpenAI** o **Gemini** con salida en formato JSON
- **Switch** para dirigir cada lead según su puntuación
- **Slack**, **Telegram** o **Gmail** para las alertas
- **HubSpot**, **Pipedrive** o **Google Sheets** para el registro

#### Prompt sugerido
```
Eres un analista comercial de Nube Contable, software de facturación electrónica para pymes peruanas.

NUESTRO CLIENTE IDEAL: empresa formal con RUC, 5-100 empleados, emite más de 50 comprobantes
al mes, necesita cumplir con SUNAT.

Datos del lead:
- Empresa: {{ empresa }}
- Empleados: {{ empleados }}
- Mensaje: {{ mensaje }}

Responde SOLO con este JSON:
{
  "puntuacion": número del 1 al 10,
  "categoria": "caliente" | "tibio" | "frio",
  "razon": "explicación en una frase",
  "siguiente_paso": "acción recomendada para el vendedor"
}
```

**📈 Resultado esperado:** que el equipo comercial contacte primero a los leads de mayor potencial y responda a los "calientes" en minutos, no en días.

---

## ✍️ 4. Ejercicio práctico paso a paso

### 🎯 Construye tu "Formulario de contacto inteligente"

**Qué vas a construir:** un formulario que, cada vez que alguien lo llena:
1. Usa IA para **clasificar** la consulta (venta, soporte o queja).
2. **Redacta una respuesta** personalizada.
3. **Guarda** todo en Google Sheets.
4. **Envía** la respuesta por correo al cliente.

**⏱️ Tiempo:** 60 a 90 minutos
**💵 Costo:** prácticamente cero (prueba gratuita de n8n y créditos mínimos de IA)

```
[Formulario n8n] → [IA clasifica y responde] → [Google Sheets] → [Gmail]
```

---

### ✅ Antes de empezar: checklist

- [ ] Cuenta de Google (Gmail + Google Sheets)
- [ ] Cuenta en n8n Cloud (la crearás en el paso 1)
- [ ] Una clave de API de IA. Elige una opción:
  - **Opción A (gratis para practicar):** Google Gemini, desde [Google AI Studio](https://aistudio.google.com)
  - **Opción B:** OpenAI, desde [platform.openai.com](https://platform.openai.com). Requiere cargar un saldo mínimo; para este ejercicio el consumo es de centavos de dólar.

> 🔐 **Seguridad:** tu clave de API es como la contraseña de tu banco. No la compartas, no la publiques y guárdala en un lugar seguro.

---

### Paso 1: Crea tu cuenta en n8n (5 min)

1. Entra a **[n8n.io](https://n8n.io)** y haz clic en **"Get started"**.
2. Regístrate con tu correo y activa la prueba gratuita de n8n Cloud.
3. Al entrar verás tu panel principal (*Overview*).
4. Haz clic en **"Create Workflow"** (o en el botón **+**).
5. Ponle nombre en la parte superior: `Formulario de contacto inteligente`.

✅ **Checkpoint:** ves un lienzo en blanco con un botón **+** en el centro.

---

### Paso 2: Prepara tu Google Sheet (5 min)

1. Abre **[Google Sheets](https://sheets.google.com)** y crea una hoja nueva.
2. Llámala `Consultas clientes`.
3. En la **fila 1**, escribe estos encabezados (uno por columna):

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Fecha | Nombre | Email | Mensaje | Categoria | Respuesta |

✅ **Checkpoint:** tu hoja tiene los 6 encabezados en la fila 1.

---

### Paso 3: Crea el formulario, es decir, el disparador (10 min)

1. En n8n, haz clic en el **+** del centro del lienzo.
2. Busca **"Form"** y selecciona **"On form submission"** (n8n Form Trigger).
3. Configura:
   - **Form Title:** `Contáctanos`
   - **Form Description:** `Cuéntanos en qué podemos ayudarte`
4. En **Form Elements**, agrega 3 campos:

| Field Label | Element Type | Required |
|---|---|---|
| `Nombre` | Text | ✅ |
| `Email` | Email | ✅ |
| `Mensaje` | Textarea | ✅ |

5. Haz clic en **"Test step"**. Se abrirá tu formulario en una pestaña nueva.
6. Llénalo con datos de prueba, por ejemplo:
   - Nombre: `Laura Gómez`
   - Email: *(tu propio correo)*
   - Mensaje: `Hola, me interesa su servicio para mi empresa de 15 personas. ¿Cuánto cuesta el plan mensual?`
7. Envía el formulario y vuelve a n8n.

✅ **Checkpoint:** en el panel de salida (*OUTPUT*) del nodo ves los datos que acabas de enviar.

---

### Paso 4: Agrega la inteligencia artificial (20 min)

1. Haz clic en el **+** a la derecha del nodo del formulario.
2. Busca el nodo de tu proveedor de IA:
   - **Gemini:** busca "Google Gemini" y elige la acción para enviar un mensaje al modelo.
   - **OpenAI:** busca "OpenAI" y elige **"Message a model"**.
3. **Conecta tus credenciales:**
   - En **Credential**, haz clic en **"Create new credential"**.
   - Pega tu clave de API y guarda.
4. Elige el **modelo**. Para empezar, uno económico y rápido es suficiente (por ejemplo, las versiones "mini" o "flash").
5. En el campo del **mensaje o prompt**, pega este texto:

```
Eres el asistente de atención al cliente de [NOMBRE DE TU NEGOCIO], que ofrece [DESCRIBE TU PRODUCTO O SERVICIO].
Tono: amable, profesional y cercano. Escribe en español latinoamericano.

Un cliente envió este mensaje:
Nombre: 
Mensaje: 

Tareas:
1. Clasifica el mensaje en UNA categoría: "venta", "soporte" o "queja".
2. Redacta una respuesta breve (máximo 80 palabras) dirigida al cliente por su nombre.
   - Si es venta: agradece el interés y di que un asesor le enviará la propuesta en 24 horas.
   - Si es soporte: muestra empatía y di que el equipo técnico lo contactará pronto.
   - Si es queja: discúlpate sinceramente y di que un responsable lo llamará hoy.
   - No inventes precios, fechas ni datos que no tengas.

Responde ÚNICAMENTE en formato JSON, sin texto adicional:
{"categoria": "...", "respuesta": "..."}
```

6. **Inserta los datos dinámicos** (esta es la parte "mágica"):
   - A la izquierda verás el panel **INPUT** con los datos del formulario.
   - **Arrastra** el campo `Nombre` y suéltalo justo después de `Nombre: ` en tu prompt.
   - Haz lo mismo con `Mensaje`.
   - Se verán algo así: `{{ $json.Nombre }}` y `{{ $json.Mensaje }}`, normalmente resaltados en color.
7. Si tu nodo tiene una opción como **"Output Content as JSON"** o **"Simplify Output"**, actívala. Esto facilita usar la categoría y la respuesta por separado en los siguientes pasos.
8. Haz clic en **"Test step"**.

✅ **Checkpoint:** en el OUTPUT ves algo como:
```json
{
  "categoria": "venta",
  "respuesta": "¡Hola Laura! Gracias por tu interés en nuestros servicios. Un asesor te enviará una propuesta personalizada para tu equipo en las próximas 24 horas."
}
```

> 🧭 **Nota:** n8n actualiza su interfaz con frecuencia, así que los nombres exactos de botones u opciones pueden variar un poco. Si no encuentras algo, busca en el nodo una opción con un nombre similar o consulta la documentación oficial.

---

### Paso 5: Guarda todo en Google Sheets (15 min)

1. Haz clic en el **+** después del nodo de IA.
2. Busca **"Google Sheets"** y elige **"Append row in sheet"** (agregar fila).
3. **Credenciales:** haz clic en **"Create new credential"** → **"Sign in with Google"** → autoriza el acceso.
4. Configura:
   - **Document:** selecciona `Consultas clientes`
   - **Sheet:** selecciona `Hoja 1` (o el nombre de tu pestaña)
   - **Mapping Column Mode:** `Map Each Column Manually`
5. Ahora **arrastra los datos** a cada columna:

| Columna | Qué poner |
|---|---|
| Fecha | Arrastra el campo `submittedAt` del formulario (o escribe `{{ $now }}`) |
| Nombre | Arrastra `Nombre` desde el nodo del formulario |
| Email | Arrastra `Email` desde el nodo del formulario |
| Mensaje | Arrastra `Mensaje` desde el nodo del formulario |
| Categoria | Arrastra `categoria` desde el nodo de IA |
| Respuesta | Arrastra `respuesta` desde el nodo de IA |

> 💡 **Tip:** en el panel INPUT puedes desplegar los datos de **cualquier nodo anterior**, no solo del inmediatamente previo. Busca el nombre del nodo del formulario para encontrar Nombre, Email y Mensaje.

6. Haz clic en **"Test step"**.

✅ **Checkpoint:** abre tu Google Sheet; ¡debe aparecer una fila nueva con todos los datos! 🎉

---

### Paso 6: Envía la respuesta por correo (10 min)

1. Haz clic en el **+** después del nodo de Google Sheets.
2. Busca **"Gmail"** y elige **"Send a message"**.
3. Conecta tu cuenta de Google igual que en el paso anterior.
4. Configura:
   - **To:** arrastra el campo `Email` del formulario
   - **Subject:** `Recibimos tu mensaje, ` + arrastra `Nombre`
   - **Email Type:** `Text`
   - **Message:** arrastra el campo `respuesta` del nodo de IA
5. Haz clic en **"Test step"**.

✅ **Checkpoint:** revisa tu bandeja de entrada (y la carpeta de spam). Debe llegarte el correo con la respuesta generada por la IA.

---

### Paso 7: Prueba completa y activación (10 min)

1. Haz clic en **"Save"** (o usa `Ctrl + S`).
2. Haz clic en **"Test workflow"** y envía **3 mensajes de prueba diferentes**:
   - 💰 *Venta:* "¿Tienen planes para empresas pequeñas?"
   - 🔧 *Soporte:* "No puedo iniciar sesión en mi cuenta."
   - 😠 *Queja:* "Pagué hace una semana y todavía no recibo nada. Estoy muy molesto."
3. Verifica que cada uno se clasifique correctamente, que aparezca en el Sheet y que llegue el correo.
4. Cuando todo funcione, activa el interruptor **"Active"** (o **"Publish"**, según tu versión) en la parte superior.
5. Abre de nuevo el nodo del formulario y copia la **Production URL**. Ese es el enlace real que puedes compartir en tu web, Instagram o WhatsApp.

✅ **Checkpoint final:** tu flujo está activo y funcionando las 24 horas. 🚀

---

### 🆘 Solución de problemas comunes

| Problema | Posible causa | Solución |
|---|---|---|
| Error de credenciales en la IA | La clave de API es incorrecta o no tienes saldo | Copia la clave de nuevo y revisa el saldo en tu cuenta de OpenAI |
| La IA responde con texto extra además del JSON | El modelo no siguió el formato | Refuerza en el prompt: "Responde SOLO el JSON, sin explicaciones" |
| No aparecen `categoria` y `respuesta` como campos separados | La salida no se interpretó como JSON | Activa la opción de salida en JSON del nodo o revisa el formato del prompt |
| Los campos aparecen vacíos en Sheets | El mapeo apunta a un nodo equivocado | Vuelve a arrastrar los campos desde el nodo correcto |
| No llega el correo | Filtro de spam o error en el campo "To" | Revisa la carpeta de spam y verifica que el campo "To" tenga el email |
| El formulario de producción no funciona | El workflow no está activado | Activa el interruptor y usa la Production URL, no la de prueba |

---

### 🌟 Retos extra (opcionales)

1. **Nivel 1:** agrega un nodo **IF** después de la IA. Si la categoría es "queja", envíate una alerta a tu correo personal o por Telegram.
2. **Nivel 2:** reemplaza el IF por un nodo **Switch** con un camino distinto para cada categoría (venta → CRM, soporte → email al equipo técnico, queja → alerta urgente).
3. **Nivel 3:** cambia el envío automático por un **borrador**. Usa la opción de Gmail para crear un borrador en lugar de enviarlo, así revisas cada respuesta antes de mandarla (humano en el circuito).

---

## 📖 5. Recursos adicionales

### 📘 Documentación oficial
- **[Documentación de n8n](https://docs.n8n.io)**: guías de cada nodo y conceptos básicos
- **[Plantillas de n8n](https://n8n.io/workflows)**: cientos de flujos listos para copiar y adaptar; busca "AI", "lead" o "customer support"
- **[Comunidad de n8n](https://community.n8n.io)**: foro para resolver dudas, muy activo

### 🎥 Video
- **Canal oficial de n8n en YouTube**: tutoriales para principiantes y casos de IA
- Busca en YouTube "n8n en español" para encontrar creadores latinoamericanos con tutoriales paso a paso

### 🧰 Herramientas mencionadas
| Herramienta | Para qué | Enlace |
|---|---|---|
| n8n | Automatización | [n8n.io](https://n8n.io) |
| Make | Alternativa visual | [make.com](https://www.make.com) |
| Zapier | Alternativa sencilla | [zapier.com](https://zapier.com) |
| Google AI Studio | Claves de API de Gemini | [aistudio.google.com](https://aistudio.google.com) |
| OpenAI Platform | Claves de API de OpenAI | [platform.openai.com](https://platform.openai.com) |

### 📝 Plantilla descargable: "Mapa de automatización"

Copia esta tabla y llénala con 5 tareas de tu negocio:

| Tarea repetitiva | Disparador | ¿Qué haría la IA? | Acción final | Veces por semana | Min. por vez | Prioridad |
|---|---|---|---|---|---|---|
| Ej.: Responder precios | Mensaje de WhatsApp | Identificar producto y responder | Enviar respuesta | 40 | 5 | 🔥 Alta |
| | | | | | | |

---

## ✅ 6. Preguntas de autoevaluación

### Pregunta 1
**Tu tienda online recibe 50 correos diarios. ¿Cuál de estas tareas es la MEJOR candidata para empezar a automatizar con IA?**

a) Negociar un contrato de distribución con un proveedor nuevo
b) Clasificar los correos entrantes y responder las preguntas frecuentes sobre envíos y pagos
c) Decidir la estrategia de precios del próximo año
d) Responder a un cliente que amenaza con una demanda legal

<details>
<summary>👉 Ver respuesta</summary>

**Respuesta correcta: b)**

Es una tarea **muy frecuente** y con **poco criterio estratégico**, el cuadrante ideal de la matriz. Las opciones a) y c) son poco frecuentes y requieren mucho criterio humano, y la d) es un caso sensible que siempre debe atender una persona, aunque la IA podría ayudar a detectarlo y escalarlo.
</details>

---

### Pregunta 2
**En el ejercicio práctico, identifica las tres partes de la automatización: ¿cuál es el disparador, cuál el procesamiento y cuál la acción?**

<details>
<summary>👉 Ver respuesta</summary>

- **Disparador:** el envío del formulario (nodo *On form submission*).
- **Procesamiento:** el nodo de IA, que clasifica la consulta y redacta la respuesta.
- **Acción:** guardar la fila en Google Sheets y enviar el correo por Gmail.

Entender esta estructura te permite diseñar cualquier automatización: siempre pregúntate *¿qué la inicia?, ¿qué se hace con la información? y ¿qué resultado produce?*
</details>

---

### Pregunta 3
**Tu asistente automático de WhatsApp le dijo a un cliente que el envío era gratis, pero no lo es. ¿Qué dos ajustes harías para evitar que se repita?**

<details>
<summary>👉 Ver respuesta</summary>

Ajustes recomendados (cualquier par de estos es válido):

1. **Darle información precisa a la IA:** incluir en el prompt o en la base de conocimiento las políticas reales de envío, con montos y condiciones claras.
2. **Agregar una regla explícita contra inventar:** "Si no tienes la información, no la inventes; di que un asesor responderá".
3. **Agregar revisión humana o escalamiento** para temas de dinero (precios, descuentos, reembolsos).
4. **Revisar el registro de conversaciones** (por ejemplo, en Google Sheets) para detectar errores y mejorar el prompt.

**Lección clave:** la IA trabaja con la información y las instrucciones que le das. Una buena automatización necesita datos correctos, reglas claras y supervisión.
</details>

---

## 🎓 Cierre del módulo

> *"No se trata de reemplazar a tu equipo, sino de liberarlo de las tareas repetitivas para que haga el trabajo que realmente mueve tu negocio."*

### 📌 Tu tarea antes del Módulo 4
1. ✅ Termina el ejercicio práctico y compártelo en la comunidad del curso con una captura de tu flujo.
2. ✅ Llena el **Mapa de automatización** con 5 tareas de tu negocio.
3. ✅ Elige la tarea de mayor prioridad y dibuja (en papel o en n8n) su flujo de disparador, procesamiento y acción.

**Próximo módulo →** *Módulo 4: Agentes de IA, asistentes que trabajan por ti*