# Claude Haiku 5.5 — startup_content/workshop_outline

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 18.229s | tokens_per_second: 217.3
- input_tokens: 315 | output_tokens: 3961
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas de bloque bien estructuradas.

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

# Workshop: "Construye tu Asistente de IA para tu Startup"
**Formato:** Presencial | **Duración:** 3 horas | **Audiencia:** 20-30 emprendedores early-stage no técnicos

---

## 1. Agenda General

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:15 | Bienvenida y "rompehielos" | 15 min |
| 0:15 - 0:40 | Bloque 1: IA sin humo (qué sí y qué no) | 25 min |
| 0:40 - 1:00 | Bloque 2: Mapea tu problema | 20 min |
| 1:00 - 1:10 | Pausa activa | 10 min |
| 1:10 - 1:30 | Bloque 3: Diseña tu asistente (prompt y personalidad) | 20 min |
| 1:30 - 2:20 | Bloque 4: Construye tu asistente (ejercicio principal) | 50 min |
| 2:20 - 2:35 | Bloque 5: Prueba, rompe y mejora | 15 min |
| 2:35 - 2:50 | Bloque 6: Demo rápida y feedback en plenaria | 15 min |
| 2:50 - 3:00 | Cierre, próximos pasos y recursos | 10 min |

---

## 2. Materiales y Preparación

**Antes del workshop (semana previa):**
- Cuenta gratuita o plan básico de un LLM (ChatGPT, Claude o Gemini) para cada participante, o acceso a una plataforma de creación de asistentes sin código (por ejemplo, GPTs personalizados, Claude Projects o Gems de Gemini).
- Email de pre-registro con una pregunta: "¿Cuál es el problema repetitivo que más te quita tiempo en tu startup?"
- Plantilla digital de "Ficha de Asistente" (Google Docs o Notion).
- Wifi confiable probado (mínimo 1 Mbps por persona en la sala; ten un hotspot de respaldo).
- Verifica que las cuentas funcionen en el espacio, con proyector y pantalla.

**En la sala:**
- Proyector, laptop del facilitador, audio para demos.
- Tarjetas/post-its de colores, marcadores, cinta adhesiva.
- Impresiones de la Ficha de Asistente (por si hay problemas de conectividad).
- Cronómetro visible.
- Stickers o badges para armar equipos de 3-4 personas.

**Checklist del facilitador:**
- [ ] Probar el ejercicio principal de principio a fin 48h antes
- [ ] Tener 2-3 ejemplos reales de asistentes listos como referencia
- [ ] Un asistente "de respaldo" preconfigurado por si alguien se queda atrás
- [ ] Lista de 3 preguntas "trampa" para el bloque de pruebas

---

## 3. Desarrollo por Bloque

### Bienvenida y rompehielos (0:00 - 0:15) · 15 min
**Objetivo:** Crear energía y romper el miedo técnico.
**Dinámica:** Ronda rápida. Cada persona dice su nombre, su startup y "una tarea que odio hacer". El facilitador las anota en un papelógrafo, y luego se revisan, porque ahí aparecen los candidatos para el asistente.
**Key takeaway:** "Aquí no necesitas saber programar. Necesitas saber explicar tu negocio."
**Slides estimadas:** 3

---

### Bloque 1: IA sin humo (0:15 - 0:40) · 25 min
**Objetivo:** Desmitificar qué es un asistente de IA y qué puede hacer hoy.
**Dinámica:** Charla corta con demo en vivo. Muestra un chat genérico vs. un asistente configurado con contexto de una startup ficticia. Mismo pregunta, respuestas radicalmente distintas.
**Contenido clave:**
- Qué es un LLM en lenguaje simple
- Qué un asistente tiene que un chat normal no tiene (instrucciones, contexto, archivos, tono)
- Lo que la IA hace bien y lo que hace mal (alucinaciones, datos desactualizados)
**Key takeaway:** "Un buen asistente es un buen brief, no un buen código."
**Slides estimadas:** 8

---

### Bloque 2: Mapea tu problema (0:40 - 1:00) · 20 min
**Objetivo:** Elegir un caso de uso concreto y acotado.
**Dinámica:** Ejercicio individual con la Ficha de Asistente. Cada participante completa:
1. Tarea repetitiva que quiere delegar
2. Quién la hace hoy y cuánto tiempo toma
3. Qué información necesita la IA para hacerla bien
4. Cómo sabría que el asistente "funcionó"
Luego, comparten en parejas (5 min).
**Key takeaway:** "Un asistente que hace una cosa bien vale más que uno que hace diez a medias."
**Slides estimadas:** 4

---

### Pausa activa (1:00 - 1:10) · 10 min
**Dinámica:** Pausa con café. El facilitador revisa rápido las fichas y arma los equipos según afinidad de problemas (marketing, ventas, operaciones, atención al cliente).

---

### Bloque 3: Diseña tu asistente (1:10 - 1:30) · 20 min
**Objetivo:** Escribir las instrucciones base: rol, tono, reglas y formato.
**Dinámica:** Mini-charla de 7 min con la "fórmula" de un buen system prompt:
- **Rol:** quién es el asistente
- **Contexto:** sobre tu startup, producto y cliente
- **Tarea:** qué debe hacer exactamente
- **Reglas:** qué no debe hacer
- **Formato:** cómo debe responder
Después, cada equipo redacta su primera versión en 10 min.
**Key takeaway:** "Si no lo escribes, la IA lo inventa."
**Slides estimadas:** 5

---

### Bloque 4: Construye tu asistente (1:30 - 2:20) · 50 min
**Objetivo:** Tener un asistente funcional al final del bloque.
**Dinámica:** Ejercicio principal (ver sección 4). Los participantes construyen en vivo con acompañamiento. El facilitador pasa por las mesas y resuelve bloqueos.
**Key takeaway:** "Lo estás construyendo tú, no lo estás comprando."
**Slides estimadas:** 3 (instrucciones paso a paso)

---

### Bloque 5: Prueba, rompe y mejora (2:20 - 2:35) · 15 min
**Objetivo:** Validar el asistente con casos reales y casos difíciles.
**Dinámica:** Cada equipo prueba su asistente con 3 preguntas: una fácil, una típica y una "trampa" (pregunta ambigua, fuera de alcance o que pida inventar datos). Anotan dónde falla y ajustan el prompt.
**Key takeaway:** "Un asistente se entrena probándolo, no pensándolo."
**Slides estimadas:** 2

---

### Bloque 6: Demo rápida y feedback (2:35 - 2:50) · 15 min
**Objetivo:** Compartir aprendizajes y recibir retroalimentación.
**Dinámica:** Cada equipo muestra su asistente en 60-90 segundos: problema, demo en vivo y un aprendizaje. El resto del grupo da una pregunta o sugerencia.
**Key takeaway:** "Lo que aprendiste de tus errores vale más que lo que funcionó a la primera."
**Slides estimadas:** 2

---

### Cierre (2:50 - 3:00) · 10 min
**Objetivo:** Asegurar la acción después del workshop.
**Dinámica:** Compromiso personal en una tarjeta: "Esta semana voy a usar mi asistente para ___ y voy a medir ___." Se pega en un mural. Agradecimientos y recursos.
**Key takeaway:** "El asistente que no usas esta semana no sirve de nada."
**Slides estimadas:** 2

---

## 4. Ejercicio Principal: "Mi Asistente en 50 minutos"

**Meta:** Cada participante termina con un asistente funcional para una tarea real de su startup.

**Paso 1 (10 min) - Define el caso:** Usa la Ficha de Asistente del bloque 2.

**Paso 2 (15 min) - Escribe las instrucciones:** Usa la fórmula Rol + Contexto + Tarea + Reglas + Formato. Incluye 2-3 ejemplos de entradas y salidas esperadas.

**Paso 3 (10 min) - Carga contexto:** Sube documentos clave (pitch, FAQs, guía de marca, precios) o pega la información más relevante en el asistente.

**Paso 4 (10 min) - Prueba inicial:** Haz 3 consultas reales y anota qué falla.

**Paso 5 (5 min) - Ajuste:** Modifica una regla o ejemplo para corregir el error más grave.

**Entregable:** Un asistente con nombre, instrucciones escritas y un enlace o captura de pantalla de su prueba.

**Ejemplos de casos que funcionan bien:**
- Respondedor de preguntas frecuentes de clientes
- Generador de borradores de emails de ventas en tu tono
- Asistente de investigación de competencia
- Redactor de descripciones de producto
- Filtro y clasificador de leads
- Coach de pitch que cuestiona tu propuesta de valor

---

## 5. Recursos para Llevar a Casa

- **Plantilla de System Prompt** (en Google Docs) con la fórmula completa y 3 ejemplos por industria.
- **Ficha de Asistente** en blanco para repetir el ejercicio con otros procesos.
- **Checklist de "Prueba de calidad"** de 10 preguntas para evaluar cualquier asistente.
- **Guía de privacidad básica:** qué datos de clientes nunca subir a herramientas públicas, y alternativas para casos sensibles.
- **Lista de herramientas sin código** organizadas por presupuesto (gratis, medio, pago).
- **Ruta de aprendizaje de 4 semanas** para seguir mejorando tu asistente.
- **Acceso a comunidad** (grupo de WhatsApp o Slack) para compartir casos y prompts.

---

## 6. Estimado de Slides por Sección

| Sección | Slides |
|---------|--------|
| Bienvenida y rompehielos | 3 |
| Bloque 1: IA sin humo | 8 |
| Bloque 2: Mapea tu problema | 4 |
| Bloque 3: Diseña tu asistente | 5 |
| Bloque 4: Construye tu asistente | 3 |
| Bloque 5: Prueba y mejora | 2 |
| Bloque 6: Demo y feedback | 2 |
| Cierre y recursos | 2 |
| **Total** | **~29 slides** |

*Nota: Mantén las slides visuales y mínimas. El ejercicio es el protagonista; la presentación es el apoyo.*