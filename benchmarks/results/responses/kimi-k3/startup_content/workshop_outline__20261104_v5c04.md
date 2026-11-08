# Kimi K3 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.69 | quality: 9.72
- latency_total: 148.296s | tokens_per_second: 36.8
- input_tokens: 235 | output_tokens: 5455
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

¡Claro! Aquí tienes un outline completo, pensado para un workshop presencial de 3 horas, dinámico, útil y muy accionable para emprendedores early-stage no técnicos.

# Workshop: “Construye tu Asistente de IA para tu Startup - Workshop Práctico”

## Enfoque general
- **Audiencia:** emprendedores early-stage no técnicos
- **Formato:** presencial, participativo, hands-on
- **Objetivo del taller:** que cada participante salga con un **primer asistente de IA funcional** para su startup, construido con herramientas no-code/low-code
- **Tono:** energético, simple, directo, cero humo
- **Promesa práctica:** “En 3 horas vas a entender qué puede hacer la IA por tu startup y vas a construir una primera versión usable”

---

# 1. Agenda detallada con tiempos

**Duración total:** 3 horas

## Agenda
1. **Bienvenida + encuadre rápido** — 10 min  
2. **Qué es un asistente de IA y qué puede hacer por tu startup** — 20 min  
3. **Mapa de casos de uso para startups** — 20 min  
4. **Demo en vivo: cómo se construye un asistente sin programar** — 20 min  
5. **Ejercicio principal: diseña y construye tu asistente de IA** — 60 min  
6. **Break** — 10 min  
7. **Testeo en parejas + mejora rápida** — 20 min  
8. **Cómo llevarlo a producción de forma simple** — 15 min  
9. **Errores comunes, límites y buenas prácticas** — 10 min  
10. **Cierre, compromisos y próximos pasos** — 15 min  

**Total:** 180 minutos

---

# 2. Materiales necesarios

## Para el facilitador
- Proyector o pantalla
- Micrófono si la sala es grande
- Pizarra o papelógrafo
- Marcadores
- Timer visible
- Laptop con acceso a internet
- Cuentas activas en 1 o 2 herramientas no-code de IA
- 2 o 3 demos preparadas
- Plantillas impresas o digitales
- Formulario de feedback final
- Código QR para recursos

## Para los participantes
- Laptop o tablet por persona
- Buena conexión wifi
- Acceso a una herramienta de IA tipo:
  - ChatGPT
  - Claude
  - Gemini
  - Zapier / Make opcional
  - Notion / Google Docs
  - Airtable / Google Sheets
- Documento base con:
  - descripción de su startup
  - cliente ideal
  - principales tareas repetitivas
  - preguntas frecuentes de clientes
  - tono de comunicación deseado

## Materiales impresos recomendados
- Canvas “Diseña tu asistente de IA”
- Ficha de casos de uso
- Checklist de calidad del asistente
- Hoja de prompts base
- Hoja de próximos pasos

## Preparación previa sugerida
Enviar 2-3 días antes:
- email con objetivo del workshop
- pedir que traigan laptop
- pedir que traigan:
  - pitch corto de su startup
  - 3 tareas repetitivas que hacen hoy
  - 5 preguntas frecuentes de clientes o usuarios
- sugerir crear cuenta gratuita en una herramienta de IA

---

# 3. Desarrollo por bloques

---

## Bloque 1: Bienvenida + encuadre rápido
**Duración:** 10 min  
**Objetivo:** activar a la sala, bajar ansiedad y alinear expectativas  
**Dinámica:** charla breve + mini dinámica de levantar la mano + encuadre del resultado esperado

### Contenido
- Presentación del facilitador
- Regla del taller: “salimos con algo construido, no solo con ideas”
- Qué sí y qué no veremos
- Encuesta rápida:
  - ¿Quién ya usa IA a diario?
  - ¿Quién la usa para ventas?
  - ¿Quién para soporte?
  - ¿Quién siente que “debería usarla más”?

### Key takeaway
**La IA no es magia: es una forma práctica de ahorrar tiempo, responder mejor y vender más.**

### Slides estimados
**3-4 slides**

---

## Bloque 2: Qué es un asistente de IA y qué puede hacer por tu startup
**Duración:** 20 min  
**Objetivo:** explicar de forma simple qué es un asistente de IA aplicado a negocios  
**Dinámica:** charla + ejemplos reales + micro-interacción

### Contenido
- Qué es un asistente de IA en lenguaje humano
- Diferencia entre:
  - chatbot tradicional
  - asistente con IA generativa
  - automatización con IA
- Qué puede hacer hoy un asistente para una startup:
  - responder FAQs
  - calificar leads
  - redactar propuestas
  - resumir conversaciones
  - ayudar con onboarding
  - generar contenido
  - organizar información interna
- Qué NO debe hacer todavía:
  - decisiones críticas sin supervisión
  - promesas comerciales no validadas
  - manejo delicado de datos sin controles

### Ejemplos para mencionar
- Asistente para responder clientes en WhatsApp/web
- Asistente para preparar reuniones comerciales
- Asistente para soporte inicial
- Asistente para crear contenido en redes
- Asistente para organizar conocimiento interno

### Key takeaway
**Un asistente útil no “hace de todo”: resuelve muy bien una tarea concreta.**

### Slides estimados
**5-6 slides**

---

## Bloque 3: Mapa de casos de uso para startups
**Duración:** 20 min  
**Objetivo:** ayudar a cada participante a elegir un caso de uso realista y valioso  
**Dinámica:** ejercicio individual guiado + compartir en voz alta

### Contenido
Presentar 6 categorías de casos de uso:
1. **Ventas**
   - responder interesados
   - calificar leads
   - preparar follow-ups
2. **Marketing**
   - ideas de contenido
   - copies
   - newsletters
3. **Soporte**
   - FAQs
   - guías de uso
   - resolución inicial de problemas
4. **Operaciones**
   - resumir reuniones
   - documentar procesos
   - organizar información
5. **Producto**
   - onboarding
   - ayuda contextual
   - feedback de usuarios
6. **Fundador/a**
   - preparar pitches
   - investigar competidores
   - redactar emails difíciles

### Ejercicio rápido
Cada persona elige:
- 1 problema frecuente
- 1 tarea repetitiva
- 1 caso de uso para el workshop

### Pregunta guía
**“¿Qué tarea de tu startup te quita tiempo todas las semanas y podría responderse con instrucciones claras + contexto?”**

### Key takeaway
**El mejor primer asistente no es el más sofisticado, es el que resuelve una tarea frecuente y concreta.**

### Slides estimados
**5 slides + 1 plantilla de ejercicio**

---

## Bloque 4: Demo en vivo: cómo se construye un asistente sin programar
**Duración:** 20 min  
**Objetivo:** mostrar que sí se puede construir algo útil sin saber programar  
**Dinámica:** demo en vivo + narración paso a paso

### Contenido
Mostrar en vivo una de estas opciones:
- Custom GPT / assistant con instrucciones
- Claude Project
- Gemini Gem
- flujo simple con Zapier/Make + IA
- asistente conectado a documentos o base de conocimiento

### Estructura de la demo
1. Definir objetivo del asistente
2. Escribir rol e instrucciones
3. Cargar contexto de la startup
4. Definir tono y límites
5. Probar con 3 ejemplos reales
6. Mejorar respuesta con ajustes simples

### Mensaje clave
No se trata de “programar”, sino de:
- dar buen contexto
- definir tareas
- poner límites
- probar y ajustar

### Key takeaway
**Construir un asistente inicial es más parecido a entrenar a un buen becario que a desarrollar software.**

### Slides estimados
**4-5 slides + demo en pantalla**

---

## Bloque 5: Ejercicio principal — diseña y construye tu asistente de IA
**Duración:** 60 min  
**Objetivo:** que cada participante construya una primera versión funcional de su asistente  
**Dinámica:** trabajo individual guiado + soporte del facilitador + plantillas

### Este es el corazón del workshop

### Resultado esperado
Cada participante termina con:
- nombre del asistente
- objetivo claro
- caso de uso definido
- instrucciones base
- prompt o configuración inicial
- 3 pruebas realizadas
- 1 mejora aplicada

### Paso a paso del ejercicio

#### Paso 1: Elegir el caso de uso — 10 min
Completar:
- Mi asistente ayudará a: ______
- El usuario principal es: ______
- La tarea que resolverá es: ______
- El resultado ideal es: ______

#### Paso 2: Definir personalidad y alcance — 10 min
Completar:
- tono: formal / cercano / directo / experto / simple
- qué sí puede hacer
- qué no debe hacer
- cuándo debe decir “no tengo suficiente información”
- cuándo debe derivar a una persona

#### Paso 3: Cargar contexto — 15 min
Agregar:
- descripción de la startup
- cliente ideal
- productos/servicios
- FAQs
- políticas básicas
- ejemplos de buenas respuestas

#### Paso 4: Crear instrucciones base — 10 min
Usar plantilla:
- rol
- objetivo
- contexto
- formato de respuesta
- restricciones
- ejemplos

#### Paso 5: Probar y mejorar — 15 min
Probar con:
- 1 pregunta fácil
- 1 pregunta ambigua
- 1 caso real difícil

Ajustar:
- claridad
- tono
- límites
- precisión

### Rol del facilitador
- circular por la sala
- ayudar a destrabar casos vagos
- empujar a que elijan algo simple y útil
- evitar que intenten hacer “un asistente para todo”

### Frases útiles para facilitación
- “Si tu asistente intenta hacer 10 cosas, no hará bien ninguna.”
- “Empieza por una tarea repetitiva, no por la más épica.”
- “Un buen asistente dice claramente qué sabe y qué no sabe.”

### Key takeaway
**Un asistente útil nace de un caso de uso claro + buen contexto + pruebas reales.**

### Slides estimados
**6-8 slides de guía + plantilla de trabajo**

---

## Bloque 6: Break
**Duración:** 10 min  
**Objetivo:** pausa activa  
**Dinámica:** break libre

### Recomendación
Dejar una consigna en pantalla:
**“Durante el break, piensa en una pregunta real que un cliente te haría y que tu asistente debería responder bien.”**

### Slides estimados
**1 slide**

---

## Bloque 7: Testeo en parejas + mejora rápida
**Duración:** 20 min  
**Objetivo:** mejorar el asistente con feedback real de otra persona  
**Dinámica:** trabajo en parejas + ronda de pruebas + ajustes

### Dinámica
- Cada persona prueba el asistente de su compañero
- Usar una checklist simple:
  - ¿se entiende qué hace?
  - ¿responde con claridad?
  - ¿suena al tono de la marca?
  - ¿sabe cuándo no responder?
  - ¿te ahorraría tiempo de verdad?

### Feedback estructurado
Cada pareja responde:
1. Qué funcionó bien
2. Qué fue confuso
3. Qué mejoraría primero

### Luego
Cada participante hace 1 mejora concreta

### Key takeaway
**La mejora más rápida viene de probar tu asistente con alguien que no conoce tu negocio.**

### Slides estimados
**3-4 slides**

---

## Bloque 8: Cómo llevarlo a producción de forma simple
**Duración:** 15 min  
**Objetivo:** mostrar caminos realistas para usarlo en la operación diaria  
**Dinámica:** charla + ejemplos + mini mapa de implementación

### Contenido
Opciones simples según nivel de madurez:
- uso interno en ChatGPT/Claude/Notion
- asistente para founders o equipo
- integración con formularios, correo o CRM
- base de conocimiento en Notion/Docs/Airtable
- automatizaciones simples con Zapier/Make
- futuro: embed en web o WhatsApp con soporte técnico

### Regla práctica
Empezar en este orden:
1. uso manual
2. uso repetido
3. plantilla estable
4. semi-automatización
5. integración

### Key takeaway
**No necesitas lanzar perfecto: necesitas empezar a usarlo en una tarea real esta semana.**

### Slides estimados
**4-5 slides**

---

## Bloque 9: Errores comunes, límites y buenas prácticas
**Duración:** 10 min  
**Objetivo:** evitar expectativas irreales y malas implementaciones  
**Dinámica:** charla rápida + ejemplos de errores

### Errores comunes
- querer automatizar todo desde el día 1
- no dar contexto suficiente
- no definir límites
- no probar con casos reales
- usar datos sensibles sin criterio
- esperar respuestas perfectas siempre
- no medir si realmente ahorra tiempo

### Buenas prácticas
- empezar con un solo caso de uso
- documentar ejemplos buenos y malos
- revisar respuestas semanalmente
- mantener supervisión humana
- actualizar contexto cada cierto tiempo
- medir impacto: tiempo ahorrado, respuestas resueltas, leads calificados

### Key takeaway
**La IA funciona mejor como copiloto supervisado, no como reemplazo total desde el primer día.**

### Slides estimados
**3-4 slides**

---

## Bloque 10: Cierre, compromisos y próximos pasos
**Duración:** 15 min  
**Objetivo:** cerrar con acción concreta y sensación de logro  
**Dinámica:** compartir en plenaria + compromiso individual + cierre energético

### Dinámica
- Invitar a 3-5 participantes a compartir:
  - qué construyeron
  - qué caso de uso eligieron
  - qué aprendieron
- Cada participante completa:
  - “Mi asistente me ayudará con…”
  - “Lo voy a probar esta semana en…”
  - “La primera mejora que haré es…”

### Cierre sugerido
Frase final:
**“Hoy no viniste a aprender sobre IA. Viniste a construir una primera herramienta que ya puede trabajar para tu startup.”**

### Key takeaway
**La ventaja no está en saber más teoría, sino en usar IA antes y mejor que tu competencia.**

### Slides estimados
**3-4 slides**

---

# 4. Ejercicio principal del workshop

## Nombre del ejercicio
**“Construye tu primer asistente útil en 60 minutos”**

## Objetivo
Que cada participante cree una versión inicial de un asistente de IA para una tarea concreta de su startup.

## Instrucciones para participantes
Vas a construir un asistente que te ayude con una de estas opciones:
- responder preguntas frecuentes
- calificar leads
- redactar respuestas comerciales
- generar contenido
- resumir información
- ayudar en onboarding
- organizar conocimiento interno

## Entregable
Al finalizar debes tener:
1. nombre del asistente
2. objetivo
3. usuario principal
4. tarea principal
5. instrucciones base
6. contexto cargado
7. 3 pruebas hechas
8. 1 mejora aplicada

## Plantilla del ejercicio

### 1. Identidad del asistente
- Nombre del asistente:
- Rol:
- Objetivo principal:
- Usuario principal:
- Problema que resuelve:

### 2. Alcance
- Qué sí debe hacer:
- Qué no debe hacer:
- Cuándo debe pedir más información:
- Cuándo debe derivar a una persona:

### 3. Contexto de negocio
- Qué hace mi startup:
- A quién ayuda:
- Productos/servicios principales:
- Preguntas frecuentes:
- Tono deseado:
- Información importante que debe conocer:

### 4. Prompt/instrucción base
**Plantilla sugerida:**

> Actúa como [rol]. Tu objetivo es ayudar a [tipo de usuario] a [resultado deseado].  
> Contexto: mi startup se dedica a [descripción breve].  
> Debes responder en un tono [tono].  
> Si la información no es suficiente, haz una pregunta antes de responder.  
> No inventes datos. Si no sabes algo, dilo claramente.  
> Entrega respuestas en formato [bullets / pasos / tabla / mensaje corto].  
> Estas son las reglas importantes: [reglas].  
> Estos son ejemplos de buenas respuestas: [ejemplos].

### 5. Pruebas
Probar con:
- una pregunta frecuente
- una pregunta confusa
- una solicitud real difícil

### 6. Mejora
- Qué falló:
- Qué ajusté:
- Qué haré después del taller:

---

# 5. Recursos para llevar a casa

Preparar un kit digital con QR o link corto:

## Recursos recomendados
1. **Plantilla editable del asistente de IA**
2. **Checklist de calidad**
   - objetivo claro
   - tono definido
   - límites claros
   - contexto cargado
   - pruebas realizadas
3. **Banco de prompts para startups**
   - ventas
   - soporte
   - marketing
   - operaciones
   - fundraising
4. **Guía rápida de herramientas no-code**
   - ChatGPT
   - Claude
   - Gemini
   - Notion AI
   - Zapier
   - Make
   - Airtable
5. **Canvas “Diseña tu asistente”**
6. **Checklist de seguridad y buenas prácticas**
7. **Plan de acción de 7 días**
   - día 1: elegir caso de uso
   - día 2: mejorar instrucciones
   - día 3: probar con 5 casos reales
   - día 4: ajustar tono y límites
   - día 5: usarlo en una tarea real
   - día 6: medir tiempo ahorrado
   - día 7: decidir siguiente paso

## Bonus opcional
- video corto con la demo grabada
- acceso a una comunidad o grupo de seguimiento
- sesión opcional de office hours 1 semana después

---

# 6. Slide count estimado por sección

## Total estimado
**38-48 slides**  
Para un workshop práctico, lo ideal es mantener las slides ligeras y usar más tiempo en ejercicios que en presentación.

## Desglose sugerido
1. Bienvenida + encuadre — **3-4 slides**
2. Qué es un asistente de IA — **5-6 slides**
3. Mapa de casos de uso — **5 slides**
4. Demo en vivo — **4-5 slides**
5. Ejercicio principal — **6-8 slides**
6. Break — **1 slide**
7. Testeo en parejas — **3-4 slides**
8. Cómo llevarlo a producción — **4-5 slides**
9. Errores y buenas prácticas — **3-4 slides**
10. Cierre y próximos pasos — **3-4 slides**

---

# Recomendaciones de facilitación

## Para que funcione con 20-30 personas
- Usar ejemplos latinos reales y cercanos
- Evitar tecnicismos innecesarios
- Tener 2 helpers si es posible
- Dar instrucciones por pasos, no todo junto
- Usar timer visible en ejercicios
- Hacer check-ins rápidos:
  - “¿Quién ya eligió su caso de uso?”
  - “¿Quién ya hizo su primera prueba?”
- Tener casos de respaldo para quienes se bloqueen:
  - asistente de FAQs
  - asistente para responder leads
  - asistente para crear posts
  - asistente para resumir reuniones

## Señales de que el workshop va bien
- la sala está construyendo, no solo escuchando
- la gente prueba y se ríe de las primeras respuestas raras
- empiezan a decir “esto sí me ahorraría tiempo”
- terminan con algo concreto, no con ideas vagas

---

Si quieres, en el siguiente paso también te puedo armar:
1. **la presentación slide by slide**,  
2. **las plantillas imprimibles del workshop**, o  
3. **el guion del facilitador minuto a minuto**.