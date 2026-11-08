# Claude Opus 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 125.629s | tokens_per_second: 109.4
- input_tokens: 390 | output_tokens: 13742
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

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

# Módulo 3: Automatización con IA, de la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 3 a 4 horas (1 h de teoría, 30 min de ejemplos, 1.5 a 2 h de práctica)
**Nivel:** Emprendedor no técnico
**Requisitos previos:** Módulos 1 y 2 (fundamentos de IA y prompting), una cuenta de Gmail y ganas de experimentar

---

## 1. Objetivo del módulo

Al terminar este módulo podrás identificar qué tareas repetitivas de tu negocio conviene automatizar con IA y diseñar el flujo de trabajo en papel antes de tocar una herramienta. También construirás tu primera automatización funcional en **n8n**, sin saber programar: un sistema que recibe prospectos desde un formulario, los evalúa con IA, los registra en una hoja de cálculo y te avisa cuando aparece un cliente prometedor. La meta no es convertirte en ingeniero. Es que dejes de gastar horas en tareas que una máquina puede hacer por ti y recuperes ese tiempo para vender, crear y tomar decisiones.

---

## 2. Contenido teórico

### 2.1 ¿Qué es una automatización?

Una automatización es una **receta** que se ejecuta sola cuando ocurre algo. Todas siguen la misma lógica:

```
CUANDO pasa algo  →  ENTONCES haz esto  →  Y DESPUÉS esto otro
   (disparador)         (acción 1)            (acción 2)
```

**Ejemplo cotidiano:**
> *Cuando* alguien llena el formulario de contacto de mi web, *entonces* guarda sus datos en Google Sheets *y después* envíale un correo de bienvenida.

Esto existe desde hace años y no necesita IA. El problema es que las automatizaciones tradicionales solo siguen **reglas rígidas**: "si el asunto contiene la palabra *factura*, muévelo a la carpeta Facturas". No entienden el lenguaje humano.

### 2.2 ¿Qué cambia cuando agregamos IA?

La IA permite automatizar tareas que antes requerían **criterio humano**, sobre todo cuando hay texto desordenado de por medio.

| Automatización tradicional | Automatización con IA |
|---|---|
| Sigue reglas exactas ("si dice X, haz Y") | Entiende intención y contexto |
| Falla si el cliente escribe distinto a lo esperado | Maneja errores de ortografía, modismos y frases ambiguas |
| Mueve datos de un lugar a otro | Lee, resume, clasifica, redacta y decide |
| Ejemplo: copiar un formulario a Excel | Ejemplo: leer el formulario y decidir si es un buen cliente |

**Las 4 superpoderes de la IA dentro de un flujo:**

1. **Clasificar:** "¿Este mensaje es una queja, una pregunta o una venta?"
2. **Extraer:** "Saca el nombre, el producto y la fecha de este correo"
3. **Generar:** "Escribe 3 versiones de este post para Instagram, LinkedIn y X"
4. **Resumir:** "Dame en 3 líneas de qué trató esta conversación de 40 mensajes"

> 💡 **Regla de oro:** la IA es el "cerebro" del flujo y la herramienta de automatización son las "manos". La IA decide; n8n ejecuta.

### 2.3 Conoce n8n

**n8n** (se pronuncia *"n-eight-n"* o *"nodemation"*) es una plataforma visual para crear automatizaciones arrastrando y conectando bloques. Es popular entre startups por tres razones:

- **Tiene IA integrada:** nodos listos para OpenAI (ChatGPT), Google Gemini, Anthropic (Claude) y agentes de IA.
- **Es flexible:** se conecta con cientos de apps (Gmail, Google Sheets, WhatsApp, Telegram, Slack, HubSpot, Shopify, Notion…).
- **Puede ser muy económica:** existe una versión en la nube (de pago, con prueba gratuita) y una versión que puedes instalar en tu propio servidor sin pagar licencia.

#### Vocabulario esencial de n8n

| Concepto | Qué es | Analogía |
|---|---|---|
| **Workflow** (flujo) | La automatización completa | La receta |
| **Nodo** | Cada bloque o paso del flujo | Cada paso de la receta |
| **Trigger** (disparador) | El nodo que inicia todo | "Cuando suene el timbre…" |
| **Credencial** | El permiso para conectarse a una app | La llave de tu casa |
| **Ejecución** | Cada vez que el flujo corre | Cada vez que cocinas la receta |
| **Expresión** | Un dato que viene de un paso anterior, escrito como `{{ }}` | "Usa los huevos que compraste en el paso 1" |

#### n8n frente a otras herramientas

| | **n8n** | **Make** | **Zapier** |
|---|---|---|---|
| Facilidad para principiantes | Media | Media-alta | Muy alta |
| Capacidades de IA | Muy avanzadas (agentes, memoria) | Buenas | Buenas |
| Costo a medida que creces | Bajo, sobre todo si lo instalas tú | Medio | Alto |
| Ideal para | Startups que quieren escalar sin pagar de más | Flujos visuales complejos | Empezar rápido sin aprender nada |

> 📌 Usamos n8n en este curso porque lo que aprendas aquí te servirá cuando tu negocio crezca. Los conceptos (disparador, acción, nodo) son los mismos en todas las herramientas.

### 2.4 ¿Qué automatizar primero? La matriz de decisión

No todo merece automatizarse. Hazte estas 4 preguntas sobre cada tarea:

| Pregunta | Si la respuesta es SÍ… |
|---|---|
| ¿La hago más de 3 veces por semana? | ✅ Buena candidata |
| ¿Sigue más o menos los mismos pasos cada vez? | ✅ Buena candidata |
| ¿Me quita más de 15 minutos cada vez? | ✅ Buena candidata |
| ¿Un error aquí sería grave (dinero, temas legales, salud)? | ⚠️ Automatiza, pero con **revisión humana** |

**Ejercicio rápido (5 min):** anota en una hoja las 5 tareas que más odias hacer cada semana y califícalas con estas preguntas. La que más ✅ tenga es tu primera candidata.

### 2.5 Riesgos y buenas prácticas

- **La IA se equivoca ("alucina").** Nunca dejes que envíe precios, promesas o información legal sin una fuente confiable o sin revisión.
- **Humano en el circuito.** Para tareas críticas, haz que la IA prepare un borrador y que una persona apruebe antes de enviar.
- **Privacidad.** Revisa qué datos de tus clientes envías a servicios de IA y cumple la ley de protección de datos de tu país (por ejemplo, la LFPDPPP en México, la Ley 1581 en Colombia o la LGPD en Brasil).
- **Empieza pequeño.** Un flujo de 4 nodos que funciona vale más que uno de 30 que nunca terminas.
- **Mide el ahorro.** Anota cuánto tiempo te tomaba la tarea antes. Es la mejor forma de justificar la inversión.

---

## 3. Tres ejemplos prácticos para startups

> Los casos son ilustrativos, basados en patrones reales de pequeñas empresas latinoamericanas. Los costos son aproximados y dependen del volumen.

### Ejemplo A: Atención al cliente automatizada

**🏪 Caso:** *"Café de Origen"*, tienda online de café de especialidad en Medellín. Recibe unos 80 mensajes diarios por WhatsApp, y el 70% son las mismas preguntas: envíos, precios, métodos de pago y estado del pedido.

**❌ Problema:** la fundadora pasa 3 horas al día respondiendo y los mensajes nocturnos esperan hasta el día siguiente, así que se pierden ventas.

**🔄 Flujo:**
```
📱 Llega mensaje (WhatsApp o Telegram)
        ↓
🤖 Agente de IA lee el mensaje + consulta la base de conocimiento
   (preguntas frecuentes, políticas, catálogo en Google Docs/Sheets)
        ↓
❓ ¿La IA tiene una respuesta confiable?
   ├── SÍ → ✉️ Responde al cliente automáticamente
   └── NO / es una queja → 🙋 Avisa a una persona por Slack o email
                            y le dice al cliente: "Te contacta un asesor pronto"
        ↓
📊 Registra la conversación en Google Sheets (para mejorar después)
```

**🧩 Nodos de n8n:** WhatsApp Trigger (o Telegram Trigger) → AI Agent + modelo de chat (OpenAI o Gemini) → nodo IF → WhatsApp/Telegram (enviar) → Gmail/Slack → Google Sheets

**💰 Costo aproximado:** USD 20 a 50 al mes (n8n más el consumo de IA)
**📈 Impacto esperado:** respuesta en segundos las 24 horas y 2 a 3 horas diarias liberadas.

> ⚠️ **Tip:** la API oficial de WhatsApp Business requiere verificar tu negocio en Meta, y eso puede tardar. Para practicar, empieza con **Telegram**, que se configura en minutos. Luego migras a WhatsApp.

**Prompt clave del agente:**
```
Eres el asistente de Café de Origen. Responde SOLO con la información
de la base de conocimiento. Tono: cálido, cercano, colombiano, breve.
Si no sabes algo, si el cliente está molesto o si pide un reembolso,
NO inventes: responde "Déjame conectarte con alguien del equipo" y
marca la conversación como ESCALAR.
```

### Ejemplo B: Generación de contenido para redes sociales

**🏪 Caso:** *"Contadora Digital"*, startup de servicios contables para freelancers en Ciudad de México. Sabe que publicar en LinkedIn e Instagram le trae clientes, pero nunca tiene tiempo.

**❌ Problema:** publica de forma irregular y cada post le toma 45 minutos.

**🔄 Flujo:**
```
⏰ Cada lunes a las 8:00 am (disparador programado)
        ↓
📋 Lee las ideas de la semana desde Google Sheets
   (ej.: "Fecha límite declaración anual", "Error común en facturas")
        ↓
🤖 La IA genera para cada idea:
   • Post de LinkedIn (profesional, 150 palabras)
   • Caption de Instagram (cercano, con emojis y hashtags)
   • Hilo corto para X
        ↓
📝 Guarda los borradores en Google Sheets con estado "Por revisar"
        ↓
👀 La fundadora revisa, ajusta y cambia el estado a "Aprobado"
        ↓
📤 (Opcional) Un segundo flujo publica o programa los aprobados
```

**🧩 Nodos de n8n:** Schedule Trigger → Google Sheets (leer) → OpenAI/Gemini → Google Sheets (actualizar) → Gmail (aviso: "Tus borradores están listos")

**💰 Costo aproximado:** menos de USD 5 al mes en IA, más n8n
**📈 Impacto esperado:** de unas 6 horas semanales a 1 hora de revisión, con publicación constante.

**Prompt clave:**
```
Eres especialista en contenido para contadores en México.
Audiencia: freelancers y dueños de pequeños negocios, 25-45 años.
Idea del post: {{ idea }}
Escribe un post de LinkedIn de máximo 150 palabras con:
1. Un gancho inicial que genere curiosidad
2. Un dato o consejo práctico
3. Una llamada a la acción para agendar una asesoría
Evita jerga técnica. No inventes cifras ni fechas oficiales.
```

> 💡 **Por qué hay revisión humana:** el contenido representa tu marca. La IA te ahorra el 80% del trabajo, y tu 20% le da autenticidad (y evita que publiques una fecha fiscal equivocada).

### Ejemplo C: Calificación automática de leads

**🏪 Caso:** *"FlotaFácil"*, SaaS de gestión de flotillas de reparto en Santiago de Chile. Recibe 200 registros mensuales en su formulario de demo, pero solo un 20% son clientes reales. El resto son estudiantes, competidores o empresas demasiado pequeñas.

**❌ Problema:** el equipo de ventas pierde horas en llamadas que no llevan a nada, mientras los clientes buenos esperan días.

**🔄 Flujo:**
```
📝 Alguien llena el formulario de demo
        ↓
🤖 La IA evalúa al prospecto según tu cliente ideal:
   tamaño de empresa, industria, presupuesto, urgencia
   → Devuelve: puntaje (1-10), categoría y razón
        ↓
📊 Guarda todo en el CRM o Google Sheets
        ↓
❓ ¿Puntaje ≥ 7?
   ├── SÍ (🔥 caliente) → Aviso inmediato a ventas + email con link para agendar
   ├── 4-6 (🌤️ tibio) → Secuencia de emails educativos
   └── ≤ 3 (❄️ frío) → Email amable con recursos gratuitos
```

**🧩 Nodos de n8n:** Form Trigger (o Webhook desde tu web) → OpenAI/Gemini → Google Sheets / HubSpot → Switch o IF → Gmail / Slack

**💰 Costo aproximado:** centavos de dólar por lead evaluado
**📈 Impacto esperado:** ventas contacta a los mejores prospectos en minutos y no en días, y deja de perder tiempo con los que no encajan.

👉 **Este es el flujo que construirás en el ejercicio práctico.**

---

## 4. Ejercicio práctico paso a paso

### 🎯 Construye tu calificador de leads con IA

**Lo que vas a lograr:** un formulario real que, cuando alguien lo llena, hace cuatro cosas: la IA califica al prospecto, se guarda en Google Sheets y recibes un correo si es un lead caliente.

```
[Formulario] → [IA califica] → [Google Sheets] → [¿Puntaje ≥ 7?] → [Email de alerta]
```

**⏱️ Tiempo:** 60 a 90 minutos

#### ✅ Antes de empezar, necesitas:

- [ ] Una cuenta de Google (Gmail y Google Sheets)
- [ ] Una cuenta en **n8n Cloud**: [n8n.io](https://n8n.io) (tiene prueba gratuita)
- [ ] Acceso a un modelo de IA. Elige **una** opción:
  - **Opción A:** API key de OpenAI ([platform.openai.com](https://platform.openai.com)). Requiere cargar saldo; unos USD 5 alcanzan para cientos de pruebas.
  - **Opción B:** API key gratuita de Google Gemini ([aistudio.google.com](https://aistudio.google.com)), que tiene un nivel gratuito con límites.
  - Las cuentas nuevas de n8n Cloud a veces incluyen créditos de OpenAI de prueba. Revisa si aparece esa opción al crear la credencial.

> 🔐 **Importante:** tu API key es como la contraseña de tu tarjeta. No la compartas ni la publiques en capturas de pantalla.

### Paso 0: Define tu cliente ideal (10 min, sin computadora)

Antes de automatizar, la IA necesita saber qué es un "buen cliente" **para ti**. Completa esto en una hoja:

```
Mi negocio: ________________________________
Mi cliente ideal es: ______________________
  • Tamaño de empresa ideal: _______________
  • Industria(s): __________________________
  • Presupuesto mínimo: ____________________
  • Señales de urgencia: ___________________
Señales de que NO es buen cliente: _________
```

**Ejemplo (FlotaFácil):** empresas de reparto o logística con 10 o más vehículos, presupuesto mayor a USD 200 al mes, que quieran implementar en los próximos 3 meses. No es buen cliente: estudiantes, personas con 1 o 2 vehículos, quien "solo está mirando".

### Paso 1: Prepara tu hoja de Google Sheets (5 min)

1. Ve a [sheets.google.com](https://sheets.google.com) y crea una hoja nueva.
2. Nómbrala **"Leads calificados"**.
3. En la **fila 1** escribe exactamente estos encabezados, uno por columna:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Fecha | Nombre | Email | Empresa | Necesidad | Puntaje | Categoria | Razon |

### Paso 2: Crea tu workflow en n8n (2 min)

1. Entra a tu cuenta de n8n.
2. Haz clic en **"Create Workflow"** (o "Nuevo workflow").
3. Arriba a la izquierda, cámbiale el nombre a **"Calificador de Leads con IA"**.

### Paso 3: Agrega el formulario como disparador (10 min)

1. Haz clic en el botón **"+"** del centro del lienzo.
2. Busca **"Form"** y selecciona **"On form submission"** (n8n Form Trigger).
3. Configura:
   - **Form Title:** `Solicita una demo`
   - **Form Description:** `Cuéntanos sobre tu negocio y te contactamos`
4. En **Form Elements**, agrega estos campos con **"Add Form Element"**:

| Etiqueta (Field Label) | Tipo | ¿Obligatorio? |
|---|---|---|
| Nombre | Text | Sí |
| Email | Email | Sí |
| Empresa | Text | Sí |
| Tamaño del equipo | Dropdown: `Solo yo`, `2-10`, `11-50`, `Más de 50` | Sí |
| Presupuesto mensual | Dropdown: `Menos de USD 50`, `USD 50-200`, `Más de USD 200` | Sí |
| Qué necesitas | Textarea | Sí |

5. Haz clic en **"Test step"**. Se abrirá tu formulario en otra pestaña.
6. **Llénalo con datos de prueba** de un cliente ideal y envíalo.
7. Vuelve a n8n: en el panel derecho verás los datos que llegaron. ✅

> 💡 Estos datos de prueba son clave. Te permitirán arrastrar campos en los siguientes pasos sin escribir nada a mano.

### Paso 4: Agrega la IA que califica (20 min)

1. Haz clic en el **"+"** a la derecha del nodo del formulario.
2. Busca **"OpenAI"** y elige la acción **"Message a model"**. Si usas Gemini, busca **"Google Gemini"** y elige la acción equivalente para enviar un mensaje.
3. **Credencial:** haz clic en "Create new credential", pega tu API key y guarda.
4. **Model:** elige un modelo económico, como `gpt-4o-mini` o el modelo "Flash" de Gemini. Son baratos y suficientes para esta tarea.
5. En **Messages**, escribe este prompt y **adáptalo con tu cliente ideal del Paso 0**:

```
Eres un experto en ventas B2B. Evalúa a este prospecto según nuestro
cliente ideal.

NUESTRO CLIENTE IDEAL:
- Empresas de 11 o más personas
- Presupuesto mensual mayor a USD 200
- Necesidad clara y urgente relacionada con [TU PRODUCTO]

DATOS DEL PROSPECTO:
- Nombre: [arrastra aquí "Nombre"]
- Empresa: [arrastra aquí "Empresa"]
- Tamaño del equipo: [arrastra aquí "Tamaño del equipo"]
- Presupuesto: [arrastra aquí "Presupuesto mensual"]
- Necesidad: [arrastra aquí "Qué necesitas"]

Responde ÚNICAMENTE en formato JSON con esta estructura:
{
  "puntaje": número del 1 al 10,
  "categoria": "Caliente", "Tibio" o "Frío",
  "razon": "explicación breve en una sola oración"
}
```

6. **Cómo "arrastrar":** en el panel izquierdo (INPUT) verás los campos del formulario. Arrastra cada uno con el mouse hasta su lugar en el prompt. n8n creará automáticamente algo como `{{ $json.Nombre }}`. ¡No necesitas escribirlo tú!
7. Busca la opción **"Output Content as JSON"** (o similar) y **actívala**. Así n8n entenderá el puntaje como dato separado.
8. Haz clic en **"Test step"**. En el panel derecho deberías ver el `puntaje`, la `categoria` y la `razon`. ✅

### Paso 5: Guarda el resultado en Google Sheets (15 min)

1. Haz clic en **"+"** después del nodo de IA.
2. Busca **"Google Sheets"** y elige **"Append row in sheet"**.
3. **Credencial:** haz clic en "Sign in with Google" y autoriza el acceso.
4. Configura:
   - **Document:** selecciona "Leads calificados"
   - **Sheet:** Hoja 1 (o "Sheet1")
   - **Mapping Column Mode:** "Map Each Column Manually"
5. Aparecerán tus columnas. Llénalas **arrastrando** desde el panel izquierdo:

| Columna | Qué arrastrar |
|---|---|
| Fecha | Escribe: `{{ $now.format('yyyy-MM-dd HH:mm') }}` |
| Nombre, Email, Empresa, Necesidad | Busca en el panel izquierdo el nodo **"On form submission"** y arrastra cada campo |
| Puntaje, Categoria, Razon | Arrastra desde la salida del nodo de **OpenAI/Gemini** |

6. Haz clic en **"Test step"** y revisa tu Google Sheet: ¡debe aparecer una fila nueva! ✅

> 💡 Si no ves los campos del formulario en el panel izquierdo, busca un selector de nodos anteriores en la parte superior de ese panel y elige "On form submission".

### Paso 6: Filtra los leads calientes (10 min)

1. Haz clic en **"+"** después de Google Sheets y busca **"If"**.
2. Configura la condición:
   - **Valor 1:** arrastra el campo `puntaje` desde el nodo de IA
   - **Operación:** Number → **"is greater than or equal to"**
   - **Valor 2:** `7`
3. El nodo tendrá dos salidas: **true** (caliente) y **false** (no caliente).

> 💡 Si sale un error de tipo de dato, activa la opción **"Convert types where required"** en las opciones del nodo If.

### Paso 7: Recibe una alerta por email (10 min)

1. En la salida **true** del nodo If, haz clic en **"+"** y busca **"Gmail"** → **"Send a message"**.
2. Conecta tu cuenta de Google.
3. Configura:
   - **To:** tu propio correo
   - **Subject:** `🔥 Lead caliente: ` + arrastra el campo **Empresa**
   - **Email Type:** Text
   - **Message:**
   ```
   ¡Tienes un nuevo lead caliente!

   Nombre: [arrastra Nombre]
   Email: [arrastra Email]
   Empresa: [arrastra Empresa]
   Puntaje: [arrastra puntaje]/10
   Por qué: [arrastra razon]

   👉 Contáctalo hoy mismo.
   ```
4. Haz clic en **"Test step"** y revisa tu bandeja de entrada. ✅

### Paso 8: Prueba todo y actívalo (10 min)

1. Haz clic en **"Save"**, arriba a la derecha.
2. Haz **3 pruebas** con perfiles distintos usando "Test workflow":
   - 🔥 Un cliente ideal (empresa grande, buen presupuesto, necesidad clara)
   - 🌤️ Un cliente intermedio
   - ❄️ Un estudiante con "Solo yo" y "Menos de USD 50"
3. Verifica que los tres aparezcan en Sheets y que **solo** el primero te envíe un email.
4. Si todo funciona, **activa el workflow** con el interruptor "Inactive/Active" de arriba.
5. Copia la **Production URL** del formulario, en el nodo del formulario. Ese es el link que compartes en tu web, Instagram o firma de correo.

> ⚠️ Mientras pruebas, n8n usa una URL de **test**. Para uso real, comparte siempre la URL de **producción** con el workflow activado.

### 🛠️ Solución de problemas comunes

| Problema | Solución probable |
|---|---|
| "Credentials not valid" en OpenAI | Revisa que copiaste la API key completa y que tienes saldo en tu cuenta |
| La IA responde texto en lugar de JSON | Activa "Output Content as JSON" y repite en el prompt "responde ÚNICAMENTE en JSON" |
| No aparece mi hoja en Google Sheets | Revisa que autorizaste la misma cuenta de Google donde está la hoja |
| El nodo If siempre da "false" | Activa "Convert types where required"; el puntaje puede estar llegando como texto |
| El formulario real no dispara nada | Verifica que el workflow esté **activo** y que usas la URL de producción |
| Los campos aparecen vacíos en Sheets | Vuelve a ejecutar el formulario de prueba para que n8n tenga datos que mostrar |

### ✅ Checklist de entrega

- [ ] Mi workflow tiene 5 nodos conectados (Form → IA → Sheets → If → Gmail)
- [ ] Probé 3 perfiles distintos y la IA los calificó de forma lógica
- [ ] Solo los leads con puntaje de 7 o más me envían email
- [ ] El workflow está activo y tengo la URL de producción
- [ ] Tomé una captura de pantalla de mi flujo para compartir en la comunidad del curso

### 🚀 Reto extra (opcional)

Lleva tu flujo al siguiente nivel:
1. **Nivel 1:** en la salida **false** del If, agrega un Gmail que envíe al prospecto un correo amable con recursos gratuitos.
2. **Nivel 2:** pídele a la IA que también redacte un **email personalizado** para cada lead caliente según su necesidad, y guárdalo en Sheets como borrador.
3. **Nivel 3:** cambia Gmail por **Telegram** o **Slack** para recibir alertas en tu celular al instante.

---

## 5. Recursos adicionales

### 📚 Documentación y plantillas
- **Documentación oficial de n8n:** [docs.n8n.io](https://docs.n8n.io). Incluye guías de inicio y explicación de cada nodo.
- **Galería de plantillas de n8n:** [n8n.io/workflows](https://n8n.io/workflows). Miles de flujos listos para copiar. Busca "lead", "customer support" o "social media".
- **Foro de la comunidad n8n:** [community.n8n.io](https://community.n8n.io). Ideal para resolver dudas; puedes escribir en inglés con ayuda de un traductor.
- **Canal oficial de n8n en YouTube:** tutoriales en video, incluidos cursos para principiantes.

### 🤖 Plataformas de IA
- **OpenAI Platform:** [platform.openai.com](https://platform.openai.com) para API keys y control de gastos.
- **Google AI Studio:** [aistudio.google.com](https://aistudio.google.com) para obtener una API key de Gemini con nivel gratuito.

### 🔄 Alternativas para comparar
- **Make:** [make.com](https://www.make.com). Muy visual, con plan gratuito.
- **Zapier:** [zapier.com](https://zapier.com). La más fácil para empezar.

### 💡 Tips de costos
- Configura un **límite de gasto mensual** en tu cuenta de OpenAI para evitar sorpresas.
- Usa modelos pequeños ("mini" o "flash") para clasificar y reserva los grandes para tareas complejas.
- Cuando tu volumen crezca, evalúa instalar n8n en tu propio servidor (self-hosted) para reducir costos.

### 📋 Plantilla descargable: "Canvas de mi automatización"

Usa este formato antes de construir cualquier flujo:

```
1. TAREA A AUTOMATIZAR: _______________________
2. ¿CUÁNTO TIEMPO ME QUITA HOY? ______ horas/semana
3. DISPARADOR (¿qué la inicia?): _______________
4. ¿DÓNDE ENTRA LA IA? (clasificar/extraer/generar/resumir): ______
5. ACCIONES (¿qué pasa después?):
   a. _______________
   b. _______________
6. ¿NECESITA REVISIÓN HUMANA? Sí / No → ¿En qué paso? _______
7. HERRAMIENTAS QUE CONECTA: ___________________
8. ¿CÓMO SABRÉ QUE FUNCIONA? (métrica): _________
```

---

## 6. Preguntas de autoevaluación

**Pregunta 1.** María tiene una tienda de ropa en línea. Cada día recibe correos de proveedores con facturas en formatos distintos y copia a mano el nombre del proveedor, el monto y la fecha a Excel. ¿Por qué esta tarea se beneficia de una automatización **con IA** y no solo de una tradicional? ¿Qué "superpoder" de la IA usaría?

<details>
<summary>👉 Ver respuesta</summary>

Como cada proveedor usa un formato distinto, una regla rígida ("el monto siempre está en la línea 5") fallaría. La IA puede **entender** cada correo aunque esté escrito de forma diferente. El superpoder es **extraer**: sacar proveedor, monto y fecha del texto desordenado. Un flujo posible: Gmail Trigger → IA extrae los datos → Google Sheets. Como involucra dinero, conviene que María revise los montos periódicamente (humano en el circuito).
</details>

**Pregunta 2.** En el flujo de atención al cliente de "Café de Origen", ¿por qué es importante que la IA **escale a una persona** cuando no tiene una respuesta confiable o cuando el cliente está molesto? Menciona al menos dos riesgos de no hacerlo.

<details>
<summary>👉 Ver respuesta</summary>

Porque la IA puede **inventar información** (alucinar). Riesgos de no escalar:
1. **Prometer cosas falsas:** un reembolso, un descuento o una fecha de entrega que no existen, con consecuencias económicas o legales.
2. **Dañar la relación con el cliente:** un cliente molesto que recibe respuestas automáticas genéricas suele enojarse más y puede dejar malas reseñas.
3. **Perder aprendizaje:** las preguntas que la IA no sabe responder indican qué información falta en tu base de conocimiento.

La buena práctica es que la IA resuelva lo repetitivo y deje lo delicado a las personas.
</details>

**Pregunta 3.** En el ejercicio práctico, el prompt pedía a la IA responder **"ÚNICAMENTE en formato JSON"** con un puntaje numérico. ¿Por qué es necesario esto para que el nodo **If** funcione? ¿Qué pasaría si la IA respondiera con un párrafo como "Este lead parece bastante bueno, le daría un 8"?

<details>
<summary>👉 Ver respuesta</summary>

El nodo **If** necesita un **dato concreto y separado** (por ejemplo, `puntaje: 8`) para comparar si es mayor o igual a 7. Con un párrafo libre, n8n no puede saber dónde está el número: el If fallaría o daría siempre "false", y nunca recibirías alertas de leads calientes. El formato JSON convierte la respuesta de la IA en **datos estructurados** que las siguientes "manos" del flujo pueden usar. La IA decide; la estructura permite que n8n ejecute.
</details>

---

### 🎓 Próximo módulo

**Módulo 4: Agentes de IA, asistentes que trabajan por ti.** Aprenderás a crear agentes con memoria que consultan tus documentos, usan herramientas y toman decisiones de varios pasos.

> **Tarea antes del Módulo 4:** deja tu calificador de leads activo una semana, compártelo en al menos un canal real y anota cuántos leads recibiste y si la IA los calificó bien. Traeremos esos datos a la siguiente sesión para mejorar el prompt.