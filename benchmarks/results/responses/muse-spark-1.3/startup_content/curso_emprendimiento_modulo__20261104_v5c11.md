# Muse Spark 1.3 — startup_content/curso_emprendimiento_modulo

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 38.218s | tokens_per_second: 106.9
- input_tokens: 234 | output_tokens: 4087
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una explicación detallada y ejemplos prácticos que son directamente útiles para emprendedores, aunque podría profundizar un poco más en los ejemplos prácticos.

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

> **Curso: IA Práctica para Emprendedores**
> **Duración estimada:** 90 minutos (45 min teoría + 45 min práctica) | **Nivel:** No-técnico | **Requisito:** Tener una cuenta de Google y una cuenta gratuita en OpenAI

---

## 1. Objetivo del Módulo

Al finalizar este módulo, serás capaz de identificar una tarea repetitiva en tu negocio, mapearla como un proceso simple de 3 pasos (disparador -> cerebro IA -> acción) y construir tu primera automatización funcional con herramientas no-code como N8N, para ahorrarte al menos 5 horas a la semana en atención al cliente, contenido o ventas sin necesidad de saber programar.

---

## 2. Contenido Teórico: ¿Qué es Automatizar con IA?

### 2.1. La idea en lenguaje emprendedor

Automatizar NO es contratar un robot. Es enseñarle a una herramienta a hacer una tarea aburrida y repetitiva por ti.

Piensa en tu negocio como una taquería en CDMX:
* **Automatización tradicional (sin IA):** Es como una máquina tortilladora. Siempre hace lo mismo: si llega un pedido, mándalo a Excel. Es rígida.
* **Automatización CON IA:** Es como contratar a un ayudante inteligente. No solo mueve datos, sino que *piensa*: entiende un mensaje enojado de un cliente, lo resume, le responde con amabilidad y decide si es urgente.

**Fórmula de oro para no-técnicos:**
> **TRIGGER (¿Cuándo empieza?) + CEREBRO IA (¿Qué tiene que pensar?) + ACCIÓN (¿Qué tiene que hacer?)**

Ejemplo: *Cuando me llega un WhatsApp (Trigger) -> ChatGPT entiende qué quiere el cliente (Cerebro) -> Lo anota en Google Sheets y le responde (Acción).*

### 2.2. Las 3 piezas que siempre necesitas

1.  **El Disparador:** El evento que inicia todo. Ej: "Llenan mi formulario de contacto", "Me etiquetan en Instagram", "Entra un pago en Mercado Pago".
2.  **El Cerebro (IA):** Normalmente ChatGPT / Claude. Hace lo que un humano haría: clasificar, redactar, resumir, traducir, decidir.
3.  **La Acción:** Donde termina el trabajo. Ej: "Enviar WhatsApp", "Crear fila en Excel", "Publicar en redes", "Avisar en Slack".

No necesitas construir esto desde cero. Usas un **conector** visual.

### 2.3. Herramientas: ¿N8N, Zapier o Make?

Para emprendedores latinos, estas son las 3 mejores. Te recomendamos empezar con **N8N**.

| Herramienta | Ideal para | Costo LatAm | Ventaja para ti |
| :--- | :--- | :--- | :--- |
| **N8N (La estrella de este módulo)** | Procesos con IA complejos | **Gratis si lo instalas tú, o desde $20 USD/mes en la nube** | Es el más barato a largo plazo, tiene 400+ integraciones y maneja IA de forma nativa. Puedes copiar plantillas de otros. |
| **Zapier** | Automatizaciones súper simples y rápidas | Caro ($29 USD/mes+) | El más fácil: "Conecta Gmail con Sheets en 2 clics". Ideal si odias la tecnología. |
| **Make (antes Integromat)** | Ver tu flujo bonito y visual | Plan gratis generoso | Perfecto para ver el dibujito de tu proceso. Muy usado en agencias en México y Argentina. |

**¿Por qué N8N para este curso?**
1.  Habla español en su interfaz visual (arrastrar y soltar).
2.  Te deja usar WhatsApp, Instagram, Google Sheets, Notion y OpenAI sin programar.
3.  Puedes empezar gratis en `n8n.cloud` y luego escalar sin que la factura se dispare como con Zapier.

> **Mito no-técnico:** "Necesito un programador para usar N8N". Falso. Si sabes usar Canva y Excel, puedes usar N8N. Es armar legos, no escribir código.

---

## 3. 3 Ejemplos Prácticos para Startups Reales

### Ejemplo 1: Atención al Cliente Automatizada 24/7
**Caso real:** *Mariana tiene una tienda de cosmética natural en Bogotá y vende por WhatsApp e Instagram. Perdìa ventas porque tardaba 4 horas en responder.*

**El flujo:**
`TRIGGER: Nuevo mensaje en WhatsApp (vía Twilio o ManyChat) -> CEREBRO IA: GPT-4 lee el mensaje + consulta un documento con FAQs (precios, envíos, horarios) -> ACCIÓN: Responde al instante. Si detecta la palabra "reclamo" o "devolución", crea un ticket en HubSpot y avisa a Mariana por Telegram.`

**Prompt que usa el cerebro:**
> "Eres 'Sofi', asistente amable de Lumina Cosmética. Responde en español colombiano, tono cercano, máximo 3 líneas. Usa SOLO esta info: [pega tus FAQs]. Si no sabes la respuesta, di: 'Déjame confirmarlo con Mariana y te escribo en 1 hora'. Nunca inventes precios."

**Resultado:** -70% de preguntas repetitivas. Mariana solo atiende los casos que sí necesitan humana. Ahorro: 12 horas/semana.

### Ejemplo 2: Generación de Contenido para Redes Sociales en Piloto Automático
**Caso real:** *Diego tiene un SaaS de facturación para freelancers en México. No tiene community manager.*

**El flujo:**
`TRIGGER: Cada lunes 8am -> CEREBRO IA: Lee las 5 noticias de su sector desde Google News + revisa comentarios de clientes -> ACCIÓN 1: Genera 3 ideas de posts + copy + hashtags -> ACCIÓN 2: Los guarda en una tabla de Notion para que Diego apruebe con un clic -> ACCIÓN 3: Los aprobados se programan en Buffer para LinkedIn e Instagram.`

**Prompt que usa:**
> "Actúa como estratega de contenido para emprendedores mexicanos. Crea 3 posts para LinkedIn sobre [tema de la semana]. Formato: hook polémico + historia de 80 palabras + 3 bullets accionables + CTA. Tono: directo, sin humo corporativo."

**Resultado:** Pasó de publicar 1 vez al mes a 3 veces por semana. +40% de leads inbound en 2 meses sin contratar a nadie.

### Ejemplo 3: Calificación Automática de Leads (Tu vendedor que no duerme)
**Caso real:** *Sofía vende cursos de repostería online en Perú y Chile. Recibe 200 formularios al mes y no sabe a quién llamar primero.*

**El flujo:**
`TRIGGER: Alguien llena Google Form "Quiero el curso" -> CEREBRO IA: Analiza respuestas (presupuesto, ciudad, urgencia, "¿para negocio o hobby?") y le pone nota del 1 al 100 -> ACCIÓN: Si nota > 80 (LEAD CALIENTE): lo manda a Google Sheets en rojo + envía WhatsApp automático a Sofía: "¡Llama YA a Ana!". Si nota < 50: lo mete a una secuencia de emails educativos automática.`

**Prompt que usa:**
> "Califica este lead del 1 al 100. Da +30 puntos si tiene negocio, +30 si tiene presupuesto > $100 USD, +20 si quiere empezar 'esta semana'. Devuélveme solo: PUNTAJE | MOTIVO en 10 palabras | SIGUIENTE PASO."

**Resultado:** Dejó de llamar a curiosos. Su tasa de cierre subió de 5% a 18% porque solo habla con calientes.

---

## 4. Ejercicio Práctico Paso a Paso: Construye tu Calificador de Leads en 30 Minutos

Vamos a hacer el Ejemplo 3, pero simplificado. No necesitas tarjeta de crédito.

**Lo que vas a lograr:** Cada vez que alguien llene un formulario, la IA lo califica y te lo ordena en un Excel. Cero código.

**Lo que necesitas (10 min de setup):**
1.  Cuenta gratis en [n8n.cloud](https://n8n.cloud) (elige Trial)
2.  Cuenta de Google (para Google Forms + Google Sheets)
3.  API Key gratuita de OpenAI (en platform.openai.com)

### Paso 1: Mapea tu idea en papel (5 min)
Antes de tocar la compu, responde esto para TU negocio:
> Mi tarea repetitiva es: ________ (ej: responder precios)
> Empieza cuando: ________ (ej: llenan mi form)
> La IA tiene que decidir: ________ (ej: ¿es cliente bueno?)
> Termina con: ________ (ej: avisarme por email)

*Tip emprendedor: Empieza con UN solo flujo que te duela. No automatices todo.*

### Paso 2: Crea la base de datos (5 min)
1.  Crea un **Google Form** con 4 preguntas: Nombre, WhatsApp, Email, y "¿Cuál es tu presupuesto / urgencia?" (texto libre).
2.  Crea un **Google Sheet** en blanco llamado `Leads Calificados IA` con columnas: Fecha | Nombre | WhatsApp | Mensaje Original | Puntaje IA | Resumen IA.

### Paso 3: Arma el flujo en N8N (15 min)
1.  En N8N, clic en `+ New Workflow` > `Add Trigger` > busca **Google Forms Trigger** (o usa Webhook si prefieres). Conéctalo a tu Form. Haz una prueba llenándolo tú mismo.
2.  Agrega un nodo `+` > busca **OpenAI**. Elige `Message a model`. Conecta tu API Key. Elige modelo `gpt-4o-mini` (barato y rápido).
3.  En el campo `Prompt`, copia y pega esto:
    ```
    Eres un calificador de leads para mi negocio: [DESCRIBE TU NEGOCIO EN 1 LÍNEA, ej: "Vendo asesorías contables para pymes en Chile"].
    Analiza esta respuesta del formulario: {{$json}}
    Devuélveme en este formato exacto:
    PUNTAJE: [número del 1 al 100]
    RESUMEN: [¿Es caliente, tibio o frío? ¿Por qué? en 15 palabras]
    ```
4.  Agrega un nodo `+` > busca **Google Sheets**. Elige `Append Row`. Conéctalo a tu hoja `Leads Calificados IA`. Mapea: Nombre = nombre del form, Puntaje IA = salida de OpenAI, etc.
5.  (Opcional Pro): Agrega un nodo **IF**. Condición: Si Puntaje > 75, entonces envía un **Gmail** a ti mismo: "¡Lead caliente! Llama a {{$json.nombre}}".

### Paso 4: Prueba y Activa (5 min)
1.  Dale clic a `Test Workflow`. Llena tu Google Form con un cliente ficticio bueno y uno malo. ¿La IA los calificó bien?
2.  Si funciona, arriba a la derecha cambia a **Active (verde)**. ¡Listo! Ya tienes un empleado IA 24/7.

> **Checklist de éxito:** ✅ Se crea una fila nueva sola ✅ El puntaje tiene sentido ✅ No tuviste que programar nada.

**Reto extra:** Cambia el último nodo de Gmail por WhatsApp (usando Twilio en N8N) para que te llegue el aviso a tu celular.

---

## 5. Recursos Adicionales (Curados para LatAm)

**Para copiar y pegar:**
1.  **Biblioteca de Plantillas N8N:** `n8n.io/workflows` -> Busca "Lead Qualification", "WhatsApp Auto Reply", "Instagram Content". Importas con 1 clic.
2.  **N8N en Español:** Canal de YouTube "Automatiza con N8N" y comunidad de Facebook "N8N en Español + IA".

**Para aprender más:**
3.  **Documentación oficial N8N + OpenAI:** Guía visual paso a paso sin tecnicismos.
4.  **Make Academy (Gratis y en español):** Si N8N se te hizo difícil, empieza aquí. Es más visual.
5.  **Prompt Pack Emprendedor:** Guarda estos 5 prompts: Resumidor de quejas, Generador de descripciones de producto para Mercado Libre, Respondedor de emails, Traductor MX-AR-CL (adapta el slang), y Creador de guiones para TikTok.

**Costos reales a considerar:**
> N8N Cloud ($20 USD) + OpenAI ($5-10 USD/mes para 1000 leads) es más barato que 2 horas de un asistente. Empieza con planes gratis y escala cuando vendas.

---

## 6. Preguntas de Autoevaluación

Responde en tu cuaderno antes de pasar al Módulo 4. No hay nota, hay claridad.

**1. Diagnóstico:** Piensa en tu semana pasada. ¿Cuál fue la tarea que más repetiste (responder lo mismo, copiar/pegar datos, perseguir clientes)? Descríbela usando la fórmula TRIGGER + CEREBRO IA + ACCIÓN. ¿Es una buena candidata para automatizar o necesita 100% toque humano? ¿Por qué?

**2. Diseño:** Si tuvieras que automatizar tu atención al cliente mañana, ¿qué le permitirías responder SOLA a la IA y en qué casos le ordenarías que se detenga y te pase el caso a ti? Define 2 reglas claras (Ej: "Responde sola precios y horarios, pero pásame a mí si menciona 'reembolso'").

**3. Riesgo y Ética:** Un lead te reclama porque tu IA le dio un precio incorrecto por WhatsApp. ¿Quién es responsable? ¿Qué harías esta semana para evitarlo (Ej: limitar la fuente de verdad a un documento, agregar un aviso de "Soy un asistente IA", revisar logs)?

---
**¿Terminaste?** Tómale screenshot a tu Google Sheet con al menos 2 leads calificados por la IA y compártelo en la comunidad del curso con el hashtag `#MiPrimerFlujoM3`. En el Módulo 4 aprenderemos a conectar esto a ventas y cobranza.
