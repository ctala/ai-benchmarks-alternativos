# Claude Fable 5.2 — startup_content/workshop_outline

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.59 | quality: 9.72
- latency_total: 65.712s | tokens_per_second: 97.9
- input_tokens: 316 | output_tokens: 6432
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

# Construye tu Asistente de IA para tu Startup: Workshop Práctico

**Formato:** presencial, 3 horas, 20-30 emprendedores early-stage no técnicos.
**Promesa:** nadie se va sin un asistente funcionando, hecho con sus propias manos y sin escribir código.

---

## 1. Agenda (180 min)

| # | Hora | Bloque | Min | Dinámica | Slides |
|---|------|--------|-----|----------|--------|
| 1 | 0:00 | Arranque con demo en vivo | 15 | Demo + rompehielos | 4 |
| 2 | 0:15 | IA sin humo | 20 | Charla interactiva | 6 |
| 3 | 0:35 | Elige tu batalla | 20 | Ejercicio individual + parejas | 4 |
| 4 | 0:55 | La fórmula CREAR | 25 | Charla + demo en vivo | 7 |
| – | 1:20 | Break | 10 | Café y networking | 1 |
| 5 | 1:30 | Build Sprint | 45 | Ejercicio principal | 4 |
| 6 | 2:15 | Rompe el asistente de tu vecino | 20 | Prueba cruzada en parejas | 3 |
| 7 | 2:35 | Showcase | 15 | Demos de participantes | 1 |
| 8 | 2:50 | Cierre y plan de 7 días | 10 | Charla + compromiso | 5 |

**Total: 180 min, unos 35 slides.** Son pocos a propósito: aquí se viene a construir.

---

## 2. Materiales

**Preparar antes (facilitador)**
- **Herramienta:** elige una principal y una de respaldo entre ChatGPT (GPTs/Proyectos), Claude (Proyectos) o Gemini (Gems). Verifica una semana antes qué permite el plan gratuito de cada una, porque cambia seguido.
- **Plan B universal:** pegar el prompt maestro al inicio de un chat normal. Funciona en cualquier herramienta gratuita.
- **Asistente de ejemplo:** uno ya construido para una startup ficticia latinoamericana (por ejemplo "Kiwi", una app de delivery de fruta), más capturas de pantalla por si falla la demo.
- **Impresos:** Canvas CREAR (uno por persona) y menú de casos de uso.
- **Apoyo:** un mentor por cada 8-10 personas para destrabar durante el sprint.
- **Digital:** QR con la carpeta de recursos y un grupo de WhatsApp del workshop.

**Sala**
- Proyector, wifi probado con más de 30 dispositivos y un hotspot de respaldo.
- Regletas, mesas en islas de 4 a 6 personas y un timer visible.
- Post-its y plumones.

**Email a participantes (3 días antes)**
- Traer laptop cargada. Quien no tenga trabaja en pareja.
- Crear la cuenta gratuita en la herramienta elegida.
- Traer 1 o 2 documentos de su startup (pitch, FAQ, descripción del producto), sin datos sensibles ni información personal de clientes.

---

## 3. Bloque por bloque

### Bloque 1: Arranque con demo en vivo (15 min)
- **Objetivo:** generar energía y mostrar el destino final en los primeros 5 minutos.
- **Dinámica:**
  - Demo de 5 minutos, sin introducción: el asistente de "Kiwi" responde a un cliente molesto, redacta un post y critica un pitch.
  - Rompehielos de pie: "¿Qué tarea de tu startup te roba más horas a la semana?". Cada uno la escribe en un post-it y lo pega en la pared.
  - Reglas del juego: cero vergüenza, cero código, todos construyen.
- **Key takeaway:** "Hoy no vienes a escuchar sobre IA, vienes a irte con una funcionando."

### Bloque 2: IA sin humo (20 min)
- **Objetivo:** dar el mínimo de conceptos necesario para construir con criterio.
- **Dinámica:** charla con votación a mano alzada.
  - Chat normal vs. asistente: el asistente ya conoce tu negocio y no hay que explicarle todo cada vez.
  - Analogía: es un practicante brillante en su primer día. Sabe mucho del mundo y nada de tu startup.
  - Qué hace bien (redactar, resumir, simular, estructurar) y qué hace mal (inventa datos con total seguridad, no conoce tus números).
  - Tres ejemplos reales: respuestas de WhatsApp, calificación de leads y simulación de inversor.
- **Key takeaway:** "La IA no reemplaza tu criterio, lo multiplica. Tú eres el jefe y revisas su trabajo."

### Bloque 3: Elige tu batalla (20 min)
- **Objetivo:** que cada persona salga con un solo caso de uso concreto.
- **Dinámica:**
  - 5 min: presentación del menú de casos (sección 4).
  - 7 min: cada uno completa la frase "Mi asistente ayuda a ___ a hacer ___ para lograr ___".
  - 8 min: en parejas se cuentan el caso y el compañero lo reta: "¿se puede hacer más específico?".
- **Filtro:** la tarea debe ser frecuente (semanal o más), basada en texto y de bajo riesgo si sale imperfecta.
- **Key takeaway:** "Un asistente que hace una cosa bien le gana a uno que hace diez cosas mal."

### Bloque 4: La fórmula CREAR (25 min)
- **Objetivo:** enseñar la receta de un buen asistente y verla aplicada en vivo.
- **Dinámica:** 10 min de charla y 15 min de demo construyendo desde cero.
  - **C, Contexto:** qué hace tu startup, para quién y qué la diferencia.
  - **R, Rol:** quién es el asistente ("eres el agente de soporte de Kiwi").
  - **E, Ejemplos:** 2 o 3 muestras de respuestas ideales.
  - **A, Acciones:** qué debe hacer, paso a paso.
  - **R, Reglas:** tono, formato, límites y qué hacer cuando no sabe ("di que no sabes y deriva a un humano").
- **Demo:** primero el asistente con instrucciones pobres, luego con CREAR completo. Lo que convence es ver el antes y el después.
- **Key takeaway:** "La calidad de tu asistente depende de la calidad de tus instrucciones. Si le das contexto genérico, te dará respuestas genéricas."

### Break (10 min)
Durante el café, cada uno busca a alguien con un post-it de dolor parecido al suyo.

### Bloque 5: Build Sprint (45 min)
- **Objetivo:** que todos tengan un asistente funcionando.
- **Dinámica:** ejercicio principal (sección 4), con música, timer visible y mentores circulando.
- **Key takeaway:** "La primera versión siempre es fea. Lo que importa es iterar: probar, ajustar y probar de nuevo."

### Bloque 6: Rompe el asistente de tu vecino (20 min)
- **Objetivo:** probar el asistente con un usuario real y mejorarlo con ese feedback.
- **Dinámica:**
  - 12 min (6 por lado): intercambian laptops y cada uno intenta hacer fallar al otro asistente con preguntas fuera de tema, un cliente grosero, datos que no existen o pedidos de descuentos inventados.
  - 8 min: cada uno ajusta sus Reglas según lo que falló.
- **Key takeaway:** "Mejor que lo rompa tu vecino hoy a que lo rompa un cliente mañana."

### Bloque 7: Showcase (15 min)
- **Objetivo:** celebrar e inspirar con casos de pares.
- **Dinámica:** 4 o 5 voluntarios proyectan su asistente durante 2 minutos cada uno: qué hace, una prueba en vivo y qué aprendieron. Termina con aplausos y un premio simbólico al "asistente más útil", votado por la sala.
- **Key takeaway:** "Si ellos lo hicieron en 45 minutos, imagina lo que logras en una semana."

### Bloque 8: Cierre y plan de 7 días (10 min)
- **Objetivo:** convertir el workshop en hábito.
- **Dinámica:**
  - Reto de 7 días: usar el asistente a diario, anotar fallas y mejorar las instrucciones una vez.
  - Tres advertencias: no subir datos sensibles, verificar siempre cifras y hechos, y revisar todo antes de que llegue a un cliente.
  - Compromiso: cada uno escribe en el grupo de WhatsApp para qué usará su asistente esta semana.
  - QR de recursos, encuesta de 1 minuto y foto grupal.
- **Key takeaway:** "Tu asistente es como un empleado nuevo: mejora cada semana si lo entrenas."

---

## 4. Ejercicio principal: "Mi asistente en 45 minutos"

**Menú de casos de uso (cada uno elige uno)**
1. **Soporte:** responde las preguntas frecuentes de clientes con tu tono, listo para copiar a WhatsApp.
2. **Ventas:** redacta mensajes de prospección y seguimiento.
3. **Contenido:** crea posts con la voz de tu marca.
4. **Inversor simulado:** critica tu pitch y hace preguntas difíciles.
5. **Cofounder crítico:** cuestiona tus decisiones y te ayuda a priorizar.
6. **Analista de clientes:** resume entrevistas y detecta patrones.

**Paso a paso**

| Min | Paso | Entregable |
|-----|------|-----------|
| 0-10 | Llenar el Canvas CREAR en papel | Canvas completo |
| 10-20 | Pasarlo a la herramienta y subir 1 o 2 documentos | Asistente v1 |
| 20-30 | Probarlo con 3 situaciones reales | Lista de fallas |
| 30-40 | Ajustar instrucciones y volver a probar | Asistente v2 |
| 40-45 | Ponerle nombre y preparar la mejor prueba para mostrar | Listo para el bloque 6 |

**Plantilla base (va impresa y en la carpeta digital)**

```
CONTEXTO: Trabajas para [startup]. Hacemos [qué] para [quién].
Nos diferencia [qué nos hace distintos].
ROL: Eres [rol] con experiencia en [área].
ACCIONES: Tu trabajo es [tarea]. Paso a paso: 1)… 2)… 3)…
EJEMPLOS: Así se ve una buena respuesta: [ejemplo 1] [ejemplo 2]
REGLAS: Tono [cercano/formal]. Máximo [X] líneas.
Nunca [límite]. Si no sabes algo, dilo y sugiere contactar a [persona/canal].
```

**Criterio de éxito:** el asistente responde bien 3 situaciones reales del negocio. Con eso basta para una primera versión.

**Red de seguridad:** quien se trabe con la herramienta pega la plantilla en un chat normal. Así todos terminan con algo funcionando.

---

## 5. Recursos para llevar a casa

- **Canvas CREAR** en PDF editable.
- **6 plantillas de prompt**, una por caso de uso del menú.
- **Checklist "Antes de usarlo con clientes":** privacidad, verificación de datos y revisión humana.
- **Guía de 1 página** para mejorar el asistente en 15 minutos a la semana.
- **Reto de 7 días** con una microtarea diaria.
- **Slides del workshop** y enlace al asistente demo, para que vean sus instrucciones.
- **Grupo de WhatsApp** activo 30 días para dudas y compartir avances.
- **Ruta de siguientes pasos:** más documentos de conocimiento, luego compartirlo con el equipo y después automatizaciones (WhatsApp Business, Zapier/Make).

---

## 6. Slides por sección

| Sección | Slides | Contenido |
|---------|--------|-----------|
| 1. Arranque | 4 | Título, promesa, pregunta rompehielos, reglas |
| 2. IA sin humo | 6 | Chat vs. asistente, analogía del practicante, hace bien/mal, 3 casos |
| 3. Elige tu batalla | 4 | Menú, frase a completar, filtro, instrucciones de parejas |
| 4. Fórmula CREAR | 7 | Uno por letra, antes/después, transición a la demo |
| Break | 1 | Timer y consigna de networking |
| 5. Build Sprint | 4 | Pasos, plantilla, criterio de éxito, timer |
| 6. Prueba cruzada | 3 | Instrucciones, ideas para romperlo, ajuste |
| 7. Showcase | 1 | Formato de demo de 2 minutos |
| 8. Cierre | 5 | Reto de 7 días, advertencias, QR, encuesta, gracias y foto |
| **Total** | **35** | |

---

**Tip de facilitación:** el Build Sprint es el corazón del workshop. Si vas atrasado, recorta el bloque 2, nunca el sprint.