# Claude Sonnet 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 75.706s | tokens_per_second: 139.9
- input_tokens: 390 | output_tokens: 10593
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

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

**Duración estimada:** 3 horas (45 min de teoría, 30 min de ejemplos, 90 min de práctica, 15 min de cierre)
**Nivel:** Emprendedor no técnico. No necesitas saber programar.
**Requisitos previos:** Haber completado los Módulos 1 y 2 (fundamentos de IA y prompting efectivo).

---

## 1. Objetivo del módulo

Al terminar este módulo, serás capaz de **identificar tareas repetitivas en tu negocio, diseñar un flujo de trabajo automatizado que combine herramientas y modelos de IA, y construir tu primera automatización funcional en N8N**. Saldrás con un flujo real de calificación de leads corriendo en tu cuenta, y con un método replicable para automatizar otros procesos de tu startup sin depender de un programador.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar con IA?

**Automatizar** es lograr que una tarea ocurra sola, cada vez que se cumple una condición, sin que tengas que hacerla manualmente.

**Automatizar con IA** añade un ingrediente clave: el flujo ya no solo mueve datos de un lugar a otro, también **entiende, decide y genera contenido** en el camino.

| | Automatización tradicional | Automatización con IA |
|---|---|---|
| **Lógica** | Reglas fijas ("si el monto > $100, enviar a X") | Interpretación flexible ("si el mensaje suena a queja urgente, escalar") |
| **Datos que maneja** | Estructurados (celdas, formularios) | Estructurados y no estructurados (correos, chats, audios, textos libres) |
| **Ejemplo** | Copiar un pedido de Shopify a una hoja de cálculo | Leer un correo de un cliente, entender qué pide y redactar la respuesta |

### 2.2 La anatomía de cualquier automatización

Todo flujo de trabajo, sin importar la herramienta, tiene tres partes:

```
   ┌──────────┐      ┌──────────────┐      ┌──────────┐
   │ TRIGGER  │ ───► │  PROCESO     │ ───► │  ACCIÓN  │
   │ (Disparador)│   │ (incluye IA) │      │ (Resultado)│
   └──────────┘      └──────────────┘      └──────────┘
   "Cuando pasa X"   "Entiende/decide"     "Haz Y"
```

- **Trigger (disparador):** el evento que inicia todo. Ej.: llega un correo, alguien llena un formulario, es lunes a las 8:00 a.m.
- **Proceso:** transformaciones, condiciones y pasos con IA. Ej.: clasificar, resumir, redactar, extraer datos.
- **Acción:** lo que ocurre al final. Ej.: enviar un mensaje, guardar en una hoja, crear una tarea.

### 2.3 Herramientas principales

| Herramienta | Mejor para | Curva de aprendizaje | Costo aproximado* |
|---|---|---|---|
| **N8N** | Flujos flexibles, con IA integrada, control de datos | Media | Gratis si lo instalas tú (self-hosted); planes en la nube de pago con prueba gratuita |
| **Make** | Flujos visuales, muchas integraciones | Baja-Media | Plan gratuito limitado y planes de pago |
| **Zapier** | Automatizaciones simples y rápidas | Baja | Plan gratuito limitado, planes de pago más caros al escalar |

*Los precios cambian con frecuencia. Verifica siempre en los sitios oficiales.

**¿Por qué usaremos N8N en este curso?**
- Tiene **nodos de IA nativos** (agentes, clasificadores, extractores de información) que no requieren código.
- Cobra por ejecución completa del flujo, no por cada paso, lo cual **sale más económico al escalar**.
- Es de código abierto, así que puedes **alojar tus propios datos**, algo importante si manejas información sensible de clientes.
- Tiene una comunidad enorme y miles de plantillas gratuitas.

### 2.4 Conceptos clave de N8N (vocabulario mínimo)

| Concepto | Qué es | Analogía |
|---|---|---|
| **Workflow** | El flujo completo | La receta |
| **Node (nodo)** | Cada paso individual | Un ingrediente o una instrucción |
| **Trigger node** | El nodo que inicia el flujo | El timbre de la puerta |
| **Credentials** | Conexiones autorizadas a tus apps (Gmail, Sheets, OpenAI) | Las llaves de cada app |
| **Expression** | Forma de usar datos de pasos anteriores, con formato `{{ $json.campo }}` | Un campo de combinación en un mail merge |
| **Execution** | Cada vez que corre el flujo | Cada vez que se cocina la receta |

> **Nota:** N8N actualiza su interfaz con frecuencia. Si algún nombre de nodo o menú cambia ligeramente, busca el equivalente. La lógica es la misma.

### 2.5 Método para pasar de la idea al flujo: **MAPA**

Antes de abrir cualquier herramienta, responde estas cuatro preguntas en papel:

1. **M**olestia: ¿Qué tarea repetitiva me quita más tiempo o se me olvida con frecuencia?
2. **A**ctivador: ¿Qué evento dispara esa tarea?
3. **P**asos: ¿Cuáles son los pasos que hago manualmente, en orden? ¿Cuáles requieren "criterio humano" (candidatos para IA)?
4. **A**cción final: ¿Cuál es el resultado esperado y dónde debe terminar?

### 2.6 Buenas prácticas y riesgos

- **Empieza pequeño:** automatiza un proceso de 5 pasos, no tu empresa entera.
- **Humano en el circuito:** al inicio, haz que la IA genere *borradores* que tú apruebas, no acciones irreversibles (como enviar correos a clientes sin revisar).
- **Privacidad:** no envíes datos sensibles (tarjetas, documentos de identidad, datos de salud) a modelos de IA sin evaluar los términos del proveedor y la normativa de protección de datos de tu país.
- **Controla costos:** las APIs de IA cobran por uso. Configura límites de gasto en tu cuenta del proveedor.
- **Documenta:** nombra bien tus nodos ("Clasificar lead con IA", no "OpenAI 1"). Tu yo del futuro lo agradecerá.
- **Maneja errores:** la IA puede equivocarse. Diseña un camino alternativo para casos dudosos (ej.: "si no estás seguro, avisa a un humano").

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**Contexto:** Una tienda online de ropa en Colombia recibe 80 mensajes diarios con preguntas repetidas: estado del pedido, tallas, envíos, devoluciones.

**Flujo:**

```
[Trigger: nuevo mensaje en WhatsApp Business / Telegram / formulario web]
              │
              ▼
[IA: Clasificar la intención]
   (¿es FAQ, estado de pedido, queja o venta?)
              │
      ┌───────┼────────────┐
      ▼       ▼            ▼
   [FAQ]  [Pedido]    [Queja/Complejo]
      │       │            │
      ▼       ▼            ▼
 [IA responde  [Consulta   [Notifica a un
  con base en   hoja de     humano por Slack
  tu documento  pedidos y   o correo con
  de FAQs]      responde]   resumen del caso]
```

**Herramientas:** N8N + WhatsApp Business API (o Telegram para empezar) + modelo de IA + Google Sheets/Docs como base de conocimiento.

**Prompt base para el nodo de IA:**
```
Eres el asistente de atención al cliente de [NOMBRE DEL NEGOCIO].
Responde SOLO con la información del documento de políticas adjunto.
Tono: cercano, amable y breve (máximo 3 oraciones). Usa "tú".
Si la respuesta no está en el documento, responde exactamente:
"Voy a conectarte con una persona del equipo para ayudarte mejor."
y marca la conversación como ESCALAR.

Mensaje del cliente: {{ $json.mensaje }}
```

**Resultado típico:** reducción notable de consultas repetitivas atendidas manualmente y respuesta en segundos, incluso fuera de horario.

**Errores comunes a evitar:**
- No limitar a la IA a tu base de conocimiento (puede inventar políticas).
- No dar una salida a un humano.
- WhatsApp Business API requiere aprobación y tiene costos por conversación. Valida con un proveedor oficial o empieza con Telegram para prototipar.

---

### Ejemplo 2: Generación de contenido para redes sociales

**Contexto:** Una fintech en México tiene un equipo de 2 personas y necesita publicar 5 veces por semana en LinkedIn e Instagram.

**Flujo:**

```
[Trigger: Todos los lunes a las 8:00 a.m. (Schedule)]
              │
              ▼
[Leer Google Sheets: banco de ideas / temas de la semana]
              │
              ▼
[IA: Generar 5 posts (uno por plataforma/formato)
     siguiendo la guía de voz de marca]
              │
              ▼
[IA: Generar descripción para imagen (opcional)]
              │
              ▼
[Guardar borradores en Google Sheets / Notion
 con estado = "Pendiente de revisión"]
              │
              ▼
[Notificar por correo/Slack: "Tus borradores están listos"]
```

**Herramientas:** N8N + Google Sheets o Notion + modelo de IA. Para publicar automáticamente, puedes sumar Buffer o la API de cada red, pero **recomendamos mantener la aprobación humana**.

**Prompt base:**
```
Actúa como community manager de [MARCA], una fintech para
freelancers en Latinoamérica.

Guía de voz: cercana, clara, sin jerga financiera, con un toque
de humor ligero. Nunca prometas rendimientos ni des asesoría
de inversión.

Tema de la semana: {{ $json.tema }}

Genera:
1. Un post para LinkedIn (máx. 150 palabras, con gancho inicial)
2. Un copy para Instagram (máx. 80 palabras + 5 hashtags)
3. Una idea de carrusel de 5 láminas (solo títulos)

Devuelve el resultado en formato claro, separado por secciones.
```

**Resultado típico:** pasas de 3 a 4 horas semanales de redacción a 30 minutos de revisión y ajuste.

**Errores comunes a evitar:**
- Publicar sin revisar: la IA puede sonar genérica o cometer errores de contexto cultural.
- No alimentar la IA con ejemplos de tus mejores posts (esto mejora mucho el estilo).
- En sectores regulados (finanzas, salud) revisa siempre el cumplimiento legal.

---

### Ejemplo 3: Calificación automática de leads

**Contexto:** Una startup SaaS B2B en Chile recibe 40 solicitudes de demo al mes. El equipo comercial pierde tiempo con prospectos que no encajan.

**Flujo:**

```
[Trigger: alguien completa el formulario de demo]
              │
              ▼
[IA: Analizar respuestas y asignar puntaje + categoría]
   (CALIENTE / TIBIO / FRÍO + justificación)
              │
              ▼
[Guardar en CRM o Google Sheets]
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
  CALIENTE  TIBIO     FRÍO
      │       │         │
      ▼       ▼         ▼
 [Alerta    [Correo   [Agregar a
  inmediata  con caso   newsletter
  al vendedor de éxito  educativo]
  + agenda   + seguimiento
  automática] en 3 días]
```

**Criterios de calificación (los defines tú):**

| Criterio | Señal de lead caliente |
|---|---|
| Tamaño de empresa | 10+ empleados |
| Cargo | Gerente, director, fundador |
| Urgencia | "Necesitamos implementarlo este trimestre" |
| Presupuesto | Menciona presupuesto o ya usa una solución similar |

**Prompt base:**
```
Eres un analista comercial de [EMPRESA]. Nuestro cliente ideal es:
empresas de 10 a 200 empleados, en Latinoamérica, que buscan
[PROBLEMA QUE RESUELVES].

Analiza este lead y responde con UNA SOLA palabra:
CALIENTE, TIBIO o FRIO.

Datos del lead:
- Nombre: {{ $json.nombre }}
- Cargo: {{ $json.cargo }}
- Empresa y tamaño: {{ $json.empresa }} / {{ $json.tamano }}
- Qué necesita: {{ $json.necesidad }}
- Cuándo quiere implementarlo: {{ $json.plazo }}
```

**Resultado típico:** el equipo comercial dedica su tiempo a los leads con mayor probabilidad de cierre, y el tiempo de primera respuesta baja de horas a minutos.

> Este es el ejemplo que construiremos juntos en el ejercicio práctico.

---

## 4. Ejercicio práctico paso a paso

### 🛠️ Construye tu "Calificador de Leads con IA"

**Tiempo estimado:** 60 a 90 minutos
**Resultado final:** un formulario que, al enviarse, es analizado por IA, guardado en una hoja de cálculo y, si el lead es "caliente", te avisa por correo.

```
[Formulario] → [IA clasifica] → [Guardar en Google Sheets] → [¿Caliente?] → [Correo de alerta]
```

### Antes de empezar: prepara tus cuentas

- [ ] Cuenta en **N8N Cloud** (n8n.io, hay prueba gratuita) o N8N instalado localmente
- [ ] Cuenta de **Google** (Sheets y Gmail)
- [ ] Una **API key** de un proveedor de IA (OpenAI, Google Gemini u otro compatible). Importante: la API se factura aparte de suscripciones como ChatGPT Plus. Carga un monto pequeño (ej.: USD 5) y activa un límite de gasto.

---

### Paso 1: Define tu lead ideal (10 min)

En un documento, escribe en 3 a 4 líneas quién es tu cliente ideal. Si aún no tienes uno, inventa un caso realista.

> *Ejemplo:* "Mi cliente ideal es una pyme de servicios de 5 a 50 empleados en Latinoamérica, con un dueño o gerente que busca automatizar su facturación en menos de 3 meses."

Guarda este texto: lo usarás en el prompt.

---

### Paso 2: Crea la hoja de cálculo (5 min)

1. Abre Google Sheets y crea una hoja llamada **"Leads IA"**.
2. En la fila 1 escribe estos encabezados, uno por columna:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Fecha | Nombre | Email | Empresa | Necesidad | Clasificación |

---

### Paso 3: Crea el workflow y el formulario (10 min)

1. En N8N, haz clic en **"Create Workflow"** y ponle el nombre: `Calificador de Leads con IA`.
2. Haz clic en **"Add first step"** y busca **"n8n Form Trigger"** (On form submission).
3. Configura:
   - **Form Title:** "Solicita tu demo"
   - **Campos (Form Elements):**
     - Nombre (texto, requerido)
     - Email (email, requerido)
     - Empresa (texto, requerido)
     - ¿Qué necesitas resolver? (área de texto, requerido)
     - ¿Cuándo quieres implementarlo? (menú desplegable: "Este mes", "En 1 a 3 meses", "Más adelante / solo explorando")
4. Haz clic en **"Test step"** (o "Execute step"), abre la **Test URL** del formulario en otra pestaña y **llénalo con datos de prueba**. Vuelve a N8N: verás los datos capturados.

✅ **Punto de control:** ves tus datos de prueba en el panel de salida del nodo.

---

### Paso 4: Conecta el nodo de IA (15 min)

1. Haz clic en el **"+"** a la derecha del nodo del formulario.
2. Busca **"OpenAI"** (o el proveedor que uses) y selecciona la acción de enviar un mensaje al modelo (*Message a model* o *Message*).
3. En **Credentials**, selecciona **"Create new credential"**, pega tu API key y guarda.
4. Selecciona un modelo económico y rápido (los modelos "mini" o "flash" son suficientes para clasificar).
5. En el campo del mensaje (rol *User*), pega este prompt y **personalízalo con tu cliente ideal del Paso 1**:

```
Eres un analista comercial. Nuestro cliente ideal es:
[PEGA AQUÍ TU CLIENTE IDEAL DEL PASO 1]

Clasifica el siguiente lead. Responde con UNA SOLA palabra,
sin puntuación ni explicación: CALIENTE, TIBIO o FRIO.

Criterios:
- CALIENTE: encaja con el cliente ideal Y quiere implementar pronto.
- TIBIO: encaja parcialmente o no tiene urgencia clara.
- FRIO: no encaja o solo está explorando.

Datos del lead:
Nombre: {{ $('On form submission').item.json['Nombre'] }}
Empresa: {{ $('On form submission').item.json['Empresa'] }}
Necesidad: {{ $('On form submission').item.json['¿Qué necesitas resolver?'] }}
Plazo: {{ $('On form submission').item.json['¿Cuándo quieres implementarlo?'] }}
```

> 💡 **Truco para no equivocarte con las expresiones:** en lugar de escribirlas a mano, **arrastra los campos** desde el panel izquierdo (INPUT) hasta el campo de texto. N8N escribe la expresión por ti. Los nombres deben coincidir exactamente con los de tu formulario.

6. Haz clic en **"Test step"**.

✅ **Punto de control:** en la salida ves una de las tres palabras. Prueba con 3 leads distintos (uno ideal, uno dudoso, uno que no encaja) y verifica que la IA los clasifique con sentido. Si no, **ajusta el prompt**: ese es el verdadero trabajo de un buen automatizador.

---

### Paso 5: Guarda el lead en Google Sheets (10 min)

1. Agrega un nuevo nodo: **Google Sheets** → acción **"Append Row"** (agregar fila).
2. Conecta tu cuenta de Google (credencial) siguiendo el asistente de N8N.
3. Selecciona tu documento **"Leads IA"** y la hoja correspondiente.
4. Mapea cada columna arrastrando los campos:
   - Fecha → `{{ $now }}`
   - Nombre, Email, Empresa, Necesidad → los campos del formulario
   - Clasificación → la respuesta del nodo de IA
5. **Test step** y revisa tu hoja de cálculo.

✅ **Punto de control:** aparece una fila nueva con la clasificación.

---

### Paso 6: Añade la condición "¿Es caliente?" (5 min)

1. Agrega un nodo **"If"** después de Google Sheets.
2. Configura la condición: el valor de la respuesta de la IA **"is equal to"** `CALIENTE`.
   - Consejo: usa la opción que ignora mayúsculas/minúsculas, o agrega antes un nodo **"Edit Fields"** que limpie espacios y ponga el texto en mayúsculas.
3. Verás dos salidas: **true** (es caliente) y **false** (no lo es).

---

### Paso 7: Envía la alerta por correo (10 min)

1. Desde la salida **true**, agrega un nodo **Gmail** → **"Send a message"**.
2. Conecta tu cuenta de Google.
3. Configura:
   - **To:** tu propio correo
   - **Subject:** `🔥 Lead caliente: {{ nombre }} de {{ empresa }}`
   - **Message:**
```
Tienes un nuevo lead caliente.

Nombre: {{ nombre }}
Empresa: {{ empresa }}
Email: {{ email }}
Necesidad: {{ necesidad }}

Contáctalo en las próximas 2 horas.
```
4. **Test step** y verifica que llegue el correo.

*(Opcional: en la salida false, no hagas nada o añade un correo de bienvenida genérico.)*

---

### Paso 8: Prueba el flujo completo y actívalo (10 min)

1. Haz clic en **"Execute workflow"** y envía el formulario con 3 leads de prueba.
2. Verifica en tu hoja que las clasificaciones sean razonables y que solo el lead caliente genere correo.
3. Cuando estés conforme, activa el interruptor **"Active"** (arriba a la derecha). Ahora el formulario usa su **Production URL**.
4. Comparte el enlace de producción del formulario o insértalo en tu web.

---

### Reto extra (opcional)

Elige uno:
- 🔹 Pide a la IA que, además de la categoría, genere **una frase de justificación** y guárdala en una columna nueva.
- 🔹 Para leads TIBIOS, envía un **correo automático** al prospecto con un recurso útil.
- 🔹 Agrega un nodo de **notificación por Telegram o Slack** además del correo.
- 🔹 Agrega un camino de error: si el nodo de IA falla, que te llegue un aviso.

### Solución de problemas frecuentes

| Problema | Posible causa | Solución |
|---|---|---|
| La IA responde con texto largo en vez de una palabra | Prompt poco estricto | Refuerza: "Responde ÚNICAMENTE con una palabra" |
| El nodo If nunca da *true* | La respuesta incluye espacios o minúsculas | Normaliza el texto o usa comparación sin distinguir mayúsculas |
| Error de credenciales en OpenAI | Sin saldo o key incorrecta | Revisa facturación y vuelve a copiar la key |
| Las expresiones aparecen vacías | Nombre de campo distinto | Arrastra el campo desde el panel INPUT |
| Google Sheets no encuentra la hoja | Permisos o nombre diferente | Reconecta la credencial y vuelve a seleccionar el documento |

---

## 5. Recursos adicionales

### Documentación y aprendizaje oficial
- **Documentación de N8N:** docs.n8n.io (busca la sección "Try it out" y "Advanced AI")
- **Plantillas de workflows de N8N:** n8n.io/workflows (miles de flujos gratuitos para importar y adaptar)
- **Canal de YouTube de N8N:** tutoriales paso a paso
- **Comunidad de N8N:** community.n8n.io (foro activo para resolver dudas)

### Alternativas para explorar
- **Make** (make.com): constructor visual, buena opción si prefieres otra interfaz
- **Zapier** (zapier.com): ideal para automatizaciones muy simples
- **Flowise / Voiceflow / Botpress:** para chatbots más avanzados

### Lecturas recomendadas
- Documentación sobre *prompt engineering* del proveedor de IA que uses (OpenAI, Anthropic, Google)
- Guías de protección de datos de tu país (ej.: Ley 1581 en Colombia, LFPDPPP en México, Ley 19.628 en Chile, LGPD en Brasil)

### Plantilla descargable sugerida (para el equipo del curso)
- **"Canvas MAPA":** una hoja con las 4 preguntas del método (Molestia, Activador, Pasos, Acción) para que el alumno diseñe sus propios flujos.

### Tarea de transferencia
Aplica el método MAPA a **un proceso de tu propio negocio** y dibuja el flujo en papel o en una herramienta como Excalidraw o Miro. Compártelo en el foro del curso para recibir retroalimentación.

---

## 6. Preguntas de autoevaluación

**Pregunta 1 (comprensión)**
¿Cuál es la principal diferencia entre una automatización tradicional y una automatización con IA? Da un ejemplo de una tarea de tu negocio que **no** podrías automatizar sin IA.

**Pregunta 2 (aplicación)**
Observa este flujo: *"Cuando llega un correo → la IA lo resume → se envía el resumen por Slack"*. Identifica cuál es el **trigger**, cuál es el **proceso** y cuál es la **acción**. ¿Qué paso añadirías para evitar que información sensible se envíe a un canal inadecuado?

**Pregunta 3 (criterio)**
Tu flujo de atención al cliente responde automáticamente y un día la IA le da a un cliente información incorrecta sobre tu política de devoluciones. ¿Qué **dos medidas** de diseño implementarías para reducir este riesgo en el futuro?

<details>
<summary><b>Ver respuestas orientativas</b></summary>

**R1:** La automatización tradicional sigue reglas fijas y maneja datos estructurados; la automatización con IA interpreta información no estructurada (texto libre, correos, audios) y puede tomar decisiones flexibles o generar contenido. Ejemplo válido: clasificar el tono de reseñas de clientes, o redactar respuestas personalizadas a correos.

**R2:** Trigger: llegada de un correo. Proceso: el resumen generado por IA. Acción: el envío a Slack. Medidas posibles: filtrar o excluir correos con datos sensibles antes del paso de IA, o enviar el resumen solo a un canal privado con acceso restringido.

**R3:** Algunas medidas válidas: (1) restringir a la IA para que responda solo con base en un documento oficial de políticas; (2) instruirla para escalar a un humano cuando no encuentre la respuesta; (3) agregar una revisión humana en casos sensibles; (4) registrar todas las conversaciones para auditarlas periódicamente.

</details>

---

### ✅ Checklist de cierre del módulo

- [ ] Entiendo la diferencia entre trigger, proceso y acción
- [ ] Construí y activé mi flujo de calificación de leads
- [ ] Probé el flujo con al menos 3 casos distintos
- [ ] Apliqué el método MAPA a un proceso real de mi negocio
- [ ] Configuré un límite de gasto en mi cuenta de IA

**Próximo módulo:** *Módulo 4: Agentes de IA: automatizaciones que razonan y actúan por ti.*