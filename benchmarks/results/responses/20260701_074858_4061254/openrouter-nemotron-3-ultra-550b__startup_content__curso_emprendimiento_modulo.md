# Nemotron 3 Ultra 550B — startup_content/curso_emprendimiento_modulo

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 65.394s | tokens_per_second: 109.5
- input_tokens: 250 | output_tokens: 7158

## Respuesta completa

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo  
**Curso:** IA Práctica para Emprendedores  
**Duración estimada:** 3 horas (1h teoría + 1.5h práctica + 0.5h autoevaluación)  
**Nivel:** Emprendedor no-técnico | **Herramienta principal:** n8n (alternativas: Make, Zapier)

---

## 1. 🎯 Objetivo del Módulo

Al finalizar este módulo, serás capaz de **identificar procesos repetitivos en tu startup que consumen tiempo valioso**, diseñar la lógica de un flujo de trabajo automatizado (prompt + herramienta + disparador + acción) y **construir tu primera automatización funcional en n8n** sin escribir código, integrando modelos de IA (como GPT o Claude) para resolver tareas reales de atención al cliente, marketing o ventas, reduciendo tu carga operativa en al menos un 30% desde la primera semana.

---

## 2. 📚 Contenido Teórico: Automatización con IA para No-Técnicos

### 2.1 ¿Qué es realmente "Automatización con IA"?
No es magia, es **orquestación**. Conectas tres piezas:
1.  **Disparador (Trigger):** Un evento que inicia el flujo (ej. "Llega un email", "Nuevo formulario", "Cada lunes a las 9am").
2.  **Cerebro (IA / Lógica):** Procesa la información. Aquí vive tu *Prompt Engineering* (Módulo 2). La IA clasifica, resume, redacta, decide o extrae datos.
3.  **Acción (Output):** El resultado tangible (ej. "Responder email", "Crear tarea en Notion", "Publicar en LinkedIn", "Actualizar CRM").

> **Analogía:** Piensa en n8n como el **gerente de operaciones** que nunca duerme. La IA es el **analista senior** que lee y entiende el contexto. Tú eres el **CEO** que define las reglas del juego una sola vez.

### 2.2 Herramientas del Ecosistema (No-Code / Low-Code)

| Herramienta | Ideal para... | Curva de aprendizaje | Costo inicial (USD/mes) | Dato clave para Latam |
| :--- | :--- | :--- | :--- | :--- |
| **n8n** (Self-hosted / Cloud) | **Control total, privacidad de datos, flujos complejos, costo fijo.** | Media (Editor visual nodos) | **Gratis** (Self-hosted) / $20+ (Cloud) | **Recomendada en este curso.** Alojas tus datos en tu servidor (DigitalOcean, AWS, Hetzner) o usas su nube. Ideal para datos sensibles de clientes (LGPD/Leyes locales). |
| **Make (ex-Integromat)** | Visualización visual muy intuitiva, muchas plantillas. | Baja-Media | Gratis (hasta 1k ops) / $9+ | Muy popular en agencias Latam. Interfaz "arrastrar y soltar" muy bonita. |
| **Zapier** | Conexiones simples (A -> B), miles de apps nativas, cero configuración técnica. | Muy Baja | Gratis (100 tareas) / $19.99+ | La más cara al escalar. "Impuesto Zapier" alto en Latam por tipo de cambio. |
| **Activepieces** | Alternativa open-source a Zapier, moderna, buena para IA. | Baja | Gratis (Self-hosted) | Comunidad creciente, buena para empezar gratis 100%. |

**¿Por qué n8n en este curso?**
1.  **Costo predecible:** Pagas servidor (~$5-10/mes), no por "operación" o "tarea". Escala sin sustos en la factura.
2.  **Nodos de IA nativos:** Tiene nodos listos para OpenAI, Anthropic, Google Gemini, Ollama (local), Pinecone, Qdrant (RAG).
3.  **Flexibilidad:** Permite código (JavaScript/Python) *si* lo necesitas luego, pero no lo requieres ahora.
4.  **Soberanía de datos:** Crítico si manejas datos de salud, finanzas o PII de usuarios en México, Colombia, Argentina, Chile, etc.

### 2.3 Arquitectura Mental de un Flujo (Workflow)
```mermaid
graph LR
    A[🔔 Disparador<br>ej. Webhook / Email / Cron] --> B{🧠 Nodo IA<br>Prompt Estructurado}
    B --> C[🛠️ Procesamiento<br>JSON / Código / Lógica]
    C --> D[✅ Acción 1<br>ej. Responder / Guardar]
    C --> E[✅ Acción 2<br>ej. Notificar Slack / CRM]
```
**Regla de Oro:** *Un flujo = Un objetivo claro de negocio.* No intentes hacer "todo en uno". Separa: "Clasificar Lead" ≠ "Enviar Email de Bienvenida".

---

## 3. 💡 3 Ejemplos Prácticos para Startups (Casos Reales Latam)

### Caso 1: Atención al Cliente Automatizada (Clasificación + Respuesta Borrador)
**Dolor:** Recibes 50+ emails/día en `soporte@tuapp.com`. Responder manualmente toma 3h/día. Muchas son FAQs.
**Flujo n8n:**
1.  **Trigger:** *Email Trigger (IMAP/Gmail/Outlook)* → Nuevo email en carpeta "Soporte".
2.  **Nodo IA (OpenAI/Anthropic):** *Prompt:* "Clasifica este email en: [Bug Técnico, Facturación, Cancelación, Consulta General, Spam]. Extrae: Nombre cliente, Urgencia (Alta/Media/Baja), Resumen 1 línea. Devuelve JSON."
3.  **Nodo IF (Lógica):**
    *   *Si "Consulta General" + Urgencia "Baja"* → **Nodo IA 2:** Genera borrador de respuesta usando Base de Conocimiento (RAG simple: PDF/Notion/Google Docs) → **Acción:** Crea borrador en Gmail / Asigna etiqueta "Auto-Responder" / Notifica a Slack #soporte: "Borrador listo para revisar".
    *   *Si "Bug Técnico" O "Cancelación" O "Alta"* → **Acción:** Reenvía a humano (Forward email / Crea ticket en Linear/Jira/Notion / Alerta Slack @equipo-soporte).
**Resultado:** El 60-70% de emails (FAQs, dudas simples) tienen borrador listo en segundos. Tú solo apruebas/editas. Ahorro: ~2h/día.

### Caso 2: Generación de Contenido para Redes Sociales (Content Repurposing)
**Dolor:** Tienes 1 artículo de blog / video / podcast semanal. Adaptarlo a LinkedIn, Twitter/X, Instagram, TikTok, Newsletter toma 4h.
**Flujo n8n:**
1.  **Trigger:** *Manual Trigger* (Tú das clic "Ejecutar") O *Cron* (Cada lunes 8am) O *Webhook* (Desde Notion al publicar).
2.  **Input:** URL del contenido original (Blog, YouTube, Drive, Notion).
3.  **Nodo HTTP Request / Scraper:** Extrae texto/transcripción del URL.
4.  **Nodo IA (Cadena de Prompts / Sub-workflows):**
    *   *Prompt 1 (Estratega):* "Analiza el contenido. Define: Tema central, 3 insights clave, Audiencia objetivo, Tono de marca (adjunta Voice Guide)."
    *   *Prompt 2 (Copywriter LinkedIn):* "Escribe post LinkedIn (1300 chars, gancho, desarrollo, CTA, 3 hashtags). Formato: Texto listo para copiar."
    *   *Prompt 3 (Copywriter Twitter/X):* "Escribe Hilo de 5-7 tweets. Gancho fuerte. Formato: Tweet 1\n---\nTweet 2..."
    *   *Prompt 4 (Copywriter Instagram):* "Texto para Caption (gancho, valor, CTA 'Link en bio'). Sugiere 3 ideas visuales (Carousel/Reel/Static)."
    *   *Prompt 5 (Newsletter):* "Resumen 3 párrafos + 'Leer más' + Sección 'Herramienta de la semana'."
5.  **Acción:** **Google Sheets / Notion / Airtable** → Crea fila con: Fecha, URL Original, Post LinkedIn, Hilo Twitter, Caption IG, Newsletter, Estado ("Pendiente Revisión").
6.  **Notificación:** Slack/Email/Telegram: "📦 Pack de contenido listo para revisar en [Link Notion]".
**Resultado:** De 4h a 30 min (revisar + programar en Buffer/Metricool/Later). Consistencia de marca garantizada por *Voice Guide* en prompts.

### Caso 3: Calificación Automática de Leads (Lead Scoring + Enriquecimiento + Routing)
**Dolor:** Formulario web trae 20 leads/día. 15 son basura (estudiantes, competidores, sin presupuesto). Ventas pierde tiempo llamando a todos.
**Flujo n8n:**
1.  **Trigger:** *Webhook* (Recibe JSON del formulario: Webflow, Typeform, Tally, HubSpot, WordPress).
2.  **Nodo IA (Clasificación + Enriquecimiento):**
    *   *Prompt:* "Recibes: Nombre, Email, Empresa, Cargo, Mensaje, Tamaño empresa (campo form). Tareas: 1. Verifica si email es corporativo (no @gmail/@yahoo/@hotmail/@outlook/@live/@icloud/@proton/@yandex). 2. Busca info pública de la empresa (simula: industria, tamaño real, tech stack si sabes). 3. Calcula Score 0-100: Email corp (20), Cargo decisor (30), Empresa >50 emp (20), Industria objetivo (20), Necesidad clara en mensaje (10). 4. Categoría: 'Hot' (80+), 'Warm' (50-79), 'Cold' (<50), 'Spam/Estudiante' (email personal + cargo junior). 5. Devuelve JSON con todo."
3.  **Nodo Switch (Routing):**
    *   *Hot* → **Acción:** Crea Deal en Pipedrive/HubSpot/Close/Attio (Stage: "Nuevo Hot") + Asigna a Vendedor Senior (Round Robin) + Alerta Slack 🔥 "LEAD HOT: [Empresa] - [Cargo] - Score: 92".
    *   *Warm* → **Acción:** Crea Deal (Stage: "Nuevo Warm") + Asigna a Vendedor Junior + Email automático sequence (Apollo/Instantly/Email nativo) "Hola [Nombre], vi que...".
    *   *Cold* → **Acción:** Guarda en Google Sheet "Leads Fríos - Nutrir" + Tag "Newsletter Only".
    *   *Spam/Estudiante* → **Acción:** Ignora / Log en Sheet "Filtrados" / No crea en CRM.
4.  **Nodo IA (Opcional - Research Agent):** Para *Hot/Warm*, segundo llamado a IA con herramienta *SerpAPI / Tavily / Exa* → "Investiga empresa: Últimas noticias, LinkedIn CEO, Stack tecnológico (BuiltWith), Dolor probable según nuestra solución". Guarda en Nota del Deal.
**Resultado:** Ventas habla **solo** con leads calificados. Ciclo de venta acortado. Marketing sabe qué canales traen *Hot* leads (UTM tracking en formulario).

---

## 4. 🛠️ Ejercicio Práctico Paso a Paso: "Clasificador de Emails de Soporte a Notion"

**Objetivo:** Crear un flujo en n8n que lea emails de una carpeta específica, use IA para clasificarlos y extraer datos clave, y guarde todo ordenado en una Base de Datos de Notion para que tu equipo los triagee visualmente.

**Tiempo:** 60-90 min  
**Prerrequisitos:**
*   Cuenta n8n (Cloud trial 14 días gratis **O** Self-hosted en VPS $5/mes - *recomendado para curso*).
*   Cuenta Google (Gmail) / Outlook / IMAP genérico.
*   Cuenta Notion (Plan Gratis sirve).
*   API Key de OpenAI (créditos $5 USD alcanzan para meses de testing) **O** Anthropic (Claude) **O** Google AI Studio (Gemini - **Gratis generoso**).

---

### Paso 1: Preparar el "Terreno" (5 min)

1.  **En Gmail:** Crea una etiqueta (label) llamada `IA_Entrada_Soporte`. Configura un filtro: *From: (tus emails de prueba) → Apply label: IA_Entrada_Soporte → Skip Inbox (Archive) [Opcional, para no ensuciar]*.
2.  **En Notion:**
    *   Crea una página nueva: `📥 Bandeja Entrada IA`.
    *   Dentro, crea una **Base de Datos - Tabla** (New database → Table view). Nombre: `Tickets Soporte IA`.
    *   Propiedades (Columnas):
        *   `📧 Asunto` (Title)
        *   `👤 Remitente` (Email)
        *   `📅 Fecha Recibido` (Date)
        *   `🏷️ Categoría` (Select: *Bug, Facturación, Consulta, Cancelación, Spam, Otro*)
        *   `⚡ Urgencia` (Select: *Alta, Media, Baja*)
        *   `📝 Resumen IA` (Text)
        *   `🔗 Link Email` (URL - para abrir original)
        *   `✅ Estado` (Select: *Nuevo, En Proceso, Resuelto, Spam* - Default: *Nuevo*)
    *   **Importante:** Copia el **Database ID** de la URL: `https://www.notion.so/TU_WORKSPACE/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX?v=...` → El ID son los 32 caracteres antes de `?v=`. Guárdalo.
    *   En Notion: Settings → Connections → Develop or manage integrations → New integration → Nombre: `n8n Soporte Bot` → Associated workspace → **Internal Integration Secret** (copia el token `secret_...`). Guárdalo.
    *   Ve a tu Base de Datos en Notion → 3 puntos (top right) → Connections → Add `n8n Soporte Bot`.

### Paso 2: Crear el Workflow en n8n (40 min)

1.  **Nuevo Workflow:** Click `+` → Name: `Clasificador Soporte → Notion`.
2.  **Nodo 1: Gmail Trigger (Disparador)**
    *   Search: `Gmail Trigger` → Add.
    *   **Credential:** New → OAuth2 → Sign in with Google → Allow n8n access.
    *   **Poll Times:** Every 5 minutes (o 15 min para ahorrar ops).
    *   **Label IDs:** Click `Load Options` → Busca `IA_Entrada_Soporte` → Selecciónalo.
    *   **Options:** `Simple: False` (para obtener body completo).
    *   *Test:* Envía un email de prueba a ti mismo con asunto "Prueba Soporte IA - No responder". Click `Execute Node` en el nodo. Verás output JSON.

3.  **Nodo 2: OpenAI / Anthropic / Google Gemini (El Cerebro)**
    *   Search: `OpenAI` (o `Anthropic`, `Google Gemini`) → Select **`Chat Model`** (no "Completion").
    *   **Credential:** New → API Key (pega tu key).
    *   **Model:** `gpt-4o-mini` (barato, rápido, bueno) / `claude-3-haiku-20240307` / `gemini-1.5-flash-latest`.
    *   **System Message (Prompt de Sistema):**
        ```markdown
        Eres un asistente de triage de soporte técnico para una SaaS B2B.
        Tu trabajo: Analizar emails entrantes y devolver SOLO un JSON válido con esta estructura exacta:
        {
          "categoria": "Bug | Facturación | Consulta General | Cancelación | Spam | Otro",
          "urgencia": "Alta | Media | Baja",
          "resumen": "Máximo 20 palabras describiendo el problema/solicitud.",
          "es_spam": true/false
        }
        Reglas:
        - "Bug": Errores, crashes, "no funciona", "sale error".
        - "Facturación": Cobros, facturas, planes, pagos, reembolsos.
        - "Cancelación": "Quiero dar de baja", "cancelar suscripción", "borrar cuenta".
        - "Spam": Ventas, ofertas, currículums, phishing, newsletters no solicitadas.
        - Urgencia Alta: Palabras "urgente", "crítico", "producción", "caído", "dinero", "factura vencida", tono muy enojado.
        - Urgencia Baja: Preguntas generales, "cómo hago", "duda", solicitudes de features, tono amable/neutro.
        - Resumen: Objetivo, sin saludos ni firmas.
        ```
    *   **User Message (Prompt Dinámico):** Click `Add Expression` (icono `{{ }}`) → Selecciona `JSON` → Pega:
        ```javascript
        // Accede al output del nodo Gmail (índice 0 usualmente)
        const email = $json[0]; // Ajusta si tu output es array directo
        return `Asunto: ${email.subject}
        De: ${email.from}
        Fecha: ${email.date}
        Cuerpo (Texto plano):
        ${email.text || email.html?.replace(/<[^>]*>/g, '').substring(0, 3000) || 'Sin cuerpo legible'}`;
        ```
        *(Nota: n8n Gmail trigger output estructura puede variar. Usa el panel "Output" del test paso 2 para ver la ruta exacta: ej. `{{ $json.subject }}`, `{{ $json.from.email }}`, `{{ $json.text }}`).*

    *   **Options:** `Response Format: JSON` (¡Clave para parsing fiable!).
    *   *Test:* Click `Execute Node`. Verifica output: `{{ $json.categoria }}`, etc. Si falla JSON, ajusta prompt "devuelve SOLO JSON".

4.  **Nodo 3: IF (Filtrar Spam - Opcional pero bueno)**
    *   Search: `IF` → Add.
    *   **Condition:** `{{ $json.es_spam }}` **Equal** `true`.
    *   **True Output:** (Conectar a "No Op" o "Slack: Log Spam" o simplemente no conectar a Notion → se pierde/ignora).
    *   **False Output:** Conectar a Siguiente Nodo (Notion).

5.  **Nodo 4: Notion - Create Page (Acción Final)**
    *   Search: `Notion` → Select **`Create Page`**.
    *   **Credential:** New → Access Token (pega `secret_...` de Paso 1).
    *   **Database ID:** Pega el ID de 32 chars de tu DB Notion.
    *   **Fields (Mapeo) - Click `Add Field` para cada uno:**
        *   `Asunto` (Title): `{{ $json[0].subject }}` (o ruta correcta del nodo Gmail).
        *   `Remitente` (Email): `{{ $json[0].from.email }}` (o `.from.value`).
        *   `Fecha Recibido` (Date): `{{ $json[0].date }}` (n8n suele parsear bien fechas ISO).
        *   `Categoría` (Select): `{{ $json.categoria }}` (¡Del nodo IA!).
        *   `Urgencia` (Select): `{{ $json.urgencia }}` (¡Del nodo IA!).
        *   `Resumen IA` (Text): `{{ $json.resumen }}` (¡Del nodo IA!).
        *   `Link Email` (URL): `https://mail.google.com/mail/u/0/#search/rfc822msgid%3A{{ $json[0].messageId }}` (Construye link directo al email en Gmail usando Message-ID).
        *   `Estado` (Select): `Nuevo` (Hardcodeado).
    *   *Test:* Click `Execute Node`. Ve a Notion → ¡Magia! Aparece la fila clasificada.

6.  **Nodo 5 (Bonus Pro): Gmail - Modify Labels (Marcar Procesado)**
    *   Search: `Gmail` → `Modify Labels`.
    *   **Credential:** Misma de Trigger.
    *   **Resource:** `Message` → `Operation`: `Modify Labels`.
    *   **Message ID:** `{{ $json[0].messageId }}` (Del nodo Trigger).
    *   **Add Labels:** `IA_Procesado` (Crea la label en Gmail antes).
    *   **Remove Labels:** `IA_Entrada_Soporte`.
    *   Conecta salida `True` del IF (o salida Notion) aquí. Así no se reprocesa.

### Paso 3: Activar y Probar en Vivo (15 min)

1.  **Save** workflow (Ctrl+S / Cmd+S).
2.  Click **`Test Workflow`** (Play button) → Ejecuta todo el camino con tu email de prueba.
3.  Revisa Notion. ¿Todo bien? ¿Categoría correcta? ¿Link abre email?
4.  **¡ACTIVAR!** Toggle switch `Active` (esquina superior derecha) → **ON**.
5.  **Prueba Real:** Envía 3 emails distintos a tu cuenta (simulando: Bug urgente, Pregunta factura, Spam venta). Espera hasta el próximo poll (5 min) o ejecuta manual.
6.  **Revisa Notion:** Deberías ver 3 filas. Spam no debería aparecer (gracias al IF). Las otras dos con categoría, urgencia, resumen y link funcional.

### Paso 4: Documenta tu Logro (5 min)
En tu Notion personal / Portafolio / LinkedIn:
*   Captura del Workflow n8n (vista general).
*   Captura de la DB Notion poblada.
*   Escribe: *"Automaticé triage de soporte con IA (n8n + GPT-4o-mini + Notion). Ahorro estimado 10h/semana. Costo: $0.002/email."*

---

## 5. 📚 Recursos Adicionales Curados

### Documentación Oficial & Tutoriales n8n
*   📖 **n8n Docs - Getting Started:** [docs.n8n.io](https://docs.n8n.io/) (Empieza por "Workflows" y "Nodes").
*   🎥 **Canal Oficial n8n (YouTube):** Workflows semanales, tutoriales nodos IA. Busca "n8n AI Agent", "n8n RAG".
*   🧩 **n8n Templates Library:** [n8n.io/workflows](https://n8n.io/workflows/) → Filtra por "AI", "Support", "Marketing", "Lead Gen". ¡No reinventes, adapta!

### IA + Automatización (Comunidad Hispana / Latam)
*   🇪🇸 **Comunidad n8n en Español (Discord/Telegram):** Busca "n8n Español" o "n8n Latam". Soporte rápido en tu idioma/huso.
*   🇲🇽 **Automatiza con IA (Newsletter/Blog):** Casos de uso reales en español.
*   🎓 **Curso Gratis n8n (YouTube - Canal "Automatización Inteligente" o similar):** Busca "Curso n8n desde cero 2024".

### Prompt Engineering para Automatización (Profundiza Módulo 2)
*   📄 **OpenAI Cookbook - Structured Outputs:** Cómo forzar JSON confiable (clave para n8n).
*   📄 **Anthropic - Prompt Engineering Interactive Tutorial:** Mejores prácticas para Claude (excelente razonamiento).
*   🛠️ **PromptFoo / Langfuse / LangSmith:** Tools para *evaluar* y *versionar* tus prompts de producción (nivel siguiente).

### Hosting n8n Self-Hosted (Producción Real, Bajo Costo)
*   ☁️ **Coolify (Panel open-source tipo Heroku):** Instala n8n, Postgres, Redis, Uptime Kuma en tu VPS con 1 click. **Muy recomendado para emprendedores.** [coolify.io](https://coolify.io/)
*   🐳 **Docker Compose Manual:** La forma "hardcore" pero estándar. Docs n8n → "Self-hosting".
*   💰 **Proveedores VPS Latam-friendly:** Hetzner (EU, mejor precio/rendimiento), DigitalOcean, Vultr, Linode (Akamai), Contabo. ~$5-8/mes (2-4GB RAM). **Evita shared hosting.**

### Plantillas Listas para Usar (Importar en n8n: Workflows → Import)
*   Busca en [n8n.io/workflows](https://n8n.io/workflows/) por:
    *   "Email Triage AI Notion"
    *   "Lead Qualification Scoring CRM"
    *   "Content Repurposing Social Media"
    *   "RAG Chatbot with n8n + Pinecone/Qdrant + Notion/Google Docs"

---

## 6. ❓ Preguntas de Autoevaluación

**Instrucciones:** Responde sin consultar el material. Luego verifica con la clave al final.

### Pregunta 1: Arquitectura de Flujo
> Estás diseñando una automatización que: (1) Detecta un nuevo lead en Typeform, (2) Usa IA para investigar la empresa en LinkedIn/Google y calificarla, (3) Si es "Hot", crea deal en CRM y alerta a Slack; si "Cold", guarda en Sheet.
>
> **¿Cuál de las siguientes afirmaciones describe MEJOR la función del nodo `IF` / `Switch` en este flujo?**
>
> A) Es el "cerebro" que entiende el lenguaje natural del lead.
> B) Es el "disparador" que inicia la automatización al recibir el webhook.
> C) Es el "router" que dirige el flujo por caminos distintos según la salida de la IA (Hot vs Cold).
> D) Es la "acción final" que escribe la base de datos en Notion.

### Pregunta 2: Prompt Engineering en Automatización (Structured Output)
> En el ejercicio práctico, usamos `Response Format: JSON` en el nodo OpenAI y un prompt de sistema estricto.
>
> **¿Por qué es CRÍTICO forzar salida JSON válido (vs texto libre) cuando la salida alimenta nodos posteriores (ej. Notion Create Page)?**
>
> A) Porque los modelos de IA solo entienden JSON, no lenguaje natural.
> B) Porque n8n requiere que los datos mapeados a campos (Select, Date, URL) tengan tipos de datos predecibles y parseables programáticamente; el texto libre rompe el mapeo.
> C) Porque JSON es más barato en tokens que el texto explicativo.
> D) Porque Notion no acepta texto plano, solo objetos JSON.

### Pregunta 3: Decisión Estratégica de Herramienta (n8n vs Zapier/Make)
> Tu startup SaaS en crecimiento (Chile/México/Colombia) procesa datos sensibles de usuarios (salud/finanzas) y espera escalar a 50k automatizaciones/mes. El CTO sugiere n8n self-hosted; el CEO prefiere Zapier por "facilidad".
>
> **¿Cuál es el argumento TÉCNICO-ECONÓMICO más fuerte a favor de n8n self-hosted en este escenario específico?**
>
> A) n8n tiene más integraciones nativas que Zapier.
> B) El costo marginal por automatización en n8n self-hosted tiende a $0 (pagas servidor fijo), mientras Zapier/Make cobran por operación/tarea, volviéndose prohibitivo a alto volumen y tipo de cambio Latam.
> C) n8n no requiere conocimientos de Docker ni servidores.
> D) Zapier no permite usar modelos de IA como GPT-4o.

---

### ✅ Clave de Autoevaluación
1.  **C** (El `IF`/`Switch` enruta la lógica de negocio basada en datos).
2.  **B** (Parsing determinista = automatización robusta. Texto libre = fragilidad).
3.  **B** (Escalabilidad económica + Soberanía de datos = Diferenciador clave n8n).

---

## 🚀 Próximo Paso: Módulo 4
**"Agentes de IA: De la automatización a la autonomía"**
Construiremos sobre este flujo: ¿Qué pasa si el agente *decide* qué herramienta usar (Buscar web, Consultar CRM, Escribir código, Enviar email) en un loop hasta resolver la tarea? Introducción a **n8n AI Agent / LangChain nodes**, *Function Calling*, *RAG* y memoria.

---

*¿Dudas en el ejercicio? Comparte tu workflow (Export → JSON) en la comunidad del curso o Discord n8n Latam. ¡Depurar en comunidad es la forma más rápida de aprender!* 💪