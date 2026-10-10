# Claude Fable 5.1 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.67 | quality: 10.0
- latency_total: 190.6s | tokens_per_second: 73.9
- input_tokens: 390 | output_tokens: 14076
- judge_score: 5 | justificación: La respuesta es precisa, relevante y ofrece una profundidad adecuada al abordar la automatización con IA, con ejemplos claros y aplicables para emprendedores, manteniendo una estructura clara y organizada.

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

# Módulo 3: Automatización con IA – De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 3 horas (1.5 h teoría y ejemplos + 1.5 h ejercicio práctico)
**Nivel:** Emprendedor no técnico
**Requisitos previos:** Haber completado el Módulo 1 (Fundamentos de IA generativa) y el Módulo 2 (Prompting efectivo para negocios)

---

## 1. Objetivo del módulo

Al finalizar este módulo, serás capaz de identificar tareas repetitivas en tu emprendimiento que pueden automatizarse, diseñar un flujo de trabajo que combine herramientas de automatización (como n8n) con modelos de IA, y construir tu primera automatización funcional sin escribir código. Más que aprender una herramienta, el objetivo es que desarrolles la **mentalidad de automatizador**: la capacidad de mirar tu operación diaria y preguntarte "¿esto lo tiene que hacer una persona, o puede hacerlo un flujo?". Terminarás el módulo con un flujo real funcionando en tu negocio y con un mapa de las próximas tres automatizaciones que te ahorrarían más tiempo.

---

## 2. Contenido teórico

### 2.1 ¿Qué es la automatización con IA?

Piensa en la rutina de Mariana, dueña de una tienda de accesorios en Guadalajara que vende por Instagram y WhatsApp. Cada mañana:

1. Revisa los mensajes de WhatsApp acumulados de la noche.
2. Responde preguntas repetidas ("¿tienen envío a Monterrey?", "¿cuánto cuesta el collar dorado?").
3. Anota en un Excel quién pidió qué.
4. Publica una historia en Instagram.
5. Le avisa a su proveedor si algo se agotó.

Eso le toma dos horas diarias. **Diez horas a la semana** en las que no vende, no diseña ni descansa.

La **automatización** consiste en conectar herramientas para que, cuando ocurra algo (llega un mensaje, se llena un formulario, es lunes a las 9 a.m.), el sistema ejecute una serie de acciones **sin intervención humana**.

La **automatización con IA** da un paso más: en lugar de solo mover datos de un lugar a otro, el flujo puede **entender, decidir y generar**. Puede leer un mensaje y detectar si el cliente está molesto, redactar una respuesta personalizada, resumir una conversación o clasificar un lead como "caliente" o "frío".

> **Idea clave:** La automatización tradicional sigue reglas fijas ("si el correo contiene la palabra *factura*, muévelo a esta carpeta"). La automatización con IA interpreta contexto ("si el correo *parece ser* una solicitud de factura, aunque no use esa palabra, responde con el formulario de datos fiscales").

### 2.2 Automatización tradicional vs. automatización con IA

| Aspecto | Automatización tradicional | Automatización con IA |
|---|---|---|
| Lógica | Reglas exactas (si X, entonces Y) | Interpretación de contexto |
| Entradas | Datos estructurados (números, casillas) | Texto libre, audio, imágenes |
| Ejemplo | Enviar correo cuando alguien compra | Leer la reseña del cliente, detectar el tono y redactar una respuesta adecuada |
| Riesgo | Se rompe si el dato no es exacto | Puede "alucinar" o equivocarse; requiere supervisión |
| Costo | Muy bajo | Bajo (centavos por ejecución), pero no cero |

La mayoría de los flujos útiles para una startup **combinan ambas**: reglas para lo predecible, IA para lo que requiere interpretación.

### 2.3 Los cuatro bloques de cualquier flujo de trabajo

Todas las automatizaciones, sin importar la herramienta, se construyen con estos bloques:

1. **Disparador (trigger):** el evento que inicia el flujo.
   *Ejemplos:* llega un correo, alguien llena un formulario, se agrega una fila en Google Sheets, son las 8 a.m. de lunes.

2. **Acciones:** lo que el flujo hace.
   *Ejemplos:* enviar un WhatsApp, crear una fila, publicar en redes, consultar una base de datos.

3. **Lógica / condiciones:** las bifurcaciones del camino.
   *Ejemplos:* "si el monto es mayor a $5,000, avisa al dueño; si no, responde automáticamente".

4. **Inteligencia (nodo de IA):** el paso donde un modelo (como GPT, Claude o Gemini) lee, clasifica, resume o genera texto.

Visualmente, un flujo se ve así:

```
[Disparador] → [Acción] → [IA interpreta] → [Condición] → [Acción A]
                                                        └→ [Acción B]
```

### 2.4 Herramientas disponibles: el panorama

Existen varias plataformas "sin código" (no-code) para construir flujos. Las tres más relevantes para un emprendedor en Latinoamérica:

| Herramienta | Fortaleza | Debilidad | Costo aproximado |
|---|---|---|---|
| **Zapier** | La más fácil de empezar, miles de integraciones | Cara al escalar; lógica limitada | Desde USD $20/mes; sube rápido |
| **Make (ex Integromat)** | Buen balance precio/potencia, interfaz visual clara | Curva de aprendizaje media | Desde USD $9/mes |
| **n8n** | Gratis si lo alojas tú mismo; nodos de IA muy potentes; sin límite de pasos | Requiere un poco más de paciencia inicial | Gratis (auto-alojado) o desde USD $20/mes en la nube |

En este curso trabajaremos principalmente con **n8n** porque:

- Tiene integraciones nativas con OpenAI, Anthropic, Google Gemini y modelos de código abierto.
- Permite construir **agentes de IA** (flujos que deciden qué hacer según el contexto), no solo cadenas lineales.
- Su versión en la nube tiene prueba gratuita suficiente para este módulo, y la versión auto-alojada no tiene costo de licencia, ideal para presupuestos de startup.
- La comunidad hispanohablante es activa y hay cientos de plantillas listas para copiar.

> Lo que aprendas aquí es **transferible**: disparadores, acciones y condiciones funcionan igual en Zapier o Make. Solo cambia el botón.

### 2.5 Cómo funciona n8n (sin tecnicismos)

n8n es un lienzo en blanco donde arrastras **nodos** (cajas) y los conectas con flechas. Cada nodo hace una cosa:

- **Nodos de disparador:** "Cuando llegue un mensaje de Telegram…", "Cuando se envíe este formulario…", "Cada día a las 9 a.m.…"
- **Nodos de aplicación:** Gmail, Google Sheets, WhatsApp Business, Instagram, HubSpot, Notion, Airtable, Shopify, Mercado Libre (vía HTTP), etc.
- **Nodos de IA:** OpenAI, Anthropic, Gemini, "AI Agent", "Text Classifier", "Summarize".
- **Nodos de lógica:** IF (si/entonces), Switch (varias opciones), Filter, Merge, Wait.

Cuando conectas dos nodos, la **salida** del primero se vuelve la **entrada** del segundo. Si el nodo 1 lee un correo, el nodo 2 (IA) recibe el texto de ese correo y puede trabajar con él.

Dos conceptos que te facilitarán la vida:

- **Credenciales:** la primera vez que uses Gmail, Sheets u OpenAI, n8n te pedirá "conectar la cuenta". Lo haces una sola vez y queda guardado.
- **Ejecución de prueba:** cada nodo tiene un botón "Test step" que lo ejecuta solo y te muestra qué datos salieron. Úsalo constantemente; es la forma de depurar sin frustrarte.

### 2.6 ¿Qué vale la pena automatizar? La matriz de decisión

No todo debe automatizarse. Usa esta matriz antes de construir cualquier flujo:

| | **Alta frecuencia** | **Baja frecuencia** |
|---|---|---|
| **Baja complejidad / bajo riesgo** | ✅ **Automatiza primero** (respuestas frecuentes, registro de datos, recordatorios) | 🤷 Quizá no vale el esfuerzo |
| **Alta complejidad / alto riesgo** | ⚠️ Automatiza **con supervisión humana** (IA propone, tú apruebas) | ❌ Hazlo manual |

Regla práctica: si una tarea te toma **más de 15 minutos a la semana** y la haces **siempre igual**, es candidata.

### 2.7 Buenas prácticas desde el día uno

1. **Empieza con "humano en el bucle".** Que la IA redacte el borrador y tú apruebes antes de enviar. Quita la aprobación cuando confíes en los resultados.
2. **Registra todo en una hoja de cálculo.** Cada ejecución debería dejar rastro: qué entró, qué decidió la IA, qué salió. Esto te permite auditar y mejorar.
3. **Escribe prompts como instrucciones de trabajo.** Lo que viste en el Módulo 2 aplica aquí: rol, contexto, formato de salida, ejemplos.
4. **Pide salidas en formato estructurado.** Si la IA debe clasificar, pídele que responda solo con una palabra de una lista ("CALIENTE / TIBIO / FRÍO") o en JSON. Eso evita que el siguiente nodo se rompa.
5. **Cuida los datos personales.** Si procesas datos de clientes con un modelo externo, revisa las políticas de privacidad y cumple la ley de tu país (LFPDPPP en México, Ley 1581 en Colombia, LGPD en Brasil, Ley 25.326 en Argentina).
6. **Pon límites de costo.** Configura alertas en tu cuenta de OpenAI/Anthropic. Un flujo mal configurado que entra en bucle puede gastar tu presupuesto en minutos.

---

## 3. Ejemplos prácticos de automatización para startups

Cada ejemplo sigue el mismo esquema: el problema, el flujo, las herramientas, el prompt central y lo que puedes esperar.

---

### Ejemplo 1: Atención al cliente automatizada por WhatsApp

**Contexto:** *Nutriplan*, una startup de Bogotá que vende planes de comida saludable por suscripción. Reciben 80–120 mensajes diarios por WhatsApp. El 70 % son las mismas 12 preguntas (zonas de entrega, precios, cambios de menú, alergias). Dos personas dedican medio día a esto.

**Objetivo:** responder automáticamente las preguntas frecuentes en segundos, con tono humano, y escalar a una persona solo los casos que lo requieren.

**El flujo:**

```
[Disparador: nuevo mensaje en WhatsApp Business API]
        ↓
[IA – Clasificador: ¿es pregunta frecuente, pedido, queja u otro?]
        ↓
[Switch: según la categoría]
   ├─ Pregunta frecuente → [IA – Agente con base de conocimiento] → [Responder por WhatsApp]
   ├─ Pedido → [Crear fila en Google Sheets] → [Responder con link de pago]
   ├─ Queja → [Notificar al equipo en Slack/Telegram con resumen] → [Responder: "Una persona te atenderá en breve"]
   └─ Otro → [Notificar al equipo]
        ↓
[Registrar conversación en Google Sheets]
```

**Herramientas:**
- WhatsApp Business API (vía Meta directamente o un proveedor como Twilio, 360dialog o Wati)
- n8n (nodo WhatsApp Trigger, nodo AI Agent, nodo Switch, nodo Google Sheets, nodo Telegram/Slack)
- OpenAI GPT-4o-mini o Claude Haiku (modelos rápidos y baratos, ideales para chat)
- Un documento de Google Docs con las preguntas frecuentes, que se carga como "base de conocimiento" del agente

**Prompt del agente (resumido):**

> Eres el asistente de Nutriplan, un servicio de comida saludable en Bogotá. Responde de forma cálida, breve y en español colombiano neutro. Usa únicamente la información de la base de conocimiento que te proporciono. Si no sabes la respuesta o el cliente pide algo fuera de tu alcance (cambios de facturación, reclamos, cancelaciones), responde exactamente: "Déjame conectarte con alguien del equipo que te puede ayudar mejor" y nada más. Nunca inventes precios ni zonas de entrega.

**Resultados típicos:**
- Tiempo de primera respuesta: de 40 minutos promedio a menos de 10 segundos.
- 65–75 % de los mensajes resueltos sin intervención humana.
- El equipo pasa de responder preguntas a atender solo casos complejos y ventas.

**Costo mensual estimado:** USD $20 (n8n cloud) + USD $5–15 en llamadas a la API de IA + el costo del proveedor de WhatsApp (varía; muchos tienen planes desde USD $0 con pago por conversación).

**Advertencia:** empieza en modo "borrador": que la IA proponga la respuesta y una persona la apruebe con un botón durante la primera semana. Así detectas errores antes de que los vea el cliente.

---

### Ejemplo 2: Generación de contenido para redes sociales

**Contexto:** *Taller Raíz*, una marca de muebles artesanales de Oaxaca con una sola persona encargada de marketing. Saben que deben publicar 4–5 veces por semana en Instagram y LinkedIn, pero rara vez pasan de dos. La barrera no es la creatividad, sino el tiempo de sentarse a redactar.

**Objetivo:** generar cada lunes una propuesta de contenido semanal (textos, hashtags e ideas visuales) a partir de la información del negocio, que la persona de marketing solo revise y ajuste.

**El flujo:**

```
[Disparador: cada lunes 7:00 a.m.]
        ↓
[Leer Google Sheets: "Temas de la semana" (productos nuevos, promociones, fechas especiales)]
        ↓
[Leer Google Docs: "Voz de marca" (tono, palabras que usamos, palabras prohibidas)]
        ↓
[IA – Generar 5 posts: cada uno con copy para Instagram, versión adaptada para LinkedIn,
 3 hashtags y descripción de la imagen sugerida]
        ↓
[Escribir resultados en Notion o Google Sheets, columna "Pendiente de aprobación"]
        ↓
[Enviar correo/Telegram: "Tu contenido de la semana está listo para revisar"]
        ↓
[Opcional: cuando una fila cambia a "Aprobado" → programar en Buffer/Metricool]
```

**Herramientas:**
- n8n (nodo Schedule Trigger, Google Sheets, Google Docs, OpenAI/Anthropic, Notion, Gmail)
- Claude Sonnet o GPT-4o (modelos con mejor redacción para contenido)
- Metricool o Buffer para programar publicaciones (ambos tienen planes gratuitos)
- Opcional: nodo de generación de imágenes (DALL·E, Flux) para bocetos visuales

**Prompt central (resumido):**

> Eres el community manager de Taller Raíz, muebles artesanales hechos a mano en Oaxaca. Nuestra voz es cercana, orgullosa de lo artesanal, sin ser cursi ni usar superlativos vacíos. Nunca usamos las palabras "increíble", "único" ni emojis de fuego. A partir de estos temas de la semana: {{temas}}, genera 5 publicaciones. Para cada una entrega: (1) copy para Instagram de máximo 120 palabras con una llamada a la acción, (2) versión para LinkedIn con enfoque en el proceso y las personas detrás del producto, (3) tres hashtags relevantes en español, (4) descripción de la foto o video que acompañaría. Responde en formato JSON con esta estructura: [...]

**Resultados típicos:**
- De 2 publicaciones semanales a 5, con 30–40 minutos de revisión en lugar de 4 horas de redacción.
- Consistencia de voz: al definir las reglas una vez, la IA las respeta mejor que un equipo rotativo.

**Costo mensual estimado:** USD $20 (n8n) + USD $2–5 de IA (son pocas ejecuciones, pero largas).

**Lección importante:** el valor no está en que la IA "escriba por ti", sino en que **nunca empieces de una hoja en blanco**. Editar es diez veces más rápido que crear.

---

### Ejemplo 3: Calificación automática de leads

**Contexto:** *Contalia*, una startup de software contable para pymes en Lima. Reciben 150–200 registros al mes desde su formulario web y anuncios de Facebook. El equipo comercial (dos personas) tarda 2–3 días en contactar a cada lead, y para entonces el 40 % ya no responde. Además, dedican tiempo igual a un freelancer curioso que a una empresa con 50 empleados lista para comprar.

**Objetivo:** que cada lead sea evaluado en el momento en que llega, reciba una respuesta inmediata y personalizada, y el equipo comercial se enfoque primero en los más valiosos.

**El flujo:**

```
[Disparador: nuevo envío en formulario web (Typeform / Tally / Webflow / Facebook Lead Ads)]
        ↓
[Enriquecer (opcional): buscar la empresa del lead vía su dominio de correo]
        ↓
[IA – Calificar: analiza nombre, empresa, cargo, tamaño, mensaje libre →
 devuelve puntaje 0–100, categoría (CALIENTE/TIBIO/FRÍO) y justificación de una línea]
        ↓
[IF: ¿puntaje ≥ 70?]
   ├─ SÍ (caliente) → [Crear contacto en HubSpot/Pipedrive con etiqueta "prioridad"]
   │                  → [Notificar a vendedor por WhatsApp con resumen]
   │                  → [IA redacta correo personalizado] → [Enviar desde Gmail]
   └─ NO → [IF: ¿puntaje ≥ 40?]
             ├─ TIBIO → [Crear en CRM] → [Secuencia de correos educativos]
             └─ FRÍO → [Crear en CRM, etiqueta "nurturing"] → [Correo genérico de bienvenida]
        ↓
[Registrar en Google Sheets: lead, puntaje, categoría, justificación, acción tomada]
```

**Herramientas:**
- Formulario: Tally (gratis) o Typeform
- n8n (nodo Webhook/Form Trigger, OpenAI, IF, HubSpot/Pipedrive, Gmail, WhatsApp, Google Sheets)
- GPT-4o-mini o Claude Haiku para clasificar (barato y rápido)
- CRM: HubSpot (plan gratuito) o Pipedrive

**Prompt de calificación (resumido):**

> Eres el analista comercial de Contalia, software contable para pymes peruanas de 5 a 200 empleados. Nuestro cliente ideal: empresas de servicios o comercio, con contador interno o externo, que hoy usan Excel o un sistema desactualizado. Evalúa este lead:
> - Nombre: {{nombre}}
> - Empresa: {{empresa}}
> - Cargo: {{cargo}}
> - Número de empleados: {{empleados}}
> - Mensaje: {{mensaje}}
>
> Responde únicamente en este formato JSON, sin texto adicional:
> {"puntaje": número de 0 a 100, "categoria": "CALIENTE" | "TIBIO" | "FRIO", "justificacion": "una oración", "siguiente_paso": "una acción concreta para el vendedor"}
>
> Criterios: +30 si el cargo es gerente, dueño, CFO o contador. +25 si tiene entre 10 y 200 empleados. +20 si el mensaje menciona un dolor concreto (errores, multas, tiempo perdido, SUNAT). −30 si es estudiante, freelancer o pide "información general" sin contexto.

**Resultados típicos:**
- Tiempo de primer contacto: de 2–3 días a menos de 5 minutos para leads calientes.
- El equipo comercial dedica el 80 % de su tiempo al 20 % de leads con mayor probabilidad de compra.
- La hoja de registro se convierte en datos para ajustar los criterios cada mes.

**Costo mensual estimado:** USD $20 (n8n) + USD $1–3 de IA (200 clasificaciones cortas cuestan centavos).

**Advertencia ética:** la IA puede heredar sesgos. Revisa periódicamente que no esté descartando leads por razones irrelevantes (nombre, género, ubicación). Mantén siempre la "justificación" visible para auditar.

---

## 4. Ejercicio práctico paso a paso

### "Mi primer flujo con IA: clasificador de mensajes de contacto"

Vas a construir una versión simplificada del Ejemplo 3, aplicada a **tu propio negocio**. Al terminar tendrás un formulario público que, al ser llenado, clasifica el mensaje con IA, lo registra en una hoja de cálculo y te avisa por correo con un resumen y una respuesta sugerida.

**Tiempo estimado:** 60–90 minutos
**Costo:** USD $0 (usaremos pruebas gratuitas)

#### Lo que necesitas antes de empezar

- [ ] Una cuenta de Google (Gmail + Google Sheets)
- [ ] Una cuenta de n8n Cloud (prueba gratuita de 14 días en [n8n.io](https://n8n.io))
- [ ] Una clave API de OpenAI ([platform.openai.com](https://platform.openai.com)) con al menos USD $5 de crédito. *Alternativa:* clave de Anthropic o Google Gemini (Gemini tiene nivel gratuito).
- [ ] 10 minutos para escribir: ¿cuáles son las 3–4 categorías de mensajes que recibe tu negocio? (Ejemplo: cotización, soporte, alianza, otro)

---

#### Paso 1: Prepara tu hoja de registro (5 min)

1. Crea una hoja nueva en Google Sheets llamada **"Leads clasificados"**.
2. En la fila 1 escribe estos encabezados, uno por columna:
   `Fecha | Nombre | Correo | Mensaje | Categoría | Urgencia | Resumen | Respuesta sugerida`
3. Guarda. No la cierres, la necesitarás.

#### Paso 2: Crea tu flujo en n8n y el disparador (10 min)

1. Entra a n8n Cloud y haz clic en **"Create workflow"**. Nómbralo "Clasificador de contactos".
2. Haz clic en el **+** del centro y busca **"n8n Form Trigger"**. Selecciónalo.
3. Configura el formulario:
   - **Form Title:** "Contáctanos – [nombre de tu negocio]"
   - **Form Description:** "Cuéntanos en qué podemos ayudarte"
   - Agrega tres campos (botón *Add Form Element*):
     - `Nombre` – tipo Text – requerido
     - `Correo` – tipo Email – requerido
     - `Mensaje` – tipo Textarea – requerido
4. Haz clic en **"Test step"**. Se abrirá una URL del formulario. Ábrela, llénala con un mensaje de prueba realista (por ejemplo: "Hola, necesito cotizar 50 unidades para entregar antes de fin de mes") y envíala.
5. Vuelve a n8n: deberías ver los datos del formulario en el panel derecho. ✅ Tu disparador funciona.

#### Paso 3: Conecta la IA (15 min)

1. Haz clic en el **+** a la derecha del nodo del formulario y busca **"OpenAI"** (o "Anthropic" / "Google Gemini").
2. Elige la acción **"Message a Model"**.
3. En **Credential**, haz clic en *Create new* y pega tu clave API. Guarda.
4. En **Model**, elige `gpt-4o-mini` (rápido y económico).
5. En **Prompt / Message**, pega el siguiente texto y **adáptalo a tu negocio** donde veas corchetes:

```
Eres el asistente de [NOMBRE DE TU NEGOCIO], que se dedica a [QUÉ HACES EN UNA LÍNEA].

Analiza el siguiente mensaje de contacto:
Nombre: {{ $json.Nombre }}
Correo: {{ $json.Correo }}
Mensaje: {{ $json.Mensaje }}

Clasifícalo en UNA de estas categorías: [COTIZACIÓN / SOPORTE / ALIANZA / OTRO]
(ajusta estas categorías a tu negocio).

Asigna una urgencia: ALTA (menciona fechas cercanas, problemas activos o montos grandes),
MEDIA o BAJA.

Responde ÚNICAMENTE con un JSON válido, sin explicaciones ni texto adicional,
con exactamente esta estructura:
{
  "categoria": "...",
  "urgencia": "...",
  "resumen": "una oración que resuma qué necesita la persona",
  "respuesta_sugerida": "un correo breve y amable de respuesta, en español, máximo 80 palabras, firmado por el equipo de [NOMBRE DE TU NEGOCIO]"
}
```

   > 💡 Las expresiones `{{ $json.Nombre }}` toman el dato del nodo anterior. En n8n también puedes arrastrar el campo desde el panel izquierdo al cuadro de texto y se escribe solo.

6. Activa la opción **"Output Content as JSON"** (o "Simplify Output" según versión) si está disponible. Esto hace que n8n convierta la respuesta en campos separados.
7. Haz clic en **"Test step"**. Deberías ver en la salida algo como:
   ```
   categoria: COTIZACIÓN
   urgencia: ALTA
   resumen: El cliente necesita cotizar 50 unidades con entrega antes de fin de mes.
   respuesta_sugerida: Hola [Nombre], gracias por escribirnos...
   ```
   Si ves el JSON como un solo bloque de texto, agrega después un nodo **"Edit Fields (Set)"** o busca la opción de "parse JSON". No te preocupes: en los recursos hay un video que muestra esto.

#### Paso 4: Registra todo en Google Sheets (10 min)

1. Agrega un nodo **"Google Sheets"** → acción **"Append Row"**.
2. Conecta tu cuenta de Google cuando lo pida (se abre una ventana de autorización).
3. Selecciona el documento **"Leads clasificados"** y la hoja (normalmente "Hoja 1").
4. En **Mapping**, elige *Map each column manually* y asigna:
   - `Fecha` → `{{ $now.format('yyyy-MM-dd HH:mm') }}`
   - `Nombre` → arrastra el campo Nombre del nodo del formulario
   - `Correo` → arrastra Correo
   - `Mensaje` → arrastra Mensaje
   - `Categoría` → arrastra `categoria` del nodo de IA
   - `Urgencia` → arrastra `urgencia`
   - `Resumen` → arrastra `resumen`
   - `Respuesta sugerida` → arrastra `respuesta_sugerida`
5. **"Test step"**. Ve a tu Google Sheet: debería haber aparecido una fila nueva. ✅

#### Paso 5: Recibe la alerta por correo (10 min)

1. Agrega un nodo **"Gmail"** → acción **"Send"**.
2. Conecta tu cuenta.
3. Configura:
   - **To:** tu propio correo
   - **Subject:** `[{{ $('OpenAI').item.json.urgencia }}] Nuevo contacto: {{ $('OpenAI').item.json.categoria }}`
   - **Message:**
     ```
     Nuevo mensaje de {{ $('n8n Form Trigger').item.json.Nombre }} ({{ $('n8n Form Trigger').item.json.Correo }})

     Categoría: {{ $('OpenAI').item.json.categoria }}
     Urgencia: {{ $('OpenAI').item.json.urgencia }}

     Resumen: {{ $('OpenAI').item.json.resumen }}

     --- Respuesta sugerida (revísala antes de enviar) ---
     {{ $('OpenAI').item.json.respuesta_sugerida }}
     ```
   > El nombre dentro de `$('...')` debe coincidir exactamente con el nombre que tenga tu nodo. Si renombraste el nodo de IA, ajústalo.
4. **"Test step"**. Revisa tu bandeja de entrada. ✅

#### Paso 6: Agrega una condición de urgencia (10 min) — *reto opcional*

Haz que los mensajes de urgencia ALTA también te lleguen por Telegram o WhatsApp:

1. Entre el nodo de IA y el de Gmail, inserta un nodo **"IF"**.
2. Condición: `{{ $json.urgencia }}` **is equal to** `ALTA`.
3. En la rama **true**, agrega un nodo de **Telegram** (necesitas crear un bot con @BotFather, toma 3 minutos; está en los recursos) que te envíe el resumen.
4. Conecta ambas ramas (true y false) al nodo de Gmail para que el correo siempre se envíe.

#### Paso 7: Activa y prueba en el mundo real (10 min)

1. Haz clic en el interruptor **"Inactive → Active"** arriba a la derecha.
2. En el nodo del formulario, copia la **Production URL** (no la de prueba).
3. Envíate el enlace y llénalo desde tu celular con tres mensajes distintos: una cotización urgente, una duda general y un mensaje raro o fuera de tema.
4. Revisa: ¿la IA clasificó bien los tres? ¿Las respuestas sugeridas tienen tu tono? Si no, ajusta el prompt en el Paso 3 y vuelve a probar. **Esta iteración es el verdadero aprendizaje.**

#### Paso 8: Documenta y proyecta (10 min)

En un documento, responde:

1. ¿Cuántos minutos por semana te ahorrará este flujo?
2. ¿Qué error cometió la IA en alguna prueba y cómo ajustaste el prompt?
3. Lista **tres automatizaciones más** para tu negocio usando la matriz de decisión (sección 2.6). Para cada una escribe: disparador → acción → dónde entra la IA.

Entrega este documento y una captura de pantalla de tu flujo activo como evidencia del módulo.

---

#### Si algo falla (problemas comunes)

| Síntoma | Causa probable | Solución |
|---|---|---|
| El nodo de IA devuelve texto y no campos separados | El modelo agregó texto extra al JSON | Refuerza en el prompt "ÚNICAMENTE JSON" y activa la opción de salida JSON del nodo |
| Google Sheets dice "columna no encontrada" | Los encabezados no coinciden exactamente | Revisa mayúsculas y tildes en la fila 1 de tu hoja |
| El correo llega con `{{ ... }}` sin reemplazar | El nombre del nodo en la expresión no coincide | Revisa el nombre exacto del nodo (clic derecho → Rename) |
| Error 401 en OpenAI | Clave inválida o sin crédito | Verifica la clave y que tengas saldo en platform.openai.com |
| El flujo no se ejecuta desde la URL pública | Está en modo inactivo | Activa el interruptor y usa la *Production URL* |

---

## 5. Recursos adicionales

### Documentación y aprendizaje
- **Documentación oficial de n8n:** [docs.n8n.io](https://docs.n8n.io) – especialmente las secciones *"Quickstart"* y *"AI Agents"*.
- **Biblioteca de plantillas de n8n:** [n8n.io/workflows](https://n8n.io/workflows) – busca "WhatsApp", "lead", "Instagram". Puedes importar un flujo completo y adaptarlo.
- **Curso gratuito de n8n (en inglés, con subtítulos):** disponible en la misma documentación, nivel 1 y 2.
- **Canal de YouTube de n8n en español:** busca "n8n español automatización IA" – hay creadores de México, Colombia y España con tutoriales paso a paso.

### Herramientas mencionadas (con planes gratuitos o pruebas)
- **Formularios:** Tally (gratis, ilimitado), Typeform
- **CRM:** HubSpot Free, Pipedrive (prueba)
- **Programación de redes:** Metricool, Buffer
- **WhatsApp Business API:** Meta Cloud API (gratis hasta cierto volumen), 360dialog, Wati, Twilio
- **Modelos de IA:** OpenAI, Anthropic Claude, Google Gemini (nivel gratuito generoso para pruebas)
- **Mensajería interna:** Telegram (crea tu bot con @BotFather – guía de 3 minutos en la documentación de n8n)

### Lecturas recomendadas
- *"The AI-Driven Leader"* – Geoff Woods (para pensar estratégicamente qué automatizar)
- Artículo: *"Human-in-the-loop: por qué la supervisión no es opcional"* – blog de Anthropic
- Guías de protección de datos por país: INAI (México), SIC (Colombia), ANPD (Brasil), AAIP (Argentina), ANPDP (Perú)

### Comunidades
- Foro oficial de n8n: [community.n8n.io](https://community.n8n.io)
- Grupos de Telegram/Discord de "No-code LATAM" y "n8n en español"
- Canal del curso: comparte tu flujo terminado y recibe retroalimentación de otros emprendedores.

### Alternativa auto-alojada (para cuando quieras ahorrar)
Cuando tu flujo esté estable y quieras dejar de pagar la nube de n8n, puedes alojarlo gratis en un servidor de bajo costo (Railway, Render o un VPS de USD $5/mes). Hay guías en español de una hora. Lo cubriremos en el Módulo 6 (Escalando tus sistemas de IA).

---

## 6. Preguntas de autoevaluación

**Pregunta 1 – Comprensión conceptual**
Explica con tus propias palabras la diferencia entre una automatización tradicional y una automatización con IA. Da un ejemplo de tu propio negocio donde una regla fija sería suficiente, y otro donde necesitarías que un modelo de IA interprete el contexto.

> *Respuesta orientativa:* La automatización tradicional ejecuta reglas exactas (si X, entonces Y); la de IA interpreta entradas ambiguas como texto libre. Ejemplo de regla fija: enviar recibo cuando se confirma un pago. Ejemplo que requiere IA: leer el mensaje de un cliente y decidir si es una queja, una consulta o una felicitación.

**Pregunta 2 – Diseño de flujos**
Tu negocio recibe reseñas en Google Maps. Quieres responder a todas, pero con tono distinto según sean positivas o negativas, y que las negativas te lleguen primero a ti antes de publicarse. Dibuja (o describe) el flujo identificando: el disparador, dónde entra la IA, qué condición usarías y qué acciones ocurren en cada rama. ¿Qué buena práctica de la sección 2.7 estarías aplicando con las reseñas negativas?

> *Respuesta orientativa:* Disparador: nueva reseña en Google Business Profile. IA: analiza sentimiento y redacta respuesta. Condición IF: ¿sentimiento negativo? Rama sí: enviar borrador al dueño para aprobación, luego publicar. Rama no: publicar directamente y registrar. Buena práctica: "humano en el bucle" para casos de mayor riesgo.

**Pregunta 3 – Criterio y riesgos**
Un amigo emprendedor te dice: "Voy a automatizar con IA todo mi proceso de cobranza: que el flujo lea los mensajes de los deudores, decida si darles prórroga y les responda solo". Usando la matriz de decisión (sección 2.6) y las buenas prácticas, ¿qué le recomendarías? Menciona al menos dos riesgos concretos y cómo mitigarlos.

> *Respuesta orientativa:* Es una tarea de alta frecuencia pero alto riesgo (dinero, relación con el cliente, posibles implicaciones legales). Recomendación: automatizar la clasificación y los recordatorios, pero mantener la decisión de prórroga con aprobación humana. Riesgos: la IA puede prometer condiciones que la empresa no puede cumplir (mitigación: prompt restrictivo + revisión), puede tratar injustamente a ciertos clientes por sesgos (mitigación: registrar justificaciones y auditar), y puede manejar datos financieros sensibles sin cumplir normativa (mitigación: revisar leyes de protección de datos del país y políticas del proveedor de IA).

---

**Siguiente módulo →** *Módulo 4: Agentes de IA – Cuando tu automatización empieza a tomar decisiones*