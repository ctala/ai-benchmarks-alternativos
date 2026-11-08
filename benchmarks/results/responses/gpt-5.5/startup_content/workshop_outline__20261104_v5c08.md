# GPT-5.5 — startup_content/workshop_outline

- model_id: `gpt-5.5`
- success: True  | final: 7.66 | quality: 9.72
- latency_total: 88.4s | tokens_per_second: 69.4
- input_tokens: 186 | output_tokens: 6139
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

# Outline completo — Workshop presencial (3 horas)  
## **“Construye tu Asistente de IA para tu Startup - Workshop Práctico”**

**Audiencia:** Emprendedores early-stage no técnicos  
**Formato:** Presencial, práctico, con ejercicios individuales y en parejas  
**Duración:** 3 horas  
**Tamaño ideal:** 20–30 personas  
**Resultado esperado:** Cada participante sale con un primer prototipo funcional de asistente de IA para una tarea real de su startup.

---

# 1. Objetivo general del workshop

Que cada emprendedor entienda cómo diseñar, construir y mejorar un asistente de IA sencillo que le ayude en una tarea concreta de su startup, sin necesidad de programar.

Al final del workshop, cada participante tendrá:

- Un caso de uso claro para su asistente.
- Un “brief” o especificación del asistente.
- Un set de instrucciones/prompt base.
- Un primer prototipo usando una herramienta tipo ChatGPT, Claude, Gemini, Poe, Custom GPT o similar.
- Un plan de mejora para llevarlo a su operación diaria.

---

# 2. Agenda detallada — 3 horas

| Tiempo | Bloque | Duración |
|---|---:|---:|
| 00:00 – 00:10 | Bienvenida y mindset: IA como copiloto de startup | 10 min |
| 00:10 – 00:25 | Qué es un asistente de IA y qué puede hacer por tu startup | 15 min |
| 00:25 – 00:45 | Mapa de oportunidades: dónde aplicar IA en tu negocio | 20 min |
| 00:45 – 01:05 | Elegir el caso de uso correcto | 20 min |
| 01:05 – 01:15 | Break rápido | 10 min |
| 01:15 – 01:35 | Anatomía de un buen asistente de IA | 20 min |
| 01:35 – 02:15 | Ejercicio principal: diseña y construye tu asistente | 40 min |
| 02:15 – 02:40 | Pruebas, feedback y mejora del asistente | 25 min |
| 02:40 – 02:55 | Cómo integrarlo en tu día a día sin volverte loco | 15 min |
| 02:55 – 03:00 | Cierre, próximos pasos y recursos | 5 min |

---

# 3. Materiales necesarios

## Para preparar antes del workshop

### Espacio físico

- Sala con mesas para trabajo individual y en parejas.
- Proyector o pantalla grande.
- Audio básico si el espacio es grande.
- WiFi estable.
- Enchufes o extensiones.
- Pizarra, rotafolios o pared para post-its.

### Para el facilitador

- Presentación en slides.
- Cronómetro visible o control del tiempo.
- Plantilla impresa o digital: “Canvas del Asistente de IA”.
- Ejemplos preparados de asistentes.
- Lista de herramientas sugeridas.
- QR code a carpeta de recursos.
- Demo lista en ChatGPT, Claude, Gemini, Perplexity o Custom GPT.
- Plan B si falla internet: prompts impresos y demo grabada o screenshots.

### Para participantes

Pedirles antes del workshop:

- Laptop o tablet. Idealmente laptop.
- Cuenta creada en alguna herramienta de IA:
  - ChatGPT
  - Claude
  - Gemini
  - Perplexity
  - Poe
  - Microsoft Copilot
- Traer una descripción corta de su startup.
- Traer una tarea repetitiva o dolorosa que quieran mejorar.
- Opcional: documentos reales no sensibles, por ejemplo:
  - FAQs
  - mensajes de clientes
  - descripción del producto
  - pitch deck
  - landing page
  - emails de venta
  - guiones comerciales

### Material impreso recomendado

- Canvas del Asistente de IA — 1 por persona.
- Checklist de buen prompt.
- Lista de 20 casos de uso para startups.
- Hoja de evaluación rápida del asistente.
- Mini guía de seguridad y privacidad.

---

# 4. Desarrollo por bloques

---

## Bloque 1: Bienvenida y mindset  
### Duración: 10 minutos

### Objetivo

Activar a la audiencia, alinear expectativas y dejar claro que el workshop será práctico, no teórico.

### Dinámica

**Charla corta + pregunta al público**

El facilitador abre con una frase potente:

> “Hoy no vinimos a hablar de IA. Vinimos a construir una herramienta que mañana pueda ahorrarte tiempo, ayudarte a vender más o entender mejor a tus clientes.”

Luego pide a los participantes responder rápidamente:

- ¿En qué parte de tu startup pierdes más tiempo hoy?
- ¿Qué tarea repites todas las semanas?
- ¿Qué te gustaría delegar, aunque todavía no puedas contratar a alguien?

Pueden responder levantando la mano o con post-its.

### Key takeaway

La IA no es solo para empresas grandes o equipos técnicos. Un fundador early-stage puede usar IA para multiplicar su capacidad operativa desde hoy.

### Slide count estimado

**3 slides**

1. Título del workshop  
2. Promesa del día: “Sales con un asistente funcionando”  
3. Reglas del juego: práctico, imperfecto, accionable  

---

## Bloque 2: Qué es un asistente de IA y qué puede hacer por tu startup  
### Duración: 15 minutos

### Objetivo

Explicar de forma simple qué es un asistente de IA, qué no es, y qué tipos de tareas puede resolver.

### Dinámica

**Charla práctica + ejemplos rápidos**

Explicar que un asistente de IA es una combinación de:

- Una tarea clara.
- Un rol definido.
- Instrucciones específicas.
- Contexto del negocio.
- Criterios para responder bien.
- Iteración y mejora continua.

Ejemplos concretos:

- Asistente para responder preguntas frecuentes de clientes.
- Asistente para generar emails de prospección.
- Asistente para analizar entrevistas con usuarios.
- Asistente para crear contenido para LinkedIn.
- Asistente para preparar reuniones comerciales.
- Asistente para revisar pitch decks.
- Asistente para priorizar feedback de usuarios.
- Asistente para generar propuestas comerciales.

También aclarar lo que no es:

- No es magia.
- No reemplaza criterio del fundador.
- No debe manejar información sensible sin cuidado.
- No funciona bien si la tarea está mal definida.

### Key takeaway

Un buen asistente de IA no empieza con tecnología. Empieza con una tarea concreta del negocio.

### Slide count estimado

**5 slides**

1. ¿Qué es un asistente de IA?  
2. IA como becario senior/copywriter/analista/copiloto  
3. Qué sí puede hacer  
4. Qué no debería hacer  
5. Ejemplos reales para startups  

---

## Bloque 3: Mapa de oportunidades — dónde aplicar IA en tu negocio  
### Duración: 20 minutos

### Objetivo

Ayudar a los participantes a identificar tareas candidatas para convertir en asistentes de IA.

### Dinámica

**Ejercicio individual + discusión breve**

Cada participante lista tareas en cuatro áreas:

### Área 1: Ventas

- Crear mensajes de prospección.
- Preparar llamadas.
- Resumir reuniones.
- Generar propuestas.
- Responder objeciones.

### Área 2: Marketing

- Crear posts.
- Adaptar contenido por canal.
- Analizar competidores.
- Escribir newsletters.
- Crear ideas de campañas.

### Área 3: Producto y clientes

- Analizar feedback.
- Resumir entrevistas.
- Crear FAQs.
- Priorizar funcionalidades.
- Detectar patrones en tickets.

### Área 4: Operaciones

- Crear procesos.
- Redactar emails.
- Preparar reportes.
- Documentar reuniones.
- Diseñar checklists.

Pregunta guía:

> “Si esta tarea se hiciera 50% más rápido o 30% mejor, ¿tendría impacto real en tu startup?”

Los participantes eligen tres posibles tareas.

### Key takeaway

Las mejores oportunidades están en tareas frecuentes, repetitivas, con texto, criterio y contexto.

### Slide count estimado

**4 slides**

1. El mapa de oportunidades  
2. Ventas y marketing  
3. Producto y clientes  
4. Operaciones y administración  

---

## Bloque 4: Elegir el caso de uso correcto  
### Duración: 20 minutos

### Objetivo

Evitar que los participantes intenten construir algo demasiado amplio. Ayudarles a seleccionar un caso de uso viable para el workshop.

### Dinámica

**Ejercicio con matriz simple**

Los participantes evalúan sus tres tareas usando dos criterios:

1. **Impacto para el negocio**
   - ¿Ahorra tiempo?
   - ¿Ayuda a vender?
   - ¿Mejora la experiencia del cliente?
   - ¿Reduce errores?
   - ¿Aumenta velocidad de aprendizaje?

2. **Facilidad para empezar**
   - ¿Tengo ejemplos?
   - ¿La tarea es clara?
   - ¿No requiere integraciones complejas?
   - ¿Puedo probarla hoy?
   - ¿El resultado se puede revisar fácilmente?

Se usa una matriz:

| | Fácil de empezar | Difícil de empezar |
|---|---|---|
| Alto impacto | Empezar aquí | Proyecto futuro |
| Bajo impacto | Quick win | Evitar |

Cada participante escoge un caso de uso para construir durante el workshop.

Ejemplos recomendados para construir en vivo:

- Asistente de prospección comercial.
- Asistente para posts de LinkedIn.
- Asistente de atención a clientes.
- Asistente para entrevistas de usuarios.
- Asistente para mejorar pitch.
- Asistente para responder objeciones de ventas.
- Asistente para generar emails de seguimiento.
- Asistente para analizar feedback de clientes.

### Key takeaway

No construyas “un asistente para todo”. Construye un asistente para una tarea específica y valiosa.

### Slide count estimado

**4 slides**

1. Error común: querer automatizar todo  
2. Matriz impacto vs facilidad  
3. Criterios para elegir buen caso de uso  
4. Ejemplos de casos ideales para hoy  

---

## Break rápido  
### Duración: 10 minutos

### Objetivo

Dar descanso y permitir que los participantes terminen de elegir su caso de uso.

### Dinámica

Descanso informal. El facilitador puede acercarse a participantes que estén bloqueados para ayudarles a definir su caso.

### Key takeaway

Volvemos con un caso de uso claro para construir.

### Slide count estimado

**1 slide**

1. Break + recordatorio: “Vuelve con tu caso elegido”  

---

## Bloque 5: Anatomía de un buen asistente de IA  
### Duración: 20 minutos

### Objetivo

Enseñar la estructura simple para crear instrucciones efectivas para un asistente.

### Dinámica

**Mini charla + demo**

Presentar el framework práctico:

## Framework R.C.T.E.S.

### R — Rol

¿Quién debe ser el asistente?

Ejemplo:

> “Actúa como un asesor comercial B2B experto en startups SaaS para América Latina.”

### C — Contexto

¿Qué debe saber sobre tu negocio?

Ejemplo:

> “Mi startup ayuda a restaurantes pequeños a controlar inventario y reducir desperdicio.”

### T — Tarea

¿Qué debe hacer exactamente?

Ejemplo:

> “Genera un email de prospección para contactar dueños de restaurantes.”

### E — Estilo y restricciones

¿Cómo debe responder?

Ejemplo:

> “Usa tono cercano, directo, no corporativo. Máximo 120 palabras. Incluye asunto del email.”

### S — Salida esperada

¿En qué formato debe entregar el resultado?

Ejemplo:

> “Entrega 3 versiones en una tabla: asunto, email, CTA.”

Luego se muestra una demo en vivo:

Prompt malo:

> “Hazme un email de ventas.”

Prompt mejorado:

> “Actúa como un experto en ventas B2B para startups SaaS en Latinoamérica. Mi startup ayuda a restaurantes pequeños a reducir desperdicio de comida con alertas de inventario. Genera 3 emails de prospección para dueños de restaurantes en Ciudad de México. Usa tono cercano, claro y práctico. Cada email debe tener máximo 120 palabras, un asunto atractivo y un llamado a agendar una demo de 15 minutos. Entrega el resultado en tabla.”

Mostrar cómo cambia la calidad.

### Key takeaway

La calidad del asistente depende de la claridad del rol, contexto, tarea, estilo y formato de salida.

### Slide count estimado

**6 slides**

1. La anatomía de un asistente  
2. Framework R.C.T.E.S.  
3. Ejemplo de prompt malo  
4. Ejemplo de prompt bueno  
5. Demo antes/después  
6. Checklist para construir el tuyo  

---

# 5. Ejercicio principal del workshop

## Bloque 6: Diseña y construye tu asistente de IA  
### Duración: 40 minutos

### Objetivo

Que cada participante cree un primer asistente funcional usando una herramienta de IA.

### Dinámica

**Ejercicio individual con apoyo del facilitador + trabajo en parejas**

Los participantes completan el **Canvas del Asistente de IA**.

---

## Canvas del Asistente de IA

### 1. Nombre del asistente

Ejemplos:

- Asistente de Prospección B2B
- Copiloto de Atención a Clientes
- Generador de Contenido para Founder-Led Sales
- Analista de Feedback de Usuarios
- Coach de Pitch para Inversionistas

---

### 2. Problema que resuelve

Completar:

> “Este asistente me ayuda a…”

Ejemplo:

> “Este asistente me ayuda a crear emails de prospección personalizados para contactar potenciales clientes sin empezar desde cero cada vez.”

---

### 3. Usuario del asistente

¿Quién lo usará?

- Fundador
- Equipo comercial
- Marketing
- Customer success
- Operaciones

---

### 4. Contexto de la startup

Completar:

- Qué vendemos:
- A quién le vendemos:
- En qué país/mercado:
- Propuesta de valor:
- Tono de marca:
- Objeciones comunes:
- Diferenciadores:

---

### 5. Tarea principal

Completar:

> “Cuando le entregue _______, debe producir _______.”

Ejemplo:

> “Cuando le entregue el nombre de una empresa, industria y dolor probable, debe producir un email de prospección personalizado.”

---

### 6. Inputs necesarios

¿Qué información necesita recibir el asistente?

Ejemplos:

- Tipo de cliente
- Industria
- Dolor del cliente
- País
- Canal
- Objetivo
- Oferta
- Etapa del funnel
- Texto de una entrevista
- Comentarios de usuarios

---

### 7. Output esperado

¿Qué debe entregar?

Ejemplos:

- Tabla
- Email
- Lista de ideas
- Resumen
- Guion
- Diagnóstico
- Recomendaciones
- Checklist
- Plan de acción

---

### 8. Reglas del asistente

Ejemplos:

- No inventes datos.
- Si falta información, haz preguntas.
- Usa tono directo.
- No uses lenguaje corporativo.
- Sé breve.
- Propón alternativas.
- Entrega siempre en tabla.
- Incluye próximos pasos.

---

### 9. Prompt base del asistente

Los participantes crean su prompt usando esta plantilla:

```text
Actúa como [ROL].

Contexto:
Mi startup es [DESCRIPCIÓN DE LA STARTUP].
Ayudamos a [CLIENTE IDEAL] a [RESULTADO / BENEFICIO].
Nuestro mercado principal es [PAÍS / REGIÓN].
Nuestro tono de marca es [TONO].
Nuestros principales diferenciadores son [DIFERENCIADORES].

Tu tarea:
Quiero que me ayudes a [TAREA PRINCIPAL].

Inputs que te voy a dar:
- [INPUT 1]
- [INPUT 2]
- [INPUT 3]

Instrucciones:
- [REGLA 1]
- [REGLA 2]
- [REGLA 3]
- Si falta información, hazme preguntas antes de responder.
- No inventes datos.
- Sé específico y práctico.

Formato de salida:
Entrega la respuesta en [FORMATO].
Incluye [ELEMENTOS OBLIGATORIOS].
```

---

### 10. Primera prueba

Cada participante prueba su asistente con un caso real.

Ejemplo para ventas:

```text
Cliente objetivo: cafeterías independientes en Bogotá.
Dolor probable: pierden dinero por mala gestión de inventario.
Objetivo: conseguir una llamada de diagnóstico.
Canal: email frío.
```

Ejemplo para contenido:

```text
Tema: Errores comunes al lanzar un marketplace.
Audiencia: fundadores early-stage en LatAm.
Canal: LinkedIn.
Objetivo: generar conversación y autoridad.
Tono: honesto, práctico, sin humo.
```

Ejemplo para customer support:

```text
Pregunta del cliente: ¿Puedo cancelar mi plan mensual en cualquier momento?
Contexto: Vendemos una plataforma de gestión financiera para freelancers.
Tono: claro, empático y breve.
Objetivo: responder y reducir fricción.
```

---

### Estructura del ejercicio de 40 minutos

| Minuto | Actividad |
|---|---|
| 0–5 | Explicación del canvas |
| 5–15 | Completar contexto, tarea e inputs |
| 15–25 | Redactar prompt base |
| 25–32 | Probar en herramienta de IA |
| 32–38 | Mejorar instrucciones según resultado |
| 38–40 | Guardar versión 1 del asistente |

### Key takeaway

Un asistente útil no necesita ser perfecto. Necesita resolver una tarea real y mejorar con cada prueba.

### Slide count estimado

**5 slides**

1. Ejercicio principal: construye tu asistente  
2. Canvas del asistente  
3. Plantilla de prompt base  
4. Ejemplos de inputs por tipo de asistente  
5. Tiempo de construcción  

---

## Bloque 7: Pruebas, feedback y mejora del asistente  
### Duración: 25 minutos

### Objetivo

Enseñar a evaluar si el asistente realmente sirve y cómo iterarlo rápidamente.

### Dinámica

**Trabajo en parejas + discusión grupal**

Los participantes se agrupan en parejas.

Cada persona muestra a su compañero:

- Caso de uso elegido.
- Prompt base.
- Primera respuesta del asistente.
- Qué salió bien.
- Qué salió flojo.

El compañero prueba el asistente o revisa la salida usando esta checklist:

## Checklist de evaluación rápida

Puntuar del 1 al 5:

1. ¿La respuesta resuelve la tarea?
2. ¿Está en el formato correcto?
3. ¿Usa el tono adecuado?
4. ¿Es suficientemente específica?
5. ¿Evita inventar información?
6. ¿Podría usar esto mañana en mi startup?
7. ¿Qué instrucción falta?

Luego cada participante mejora su prompt agregando:

- Más contexto.
- Mejores restricciones.
- Ejemplos de buena respuesta.
- Preguntas cuando falte información.
- Formato más claro.
- Criterios de calidad.

### Frases útiles para mejorar el asistente

- “Antes de responder, hazme hasta 3 preguntas si falta información clave.”
- “No asumas datos que no te di.”
- “Dame 3 versiones: conservadora, creativa y directa.”
- “Explica por qué recomiendas cada opción.”
- “Prioriza acciones de bajo costo y alto impacto.”
- “Usa español latinoamericano, tono claro y sin tecnicismos.”
- “Entrega en tabla con columnas: idea, objetivo, mensaje, CTA.”
- “Actúa como editor crítico y mejora esta respuesta.”

### Key takeaway

El primer resultado casi nunca es el mejor. La ventaja está en saber iterar.

### Slide count estimado

**4 slides**

1. Cómo saber si tu asistente sirve  
2. Checklist de evaluación  
3. Cómo mejorar un prompt  
4. Trabajo en parejas  

---

## Bloque 8: Cómo integrarlo en tu día a día sin volverte loco  
### Duración: 15 minutos

### Objetivo

Mostrar cómo pasar de un experimento divertido a una herramienta útil en la operación diaria.

### Dinámica

**Charla práctica + mini plan de acción**

Explicar niveles de adopción:

### Nivel 1: Prompt guardado

Guardar el prompt en:

- Google Docs
- Notion
- Trello
- Slack
- WhatsApp contigo mismo

Ideal para empezar.

### Nivel 2: Asistente personalizado

Crear un Custom GPT, proyecto en Claude, Gem de Gemini o bot en Poe.

Ideal cuando se usa varias veces por semana.

### Nivel 3: Flujo semi-automatizado

Conectar con herramientas no-code como:

- Zapier
- Make
- Airtable
- Google Sheets
- Typeform
- Notion
- Slack

Ideal cuando la tarea ya está validada.

### Nivel 4: Automatización avanzada

Solo si ya hay volumen, proceso claro y ROI.

Puede incluir:

- Integración con CRM.
- Respuestas automáticas.
- Base de conocimiento.
- APIs.
- Workflows internos.

Luego los participantes completan un mini plan:

> “Durante los próximos 7 días voy a usar mi asistente para ______, al menos ____ veces, y mediré ______.”

Ejemplos de métricas:

- Tiempo ahorrado.
- Número de emails generados.
- Tasa de respuesta.
- Calidad de respuestas.
- Posts publicados.
- Ideas validadas.
- Tickets resueltos.
- Reuniones preparadas.

### Key takeaway

No automatices demasiado pronto. Primero valida que el asistente te ahorra tiempo o mejora resultados.

### Slide count estimado

**4 slides**

1. Del prompt al proceso  
2. Niveles de adopción  
3. Herramientas no-code para después  
4. Plan de 7 días  

---

## Bloque 9: Cierre, próximos pasos y recursos  
### Duración: 5 minutos

### Objetivo

Cerrar con energía, reforzar el aprendizaje y dar siguientes pasos claros.

### Dinámica

**Cierre rápido + compromiso**

Pedir que 2 o 3 voluntarios compartan:

- Qué asistente construyeron.
- Para qué lo van a usar esta semana.

Cierre del facilitador:

> “La pregunta ya no es si la IA puede ayudarte. La pregunta es qué tarea de tu startup vas a rediseñar primero.”

Invitar a escanear QR con recursos.

### Key takeaway

El asistente construido hoy es una versión 1. El valor aparece cuando lo usas, lo mejoras y lo incorporas a tu operación.

### Slide count estimado

**2 slides**

1. Tu reto de 7 días  
2. QR de recursos + gracias  

---

# 6. Resumen de slide count estimado

| Sección | Slides estimadas |
|---|---:|
| Bienvenida y mindset | 3 |
| Qué es un asistente de IA | 5 |
| Mapa de oportunidades | 4 |
| Elegir caso de uso | 4 |
| Break | 1 |
| Anatomía de un buen asistente | 6 |
| Ejercicio principal | 5 |
| Pruebas y mejora | 4 |
| Integración al día a día | 4 |
| Cierre | 2 |
| **Total estimado** | **38 slides** |

Recomendación: mantener entre **30 y 40 slides**, con poco texto y muchos ejemplos.

---

# 7. Recursos para llevar a casa

Crear una carpeta digital con QR que incluya:

## Plantillas

1. Canvas del Asistente de IA.
2. Plantilla de prompt base.
3. Checklist de evaluación del asistente.
4. Matriz impacto vs facilidad.
5. Plan de adopción de 7 días.
6. Plantilla para documentar casos de uso de IA.

## Prompts reutilizables

1. Prompt para ventas B2B.
2. Prompt para contenido de LinkedIn.
3. Prompt para atención a clientes.
4. Prompt para análisis de feedback.
5. Prompt para entrevistas de usuarios.
6. Prompt para pitch deck.
7. Prompt para investigación de mercado.
8. Prompt para preparar reuniones.
9. Prompt para responder objeciones.
10. Prompt para crear procesos internos.

## Herramientas sugeridas

### IA conversacional

- ChatGPT
- Claude
- Gemini
- Microsoft Copilot
- Perplexity
- Poe

### Organización

- Notion
- Google Docs
- Airtable
- Trello
- Coda

### Automatización no-code

- Zapier
- Make
- n8n
- Airtable Automations

### Captura de información

- Typeform
- Tally
- Google Forms

### Grabación y transcripción

- Otter
- Fireflies
- Fathom
- tl;dv

## Lecturas o guías prácticas

- Guía básica de prompting para founders.
- Guía de privacidad y datos sensibles.
- Checklist: cuándo automatizar y cuándo no.
- Ejemplos de asistentes por área de negocio.

---

# 8. Ejemplos de asistentes sugeridos para participantes

Para ayudar a quienes lleguen sin idea clara, ofrecer un menú de opciones.

## Ventas

### Asistente de prospección

Crea emails, mensajes de LinkedIn o WhatsApp para potenciales clientes.

### Asistente de objeciones

Ayuda a responder frases como:

- “Está muy caro.”
- “Lo voy a pensar.”
- “Ya usamos otra solución.”
- “No es prioridad ahora.”

### Asistente de preparación de llamadas

Resume el perfil del cliente, posibles dolores y preguntas para la reunión.

---

## Marketing

### Asistente de contenido founder-led

Convierte ideas del fundador en posts para LinkedIn, X, newsletter o blog.

### Asistente de campañas

Genera ideas de campañas simples para adquisición de usuarios.

### Asistente de análisis competitivo

Ayuda a comparar mensajes, precios y posicionamiento de competidores.

---

## Producto

### Asistente de entrevistas con usuarios

Genera preguntas, resume respuestas y detecta patrones.

### Asistente de priorización de features

Clasifica feedback según frecuencia, impacto y esfuerzo.

### Asistente de onboarding

Crea mensajes y guías para nuevos usuarios.

---

## Operaciones

### Asistente de documentación

Convierte procesos desordenados en checklists claros.

### Asistente de reportes

Transforma notas o métricas en resúmenes ejecutivos.

### Asistente de toma de decisiones

Organiza opciones, riesgos, beneficios y próximos pasos.

---

# 9. Recomendaciones para facilitar el workshop

## Mantener alta energía

- Usar ejemplos latinoamericanos: restaurantes, fintech, edtech, logística, ecommerce, servicios B2B.
- Evitar tecnicismos.
- Repetir: “No busquen perfecto, busquen útil.”
- Caminar por la sala durante ejercicios.
- Celebrar prototipos imperfectos.

## Cuidar tiempos

Este workshop puede desviarse fácilmente porque la gente se entusiasma. Usar frases como:

- “Tienen 5 minutos, no 50.”
- “Versión 1, no obra maestra.”
- “Si está medio feo pero funciona, vamos bien.”
- “Primero claridad, después automatización.”

## Ayudar a participantes bloqueados

Si alguien no sabe qué construir, sugerir uno de estos tres:

1. Asistente para crear emails de venta.
2. Asistente para generar posts de LinkedIn.
3. Asistente para responder preguntas frecuentes.

## Reglas de privacidad

Recordar:

- No subir datos sensibles de clientes.
- No pegar información confidencial sin anonimizar.
- No compartir claves, contratos privados o datos financieros delicados.
- Revisar todo antes de enviarlo a clientes.
- La IA puede equivocarse; el fundador sigue siendo responsable.

---

# 10. Resultado final esperado

Al terminar las 3 horas, cada participante debería tener algo como esto:

```text
Nombre:
Asistente de Prospección para Restaurantes

Caso de uso:
Crear emails de prospección para dueños de restaurantes independientes.

Prompt base:
Actúa como un experto en ventas B2B para startups SaaS en América Latina...

Inputs:
- Ciudad
- Tipo de restaurante
- Dolor principal
- Objetivo del mensaje
- Canal

Output:
Tabla con 3 versiones de email, asunto, mensaje y CTA.

Reglas:
- Máximo 120 palabras
- Tono cercano y directo
- No inventar datos
- Incluir llamada a demo de 15 minutos

Plan de 7 días:
Usarlo para crear 30 mensajes de prospección y medir tasa de respuesta.
```

Ese es el espíritu del workshop: **menos teoría, más construcción; menos hype, más utilidad real para la startup.**