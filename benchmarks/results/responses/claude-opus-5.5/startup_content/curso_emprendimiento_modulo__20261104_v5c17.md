# Claude Opus 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.9 | quality: 10.0
- latency_total: 151.713s | tokens_per_second: 106.2
- input_tokens: 390 | output_tokens: 16111
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y un ejercicio paso a paso.

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

> **Curso:** IA Práctica para Emprendedores
> **Duración estimada:** 3 a 4 horas (1 h teoría, 1 h ejemplos, 1.5 a 2 h ejercicio práctico)
> **Nivel:** Emprendedor no técnico. No necesitas saber programar.
> **Requisitos previos:** Módulos 1 y 2 (fundamentos de IA y escritura de prompts), una cuenta de Google y un navegador web.

---

## 1. Objetivo del módulo

Al terminar este módulo podrás identificar qué tareas repetitivas de tu emprendimiento conviene automatizar con inteligencia artificial y convertirlas en flujos de trabajo funcionales usando herramientas visuales como **n8n**, sin escribir código. Entenderás la lógica de *disparador → acción → decisión*, sabrás conectar un modelo de IA (como ChatGPT o Gemini) con tus herramientas del día a día (Gmail, Google Sheets, WhatsApp, formularios) y construirás tu primera automatización real: un **sistema que recibe prospectos, los califica con IA y te avisa cuando aparece un cliente con alta probabilidad de compra**. El objetivo final es que dediques tu tiempo a lo que solo tú puedes hacer, como vender, decidir y crear relaciones, y que delegues lo repetitivo a un sistema que trabaja 24/7.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar?

Automatizar es **lograr que una tarea ocurra sola cada vez que se cumple una condición**, sin que tengas que intervenir.

Seguramente ya conoces automatizaciones simples:
- La respuesta automática de "estoy de vacaciones" en tu correo.
- El mensaje de bienvenida de WhatsApp Business.
- Un recordatorio de pago programado.

Estas automatizaciones tradicionales tienen un límite: **solo siguen reglas fijas**. Hacen exactamente lo mismo siempre y no "entienden" nada.

### 2.2 ¿Qué cambia cuando agregamos IA?

La IA aporta algo que antes era imposible de automatizar: **la capacidad de interpretar, redactar y decidir con criterio**.

| Automatización tradicional | Automatización con IA |
|---|---|
| "Si el correo contiene la palabra *factura*, muévelo a la carpeta Facturas" | "Lee el correo, entiende si es una queja, una consulta o una oportunidad de venta, y actúa según el caso" |
| Responde siempre el mismo texto | Redacta una respuesta personalizada según lo que preguntó el cliente |
| Necesita datos ordenados (números, opciones fijas) | Entiende texto libre, audios transcritos y mensajes con faltas de ortografía |
| Rígida: falla ante lo inesperado | Flexible: se adapta, aunque a veces se equivoca (por eso hay que supervisarla) |

> 💡 **Idea clave:** La automatización tradicional son las **manos** (mueve datos de un lugar a otro). La IA es el **cerebro** (entiende y decide). Juntas forman un "empleado digital" que hace tareas completas.

### 2.3 Anatomía de un flujo de trabajo (workflow)

Toda automatización, por compleja que parezca, tiene tres piezas básicas:

```
 ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
 │  DISPARADOR  │ ───▶ │  PROCESO     │ ───▶ │  ACCIÓN      │
 │  (Trigger)   │      │  (IA/lógica) │      │  (Resultado) │
 └──────────────┘      └──────────────┘      └──────────────┘
  "¿Qué lo inicia?"    "¿Qué se hace        "¿Qué pasa al
                        con la info?"         final?"
```

**Ejemplo cotidiano:**
1. **Disparador:** Llega un mensaje de WhatsApp de un cliente.
2. **Proceso:** La IA lee el mensaje y detecta que pregunta por el horario de atención.
3. **Acción:** Se envía la respuesta con el horario y se registra la consulta en una hoja de cálculo.

Además de estas piezas, existen las **condiciones** (si pasa X, haz esto; si no, haz aquello). Son las bifurcaciones del camino.

### 2.4 Conceptos que vas a escuchar (glosario rápido)

| Término | Qué significa en lenguaje simple |
|---|---|
| **Workflow / flujo** | La secuencia completa de pasos de tu automatización |
| **Nodo** | Cada "cajita" o paso del flujo (ej. "leer Gmail", "preguntar a la IA") |
| **Trigger / disparador** | El nodo que da inicio a todo |
| **Credencial** | El permiso que le das a la herramienta para entrar a tu Gmail, Sheets, etc. |
| **API** | La "puerta de servicio" por la que dos programas se comunican. No necesitas entenderla a fondo, solo saber que existe. |
| **API Key** | Una contraseña especial que te da un servicio (como OpenAI) para usarlo desde otra herramienta |
| **Webhook** | Una dirección web que "escucha" y activa tu flujo cuando recibe información |
| **Expresión** | Una forma de usar datos de un paso anterior (ej. "usa el nombre que escribió el cliente") |
| **Ejecución** | Cada vez que el flujo corre de principio a fin |

### 2.5 Herramientas de automatización: el panorama

| Herramienta | Ventajas | Desventajas | Ideal para |
|---|---|---|---|
| **Zapier** | La más fácil de usar, miles de integraciones | Se encarece rápido al crecer el volumen | Empezar en minutos con flujos simples |
| **Make** (ex Integromat) | Muy visual, buena relación precio/potencia | Curva de aprendizaje media | Flujos medianos con presupuesto ajustado |
| **n8n** | Muy potente con IA, se puede instalar en tu propio servidor, costo bajo a gran escala | La interfaz tiene más opciones y puede intimidar al principio | Startups que quieren escalar y controlar sus datos |

### 2.6 ¿Por qué n8n en este curso?

**n8n** (se pronuncia "n-eight-n") es una plataforma de automatización visual donde construyes flujos **arrastrando y conectando nodos**, como armar un diagrama.

**Razones para elegirla:**
1. **Nodos de IA integrados:** trae nodos listos para OpenAI (ChatGPT), Google Gemini, Anthropic (Claude) y "Agentes de IA" que pueden usar herramientas por sí mismos.
2. **Dos formas de usarla:**
   - **n8n Cloud:** la usas desde el navegador, sin instalar nada. Es de pago, con periodo de prueba gratuito. **Es la que usaremos en el ejercicio.**
   - **Autoalojada (self-hosted):** la instalas en tu propio servidor. Su código es abierto (licencia "fair-code") y el uso interno en tu empresa no paga licencia, aunque sí pagas el servidor. Requiere algo de conocimiento técnico o ayuda de un desarrollador.
3. **Escalabilidad de costos:** cobra por ejecución del flujo completo, no por cada paso, lo que suele salir más barato cuando tus flujos crecen.
4. **Plantillas:** tiene una biblioteca con miles de flujos hechos por la comunidad que puedes copiar y adaptar.
5. **Control de datos:** si la instalas tú, la información de tus clientes no pasa por servidores de terceros (salvo los servicios de IA que conectes).

> ⚠️ **Nota:** Los precios y nombres de los planes cambian con frecuencia. Revisa siempre la página oficial antes de decidir.

### 2.7 ¿Qué conviene automatizar? La matriz de decisión

No todo merece automatizarse. Usa esta regla rápida:

**Automatiza si la tarea es:**
- ✅ **Repetitiva:** ocurre muchas veces por semana.
- ✅ **Predecible:** sigue más o menos los mismos pasos.
- ✅ **De bajo riesgo** si sale mal, o fácil de revisar.
- ✅ **Consumidora de tiempo:** te quita más de 2 a 3 horas semanales.

**No automatices (todavía) si:**
- ❌ Ocurre una vez al mes.
- ❌ Requiere mucho criterio humano, empatía o negociación delicada.
- ❌ Un error tendría consecuencias graves (legales, financieras, de reputación) y nadie revisaría.
- ❌ Aún no entiendes bien el proceso manual. **Primero se ordena, luego se automatiza.**

> 🧠 **Regla de oro:** *Automatizar un proceso desordenado solo produce desorden más rápido.* Antes de abrir n8n, escribe el proceso paso a paso en papel.

### 2.8 Principio "humano en el circuito" (human-in-the-loop)

La IA puede equivocarse o "alucinar", es decir, inventar información con seguridad. Por eso, en tus primeras automatizaciones:
- Haz que la IA **prepare borradores** y que una persona apruebe antes de enviar algo importante.
- Registra todo en una hoja de cálculo para **auditar** qué hizo el sistema.
- Define **cuándo debe escalar a un humano** (ej. cliente molesto, reclamo de dinero, tema legal).

### 2.9 Privacidad y datos personales

Cuando automatizas con datos de clientes (nombres, teléfonos, correos), recuerda:
- En América Latina existen leyes de protección de datos, por ejemplo la LGPD en Brasil, la Ley 1581 en Colombia, la LFPDPPP en México y la Ley 25.326 en Argentina. Infórmate de la que aplica en tu país.
- Avisa a tus clientes cómo usarás sus datos (aviso de privacidad).
- No envíes a la IA información sensible innecesaria (datos de salud, números de tarjeta, documentos de identidad).
- Revisa las políticas de uso de datos del proveedor de IA que elijas.

---

## 3. Ejemplos prácticos de automatización para startups

> Los siguientes casos son **ilustrativos**. Están basados en situaciones comunes de emprendimientos latinoamericanos, y los tiempos ahorrados son estimaciones de referencia.

---

### 🟢 Ejemplo 1: Atención al cliente automatizada por WhatsApp

**🏪 Caso:** *"Dulce Raíz"*, una tienda online de snacks saludables en Bogotá. Recibe unas 80 consultas diarias por WhatsApp. El 70% son preguntas repetidas: precios, envíos, ingredientes, estado del pedido. La fundadora pasa 3 horas diarias respondiendo.

**🎯 Objetivo:** Responder al instante las preguntas frecuentes y derivar a un humano solo los casos complejos.

**🔄 Flujo:**

```
[Mensaje entra por WhatsApp Business]
            │
            ▼
[Agente de IA lee el mensaje]
 + consulta documento de preguntas frecuentes
 + consulta hoja de pedidos (Google Sheets)
            │
            ▼
   ¿Puede resolverlo con seguridad?
     │                     │
    SÍ                    NO (queja, reembolso,
     │                     cliente molesto)
     ▼                     ▼
[Responde por WhatsApp]  [Avisa a la fundadora por
     │                    Telegram/correo + responde:
     │                    "Te contactará una persona
     │                     en breve"]
     ▼                     │
[Registra la conversación en Google Sheets] ◀──┘
```

**🧰 Herramientas:**
- n8n: nodo *WhatsApp Trigger* / *WhatsApp Business Cloud* y nodo *AI Agent*
- WhatsApp Business Platform (API oficial de Meta, requiere verificación del negocio)
- OpenAI o Gemini como "cerebro"
- Google Sheets (base de pedidos y registro)

**✍️ Fragmento del prompt del agente:**
```
Eres el asistente de atención de Dulce Raíz, tienda de snacks saludables en Colombia.
Tono: cálido, cercano, breve. Tutea al cliente. Usa máximo 1 emoji por mensaje.

Reglas:
- Responde SOLO con información del documento de preguntas frecuentes y de la hoja de pedidos.
- Si no sabes algo, NO lo inventes: di que lo consultarás con el equipo.
- Si el cliente está molesto, pide un reembolso o menciona un problema de salud,
  responde con empatía y marca la conversación como ESCALAR.
```

**📊 Resultado estimado:** Respuesta en segundos (antes: hasta 4 horas). La fundadora pasa de 3 horas a unos 30 minutos diarios, dedicados solo a casos escalados.

**⚠️ Cuidados:**
- Usa la **API oficial de WhatsApp**. Las soluciones no oficiales pueden provocar el bloqueo de tu número.
- Meta cobra por ciertos tipos de conversación. Revisa la tarifa vigente para tu país.
- Revisa semanalmente una muestra de conversaciones para detectar errores.

---

### 🔵 Ejemplo 2: Generación de contenido para redes sociales

**🏪 Caso:** *"Ruta Andina"*, una startup de turismo de experiencias en Cusco. Sabe que debe publicar 5 veces por semana en Instagram y LinkedIn, pero el equipo de 3 personas nunca tiene tiempo. Publican de forma irregular.

**🎯 Objetivo:** Convertir una idea breve en borradores listos para cada red social, con aprobación humana antes de publicar.

**🔄 Flujo:**

```
[Lunes 8:00 a.m. (disparador programado)]
            │
            ▼
[Lee la hoja "Ideas de contenido" en Google Sheets]
 (el equipo anota ideas sueltas durante la semana:
  "turistas sorprendidos por la chicha morada")
            │
            ▼
[IA genera para cada idea:]
 • Post de Instagram (texto + hashtags)
 • Post de LinkedIn (tono profesional)
 • Sugerencia de imagen o guion de video corto
            │
            ▼
[Guarda los borradores en la hoja con estado "Por revisar"]
            │
            ▼
[Envía correo al equipo: "Tienes 5 borradores listos"]
            │
            ▼
[👤 HUMANO revisa, ajusta y cambia estado a "Aprobado"]
            │
            ▼
[Programación en herramienta de redes (Meta Business Suite,
 Buffer, etc.), manual o con un segundo flujo]
```

**🧰 Herramientas:**
- n8n: nodo *Schedule Trigger*, *Google Sheets*, *OpenAI/Gemini*, *Gmail*
- Opcional: generador de imágenes con IA o plantillas en Canva

**✍️ Fragmento del prompt:**
```
Actúa como community manager de Ruta Andina, startup de turismo de experiencias en Cusco.
Nuestra audiencia: viajeros de 25 a 40 años que buscan experiencias auténticas, no turismo masivo.
Voz de marca: inspiradora, respetuosa con las comunidades locales, sin clichés.

Idea: {{idea de la hoja}}

Genera:
1. Post de Instagram: gancho en la primera línea, máximo 150 palabras, llamado a la acción, 5 hashtags.
2. Post de LinkedIn: enfoque en turismo sostenible e impacto local, máximo 200 palabras.
3. Descripción de una imagen ideal para acompañar el post.
```

**📊 Resultado estimado:** El equipo pasa de unas 6 horas semanales creando contenido a 1.5 horas revisando y ajustando. La frecuencia de publicación se vuelve constante.

**⚠️ Cuidados:**
- La IA tiende a sonar genérica. Dale ejemplos de posts anteriores exitosos para que imite tu estilo.
- **Nunca publiques sin revisión humana:** la IA puede inventar datos (fechas, cifras, nombres de lugares).
- Revisa la sensibilidad cultural, sobre todo al hablar de comunidades o tradiciones.

---

### 🟠 Ejemplo 3: Calificación automática de leads

**🏪 Caso:** *"ContaFácil"*, un software de contabilidad para pymes en México. Su formulario web recibe unos 200 registros mensuales. El único vendedor llama a todos en orden de llegada y pierde tiempo con estudiantes y curiosos, mientras empresas listas para comprar esperan días.

**🎯 Objetivo:** Que la IA analice cada prospecto, lo clasifique por potencial y avise de inmediato cuando llega uno valioso.

**🔄 Flujo:**

```
[Prospecto llena formulario web]
 (nombre, empresa, tamaño, necesidad, presupuesto)
            │
            ▼
[IA analiza y clasifica: CALIENTE / TIBIO / FRÍO]
 según criterios definidos por el equipo de ventas
            │
            ▼
[Guarda el prospecto + clasificación en Google Sheets (mini CRM)]
            │
            ▼
      ¿Es CALIENTE?
       │          │
      SÍ          NO
       │          │
       ▼          ▼
[Alerta inmediata    [Entra a secuencia de
 al vendedor por      correos educativos
 correo/Telegram]     (nutrición)]
```

**🧰 Herramientas:**
- n8n: formulario o *Webhook*, *OpenAI/Gemini*, *Google Sheets*, nodo *If*, *Gmail*
- Opcional: un CRM como HubSpot, Pipedrive o Zoho en lugar de Sheets

**✍️ Criterios que se le dan a la IA (ejemplo):**
| Clasificación | Señales |
|---|---|
| 🔥 **CALIENTE** | Empresa con 5 o más empleados, necesidad concreta y urgente, menciona presupuesto o plazo |
| 🌤️ **TIBIO** | Negocio real pero sin urgencia, o necesidad vaga |
| ❄️ **FRÍO** | Estudiante, curioso, competencia o datos incoherentes |

**📊 Resultado estimado:** El tiempo de respuesta a los prospectos calientes baja de 2 o 3 días a menos de 1 hora. Responder rápido suele aumentar mucho la probabilidad de cerrar la venta.

**⚠️ Cuidados:**
- **Este es el ejemplo que construirás en el ejercicio práctico.**
- Revisa periódicamente si la IA clasifica bien. Compara sus decisiones con los resultados reales de venta y ajusta los criterios.
- No descartes a nadie automáticamente: los "fríos" igual reciben atención, aunque menos prioritaria.

---

## 4. Ejercicio práctico paso a paso

### 🛠️ Construye tu calificador automático de leads con IA

**⏱️ Tiempo estimado:** 60 a 90 minutos
**💰 Costo:** prueba gratuita de n8n Cloud + unos pocos centavos de dólar en IA (o gratis con Gemini, si usas su nivel gratuito)

**Lo que vas a construir:**

```
[Formulario n8n] → [IA clasifica] → [Google Sheets guarda] → [¿CALIENTE?] → [Gmail te avisa]
```

> 📌 **Nota importante:** n8n actualiza su interfaz con frecuencia. Si algún botón o nombre no coincide exactamente con lo que describimos, busca la opción más parecida. La lógica del flujo es la misma.

---

### ✅ Antes de empezar: checklist

- [ ] Cuenta de Google (Gmail + Google Sheets)
- [ ] Correo para registrarte en n8n
- [ ] Acceso a una IA con API. Elige **una**:
  - **Opción A, OpenAI:** cuenta en [platform.openai.com](https://platform.openai.com). Requiere cargar saldo (unos USD 5 alcanzan para miles de pruebas).
  - **Opción B, Google Gemini:** cuenta en [aistudio.google.com](https://aistudio.google.com). Tiene un nivel gratuito con límites de uso.
- [ ] 15 minutos para definir **tus** criterios de cliente ideal (Paso 0)

---

### Paso 0: Define tu cliente ideal (sin computadora) 📝

Este es el paso más importante. **La IA solo será tan buena como tus criterios.**

Completa esta tabla para tu propio emprendimiento:

| Pregunta | Tu respuesta |
|---|---|
| ¿Qué tipo de cliente compra más rápido? | |
| ¿Qué tamaño o perfil tiene? | |
| ¿Qué frase o necesidad indica urgencia? | |
| ¿Qué señales indican que NO es buen prospecto? | |

**Ejemplo (agencia de marketing digital):**
- Compra rápido: negocios que ya venden y quieren crecer.
- Perfil: facturan, tienen al menos 3 empleados.
- Urgencia: "lanzamos en un mes", "necesitamos más ventas ya".
- No es buen prospecto: "solo quiero información", estudiantes, presupuesto "cero".

---

### Paso 1: Crea tu cuenta en n8n Cloud ☁️

1. Entra a **[n8n.io](https://n8n.io)** y haz clic en **"Get started"** o **"Start free trial"**.
2. Regístrate con tu correo y elige un nombre para tu espacio de trabajo (ej. `miempresa`).
3. Al terminar, verás el panel principal. Haz clic en **"Create Workflow"** (o el botón **"+"**).
4. Ponle nombre al flujo arriba a la izquierda: `Calificador de Leads con IA`.

✅ **Checkpoint:** Ves un lienzo en blanco con un botón **"+"** en el centro.

---

### Paso 2: Prepara tu hoja de Google Sheets 📊

1. Abre [sheets.google.com](https://sheets.google.com) y crea una hoja nueva llamada `Leads - Mi Empresa`.
2. En la **fila 1**, escribe estos encabezados, uno por columna:

| A | B | C | D | E |
|---|---|---|---|---|
| Fecha | Nombre | Email | Mensaje | Clasificacion |

3. Escríbelos **sin tildes** y tal cual. Así evitas problemas al conectarlos.

✅ **Checkpoint:** Tienes una hoja con 5 encabezados en la fila 1.

---

### Paso 3: Crea el formulario (disparador) 📋

En lugar de conectar un formulario externo, usaremos el que ya trae n8n.

1. En el lienzo, haz clic en **"+"** y busca **"Form"**. Elige **"On form submission"** (n8n Form Trigger).
2. Configura:
   - **Form Title:** `Cuéntanos sobre tu proyecto`
   - **Form Description:** `Te contactaremos en menos de 24 horas.`
3. En **Form Elements / Form Fields**, agrega 3 campos:

| Field Label | Element Type | Required |
|---|---|---|
| `Nombre` | Text | ✅ |
| `Email` | Email | ✅ |
| `Mensaje` | Textarea | ✅ |

   *Sugerencia para el campo Mensaje: usa como placeholder "Cuéntanos qué necesitas, para cuándo y el tamaño de tu negocio".*

4. Haz clic en **"Test step"** (o **"Execute step"**). Se abrirá el formulario en una pestaña nueva.
5. Llénalo con un **prospecto de prueba caliente**:
   - Nombre: `Laura Méndez`
   - Email: `laura@ejemplo.com`
   - Mensaje: `Tengo una cadena de 3 cafeterías en Guadalajara con 15 empleados. Necesito una solución antes de fin de mes, tenemos presupuesto aprobado.`
6. Envíalo y regresa a n8n. Verás los datos recibidos en el panel derecho (**Output**).

✅ **Checkpoint:** En el Output del nodo aparecen Nombre, Email y Mensaje de Laura.

> 💡 **Tip:** Cada vez que pruebas un nodo, n8n guarda esos datos. Así puedes construir los siguientes pasos sin volver a llenar el formulario.

---

### Paso 4: Conecta la IA para clasificar 🤖

1. Haz clic en el **"+"** que aparece a la derecha del nodo del formulario.
2. Busca **"OpenAI"** (o **"Google Gemini"** si elegiste la opción B).
3. Elige la acción **"Message a model"** (enviar mensaje a un modelo).
4. **Crea la credencial**, que es darle permiso a n8n para usar tu IA:
   - En **"Credential to connect with"**, haz clic en **"Create new credential"**.
   - **OpenAI:** ve a [platform.openai.com/api-keys](https://platform.openai.com/api-keys) → **"Create new secret key"** → copia la clave → pégala en n8n → **Save**.
   - **Gemini:** ve a [aistudio.google.com](https://aistudio.google.com) → **"Get API key"** → **"Create API key"** → copia y pega en n8n → **Save**.

   > 🔒 **Seguridad:** Tu API Key es como la contraseña de tu tarjeta. No la compartas, no la publiques y no la pegues en documentos públicos.

5. **Modelo:** elige uno económico, como `gpt-4o-mini` (OpenAI) o un modelo `Flash` (Gemini). Para clasificar no necesitas el más caro.
6. **Mensaje / Prompt:** en el campo del mensaje (rol *User*), pega este texto y **adáptalo con tus criterios del Paso 0**:

```
Eres un experto en ventas B2B. Tu tarea es clasificar prospectos de mi empresa.

MI EMPRESA: [describe en 1 línea qué vendes, ej: "software de inventarios para restaurantes"]

CRITERIOS:
- CALIENTE: [tus señales de cliente listo para comprar]
- TIBIO: [tus señales de interés sin urgencia]
- FRIO: [tus señales de mal prospecto]

PROSPECTO:
Nombre: 
Mensaje: 

Responde ÚNICAMENTE con una de estas tres palabras, sin puntos, sin explicación:
CALIENTE
TIBIO
FRIO
```

7. **Inserta los datos del formulario.** Esta es la parte "mágica":
   - Asegúrate de ver el panel izquierdo (**Input**) con los datos de Laura.
   - **Arrastra** el campo `Nombre` desde el panel izquierdo y suéltalo justo después de `Nombre: ` en tu prompt.
   - Haz lo mismo con `Mensaje` después de `Mensaje: `.
   - Verás que aparece algo como `{{ $json.Nombre }}` en color. Eso es una **expresión**: le dice a n8n "aquí pon el dato real de cada prospecto".

8. Haz clic en **"Test step"**.

✅ **Checkpoint:** En el Output aparece la respuesta de la IA con la palabra **CALIENTE**.

> 🐛 **Si falla:**
> - *"Insufficient quota"* o un error de cuota: tu cuenta de OpenAI no tiene saldo cargado.
> - *"Invalid API key"*: vuelve a copiar la clave completa, sin espacios.
> - La IA responde con una frase larga: refuerza en el prompt "Responde ÚNICAMENTE con una palabra".

---

### Paso 5: Guarda el prospecto en Google Sheets 💾

1. Haz clic en **"+"** a la derecha del nodo de IA y busca **"Google Sheets"**.
2. Elige la acción **"Append row in sheet"** (agregar fila).
3. **Credencial:** **"Create new credential"** → **"Sign in with Google"** → elige tu cuenta → acepta los permisos.
4. Configura:
   - **Document:** elige de la lista `Leads - Mi Empresa`
   - **Sheet:** `Hoja 1` (o `Sheet1`)
   - **Mapping Column Mode:** `Map Each Column Manually`
5. Verás tus 5 columnas. Llénalas **arrastrando** datos del panel izquierdo:

| Columna | Qué poner |
|---|---|
| **Fecha** | Escribe `{{ $now.format('yyyy-MM-dd HH:mm') }}` (pon el campo en modo *Expression*) o arrastra el campo de fecha que entrega el formulario, si aparece |
| **Nombre** | Arrastra `Nombre` desde el nodo del **formulario** |
| **Email** | Arrastra `Email` desde el nodo del **formulario** |
| **Mensaje** | Arrastra `Mensaje` desde el nodo del **formulario** |
| **Clasificacion** | Arrastra el **texto de respuesta** de la IA (suele llamarse `content` o `text`) desde el nodo de **OpenAI/Gemini** |

   > 💡 **Tip:** En el panel izquierdo puedes desplegar datos de **cualquier nodo anterior**, no solo del inmediato. Busca el selector con el nombre del nodo o desplázate hacia arriba.

6. **"Test step"** y luego abre tu Google Sheet.

✅ **Checkpoint:** Aparece una fila nueva con los datos de Laura y la palabra `CALIENTE`.

---

### Paso 6: Agrega la condición "¿es CALIENTE?" 🔀

1. **"+"** a la derecha del nodo de Google Sheets → busca **"If"**.
2. Configura la condición:
   - **Valor 1:** arrastra la clasificación de la IA (desde el nodo de OpenAI/Gemini).
   - **Operador:** `String` → **`contains`** (contiene)
   - **Valor 2:** escribe `CALIENTE`
3. **"Test step"**.

✅ **Checkpoint:** El resultado de Laura sale por la rama **"true"** (verdadero).

> 💡 **¿Por qué "contains" y no "is equal to"?** Porque a veces la IA agrega un espacio o un salto de línea invisible. Con "contiene" el flujo es más tolerante a esos detalles.

---

### Paso 7: Envíate una alerta por Gmail 📧

1. En la salida **"true"** del nodo If, haz clic en **"+"** y busca **"Gmail"**.
2. Elige **"Send a message"**.
3. **Credencial:** **"Sign in with Google"**, igual que en Sheets.
4. Configura:
   - **To:** tu propio correo
   - **Subject:** `🔥 Lead CALIENTE: ` y arrastra el `Nombre` del formulario después del texto
   - **Email Type:** `Text`
   - **Message:**
     ```
     ¡Llegó un prospecto con alta probabilidad de compra! Contáctalo HOY.

     Nombre: [arrastra Nombre]
     Email: [arrastra Email]
     Mensaje: [arrastra Mensaje]
     ```
5. **"Test step"** y revisa tu bandeja de entrada.

✅ **Checkpoint:** Recibiste el correo de alerta con los datos de Laura. 🎉

---

### Paso 8: Prueba completa y activación 🚀

1. **Guarda** el flujo (`Ctrl + S` o el botón **Save**).
2. Haz una prueba completa con **"Test workflow"** (o **"Execute workflow"**) y llena el formulario con estos 3 casos:

| Prueba | Mensaje de ejemplo | Resultado esperado |
|---|---|---|
| 🔥 | "Tengo una empresa de 20 personas y necesito empezar la próxima semana. Ya tengo presupuesto." | CALIENTE + correo |
| 🌤️ | "Tengo un emprendimiento pequeño, me interesa para más adelante, quizás el próximo año." | TIBIO, sin correo |
| ❄️ | "Soy estudiante y estoy haciendo una tarea sobre empresas." | FRIO, sin correo |

3. Si las tres pruebas funcionan, **activa el flujo** con el interruptor **"Inactive → Active"** (arriba a la derecha). Según tu versión de n8n, puede llamarse **"Publish"**.
4. Abre el nodo del formulario y copia la **Production URL**. **Ese es el enlace real de tu formulario**: puedes ponerlo en tu Instagram, web o firma de correo.

> ⚠️ **Importante:** La *Test URL* solo funciona mientras pruebas. Para uso real, comparte siempre la **Production URL** con el flujo activado.

✅ **Checkpoint final:** Tu flujo se ve así y funciona solo, 24/7:

```
[On form submission] → [OpenAI/Gemini] → [Google Sheets] → [If] ─true─→ [Gmail]
                                                                └─false─→ (fin)
```

---

### 🏆 Retos opcionales (para subir de nivel)

1. **🟢 Fácil:** Además de la palabra, pide a la IA una **razón de una línea** en el correo de alerta. *Pista: crea un segundo nodo de IA que solo explique el porqué.*
2. **🟡 Medio:** En la rama **"false"**, envía un correo automático al prospecto agradeciéndole y compartiendo un recurso útil (guía, video, catálogo).
3. **🔴 Avanzado:** Reemplaza Gmail por **Telegram** para recibir las alertas en tu celular al instante.
4. **🔴 Avanzado:** Pide a la IA que también **redacte un borrador de respuesta personalizada** para cada lead caliente, listo para que tú lo revises y envíes.

---

### 📤 Entregable del módulo

Comparte en el foro del curso:
1. Captura de pantalla de tu flujo en n8n.
2. Captura de tu Google Sheet con al menos 3 prospectos clasificados.
3. Tu prompt de clasificación (sin datos sensibles).
4. Una reflexión breve: ¿qué otra tarea de tu negocio automatizarías con lo aprendido?

---

## 5. Recursos adicionales

### 📚 Documentación oficial
| Recurso | Para qué sirve |
|---|---|
| [docs.n8n.io](https://docs.n8n.io) | Documentación oficial de n8n (en inglés; puedes usar el traductor del navegador) |
| [n8n.io/workflows](https://n8n.io/workflows) | Miles de plantillas listas para copiar. Busca "lead", "WhatsApp", "social media" |
| [community.n8n.io](https://community.n8n.io) | Foro de la comunidad para resolver dudas |
| [Canal de YouTube de n8n](https://www.youtube.com/@n8n-io) | Tutoriales oficiales en video |

### 🤖 Plataformas de IA
| Recurso | Para qué sirve |
|---|---|
| [platform.openai.com](https://platform.openai.com) | API de OpenAI (modelos GPT) |
| [aistudio.google.com](https://aistudio.google.com) | API de Google Gemini, con nivel gratuito |
| [console.anthropic.com](https://console.anthropic.com) | API de Anthropic (modelos Claude) |

### 🔁 Herramientas alternativas
| Herramienta | Cuándo considerarla |
|---|---|
| [Make.com](https://www.make.com) | Si prefieres una interfaz aún más visual y flujos medianos |
| [Zapier](https://zapier.com) | Si necesitas algo muy simple en 10 minutos |
| [WhatsApp Business Platform](https://business.whatsapp.com/products/business-platform) | Para automatizar WhatsApp de forma oficial |

### 💡 Recomendaciones de práctica
- **Busca en YouTube** "n8n tutorial español": la comunidad hispanohablante de n8n es muy activa.
- **Empieza con plantillas:** copia una, ejecútala y modifícala. Es la forma más rápida de aprender.
- **Lleva una "bitácora de tareas repetitivas"** durante una semana: anota cada tarea que repites. Ahí están tus próximas automatizaciones.

---

## 6. Preguntas de autoevaluación

**Pregunta 1.** ¿Cuál es la principal diferencia entre una automatización tradicional y una automatización con IA?

- a) La automatización con IA es siempre gratuita.
- b) La automatización con IA puede interpretar texto libre y tomar decisiones con criterio, mientras que la tradicional solo sigue reglas fijas.
- c) La automatización tradicional no necesita disparador.
- d) La automatización con IA nunca comete errores.

<details>
<summary>👉 Ver respuesta</summary>

**Respuesta correcta: b)**

La IA aporta la capacidad de entender lenguaje natural (mensajes, correos, comentarios) y decidir según el contexto. La opción **d** es un error común: la IA **sí** puede equivocarse o inventar información, por eso aplicamos el principio de *humano en el circuito*.
</details>

---

**Pregunta 2.** Ordena correctamente los componentes del flujo que construiste en el ejercicio y explica la función del nodo **If**.

`[Gmail]` · `[Formulario]` · `[If]` · `[IA]` · `[Google Sheets]`

<details>
<summary>👉 Ver respuesta</summary>

**Orden correcto:** Formulario → IA → Google Sheets → If → Gmail

- **Formulario:** disparador; inicia el flujo cuando alguien envía sus datos.
- **IA:** analiza el mensaje y clasifica al prospecto.
- **Google Sheets:** guarda **todos** los prospectos, sin importar su clasificación.
- **If:** es la **condición o bifurcación**. Revisa si la clasificación contiene "CALIENTE" y solo en ese caso deja pasar el flujo hacia el correo de alerta. Así evitas recibir notificaciones de prospectos poco prioritarios.
- **Gmail:** acción final; te avisa para que contactes al lead de inmediato.
</details>

---

**Pregunta 3 (caso aplicado).** Carlos tiene una startup de clases de inglés en línea en Lima. Le preocupan tres tareas:

1. Responder cada día las mismas 10 preguntas por Instagram (precios, horarios, niveles).
2. Negociar contratos corporativos con empresas grandes (unas 2 al mes, montos altos).
3. Enviar recordatorios de clase a 150 alumnos cada semana.

¿Cuáles debería automatizar primero y cuál **no**? Justifica tu respuesta usando la matriz de decisión del módulo.

<details>
<summary>👉 Ver respuesta</summary>

**Automatizar primero:**
- **Tarea 3 (recordatorios):** muy repetitiva, totalmente predecible, de bajo riesgo y consume tiempo. Es la candidata ideal; ni siquiera necesita IA, basta una automatización tradicional.
- **Tarea 1 (preguntas frecuentes):** repetitiva y frecuente. Aquí la IA aporta valor porque los alumnos escriben de formas distintas. Debe incluir la regla de escalar a un humano cuando la IA no sepa la respuesta.

**No automatizar (todavía):**
- **Tarea 2 (contratos corporativos):** ocurre poco (2 al mes), requiere negociación, relación personal y criterio, y un error tendría alto impacto económico. Como mucho, la IA podría **ayudar** a preparar borradores de propuesta, pero la negociación debe seguir siendo humana.

*Clave: no todo lo que se puede automatizar se debe automatizar. Prioriza alta frecuencia + bajo riesgo + mucho tiempo invertido.*
</details>

---

## ✨ Cierre del módulo

> **"No se trata de reemplazar personas, sino de liberar a las personas para que hagan lo que mejor saben hacer."**

Ya tienes tu primer "empleado digital" funcionando. En el **Módulo 4** aprenderás a construir **Agentes de IA**: asistentes que no solo siguen un flujo fijo, sino que deciden por sí mismos qué herramienta usar para resolver una tarea.

📌 **Antes de continuar:** comparte tu entregable en el foro y comenta el flujo de al menos un compañero. ¡Aprender en comunidad multiplica los resultados!