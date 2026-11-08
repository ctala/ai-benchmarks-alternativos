# Claude Fable 5.1 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.67 | quality: 10.0
- latency_total: 142.722s | tokens_per_second: 76.5
- input_tokens: 390 | output_tokens: 10912
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y un ejercicio claro.

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

# Módulo 3: Automatización con IA — De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 3 horas (1 h teoría · 1.5 h ejercicio práctico · 0.5 h autoevaluación)
**Nivel:** Emprendedor no técnico
**Requisitos previos:** Haber completado el Módulo 2 (uso básico de ChatGPT / prompts)

---

## 1. Objetivo del módulo

Al finalizar este módulo, el emprendedor será capaz de identificar tareas repetitivas en su negocio que puedan automatizarse, diseñar un flujo de trabajo simple en papel usando la lógica "disparador → acción → decisión", y construir con sus propias manos una automatización funcional en **n8n** que combine herramientas que ya usa (formularios, correo, hojas de cálculo, WhatsApp) con un modelo de IA. El foco no es "entender la tecnología", sino **recuperar horas de trabajo a la semana** y mejorar la experiencia de sus clientes sin contratar un programador.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar? (y qué cambia cuando le sumamos IA)

**Automatizar** es hacer que una tarea se ejecute sola cuando ocurre algo. Ejemplo clásico: "cuando alguien llena el formulario de mi web, que su correo se guarde en una planilla".

Eso ya existía hace años. Lo que cambia con la IA es que ahora las automatizaciones pueden **entender, decidir y redactar**:

| Automatización tradicional | Automatización con IA |
|---|---|
| Mueve datos de A a B | Mueve datos **y los interpreta** |
| Sigue reglas fijas ("si el campo dice X") | Entiende texto libre ("este cliente parece molesto") |
| Envía mensajes plantilla | Redacta respuestas personalizadas |
| Falla si el dato llega distinto | Tolera variaciones humanas |

**Analogía:** la automatización tradicional es una cinta transportadora. La automatización con IA es una cinta transportadora con un asistente parado al lado que revisa cada paquete, lo clasifica y le escribe una nota al destinatario.

### 2.2 La anatomía de todo flujo de trabajo

Todo flujo, sin importar la herramienta, tiene 4 piezas. Si entiendes esto, entiendes el 80% de la automatización:

```
[DISPARADOR] → [ACCIÓN] → [DECISIÓN] → [ACCIÓN FINAL]
```

1. **Disparador (trigger):** el evento que arranca todo.
   *Ejemplos:* llega un correo, alguien llena un formulario, son las 8:00 am, entra un pedido en Mercado Libre, alguien escribe por WhatsApp.

2. **Acción:** algo que el flujo hace con la información.
   *Ejemplos:* guardar en Google Sheets, enviar un correo, preguntarle a ChatGPT.

3. **Decisión (condición):** una bifurcación.
   *Ejemplos:* ¿el cliente es nuevo o recurrente? ¿la pregunta es sobre precios o sobre envíos? ¿el lead es "caliente" o "frío"?

4. **Acción final:** lo que ocurre según la decisión.
   *Ejemplos:* avisar al vendedor por Telegram, responder automáticamente, archivar.

> **Ejercicio mental (2 minutos):** Piensa en una tarea que hiciste hoy más de dos veces. Escríbela en formato *"Cuando ___ , entonces ___ , y si ___ , entonces ___"*. Acabas de diseñar tu primer flujo.

### 2.3 Herramientas: el mapa del territorio

Existen tres herramientas "sin código" dominantes. Las tres funcionan con la misma lógica de bloques conectados:

| Herramienta | Ideal para | Costo | Curva de aprendizaje |
|---|---|---|---|
| **Zapier** | Empezar en 10 minutos | Caro al escalar (cobra por tarea) | Muy baja |
| **Make (ex Integromat)** | Flujos visuales complejos | Medio | Media |
| **n8n** | Control total, costo bajo, IA integrada | Gratis (autoalojado) o plan cloud económico | Media |

**En este curso usamos n8n** por tres razones:
- Tiene nodos de IA nativos (OpenAI, Anthropic, Google Gemini) y un "AI Agent" listo para usar.
- Si tu negocio crece, puedes instalarlo en tu propio servidor y dejar de pagar por tarea.
- La comunidad en español es grande y hay cientos de plantillas gratuitas.

### 2.4 Vocabulario mínimo de n8n (solo lo necesario)

No necesitas saber programar, pero sí hablar el idioma básico:

- **Workflow:** tu flujo completo. Un "proyecto".
- **Nodo (node):** cada bloque del flujo. Un nodo = una acción o un disparador.
- **Conexión:** la línea que une dos nodos. Por ahí viaja la información.
- **Credencial:** el "permiso" que le das a n8n para usar tu Gmail, tu Google Sheets, tu cuenta de OpenAI. Se configura una sola vez.
- **API Key:** una contraseña larga que te da un servicio (ej. OpenAI) para que n8n pueda usarlo. Se copia y pega, nada más.
- **Webhook:** una "dirección web" que n8n te da para que otras apps le avisen cuando pasa algo. Piensa en él como un buzón.
- **Ejecutar (Execute):** probar el flujo con datos reales para ver qué pasa en cada nodo.

### 2.5 ¿Qué automatizar primero? Los 4 criterios

No todo vale la pena automatizar. Antes de construir, pasa la tarea por este filtro:

1. **Frecuencia:** ¿ocurre al menos 5 veces por semana?
2. **Reglas claras:** ¿puedes explicarle a un empleado nuevo cómo hacerlo en menos de 10 minutos?
3. **Bajo riesgo:** si la IA se equivoca una vez, ¿el daño es recuperable? (No empieces automatizando cobros ni contratos.)
4. **Dolor real:** ¿te quita tiempo que preferirías usar vendiendo?

Si cumple 3 de 4, es candidata. Si cumple las 4, hazla esta semana.

### 2.6 El rol del prompt dentro de un flujo

En el Módulo 2 escribías prompts en un chat. Dentro de una automatización el prompt es distinto en una cosa clave: **la IA no tiene un humano leyendo la respuesta**. El resultado va directo a otro nodo. Por eso:

- Pide **formatos fijos**: "Responde solo con una palabra: CALIENTE, TIBIO o FRÍO".
- Da **contexto del negocio** en el prompt: qué vendes, a quién, qué tono usas.
- Define **qué hacer ante la duda**: "Si no estás seguro, responde REVISAR_HUMANO".
- Prueba con **al menos 10 casos reales** antes de activar el flujo.

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada (nivel 1)

**El problema:** Una tienda de productos naturales en Bogotá recibe 60 mensajes diarios por WhatsApp. El 70% son las mismas 8 preguntas (horarios, envíos, precios, si tienen stock). La fundadora responde desde el celular hasta las 11 pm.

**El flujo:**

```
[Mensaje entra por WhatsApp]
        ↓
[IA clasifica: ¿es pregunta frecuente o caso especial?]
        ↓
   ┌────┴────┐
   ↓         ↓
[Frecuente] [Especial]
   ↓         ↓
[IA redacta  [Se envía al
 respuesta    humano por
 usando el    Telegram con
 documento    resumen del
 de FAQ]      caso]
   ↓
[Se envía por WhatsApp]
   ↓
[Se registra en Google Sheets]
```

**Herramientas:** WhatsApp Business API (vía Twilio, 360dialog o Evolution API) + n8n + OpenAI + Google Sheets + Telegram.

**El prompt central (simplificado):**
```
Eres el asistente de [Nombre de la tienda]. Vendemos productos naturales en Bogotá.
Aquí tienes nuestras preguntas frecuentes: [pegar FAQ].

Lee el siguiente mensaje de un cliente y responde en formato JSON:
{
  "tipo": "FRECUENTE" o "ESPECIAL",
  "respuesta": "texto de la respuesta si es FRECUENTE, vacío si es ESPECIAL",
  "resumen": "una línea explicando qué quiere el cliente"
}

Reglas: tono cercano y breve, máximo 3 oraciones. Si el cliente menciona
una queja, reembolso o problema de salud, siempre es ESPECIAL.
```

**Resultado esperado:** 40 de 60 mensajes resueltos sin intervención. Tiempo recuperado: ~2.5 horas diarias.

**Error común:** dejar que la IA invente precios o stock. Solución: la IA solo responde con lo que está en el documento de FAQ; si no está, deriva a humano.

---

### Ejemplo 2: Generación de contenido para redes sociales

**El problema:** Una startup de software para restaurantes en Guadalajara sabe que debe publicar en LinkedIn e Instagram 3 veces por semana, pero el equipo son 3 personas y nadie tiene tiempo. Publican una vez al mes, cuando se acuerdan.

**El flujo:**

```
[Disparador: cada lunes 7:00 am]
        ↓
[Lee ideas de contenido desde Google Sheets
 (el equipo las anota durante la semana)]
        ↓
[IA genera 3 posts: uno para LinkedIn, uno para
 Instagram, un hilo corto para X]
        ↓
[IA genera un prompt de imagen para cada post]
        ↓
[Crea borradores en Notion / Google Docs]
        ↓
[Envía a Slack/WhatsApp: "Tus 3 posts de la semana
 están listos para revisar: [link]"]
        ↓
[Humano aprueba → otro flujo publica vía Buffer/Metricool]
```

**Herramientas:** n8n + Google Sheets + OpenAI (texto) + DALL·E o Flux (imagen) + Notion + Metricool.

**Clave del diseño:** el humano **siempre aprueba antes de publicar**. La IA genera borradores; la marca la cuida una persona.

**Prompt para el nodo de IA (fragmento):**
```
Eres el community manager de [Startup]. Nuestro tono es: directo, sin
jerga corporativa, con humor ligero. Nuestro cliente es dueño de
restaurante que no tiene tiempo.

Idea de contenido de esta semana: {{ $json.idea }}

Genera:
1. Post para LinkedIn (máx 150 palabras, empieza con un gancho, termina con pregunta)
2. Caption para Instagram (máx 80 palabras, 5 hashtags en español)
3. Descripción de imagen para generar con IA (en inglés, estilo fotografía real)

Nunca uses las palabras "revolucionario", "innovador" ni "sinergia".
```

**Resultado esperado:** de 1 post al mes a 12. Tiempo invertido por el equipo: 20 minutos de revisión semanal.

---

### Ejemplo 3: Calificación automática de leads

**El problema:** Una agencia de marketing en Lima recibe 40 formularios de contacto por semana. El vendedor los llama todos en orden de llegada. El 60% no tiene presupuesto. Los buenos leads se enfrían mientras él pierde tiempo con los malos.

**El flujo:**

```
[Formulario web enviado]
        ↓
[IA lee nombre, empresa, mensaje, presupuesto declarado]
        ↓
[IA asigna puntaje 1-10 y categoría: CALIENTE / TIBIO / FRÍO]
        ↓
   ┌────┼────────────┐
   ↓    ↓            ↓
[CALIENTE] [TIBIO]  [FRÍO]
   ↓        ↓          ↓
[Telegram   [Email de  [Email con
 inmediato  seguimiento recursos
 al vendedor en 24h,    gratuitos,
 + agenda   se agrega   se agrega
 link]      a CRM]      a newsletter]
        ↓
[Todo se registra en Google Sheets / HubSpot]
```

**Herramientas:** Typeform o Google Forms + n8n + OpenAI + Google Sheets o HubSpot + Gmail + Telegram.

**Criterios que la IA evalúa (los define el emprendedor):**
- ¿Menciona presupuesto? ¿Cuánto?
- ¿Tiene empresa con sitio web activo?
- ¿Describe un problema concreto o es vago?
- ¿Pide una reunión o solo "información"?

**Prompt (este es el que construiremos en el ejercicio):** ver sección 4, paso 5.

**Resultado esperado:** el vendedor llama primero a los 8-10 leads calientes de la semana. Tasa de cierre sube porque el contacto llega en minutos, no en días.

---

## 4. Ejercicio práctico paso a paso: Tu primer calificador de leads

**Qué vas a construir:** un flujo que recibe un formulario, usa IA para calificar al prospecto, lo guarda en una hoja de cálculo y te avisa por correo si es un lead caliente.

**Tiempo:** 60–90 minutos
**Costo:** $0 (n8n tiene prueba gratuita; OpenAI requiere cargar ~USD 5 que durarán meses con este uso)

**Necesitas antes de empezar:**
- Una cuenta de Google (Gmail + Sheets)
- Una cuenta en OpenAI con API key ([platform.openai.com](https://platform.openai.com) → *API keys* → *Create new secret key*). Cópiala en un lugar seguro.

---

### Paso 1: Crea tu cuenta en n8n

1. Ve a [n8n.io](https://n8n.io) y haz clic en **Start free**.
2. Crea tu cuenta (14 días gratis en la nube, sin tarjeta).
3. Al entrar verás un lienzo vacío. Haz clic en **Create Workflow**.
4. Ponle nombre arriba a la izquierda: `Calificador de leads`.

> **Alternativa gratuita permanente:** si tienes alguien técnico cerca, n8n puede instalarse gratis con Docker. Para este ejercicio usa la versión cloud.

### Paso 2: Prepara tu hoja de cálculo

1. Crea un Google Sheets nuevo llamado `Leads`.
2. En la fila 1 escribe estos encabezados, uno por columna:
   `Fecha` · `Nombre` · `Email` · `Empresa` · `Mensaje` · `Presupuesto` · `Puntaje` · `Categoría` · `Razón`
3. Deja la hoja abierta; la necesitarás en el paso 6.

### Paso 3: Agrega el disparador (formulario)

1. En el lienzo, haz clic en el **+** y busca `Form Trigger`. Selecciónalo.
2. Configura el formulario:
   - **Form Title:** `Contáctanos`
   - Agrega estos campos (botón *Add Form Element*):
     - `Nombre` (texto, obligatorio)
     - `Email` (email, obligatorio)
     - `Empresa` (texto)
     - `Presupuesto mensual aproximado` (texto)
     - `Cuéntanos qué necesitas` (textarea, obligatorio)
3. Haz clic en **Back to canvas**. Verás que el nodo tiene una URL de formulario de prueba. Guárdala.

### Paso 4: Agrega el nodo de IA

1. Haz clic en el **+** a la derecha del Form Trigger.
2. Busca `OpenAI` y elige la acción **Message a model**.
3. En **Credential**, haz clic en *Create new* y pega tu API key. Guarda.
4. En **Model**, elige `gpt-4o-mini` (barato y suficiente).
5. En **Messages**, agrega un mensaje con rol `System` y otro con rol `User`.

### Paso 5: Escribe el prompt

En el mensaje **System**, pega esto (adáptalo a tu negocio):

```
Eres el asistente comercial de [TU EMPRESA]. Vendemos [QUÉ VENDES]
a [QUIÉN ES TU CLIENTE IDEAL]. Nuestro ticket mínimo es [MONTO].

Tu trabajo es calificar prospectos. Responde ÚNICAMENTE con un JSON
válido, sin texto adicional, con esta estructura exacta:

{
  "puntaje": número del 1 al 10,
  "categoria": "CALIENTE" | "TIBIO" | "FRIO",
  "razon": "una oración explicando el puntaje"
}

Criterios:
- CALIENTE (8-10): presupuesto igual o mayor a nuestro mínimo, problema
  concreto, empresa identificable, pide reunión o cotización.
- TIBIO (5-7): interés real pero falta presupuesto claro o urgencia.
- FRIO (1-4): sin presupuesto, mensaje vago, estudiante, competidor,
  o pide trabajo.
Si hay duda entre dos categorías, elige la más baja.
```

En el mensaje **User**, escribe esto (los textos entre llaves se reemplazan solos con los datos del formulario; puedes arrastrarlos desde el panel izquierdo):

```
Nombre: {{ $json.Nombre }}
Email: {{ $json.Email }}
Empresa: {{ $json.Empresa }}
Presupuesto: {{ $json['Presupuesto mensual aproximado'] }}
Mensaje: {{ $json['Cuéntanos qué necesitas'] }}
```

6. Activa la opción **Output Content as JSON** (en *Options*). Esto hace que n8n entienda la respuesta como datos y no como texto.

### Paso 6: Guarda en Google Sheets

1. Haz clic en **+** después del nodo de OpenAI. Busca `Google Sheets` → **Append row**.
2. Conecta tu cuenta de Google cuando lo pida (*Sign in with Google*).
3. Selecciona el documento `Leads` y la hoja `Sheet1`.
4. En **Mapping**, elige *Map each column manually* y arrastra cada dato a su columna:
   - `Fecha` → escribe `{{ $now.format('dd/MM/yyyy HH:mm') }}`
   - `Nombre`, `Email`, `Empresa`, `Mensaje`, `Presupuesto` → arrástralos desde el nodo Form Trigger
   - `Puntaje`, `Categoría`, `Razón` → arrástralos desde el nodo OpenAI (aparecen como `message.content.puntaje`, etc.)

### Paso 7: Agrega la decisión

1. Haz clic en **+** después de Google Sheets. Busca `IF`.
2. Condición: el valor `{{ $('OpenAI').item.json.message.content.categoria }}` **is equal to** `CALIENTE`.
3. Ahora el nodo IF tiene dos salidas: **true** y **false**.

### Paso 8: Avísate por correo cuando el lead es caliente

1. Desde la salida **true** del IF, agrega el nodo `Gmail` → **Send a message**.
2. Conecta tu cuenta de Gmail.
3. **To:** tu correo.
4. **Subject:** `🔥 Lead caliente: {{ $('Form Trigger').item.json.Nombre }}`
5. **Message:**
```
Nuevo lead CALIENTE recibido.

Nombre: {{ $('Form Trigger').item.json.Nombre }}
Empresa: {{ $('Form Trigger').item.json.Empresa }}
Email: {{ $('Form Trigger').item.json.Email }}
Presupuesto: {{ $('Form Trigger').item.json['Presupuesto mensual aproximado'] }}

Puntaje IA: {{ $('OpenAI').item.json.message.content.puntaje }}/10
Razón: {{ $('OpenAI').item.json.message.content.razon }}

Mensaje original:
{{ $('Form Trigger').item.json['Cuéntanos qué necesitas'] }}

Llámalo en los próximos 15 minutos.
```
6. La salida **false** del IF la dejas vacía por ahora (el lead ya quedó guardado en Sheets).

### Paso 9: Prueba el flujo completo

1. Haz clic en **Test workflow** (arriba a la derecha).
2. Abre la URL del formulario de prueba en otra pestaña.
3. Llénalo simulando un lead caliente:
   > *Nombre:* María Torres · *Empresa:* Clínica Dental Sonrisa · *Presupuesto:* 800 USD/mes · *Mensaje:* "Necesitamos campañas en Instagram para conseguir pacientes nuevos, queremos empezar este mes. ¿Pueden cotizarnos?"
4. Vuelve a n8n: verás cada nodo con un check verde. Haz clic en cada uno para ver qué datos pasaron.
5. Revisa tu Google Sheets (debe haber una fila nueva) y tu correo (debe haber llegado el aviso).
6. Repite con un lead frío:
   > *Mensaje:* "Hola, soy estudiante y quería saber si tienen pasantías."
7. Verifica que se guardó en Sheets pero **no** llegó correo.

### Paso 10: Actívalo

1. Si todo funcionó, cambia el interruptor **Inactive → Active** arriba a la derecha.
2. El Form Trigger ahora te da una **URL de producción**. Esa es la que pones en tu web, en tu bio de Instagram o en tu WhatsApp.
3. Durante las primeras dos semanas, revisa la columna `Categoría` en Sheets una vez al día y corrige a mano si la IA se equivocó. Ajusta el prompt con lo que aprendas.

---

### Checklist de entrega del ejercicio

- [ ] Flujo con 5 nodos conectados (Form → OpenAI → Sheets → IF → Gmail)
- [ ] Al menos 3 pruebas registradas en Google Sheets (1 caliente, 1 tibio, 1 frío)
- [ ] Captura de pantalla del correo recibido
- [ ] Prompt adaptado a tu negocio real (no el ejemplo genérico)

### Retos opcionales (para quien quiera ir más allá)

- **Reto 1:** Reemplaza Gmail por Telegram o WhatsApp para recibir la alerta en el celular.
- **Reto 2:** Agrega un nodo de Gmail en la salida **false** que envíe un correo automático de "gracias, te escribiremos pronto" al lead.
- **Reto 3:** Cambia el disparador de Form Trigger a Typeform o a un webhook de tu página web actual.

---

## 5. Recursos adicionales

### Plantillas listas para usar
- **Biblioteca de plantillas de n8n:** [n8n.io/workflows](https://n8n.io/workflows) — filtra por "AI" o "lead". Puedes importar un flujo completo con un clic y modificarlo.
- Busca específicamente: *"AI lead qualification"*, *"WhatsApp AI chatbot"*, *"Social media content generator"*.

### Documentación y aprendizaje
- **Curso oficial gratuito de n8n (en inglés):** [docs.n8n.io/courses](https://docs.n8n.io/courses/) — nivel 1 toma ~2 horas.
- **Comunidad n8n en español:** foro oficial [community.n8n.io](https://community.n8n.io) (busca hilos en español) y grupos de Telegram "n8n Español" / "n8n Latam".
- **Playground de prompts de OpenAI:** [platform.openai.com/playground](https://platform.openai.com/playground) — para probar tu prompt antes de ponerlo en el flujo.

### Herramientas de conexión para Latinoamérica
- **WhatsApp:** Evolution API (gratis, autoalojado) · 360dialog · Twilio.
- **Formularios:** Tally (gratis y potente) · Typeform · Google Forms.
- **CRM sin costo:** HubSpot Free · Notion · Google Sheets.
- **Publicación en redes:** Metricool (plan gratis) · Buffer.

### Lecturas breves recomendadas
- *"The Automation Mindset"* — Zapier blog (inglés): cómo pensar en procesos antes que en herramientas.
- Artículo *"Cuándo NO automatizar"* del Módulo 1 de este curso (repasar sección 1.4).

### Calculadora de ROI de automatización (plantilla del curso)
Descarga la hoja `ROI_Automatizacion.xlsx` del aula virtual. Ingresa: minutos por tarea × veces por semana × tu costo por hora. Si el resultado supera USD 50/mes, la automatización se paga sola.

---

## 6. Preguntas de autoevaluación

**Pregunta 1.**
Tu socio quiere automatizar con IA el envío de facturas y el cobro automático a tarjetas de crédito de los clientes. Según los 4 criterios del módulo, ¿qué le dirías y por qué?

<details>
<summary>Ver respuesta sugerida</summary>

La tarea cumple con frecuencia y reglas claras, pero **falla en "bajo riesgo"**: un error de la IA (cobrar de más, cobrar dos veces, facturar al cliente equivocado) genera daño difícil de revertir y problemas legales. La recomendación es: automatizar la parte sin riesgo (generar el borrador de factura, recordar al cliente que vence su pago) y dejar la **aprobación del cobro en manos de un humano**. Empieza por automatizaciones donde el peor error sea "un mensaje mal redactado", no "dinero mal cobrado".
</details>

---

**Pregunta 2.**
Un emprendedor construyó un flujo de atención al cliente y la IA empezó a prometer descuentos que no existen y a inventar fechas de entrega. ¿Cuál es la causa más probable y cómo se corrige dentro del flujo?

<details>
<summary>Ver respuesta sugerida</summary>

La causa es un **prompt sin límites de información**: la IA responde con lo que "cree" en vez de con lo que la empresa definió. Se corrige de tres formas: (1) incluir en el prompt del sistema un documento de FAQ/políticas y la instrucción explícita *"responde solo con esta información"*; (2) agregar la regla *"si la pregunta no está cubierta, responde REVISAR_HUMANO"* y un nodo IF que derive esos casos a una persona; (3) prohibir explícitamente temas sensibles en el prompt ("nunca ofrezcas descuentos ni prometas fechas de entrega").
</details>

---

**Pregunta 3.**
Describe, usando la estructura *disparador → acción → decisión → acción final*, una automatización para **tu propio negocio** que no sea ninguna de las tres vistas en el módulo. Indica qué herramienta usarías en cada paso y qué le pedirías a la IA.

<details>
<summary>Criterios para autoevaluarte</summary>

Tu respuesta está completa si:
- El **disparador** es un evento concreto y observable (no "cuando tenga tiempo").
- La **IA tiene un rol claro**: clasificar, resumir, redactar o extraer datos. Si no hay nada que interpretar, probablemente no necesitas IA, solo automatización simple.
- La **decisión** tiene al menos dos caminos y el criterio de cada uno es verificable.
- Identificaste **qué pasa si la IA se equivoca** y hay un punto de revisión humana en los casos de mayor riesgo.
- Puedes estimar cuántas horas por semana recuperarías.

Ejemplo de respuesta válida: *"Cuando llega un correo con un PDF de factura de proveedor (Gmail trigger) → la IA extrae proveedor, monto y fecha de vencimiento (OpenAI) → si el monto supera USD 500 (IF) → me avisa por Telegram para aprobar; si no, lo registra directo en Sheets de cuentas por pagar."*
</details>

---

**Siguiente módulo:** Módulo 4 — "Agentes de IA: cuando la automatización toma decisiones" (construiremos un agente que consulta tu inventario y responde pedidos completos).