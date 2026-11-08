# Nemotron 3 Ultra 550B — startup_content/curso_emprendimiento_modulo

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 62.616s | tokens_per_second: 88.0
- input_tokens: 250 | output_tokens: 5508
- judge_score: 5.0 | justificación: 

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

---

## 1. Objetivo del Módulo

Al finalizar este módulo, serás capaz de **identificar procesos repetitivos en tu startup**, **diseñar flujos de trabajo lógicos** y **construir automatizaciones funcionales sin escribir código** utilizando herramientas visuales (no-code) como **n8n**, integrando modelos de IA (OpenAI, Anthropic, Gemini) para resolver tareas reales de atención al cliente, marketing y ventas, pasando de "tengo una idea" a "tengo un flujo corriendo en producción" en menos de una hora.

---

## 2. Contenido Teórico: Automatización con IA para No-Técnicos

### 2.1 ¿Qué es realmente una "Automatización con IA"?

No es magia. Es una **receta lógica** que conecta tres piezas:
1.  **Disparador (Trigger):** "Cuando pase X..." (Ej: Llega un email, se llena un formulario, es lunes 9:00 AM).
2.  **Procesamiento con IA (Action):** "...pídele a la IA que haga Y con ese dato..." (Ej: Resume, clasifica, redacta, decide, extrae datos).
3.  **Acción Final (Output):** "...y envía el resultado a Z." (Ej: Responde el email, crea tarea en Notion, actualiza CRM, publica en LinkedIn).

> **Regla de oro:** Si lo haces más de 2 veces por semana y sigue un patrón, **automatízalo**.

### 2.2 ¿Por qué n8n? (Nuestra herramienta principal del curso)

| Característica | Ventaja para Emprendedores |
| :--- | :--- |
| **Visual (Nodos y Conexiones)** | Ves el flujo completo como un mapa mental. No hay "caja negra". |
| **Self-hosted / Cloud** | Empiezas gratis en la nube (n8n.cloud) o en tu servidor (control total de datos). |
| **Nodos de IA Nativos** | Tiene nodos listos para: *Agentes, Cadenas, Embeddings, Extracción de info, Clasificación*. |
| **400+ Integraciones** | Conecta Gmail, WhatsApp (vía Twilio/Meta), HubSpot, Airtable, Notion, Google Sheets, Slack, Typeform, Webhooks... |
| **Costo Predecible** | No pagas por "ejecución" (como Zapier/Make), pagas por hosting o plan fijo. Ideal para escalar. |

### 2.3 Conceptos Clave que Dominarás Hoy

1.  **Credenciales (Credentials):** Llaves seguras (API Keys, OAuth) que n8n guarda encriptadas para conectar con OpenAI, Google, etc.
2.  **Expresiones (`{{ $json.campo }}`):** La "pegamento" para pasar datos del Nodo A al Nodo B. *Ej: El asunto del email que llegó es `{{ $json.subject }}`*.
3.  **Prompt Engineering en Nodos:** No escribes prompts sueltos; los incrustas en nodos **`Basic LLM Chain`** o **`Information Extractor`** con variables dinámicas.
4.  **Manejo de Errores (Error Workflow):** Qué pasa si la IA alucina o la API falla (reintentos, notificación a Slack, fallback humano).

---

## 3. Tres Ejemplos Prácticos para Startups (Casos Reales)

### Caso 1: Atención al Cliente Automatizada (Clasificación + Respuesta Borrador)
**El Dolor:** Recibes 20+ emails/día en `soporte@tustartup.com`. Pierdes 1h clasificando y respondiendo FAQs.
**El Flujo (n8n):**
1.  **Trigger:** `Gmail Trigger` (New Email in Label "Por Procesar").
2.  **Nodo IA:** `Information Extractor` (Modelo: GPT-4o-mini).
    *   *Prompt:* "Clasifica este email en: [Bug, Facturación, Feature Request, Spam, Urgente]. Extrae: Nombre cliente, Resumen 1 frase, Acción sugerida (Responder/Escalar/Ignorar). Devuelve JSON."
3.  **Nodo Lógico:** `IF` (Si "Urgente" O "Bug" -> Slack al canal #alertas-equipo).
4.  **Nodo IA:** `Basic LLM Chain` (Solo si Categoría != Spam).
    *   *Prompt:* "Redacta respuesta profesional en español usando nuestra Base de Conocimiento (adjunta como contexto RAG). Tono: Empático, resolutivo. Firma: Equipo [TuStartup]."
5.  **Acción:** `Gmail` -> **Create Draft** (Borrador en Gmail listo para que tú revises y envíes).
6.  **Limpieza:** `Gmail` -> Modify Labels (Quita "Por Procesar", pone "Procesado por IA").

> **Resultado:** Cero emails en bandeja de entrada sin leer. Tú solo apruebas borradores. Tiempo: 10 min/día vs 1h.

---

### Caso 2: Generación de Contenido para Redes Sociales (Content Repurposing)
**El Dolor:** Escribes un blog/post largo. Adaptarlo a LinkedIn, Twitter/X, Instagram, Newsletter te lleva 2 horas.
**El Flujo (n8n):**
1.  **Trigger:** `Manual Trigger` (Tú pegas la URL del blog o el texto crudo en un formulario n8n).
2.  **Nodo Previo:** `HTTP Request` / `Read Binary File` (Obtiene el texto limpio de la URL/PDF).
3.  **Nodo IA (Paralelo - Split In Batches):** `Basic LLM Chain` (4 ramas simultáneas, una por plataforma).
    *   *Rama LinkedIn:* Prompt: "Convierte en post LinkedIn: Gancho fuerte, 3 bullets con valor, CTA comentario. Formato: Texto + 3 Hashtags. Max 1300 chars."
    *   *Rama Twitter/X:* Prompt: "Hilo de 5 tweets. Tweet 1: Gancho. Tweets 2-4: Valor denso. Tweet 5: CTA a newsletter. Emojis estratégicos."
    *   *Rama Instagram:* Prompt: "Caption visual: Gancho, historia corta, 3 tips numerados, CTA 'Link en bio'. 15 Hashtags nicho."
    *   *Rama Newsletter:* Prompt: "Asunto irresistible + Preheader. Estructura: Gancho personal -> Lección clave -> Acción práctica -> P.D."
4.  **Nodo Agregador:** `Merge` / `Set` (Junta los 4 resultados en un solo JSON).
5.  **Acción:** `Google Sheets` / `Notion` / `Airtable` (Guarda en tu "Calendario de Contenido" con columnas: Plataforma, Copy, Estado "Por Revisar", Fecha Programada).
6.  **Notificación:** `Slack` / `Email` -> "Tus 4 adaptaciones están listas para revisar en Notion 🚀".

> **Resultado:** De 1 input -> 4 outputs listos para revisar en 2 min. Tú eres Editor, no Redactor desde cero.

---

### Caso 3: Calificación Automática de Leads (Lead Scoring + Enriquecimiento)
**El Dolor:** Llegan 50 leads/semana por Typeform/Webflow. El equipo de ventas llama a todos. 80% no califican. Tiempo perdido.
**El Flujo (n8n):**
1.  **Trigger:** `Webhook` (Recibe datos del formulario: Email, Empresa, Cargo, Tamaño empresa, Reto actual).
2.  **Nodo Enriquecimiento:** `Clearbit` / `Apollo` / `Hunter.io` (Busca: Ingresos estimados, Tech stack, LinkedIn CEO, Ubicación).
3.  **Nodo IA:** `Information Extractor` (Modelo: GPT-4o).
    *   *Input:* Datos Formulario + Datos Enriquecidos.
    *   *Prompt:* "Actúa como SDR Senior. Evalúa fit con nuestro ICP: [Define tu ICP aquí: Ej. SaaS B2B, 50-500 empleados, Latam, usan HubSpot]. Output JSON: `score` (0-100), `tier` (Hot/Warm/Cold), `reasoning` (por qué), `talking_points` (3 bullets para la llamada), `red_flags`."
4.  **Nodo Lógico:** `Switch` (Basado en `tier`):
    *   **Hot (Score > 80):** `HubSpot`/`Pipedrive` Create Deal (Stage: "Nuevo Hot") + Asigna Owner (Round Robin) + `Slack` @Ventas "🔥 Lead HOT: [Empresa] - [Cargo] - Score: 92".
    *   **Warm (50-80):** `HubSpot` Create Contact (Lead Status: "Nurture") + Añade a Secuencia Email "Educacional" (n8n -> Gmail/ActiveCampaign).
    *   **Cold (<50):** `HubSpot` Create Contact (Lead Status: "Unqualified") + Tag "Revisar en 6 meses".
5.  **Dashboard:** `Google Sheets` Append Row (Log histórico para análisis de conversión por canal).

> **Resultado:** Ventas llama solo a "Hot". Marketing nutre "Warm". Tú ves métricas reales en Sheets. CRO (Conversion Rate Optimization) basado en datos, no corazonadas.

---

## 4. Ejercicio Práctico Paso a Paso: "Clasificador Inteligente de Emails de Ventas"

**Objetivo:** Construir en **n8n Cloud (gratis)** un flujo que lea emails entrantes a una cuenta de prueba, use IA para detectar si es una **Oportunidad de Venta**, **Soporte**, **Spam** u **Otro**, y guarde el resultado en una **Google Sheet** compartida con tu equipo.

**Tiempo estimado:** 30-45 minutos.
**Requisitos previos:** Cuenta n8n Cloud (n8n.cloud), Cuenta Google, API Key de OpenAI (créditos $5 USD bastan).

---

### Paso 1: Preparación del Entorno (5 min)

1.  **Crea una Hoja de Cálculo en Google Sheets:**
    *   Nombre: `Leads_IA_Clasificados`.
    *   Columnas (Fila 1): `Fecha` | `Remitente` | `Asunto` | `Cuerpo_Truncado` | `Categoria_IA` | `Confianza` | `Resumen_IA` | `Link_Email`.
    *   Comparte: **Cualquiera con el enlace -> Editor** (copia el ID de la URL: `docs.google.com/spreadsheets/d/**ID_AQUI**/edit`).
2.  **Consigue tu OpenAI API Key:**
    *   `platform.openai.com/api-keys` -> Create New Secret Key. Guárdala segura.
3.  **Accede a n8n Cloud:** Inicia sesión o crea cuenta trial (14 días gratis).

---

### Paso 2: Crear Credenciales en n8n (3 min)

1.  Menú lateral -> **Credentials** -> **New Credential**.
2.  Busca **OpenAI** -> Pega tu API Key -> Save.
3.  **New Credential** -> Busca **Google Sheets** -> **OAuth2** -> Connect Account -> Elige tu cuenta Google -> Allow. Save.
4.  **New Credential** -> Busca **Gmail** (o IMAP/Outlook) -> OAuth2 -> Connect. Save.

---

### Paso 3: Construir el Flujo (Nodo a Nodo) (25 min)

#### 🟢 Nodo 1: Trigger - Gmail Trigger
*   **Añade nodo:** `Gmail Trigger` (Busca "Gmail" en panel derecho, arrastra "Gmail Trigger").
*   **Credential:** Selecciona tu credencial Gmail.
*   **Event:** `On New Email`.
*   **Poll Time:** `Every 5 Minutes` (para testing) / `Every Hour` (producción).
*   **Filters:**
    *   `Label IDs`: `INBOX` (o crea label "IA-Entrada" y úsala).
    *   `Max Results`: `5` (para no gastar créditos testing).
*   **Options:** `Download Attachments`: `False`.
*   **Ejecuta nodo (Play):** Debe traer 1 email de prueba. Verifica output: `subject`, `from`, `text` (cuerpo plano), `id` (messageId).

#### 🟡 Nodo 2: Preprocesamiento - Set (Limpieza)
*   **Añade nodo:** `Set` (Utilities).
*   **Mode:** `Manual` (Keep Only Set).
*   **Campos a crear:**
    *   `asunto`: `{{ $json.subject }}`
    *   `remitente`: `{{ $json.from.email }}` (expresión: click en `from` -> `email`)
    *   `cuerpo_limpio`: `{{ $json.text.substring(0, 3000) }}` *(Corta a 3000 chars para ahorrar tokens)*.
    *   `message_id`: `{{ $json.id }}`
    *   `link_email`: `https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}`
*   **Conecta:** Gmail Trigger -> Set.

#### 🟣 Nodo 3: IA - Information Extractor (El Cerebro)
*   **Añade nodo:** `Information Extractor` (En sección **AI** / **LangChain**).
*   **Credential:** OpenAI.
*   **Model:** `gpt-4o-mini` (Barato, rápido, inteligente).
*   **Schema (Definición de Salida JSON):** Copia y pega **exactamente** esto en el editor JSON del nodo (botón `</>` JSON Schema):

```json
{
  "type": "object",
  "properties": {
    "categoria": {
      "type": "string",
      "enum": ["Oportunidad_Venta", "Soporte_Tecnico", "Spam_Promocional", "Otro"],
      "description": "Clasificación única y exclusiva del email."
    },
    "confianza": {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "description": "Qué tan seguro estás (0-100)."
    },
    "resumen_ejecutivo": {
      "type": "string",
      "description": "Resumen en 1 frase accionable para el equipo de ventas/soporte."
    },
    "datos_clave": {
      "type": "object",
      "properties": {
        "empresa_mencionada": { "type": "string" },
        "presupuesto_mencionado": { "type": "string" },
        "urgencia": { "type": "string", "enum": ["Alta", "Media", "Baja", "No Aplica"] }
      }
    }
  },
  "required": ["categoria", "confianza", "resumen_ejecutivo", "datos_clave"]
}
```

*   **Text Input (El Prompt):** En el campo `Text` (o conecta `Set` -> `Information Extractor` y usa expresión):
    *   `Asunto: {{ $json.asunto }}\nRemitente: {{ $json.remitente }}\nCuerpo: {{ $json.cuerpo_limpio }}`
*   **System Prompt (Opcional pero recomendado):** Click `Options` -> `System Message`:
    > "Eres un analista de ventas B2B experto. Clasifica emails entrantes para un equipo comercial. Sé estricto: 'Oportunidad_Venta' SOLO si hay intención clara de compra, presupuesto o solicitud de demo/precios. 'Soporte_Tecnico' si ya es cliente reportando fallo. 'Spam_Promocional' si es cold sales hacia NOSOTROS. 'Otro' para todo lo demás."

#### 🔵 Nodo 4: Acción - Google Sheets (Append Row)
*   **Añade nodo:** `Google Sheets` -> **Append** (no Update).
*   **Credential:** Tu Google Sheets OAuth.
*   **Document ID:** Pega el **ID** de tu Sheet (el string largo de la URL).
*   **Sheet Name:** `Hoja 1` (o el nombre de tu pestaña).
*   **Columns:** `User Entered` (deja que n8n lea cabeceras).
*   **Mapping (Campos):** Click `Map Automatically` o manual:
    *   `Fecha`: `{{ $now.format('YYYY-MM-DD HH:mm') }}`
    *   `Remitente`: `{{ $json.remitente }}`
    *   `Asunto`: `{{ $json.asunto }}`
    *   `Cuerpo_Truncado`: `{{ $json.cuerpo_limpio }}`
    *   `Categoria_IA`: `{{ $json.categoria }}` *(Viene del Nodo 3)*
    *   `Confianza`: `{{ $json.confianza }}`
    *   `Resumen_IA`: `{{ $json.resumen_ejecutivo }}`
    *   `Link_Email`: `{{ $json.link_email }}`
*   **Conecta:** Information Extractor -> Google Sheets.

#### 🟠 Nodo 5 (Bonus Pro): Notificación Slack si es "Hot"
*   **Añade nodo:** `IF` (Logic).
*   **Condition:** `categoria` **Equal** `Oportunidad_Venta` **AND** `confianza` **Greater Than** `75`.
*   **True Branch:** `Slack` -> `Post Message` -> Canal `#ventas-alertas` -> Text: `🔥 *Nueva Oportunidad HOT*\n*De:* {{ $json.remitente }}\n*Asunto:* {{ $json.asunto }}\n*Resumen:* {{ $json.resumen_ejecutivo }}\n*Empresa:* {{ $json.datos_clave.empresa_mencionada }}\n<{{ $json.link_email }}|Abrir en Gmail>`.
*   **Conecta:** Information Extractor -> IF -> Slack (True).

---

### Paso 4: Probar y Activar (5 min)

1.  **Save Workflow** (Botón superior derecho). Nombre: `Clasificador Emails Ventas v1`.
2.  **Test Manual:** Click **`Execute Workflow`** (botón Play grande).
    *   Si no hay emails nuevos, ve a Gmail, envíate un email de prueba simulando un lead: *"Hola, soy Juan de EmpresaX, queremos contratar 50 licencias para la semana que viene, pasen presupuesto"*.
    *   Vuelve a n8n -> Execute Workflow.
3.  **Verifica:**
    *   Nodo **Set**: ¿Trae datos limpios?
    *   Nodo **Information Extractor**: ¿Output JSON válido? ¿Categoría `Oportunidad_Venta`? ¿Confianza > 80?
    *   Nodo **Google Sheets**: ¿Fila nueva en tu Sheet?
    *   Nodo **Slack** (si activaste): ¿Llegó notificación?
4.  **Activar:** Toggle **`Active`** (esquina superior derecha) -> **ON**.
    *   *Ahora corre solo cada 5 min en la nube.*

---

### Paso 5: Iterar (Tu Tarea Post-Curso)

*   **Mejora el Prompt:** Añade ejemplos (Few-shot) en el System Message si falla casos borde.
*   **Añade RAG:** Conecta un nodo `Vector Store` (Pinecone/Supabase/Postgres) con tu PDF de "Precios y FAQ" para que la IA responda con *tus* datos reales.
*   **Escala:** Cambia Trigger a `Webhook` y conecta tu formulario Webflow/Typeform directamente (más rápido que email).

---

## 5. Recursos Adicionales Curados

### 🛠️ Herramientas y Plantillas
| Recurso | Link | Uso |
| :--- | :--- | :--- |
| **n8n Templates Oficiales** | [n8n.io/workflows](https://n8n.io/workflows) | 1000+ flujos listos para importar (Busca "Lead", "Content", "Support"). |
| **Plantilla Este Ejercicio** | *[Link de importación JSON que el profe proveerá en clase]* | Importa en n8n: Workflows -> Import -> Pega JSON. |
| **OpenAI Playground** | [platform.openai.com/playground](https://platform.openai.com/playground) | Prueba prompts y schemas JSON *antes* de meterlos en n8n. |
| **Google Sheets API Limits** | [developers.google.com/sheets/api/limits](https://developers.google.com/sheets/api/limits) | 500 req/100 seg/user. Suficiente para empezar. |

### 📚 Aprendizaje Profundo
*   **Curso Gratis n8n (Español):** Canal YouTube **"Automatiza con n8n"** (Busca: "n8n en español", "IA n8n", "Agentes n8n").
*   **Documentación Nodos IA n8n:** [docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain/) (La biblia técnica).
*   **Prompt Engineering para Estructuras:** Guía "Structured Outputs" de OpenAI (clave para `Information Extractor`).

### 💡 Inspiración de Casos de Uso Latam
*   **Newsletter "Automatización LATAM"** (Substack) - Casos reales de founders de México, Colombia, Argentina.
*   **Comunidad No-Code Latam:** Discord/Slack groups (Busca "NoCode Latam", "Makerpad Latam").

---

## 6. Autoevaluación: ¿Estás Listo para Automatizar?

Responde **Verdadero (V)** o **Falso (F)**. Al final, verifica con la clave.

1.  **( V / F )** En n8n, el nodo **`Information Extractor`** es ideal cuando necesitas que la IA devuelva un **JSON estructurado y validado** (ej: score numérico, categoría de lista fija) para usar en nodos posteriores como `IF` o `Google Sheets`.
2.  **( V / F )** Para conectar n8n con Gmail y Google Sheets de forma segura sin manejar contraseñas, debo crear credenciales de tipo **OAuth2** dentro de n8n y autorizar el acceso desde mi cuenta de Google.
3.  **( V / F )** La expresión `{{ $json.cuerpo_limpio.substring(0, 3000) }}` en un nodo `Set` sirve para **enviar solo los primeros 3000 caracteres del email a la IA**, reduciendo costos de tokens y evitando errores de límite de contexto.

---

### 🔑 Clave de Respuestas
1.  **V** -> Es su propósito principal: *Structured Output Parsing* nativo.
2.  **V** -> OAuth2 es el estándar seguro; n8n gestiona el token refresh automáticamente.
3.  **V** -> Control de costos y latencia esencial. `substring` es JavaScript puro dentro de expresiones n8n.

---

> **"No automatices para hacer más, automatiza para hacer lo que solo tú puedes hacer: Estrategia, Producto, Ventas de Alto Nivel."**
> — *Tu Instructor, Módulo 3*