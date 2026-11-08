# Claude Sonnet 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 75.6s | tokens_per_second: 143.3
- input_tokens: 390 | output_tokens: 10831
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

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 3 a 4 horas (1 h de teoría + 30 min de ejemplos + 1.5-2 h de ejercicio práctico)
**Nivel:** Emprendedor no técnico (no necesitas saber programar)

---

## 1. Objetivo del módulo

Al terminar este módulo serás capaz de identificar qué tareas repetitivas de tu negocio se pueden automatizar, diseñar un flujo de trabajo con IA en papel y construir tu primera automatización funcional en N8N. Pasarás de usar la IA como un chat que consultas manualmente a integrarla como un "empleado digital" que trabaja dentro de tus procesos, 24/7, y libera tiempo para lo que realmente mueve tu startup: vender, crear producto y hablar con clientes.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatización con IA?

**Automatización tradicional:** sigue reglas fijas.
> *"Si llega un correo con la palabra 'factura', guárdalo en la carpeta Facturas."*

**Automatización con IA:** toma decisiones o genera contenido a partir de información no estructurada.
> *"Lee este correo, entiende qué quiere el cliente, redacta una respuesta adecuada y, si es una queja grave, avísame por WhatsApp."*

| | Automatización clásica | Automatización con IA |
|---|---|---|
| Entiende texto libre | ❌ | ✅ |
| Genera contenido | ❌ | ✅ |
| Clasifica y prioriza | Solo con reglas exactas | Con criterio flexible |
| Riesgo de error | Bajo, pero rígida | Medio, requiere supervisión |

La combinación de ambas es lo más potente: **reglas para la estructura, IA para el criterio**.

### 2.2 Anatomía de un flujo de trabajo

Todo flujo de automatización tiene cuatro piezas:

```
[TRIGGER] → [PROCESAMIENTO] → [DECISIÓN] → [ACCIÓN]
 Qué lo      Aquí entra        Qué camino    Qué se
 dispara     la IA             tomar         hace al final
```

**Ejemplo:** un cliente escribe por WhatsApp (trigger) → la IA entiende la consulta y busca en tu FAQ (procesamiento) → ¿es una consulta simple o requiere un humano? (decisión) → responde o crea un ticket y te avisa (acción).

### 2.3 Cómo saber qué automatizar: la regla de las 3 R

Automatiza tareas que sean:

1. **Repetitivas:** las haces más de 5 veces por semana.
2. **Reglamentables:** puedes explicar los pasos o criterios en palabras.
3. **De bajo Riesgo:** un error ocasional no destruye la relación con un cliente ni genera un problema legal.

**Matriz de priorización rápida:**

| | Bajo esfuerzo de implementar | Alto esfuerzo |
|---|---|---|
| **Alto impacto en tiempo/dinero** | ✅ Hazlo primero | 📅 Planifícalo |
| **Bajo impacto** | 🤷 Solo si sobra tiempo | ❌ Ignóralo |

### 2.4 Herramientas de automatización

| Herramienta | Ventaja principal | Ideal para |
|---|---|---|
| **N8N** | Muy flexible, versión gratuita autoalojada, buenos nodos de IA | Quien quiere control y escalar sin que el costo se dispare |
| **Make (Integromat)** | Interfaz muy visual | Flujos de complejidad media |
| **Zapier** | La más fácil de empezar, miles de integraciones | Automatizaciones simples y rápidas |

En este curso usaremos **N8N** porque:
- Tiene versión *cloud* (con prueba gratuita) y versión de código abierto que puedes instalar tú mismo.
- Cobra por ejecución de flujo completo, no por cada paso, lo que suele ser más económico al escalar.
- Tiene nodos nativos para IA (OpenAI, Anthropic, Google Gemini, agentes, memoria).

> 💡 **Nota:** Los precios y planes cambian con frecuencia. Verifica siempre las condiciones actuales en la web oficial antes de decidir.

### 2.5 Conceptos clave de N8N

- **Workflow (flujo):** el conjunto completo de pasos de tu automatización.
- **Nodo (node):** cada bloque individual (ej.: "Gmail", "OpenAI", "Google Sheets").
- **Trigger (disparador):** el nodo que inicia el flujo (nuevo correo, nuevo formulario, horario programado, mensaje de WhatsApp).
- **Credenciales:** las "llaves" que conectan N8N con tus otras cuentas (Google, OpenAI, etc.).
- **Expresiones:** forma de pasar datos de un nodo al siguiente. Se ven como `{{ $json.nombre }}`.
- **Ejecución:** cada vez que el flujo corre. Puedes revisar el historial para ver qué falló.

### 2.6 El prompt dentro de una automatización

Cuando la IA trabaja dentro de un flujo, no hay un humano corrigiendo en tiempo real. Tu prompt debe ser más estricto que en un chat:

**Fórmula R-C-F-L:**
- **R**ol: "Eres un asistente de ventas de una startup de..."
- **C**ontexto: información de tu negocio, criterios, tono.
- **F**ormato de salida: "Responde SOLO con una palabra: CALIENTE, TIBIO o FRÍO."
- **L**ímites: "Si no tienes información suficiente, responde 'REVISAR'. No inventes datos."

### 2.7 Buenas prácticas y riesgos

✅ **Haz esto:**
- Empieza con un solo flujo pequeño y mídelo.
- Incluye un **"humano en el loop"** en decisiones sensibles (reembolsos, quejas graves, contratos).
- Guarda un registro (por ejemplo, en Google Sheets) de lo que la IA hizo.
- Prueba con datos reales pero con pocos casos antes de activar.

⚠️ **Evita esto:**
- Dar a la IA acceso a datos sensibles innecesarios (tarjetas, contraseñas, documentos de identidad).
- Publicar contenido generado por IA sin revisión, al menos las primeras semanas.
- Automatizar un proceso que aún no funciona bien manualmente. *Automatizar el caos solo produce caos más rápido.*
- Ignorar la normativa de protección de datos de tu país (por ejemplo, LGPD en Brasil, Ley 1581 en Colombia, LFPDPPP en México, Ley 25.326 en Argentina). Informa a tus clientes cuando interactúan con un asistente automatizado.

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**Caso:** *Andina Café*, un e-commerce colombiano de café de especialidad, recibe 60+ mensajes diarios por WhatsApp y correo. El 70% son preguntas repetidas: estado del pedido, tiempos de envío, métodos de pago y formas de preparación.

**Flujo:**

```
[Trigger: nuevo mensaje en WhatsApp Business / Gmail]
        ↓
[IA: clasifica la intención]
   (estado de pedido / info de producto / queja / otro)
        ↓
[Decisión]
   ├─ Consulta simple → [IA responde usando tu base de FAQ]
   ├─ Estado de pedido → [Consulta Google Sheets/Shopify → IA redacta respuesta]
   └─ Queja o caso complejo → [Notifica a un humano por Slack/Telegram + crea ticket]
        ↓
[Registra la conversación en Google Sheets]
```

**Herramientas:** N8N + WhatsApp Business Cloud API (o Telegram/Gmail para empezar) + OpenAI/Claude/Gemini + Google Sheets.

**Prompt base:**
```
Eres el asistente virtual de Andina Café, tienda colombiana de café de
especialidad. Tono: cercano, amable y profesional. Tuteas al cliente.

Usa ÚNICAMENTE la siguiente información para responder:
{{ base_de_conocimiento }}

Reglas:
- Si la respuesta no está en la información, responde: "Déjame
  conectarte con una persona del equipo que te ayudará enseguida."
- Nunca inventes precios, plazos ni políticas.
- Máximo 80 palabras.
- Si el cliente expresa enojo o menciona reembolso, responde SOLO: ESCALAR
```

**Resultados típicos a medir:**
- % de consultas resueltas sin intervención humana (meta inicial: 40-60%)
- Tiempo de primera respuesta
- Satisfacción del cliente (una pregunta simple al final)

**⚠️ Error común:** no darle a la IA una base de conocimiento clara. Sin ella, inventa respuestas.

---

### Ejemplo 2: Generación de contenido para redes sociales

**Caso:** *Verde Urbano*, una startup mexicana de huertos urbanos, tiene un equipo de 3 personas y no logra publicar de forma constante.

**Flujo:**

```
[Trigger: cada lunes a las 8:00 am (Schedule)]
        ↓
[Lee tu "banco de ideas" en Google Sheets / Notion]
   (temas, productos, FAQs, testimonios, novedades)
        ↓
[IA: genera 5 publicaciones para la semana]
   (adaptadas a Instagram, LinkedIn y X)
        ↓
[IA: genera descripción de imagen o prompt para diseño]
        ↓
[Guarda borradores en Google Sheets con estado "Pendiente de revisión"]
        ↓
[Te envía un resumen por correo/Telegram para aprobar]
        ↓
[Cuando cambias el estado a "Aprobado" → publica o programa]
```

**Herramientas:** N8N + OpenAI/Claude + Google Sheets/Notion + Buffer/Metricool (o las APIs de redes) + Canva (para el diseño).

**Prompt base:**
```
Eres community manager de Verde Urbano, startup mexicana que vende
kits de huertos para departamentos pequeños.

Público: jóvenes profesionales de 25-40 años en ciudades grandes.
Tono: positivo, práctico, con un toque de humor. Usa español mexicano
neutro, sin exagerar con modismos.

Tema de la semana: {{ tema }}

Genera 3 publicaciones:
1. Instagram (máx. 120 palabras + 5 hashtags + sugerencia de imagen)
2. LinkedIn (tono más profesional, enfocado en emprendimiento sostenible)
3. Hilo de X (3 tuits)

Cada pieza debe terminar con un llamado a la acción distinto.
```

**Resultados típicos a medir:**
- Horas ahorradas por semana (pasa de ~5 h a ~1 h de revisión)
- Consistencia de publicación (publicaciones/semana)
- Engagement (comparado con el mes anterior)

**⚠️ Error común:** publicar sin revisar. La IA puede sonar genérica. Alimenta el flujo con tus propias historias, datos y fotos reales para diferenciarte.

---

### Ejemplo 3: Calificación automática de leads

**Caso:** *FacturaFácil*, un SaaS chileno de facturación para pymes, recibe 100+ formularios mensuales. El equipo comercial pierde tiempo con leads que no encajan (freelancers muy pequeños, estudiantes, competidores).

**Flujo:**

```
[Trigger: nuevo registro en formulario web]
        ↓
[Enriquece datos: dominio del correo, tamaño de empresa (opcional)]
        ↓
[IA: evalúa el lead según tu perfil de cliente ideal (ICP)]
   → Devuelve: CALIENTE / TIBIO / FRÍO + motivo en una línea
        ↓
[Decisión]
   ├─ CALIENTE → Alerta inmediata al vendedor + correo personalizado
   ├─ TIBIO   → Secuencia de nutrición automática
   └─ FRÍO    → Recurso educativo automático, sin intervención del equipo
        ↓
[Actualiza CRM (HubSpot / Pipedrive / Google Sheets)]
```

**Herramientas:** N8N + Typeform/Google Forms + OpenAI/Claude + CRM (o Google Sheets) + Gmail/Slack.

**Prompt base:**
```
Eres un analista de ventas de FacturaFácil, software de facturación
para pymes en Latinoamérica.

CLIENTE IDEAL: empresas de 5 a 100 empleados, que facturan
mensualmente, en Chile, Perú, Colombia o México. Decisor: dueño,
gerente o contador.

Datos del lead:
- Nombre: {{ nombre }}
- Cargo: {{ cargo }}
- Empresa: {{ empresa }}
- Empleados: {{ empleados }}
- País: {{ pais }}
- Mensaje: {{ mensaje }}

Clasifica en CALIENTE, TIBIO o FRIO. Responde exactamente en este
formato:
CLASIFICACION: [valor]
MOTIVO: [una frase de máximo 20 palabras]
```

**Resultados típicos a medir:**
- Tiempo de respuesta a leads calientes (meta: menos de 10 min)
- Tasa de conversión de leads calientes vs. anteriores
- Horas de tu equipo comercial ahorradas en filtrado

**⚠️ Error común:** no revisar la calidad de la clasificación. Durante las primeras 2-3 semanas compara manualmente 20 casos y ajusta el prompt.

---

## 4. Ejercicio práctico paso a paso

### 🎯 Proyecto: "Mi primer clasificador automático de leads"

**Lo que construirás:** un flujo que detecta cuando alguien se registra en un formulario, usa IA para clasificarlo como CALIENTE, TIBIO o FRÍO, guarda el resultado y te avisa por correo si es un lead caliente.

**Tiempo:** 1.5 a 2 horas
**Costo:** gratuito o de muy bajo costo (prueba gratuita de N8N Cloud + unos centavos de crédito de API)

### Requisitos previos

- [ ] Cuenta de Google (para Forms, Sheets y Gmail)
- [ ] Cuenta en [n8n.io](https://n8n.io) (prueba gratuita en la versión cloud)
- [ ] Una API key de un proveedor de IA (por ejemplo, OpenAI en platform.openai.com; requiere cargar un saldo pequeño, como 5 USD, que sobra para cientos de pruebas)

> 🔐 **Seguridad:** nunca compartas tu API key ni la pegues en capturas públicas o chats.

---

### Fase 1: Prepara tus datos (15 min)

**Paso 1.1: Define tu cliente ideal.**
Escribe en un documento, en 4-5 líneas, quién es tu cliente perfecto (industria, tamaño, país, cargo, presupuesto, problema). Si no tienes negocio aún, usa el de uno de los ejemplos.

**Paso 1.2: Crea un Google Form.**
Campos sugeridos:
- Nombre
- Correo
- Empresa
- Cargo
- Tamaño de la empresa (lista: 1-5, 6-20, 21-100, 100+)
- País
- "¿Qué problema quieres resolver?" (párrafo)

**Paso 1.3: Vincula el formulario a una hoja de cálculo.**
En el Form: pestaña *Respuestas* → *Vincular con Hojas de cálculo*.

**Paso 1.4: Agrega columnas a la hoja.**
Al final de las columnas existentes, añade: `Clasificacion` y `Motivo`.

**Paso 1.5: Carga 3 respuestas de prueba**, una que debería ser caliente, una tibia y una fría. Esto te permitirá validar los resultados.

---

### Fase 2: Crea tu flujo en N8N (45 min)

**Paso 2.1: Crea un nuevo workflow.**
Entra a N8N → *Create workflow* → ponle el nombre `Clasificador de Leads`.

**Paso 2.2: Agrega el Trigger.**
- Clic en **"Add first step"** → busca **Google Sheets Trigger**.
- Evento: **Row Added**.
- Conecta tu cuenta de Google (*Create new credential* → sigue el asistente).
- Selecciona tu hoja y pestaña de respuestas.
- Frecuencia de revisión: cada minuto (para pruebas).
- Pulsa **"Fetch Test Event"** para traer una fila de ejemplo.

✅ *Checkpoint:* deberías ver los datos de una respuesta en el panel derecho.

**Paso 2.3: Agrega el nodo de IA.**
- Clic en **+** → busca **OpenAI** → acción **Message a Model** (o *Basic LLM Chain* si prefieres otro proveedor).
- Crea la credencial pegando tu API key.
- Modelo: elige uno económico y rápido (por ejemplo, la versión "mini" disponible).
- En el mensaje del usuario, pega este prompt y **arrastra los campos** desde el panel izquierdo a los espacios correspondientes:

```
Eres un analista de ventas. Clasifica este lead según el cliente
ideal descrito abajo.

CLIENTE IDEAL:
[PEGA AQUÍ TU DESCRIPCIÓN DEL PASO 1.1]

DATOS DEL LEAD:
- Nombre: {{ $json["Nombre"] }}
- Empresa: {{ $json["Empresa"] }}
- Cargo: {{ $json["Cargo"] }}
- Tamaño: {{ $json["Tamaño de la empresa"] }}
- País: {{ $json["País"] }}
- Problema: {{ $json["¿Qué problema quieres resolver?"] }}

Responde EXACTAMENTE en este formato, sin texto adicional:
CLASIFICACION: CALIENTE o TIBIO o FRIO
MOTIVO: una frase de máximo 20 palabras
```

> 💡 *Los nombres entre llaves deben coincidir con los encabezados de tu hoja. Lo más fácil es arrastrarlos desde el panel de datos, no escribirlos.*

- Pulsa **"Execute step"** y revisa la respuesta.

✅ *Checkpoint:* la IA debe devolver las dos líneas con el formato pedido.

**Paso 2.4: Separa la clasificación del motivo.**
- Agrega un nodo **Edit Fields (Set)**.
- Crea dos campos de tipo texto:
  - `clasificacion` → expresión:
    `{{ $json.message.content.split("\n")[0].replace("CLASIFICACION:", "").trim() }}`
  - `motivo` → expresión:
    `{{ $json.message.content.split("\n")[1].replace("MOTIVO:", "").trim() }}`

> ⚙️ *La ruta `message.content` puede variar según el nodo y la versión de N8N. Si no funciona, haz clic en el nodo anterior, mira la estructura de salida y arrastra el campo de texto correcto.*

> 🆘 *Si esto te resulta complicado, alternativa más simple: pídele a la IA que responda solo una palabra (CALIENTE/TIBIO/FRIO) y omite el motivo en la primera versión.*

**Paso 2.5: Actualiza la hoja de cálculo.**
- Agrega un nodo **Google Sheets** → acción **Update Row**.
- Columna para identificar la fila: usa `row_number` (viene del trigger).
- Mapea `Clasificacion` ← `clasificacion` y `Motivo` ← `motivo`.

**Paso 2.6: Agrega la decisión.**
- Agrega un nodo **IF**.
- Condición: `clasificacion` **is equal to** `CALIENTE`.

**Paso 2.7: Notifica los leads calientes.**
- En la rama **true** del IF, agrega un nodo **Gmail** → **Send a Message**.
- Para: tu correo.
- Asunto: `🔥 Lead caliente: {{ nombre }} de {{ empresa }}`
- Mensaje: incluye nombre, cargo, empresa, correo del lead y el motivo de la IA.

**Paso 2.8 (opcional): Rama false.**
En la rama **false**, puedes dejarla vacía o añadir un correo automático con un recurso educativo para leads tibios y fríos.

---

### Fase 3: Prueba y ajusta (30 min)

**Paso 3.1: Ejecuta el flujo completo** con el botón **"Execute Workflow"** usando tus 3 casos de prueba.

**Paso 3.2: Completa esta tabla de validación:**

| Lead de prueba | Clasificación esperada | Clasificación de la IA | ¿Coincide? |
|---|---|---|---|
| Caso caliente | CALIENTE | | |
| Caso tibio | TIBIO | | |
| Caso frío | FRIO | | |

**Paso 3.3: Ajusta el prompt si hay errores.** Estrategias:
- Hazlos más explícitos: *"Es CALIENTE solo si cumple al menos 3 de estos 4 criterios..."*
- Agrega 2 o 3 **ejemplos** de leads con su clasificación correcta (técnica *few-shot*).
- Baja la "temperature" del modelo a 0 o 0.2 para que sea más consistente.

**Paso 3.4: Prueba con un formulario real.** Envía una respuesta desde tu Google Form y espera 1-2 minutos. Verifica que:
- [ ] La fila se actualizó con la clasificación y el motivo
- [ ] Recibiste el correo si era caliente

**Paso 3.5: Activa el workflow.**
Cambia el interruptor **Inactive → Active** (arriba a la derecha). Desde ahora corre solo.

---

### Fase 4: Reflexión y mejora (10 min)

Responde en tu cuaderno:
1. ¿Cuánto tiempo semanal te ahorraría este flujo en tu negocio real?
2. ¿Qué pasaría si la IA clasifica mal un lead? ¿Cómo lo detectarías?
3. ¿Qué otro paso agregarías? (por ejemplo, enviar un mensaje de WhatsApp, agendar una llamada con Calendly, crear una tarea en Trello)

---

### 🛠 Solución de problemas comunes

| Problema | Posible causa | Solución |
|---|---|---|
| El trigger no trae datos | Hoja o pestaña equivocada | Verifica que elegiste la pestaña de respuestas del Form |
| Error de credenciales en OpenAI | API key incorrecta o sin saldo | Revisa que la key esté bien copiada y que tengas crédito |
| La IA responde con formato distinto | Prompt poco estricto | Refuerza: "Responde EXACTAMENTE...", baja la temperature |
| Los campos aparecen vacíos (`undefined`) | Nombre de columna distinto | Arrastra los campos desde el panel en vez de escribirlos |
| El flujo no corre solo | Workflow inactivo | Activa el interruptor y revisa el intervalo del trigger |

### 🏆 Desafío extra (opcional)

- Añade un nodo que envíe una alerta por **Telegram o Slack** además del correo.
- Crea un segundo flujo que cada viernes te envíe un **resumen semanal**: cuántos leads de cada tipo llegaron.
- Redacta con IA un **correo de bienvenida personalizado** para cada lead según su problema declarado.

---

## 5. Recursos adicionales

### Documentación y aprendizaje oficial
- **N8N Docs:** https://docs.n8n.io (busca la sección *Try it out* y *AI*)
- **N8N Templates:** https://n8n.io/workflows (miles de flujos listos para importar y adaptar)
- **N8N Community:** https://community.n8n.io (foro activo para resolver dudas)
- **Canal oficial de N8N en YouTube** (tutoriales paso a paso, muchos con subtítulos)

### Plataformas alternativas para explorar
- **Make:** https://www.make.com
- **Zapier:** https://zapier.com
- **Flowise / Langflow:** para quienes quieran explorar agentes de IA más avanzados

### Guías de prompts
- Guías oficiales de prompting de OpenAI, Anthropic y Google (gratuitas, en sus sitios de documentación)
- Repositorio de *Prompt Engineering Guide*: https://www.promptingguide.ai

### Herramientas complementarias
- **Google Sheets / Airtable / Notion:** como "base de datos" ligera
- **WhatsApp Business Platform (Meta):** para atención al cliente
- **Buffer / Metricool:** programación de redes sociales
- **HubSpot CRM (plan gratuito):** CRM para startups

### Plantilla descargable sugerida para el curso
📄 **"Canvas de Automatización"** (una página, para completar antes de construir):
`Tarea a automatizar | Frecuencia | Tiempo actual | Trigger | Datos de entrada | Qué hará la IA | Salida esperada | Quién revisa | Métrica de éxito`

---

## 6. Preguntas de autoevaluación

**Pregunta 1 (opción múltiple)**
¿Cuál de las siguientes tareas es la **mejor candidata** para empezar a automatizar con IA según la regla de las 3 R?

a) Negociar un contrato de inversión con un fondo de capital de riesgo
b) Clasificar y responder preguntas frecuentes de clientes que llegan todos los días
c) Decidir la estrategia de precios para el próximo año
d) Despedir a un colaborador

> ✅ **Respuesta correcta: b).** Es repetitiva, se puede describir con criterios claros y tiene bajo riesgo si se deja un camino de escalamiento a humanos. Las demás son decisiones estratégicas o sensibles que requieren juicio humano.

---

**Pregunta 2 (verdadero o falso, con justificación)**
*"Una vez que activo un flujo de IA en N8N, no necesito volver a revisarlo porque la IA siempre toma decisiones correctas."*

> ✅ **Respuesta correcta: Falso.** La IA puede cometer errores o "alucinar". Se debe monitorear el desempeño, revisar muestras periódicamente, ajustar los prompts y mantener supervisión humana en decisiones sensibles.

---

**Pregunta 3 (aplicación)**
Piensa en tu propio negocio o idea. Describe una tarea que podrías automatizar y completa esta estructura:

- **Trigger:** ¿Qué dispara el flujo?
- **Procesamiento con IA:** ¿Qué hará la IA?
- **Decisión:** ¿Qué caminos posibles hay?
- **Acción final:** ¿Qué resultado se produce?
- **Supervisión humana:** ¿En qué punto intervienes tú?

> 📝 **Criterios de una buena respuesta:** el flujo tiene los cuatro componentes claros, la tarea cumple las 3 R, se define una métrica de éxito y se identifica al menos un punto de control humano.

---

## 📌 Resumen del módulo

- La automatización con IA combina **reglas (estructura)** con **IA (criterio y generación)**.
- Todo flujo tiene: **Trigger → Procesamiento → Decisión → Acción**.
- Automatiza lo **Repetitivo, Reglamentable y de bajo Riesgo**.
- N8N permite construir flujos potentes **sin programar**.
- Empieza **pequeño**, **mide**, **supervisa** y **mejora**.

**➡️ Próximo módulo:** *Agentes de IA y asistentes personalizados para tu negocio.*