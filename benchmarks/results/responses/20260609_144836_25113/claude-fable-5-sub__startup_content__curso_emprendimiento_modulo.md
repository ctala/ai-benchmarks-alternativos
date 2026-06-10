# Claude Fable 5 (suscripción) — startup_content/curso_emprendimiento_modulo

- model_id: `claude-fable-5`
- success: True  | final: 7.29 | quality: 10.0
- latency_total: 90.403s | tokens_per_second: 72.0
- input_tokens: 2 | output_tokens: 6509

## Respuesta completa

# Módulo 3 — Automatización con IA: De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 2.5 horas (1 hora teoría + 1.5 horas práctica)
**Nivel:** Emprendedor no-técnico (no necesitas saber programar)

---

## 1. Objetivo del módulo

Al terminar este módulo serás capaz de identificar qué tareas repetitivas de tu negocio puedes automatizar con IA, y construirás tu primer flujo de trabajo funcional usando n8n sin escribir una línea de código. El objetivo no es que aprendas tecnología por aprender: es que recuperes horas de tu semana. Si hoy dedicas 10 horas semanales a responder correos, publicar en redes y revisar leads, al final de este módulo tendrás un plan concreto para reducir eso a 2-3 horas de supervisión.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar con IA?

Una automatización tradicional sigue reglas fijas: "si llega un correo con la palabra 'factura', muévelo a la carpeta Facturas". Es útil, pero rígida.

La automatización **con IA** agrega una capa de comprensión: el sistema puede leer el correo, entender de qué trata aunque no contenga palabras exactas, redactar una respuesta y decidir si necesita intervención humana.

La fórmula que vas a usar todo el módulo:

```
DISPARADOR → PROCESAMIENTO CON IA → ACCIÓN
```

| Componente | Qué es | Ejemplo |
|---|---|---|
| **Disparador** | El evento que inicia el flujo | Llega un correo, alguien llena un formulario, son las 9:00 AM |
| **Procesamiento IA** | Lo que la IA hace con la información | Clasificar, resumir, redactar, extraer datos, puntuar |
| **Acción** | El resultado en el mundo real | Enviar respuesta, publicar post, actualizar tu CRM, avisarte por WhatsApp |

### 2.2 Qué automatizar (y qué NO)

**Regla práctica:** automatiza tareas que cumplen las 3 condiciones:

1. **Repetitivas** — las haces más de 3 veces por semana
2. **Con patrón claro** — podrías explicarle a un practicante cómo hacerlas en 15 minutos
3. **De bajo riesgo si fallan** — un error no destruye una relación con un cliente clave

**NO automatices (todavía):** negociaciones, decisiones estratégicas, conversaciones con clientes enojados, nada legal o financiero sin revisión humana.

**Principio del "humano en el circuito":** en tus primeras automatizaciones, la IA *prepara* y tú *apruebas*. Cuando confíes en los resultados (después de 2-4 semanas de revisión), dejas que algunas acciones corran solas.

### 2.3 La herramienta: n8n

Existen varias plataformas de automatización (Zapier, Make, n8n). En este curso usamos **n8n** por tres razones:

| Criterio | n8n | Zapier |
|---|---|---|
| Costo inicial | Gratis (auto-alojado) o ~$24/mes en la nube | Desde $30/mes y escala rápido con el volumen |
| Flexibilidad con IA | Nodos nativos para OpenAI, Anthropic, agentes IA | Más limitado en flujos complejos |
| Tus datos | Pueden quedarse en tu servidor | Pasan por servidores de terceros |

**Cómo se ve n8n:** es un lienzo visual donde conectas cajas (llamadas "nodos"). Cada nodo hace una cosa: recibir un correo, llamar a ChatGPT, enviar un mensaje. Las conectas con flechas y eso es tu flujo. Arrastrar, soltar, configurar. Sin código.

**Vocabulario mínimo que necesitas:**

- **Nodo:** una caja que hace una acción (ej. "leer Gmail")
- **Workflow (flujo):** la cadena completa de nodos conectados
- **Trigger (disparador):** el primer nodo, el que inicia todo
- **Credencial:** la "llave" que conecta n8n con tus cuentas (Gmail, WhatsApp, etc.)

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**El problema:** Andrea tiene un e-commerce de productos naturales. Recibe 40-60 correos diarios. El 70% son las mismas 5 preguntas: estado del pedido, política de devoluciones, tiempos de envío, métodos de pago, disponibilidad de stock.

**El flujo:**

```
Correo entrante (Gmail)
  → IA clasifica: ¿es pregunta frecuente o caso complejo?
  → Si es frecuente: IA redacta respuesta usando la base de conocimiento
  → Respuesta queda en BORRADORES para aprobación (humano en el circuito)
  → Si es complejo: se etiqueta "URGENTE - revisar" y llega notificación al celular
```

**Resultado medible:** Andrea pasó de 3 horas diarias respondiendo correos a 40 minutos aprobando borradores. Después de 3 semanas, activó envío automático para las 3 preguntas más simples.

**Clave del éxito:** la IA necesita una "base de conocimiento" — un documento simple con tus políticas, precios y respuestas tipo. Sin eso, inventa respuestas. Con eso, responde como tu mejor empleado.

---

### Ejemplo 2: Generación de contenido para redes sociales

**El problema:** Marco dirige una agencia de marketing para restaurantes. Sabe que debe publicar 5 veces por semana en LinkedIn e Instagram, pero entre clientes y operación, publica 1 vez (con suerte).

**El flujo:**

```
Disparador: cada lunes a las 8:00 AM
  → IA lee las últimas noticias del sector (fuente RSS de blogs de la industria)
  → IA genera 5 borradores de posts adaptados a la voz de marca de Marco
  → Los borradores llegan a un Google Sheet
  → Marco revisa en 20 minutos, edita lo que quiere, marca "aprobado"
  → Los aprobados se programan automáticamente en la semana
```

**Resultado medible:** de 1 post semanal a 5. Tiempo invertido: 20-30 minutos los lunes en vez de 5 horas dispersas.

**Clave del éxito:** el "prompt de voz de marca". Marco escribió un documento de 1 página: cómo habla, qué palabras nunca usa, 3 ejemplos de sus mejores posts. Eso se incluye en cada solicitud a la IA. La diferencia entre contenido genérico y contenido que suena a ti está en ese documento.

---

### Ejemplo 3: Calificación automática de leads

**El problema:** Sofía vende software para clínicas dentales. Su formulario web recibe 80 leads al mes, pero solo 15 son realmente compradores potenciales. Su vendedor pierde horas llamando a curiosos.

**El flujo:**

```
Alguien llena el formulario web
  → IA analiza las respuestas: tamaño de la clínica, presupuesto declarado,
    urgencia, cargo de quien escribe
  → IA asigna puntaje de 1 a 100 y una etiqueta:
    🔥 Caliente (70+): notificación inmediata al vendedor por WhatsApp
    🌡️ Tibio (40-69): entra a secuencia de correos educativos
    ❄️ Frío (<40): newsletter mensual, sin esfuerzo de venta
  → Todo se registra automáticamente en el CRM
```

**Resultado medible:** el vendedor pasó de llamar 80 leads a llamar 15-20. Tasa de cierre subió de 4% a 12% — mismas ventas con un tercio del esfuerzo.

**Clave del éxito:** los criterios de puntuación los define Sofía, no la IA. Ella sabe que "clínica con 3+ sillones" vale más que "presupuesto alto pero clínica de 1 dentista". La IA aplica SU criterio a escala.

---

## 4. Ejercicio práctico paso a paso

### Tu primera automatización: resumen diario de correos importantes

Vas a construir un flujo que cada mañana lee tus correos sin leer, identifica los importantes con IA, y te envía un resumen. Es el "Hola Mundo" de la automatización con IA: simple, útil desde el día 1, y de cero riesgo (no responde nada, solo te informa).

**Tiempo estimado:** 60-90 minutos
**Necesitas:** una cuenta de Gmail y una tarjeta para crear cuenta en n8n Cloud (tiene prueba gratis, no te cobran al inicio)

#### Paso 1 — Crea tu cuenta en n8n (10 min)

1. Ve a [n8n.io](https://n8n.io) y haz clic en "Get started"
2. Crea tu cuenta con tu correo (la prueba gratuita dura 14 días, suficiente para este módulo)
3. Al entrar verás el lienzo vacío. Haz clic en **"Create Workflow"** y nómbralo: `Resumen diario de correos`

#### Paso 2 — Agrega el disparador (10 min)

1. Haz clic en el botón **"+"** del lienzo
2. Busca **"Schedule Trigger"** y selecciónalo
3. Configura: **Every Day**, a las **8:00 AM** (ajusta a tu zona horaria en la configuración del workflow)
4. Listo: tu flujo se activará solo cada mañana

#### Paso 3 — Conecta Gmail (15 min)

1. Haz clic en **"+"** después del disparador
2. Busca **"Gmail"** y elige la operación **"Get Many Messages"**
3. Te pedirá una credencial: haz clic en "Create New Credential" y sigue el proceso de autorización con tu cuenta de Google (n8n te guía pantalla por pantalla)
4. En filtros, configura: **Read Status = Unread** y **Received = últimas 24 horas**
5. Haz clic en **"Execute step"** para probar. Deberías ver tus correos sin leer como resultado. Si aparecen, vas bien.

#### Paso 4 — Agrega la IA (20 min)

1. Agrega un nodo nuevo: busca **"OpenAI"** (o "Anthropic" si prefieres Claude)
2. Necesitarás una API key: créala en [platform.openai.com](https://platform.openai.com) (carga $5 USD, este ejercicio gastará menos de $0.10)
3. Elige la operación **"Message a Model"** y el modelo **gpt-4o-mini** (barato y suficiente)
4. En el campo del mensaje, pega este prompt:

```
Eres mi asistente ejecutivo. Analiza estos correos y genera un resumen con este formato:

🔴 REQUIEREN ACCIÓN HOY: (correos de clientes, pagos, plazos)
🟡 IMPORTANTES PERO PUEDEN ESPERAR:
⚪ IGNORABLES: (newsletters, promociones — solo menciona la cantidad)

Para cada correo importante incluye: remitente, asunto, y qué acción sugiere en máximo 1 línea.

Correos: {{ $json }}
```

5. Ejecuta el paso y revisa el resumen que genera. Si la clasificación no te convence, ajusta el prompt — por ejemplo, agrega "los correos de [nombre de tu cliente clave] siempre van en REQUIEREN ACCIÓN".

#### Paso 5 — Recibe el resumen (15 min)

Elige UNA de estas dos opciones (la primera es más simple):

**Opción A — Por correo:** agrega un nodo **Gmail** con operación "Send Message", destinatario tú mismo, asunto `📋 Tu resumen de correos — {{ $now.format('dd/MM') }}`, y en el cuerpo inserta la respuesta de la IA.

**Opción B — Por Telegram:** agrega un nodo **Telegram**, crea un bot con @BotFather (n8n tiene guía integrada), y recibe el resumen directo en tu celular.

#### Paso 6 — Activa y verifica (10 min)

1. Haz clic en **"Execute Workflow"** para probar el flujo completo de punta a punta
2. Si el resumen llega correctamente, activa el interruptor **"Active"** arriba a la derecha
3. Mañana a las 8:00 AM recibirás tu primer resumen automático

#### ✅ Entregable del módulo

Captura de pantalla de: (1) tu workflow con los nodos conectados, y (2) el resumen recibido. Súbelas al espacio del curso con una reflexión de 3 líneas: *¿qué otra tarea de tu negocio automatizarías con esta misma lógica disparador → IA → acción?*

#### Si algo falla (los 3 errores más comunes)

| Error | Causa probable | Solución |
|---|---|---|
| Gmail no conecta | Permisos de Google no otorgados | Repite la autorización y acepta TODOS los permisos |
| La IA responde vacío o raro | El nodo no recibe los correos | Verifica que ejecutaste el nodo Gmail antes (debe mostrar datos) |
| "Insufficient quota" en OpenAI | No has cargado crédito | Carga $5 en platform.openai.com → Billing |

---

## 5. Recursos adicionales

**Para profundizar en n8n:**
- 📺 Canal oficial de YouTube de n8n — tutoriales en inglés con subtítulos (busca "n8n beginner course")
- 📚 [n8n.io/workflows](https://n8n.io/workflows) — más de 2,000 plantillas listas para copiar. Busca "Gmail AI" o "lead scoring" y adapta en vez de construir desde cero
- 📖 Documentación oficial: [docs.n8n.io](https://docs.n8n.io)

**Para mejorar tus prompts (la habilidad #1 de este módulo):**
- Guía de prompting de OpenAI: [platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- Repasa el Módulo 2 de este curso (Prompts efectivos para negocios)

**Plantillas del curso (descargables en el aula):**
- 📄 Plantilla "Base de conocimiento para atención al cliente" (la del Ejemplo 1)
- 📄 Plantilla "Documento de voz de marca" (la del Ejemplo 2)
- 📄 Matriz "¿Qué automatizo primero?" — evalúa tus tareas con las 3 condiciones de la sección 2.2

**Costos de referencia (junio 2026):**
- n8n Cloud: desde ~$24 USD/mes (o gratis auto-alojado si tienes quien te lo configure)
- OpenAI API con gpt-4o-mini: una startup típica gasta $3-15 USD/mes en automatizaciones como las de este módulo

---

## 6. Preguntas de autoevaluación

**Pregunta 1.** Tu startup recibe 30 solicitudes de cotización por semana, cada una requiere revisar 4 datos del cliente y responder con una de 3 plantillas de precios. ¿Esta tarea cumple las 3 condiciones para ser automatizada? Justifica cada condición.

<details>
<summary>Ver respuesta orientativa</summary>

Sí cumple las tres: es **repetitiva** (30 veces/semana, muy por encima del umbral de 3), tiene **patrón claro** (4 datos a revisar + 3 plantillas posibles = reglas explicables a un practicante en minutos), y es de **bajo riesgo** si mantienes humano en el circuito (la IA prepara la cotización en borrador y tú apruebas antes de enviar; un error se detecta antes de llegar al cliente). Sería una candidata ideal para tu segunda automatización.
</details>

**Pregunta 2.** En el flujo de calificación de leads del Ejemplo 3, ¿quién define los criterios de puntuación: la IA o el emprendedor? ¿Por qué importa esa distinción?

<details>
<summary>Ver respuesta orientativa</summary>

El emprendedor. La IA es excelente *aplicando* criterios a escala (80 leads al mes sin cansarse), pero el conocimiento del negocio — saber que una clínica de 3+ sillones vale más que un presupuesto alto en una clínica unipersonal — viene de tu experiencia vendiendo. Si dejas que la IA "decida" sin tus criterios, puntuará con lógica genérica y filtrará mal. Regla general del módulo: tú aportas el criterio, la IA aporta la escala.
</details>

**Pregunta 3.** Construiste un flujo que responde correos de clientes automáticamente y funciona bien en pruebas. ¿Cuál es el error de implementación más probable si lo activas hoy con envío 100% automático, y cómo lo evitarías?

<details>
<summary>Ver respuesta orientativa</summary>

El error es saltarse la fase de "humano en el circuito". Las pruebas no cubren los casos raros: un cliente enojado, una pregunta ambigua, un correo legal. Si la IA responde mal uno de esos, el costo reputacional supera todo el tiempo ahorrado. Lo correcto: 2-4 semanas con las respuestas en borradores que tú apruebas, midiendo cuántas necesitaste editar. Cuando el porcentaje de edición baje (ej. menos del 10%), activas envío automático solo para las categorías más simples, y mantienes revisión humana para el resto.
</details>

---

> **Próximo módulo:** Módulo 4 — "Conecta tus automatizaciones a tu negocio real: CRM, WhatsApp y métricas". Vas a tomar el flujo que construiste hoy y conectarlo con las herramientas que ya usas.