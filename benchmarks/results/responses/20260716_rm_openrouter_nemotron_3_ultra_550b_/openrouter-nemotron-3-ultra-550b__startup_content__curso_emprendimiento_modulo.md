# Nemotron 3 Ultra 550B — startup_content/curso_emprendimiento_modulo

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 62.577s | tokens_per_second: 102.0
- input_tokens: 250 | output_tokens: 6381
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una guía completa y práctica para emprendedores sobre la automatización con IA.

## Respuesta completa

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

---

## 1. Objetivo del Módulo

Al finalizar este módulo, serás capaz de **identificar procesos repetitivos en tu startup**, **diseñar flujos de trabajo lógicos** y **construir tu primera automatización funcional sin escribir código** utilizando herramientas visuales (no-code) como n8n, integrando modelos de IA para resolver problemas reales de atención al cliente, marketing y ventas, pasando de "tengo una idea" a "tengo un sistema que trabaja mientras yo duermo".

---

## 2. Contenido Teórico: Automatización + IA = Tu nuevo socio 24/7

### 2.1 ¿Qué es la Automatización con IA? (Más allá de Zapier/Make)
La automatización tradicional (RPA) sigue reglas estáticas: *"Si pasa A, haz B"*.
La **Automatización con IA (Agentic Workflows)** introduce **razonamiento**: *"Analiza el contexto de A, decide la mejor acción entre B, C o D, y ejecútala"*.

**La ecuación del valor:**
> **Disparador (Trigger) + Contexto/Datos + Modelo de IA (Cerebro) + Acción (Manos) = Flujo Autónomo**

### 2.2 Conceptos Clave para No-Técnicos
| Concepto | Analogía | Ejemplo en n8n |
| :--- | :--- | :--- |
| **Nodo (Node)** | Un ladrillo / Un paso en tu receta | "Nodo HTTP Request", "Nodo OpenAI", "Nodo Gmail" |
| **Flujo (Workflow)** | La receta completa | "Procesar Lead Entrante" |
| **Disparador (Trigger)** | El timbre de la puerta | "Webhook: Nuevo formulario Typeform" |
| **Expresión / Variable** | Los ingredientes que pasan de un paso a otro | `{{ $json.email }}` (El email que vino del formulario) |
| **Agente de IA** | Un pasante súper listo al que le das instrucciones | Nodo "AI Agent" con herramienta "Buscar en Google" y "Enviar Email" |

### 2.3 La Herramienta Estrella: **n8n** (pronunciado "n-eight-n")
¿Por qué n8n para emprendedores latinos?
1.  **Self-hosted (Opcional):** Puedes correrlo en tu servidor (VPS ~$5-10 USD/mes) → **Costo fijo, ejecuciones ilimitadas**. Ideal para escalar sin que la factura explote.
2.  **Visual y Potente:** Interfaz de "arrastrar y soltar" pero permite código (JavaScript/Python) si luego necesitas algo complejo.
3.  **Nodos de IA Nativos:** Tiene nodos listos para *OpenAI, Anthropic, Google Gemini, Ollama (local), Pinecone, Qdrant, Supabase (Vector Store)*.
4.  **Comunidad y Plantillas:** Cientos de flujos listos para importar (JSON).

> **Alternativas si no quieres servidor propio:** Make (ex Integromat) - más visual, modelo por operaciones; Zapier - más caro, menos flexible para IA compleja; Dify / Flowise - enfocados 100% en apps de chat/RAG, menos en automatización de procesos de negocio.

### 2.4 Arquitectura Mental para Diseñar Flujos (Framework **D-D-E-A**)
Antes de abrir n8n, responde en papel:
1.  **D**isparador: ¿Qué inicia el proceso? (Email, Formulario, Hora, Webhook, Nuevo row en BD).
2.  **D**atos: ¿Qué info necesito *antes* de llamar a la IA? (Historial cliente, catálogo productos, prompt del sistema).
3.  **E**strategia (Prompt/Logic): ¿Qué le pido a la IA? (Clasificar, Responder, Extraer, Decidir, Generar). *Tip: Usa "Structured Output" (JSON) para que la IA devuelva datos limpios para el siguiente nodo.*
4.  **A**cción: ¿Qué pasa con la respuesta? (Enviar email, Crear ticket en Notion/Linear, Actualizar CRM, Postear en LinkedIn, Notificar a Slack/Telegram).

---

## 3. Ejemplos Prácticos para Startups (Casos Reales)

### Ejemplo 1: Atención al Cliente Automatizada (Nivel 1: Clasificar y Responder FAQ)
**Dolor:** Recibes 20 emails/día en `soporte@tustartup.com`. El 60% son "¿Cómo descargo la factura?", "¿Cuál es mi plan?", "Error 404".
**Flujo n8n:**
1.  **Trigger:** *IMAP Email* (Cada 5 min revisa bandeja "No leídos").
2.  **Nodo Function (Pre-procesar):** Extrae `from`, `subject`, `text`. Marca como leído.
3.  **Nodo AI Agent (Clasificador):**
    *   *System Prompt:* "Eres un clasificador. Devuelve SOLO JSON: `{ "categoria": "facturacion|tecnico|ventas|otro", "urgencia": "alta|media|baja", "respuesta_sugerida": "texto o null" }`. Usa la base de conocimiento adjunta (Vector Store) para responder FAQs."
    *   *Tools:* **Vector Store (RAG)** con tus PDFs de FAQ / Notion / Web.
4.  **IF Node (Lógica):**
    *   *Si* `categoria == "faq" AND confianza > 0.9` → **Nodo Gmail: Enviar respuesta automática** (Plantilla HTML bonita).
    *   *Sino* → **Nodo Slack/Telegram: Notificar a humano** ("🚨 Ticket requiere atención: [Asunto] - [Link a Gmail]") + **Nodo Google Sheets/Notion: Crear Ticket**.
**Resultado:** Resuelves el 60% instantáneo, tu equipo humano enfocado en lo complejo.

---

### Ejemplo 2: Generación de Contenido para Redes Sociales (Content Repurposing)
**Dolor:** Escribes un blog/post largo. Adaptarlo a LinkedIn, Twitter (X), Instagram, Threads, Newsletter te toma 2 horas.
**Flujo n8n:**
1.  **Trigger:** *Manual Trigger* (Botón "Ejecutar ahora") o *Webhook* (Desde botón en Notion/Airtable).
2.  **Input:** Pegas la **URL del artículo** o el **Texto completo**.
3.  **Nodo HTTP Request / Jina AI Reader:** Extrae texto limpio de la URL.
4.  **Nodo AI Agent (Content Repurposer):**
    *   *System Prompt:* "Eres un Social Media Manager experto en LatAm. Convierte el texto input en 5 formatos. Devuelve JSON estricto."
    *   *Output Schema (Structured Output):*
        ```json
        {
          "linkedin": "Post profesional, storytelling, 3 hashtags, call to action comentario.",
          "twitter_thread": "Array de 5-7 tweets, hooks fuertes, numerados.",
          "instagram_caption": "Visual, emojis, 10 hashtags nicho, CTA link en bio.",
          "newsletter_intro": "Gancho personal, 3 bullets clave, link 'Leer más'.",
          "tiktok_script": "Gancho 3s, desarrollo, CTA final, sugerencias visuales."
        }
        ```
5.  **Nodo Google Docs / Notion:** Crea documento "Contenido Semana X - [Tema]" con tabs para cada red.
6.  **Nodo Slack/Email:** Te envía: "✅ Contenido listo para revisar: [Link Notion]".
**Resultado:** De 2 horas a 15 min de revisión/edición. Consistencia de voz de marca garantizada por *System Prompt*.

---

### Ejemplo 3: Calificación Automática de Leads (Lead Scoring & Enrichment)
**Dolor:** Llegan 50 leads/semana por Typeform/Webflow. El equipo de ventas llama a todos, pierden tiempo en "curiosos" o estudiantes.
**Flujo n8n:**
1.  **Trigger:** *Webhook* (Recibe JSON del formulario: `email`, `empresa`, `rol`, `mensaje`).
2.  **Nodo HTTP Request (Enriquecimiento - Opcional pero potente):** Llama a **Apollo.io / Clearbit / Hunter.io / LinkedIn API** con el `email` → Obtiene: `tamaño_empresa`, `industria`, `tecnologias`, `seniority_real`.
3.  **Nodo AI Agent (Lead Scorer):**
    *   *Input:* Datos formulario + Datos enriquecidos.
    *   *System Prompt:* "Eres un SDR Senior. Puntúa 0-100. Criterios: ICP (Ideal Customer Profile) = Empresas 50-500 emp, SaaS/Fintech, Rol Decision Maker (CTO/CEO/VP). Penaliza: Gmail/Outlook personal, Estudiantes, Competencia. Devuelve JSON: `{ "score": 85, "tier": "Hot|Warm|Cold", "razones": ["Usa HubSpot", "CTO", "200 empleados"], "accion_recomendada": "Llamar en < 24h | Enviar caso de estudio | Meter en nurture" }`"
4.  **Switch Node (Router):**
    *   **Score > 80 (Hot):** → **Nodo HubSpot/Pipedrive: Crear Deal + Asignar Owner + Tarea "Llamar HOY"** → **Nodo Slack: @Ventas 🔥 LEAD CALIENTE: [Nombre] - [Empresa] - Score: 90**.
    *   **Score 50-80 (Warm):** → **Nodo HubSpot: Crear Contacto + Lista "Nurture Sequencia"** → **Nodo Email: Enviar "Guía Gratis X"**.
    *   **Score < 50 (Cold):** → **Nodo Google Sheets: Log "Leads Fríos [Fecha]"** (Para revisión mensual).
**Resultado:** Ventas habla *solo* con quienes compran. Marketing nutre al resto automáticamente.

---

## 4. Ejercicio Práctico Paso a Paso: "Clasificador de Emails de Ventas"

> **Objetivo:** Crear un flujo que lea un email nuevo, use IA para decidir si es una **Oportunidad de Venta**, **Soporte** o **Spam/Noise**, y te avise por Telegram/Slack solo de las oportunidades.
> **Tiempo estimado:** 45-60 min.
> **Prerrequisitos:** Cuenta n8n (Cloud trial 14 días gratis o Self-hosted), Cuenta OpenAI (API Key con $5 crédito), Cuenta Telegram (BotFather) o Slack (App).

---

### Paso 1: Preparar las Credenciales (5 min)
1.  **OpenAI:** Ve a `platform.openai.com/api-keys` → *Create new secret key* → Copia `sk-...`. En n8n: *Credentials* → *New Credential* → **OpenAI API** → Pega key.
2.  **Telegram (Recomendado por simplicidad):**
    *   Abre Telegram → Busca `@BotFather` → `/newbot` → Nombre: `MiClasificadorBot` → User: `mi_clasificador_bot`.
    *   Copia el **Token** (ej: `123456:ABC-DEF...`).
    *   En n8n: *Credentials* → *New Credential* → **Telegram API** → Pega Token.
    *   **Obtener tu Chat ID:** Escribele a tu bot `/start`. Ve a `https://api.telegram.org/bot< TU_TOKEN >/getUpdates`. Busca `"chat":{"id": 123456789 }`. **Ese número es tu Chat ID**. Guárdalo.
3.  **Email (IMAP):** Usa tu email real (Gmail/Outlook).
    *   Gmail: Habilita IMAP en Settings. Crea *App Password* (Security → 2FA → App Passwords → "Mail" → "Other" → n8n).
    *   En n8n: *Credentials* → *IMAP Email* → User: `tu@gmail.com`, Pass: *App Password*, Host: `imap.gmail.com`, Port: `993`, SSL: On.

---

### Paso 2: Crear el Workflow Base (10 min)
1.  En n8n: **New Workflow** → Nombre: `Clasificador Ventas v1`.
2.  Arrastra nodo **IMAP Email** (Trigger).
    *   *Credential:* Tu IMAP.
    *   *Folder:* `INBOX` (o crea label "IA-Test" y filtra ahí para no tocar tu inbox real).
    *   *Options:* `Mark as Read` = True, `Download Attachments` = False, `Simple` = False (queremos el body HTML/Text).
    *   *Poll Times:* Every 5 Minutes (para test, pon "Every Minute" y luego lo subes).
3.  Click **Execute Node** (Testea que traiga un email real). Verás output: `subject`, `from`, `text`, `html`.

---

### Paso 3: El Cerebro - Nodo AI Agent (15 min)
1.  Arrastra **AI Agent** (en categoría *AI* → *LangChain* → *Agent* → *AI Agent*... o busca "AI Agent" en el panel derecho).
    *   *Nota: En n8n v1.0+ el nodo se llama "Agent". Usa el modelo "OpenAI Chat Model" dentro.*
2.  Conecta **IMAP Email** → **AI Agent**.
3.  Configura **AI Agent**:
    *   **Model:** *OpenAI Chat Model* (Cred: Tu OpenAI) → Model: `gpt-4o-mini` (Barato, rápido, inteligente).
    *   **System Prompt:** (Copia y pega esto **exacto**):
        ```markdown
        Eres un clasificador experto de emails B2B para una startup SaaS B2B.
        Analiza el asunto y cuerpo del email. Devuelve **SOLO un JSON válido** con esta estructura exacta:
        {
          "categoria": "venta | soporte | spam | otro",
          "confianza": 0.95,
          "resumen_una_linea": "CEO de Empresa X (200 emp) pide demo para 50 usuarios",
          "accion": "notificar_ventas | crear_ticket_soporte | ignorar"
        }

        REGLAS:
        - "venta": Intención clara de compra, demo, precios, escalar, decisor (CEO, CTO, VP, Head). Palabras: "demo", "precios", "contrato", "piloto", "presupuesto", "escalar".
        - "soporte": Usuario actual reporta bug, duda técnica, facturación, acceso.
        - "spam": Frío masivo, SEO, agencias ofreciendo servicios, newsletters, phishing.
        - "otro": No encaja arriba (ej: RRHH, proveedores, personal).
        - "confianza": 0.0 a 1.0. Si dudas, baja confianza y pon "otro".
        ```
    *   **Prompt Type:** `Define` (o *System Message* según versión).
    *   **Input Data (User Message):** Haz clic en *Add Expression* (icono `{{x}}`) al lado de *Prompt* / *User Message* → Arrastra `Subject` y `Text` del nodo IMAP.
        *   *Expresión final:* `Asunto: {{ $json.subject }}\n\nCuerpo: {{ $json.text }}`

4.  **Output Parser (CRUCIAL):** En el nodo AI Agent, busca *Output Parser* → Selecciona **Structured Output Parser**.
    *   Click en el parser → *Define Schema* → Pega este JSON Schema:
        ```json
        {
          "type": "object",
          "properties": {
            "categoria": { "type": "string", "enum": ["venta", "soporte", "spam", "otro"] },
            "confianza": { "type": "number", "minimum": 0, "maximum": 1 },
            "resumen_una_linea": { "type": "string" },
            "accion": { "type": "string", "enum": ["notificar_ventas", "crear_ticket_soporte", "ignorar"] }
          },
          "required": ["categoria", "confianza", "resumen_una_linea", "accion"]
        }
        ```
    *   *Esto fuerza a la IA a devolver JSON limpio, sin alucinaciones de texto extra.*

5.  **Test:** Click *Execute Node* en AI Agent. Verifica output: `{{ $json.categoria }}`, `{{ $json.resumen_una_linea }}`, etc.

---

### Paso 4: Lógica de Decisión (IF / Switch) (5 min)
1.  Arrastra nodo **IF** (Logic).
2.  Conecta **AI Agent** → **IF**.
3.  Condición 1 (Venta Caliente):
    *   *Value 1:* `{{ $json.categoria }}` (arrastra de AI Agent)
    *   *Operation:* **Equal**
    *   *Value 2:* `venta`
    *   *AND* → *Add Condition*:
        *   *Value 1:* `{{ $json.confianza }}`
        *   *Operation:* **Greater Than or Equal**
        *   *Value 2:* `0.85`
    *   *Output:* **True** (Sale por arriba) → Renombra salida a "🔥 VENTA".
4.  Condición 2 (Soporte):
    *   Click *Add Else If* (o segundo IF conectado a False del primero).
    *   `categoria` **Equal** `soporte` AND `confianza` **>=** `0.8`.
    *   *Output True:* Renombra "🛠 SOPORTE".
5.  *False* (Todo lo demás: Spam, Otro, Baja confianza) → Renombra "🗑 IGNORAR/REVISAR".

---

### Paso 5: Acciones - Notificar por Telegram (10 min)
**Rama "🔥 VENTA" (True del primer IF):**
1.  Arrastra **Telegram** → *Send Message*.
    *   *Credential:* Tu Telegram.
    *   *Chat ID:* Tu Chat ID (el número que sacaste en Paso 1).
    *   *Text:* (Modo Expression `{{x}}`):
        ```
        🔥 **NUEVA OPORTUNIDAD DE VENTA** 🔥
        
        📧 **De:** {{ $node["IMAP Email"].json["from"] }}
        📝 **Asunto:** {{ $node["IMAP Email"].json["subject"] }}
        
        🤖 **Análisis IA:**
        {{ $node["AI Agent"].json["resumen_una_linea"] }}
        
        🎯 **Confianza:** {{ $node["AI Agent"].json["confianza"] * 100 }}%
        
        👉 **Acción:** Responder en < 1 hora.
        ```
    *   *Options:* `Parse Mode` = **Markdown**.

**Rama "🛠 SOPORTE" (True del segundo IF):**
1.  Otro nodo **Telegram Send Message** (o mismo con expresión condicional, pero mejor separado para claridad).
    *   *Text:*
        ```
        🛠 **TICKET SOPORTE**
        📧 {{ $node["IMAP Email"].json["from"] }}
        📝 {{ $node["IMAP Email"].json["subject"] }}
        🤖 {{ $node["AI Agent"].json["resumen_una_linea"] }}
        ```

**Rama "🗑 IGNORAR" (False final):**
1.  (Opcional) Nodo **No Operation, Do Nothing** o log en Google Sheets para auditoría semanal.

---

### Paso 6: Prueba End-to-End (5 min)
1.  **Activa el Workflow** (Toggle *Active* arriba a la derecha).
2.  Envía un email **de prueba** a tu cuenta (desde otro email tuyo) con asunto: *"Interesado en demo para mi equipo de 50 personas, soy CTO"*.
3.  Espera 1 min (o ejecuta manual *Execute Workflow*).
4.  **Revisa Telegram:** ¡Debe llegar el mensaje formateado con 🔥!
5.  Prueba uno de soporte: *"No puedo entrar a mi cuenta, error 500"*.
6.  Prueba spam: *"Compre listas de emails baratas"*.
7.  **Revisa la pestaña "Executions" (Execuciones)** en n8n si algo falla (Click en execution fallida → ver error en nodo rojo).

---

### Paso 7: Iteración y Mejora (Tarea para casa)
*   **Mejora 1:** Añade nodo **Google Sheets / Notion** en rama VENTA para loggear lead automáticamente.
*   **Mejora 2:** En rama SOPORTE, crea ticket en **Linear / Jira / Trello / Notion** via HTTP Request.
*   **Mejora 3:** Añade **Enriquecimiento** (Apollo/Clearbit) antes del AI Agent usando el email del remitente para que la IA sepa tamaño de empresa/rol real.
*   **Mejora 4:** Cambia Trigger a **Webhook** y conecta tu formulario Webflow/Typeform → Mismo cerebro, entrada distinta.

---

## 5. Recursos Adicionales

### 🎓 Aprendizaje Estructurado (Gratis / Español)
*   **n8n Official Docs (ES):** `docs.n8n.io` (Busca "LangChain", "AI Agent", "Structured Output").
*   **Canal YouTube: "n8n Ninja" / "Automatiza con n8n" (Comunidad Hispana):** Tutoriales paso a paso muy visuales.
*   **Curso Gratis n8n + IA (English but clear):** *Learn n8n* en YouTube (canal oficial n8n) → Playlist "AI Starter Kit".
*   **Plantillas Lista para Importar (JSON):** `n8n.io/workflows` → Filtra tag "AI", "LangChain", "Sales", "Support". *Descarga JSON → En n8n: Workflows → Import.*

### 🛠 Herramientas Complementarias (Stack Recomendado)
| Necesidad | Herramienta | Plan Inicio | Uso en Flujo |
| :--- | :--- | :--- | :--- |
| **Hosting n8n (Self-hosted)** | **Coolify** (en VPS Hetzner/DigitalOcean/Contabo) | ~$5-10/mes | Control total, 0 límites ops. |
| **Vector Store (RAG)** | **Supabase (pgvector)** / **Qdrant Cloud** | Free Tier generoso | Base conocimiento para FAQ / Docs. |
| **Enriquecimiento Leads** | **Apollo.io** / **Clay.com** / **FullEnrich** | Free / Pay per use | API en n8n para saber empresa/tamaño/tech stack. |
| **Scraping Web Limpio** | **Jina AI Reader** (`r.jina.ai/http://...`) | Gratis | Input barato para "Resume esta URL". |
| **Observabilidad** | **Langfuse** / **Helicone** | Free Tier | Ver prompts, costos, latencia, evaluar calidad. |

### 💡 Prompts Base para tu Biblioteca (Copia/Pega/Adapta)
*   *Clasificador Universal:* (El usado en el ejercicio).
*   *Extractos Estructurados:* "Extrae: Nombre, Email, Empresa, Dolor Principal, Presupuesto, Timeline. JSON only."
*   *Redactor Respuestas Empáticas:* "Responde como Customer Success Senior. Tono: cercano, proactivo, solución. Máx 3 párrafos. Firma: 'Equipo [Startup]'."

---

## 6. Preguntas de Autoevaluación

**1. (Conceptual) Diferencia clave:** ¿Cuál es la diferencia fundamental entre un flujo de automatización tradicional (ej. Zapier básico) y un flujo **"Agentic"** usando un nodo *AI Agent* con *Structured Output* en n8n?
> A) El Agentic usa más nodos HTTP Request.
> B) El Agentic permite que la IA **razone, tome decisiones condicionales y devuelva datos tipados (JSON)** para ramificar la lógica del flujo, en lugar de solo ejecutar pasos lineales predefinidos.
> C) El Agentic solo funciona con modelos locales (Ollama).
> D) No hay diferencia, es solo marketing.

**2. (Práctica - Debugging):** Tu flujo de "Clasificador de Emails" se ejecuta sin errores en n8n (todo verde), pero **no llega el mensaje a Telegram**. El nodo Telegram muestra "Success" en la ejecución. ¿Cuáles son las **3 causas más probables** en orden de prioridad?
> 1. ___________________________________________________________
> 2. ___________________________________________________________
> 3. ___________________________________________________________

**3. (Diseño Estratégico):** Vas a automatizar la **calificación de leads entrantes por webhook (Typeform)**. Tienes presupuesto limitado para APIs de enriquecimiento (Apollo, Clearbit). Diseña la **lógica de decisión (pseudocódigo o diagrama mental)** para maximizar el valor: ¿Cuándo vale la pena gastar un crédito de enriquecimiento ANTES de llamar a la IA, y cuándo la IA puede calificar bien solo con los datos del formulario?
> *Escribe tu lógica en 3-5 pasos claros.*

---

### 🎯 **Checklist de Salida del Módulo**
- [ ] Tengo n8n corriendo (Cloud o VPS).
- [ ] Conecté OpenAI y Telegram/Slack correctamente.
- [ ] Ejecuté el **Ejercicio Práctico** y recibí notificación en mi celular.
- [ ] Entiendo qué es *Structured Output Parser* y por qué es crítico.
- [ ] Identifiqué **2 procesos** en mi startup para automatizar esta semana.
- [ ] Importé al menos 1 plantilla de `n8n.io/workflows` y la modifiqué.

---

> **"La automatización no es para reemplazar humanos, es para liberar a los humanos de ser robots. Tu siguiente paso: Elige un flujo manual que hagas esta semana y conviértelo en tu segundo workflow en n8n."**