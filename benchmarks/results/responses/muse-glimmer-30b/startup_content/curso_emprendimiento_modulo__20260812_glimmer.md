# Muse Glimmer 30B — startup_content/curso_emprendimiento_modulo

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.27 | quality: 9.44
- latency_total: 30.545s | tokens_per_second: 61.8
- input_tokens: 235 | output_tokens: 1888
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

**Duración estimada:** 2 horas 30 min
**Nivel:** Emprendedor no-técnico

## 1. Objetivo del módulo

Al finalizar este módulo podrás identificar procesos repetitivos de tu startup y convertirlos en flujos de trabajo automatizados con IA usando herramientas no-code como n8n. Aprenderás a conectar datos, decisiones inteligentes y acciones sin programar, liberando tiempo para vender, atender y escalar.

## 2. Contenido teórico

### ¿Qué es automatizar con IA?

Automatizar con IA es diseñar un flujo donde la información entra, la IA toma una decisión o crea algo, y el sistema ejecuta una acción automáticamente. No es solo "hacer más rápido", es hacer que tu negocio piense y responda solo.

Un flujo típico tiene 3 partes:
1. **Disparador:** Qué inicia el flujo. Ej: llega un mensaje por WhatsApp, un formulario se llena, llega un email.
2. **Cerebro IA:** Qué analiza o genera. Ej: clasifica un lead, responde una pregunta, resume un texto.
3. **Acción:** Qué pasa después. Ej: guarda en Google Sheets, envía a Slack, responde al cliente, publica en redes.

### Herramientas clave: n8n

**n8n** es una plataforma de automatización visual tipo "arrastrar y soltar". Conecta más de 400 apps como Gmail, WhatsApp, Google Sheets, OpenAI, Slack, Instagram y más.

¿Por qué n8n para emprendedores?
* No necesitas código, solo conectas nodos.
* Puedes ver el flujo completo como un mapa.
* Tiene plan gratuito y se puede usar en la nube.
* Permite usar IA de OpenAI, Gemini o Claude dentro del flujo.

Otros complementos útiles: Make.com, Zapier para casos simples, y ChatGPT con Actions para prototipos rápidos.

> Regla de oro: Automatiza primero procesos que son repetitivos, claros y con datos de entrada/salida definidos.

## 3. 3 ejemplos prácticos de automatización para startups

### 1. Atención al cliente automatizada
**Problema:** Respondes las mismas preguntas 20 veces al día.
**Flujo:** WhatsApp / Instagram DM -> n8n -> OpenAI con contexto de tu negocio -> Respuesta automática + registro en Google Sheets.
**Valor:** Respuesta en segundos, 24/7, y tú solo intervienes en casos complejos.

### 2. Generación de contenido para redes sociales
**Problema:** No tienes tiempo para crear posts diarios.
**Flujo:** Cron semanal -> OpenAI genera 3 ideas de post a partir de tu nicho y calendario -> n8n crea borrador en Google Docs y notifica a Slack para aprobación.
**Valor:** Pasas de 0 a borrador listo en minutos, mantienes constancia sin bloquearte.

### 3. Calificación automática de leads
**Problema:** Todos los leads van al mismo lugar y pierdes oportunidades.
**Flujo:** Formulario de captación -> n8n -> OpenAI analiza respuestas y asigna puntaje: Caliente / Templado / Frío + motivo -> Guarda en Google Sheets y envía notificación a Slack/WhatsApp solo si es Caliente.
**Valor:** Tu equipo vende primero a quien más probabilidad tiene de comprar.

## 4. Ejercicio práctico paso a paso

**Proyecto:** Lead de formulario calificado automáticamente

Vas a crear un flujo que recibe un lead, lo califica con IA y lo guarda.

**Prerrequisitos:** Cuenta gratuita en n8n.io, cuenta en OpenAI y Google Sheets.

1. **Crea el disparador.** En n8n crea un nuevo workflow. Añade nodo `Webhook`. Actívalo y copia la URL. Esa URL la usarás como acción de tu formulario.
2. **Conecta la IA.** Añade nodo `OpenAI > Chat Model`. En `Prompt` pega:
   ```
   Eres un calificadord e leads. Clasifica este lead como Caliente, Templado o Frío.
   Responde solo en JSON con: {clasificacion, motivo, prioridad 1-10}
   Datos del lead: {{$json["nombre"]}}, {{$json["email"]}}, {{$json["mensaje"]}}
   ```
3. **Guarda el resultado.** Añade nodo `Google Sheets > Append`. Conéctalo a tu hoja "Leads". Mapea nombre, email, mensaje, clasificación, motivo y prioridad.
4. **Notifica si es caliente.** Añade nodo `IF`. Condición: `clasificacion` igual a `Caliente`. Si sí, añade nodo `Slack` o `Email` para avisar al equipo.
5. **Prueba.** Envía datos de prueba al Webhook con un formulario o Postman. Revisa que se guarde en Sheets y que llegue la notificación.

Tip no-técnico: No intentes automatizar todo. Empieza con un flujo, pruébalo 1 semana y mejora el prompt de la IA.

## 5. Recursos adicionales

* **n8n Docs Oficial:** n8n.io/workflows
* **Plantillas listas para emprendedores:** n8n.io/workflows/tag/ia
* **Curso rápido n8n para no técnicos:** YouTube - "n8n desde cero en español"
* **Guía de prompts para calificación de leads:** PromptHub - Lead Scoring
* **Comunidad:** Comunidad n8n en Discord y r/n8n

## 6. Preguntas de autoevaluación

1. ¿Cuál es la diferencia entre un disparador, un cerebro IA y una acción en un flujo de automatización?
2. ¿Qué proceso repetitivo de tu negocio podrías automatizar esta semana con n8n + OpenAI y qué datos necesitarías de entrada y salida?
3. ¿Por qué es importante probar un flujo con datos reales antes de activarlo para clientes?

¿Listo para el Módulo 4?