# Claude Opus 5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.72 | quality: 10.0
- latency_total: 195.145s | tokens_per_second: 74.2
- input_tokens: 388 | output_tokens: 14489
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

# Módulo 3: Automatización con IA — De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 4 horas (2h teoría + 2h práctica)
**Nivel:** Emprendedor no-técnico (no se requiere saber programar)

---

## 1. Objetivo del módulo

Al finalizar este módulo serás capaz de identificar tareas repetitivas en tu negocio que consumen tu tiempo (o el de tu equipo) y convertirlas en flujos de trabajo automatizados con inteligencia artificial, sin escribir código. Aprenderás la lógica detrás de cualquier automatización —disparador, procesamiento y acción—, conocerás las herramientas no-code más usadas en Latinoamérica (N8N, Make, Zapier) y construirás tu primer flujo funcional de punta a punta. El objetivo final no es técnico sino estratégico: que salgas con al menos un proceso de tu empresa automatizado y con un criterio claro para decidir **qué vale la pena automatizar y qué no**.

---

## 2. Contenido teórico

### 2.1 ¿Qué es realmente "automatizar con IA"?

Automatizar es hacer que una tarea ocurra **sin que alguien tenga que recordar hacerla**. Automatizar *con IA* agrega algo nuevo: la máquina ya no solo mueve datos de un lado a otro, ahora puede **interpretar, redactar, clasificar y decidir**.

| Automatización tradicional | Automatización con IA |
|---|---|
| "Cuando llegue un formulario, guárdalo en una hoja de cálculo" | "Cuando llegue un formulario, **lee el mensaje, clasifica la urgencia**, y guárdalo con una etiqueta" |
| Reglas fijas (si pasa X, haz Y) | Reglas + juicio (entiende contexto, texto libre, imágenes) |
| Falla si el input cambia de formato | Tolera input desordenado y humano |

**Ejemplo concreto:** antes, para responder un email necesitabas plantillas rígidas. Hoy, un flujo puede leer el email de un cliente enojado, entender que es un reclamo de envío, buscar el número de guía en tu base de datos y redactar una respuesta empática personalizada. Todo en 12 segundos.

### 2.2 La anatomía de todo flujo de trabajo

Absolutamente **toda** automatización, por compleja que parezca, tiene esta estructura de tres partes:

```
[ DISPARADOR ] ──> [ PROCESAMIENTO ] ──> [ ACCIÓN ]
   (Trigger)          (Lógica + IA)         (Output)
```

**1. Disparador (Trigger):** el evento que enciende el flujo.
- Llega un mensaje de WhatsApp
- Alguien llena un formulario
- Son las 8:00 AM del lunes (disparador por tiempo)
- Se agrega una fila nueva en Google Sheets

**2. Procesamiento:** lo que pasa en medio.
- Filtros ("solo si el monto es mayor a $500")
- Consultas a bases de datos
- **Nodo de IA**: aquí entra el modelo (GPT, Claude, Gemini) a leer, resumir, clasificar o redactar
- Condicionales ("si es urgente → camino A, si no → camino B")

**3. Acción:** el resultado visible.
- Enviar un email o mensaje
- Crear una tarjeta en Trello/Notion
- Publicar en redes sociales
- Notificar a tu equipo en Slack

> **Regla de oro del módulo:** si no puedes describir tu automatización en una frase con la forma *"Cuando pase ___, quiero que la IA ___, y entonces ___"*, todavía no está lista para construirse.

### 2.3 El panorama de herramientas

| Herramienta | Modelo de precio | Curva de aprendizaje | Ideal para |
|---|---|---|---|
| **N8N** | Gratis (self-hosted) / desde ~$20 USD cloud | Media | Startups que quieren control total y costos bajos a escala |
| **Make** (ex-Integromat) | Freemium, por operaciones | Baja-media | Flujos visuales complejos, buen balance |
| **Zapier** | Freemium, caro al escalar | Muy baja | Validar rápido, equipos sin tiempo |
| **Relevance AI / Flowise** | Freemium | Media | Agentes de IA especializados |

### 2.4 ¿Por qué N8N para este módulo?

N8N (se pronuncia "n-eight-n", de *nodemation*) es nuestra herramienta principal por cuatro razones muy prácticas para el contexto latinoamericano:

1. **Precio por ejecución vs. precio por tarea.** Zapier te cobra por cada paso ejecutado. N8N te cobra por *flujo completo ejecutado*. Un flujo de 15 pasos cuesta lo mismo que uno de 2. En volumen, la diferencia es de 10x o más.
2. **Puedes auto-hospedarlo gratis.** Si tienes un servidor de $5 USD/mes (DigitalOcean, Hetzner), N8N es ilimitado y gratuito. Esto es decisivo cuando facturas en pesos y pagas en dólares.
3. **Nodos de IA nativos.** Tiene integración directa con OpenAI, Anthropic, Google, bases vectoriales y un constructor de agentes. No necesitas conectores de terceros.
4. **No te deja encerrado.** Tus flujos son archivos JSON que puedes exportar, versionar y mover.

**Conceptos clave de N8N que usaremos:**

- **Nodo:** cada cajita del flujo. Hace una cosa.
- **Canvas:** el lienzo donde arrastras y conectas nodos.
- **Credencial:** la "llave" guardada de cada servicio (tu cuenta de Gmail, tu API key de OpenAI). Se configura una vez y se reutiliza.
- **Ejecución:** cada vez que el flujo corre. N8N guarda el historial, lo que te permite ver **exactamente dónde falló** algo.
- **Expresión:** la forma de referirse a datos de pasos anteriores. Se escribe `{{ $json.nombre_del_campo }}`.

### 2.5 El criterio de decisión: qué automatizar primero

No automatices por moda. Usa esta matriz:

|  | **Alta frecuencia** | **Baja frecuencia** |
|---|---|---|
| **Alto valor** | 🟢 **AUTOMATIZA YA** | 🟡 Documenta y delega |
| **Bajo valor** | 🟢 Automatiza (quick win) | 🔴 Elimina la tarea |

Y antes de construir, calcula el ROI con esta fórmula simple:

```
Horas ahorradas/mes × tu costo por hora = Ahorro mensual
Ahorro mensual − costo de herramientas = Beneficio neto
```

**Ejemplo real:** Responder 60 consultas repetidas de WhatsApp al mes = 5 horas. Si tu hora vale $15 USD, son $75/mes. La automatización cuesta $12/mes (N8N + API de IA). Beneficio neto: **$63/mes y 5 horas de tu vida de vuelta**.

> ⚠️ **Advertencia importante:** automatizar un proceso roto solo hace que se rompa más rápido. Si tu proceso de ventas no funciona manualmente, automatizarlo no lo arreglará.

---

## 3. Tres ejemplos prácticos de automatización para startups

### 📩 Ejemplo 1: Atención al cliente automatizada

**El problema:** El 70% de las consultas que recibes son las mismas 8 preguntas (precios, horarios, cómo comprar, estado de envío). Responderlas te roba el foco y además respondes lento fuera de horario.

**La frase del flujo:**
> *Cuando llegue un mensaje de un cliente, quiero que la IA lo lea, busque la respuesta en mi documentación, y responda — escalando a un humano si no sabe.*

**Diagrama del flujo:**

```
[WhatsApp/Email entrante]
        ↓
[Nodo IA: ¿Es consulta frecuente, reclamo o venta?]
        ↓
   ┌────┴────┬──────────┐
   ↓         ↓          ↓
[Frecuente] [Reclamo]  [Venta]
   ↓         ↓          ↓
[Busca en   [Notifica  [Crea lead
 base de     a soporte  en CRM +
 conocimiento] en Slack]  notifica
   ↓                      a ventas]
[IA redacta
 respuesta]
   ↓
[¿Confianza > 80%?]
   ↓ Sí        ↓ No
[Envía]    [Escala a humano]
```

**Nodos en N8N:**

| # | Nodo | Qué hace |
|---|---|---|
| 1 | Webhook / Gmail Trigger | Recibe el mensaje |
| 2 | OpenAI (Classify) | Clasifica en: `frecuente`, `reclamo`, `venta`, `otro` |
| 3 | Switch | Dirige a cada rama |
| 4 | Vector Store / Google Docs | Busca en tu FAQ, políticas, catálogo |
| 5 | AI Agent | Redacta respuesta usando SOLO esa info |
| 6 | IF | Evalúa confianza |
| 7 | Send Message / Slack | Responde o escala |

**Prompt sugerido para el nodo de IA:**

```
Eres el agente de soporte de [TU EMPRESA].

REGLAS ESTRICTAS:
1. Responde ÚNICAMENTE con información del CONTEXTO.
2. Si la respuesta no está en el contexto, responde
   exactamente: "ESCALAR_A_HUMANO".
3. Nunca inventes precios, plazos ni políticas.
4. Tono: cercano, claro, máximo 4 líneas. Tutea.
5. Si el cliente está molesto, reconoce la molestia
   antes de dar la solución.

CONTEXTO: {{ $json.documentacion }}
MENSAJE DEL CLIENTE: {{ $json.mensaje }}
```

**Métricas de éxito:**
- % de consultas resueltas sin humano (meta inicial: 50-60%)
- Tiempo de primera respuesta (de horas → segundos)
- Tasa de escalamiento innecesario (<10%)

**Errores comunes:**
- ❌ No poner la regla de "escalar si no sabe" → la IA inventa precios. **Desastroso.**
- ❌ No avisar al cliente que habla con un bot → genera desconfianza. Pon: *"Soy el asistente de X, si necesitas a una persona escribe HUMANO".*
- ❌ Dejar el flujo sin supervisión la primera semana. Revisa **todas** las respuestas los primeros 7 días.

---

### 📱 Ejemplo 2: Generación de contenido para redes sociales

**El problema:** Sabes que debes publicar consistentemente, pero cada post te toma 40 minutos entre pensar la idea, escribirla y adaptarla a cada red. Resultado: publicas 3 veces y abandonas.

**La frase del flujo:**
> *Cada lunes a las 7 AM, quiero que la IA tome un tema de mi banco de ideas, genere 3 versiones adaptadas a LinkedIn, Instagram y X, y me las deje listas para aprobar.*

**Diagrama del flujo:**

```
[Schedule: Lunes 7:00 AM]
        ↓
[Google Sheets: trae próxima idea pendiente]
        ↓
[Nodo IA: genera post para LinkedIn (tono profesional)]
        ↓
[Nodo IA: adapta a Instagram (más visual, emojis, CTA)]
        ↓
[Nodo IA: adapta a X (280 caracteres, punchy)]
        ↓
[Nodo IA: genera prompt de imagen] → [DALL·E / Ideogram]
        ↓
[Telegram/Slack: envía los 3 posts + imagen para APROBAR]
        ↓
[¿Aprobado?] → Sí → [Publica o programa en Buffer/Metricool]
              → No → [Vuelve a generar con feedback]
```

**El elemento clave: el "banco de ideas"**

Crea una Google Sheet con estas columnas:

| Tema | Ángulo | Audiencia | Estado | Fecha publicación |
|---|---|---|---|---|
| Errores al contratar al primer empleado | Lista de 3 errores que cometí yo | Fundadores early-stage | Pendiente | |
| Cómo calculamos nuestro precio | Transparencia de números | Clientes potenciales | Publicado | 2024-03-11 |

Esto resuelve el problema #1 de la IA para contenido: **sin dirección, genera genérico.**

**Prompt sugerido:**

```
Eres copywriter de [TU EMPRESA], que ayuda a
[AUDIENCIA] a [RESULTADO].

Voz de marca:
- Directo, sin jerga corporativa
- Hablamos de números y casos reales, no de teoría
- Nunca usamos: "desbloquea tu potencial", "el futuro es
  ahora", "en la era digital"
- Español neutro latinoamericano

TAREA: Escribe un post de LinkedIn sobre:
Tema: {{ $json.tema }}
Ángulo: {{ $json.angulo }}

ESTRUCTURA:
- Línea 1: gancho de máximo 10 palabras que genere tensión
- Cuerpo: 120-180 palabras, frases cortas, un salto de
  línea cada 1-2 frases
- Cierre: una pregunta abierta a la audiencia
- Sin hashtags en el cuerpo. 3 hashtags al final.

NO uses emojis en LinkedIn.
```

**Métricas de éxito:**
- Posts publicados por semana (consistencia > perfección)
- % de posts aprobados sin edición (si es <40%, mejora el prompt, no la IA)
- Tiempo invertido por post (meta: de 40 min → 5 min)

**Errores comunes:**
- ❌ **Publicar sin revisión humana.** La IA genera un dato falso, lo publicas, y ese screenshot vive para siempre. Siempre deja el paso de aprobación.
- ❌ No definir la "voz de marca" → todos tus posts suenan a LinkedIn genérico de 2019.
- ❌ Automatizar cantidad sin estrategia. 30 posts malos son peores que 4 buenos.

---

### 🎯 Ejemplo 3: Calificación automática de leads

**El problema:** Recibes 80 formularios al mes. Los atiendes por orden de llegada. El cliente que iba a pagarte $20.000 USD esperó 3 días mientras atendías a un estudiante haciendo una tarea.

**La frase del flujo:**
> *Cuando alguien llene el formulario, quiero que la IA investigue su empresa, le asigne un puntaje de 0 a 100, y si es alto me avise al teléfono inmediatamente.*

**Diagrama del flujo:**

```
[Formulario web / Typeform]
        ↓
[Enriquecimiento: busca dominio, tamaño de empresa, sector]
        ↓
[Nodo IA: califica según criterios ICP → score 0-100]
        ↓
[Switch por score]
    ↓           ↓            ↓
[80-100]     [50-79]       [0-49]
🔥 Caliente   🟡 Tibio      ❄️ Frío
    ↓           ↓            ↓
[WhatsApp a  [Secuencia   [Newsletter
 vendedor +   de email      + nurturing
 crea deal    educativo]    pasivo]
 en CRM +
 agenda link]
        ↓
[Todos → Registrar en CRM con score + razonamiento]
```

**Definir tu ICP (Perfil de Cliente Ideal) — paso obligatorio:**

Antes de escribir el prompt, completa esto:

```
SEÑALES POSITIVAS (suben el score):
- Empresa de 10-200 empleados
- Sector: e-commerce, servicios profesionales
- Problema declarado coincide con lo que resolvemos
- Rol: fundador, gerente, director (tiene presupuesto)
- Urgencia explícita ("necesitamos esto este mes")
- Email corporativo

SEÑALES NEGATIVAS (bajan el score):
- Estudiante / investigación académica
- Busca empleo, no cliente
- Pide algo que NO hacemos
- Email genérico sin empresa
- Competidor
```

**Prompt sugerido:**

```
Eres analista de ventas de [TU EMPRESA].
Vendemos [PRODUCTO] a [ICP]. Ticket promedio: [$X].

Califica este lead de 0 a 100 según nuestro ICP:

SEÑALES POSITIVAS: [pega tu lista]
SEÑALES NEGATIVAS: [pega tu lista]

DATOS DEL LEAD:
{{ JSON.stringify($json) }}

Responde SOLO con este JSON, sin texto adicional:
{
  "score": 0-100,
  "categoria": "caliente|tibio|frio",
  "razonamiento": "2 frases explicando el score",
  "senales_positivas": ["..."],
  "banderas_rojas": ["..."],
  "pregunta_clave": "la mejor pregunta para hacerle en
                     el primer contacto",
  "accion_sugerida": "..."
}
```

> 💡 **Tip técnico:** activa el modo "JSON Output" en el nodo de OpenAI/Anthropic. Garantiza que la respuesta sea JSON válido y no se rompa el flujo.

**Métricas de éxito:**
- Tiempo de respuesta a leads calientes (meta: <5 minutos — la probabilidad de conversión cae 80% después de 1 hora)
- Tasa de conversión de leads "calientes" vs "fríos" (si es similar, tu ICP está mal definido)
- % de leads mal calificados (revisa 20 manualmente cada mes)

**Errores comunes:**
- ❌ Descartar automáticamente los "fríos". Nunca borres: ponlos en nurturing. El estudiante de hoy es el gerente de 2027.
- ❌ No guardar el razonamiento de la IA → no puedes auditar ni mejorar el sistema.
- ❌ Confiar en el score sin calibrar. Las primeras 50 calificaciones revísalas tú y ajusta el prompt.

---

## 4. Ejercicio práctico paso a paso

### 🛠️ Tu primer flujo: "Clasificador y responder de consultas"

**Qué vas a construir:** un flujo que recibe una consulta por formulario, la clasifica con IA, la guarda en una hoja de cálculo y te notifica. Es el esqueleto del Ejemplo 1, simplificado para que lo termines hoy.

**Tiempo:** 60-90 minutos
**Costo:** $0 (todo en capas gratuitas)
**Requisitos previos:** una cuenta de Google. Nada más.

---

#### PARTE A — Preparación (15 min)

**Paso 1. Crea tu cuenta de N8N**

1. Ve a [n8n.io](https://n8n.io) → **Start free** (14 días de prueba cloud, sin tarjeta).
2. *Alternativa gratuita permanente:* si tienes algo de soltura técnica, usa Railway o Render con la plantilla de N8N. Pero para este ejercicio, **usa la nube**. No te traben en la instalación.

**Paso 2. Obtén tu API key de IA**

*Opción A — OpenAI:* [platform.openai.com](https://platform.openai.com) → API Keys → Create. Requiere cargar $5 USD mínimo (te durará meses para este uso).

*Opción B — Google Gemini (GRATIS):* [aistudio.google.com](https://aistudio.google.com) → Get API Key. Tiene capa gratuita generosa. **Recomendada si estás empezando.**

> 🔒 Copia la key en un gestor de contraseñas. Si se filtra, alguien gasta tu saldo.

**Paso 3. Crea la hoja de cálculo**

Nueva Google Sheet llamada `Consultas-Automatizadas`. En la fila 1, estos encabezados **exactos**:

```
A1: fecha
B1: nombre
C1: email
D1: mensaje
E1: categoria
F1: urgencia
G1: resumen
H1: respuesta_sugerida
```

---

#### PARTE B — Construir el flujo (40 min)

**Paso 4. Nodo 1 — El disparador**

1. En N8N: **+ Add workflow** → nómbralo `M3 - Clasificador de consultas`.
2. Clic en el `+` grande → busca **"On form submission"** (N8N Form Trigger).
3. Configura el formulario:
   - **Form Title:** `Contáctanos`
   - **Form Fields:**

| Field Name | Type | Required |
|---|---|---|
| `nombre` | Text | ✅ |
| `email` | Email | ✅ |
| `mensaje` | Textarea | ✅ |

4. Clic en **Execute step** → se abre una URL de formulario. Llénalo con un caso de prueba realista:

> **Nombre:** Laura Méndez
> **Email:** laura@tiendaandina.com
> **Mensaje:** Hola, compré hace 9 días y mi pedido #4471 sigue sin llegar. Necesito saber si me lo van a enviar o si me devuelven el dinero porque era un regalo para el sábado.

5. Vuelve a N8N. Deberías ver tus datos en el panel de output. ✅ **Checkpoint 1: tienes datos entrando.**

---

**Paso 5. Nodo 2 — El cerebro (IA)**

1. Clic en el `+` después del trigger → busca **"Google Gemini"** (o **"OpenAI"**) → acción **"Message a Model"**.
2. **Credential** → *Create new* → pega tu API key → Save.
3. **Model:** `gemini-2.0-flash` (o `gpt-4o-mini`).
4. En **Messages**, agrega un mensaje con Role = `User` y pega esto en Content:

```
Eres asistente de atención al cliente de una tienda online.

Analiza esta consulta y devuelve SOLO un objeto JSON,
sin bloques de código ni texto adicional:

{
  "categoria": "una de: envio, producto, pago, reclamo, otro",
  "urgencia": "una de: alta, media, baja",
  "resumen": "la consulta en una sola frase",
  "respuesta_sugerida": "respuesta empática de máximo 3
   frases, tuteando al cliente. Si no tienes el dato
   exacto, promete seguimiento con plazo concreto."
}

CONSULTA:
Nombre: {{ $json.nombre }}
Mensaje: {{ $json.mensaje }}
```

> 📌 **Cómo insertar las variables:** arrastra el campo desde el panel izquierdo (INPUT) hacia el texto, o escribe `{{ $json.nombre }}` manualmente. Si ves el valor real en gris debajo del campo, está bien conectado.

5. **Execute step.** Deberías recibir el JSON. ✅ **Checkpoint 2: la IA está respondiendo.**

---

**Paso 6. Nodo 3 — Limpiar la respuesta**

La IA a veces envuelve el JSON en ```` ```json ````. Vamos a limpiarlo.

1. Agrega un nodo **"Code"**.
2. **Mode:** `Run Once for All Items`.
3. Pega este código (cópialo tal cual, no necesitas entenderlo):

```javascript
const items = [];

for (const item of $input.all()) {
  // Obtener el texto de la respuesta de IA
  let texto = item.json.content?.parts?.[0]?.text
           ?? item.json.text
           ?? item.json.message?.content
           ?? '';

  // Quitar bloques de código markdown
  texto = texto.replace(/```json/gi, '')
               .replace(/```/g, '')
               .trim();

  let datos;
  try {
    datos = JSON.parse(texto);
  } catch (e) {
    datos = {
      categoria: 'otro',
      urgencia: 'media',
      resumen: 'No se pudo analizar automáticamente',
      respuesta_sugerida: 'REVISAR MANUALMENTE'
    };
  }

  items.push({ json: datos });
}

return items;
```

4. **Execute step.** Ahora deberías ver 4 campos limpios y separados. ✅ **Checkpoint 3: datos estructurados.**

---

**Paso 7. Nodo 4 — Guardar en Google Sheets**

1. Agrega nodo **"Google Sheets"** → acción **"Append Row in Sheet"**.
2. **Credential** → *Create new* → *Sign in with Google* → autoriza.
3. **Document:** selecciona `Consultas-Automatizadas`. **Sheet:** `Sheet1`.
4. **Mapping Column Mode:** `Map Each Column Manually`.
5. Mapea así:

| Columna | Valor a insertar |
|---|---|
| fecha | `{{ $now.format('yyyy-MM-dd HH:mm') }}` |
| nombre | `{{ $('On form submission').item.json.nombre }}` |
| email | `{{ $('On form submission').item.json.email }}` |
| mensaje | `{{ $('On form submission').item.json.mensaje }}` |
| categoria | `{{ $json.categoria }}` |
| urgencia | `{{ $json.urgencia }}` |
| resumen | `{{ $json.resumen }}` |
| respuesta_sugerida | `{{ $json.respuesta_sugerida }}` |

> 💡 **Por qué `$('On form submission')`:** los datos del formulario ya no están en el paso anterior. Esta sintaxis dice "ve a buscar el dato en ese nodo específico". Es el concepto más útil de N8N — memorízalo.

6. **Execute step** → revisa tu Google Sheet. ✅ **Checkpoint 4: fila creada.**

---

**Paso 8. Nodo 5 — Notificación solo si es urgente**

1. Agrega un nodo **"If"**.
2. Condición: **Value 1** = `{{ $('Code').item.json.urgencia }}` → **Operation** = `is equal to` (String) → **Value 2** = `alta`
3. De la salida **true**, agrega **"Gmail"** → *Send a message*:
   - **To:** tu propio email
   - **Subject:** `🔥 URGENTE: {{ $('Code').item.json.categoria }} - {{ $('On form submission').item.json.nombre }}`
   - **Message:**
     ```
     Consulta urgente recibida.

     Cliente: {{ $('On form submission').item.json.nombre }}
     Email: {{ $('On form submission').item.json.email }}

     Resumen: {{ $('Code').item.json.resumen }}

     Respuesta sugerida:
     {{ $('Code').item.json.respuesta_sugerida }}
     ```
4. Deja la salida **false** sin conectar (los casos no urgentes solo quedan en la hoja).

---

#### PARTE C — Probar y activar (20 min)

**Paso 9. Prueba con casos diversos**

Clic en **Execute workflow** y envía estos 4 casos por el formulario. Verifica qué hace el flujo con cada uno:

| # | Mensaje de prueba | Esperado |
|---|---|---|
| 1 | "¿Cuáles son sus horarios de atención?" | categoria: otro, urgencia: baja, **sin email** |
| 2 | "Me cobraron dos veces, exijo reembolso HOY" | categoria: pago/reclamo, urgencia: alta, **con email** 🔥 |
| 3 | "hola" | Debe manejarlo sin romperse |
| 4 | "El producto llegó roto y además era el color equivocado" | categoria: producto, urgencia: alta/media |

**Paso 10. Revisa el historial**

Ve a la pestaña **Executions**. Ahí ves cada corrida, con los datos exactos que pasaron por cada nodo. **Este es tu mejor amigo para depurar.** Si algo falla, el nodo aparece en rojo y puedes ver el error.

**Paso 11. Activa el flujo**

Toggle **Inactive → Active** (arriba a la derecha). Copia la URL de producción del formulario. Ya está vivo: ahora funciona 24/7 sin que tengas N8N abierto.

---

#### 🚀 Retos de extensión (elige 1)

| Reto | Dificultad | Qué agregar |
|---|---|---|
| **Responder automático** | ⭐ | Nodo Gmail después del Code que envíe la `respuesta_sugerida` al cliente |
| **Notificación por WhatsApp** | ⭐⭐ | Reemplaza Gmail por nodo HTTP Request a la API de WhatsApp Cloud |
| **Con base de conocimiento** | ⭐⭐⭐ | Antes del nodo IA, agrega Google Docs que traiga tu FAQ y pásalo como contexto |
| **Reporte semanal** | ⭐⭐ | Flujo nuevo: Schedule (lunes 8AM) → lee la Sheet → IA resume tendencias → email |

#### 🔧 Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| Nodo IA en rojo, error 401 | API key mal pegada | Recrea la credencial, sin espacios |
| Nodo IA en rojo, error 429 | Excediste cuota o sin saldo | Espera, o carga saldo / cambia a Gemini |
| Code devuelve "REVISAR MANUALMENTE" | La IA no devolvió JSON | Agrega al prompt: "Responde ÚNICAMENTE JSON válido" |
| Sheets: celdas vacías | Mala referencia de nodo | Verifica el nombre del nodo entre `$('...')` — debe ser idéntico |
| Sheets: columnas no aparecen | Encabezados no detectados | Vuelve a cargar la lista con el botón de refrescar |
| El formulario no dispara nada | Flujo inactivo | Activa el toggle y usa la URL de **producción**, no la de test |

---

## 5. Recursos adicionales

### Documentación esencial
- **[Documentación oficial N8N](https://docs.n8n.io)** — empieza por *Try it out → Quickstart*
- **[N8N Workflow Templates](https://n8n.io/workflows/)** — +2.000 flujos listos para importar. **Úsalos:** no construyas de cero, copia y adapta.
- **[Guía de expresiones de N8N](https://docs.n8n.io/code/expressions/)** — para dominar `{{ }}`

### Video y comunidad
- **Canal de YouTube de N8N** — serie "Beginner Course" (gratuita, ~2h)
- **[Foro de la comunidad N8N](https://community.n8n.io)** — respuestas en horas, muy activo
- **Comunidades en español:** busca "Automatización No-Code LATAM" en Discord/WhatsApp

### Para escribir mejores prompts
- **[Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)** — la mejor guía gratuita que existe
- **OpenAI Cookbook** — ejemplos de extracción estructurada

### Herramientas complementarias
| Necesidad | Herramienta | Nota |
|---|---|---|
| Hospedar N8N barato | Hetzner / DigitalOcean | $5-6 USD/mes |
| Base de datos sin código | Airtable / Baserow | Baserow tiene versión gratis self-hosted |
| Programar redes | Metricool / Buffer | Metricool tiene mejor soporte LATAM |
| CRM gratuito con API | HubSpot Free / Twenty | |
| WhatsApp API | Meta Cloud API / Wati | Cloud API: 1.000 conversaciones gratis/mes |
| Calcular costos de IA | [tokencost.com](https://tokencost.com) | Estima antes de escalar |

### Plantillas descargables del módulo
1. **Matriz de priorización de automatizaciones** (Sheets)
2. **Calculadora de ROI de automatización** (Sheets)
3. **Biblioteca de prompts** para los 3 casos del módulo
4. **JSON del ejercicio completo** — importable en N8N

### Lectura recomendada
- *The E-Myth Revisited*, Michael Gerber — por qué sistematizar antes que escalar
- *Build* (capítulos sobre procesos), Tony Fadell

---

## 6. Preguntas de autoevaluación

### Pregunta 1 — Comprensión conceptual

Tu amigo te dice: *"Instalé N8N y conecté la IA, pero mi automatización de ventas sigue sin traer clientes. La IA no sirve."*

Explica en 3-4 frases **por qué el diagnóstico de tu amigo probablemente está equivocado**, usando el concepto de "automatizar un proceso roto" del módulo. Luego, propón las dos preguntas que le harías antes de tocar un solo nodo.

<details>
<summary>💡 Ver guía de respuesta</summary>

**Puntos clave esperados:**
- La automatización **amplifica** un proceso existente, no lo crea. Si el proceso de ventas no convertía manualmente (mal ICP, oferta poco clara, mensaje que no conecta), automatizarlo solo genera más contactos malos, más rápido.
- La IA ejecuta la lógica que le diste; si la lógica estaba mal, el output será malo con alta eficiencia.
- El problema es de **estrategia comercial**, no de herramienta.

**Preguntas sugeridas:**
1. *"¿Cuántos clientes cerraste haciendo esto a mano, y de cuántos intentos?"* → si nunca funcionó manual, el problema es la oferta.
2. *"¿Tienes definido tu ICP por escrito?"* → sin criterio, la IA califica al azar.
3. *(Bonus)* "¿Revisaste el historial de ejecuciones? ¿El flujo técnicamente corre bien?" → separa falla técnica de falla estratégica.
</details>

---

### Pregunta 2 — Aplicación técnica

Observa este flujo que un emprendedor construyó para atención al cliente:

```
[Email entrante] → [Nodo IA: redacta respuesta] → [Enviar email al cliente]
```

Identifica **tres riesgos concretos** de este diseño y para cada uno indica **qué nodo o instrucción agregarías** para mitigarlo. Sé específico (nombra el tipo de nodo de N8N).

<details>
<summary>💡 Ver guía de respuesta</summary>

**Riesgos y mitigaciones esperadas (cualquier 3 bien argumentadas):**

| Riesgo | Mitigación |
|---|---|
| **La IA inventa información** (precios, plazos, políticas que no existen) | Agregar nodo de base de conocimiento (Google Docs / Vector Store) **antes** del nodo IA + instrucción en el prompt: "responde solo con el contexto; si no está, devuelve ESCALAR_A_HUMANO" |
| **Cero control humano** — cualquier respuesta sale directo al cliente | Nodo **IF** que evalúe confianza/categoría, o un paso de aprobación por Slack/Telegram antes de enviar |
| **No distingue tipos de consulta** — trata igual una pregunta de horario y una amenaza legal | Nodo IA de clasificación + nodo **Switch** para rutear por categoría |
| **No registra nada** — no hay datos para auditar ni mejorar | Nodo **Google Sheets / Airtable** (Append Row) que guarde input, output y razonamiento |
| **Sin manejo de errores** — si la API de IA falla, el cliente nunca recibe respuesta | Configurar *Error Workflow* o *Continue On Fail* + rama de notificación al equipo |
| **El cliente no sabe que es un bot** | Instrucción en el prompt para identificarse + opción de escalar ("escribe HUMANO") |
</details>

---

### Pregunta 3 — Decisión estratégica

Eres fundador de una agencia de 4 personas. Tienes presupuesto para automatizar **un solo** proceso este mes. Estos son tus candidatos:

| Proceso | Frecuencia | Tiempo por vez | Quién lo hace |
|---|---|---|---|
| **A.** Armar propuestas comerciales | 6 veces/mes | 90 min | Tú (fundador) |
| **B.** Responder dudas de clientes por WhatsApp | 100 veces/mes | 4 min | Asistente |
| **C.** Cerrar la facturación mensual | 1 vez/mes | 4 horas | Administradora |

Usando la **matriz de priorización** y la **fórmula de ROI** del módulo:

1. Calcula las horas mensuales que consume cada proceso.
2. Clasifica cada uno en la matriz (frecuencia / valor).
3. Elige **uno** y justifica por qué, mencionando al menos un riesgo de tu elección.

<details>
<summary>💡 Ver guía de respuesta</summary>

**1. Horas mensuales:**
- A: 6 × 90 min = **9 h/mes**
- B: 100 × 4 min = **6,7 h/mes**
- C: 1 × 4 h = **4 h/mes**

**2. Clasificación:**
- **A:** frecuencia media, **valor alto** (impacta ingresos directamente y consume tiempo del fundador, el recurso más caro) → zona verde
- **B:** **frecuencia muy alta**, valor medio (impacta satisfacción, tarea muy repetitiva y estandarizable) → zona verde, quick win
- **C:** **baja frecuencia**, alto valor pero poco repetible; además la facturación tiene implicaciones legales/fiscales → zona amarilla: documentar/delegar o usar software contable, no automatización a medida

**3. Respuestas defendibles (ambas correctas si están bien argumentadas):**

*Opción B (la más recomendable para un primer proyecto):*
- Mayor volumen = la IA aprende sobre más casos y el ROI se nota rápido
- Tarea muy estandarizable (las mismas preguntas se repiten)
- Baja complejidad técnica → alta probabilidad de terminarlo este mes
- Mejora el tiempo de respuesta, lo que impacta retención
- **Riesgo:** la IA puede dar información incorrecta a clientes reales → mitigar con base de conocimiento cerrada, regla de escalamiento y revisión humana la primera semana

*Opción A (defendible si el cuello de botella es el fundador):*
- Libera 9 h del recurso más caro de la empresa
- Impacto directo en ventas: propuestas más rápidas = más cierres
- **Riesgo:** una propuesta mal generada puede costar un cliente grande → debe mantener aprobación humana obligatoria; automatizar el *borrador*, no el envío

*Elegir C debería marcarse como débil:* baja frecuencia, alto riesgo de error con consecuencias fiscales, y probablemente se resuelve mejor con un software contable existente que con una automatización propia.
</details>

---

## ✅ Checklist de cierre del módulo

Antes de pasar al Módulo 4, confirma que:

- [ ] Tengo cuenta activa en N8N y una API key de IA funcionando
- [ ] Completé el ejercicio práctico y mi flujo está **activo**
- [ ] Probé el flujo con al menos 4 casos distintos, incluyendo uno "raro"
- [ ] Llené la matriz de priorización con los procesos reales de **mi** negocio
- [ ] Identifiqué mi próxima automatización y escribí su frase: *"Cuando pase ___, quiero que la IA ___, y entonces ___"*
- [ ] Respondí las 3 preguntas de autoevaluación

---

> **Próximo módulo —** *Módulo 4: Agentes de IA: cuando la automatización toma decisiones*
> Pasaremos de flujos lineales (A→B→C) a agentes que eligen qué herramienta usar según el contexto. Construiremos un asistente que consulta tu CRM, tu calendario y tu base de conocimiento por su cuenta.