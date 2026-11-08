# Fugu Max — startup_content/curso_emprendimiento_modulo

- model_id: `sakana/fugu-max`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 30.098s | tokens_per_second: 216.0
- input_tokens: 363 | output_tokens: 6501
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

# Módulo 3 — Automatización con IA: De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Nivel:** Emprendedor no-técnico (no necesitas saber programar)
**Duración estimada:** 3 horas (2 h de lectura y ejemplos + 1 h de ejercicio práctico)
**Requisitos:** Haber completado el Módulo 1 (fundamentos de IA) y el Módulo 2 (prompts efectivos). Una computadora con navegador e internet.

---

## 1. Objetivo del módulo

Al terminar este módulo, vas a poder identificar qué tareas repetitivas de tu negocio se pueden automatizar con inteligencia artificial, diseñar el flujo de trabajo correspondiente en papel y construir tu primera automatización funcional usando una herramienta visual como n8n, sin escribir código. El objetivo no es que te conviertas en experto en automatización, sino que salgas con **un flujo real de tu negocio funcionando de punta a punta** —por ejemplo, un asistente que responde consultas, califica leads y los registra en una hoja de cálculo— y que puedas replicar el proceso para otras áreas: contenido, ventas, operaciones o finanzas.

---

## 2. Contenido teórico

### 2.1 ¿Qué significa "automatizar con IA"?

Automatizar es hacer que una tarea ocurra **sola**, disparada por un evento, sin que tengas que ejecutarla manualmente. La IA agrega una capa nueva: no solo automatiza el *movimiento* de datos, sino también la **interpretación**.

Comparación rápida:

| | Automatización tradicional | Automatización con IA |
|---|---|---|
| Qué hace | "Si pasa X, haz Y" | "Si pasa X, **entiende** qué significa y decide cómo responder" |
| Ejemplo | Enviar un email de bienvenida cuando alguien se registra | Leer el email de respuesta del cliente, entender si está interesado o molesto, y etiquetarlo |
| Limitación | Solo funciona con reglas fijas | Maneja texto libre, ambigüedad y casos no previstos |
| Riesgo | Bajo (hace siempre lo mismo) | Medio (puede equivocarse; requiere revisión humana) |

Un ejemplo concreto de tu negocio: si usas un formulario de contacto, la automatización tradicional solo puede mandarte un correo. Una automatización con IA puede leer el mensaje, clasificarlo como *consulta de precio*, *soporte* o *spam*, detectar si el prospecto es un cliente prioritario y redactarte una respuesta borrador lista para enviar.

### 2.2 La anatomía de un flujo de trabajo

Todo flujo automatizado, por complejo que parezca, tiene cuatro piezas. Apréndetelas y ya sabes diseñar:

1. **Disparador (trigger):** el evento que inicia el flujo. Puede ser un mensaje de WhatsApp/Telegram, un formulario enviado, un correo recibido, una fila nueva en Google Sheets o una hora del día (ej. todos los lunes a las 9 a.m.).
2. **Pasos de proceso:** las acciones. Aquí vive la IA: *resumir, clasificar, redactar, extraer datos, traducir, responder*.
3. **Condiciones (lógica):** "si el lead es caliente, avísame por Telegram; si no, solo guárdalo en la hoja".
4. **Salida:** dónde queda el resultado. Un mensaje, una fila en Sheets, una tarjeta en Notion, un correo o una tarea en tu CRM.

> **Regla de oro:** si no puedes dibujar el proceso en un diagrama de cajas con flechas en una servilleta, todavía no está listo para automatizar.

### 2.3 n8n y el mapa de herramientas

**n8n** es una herramienta de automatización visual: arrastras nodos (cajitas) a un lienzo y los conectas con flechas. Cada nodo es un paso: "recibir mensaje de Telegram", "consultar a un modelo de IA", "escribir en Google Sheets". Tiene una ventaja clave para emprendedores: puedes empezar con una **prueba gratuita en la nube** o **autoalojarlo sin costo** si tienes apoyo técnico, y sus flujos son muy flexibles.

Alternativas que conviene conocer:

| Herramienta | Fortaleza | Ideal si... |
|---|---|---|
| **n8n** | Muy flexible, buena integración con IA, opción gratuita autoalojada | Quieres control y no temes una curva de aprendizaje media |
| **Make.com** | Interfaz muy visual, buen plan gratuito (≈1.000 operaciones/mes) | Es tu primera automatización y quieres algo amigable |
| **Zapier** | El más simple, muchísimas integraciones, plan gratuito limitado | Automatizas procesos sencillos entre apps conocidas |
| **Google Apps Script + API de IA** | Gratis, vive dentro de Google Workspace | Tienes una base técnica o un aliado que la tenga |

> **Nota de costos para LATAM:** los precios están en dólares y se cobran con tarjeta internacional. Antes de escalar, calcula cuántas ejecuciones al mes necesitas de verdad. Casi siempre el plan gratuito alcanza para validar la idea; paga solo cuando el flujo ya te esté ahorrando horas reales.

### 2.4 El prompt es parte del flujo

En automatización, el prompt deja de ser una conversación y se vuelve una **instrucción fija de producción**. Debe incluir: rol, tarea, contexto del negocio, formato de salida (idealmente JSON) y qué hacer si no sabe la respuesta. Un prompt dentro de un flujo debe ser **predecible**, no creativo.

### 2.5 Buenas prácticas y errores comunes

**Haz esto:**
- Empieza por el proceso que **más tiempo te quita** y es más repetitivo, no por el más emocionante.
- Deja siempre un **humano en el circuito** al inicio (que la IA redacte, tú apruebes).
- Agrega un paso de **registro** (log en Sheets): sin datos no puedes mejorar el flujo.
- Prueba con **casos raros**: el cliente que escribe en mayúsculas, el que manda un audio, el que pregunta algo fuera de tu catálogo.

**Evita esto:**
- Automatizar un proceso que **aún no funciona manualmente** (automatizar el caos produce caos más rápido).
- Darle a la IA acceso a decisiones irreversibles (reembolsos, cancelaciones, precios).
- Olvidar el manejo de errores: ¿qué pasa si la API falla o si el modelo responde algo vacío?

---

## 3. Tres ejemplos prácticos de automatización para startups

### Ejemplo A — Atención al cliente automatizada (primer nivel)

**Problema:** recibes 40 mensajes diarios con las mismas 8 preguntas (precio, horarios, envíos, formas de pago). Responder te toma 1,5 horas al día.

**Flujo:**

```
[Cliente escribe por Telegram/WhatsApp]
        ↓
[Disparador: mensaje entrante]
        ↓
[IA: clasifica la intención + responde usando tu base de conocimiento]
        ↓
   ┌────┴────┐
   │         │
[Responde]  [No está seguro] → [Avisa a humano + registra para revisión]
   ↓
[Registra la conversación en Google Sheets]
```

**Prompt base del nodo de IA:**

```text
Eres el asistente de atención de [NOMBRE DEL NEGOCIO], una [categoría]
que vende [productos]. Responde en español neutro, cálido y breve
(máximo 4 líneas).

BASE DE CONOCIMIENTO:
- Precios: [lista]
- Horarios: [lista]
- Envíos: [política]
- Formas de pago: [lista]

REGLAS:
- Si la pregunta está en la base, responde con ese dato.
- Si no está, responde: "Déjame confirmarlo con el equipo y te escribo
  en un rato" y marca requiere_humano = true.
- Nunca inventes precios ni promociones.

Devuelve SOLO este JSON:
{"respuesta": "...", "intencion": "...", "requiere_humano": true/false}
```

**Impacto típico:** 60–80 % de las consultas resueltas sin intervención; el equipo solo atiende casos complejos.
**Métrica a medir:** % de conversaciones cerradas sin humano y tiempo de primera respuesta.

---

### Ejemplo B — Generación de contenido para redes sociales

**Problema:** sabes que deberías publicar 4 veces por semana, pero entre operar el negocio y crear contenido, terminas publicando una vez cada dos semanas.

**Flujo:**

```
[Disparador: lunes 8:00 a.m. (cron)]
        ↓
[IA: genera 5 ideas de post a partir de tu "banco de temas"]
        ↓
[IA: redacta copy + hashtags + guion visual para cada idea]
        ↓
[Escribe las propuestas en Google Sheets o Notion con estado "Pendiente"]
        ↓
[Notificación a Telegram: "Tienes 5 posts listos para revisar"]
        ↓
[TÚ apruebas/editas] → [Publicación]
```

**Truco clave:** alimenta el flujo con un **banco de temas y un documento de voz de marca** (cómo hablas, qué palabras usas, qué palabras evitas). Sin eso, el contenido sale genérico. Con eso, suena a ti.

**Prompt de ejemplo (extracto):**

```text
Actúa como community manager de [NEGOCIO].
Voz de marca: cercana, directa, sin tecnicismos, tuteo.
Público: emprendedores de 25-40 años en LATAM.
A partir del tema "{tema}", genera:
1) Un hook de 1 línea que detenga el scroll.
2) Copy de 60-90 palabras con un llamado a la acción.
3) 5 hashtags relevantes en español.
4) Sugerencia visual en 1 línea.
```

**Impacto típico:** de 3 horas semanales creando contenido a 30 minutos de edición y aprobación.
**Regla:** la IA produce el **borrador**, tú produces el **criterio**. Nunca publiques sin revisar.

---

### Ejemplo C — Calificación automática de leads

**Problema:** llegan 100 leads al mes por formulario y los revisas "cuando puedes". Los buenos se enfrían esperando.

**Flujo:**

```
[Disparador: nueva respuesta en formulario / Google Sheets]
        ↓
[IA: extrae datos (nombre, empresa, necesidad, presupuesto, urgencia)]
        ↓
[IA: asigna puntaje 1-10 y categoría: CALIENTE / TIBIO / FRÍO]
        ↓
   ┌────┴─────────┐
   │              │
[CALIENTE]    [TIBIO/FRÍO]
   ↓              ↓
[Alerta inmediata  [Secuencia de nurturing
 por Telegram/Slack] o solo registro]
   ↓
[Escribe todo en Google Sheets / CRM]
```

**Criterios que le das a la IA (esto es lo importante):**

```text
Puntúa el lead de 1 a 10 con esta rúbrica:
+3 si menciona presupuesto o pide cotización formal
+3 si describe una necesidad concreta y urgente
+2 si es una empresa (no persona natural) o tiene equipo
+2 si el mensaje incluye detalles específicos (volumen, plazos, uso)
-3 si es spam, consulta genérica o "solo estoy mirando"

Categoría: 8-10 = CALIENTE, 5-7 = TIBIO, 1-4 = FRÍO.
Devuelve JSON: {"puntaje": n, "categoria": "...", "razon": "...",
"datos_extraidos": {...}}
```

**Impacto típico:** tiempo de respuesta a leads calientes baja de días a minutos; el equipo comercial deja de perder tiempo en contactos irrelevantes.
**Advertencia:** la IA **prioriza**, no **descarta**. Un lead "frío" hoy puede ser tu mejor cliente en seis meses.

---

## 4. Ejercicio práctico paso a paso

### Construye tu "Recepcionista IA": responde, califica y registra

**Qué vas a lograr:** un flujo en n8n que recibe mensajes de Telegram, responde con IA usando *tu* información de negocio, clasifica al prospecto y guarda todo en Google Sheets.

**Tiempo:** 60–90 minutos. **Costo:** $0 si usas planes gratuitos/pruebas.

---

#### Paso 0 — Diseña en papel (15 min) ✍️

Antes de tocar la computadora, responde:

- [ ] ¿Cuáles son las **5 preguntas más frecuentes** que te hacen? Escríbelas con tu respuesta exacta.
- [ ] ¿Qué hace a un prospecto **caliente** para ti? Escribe 3 señales concretas.
- [ ] ¿Dónde quieres que quede el registro? (recomendado: Google Sheets)
- [ ] ¿A dónde quieres que llegue la alerta cuando alguien es caliente? (Telegram es lo más rápido)

Guarda esto en un documento: será tu **base de conocimiento** y tu **rúbrica**.

---

#### Paso 1 — Prepara las cuentas (15 min)

1. Crea una cuenta en **n8n** (n8n.cloud, prueba gratuita) o usa una instancia autoalojada si tienes apoyo técnico.
2. Consigue una **API key de un modelo de IA** (OpenAI, Google Gemini, Anthropic u otro proveedor). Guárdala en un lugar seguro — es como la contraseña de tu cuenta bancaria.
3. Ten a mano tu **Google Sheets** con estas columnas en la fila 1:
   `fecha | nombre | usuario | mensaje | respuesta | intencion | categoria | requiere_humano`

---

#### Paso 2 — Crea tu bot de Telegram (5 min)

1. Abre Telegram y busca **@BotFather**.
2. Escribe `/newbot`, elige un nombre y un usuario terminado en `bot`.
3. Copia el **token** que te entrega (una cadena larga). No lo compartas.

---

#### Paso 3 — Arma el flujo en n8n (25 min)

Agrega los nodos en este orden y conéctalos:

1. **Telegram Trigger** → evento: *On Message*.
   - Crea la credencial pegando el token del Paso 2.
2. **AI / LLM node** (o *HTTP Request* a la API del modelo).
   - Crea la credencial con tu API key.
   - Pega tu prompt, adaptando esta plantilla:

```text
Eres el asistente de [TU NEGOCIO], que vende [PRODUCTO/SERVICIO].
Responde en español, tono cercano, máximo 4 líneas.

INFORMACIÓN OFICIAL:
1. [Pregunta] → [Respuesta]
2. [Pregunta] → [Respuesta]
3. [Pregunta] → [Respuesta]
4. [Pregunta] → [Respuesta]
5. [Pregunta] → [Respuesta]

RÚBRICA DE CALIFICACIÓN:
+3 [señal 1] / +3 [señal 2] / +2 [señal 3] / +2 [señal 4]
Categoría: 8-10 CALIENTE · 5-7 TIBIO · 1-4 FRÍO

Si la pregunta no está en la información oficial, responde
"Déjame confirmarlo con el equipo" y marca requiere_humano = true.

Mensaje del cliente: {{ $json.message.text }}

Devuelve SOLO JSON:
{"respuesta":"...","intencion":"...","categoria":"...","puntaje":n,"requiere_humano":false}
```

3. **Telegram (Send Message)** → envía `{{ $json.respuesta }}` al mismo chat.
4. **Google Sheets (Append Row)** → mapea cada campo del JSON a su columna.
5. **(Opcional) IF + Telegram** → si `categoria = CALIENTE`, mándate un mensaje a ti mismo con los datos del prospecto.

---

#### Paso 4 — Prueba con casos reales (15 min)

Ejecuta el flujo manualmente ("Execute Workflow") y prueba **5 mensajes distintos**:

| Prueba | Mensaje de ejemplo | Resultado esperado |
|---|---|---|
| 1 | "Hola, ¿cuánto cuesta el plan básico?" | Respuesta correcta + categoría |
| 2 | "Necesito 50 unidades para mi empresa, urgente, ¿me cotizas?" | CALIENTE + alerta |
| 3 | "asdkjaskdj" | No rompe el flujo |
| 4 | "¿Tienen descuentos para ONGs?" (no está en tu base) | "Déjame confirmarlo" + requiere_humano = true |
| 5 | "¿Hacen envíos a Chile?" | Respuesta desde tu base de conocimiento |

Si algo falla, revisa en este orden: **¿el disparador recibió el dato? → ¿el prompt tiene la información? → ¿el formato JSON salió bien? → ¿el mapeo a Sheets está correcto?**

---

#### Paso 5 — Activa y monitorea (10 min)

1. Cambia el flujo a **Active**.
2. Escríbele a tu bot como si fueras un cliente.
3. Revisa que la fila aparezca en Google Sheets.
4. Define una rutina: **revisar el log 10 minutos al día durante la primera semana**. Anota cada respuesta mala y mejora el prompt.

---

### Checklist de entrega

- [ ] El bot responde al menos 5 preguntas frecuentes correctamente
- [ ] Los leads se clasifican en CALIENTE / TIBIO / FRÍO
- [ ] Cada conversación queda registrada en Google Sheets
- [ ] Recibes alerta cuando un lead es CALIENTE
- [ ] Probaste al menos un caso "raro" sin que el flujo se rompiera

**Entregable del módulo:** captura de pantalla del flujo funcionando + el enlace a tu hoja de registro con al menos 5 conversaciones.

---

## 5. Recursos adicionales

**Documentación y aprendizaje**
- Documentación oficial de n8n (en español parcial): `docs.n8n.io`
- Plantillas de flujos listos para copiar dentro de n8n (sección *Templates*) — busca "customer support", "lead scoring", "content generator"
- Documentación de la API del modelo que elijas (OpenAI, Google AI Studio, Anthropic): ahí están los límites de uso y precios
- Guía de BotFather para bots de Telegram: `core.telegram.org/bots`

**Herramientas complementarias**
- **Make.com** y **Zapier**: alternativas más simples si n8n te resulta complejo al inicio
- **Google Sheets**: tu "base de datos" gratuita para validar cualquier flujo
- **Notion / Airtable**: si prefieres ver los leads como tablero en lugar de filas

**Lectura recomendada**
- Concepto de "human in the loop": por qué siempre debe haber una persona aprobando al inicio
- Buenas prácticas de prompts para producción: instrucciones fijas, formato JSON, manejo de "no sé"
- Plantilla de *prompt library*: guarda todos tus prompts en un documento versionado con fecha y resultado

**Comunidad**
- Foro oficial de n8n y su Discord (hay mucha gente resolviendo dudas concretas)
- Grupos locales de no-code / automatización en tu ciudad o país: suelen hacer sesiones de "construye conmigo"

---

## 6. Preguntas de autoevaluación

**1. Un emprendedor quiere automatizar la respuesta a los mensajes de Instagram de su tienda de café. Antes de abrir n8n, ¿qué debería tener listo y por qué?**
> Debería tener mapeado el proceso: las preguntas frecuentes con sus respuestas oficiales, la definición de qué consulta requiere intervención humana y el destino del registro. Razón: automatizar un proceso que no está claro solo acelera la confusión; la IA necesita una base de conocimiento y reglas explícitas para responder bien.

**2. ¿Cuál es la diferencia entre automatización tradicional y automatización con IA, y qué riesgo adicional introduce esta última?**
> La tradicional ejecuta reglas fijas ("si pasa X, haz Y") y solo mueve datos; la IA además *interpreta* texto libre y decide. El riesgo adicional es el error de criterio: el modelo puede clasificar mal, inventar un dato o responder algo inapropiado, por lo que requiere validación humana, instrucciones claras y pruebas con casos límite.

**3. Tienes un flujo que califica leads de 1 a 10. Un lunes, un lead obtiene 3 puntos (FRÍO) pero escribe pidiendo una cotización para 200 unidades. ¿Qué harías con el flujo?**
> Revisaría el log y la respuesta del modelo, ajustaría la rúbrica de puntuación (probablemente el criterio de "volumen" no estaba bien ponderado o el modelo no lo detectó) y volvería a probar con casos similares. Además, mantendría la regla de que la IA *prioriza* pero no *descarta*: los leads fríos deben seguir recibiendo seguimiento, solo que con menor urgencia.

---

### Respuestas sugeridas

1. Mapeo del proceso + base de conocimiento + reglas de escalamiento + registro. Sin eso, el flujo produce errores rápidos y consistentes.
2. Reglas fijas vs. interpretación. El riesgo es el error de criterio y la necesidad de supervisión humana.
3. Revisar → ajustar rúbrica/prompt → re-probar → mantener seguimiento para todos los leads.

---

> **Antes de pasar al Módulo 4:** deja tu flujo corriendo una semana completa y anota cuántas horas te ahorró y en qué casos falló. Ese registro será la base de tu caso de negocio para escalar la automatización.