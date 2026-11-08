# Claude Sonnet 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.9 | quality: 9.72
- latency_total: 79.816s | tokens_per_second: 144.8
- input_tokens: 390 | output_tokens: 11554
- judge_score: 4.8 | justificación: 

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

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

**Duración estimada:** 3 horas (1 h de teoría y ejemplos + 2 h de práctica)
**Nivel:** Emprendedor no técnico (no se requiere programar)
**Requisitos previos:** Haber completado los Módulos 1 y 2, cuenta de Google y una cuenta de OpenAI, Google AI Studio u otro proveedor de IA con acceso por API

---

## 1. Objetivo del módulo

Al finalizar este módulo podrás **identificar qué procesos de tu negocio conviene automatizar, diseñar un flujo de trabajo con lógica clara (disparador → IA → decisión → acción) y construir tu primera automatización funcional con N8N**. No necesitas saber programar: aprenderás a pensar en flujos, escribir instrucciones efectivas para la IA dentro de ellos y establecer controles para que la automatización ayude a tu negocio sin comprometer la calidad ni la confianza de tus clientes.

---

## 2. Contenido teórico

### 2.1 ¿Qué es la automatización con IA?

**Automatización tradicional:** sigue reglas fijas. *"Si llega un correo con la palabra 'factura', guárdalo en la carpeta Facturas."*

**Automatización con IA:** además de seguir reglas, puede **interpretar, clasificar, redactar y decidir** con información ambigua o no estructurada. *"Lee este correo, entiende qué quiere el cliente, clasifícalo por urgencia y redacta un borrador de respuesta."*

| Característica | Automatización tradicional | Automatización con IA |
|---|---|---|
| Tipo de datos | Estructurados (formularios, números) | Texto libre, audios, imágenes, documentos |
| Lógica | Reglas exactas "si pasa X, haz Y" | Interpretación de contexto |
| Flexibilidad | Se rompe si el formato cambia | Se adapta a variaciones |
| Ejemplo | Copiar datos de un formulario a una hoja | Leer un mensaje y detectar si el cliente está molesto |

> **Idea clave:** la IA es una *pieza* dentro del flujo, no el flujo completo. El valor está en conectar la IA con tus herramientas de trabajo (correo, WhatsApp, hojas de cálculo, CRM).

### 2.2 Anatomía de un flujo de trabajo

Todo flujo automatizado se construye con cuatro bloques:

```
┌─────────────┐   ┌──────────────┐   ┌─────────────┐   ┌──────────────┐
│ 1. DISPARADOR│ → │ 2. PROCESAR  │ → │ 3. DECIDIR  │ → │ 4. ACTUAR    │
│ (Trigger)    │   │ (con IA)     │   │ (Condición) │   │ (Acción)     │
└─────────────┘   └──────────────┘   └─────────────┘   └──────────────┘
 ¿Qué inicia       ¿Qué debe          ¿Qué camino      ¿Qué se hace
 el flujo?         entender o crear   se sigue según   al final?
                   la IA?             el resultado?
```

**Ejemplo en lenguaje cotidiano:**
- **Disparador:** llega un nuevo mensaje de un cliente.
- **Procesar:** la IA lo lee y lo clasifica (consulta, queja, venta).
- **Decidir:** ¿es una queja grave?
- **Actuar:** si sí, avisa al dueño por Telegram; si no, responde automáticamente.

### 2.3 ¿Qué automatizar primero? La matriz de prioridad

No automatices todo. Evalúa cada tarea con estas preguntas:

| Criterio | Pregunta | Puntaje (1-5) |
|---|---|---|
| **Frecuencia** | ¿Cuántas veces a la semana se repite? | |
| **Tiempo** | ¿Cuánto tiempo consume cada vez? | |
| **Claridad** | ¿Puedo describir los pasos con claridad? | |
| **Bajo riesgo** | ¿Un error tendría poco impacto? | |

**Regla práctica:** empieza por tareas con puntaje alto en las cuatro dimensiones. Evita al inicio automatizar decisiones de alto riesgo (reembolsos grandes, temas legales, despidos).

### 2.4 Herramientas de automatización

| Herramienta | Tipo | Ventaja principal | Consideración |
|---|---|---|---|
| **N8N** | Visual, código abierto | Muy flexible, versión autoalojada gratuita, nodos de IA nativos | Curva de aprendizaje un poco mayor |
| **Make** (ex Integromat) | Visual | Interfaz amigable, muchas integraciones | El costo escala con el número de operaciones |
| **Zapier** | Visual | La más simple para empezar | Suele ser la más costosa al crecer |

> **Nota:** los planes y precios cambian con frecuencia. Verifica siempre las condiciones actuales en el sitio oficial de cada herramienta.

**¿Por qué usaremos N8N en este curso?**
1. Puedes empezar con su prueba gratuita en la nube o instalarlo tú mismo sin pagar licencia (versión *community*).
2. Tiene nodos específicos para IA (OpenAI, Google Gemini, agentes de IA, memoria conversacional).
3. Es muy popular entre startups por su flexibilidad y control de datos.
4. Su lógica visual (cajas conectadas por líneas) es fácil de entender.

### 2.5 Vocabulario esencial de N8N

| Término | Qué significa | Analogía |
|---|---|---|
| **Workflow** | El flujo completo | La receta |
| **Nodo** | Cada paso del flujo | Un ingrediente o paso de la receta |
| **Trigger** | El nodo que inicia el flujo | El timbre que se toca |
| **Credencial** | Permiso para conectar N8N con otra app | La llave de una puerta |
| **Webhook** | Una "dirección" que recibe datos de otras apps | Un buzón |
| **Ejecución** | Cada vez que el flujo corre | Cada vez que cocinas la receta |
| **API Key** | Clave que identifica tu cuenta en un servicio de IA | Tu contraseña de acceso |

### 2.6 Buenas prácticas y riesgos

**Buenas prácticas**
- **Humano en el circuito (human-in-the-loop):** al inicio, haz que la IA redacte borradores y que una persona apruebe antes de enviar.
- **Prompts específicos:** indica rol, contexto, formato de salida y restricciones.
- **Empieza pequeño:** un flujo de 4 a 6 nodos que funcione es mejor que uno de 30 que nadie entiende.
- **Documenta:** anota qué hace cada flujo y quién es responsable.
- **Mide:** registra tiempo ahorrado, errores y satisfacción del cliente.

**Riesgos a controlar**
- **Alucinaciones:** la IA puede inventar datos (precios, políticas). Dale información de referencia y prohíbele inventar.
- **Privacidad:** no envíes datos sensibles (documentos de identidad, datos financieros) a servicios de IA sin revisar sus políticas. Considera la normativa de tu país (por ejemplo, LFPDPPP en México, Ley 25.326 en Argentina, Ley 1581 en Colombia, LGPD en Brasil).
- **Costos descontrolados:** cada llamada a la IA tiene un costo por uso. Define límites de gasto en tu cuenta del proveedor.
- **Pérdida del toque humano:** automatiza lo repetitivo, no la relación estratégica con tus mejores clientes.
- **Términos de plataformas:** si automatizas WhatsApp, usa la API oficial (WhatsApp Business Platform) y revisa sus políticas.

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**Caso:** *Tienda online de café de especialidad en Colombia.* Recibe 40 a 60 mensajes diarios con preguntas repetitivas: envíos, precios, estado de pedidos, métodos de pago.

**Flujo:**

```
[Mensaje de WhatsApp/Telegram/Web]
          ↓
[IA: clasifica la intención]
 (envíos / precios / pedido / queja / otro)
          ↓
     [¿Qué tipo es?]
     ├── Pregunta frecuente → [IA responde usando la base de conocimiento]
     ├── Estado de pedido  → [Consulta en Google Sheets → IA redacta respuesta]
     └── Queja o complejo  → [Notifica a un humano + respuesta de "te contactaremos pronto"]
```

**Herramientas:** N8N + WhatsApp Business Cloud API (o Telegram para empezar) + OpenAI/Gemini + Google Sheets (como base de conocimiento y pedidos).

**Prompt base de ejemplo:**
```
Eres el asistente de atención al cliente de "Café Montaña", una tienda
de café de especialidad en Colombia. Responde de forma cálida, breve
(máximo 3 oraciones) y en español neutro latinoamericano.

REGLAS:
- Usa SOLO la información de la sección BASE DE CONOCIMIENTO.
- Si no sabes la respuesta, di: "Déjame confirmarlo con el equipo y te
  escribimos en breve" y no inventes datos.
- Si el cliente expresa molestia, discúlpate y deriva a un humano.

BASE DE CONOCIMIENTO:
{{ aquí van tus políticas de envío, precios, horarios, devoluciones }}

MENSAJE DEL CLIENTE:
{{ mensaje }}
```

**Resultados esperados:** reducir el tiempo de primera respuesta de horas a segundos para consultas frecuentes y liberar tiempo del equipo.

**Precauciones:** incluye siempre una vía para hablar con una persona y revisa semanalmente las conversaciones para mejorar la base de conocimiento.

**Dificultad:** ⭐⭐⭐ (intermedia)

---

### Ejemplo 2: Generación de contenido para redes sociales

**Caso:** *Startup de software contable para pymes en México.* Con un equipo de 3 personas, no logran publicar con constancia.

**Flujo:**

```
[Programación semanal: lunes 8:00 am]
          ↓
[Lee una hoja de Google Sheets con temas/ideas pendientes]
          ↓
[IA: genera 3 versiones de post]
 (LinkedIn · Instagram · X/Twitter)
          ↓
[IA: genera sugerencia de imagen o prompt visual]
          ↓
[Guarda borradores en Google Sheets/Notion]
          ↓
[Notifica al equipo por correo/Slack para revisión]
          ↓
[Tras aprobación manual → publica o programa]
```

**Herramientas:** N8N (nodo Schedule) + Google Sheets + OpenAI/Gemini + Gmail/Slack. Opcional: generador de imágenes y herramientas de programación de publicaciones.

**Prompt base de ejemplo:**
```
Actúa como community manager de una startup de software contable para
pymes en México. Tono: cercano, profesional, sin tecnicismos.

TEMA: {{ tema }}
PÚBLICO: dueños de pequeños negocios sin formación contable.

Genera:
1. Post para LinkedIn (máx. 120 palabras, con un gancho inicial y una
   pregunta final).
2. Post para Instagram (máx. 60 palabras, 3 hashtags relevantes).
3. Hilo para X de 3 tuits (máx. 250 caracteres cada uno).

No inventes estadísticas. Si necesitas un dato, indícalo con [VERIFICAR].
```

**Resultados esperados:** pasar de publicar de forma irregular a mantener un calendario semanal, ahorrando varias horas de redacción.

**Precauciones:** la revisión humana es obligatoria. Cuida la voz de marca, verifica datos y evita contenido genérico. Alimenta a la IA con ejemplos de tus mejores publicaciones.

**Dificultad:** ⭐⭐ (básica-intermedia)

---

### Ejemplo 3: Calificación automática de leads

**Caso:** *Agencia de marketing digital en Chile.* Recibe solicitudes de cotización por formulario web, pero el equipo pierde tiempo con prospectos que no tienen presupuesto o que no son su cliente ideal.

**Flujo:**

```
[Nuevo formulario enviado]
          ↓
[Se guarda en Google Sheets]
          ↓
[IA: analiza y puntúa el lead según tu cliente ideal]
 (Caliente / Tibio / Frío + motivo)
          ↓
     [¿Qué categoría?]
     ├── Caliente → [Aviso inmediato al vendedor + correo de agendamiento]
     ├── Tibio    → [Correo con caso de éxito + seguimiento en 3 días]
     └── Frío     → [Correo con recursos gratuitos / newsletter]
          ↓
[Actualiza la hoja con la categoría y el motivo]
```

**Herramientas:** Google Forms o formulario web + N8N + Google Sheets (o un CRM como HubSpot) + OpenAI/Gemini + Gmail.

**Prompt base de ejemplo:**
```
Eres un analista comercial de una agencia de marketing digital para
pymes en Chile.

CLIENTE IDEAL: empresas de 5 a 50 empleados, presupuesto mensual de
marketing superior a USD 800, con necesidad clara y plazo de inicio
menor a 2 meses.

Evalúa este lead y responde SOLO en este formato:
CATEGORIA: Caliente | Tibio | Frío
MOTIVO: (una frase)

DATOS DEL LEAD:
Empresa: {{ empresa }}
Empleados: {{ empleados }}
Presupuesto: {{ presupuesto }}
Necesidad: {{ necesidad }}
Plazo: {{ plazo }}
```

**Resultados esperados:** respuesta en minutos a los leads de mayor potencial, que es cuando más probabilidad de cierre hay, y menos tiempo perdido en prospectos poco calificados.

**Precauciones:** revisa periódicamente la calidad de la clasificación. Si la IA descarta leads que luego resultan buenos, ajusta los criterios. No uses la clasificación para tratar mal a nadie: incluso un lead "frío" merece una respuesta respetuosa.

**Dificultad:** ⭐⭐ (básica-intermedia)

---

## 4. Ejercicio práctico: Construye tu sistema de calificación de leads

**Tiempo estimado:** 90 a 120 minutos
**Resultado final:** un flujo en N8N que recibe un lead desde Google Sheets, lo clasifica con IA y te avisa por correo cuando es "Caliente".

### Antes de empezar: checklist

- [ ] Cuenta de Google (Gmail, Sheets y Forms)
- [ ] Cuenta en N8N Cloud (con prueba gratuita) o N8N instalado
- [ ] Cuenta con API de un proveedor de IA (OpenAI o Google Gemini) con un monto pequeño de crédito. Para el ejercicio, el costo suele ser mínimo
- [ ] Definición escrita de tu **cliente ideal** (3 a 5 líneas)

---

### Paso 1: Define tu cliente ideal (10 min)

Escribe en un documento:
1. ¿Qué tipo de empresa o persona es tu mejor cliente?
2. ¿Qué presupuesto mínimo necesita?
3. ¿Qué señales indican urgencia?
4. ¿Qué señales indican que **no** es buen prospecto?

> Esta definición será el "cerebro" de tu prompt.

---

### Paso 2: Crea la hoja de leads (10 min)

1. Crea una hoja de Google Sheets llamada `Leads - Módulo 3`.
2. En la fila 1 escribe estos encabezados, uno por columna:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Nombre | Email | Empresa | Empleados | Presupuesto | Necesidad | Categoría | Motivo |

3. Agrega **3 leads de prueba** (uno claramente bueno, uno dudoso y uno claramente malo). Deja vacías las columnas G y H.

**Ejemplos para copiar:**
- *Caliente:* Laura Pérez, laura@empresa.com, Muebles Andes, 25, USD 2.000/mes, "Necesitamos campañas en Meta y Google, queremos empezar este mes."
- *Tibio:* Carlos Díaz, carlos@correo.com, Estudio CD, 4, USD 600/mes, "Estamos viendo opciones para el próximo trimestre."
- *Frío:* Ana Ruiz, ana@correo.com, (vacío), 1, USD 50/mes, "Quiero saber cuánto cuesta hacer un logo."

---

### Paso 3: Crea el flujo en N8N (5 min)

1. Entra a tu cuenta de N8N y haz clic en **Create Workflow**.
2. Nómbralo: `Calificación de leads con IA`.

---

### Paso 4: Agrega el disparador (10 min)

1. Haz clic en **Add first step** y busca **Google Sheets**.
2. Elige el trigger **On row added** (cuando se agrega una fila).
3. En **Credential**, haz clic en *Create new* y sigue el asistente para conectar tu cuenta de Google.
4. Selecciona tu documento `Leads - Módulo 3` y la hoja correspondiente.
5. Haz clic en **Fetch Test Event**. Debes ver los datos de uno de tus leads de prueba.

✅ **Punto de control:** ves en pantalla campos como `Nombre`, `Presupuesto` y `Necesidad`.

> **Si falla:** revisa que la API de Google Sheets esté habilitada y que hayas autorizado los permisos. Si usas N8N Cloud, el asistente de credenciales de Google suele resolverlo.

---

### Paso 5: Agrega el nodo de IA (20 min)

1. Haz clic en el **+** a la derecha del nodo anterior.
2. Busca **OpenAI** (o el de tu proveedor) y elige la acción para enviar un mensaje a un modelo (*Message a model* o similar, según la versión).
3. Crea la credencial pegando tu **API Key**.
4. Elige un modelo económico y rápido, suficiente para clasificar texto.
5. En el mensaje, pega este prompt y **personalízalo con tu cliente ideal del Paso 1**:

```
Eres un analista comercial. Evalúa si este prospecto es un buen cliente
para mi negocio.

MI CLIENTE IDEAL:
[PEGA AQUÍ TU DEFINICIÓN DEL PASO 1]

Responde EXACTAMENTE con este formato, sin texto adicional:
CATEGORIA: Caliente | Tibio | Frío
MOTIVO: una frase de máximo 20 palabras

DATOS DEL PROSPECTO:
Nombre: {{ $json.Nombre }}
Empresa: {{ $json.Empresa }}
Empleados: {{ $json.Empleados }}
Presupuesto: {{ $json.Presupuesto }}
Necesidad: {{ $json.Necesidad }}
```

> Las expresiones `{{ $json.Campo }}` se insertan arrastrando los campos desde el panel izquierdo (*Input*) hacia el cuadro de texto. Los nombres deben coincidir exactamente con los encabezados de tu hoja.

6. Haz clic en **Execute step** y revisa la respuesta.

✅ **Punto de control:** la IA responde con `CATEGORIA: ...` y `MOTIVO: ...`.

> **Si falla:** si la respuesta incluye texto extra, refuerza la instrucción: *"No agregues saludos ni explicaciones."* Si da error de autenticación, revisa tu API Key y que tu cuenta tenga saldo.

---

### Paso 6: Extrae la categoría y el motivo (10 min)

1. Agrega un nodo **Edit Fields (Set)**.
2. Crea dos campos de tipo texto:
   - `categoria` con esta expresión (ajusta la ruta de la respuesta según lo que veas en tu nodo de IA):
     ```
     {{ $json.output[0].content[0].text.split('\n')[0].replace('CATEGORIA:','').trim() }}
     ```
   - `motivo` con:
     ```
     {{ $json.output[0].content[0].text.split('\n')[1].replace('MOTIVO:','').trim() }}
     ```
3. Haz clic en **Execute step**.

> **Importante:** la ruta exacta de la respuesta (`output[0].content[0].text`) varía según la versión del nodo. Haz clic y arrastra el campo de texto de la respuesta desde el panel *Input* y luego añade `.split(...)`. Si te cuesta, usa el asistente de IA integrado de N8N o pídele a ChatGPT: *"Tengo este JSON de salida [pega el JSON]. Dame la expresión de N8N para extraer la línea que empieza con CATEGORIA."*

✅ **Punto de control:** ves `categoria` = "Caliente" (o la que corresponda) y `motivo` con una frase.

---

### Paso 7: Actualiza la hoja de cálculo (10 min)

1. Agrega un nodo **Google Sheets** con la acción **Update row**.
2. Selecciona el mismo documento y hoja.
3. En **Column to match on**, elige `Email` (o la columna que identifique al lead de forma única) y asigna el valor del lead original.
4. Mapea:
   - Columna `Categoría` → `{{ $json.categoria }}`
   - Columna `Motivo` → `{{ $json.motivo }}`
5. Ejecuta el paso.

✅ **Punto de control:** en tu hoja de Google Sheets aparecen la categoría y el motivo en la fila del lead.

---

### Paso 8: Agrega la decisión (10 min)

1. Agrega un nodo **IF**.
2. Condición: `{{ $json.categoria }}` **is equal to** `Caliente`.
3. Tendrás dos salidas: **true** (es caliente) y **false** (no lo es).

---

### Paso 9: Configura la acción para leads calientes (10 min)

1. En la salida **true**, agrega un nodo **Gmail → Send a message**.
2. Conecta tu cuenta de Gmail.
3. Configura:
   - **To:** tu correo
   - **Subject:** `🔥 Lead caliente: {{ $json.Nombre }}`
   - **Message:**
     ```
     Nuevo lead de alta prioridad.

     Nombre: {{ $json.Nombre }}
     Empresa: {{ $json.Empresa }}
     Motivo de la calificación: {{ $json.motivo }}

     Contáctalo en las próximas 2 horas.
     ```

**Reto opcional:** en la salida **false**, agrega otro correo, esta vez al lead, con un mensaje cordial y un recurso útil. Para empezar, envíatelo a ti mismo como prueba.

---

### Paso 10: Prueba y activa (15 min)

1. Haz clic en **Execute Workflow** para probar el flujo completo.
2. Agrega manualmente un nuevo lead en tu hoja y verifica que el flujo se active y funcione.
3. Revisa las **Executions** (historial) para ver cómo se comportó cada nodo.
4. Cuando todo funcione, activa el flujo con el interruptor **Active**.

✅ **Punto de control final:**
- [ ] Los tres leads de prueba se clasifican de forma coherente
- [ ] La hoja se actualiza con categoría y motivo
- [ ] Recibes un correo solo para el lead caliente

---

### Paso 11: Mide y mejora (10 min)

Completa esta tabla de evaluación:

| Lead de prueba | Categoría esperada | Categoría de la IA | ¿Coincide? |
|---|---|---|---|
| Laura (Muebles Andes) | Caliente | | |
| Carlos (Estudio CD) | Tibio | | |
| Ana (sin empresa) | Frío | | |

Si no coincide, ajusta el prompt: agrega criterios más específicos, ejemplos de cada categoría o umbrales numéricos claros.

---

### Entregable del módulo

Entrega los siguientes elementos:
1. Captura de pantalla de tu flujo completo en N8N.
2. Tu prompt final con tu cliente ideal.
3. La tabla de evaluación del Paso 11.
4. Un párrafo de reflexión: *"¿Qué proceso de mi negocio automatizaría después y por qué?"*

### Problemas frecuentes

| Problema | Posible causa | Solución |
|---|---|---|
| El trigger no detecta filas nuevas | Intervalo de sondeo o permisos | Ejecuta el test manual, revisa credenciales y la frecuencia de revisión |
| La IA responde con formato distinto | Prompt poco restrictivo | Pide "responde EXACTAMENTE con este formato" e incluye un ejemplo |
| Campos vacíos en el prompt | Nombres distintos a los de la hoja | Arrastra los campos desde el panel Input en lugar de escribirlos |
| Error 401 o 429 en el nodo de IA | API Key incorrecta, sin saldo o límite alcanzado | Verifica la clave, el saldo y los límites de tu cuenta |
| Se ejecuta varias veces el mismo lead | Se actualiza la fila y vuelve a disparar el trigger | Agrega una condición para procesar solo filas con `Categoría` vacía |

---

## 5. Recursos adicionales

### Documentación y aprendizaje oficial
- **N8N Docs** (docs.n8n.io): guías de nodos, credenciales y conceptos básicos.
- **N8N Workflow Templates** (n8n.io/workflows): miles de plantillas que puedes importar y adaptar.
- **Canal oficial de N8N en YouTube:** tutoriales paso a paso.
- **Documentación de OpenAI y Google AI Studio:** guías de prompts y límites de uso.

### Plantillas para explorar
Busca en la biblioteca de N8N términos como *"lead qualification"*, *"customer support chatbot"*, *"social media content"* o *"Telegram AI assistant"*. Importa una, ejecútala y estudia cómo está construida.

### Herramientas complementarias
- **Make** y **Zapier:** alternativas para comparar.
- **Airtable / Notion:** como base de datos ligera o mini-CRM.
- **Telegram Bot (BotFather):** forma gratuita de practicar chatbots antes de pasar a WhatsApp API.
- **Google Apps Script:** para quienes quieran dar un paso más hacia el código.

### Lecturas recomendadas
- Guías de ingeniería de prompts de OpenAI, Anthropic y Google.
- Normativa de protección de datos de tu país (busca en el sitio de tu autoridad de protección de datos).

### Comunidades
- Foro de la comunidad de N8N (community.n8n.io).
- Grupos de emprendedores y no-code en español en LinkedIn, Telegram y Discord.

> **Consejo:** la mejor forma de aprender es **clonar y modificar**. Toma una plantilla, cámbiale un nodo y observa qué ocurre.

---

## 6. Preguntas de autoevaluación

**Pregunta 1.** Un amigo emprendedor dice: *"Voy a automatizar toda mi atención al cliente con IA para no volver a leer un mensaje."* Con lo aprendido, ¿qué riesgos le señalarías y qué diseño le recomendarías en su lugar? Menciona al menos dos buenas prácticas del módulo.

**Pregunta 2.** Describe con tus palabras los cuatro bloques de un flujo de trabajo (disparador, procesar, decidir, actuar) usando como ejemplo un proceso real de tu negocio o idea de negocio. Indica qué herramienta usarías en cada bloque.

**Pregunta 3.** Aplicas la matriz de prioridad a tres tareas de tu negocio: (a) responder preguntas frecuentes por WhatsApp, (b) negociar contratos con tus clientes más grandes y (c) clasificar facturas recibidas por correo. ¿Cuál automatizarías primero, cuál después y cuál no automatizarías (o lo harías con supervisión humana estricta)? Justifica tu respuesta.

---

### Respuestas orientativas para el instructor

1. Riesgos: respuestas inventadas, clientes frustrados sin salida a un humano, errores sin detectar, fuga de datos personales, costos no controlados. Recomendación: automatizar preguntas frecuentes con base de conocimiento controlada, derivar quejas y casos complejos a una persona, revisar conversaciones periódicamente y empezar con borradores aprobados por humanos.
2. Debe identificar un disparador concreto, una tarea de IA específica (clasificar, resumir, redactar), una condición de decisión y una acción final, cada uno con su herramienta.
3. Orden sugerido: (a) primero (frecuente, clara, riesgo bajo/medio), (c) después (repetitiva y estructurable, con revisión de excepciones), (b) no automatizar la negociación; a lo sumo, usar IA para preparar resúmenes, y siempre con decisión humana.

---

### 🚀 Próximo módulo

En el **Módulo 4** llevarás tus automatizaciones al siguiente nivel: construirás **agentes de IA con memoria y acceso a tus datos**, y aprenderás a medir el retorno de inversión de tus automatizaciones.