# MiniMax M3 — startup_content/curso_emprendimiento_modulo

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.0 | quality: 9.4
- latency_total: 107.943s | tokens_per_second: 78.0
- input_tokens: 364 | output_tokens: 8420
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una estructura bien organizada y ejemplos prácticos que son directamente útiles para emprendedores, aunque podría profundizar un poco más en algunos aspectos teóricos.

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

**Curso:** IA Práctica para Emprendedores  
**Duración estimada:** 3 horas  
**Nivel:** Emprendedor no técnico

---

## 1. Objetivo del módulo

En este módulo aprenderás cómo convertir una tarea repetitiva de tu negocio en un flujo de trabajo automatizado con inteligencia artificial, utilizando herramientas como n8n. Partiendo de un problema concreto —como responder clientes, publicar contenido o calificar prospectos— identificarás qué parte del proceso necesita IA, elegirás las herramientas adecuadas y construirás un flujo que puedas poner a funcionar. El objetivo no es que te conviertas en programador, sino que entiendas la lógica de la automatización y seas capaz de delegarla o construirla con ayuda.

---

## 2. Contenido teórico

### 2.1 ¿Qué es la automatización con IA?

**Automatizar** significa que una tarea que antes依赖于 que alguien la hiciera —como copiar datos, enviar correos o clasificar mensajes— ahora la realiza un sistema de forma automática.

La automatización tradicional usa reglas fijas:

> "Si el cliente escribe en Instagram, envíale este mensaje."

La automatización con IA es más flexible porque **interpreta el lenguaje**. Puede entender lo que el cliente quiere decir, aunque no use las palabras exactas que esperabas.

| Tipo | Ejemplo | Limitación |
|---|---|---|
| Regla simple | Si el correo contiene "factura", envíala al equipo contable | Solo funciona con palabras clave exactas |
| Automatización con IA | Lee el correo, detecta que es una factura, la clasifica y la envía | Entiende el contexto, aunque el redactado sea informal |

### 2.2 ¿Cuándo tiene sentido automatizar?

No todo debe automatizarse. La automatización tiene sentido cuando una tarea:

- ✅ Se repite muchas veces al día o a la semana
- ✅ Sigue siempre el mismo patrón o reglas claras
- ✅ Consume tiempo que podrías usar en decisiones estratégicas
- ✅ Genera errores humanos por volumen o cansancio

**No conviene automatizar:**

- ❌ Tareas que cambian constantly y requieren criterio humano
- ❌ Procesos que aún estás entendiendo o validando
- ❌ Decisiones delicadas sin supervisión (contrataciones, Queries legales, reclamos complejos)
- ❌ Tareas donde el costo de un error es muy alto

> **Regla práctica:** primero automatiza lo que ya sabes hacer bien. Si el proceso manual es un caos, automatizar solo acelera el caos.

### 2.3 Las 4 capas de un flujo de trabajo típico

Un flujo de automatización con IA suele tener cuatro piezas:

**1. Disparador (Trigger)** — el evento que inicia todo
- Un mensaje llega a WhatsApp
- Un formulario se envía
- Se crea un registro en tu CRM

**2. Procesamiento con IA** — donde ocurre el trabajo inteligente
- Clasificar, resumir, extraer datos, redactar, traducir
- Es la parte que usa el modelo de lenguaje (como GPT, Claude o Gemini)

**3. Condición (Logic)** — las reglas de decisión
- "Si el cliente menciona un problema técnico, escala a soporte"
- "Si la Probability de compra es mayor a 70%, notifica al vendedor"

**4. Acción (Action)** — lo que sucede al final
- Responder al cliente
- Crear una tarea en el CRM
- Publicar en redes sociales
- Enviar un informe por correo

### 2.4 ¿Qué es n8n?

**n8n** es una herramienta de automatización visual (código abierto) que permite conectar aplicaciones entre sí mediante nodos, sin necesidad de saber programar.

**Analogía simple:** imagina que automatizar es como montar una línea de producción con piezas en una cinta transportadora. En n8n:

- Cada **nodo** es una pieza (recibir mensaje, analizar con IA, guardar en base de datos)
- Las **conexiones** son la cinta transportadora
- El **flujo de trabajo** es el recorrido completo del producto

**¿Por qué n8n para emprendedores?**

| Ventaja | Qué significa para ti |
|---|---|
| Interfaz visual | Ves el flujo como un diagrama, no como código |
| Se conecta con muchas herramientas | Gmail, WhatsApp, Google Sheets, Slack, HubSpot, Shopify, Trello |
| Permite IA dentro del flujo | Integra modelos de lenguaje para analizar y redactar |
| Código abierto | Puedes autoalojarlo si prefieres control y privacidad |
| throat de IA a nivel de flujo | Puedes usar modelos propios o conectarte a APIs de OpenAI, Anthropic, Gemini |

**Conceptos mínimos que necesitas:**

- **Nodo:** un paso individual del proceso
- **Workflow:** el conjunto de nodos conectados
- **Credencial:** la autorización para que n8n acceda a tus cuentas (como tu Gmail o HubSpot)
- **Webhook:** un enlace que dispara el flujo cuando ocurre un evento externo
- **Ejecución:** cada vez que el flujo corre, n8n guarda un registro con lo que pasó

### 2.5 Alternativas y complementarios a n8n

No tienes que usar n8n para todo. Estas son otras opciones, según tu contexto:

| Herramienta | Ideal para | Nivel técnico |
|---|---|---|
| **n8n** | Flujos complejos, IA a nivel de workflow, autoalojamiento | Bajo a medio |
| **Zapier** | Integraciones rápidas entre apps, sin código | Muy bajo |
| **Make** | Automatizaciones visuales con lógica intermedia | Bajo |
| **LangChain / CrewAI** | Agentes de IA autónomos con herramientas | Medio a alto (código) |
| **ChatGPT / Claude con GPTs** | Asistentes internos que usan tus documentos | Muy bajo |
| **Microsoft Power Automate** | Ecosistema Microsoft (Office 365, Dynamics) | Bajo |

> **Consejo:** empieza con la opción más simple que resuelva tu problema. Many德拉figura現代 antes de saltar a n8n.

### 2.6 Buenas prácticas antes de construir

1. **Documenta el proceso manual actual.** Escribe cada paso tal como lo haces hoy.
2. **Identifica el cuello de botella.** ¿Dónde se va más tiempo? ¿Dónde hay más errores?
3. **Define qué NO debe hacer la IA.** Esto se llama *guardarraíl* o護栏 y evita sorpresas.
4. **Empieza pequeño.** Un flujo, una tarea, un canal.
5. **Prueba con casos reales.** 5 a 10 casos antes de dejarlo en producción.
6. **Mantén a un humano en el circuito.** Para temas sensibles, siempre必须有 revisión humana.
7. **Registra y vigila.** Revisa las ejecuciones semanales durante el primer mes.

---

## 3. Ejemplos prácticos de automatización para startups

### Ejemplo 1: Atención al cliente automatizada

**El problema**

Una startup de software B2B recibe 80-120 mensajes por semana por WhatsApp y email. El equipo responde manualmente las mismas preguntas: precios, horarios, estado de cuenta,如何 resetear una contraseña. Esto consume entre 15 y 20 horas semanales.

**El flujo automatizado**

```
[Cliente escribe por WhatsApp]
        ↓
[IA: clasifica la intención del mensaje]
        ↓
   ┌────────────────┬──────────────────┬─────────────────┐
   ↓                ↓                  ↓                 ↓
[Pregunta        [Problema         [Solicitud       [Mensaje
 frecuente]      técnico]        comercial]        fuera de scope]
   ↓                ↓                  ↓                 ↓
[IA redacta      [Escala a        [Notifica al      [Respuesta
 respuesta con   soporte humano   vendedor con      genérica +
 info de la      con contexto      resumen +         contacto
 base de         + prioridad      score]            humano]
 conocimiento]
   ↓                ↓                  ↓                 ↓
[Envía respuesta] [Envía respuesta  [Envía respuesta  [Envía respuesta
 + pide          + da tiempo       + ofrece        + deriva a
 confirmación]   estimado]        llamada]         persona]
```

**Lo que hace la IA aquí**

- **Clasificar** la intención: "facturación", "soporte técnico", "ventas", "otro"
- **Extraer datos** relevantes: número de cuenta, error reportado, fecha
- **Redactar** una respuesta acorde al tono de tu marca
- **Resumir** el historial para que el humano no tenga que leer toda la conversación

**Herramientas sugeridas**

| Paso | Herramientas |
|---|---|
| Entrada | WhatsApp Business API, Telegram Bot, formulario web |
| IA | OpenAI, Anthropic, Gemini vía n8n |
| Base de conocimiento | Google Sheets, Notion, Airtable, Pinecone (búsqueda semántica) |
| Salida | Respuesta automática + notificaciones a Slack o email |

**Métricas para seguir**

- % de mensajes resueltos sin intervención humana
- Tiempo promedio de respuesta (objetivo: < 2 minutos)
- Tasa de escalamiento a humano
- Satisfacción (CSAT) post-conversación

**Riesgos y mitigación**

- ⚠️ *El cliente cree que habla con una persona y se molesta al descubrirlo* → Incluye un aviso de transparencia: "Soy el asistente virtual de [Empresa]. ¿Te paso con un asesor?"
- ⚠️ *La IA da información incorrecta sobre precios* → Limita la IA a información cargada desde una fuente oficial y siempre ofrece escalar.
- ⚠️ *Se pierden conversaciones en temas complejos* → Guarda todo en el CRM con el resumen completo.

---

### Ejemplo 2: Generación de contenido para redes sociales

**El problema**

El fundador de una startup de nutrition spends 6-8 horas por semana escribiendo publicaciones para Instagram y LinkedIn. Lo pospone, el contenido es irregular y las publicaciones no tienen una estructura consistente. Quiere publicar 4 veces por semana sin que eso se convierta en su segundo empleo.

**El flujo automatizado**

```
[Programador (scheduler) — lunes, miércoles, viernes 9:00 AM]
        ↓
[Carga: pilares de contenido + tono de marca + productos del mes]
        ↓
[IA genera 3 variantes de copy por cada pilar]
        ↓
[IA genera sugerencias de imagen (prompt para IA visual)]
        ↓
[Guarda en cola de aprobación: Google Sheets / Notion / Airtable]
        ↓
[Notificación al fundador: "3 publicaciones listas para revisar"]
        ↓
[Fundador edita y aprueba]
        ↓
[Publicación automática en la plataforma]
        ↓
[Se registra el resultado: interacción, alcance, clics]
```

**Lo que hace la IA aquí**

- Genera variantes de copy adaptadas a cada plataforma (LinkedIn es más profesional; Instagram, más visual y cercano)
- Adapta la longitud y el tono
- Crea ideas de visual a partir de una descripción
- Reutiliza contenido existente con ángulos nuevos ("5 formas de...", "el error más común en...", "historia de un cliente...")

**Estructura de un prompt reutilizable**

```
ROL: Eres copywriter de una startup de nutrición deportiva.

CONTEXTO DE MARCA:
- Tono: cercano, basado en evidencia, sin promesas mágicas
- Audiencia: nanoparticles de 28-40 años que quieren energía
- Palabras que no usamos: "transformador", "revolucionario", "milagroso"

TAREA: Escribe un post para {plataforma} sobre {tema}.

REQUISITOS:
- Gancho en las primeras 2 líneas
- 1 idea central + 3 puntos accionables
- Cierre con pregunta
- 120-200 palabras

FORMATO DE SALIDA:
1. Versión A (storytelling)
2. Versión B (lista práctica)
3. Versión C (dato sorprendente)
```

**Herramientas sugeridas**

| Paso | Herramientas |
|---|---|
| Programación | n8n (nodo Schedule/Cron) |
| IA de texto | GPT, Claude, Gemini |
| Programación visual | n8n con credenciales de Instagram y LinkedIn, o Make/Zapier |
| Cola de aprobación | Notion, Airtable, Google Sheets + formulario |
| Almacenamiento de assets | Google Drive, Dropbox |

**Métricas para seguir**

- Publicaciones realizadas vs. planificadas
- Tiempo activo del fundador en contenido (objetivo: < 2 h/semana)
- Engagement rate promedio por pilar de contenido
- Clics al sitio web atribuidos a cada publicación

**Riesgos y mitigación**

- ⚠️ *Publicar sin revisión y que suene a robot* → Siempre deja la aprobación humana antes de publicar. La IA propone, el humano decide.
- ⚠️ *Contenido genérico que no diferencia a la marca* → Alimenta el prompt con pilares de contenido, casos de clientes reales y datos propios.
- ⚠️ *Publicaciones repetidas o sobre un tema saturado* → Guarda un registro de lo publicado y pídele a la IA que no repita temas.

---

### Ejemplo 3: Calificación automática de leads

**El problema**

Una startup SaaS B2B recibe entre 100 y 300 leads al mes desde formularios de Ads, referidos y eventos. El equipo comercial pierde tiempo en responder a personas que no tienen presupuesto ni encaje, y en cambio se demora en atender a los prospectos calificados. El problema clásico: **responden tarde a los buenos**.

**El flujo automatizado**

```
[Lead se registra en el CRM (formulario, web, evento)]
        ↓
[IA analiza: empresa, cargo, tamaño, industria, mensaje, interacciones]
        ↓
[IA extrae datos estructurados]
        ↓
[IA asigna score 0-100 + etiqueta de prioridad]
        ↓
   ┌───────────────┬───────────────┬──────────────────┐
   ↓               ↓               ↓                  ↓
[Score ≥ 80]    [50-79]         [20-49]           [< 20]
   ↓               ↓               ↓                  ↓
[Asignar al     [Asignar al     [Nutrir con        [Archivar +
 comercial con   comercial con  contenido          no contactar]
 respuesta       seguimiento    automático]
 inmediata en    en 24h         + email a
 < 5 min]        + nurturing   bsd comercial]
```

**Criterios de calificación configurables**

| Criterio | Ejemplo | Peso |
|---|---|---|
| Ajuste de producto (ICP) | ¿Es una empresa de 10-200 empleados en retail? | 30% |
| Nivel del cargo | ¿Es fundador, director o analista junior? | 20% |
| Señales de intención | ¿Visitó precios? ¿Asistió a un webinar? | 25% |
| Tamaño de la empresa | ¿El presupuesto potencial supera el mínimo? | 15% |
| Urgencia declarada | ¿Menciona "necesito para el mes que viene"? | 10% |

**Lo que hace la IA aquí**

- **Extrae y normaliza** datos de un mensaje libre de texto: "somos una奇的 de 45 personas en ecommerce" → empresa: 45 empleados, industria: ecommerce
- **Analiza** el perfil y el comportamiento
- **Redacta** un mensaje de primer contacto personalizado
- **Explica** su decisión: "Lead de 85 puntos: empresa de 120 empleados en retail (ICP exacto),-fundadora,Cpp-pedido demo"

**Herramientas sugeridas**

| Paso | Herramientas |
|---|---|
| Captura | Formulario web, Typeform, landing con tracking |
| Enriquecimiento | Clearbit, Apollo.io, LinkedIn Sales Navigator |
| IA | GPT, Claude, Gemini con prompt + criterios de scoring |
| CRM | HubSpot, Pipedrive, Salesforce, Notion |
| Outreach | Email (Mailgun, SendGrid), WhatsApp, LinkedIn |
| Notificaciones | Slack, email al comercial |

**Métricas para seguir**

- **Speed to lead:** tiempo entre el registro del lead y el primer contacto (meta: < 5 min para leads quentes)
- % de leads con scoring automático vs. manual
- Tasa de conversión a demo (lead → reunión → cliente)
- % de Commercial rep time en leads que realmente califican
- Ratio de inbound vs. outbound en el pipeline

**Riesgos y mitigación**

- ⚠️ *El modelo tiene sesgos y descarta buenos leads por ser "raros"* → Configura un canal de revisión: "Leads边缘 — decisión dudosa → humano".
- ⚠️ *Mensajes de primer contacto genéricos que dañan la marca* → Personaliza usando datos reales del lead; nunca con templates vacíos.
- ⚠️ *Riesgo legal por contacto automatizado* → Cumple GDPR/LGPD y las políticas del proveedor de email (no uses tu cuenta personal).
- ⚠️ *El comercial no confía en el score y lo ignora* → Explica los criterios y muéstrale el razonamiento. La transparencia genera confianza.

---

## 4. Ejercicio práctico paso a paso

### 🎯 Objetivo del ejercicio

Construirás un flujo funcional de **clasificación y respuesta de leads** en n8n con IA. Es el Ejemplo 3 simplificado: un formulario de contacto que llega a tu email o Google Sheets, la IA clasifica al lead y le responde, y tú recibes una notificación con el resultado.

**Tiempo estimado:** 60-90 minutos  
**Resultado:** un flujo activo que puedes mostrar a un socio, cliente o inversor.

---

### Paso 0 — Requisitos previos

**Cuentas necesarias (todas tienen plan gratuito):**

- [ ] Cuenta en [n8n.cloud](https://n8n.cloud) (o n8n autoalojado)
- [ ] Cuenta en [OpenAI](https://platform.openai.com) (necesitas agregar saldo mínimo para la API)
- [ ] Cuenta de Google con acceso a Gmail y Google Sheets
- [ ] Un documento con la información de tu negocio (precios, FAQ, descripción)

**Alternativa sin costo:** usa los nodos de credenciales genéricas con un modelo open-source local, o el nodo de OpenAI en modo simulación de n8n Cloud.

---

### Paso 1 — Define tu negocio en un documento

Crea un documento de Google con esta estructura. **Este documento será la "memoria" de tu IA.**

```
NOMBRE DE LA EMPRESA: [Nombre]
QUÉ HACEMOS: [Descripción en 2 líneas]
A QUIÉN SERVIMOS: [Cliente ideal]
PRECIO DEL SERVICIO: [Precio]
TIEMPO DE ENTREGA: [Plazo]
HORARIO DE ATENCIÓN: [Horario]
PREGUNTAS FRECUENTES:
  1. [Pregunta] → [Respuesta]
  2. [Pregunta] → [Respuesta]
  3. [Pregunta] → [Respuesta]
LO QUE NO VENDEMOS: [Límites claros]
TONO DE COMUNIDAD: [Formal / cercano / técnico]
```

---

### Paso 2 — Crea el formulario de entrada

1. En n8n, haz clic en **"Start"** y luego en **"Trigger manually"** (por ahora lo probaremos manual; luego lo automatizamos).
2. Añade el nodo **"Google Sheets"** → operación **Create Row** (o **Append Row**).
3. Configura las credenciales de Google.
4. Crea un Google Sheet llamado **Leads** con estas columnas:

| Nombre | Email | Empresa | Mensaje |
|---|---|---|---|
| (vacío) | (vacío) | (vacío) | (vacío) |

5. Selecciona el spreadsheet y la pestaña en el nodo.
6. En el nodo de Google Sheets, activa **"Simplify"** y en el campo de expresión escribe:

```
{{ $json.Nombre }}
```

Repite para Email, Empresa y Mensaje.

---

### Paso 3 — Agrega el nodo de IA

1. Añade el nodo **"OpenAI"** (o **"Basic LLM Chain"** + **"OpenAI Chat Model"**, que es más flexible).
2. Configura la credencial de OpenAI (API Key).
3. Selecciona el modelo **gpt-4o-mini** (rápido y económico) o el equivalente de tu proveedor.
4. En el **Prompt**, pega este texto (adáptalo a tu negocio):

```
Eres el asistente de clasificación de leads de [TU EMPRESA].

INFORMACIÓN DE LA EMPRESA:
[Aquí pega el contenido del Paso 1]

CONTEXTO DEL LEAD:
- Nombre: {{ $json.Nombre }}
- Email: {{ $json.Email }}
- Empresa: {{ $json.Empresa }}
- Mensaje: {{ $json.Mensaje }}

TAREA:
Analiza el lead y devuelve únicamente un JSON válido con esta estructura:

{
  "categoria": "interesado" | "pregunta" | "no_encaja" | "duda_especifica",
  "prioridad": "alta" | "media" | "baja",
  "motivo": "Explicación de máximo 2 frases de por qué clasificaste así",
  "respuesta_sugerida": "Respuesta breve y cordial al lead, máximo 4 líneas",
  "requiere_humano": true | false
}

CRITERIOS:
- "interesado": menciona precios, demo, quiere contratar o pregunta por el servicio explícitamente
- "pregunta": duda sobre funcionalidades, proceso o detalles técnicos
- "no_encaja": busca algo que no vendemos, empresa fuera del perfil o presupuesto menor al mínimo
- "duda_especifica": necesita información técnica o humana antes de decidir

TONO: {{ [Tu tono de comunidad] }}
No inventes información que no esté en el documento de la empresa.
```

5. En **Output Parser** (si usas Basic LLM Chain) o en la configuración de salida, indica que debe devolver **JSON**.
6. Agrega un nodo **"Code"** o **"Parse JSON"** para transformar la salida en campos utilizables.

---

### Paso 4 — Bifurca el flujo según la prioridad

1. Añade el nodo **"IF"** (Switch).
2. Configura las condiciones:

| Condición | Valor | Rama |
|---|---|---|
| `{{ $json.prioridad }}` | equals | `alta` |
| `{{ $json.prioridad }}` | equals | `media` |
| `{{ $json.prioridad }}` | equals | `baja` |

3. En la rama **alta**, añade un nodo **"Gmail"** → **Send Email**:
   - **To:** tu email
   - **Subject:** `🔥 Lead alta prioridad: {{ $json.Nombre }}`
   - **Body:** `Nombre: {{ $json.Nombre }}\nEmpresa: {{ $json.Empresa }}\nMotivo: {{ $json.motivo }}\n\nRespuesta sugerida:\n{{ $json.respuesta_sugerida }}`

4. En la rama **baja**, añade un nodo **"Gmail"** → **Send Email**:
   - **To:** tu email (o el de tu comercial)
   - **Subject:** `ℹ️ Lead baja prioridad: {{ $json.Nombre }}`
   - **Body:** con los datos y el motivo.

5. En la rama **media**, añade un nodo **"Google Sheets"** → **Update Row** para registrar la respuesta sugerida en una pestaña llamada **"Seguimiento"**.

---

### Paso 5 — Envía la respuesta automática al lead

1. En la rama **alta**, añade un nodo **"Gmail"** → **Send Email** (o un nodo de **HTTP Request** si usas la API de WhatsApp).
2. **To:** `{{ $json.Email }}`
3. **Subject:** `Gracias por escribir a [TU EMPRESA], {{ $json.Nombre }}`
4. **Body:**

```
Hola {{ $json.Nombre }},

{{ $json.respuesta_sugerida }}

Si quieres avanzar, responde a este correo y lo coordino
directamente contigo.

Saludos,
[Tu nombre]
[Tu empresa]
```

5. En la rama **baja**, envía también un correo pero con una respuesta de cortesía estándar (sin 빠진promesas comerciales).

---

### Paso 6 — Prueba el flujo

1. Haz clic en **"Execute Workflow"**.
2. En el nodo de Google Sheets, completa los datos manualmente:

```
Nombre: María González
Email: maria@techstore.com
Empresa: TechStore
Mensaje: Hola, somos una empresa de 60 personas en retail.
      Vi su producto y me interesa saber precios y si tienen demo.
      Necesitaríamos empezar el próximo mes.
```

3. Ejecuta y revisa cada nodo. Toca cualquier nodo para ver la **entrada y la salida** de los datos.
4. Revisa tu bandeja de entrada y la hoja de cálculo.

---

### Paso 7 — Valida con 5 casos de prueba

Ejecuta el flujo con estos casos y anota los resultados en una tabla:

| # | Nombre | Empresa | Mensaje | Prioridad esperada | ¿Aceptable? | Ajuste necessário |
|---|---|---|---|---|---|---|
| 1 | María González | TechStore (60 pers., retail) | "Me interesa precios y demo" | Alta | | |
| 2 | Juan Pérez | MicroApp (3 pers.) | "¿Cuánto cuesta?" | Baja (fuera de ICP) | | |
| 3 | Ana Ruiz | TechStore (60 pers., retail) | "¿Tiene integración con Shopify?" | Media | | |
| 4 | Carlos Díaz | RandomCorp | "Busco IA para hacer|Augmented reality" | Baja | | |
| 5 | Laura Soto | TechStore (60 pers., retail) | "Queremos una demo la próxima semana" | Alta | | |

**Si un caso falla, normalmente el problema está en:**
- Los criterios del prompt (poco claros o incompletos)
- El formato de salida JSON (pide JSON estricto explícitamente)
- Las condiciones del nodo IF (revisa que usen el campo correcto)

---

### Paso 8 — Conecta un disparador real

Ahora que el flujo funciona manual, cámbialo a producción:

**Opción A — Google Forms (gratis):**
1. Crea un Google Form con los campos: Nombre, Email, Empresa, Mensaje.
2. Ve a **Extensions → Apps** → conéctalo a Google Sheets con una pestaña nueva llamada **Entradas**.
3. En n8n, cambia el nodo de Google Sheets para que lea de **Entradas** con la opción **"Poll"** cada 1 minuto.

**Opción B — Webhook (más flexible):**
1. Reemplaza el nodo inicial por **"Webhook"** → método POST.
2. Copia la URL del webhook (test y producción).
3. Conecta tu formulario web o landing page para que envíe los datos a esa URL.

**Opción C — CRM:**
1. Si usas HubSpot o Pipedrive, usa su nodo nativo como disparador: **"HubSpot Trigger"** o **"Pipedrive Trigger"**.

---

### Paso 9 — Agrega control humano y monitoreo

1. En las ramas **alta** y **media**, añade un nodo **"Slack"** o **"Telegram"** que notifique al equipo:
```
🔔 Nuevo lead clasificado
{{ $json.Nombre }} — {{ $json.Empresa }}
Prioridad: {{ $json.prioridad }}
```
2. Activa las **ejecuciones guardadas** en n8n (Settings → executions) para poder revisar qué pasó.
3. Programa una revisión semanal: mira las ejecuciones fallidas y los casos mal clasificados, y ajusta el prompt.

---

### Paso 10 — Documenta y mide

Crea una ficha simple con esto:

```
FLUJO: Clasificación y respuesta de leads
DISPARADOR: Google Forms → Sheets → n8n (cada 1 min)
IA UTILIZADA: gpt-4o-mini / Claude Haiku
DATOS DE ENTRADA: Nombre, Email, Empresa, Mensaje
CRITERIOS DE PRIORIDAD: [copia del prompt]
LÍMITES (lo que la IA NO hace): [ej. no negocia precios, no promete fechas]
REVISIÓN HUMANA REQUERIDA: [ej. todo lead "alta" antes de envío]
MÉTRICAS: speed to lead, % alta prioridad, tasa de error
FECHA DE ÚLTIMA REVISIÓN: [fecha]
```

> 📌 **Consejo final:** este mismo flujo puede convertirse en tu **ejercicio de venta**. En una reunión con un prospecto, muéstrale el diagrama y explica cuánto tiempo le ahorra a su equipo. La automatización se vuelve una ventaja competitiva cuando la puedes demostrar.

---

## 5. Recursos adicionales

### 📚 Documentación y aprendizaje

| Recurso | Enlace | Para qué te sirve |
|---|---|---|
| Documentación oficial de n8n | [docs.n8n.io](https://docs.n8n.io) | Referencia de nodos y Integraciones |
| n8n Academy (courses) | [academy.n8n.io](https://academy.n8n.io) | Cursos gratuitos paso a paso |
| n8n Templates | [n8n.io/workflows](https://n8n.io/workflows) | Flujos listos para adaptar |
| OpenAI Platform Docs | [platform.openai.com/docs](https://platform.openai.com/docs) | Referencia de la API y prompts |
| Anthropic Docs | [docs.anthropic.com](https://docs.anthropic.com) | Guías de prompting y uso de Claude |
| Anthropic Prompt Library | [docs.anthropic.com/en/prompt-library](https://docs.anthropic.com/en/prompt-library) | Prompts probados por categoría |
| Learn Prompting | [learnprompting.org](https://learnprompting.org) | Curso gratuito de prompt engineering |
| Zapier Blog (automatización) | [zapier.com/blog](https://zapier.com/blog) | Ideas de flujos e inspiraciones |

### 🛠️ Herramientas complementarias

- **Diagrama de flujos:** [diagrams.net](https://app.diagrams.net) (gratis) o FigJam
- **Documentos de conocimiento:** Notion, Google Docs, Airtable
- **CRM gratuito:** HubSpot Free, Pipedrive (plan básico), Notion + Sheets
- **Formularios:** Google Forms, Typeform, Tally
- **Búsqueda semántica:** Pinecone, Weaviate, o simplemente Google Sheets + GPT
- **Mensajería transaccional:** Twilio, SendGrid, WhatsApp Business API

### 🎥 Canales en español

- YouTube: **Automatiza con n8n**, **Aprende IA con empathy.io**, **Codeando Scripts**
- YouTube: **La coded school**, **HolaTech** (IA aplicada a negocios)
- Podcast: **Decoder Ring** (IA), **Cuando conectado** (negocios y tecnología)

### 📖 Libros recomendados

- *AI for Small Business* — Stephen M. Johnson
- *The Checklist Manifesto* — Atul Gawande (pensamiento en procesos)
- *Superforecasting* — Tetlock & Gardner (toma de decisiones con incertidumbre)
- *Automate the Boring Stuff with Python* — Al Sweigart (automatización, aunque con código)

### ⚖️ Consideraciones legales y de privacidad

- Revisa el **RGPD** (Europa) o la **LGPD** (Latinoamérica) si manejas datos personales
- Usa los **Acuerdos de Procesamiento de Datos (DPA)** de OpenAI, Anthropic y Google para empresas
- En marketing por email, cumple las **normas CAN-SPAM** (EE.UU.) o equivalentes locales
- Documenta cómo usas IA en tus políticas de privacidad (obligatorio en varios países)

---

## 6. Preguntas de autoevaluación

### Pregunta 1 — Diseño del flujo

Estás automatizando la respuesta a mensajes de clientes en WhatsApp. Tu negocio vende un producto B2B con un proceso de onboarding de 2 semanas. Explica en un párrafo (máximo 150 palabras):

- ¿Qué nodos usarías y en qué orden?
- ¿En qué punto la IA entra y qué tarea específica le delegarías?
- ¿En qué punto detendrías el flujo para que un humano intervenga y por qué?

<details>
<summary>Ver respuesta sugerida</summary>

```
Flujo propuesto:
1. Trigger: WhatsApp Business API (mensaje entrante)
2. IA: clasificar intención (soporte, ventas, onboarding, otro)
   + extraer datos clave
3. IA: redactar respuesta usando la base de conocimiento
4. IF: ¿intención = onboarding o requiere_humano = true?
   → Sí: escala a humano con resumen + contexto + prioridad
   → No: envía respuesta automática
5. Acción final: guarda toda la conversación en el CRM
   y notifica al equipo en Slack

Punto de intervención humana: onboarding (proceso de 2 semanas
que requiere coordinación, políticas y excepciones) y cualquier
mensaje que mencione reclamos, pagos o dissatisfaction. Ahí la IA
prepara el contexto, pero no decide ni promete fechas.

Justificación: las preguntas frecuentes son alto volumen y baja
complejidad (la IA las resuelve bien y rápido); los casos de
onboarding son bajo volumen y alta complejidad (un error cuesta
un cliente).
```
</details>

---

### Pregunta 2 — Criterios de automatización

Una startup de 5 personas recibe 200 mensajes al mes por Instagram. El fundador dice: *"Quiero automatizar TODO con IA, así no tenemos que responder"*. ¿Qué le recomendarías? Menciona **al menos dos razones por las que no conviene automatizar todo** y qué automatizarías primero.

<details>
<summary>Ver respuesta sugerida</summary>

```
Le recomendaría empezar por automatizar solo una parte, por estas razones:

1. Volumen bajo: 200 mensajes/mes es manejable a mano (~1 hora
   semanal). El esfuerzo de construir y mantener el flujo no se
   justifica todavía. La automatización tiene un costo de
   setup y mantenimiento que a este volumen no se recupera.

2. Riesgo de la experiencia del cliente: un mensaje mal interpretado
   o una respuesta incorrecta en Instagram puede costar más que
   el tiempo que se ahorra. La marca se juega en la conversación.

3. "TODO" nunca funciona bien: las excepciones, los reclamos
   complejos y las conversaciones que piden un humano necesitan
   un路径清晰 de escalamiento.

4. La IA no sabe todavía: el proceso manual de respuesta todavía
   no está documentado ni optimizado. Automatizar un proceso
   disorderly amplifica el desorden.

Qué automatizaría primero:
- Clasificación de intención de cada mensaje (etiquetado automático
  en el inbox: ventas / soporte / reclamo / consulta)
- Respuestas automáticas a las 3 preguntas más frecuentes
  (horarios, precios, ubicación)
- Notificación al equipo para los mensajes marcados como urgentes
  o reclamos, con resumen y cliente highlighted

Dejaría en manos humanas: reclamos, negociacio commercial,
conversaciones con，申请 de Employment o temas legales.
```
</details>

---

### Pregunta 3 — Criterio de éxito y mejora

Construiste el flujo de calificación de leads del ejercicio. Tres semanas después observas estos datos:

| Métrica | Resultado | Meta |
|---|---|---|
| Speed to lead (alta prioridad) | 9 minutos | < 5 minutos |
| Leads clasificados correctamente | 82% | > 90% |
| Tasa de conversión a demo | 14% | 20% |
| Lead contactado que no estaba en ICP | 12% | < 5% |

**¿Qué tres cambios concretos harías en el flujo para mejorar estos indicadores, y cómo los medirías?**

<details>
<summary>Ver respuesta sugerida</summary>

```
1. Speed to lead (9 min vs. meta < 5 min):
   Cambiar el trigger de polling (cada 1 min) a webhook directo
   desde el formulario/CRM. Así el lead entra al flujo en segundos.
   Medir: tiempo entre timestamp del formulario y timestamp del
   primer contacto, con alerta en Slack si supera 5 minutos.

2. Precisión de clasificación (82% vs. meta > 90%):
   Revisar los 20 casos mal clasificados y enrich el prompt con
   ejemplos concretos de tu negocio (few-shot prompting: "ESTE
   lead es alta prioridad porque...; ESTE no lo es porque...").
   Agregar un nodo IF que mande a revisión manual los leads con
   score entre 70 y 85 (zona de ambigüedad).
   Medir: % de clasificación correcta semanal, evaluada con una
   muestra de 10 leads auditada por el comercial.

3. Leads fuera del ICP contactados (12% vs. meta < 5%):
   Endurecer los criterios de tamaño de empresa e industria en el
   prompt y añadir un filtro determinístico (nodo IF, no IA) que
   descarte automáticamente empresas fuera del rango antes de que
   la IA los procese. Dejar el scoring flexible solo dentro del
   ICP.
   Medir: ratio de leads contactados / leads dentro del ICP.

Bonus: la conversión a demo (14%) depende más del mensaje que
del scoring. Probaría 2 versiones del mensaje de primer contacto
(A/B testing con nodo IF + Split + Google Sheets) y mediría
conversión por variante.
```
</details>

---

## ✅ Checklist de cierre del módulo

- [ ] Entiendo las 4 capas de un flujo (trigger, IA, condición, acción)
- [ ] Documenté un proceso manual de mi negocio paso a paso
- [ ] Identifiqué qué parte de ese proceso tiene mayor volumen y menor complejidad
- [ ] Construí un flujo funcional en n8n con al menos un nodo de IA
- [ ] Lo probé con 5 casos reales y ajusté el prompt
- [ ] Lo conecté a un disparador real (Forms, webhook o CRM)
- [ ] Definí los límites de la IA y los puntos de revisión humana
- [ ] Definí 3 métricas para medir el impacto en mi negocio
- [ ] Calculé el ahorro estimado de tiempo vs. el costo del flujo

---

> 💡 **Para el siguiente módulo:** llevarás estos flujos de automatización hacia **agentes de IA** que no solo ejecutan tareas, sino que toman decisiones y usan herramientas de forma autónoma. Primero necesitas tener automatizaciones sólidas — ahora las tienes.

---

*Módulo 3 — IA Práctica para Emprendedores*
*¿Tienes dudas con algún paso del ejercicio? Comparte tu flujo en el espacio de la comunidad para recibir feedback.*