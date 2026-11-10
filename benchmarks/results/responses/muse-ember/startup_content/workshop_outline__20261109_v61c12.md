# Muse Ember — startup_content/workshop_outline

- model_id: `meta/muse-ember`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 10.815s | tokens_per_second: 457.9
- input_tokens: 201 | output_tokens: 4952
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el workshop.

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

¡Perfecto! Aquí tienes el outline listo para ejecutar. Pensado para emprendedores no-técnicos en LatAm: cero código, cero teoría aburrida, 100% manos a la obra. Salen con un asistente *real y probado*, no solo con slides.

**Título:** Construye tu Asistente de IA para tu Startup - Workshop Práctico
**Duración:** 3 horas presenciales
**Audiencia:** 20-30 emprendedores early-stage, mesas de 4-5 personas
**Objetivo final:** Cada participante sale con 1 asistente funcional (en ChatGPT, Claude o Gemini) entrenado con el contexto de SU startup para resolver 1 problema concreto: ventas, atención al cliente o contenido.

### 1. AGENDA DETALLADA - 180 MINUTOS

| Hora | Bloque | Duración |
| :--- | :--- | :--- |
| 0:00 - 0:15 | 1. Apertura y Rompehielos | 15 min |
| 0:15 - 0:35 | 2. El Problema: ChatGPT no conoce tu startup | 20 min |
| 0:35 - 1:00 | 3. El Framework que funciona: R-C-T-F-E | 25 min |
| 1:00 - 1:15 | 4. Demo en Vivo: Lo construyo en 10 minutos | 15 min |
| 1:15 - 1:25 | **PAUSA** | 10 min |
| 1:25 - 2:10 | 5. EJERCICIO PRINCIPAL: Construye tu Asistente v1 | 45 min |
| 2:10 - 2:30 | 6. Hazlo Real: Conéctalo a WhatsApp / Sheets / Instagram | 20 min |
| 2:30 - 2:45 | 7. Test de Estrés + Feedback en Parejas | 15 min |
| 2:45 - 3:00 | 8. Cierre y Plan de 7 Días | 15 min |

### 2. MATERIALES NECESARIOS (Qué preparar antes)

**A. Lo que DEBES pedir a los participantes 3 días antes (email/WhatsApp):**
1. Laptop cargada + cuenta gratuita creada en ChatGPT, Claude o Gemini (avisa que NO necesitan pagar Plus)
2. Traer por escrito: 1 párrafo de qué vende su startup, a quién, y cuánto cuesta
3. Traer 3 preguntas reales que les hacen sus clientes por WhatsApp/Instagram
4. Traer 1 documento clave: menú, lista de precios, catálogo, PDF de servicios

> Frase para el email: "No vengan a aprender teoría. Vengan con un problema real de su negocio y nos vamos con la solución probada."

**B. Materiales del facilitador:**
- **Físicos:** Proyector, micrófono, extensiones de poder para cada mesa (crítico), 30 worksheets impresos de 1 página con el template de prompt, post-its, marcadores, timer visible
- **Digitales:** Slides (27 total), QR gigante en pantalla para unirse a grupo de WhatsApp de la comunidad, carpeta en Google Drive/Notion con todos los recursos, 2 laptops de respaldo con internet
- **Equipo:** Idealmente 1 co-facilitador/ayudante para circular y desbloquear a los no-técnicos. Con 30 personas, tú solo no llegas.
- **Plan B LatAm:** Descarga los videos de demo por si falla el WiFi. Ten todo en prompts copiables, no escribas en vivo.

**C. Setup del salón:** Mesas redondas, no filas de auditorio. Todos deben verse y poder trabajar en equipo. Nada de pupitres escolares.

### 3. DETALLE POR BLOQUE

**BLOQUE 1: Apertura y Rompehielos**
**Duración:** 15 min | **Slides:** 4
**Objetivo:** Energía alta, conexión y dejar claro que hoy se construye, no se escucha.
**Dinámica:** Ejercicio rápido. En mesa, cada uno presenta su startup en 30 segundos como si se la vendiera a un robot: ¿qué haces, para quién, qué dolor resuelves? La mesa elige la mejor.
**Key Takeaway:** "Un asistente de IA no es magia, es un empleado digital que entrenas con tu contexto."

**BLOQUE 2: El Problema: ChatGPT no conoce tu startup**
**Duración:** 20 min | **Slides:** 4
**Objetivo:** Mostrar por qué usar ChatGPT suelto no sirve para un negocio.
**Dinámica:** Charla + Discusión. Demo de un prompt genérico: "Escríbeme un mensaje de ventas" vs. uno con contexto. Pregunta a la sala: ¿Cuál vendería más? Discusión en mesa de 3 min.
**Key Takeaway:** "La IA genérica te da respuestas genéricas. La IA con tu contexto te da ventas."

**BLOQUE 3: El Framework: R-C-T-F-E**
**Duración:** 25 min | **Slides:** 5
**Objetivo:** Entregar UNA fórmula simple para crear cualquier asistente.
**Dinámica:** Charla práctica. Explicas el framework en una sola slide gigante:
**R**ol: Actúa como un vendedor experto en...
**C**ontexto: Mi startup es..., mi cliente es..., vendo...
**T**area: Tu trabajo es responder preguntas sobre precios/horarios...
**F**ormato: Responde corto, amable, en español mexicano, máximo 3 líneas para WhatsApp
**E**jemplos: Aquí hay 2 ejemplos de cómo quiero que respondas
**Key Takeaway:** "Si tu prompt no tiene Rol + Contexto + Tarea + Formato, no tienes un asistente, tienes un chat."

**BLOQUE 4: Demo en Vivo**
**Duración:** 15 min | **Slides:** 2 (el resto es pantalla en vivo)
**Objetivo:** Probar que se puede construir en 10 minutos, sin código.
**Dinámica:** Demo. Construyes en vivo un asistente para una startup inventada pero muy LatAm: una dark kitchen de hamburguesas en CDMX. Lo entrenas con su menú y lo pruebas con preguntas reales de clientes. La sala te grita qué preguntarle.
**Key Takeaway:** "No necesitas saber programar. Necesitas saber explicar tu negocio."

**BLOQUE 5: EJERCICIO PRINCIPAL** - Ver detalle abajo
**Duración:** 45 min | **Slides:** 3
**Objetivo:** Que cada uno cree su Asistente v1.
**Dinámica:** Ejercicio guiado por pasos con timer.
**Key Takeaway:** "Tu asistente v1 feo y funcional vale 10 veces más que la idea perfecta en tu cabeza."

**BLOQUE 6: Hazlo Real: Conéctalo a tu operación**
**Duración:** 20 min | **Slides:** 4
**Objetivo:** Sacar el asistente de la pestaña del navegador y llevarlo a donde viven sus clientes.
**Dinámica:** Demo + Charla. No APIs. Muestras 3 rutas no-code: 1) Copiar/pegar a WhatsApp Business (la ruta #1 en LatAm), 2) Usarlo con Google Sheets para responder cotizaciones, 3) Con Make/Zapier para Instagram DM. Enfasis en WhatsApp.
**Key Takeaway:** "El mejor asistente es el que responde por WhatsApp en 10 segundos, no el más inteligente en una app que nadie abre."

**BLOQUE 7: Test de Estrés + Feedback en Parejas**
**Duración:** 15 min | **Slides:** 2
**Objetivo:** Romper el asistente antes de que lo haga un cliente real.
**Dinámica:** Ejercicio en parejas. Intercambian laptops. Intentan "romper" el asistente del otro con preguntas difíciles, reclamos, preguntas fuera de tema. Luego le dan 1 feedback concreto para mejorarlo.
**Key Takeaway:** "Un asistente que no pruebas con clientes reales, te va a quedar mal en público."

**BLOQUE 8: Cierre y Plan de 7 Días**
**Duración:** 15 min | **Slides:** 3
**Objetivo:** Evitar que todo quede en el workshop.
**Dinámica:** Charla + Compromiso. Entregas el Plan de 7 días: Día 1-2 usarlo para 5 clientes reales, Día 3-4 ajustar prompt, Día 5 conectarlo a WhatsApp, Día 7 medir tiempo ahorrado. Cada mesa grita su compromiso.
**Key Takeaway:** "La IA no reemplaza al fundador. Reemplaza las 2 horas diarias que pierdes respondiendo lo mismo."

### 4. EJERCICIO PRINCIPAL: Construye tu Asistente v1 (45 min)

Este es el corazón del workshop. Todos hacen lo mismo, con su propio negocio.

**Paso 1: Elige tu caso de uso (5 min)**
Cada uno elige SOLO UNO: A) Atender preguntas y vender por WhatsApp, B) Crear contenido para Instagram/TikTok, C) Responder cotizaciones y operaciones. Nada de "quiero que haga todo".

**Paso 2: Completa tu Contexto (10 min)**
En su worksheet, completan: Nombre de la startup, qué vende, cliente ideal, precios, zona, horarios, tono (formal, cercano, divertido). Usan los materiales que trajeron.

**Paso 3: Arma tu Prompt Maestro (10 min)**
Copian el template y lo rellenan. El facilitador y ayudante circulan mesa por mesa desbloqueando.

Template que les entregas:
```
Actúa como [ROL: el mejor vendedor/atendedor de mi startup].
Contexto: Mi negocio es [X]. Vendemos [Y] a [cliente Z] en [ciudad]. Nuestros precios son [..]. Nuestro tono es [..].
Tarea: Responde las preguntas de un cliente sobre [precios, horarios, envíos, etc.].
Formato: Máximo 4 líneas, listo para copiar a WhatsApp, español claro y amable.
Reglas: Si no sabes la respuesta, di "Te confirmo en un momento" y no inventes. Nunca des descuentos sin permiso.
Ejemplos: [Pega 2 ejemplos de respuestas que SÍ te gustan]
```

**Paso 4: Prueba con 3 Preguntas Reales (10 min)**
Prueban con las 3 preguntas reales que trajeron de WhatsApp. ¿Responde bien? ¿Suena a ellos?

**Paso 5: Itera 1 vez (10 min)**
Ajustan UNA sola cosa: que sea más corto, más amable, que incluya una pregunta de cierre para vender. Guardan el prompt en un Google Doc con nombre: "Mi Asistente - [Nombre Startup]".

**Entregable al final del bloque:** Cada persona tiene nombre para su asistente (ej: "Valentina, mi vendedora"), su prompt guardado y 3 pruebas hechas.

### 5. RECURSOS PARA LLEVAR A CASA

Entrégalo como un pack digital (QR al final) y también impreso el checklist:

1.  **Template Maestro en Notion/Google Docs:** Para copiar y reutilizar
2.  **Banco de 15 Prompts Listos:** 5 para ventas por WhatsApp, 5 para atención al cliente, 5 para contenido
3.  **Checklist de 1 Página: "Mi Asistente en 20 Minutos"**
4.  **Video de 12 min:** Cómo conectar tu asistente a WhatsApp Business con Make (sin código)
5.  **Guía de Errores Comunes:** No inventar precios, no ser demasiado largo, no intentar que haga todo
6.  **Acceso a Comunidad:** Grupo de WhatsApp/Telegram de alumni por 30 días para resolver dudas y compartir prompts que funcionan

### 6. SLIDE COUNT ESTIMADO POR SECCIÓN

Total recomendado: **27 slides**. Más de eso y se vuelve clase. Menos de eso y te quedas sin guía.

Bloque 1: 4 | Bloque 2: 4 | Bloque 3: 5 | Bloque 4: 2 | Bloque 5: 3 | Bloque 6: 4 | Bloque 7: 2 | Bloque 8: 3

**Tip final de facilitador:** Tu energía es el material más importante. Con emprendedores early-stage, si tú te aburres, ellos se van. Habla de dinero, tiempo y clientes reales, no de "inteligencia artificial generativa". Cada 15 minutos, que estén escribiendo, probando o hablando.