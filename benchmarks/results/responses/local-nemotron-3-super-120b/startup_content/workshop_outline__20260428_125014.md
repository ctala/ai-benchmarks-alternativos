# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — startup_content/workshop_outline

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.73 | quality: 9.24
- latency_total: 242.54s | tokens_per_second: 18.5
- input_tokens: 206 | output_tokens: 4481
- judge_score: 4.6 | justificación: 

## Respuesta completa

**WORKSHOP: “Construye tu Asistente de IA para tu Startup – Workshop Práctico”**  
*Duración total: 3 horas (180 min)*  
*Audiencia: Emprendedores early‑stage, no‑técnicos (20‑30 personas)*  

---

## 1. Agenda detallada (con tiempos)

| Hora | Bloque | Duración | Tipo de actividad |
|------|--------|----------|-------------------|
| 09:00‑09:10 | **Bienvenida & Ice‑breaker** | 10 min | Charla rápida + dinámica de presentación |
| 09:10‑09:25 | **¿Por qué un Asistente de IA?** | 15 min | Mini‑charla + encuesta en mano |
| 09:25‑09:45 | **Casos de uso reales para startups** | 20 min | Discusión guiada + ejemplos en pantalla |
| 09:45‑10:05 | **Herramientas No‑Code + IA (panorama rápido)** | 20 min | Demo en vivo + tabla comparativa |
| 10:05‑10:10 | **Mini‑break** | 5 min | Agua, estiramiento |
| 10:10‑11:10 | **¡Manos a la obra! Construye tu asistente paso a paso** | 60 min | Ejercicio práctico guiado (individual + apoyo en parejas) |
| 11:10‑11:30 | **Testeo, iteración y métricas simples** | 20 min | Demo de testing + ejercicio de “qué mejorar” |
| 11:30‑11:45 | **Pitch relámpago & feedback grupal** | 15 min | Cada equipo muestra 1‑min demo + retroalimentación |
| 11:45‑11:55 | **Próximos pasos & recursos** | 10 min | Charla motivadora + entrega de materiales |
| 11:55‑12:00 | **Cierre & foto grupal** | 5 min | Agradecimientos y networking informal |

*Total: 180 min (3 h).*

---

## 2. Materiales necesarios (preparar antes)

| Ítem | Cantidad / Detalle | Comentario |
|------|--------------------|------------|
| Sala con capacidad ≥30 personas, sillas móviles y mesas para trabajar en parejas | 1 | Facilita movimiento y trabajo colaborativo |
| Proyector o pantalla grande + cable HDMI | 1 | Para slides y demos en vivo |
| Computer portátil del facilitador (con cuenta de prueba de herramientas) | 1 | Con acceso a internet y permisos de admin |
| **Laptops** de los participantes (se asume que traen su propio) | 20‑30 | Si alguno no tiene, tener 2‑3 laptops de reserva |
| Cargadores y extensiones | Suficientes | Para evitar que se queden sin batería |
| Flipchart o pizarrón blanco + marcadores de colores | 1‑2 | Para brainstorming y anotaciones rápidas |
| Post‑its (3 colores) y marcadores finos | 1 bloque | Para ejercicios de clasificación de ideas |
| Impresión de **handout**: “Cheat sheet de prompts y herramientas No‑Code” (1 página) | 1 por persona | Incluye enlaces, ejemplos de prompts y tabla de precios |
| Acceso a cuentas de prueba (sandbox) de: <br>• OpenAI API (o alternativa gratuita como HuggingFace Inference API) <br>• Plataforma No‑Code elegida (ej. **Make.com**, **Zapier**, **Voiceflow**, **Bubble + AI plugin**) | 1 cuenta compartida + credenciales de invitado | Crear previamente y compartir vía QR o link corto |
| Encuesta rápida (Google Forms o Mentimeter) para ice‑breaker y feedback final | 1 link | Para medir expectativas y satisfacción |
| Botellas de agua y snack ligero (fruta, barritas) | Opcional | Mantener energía |
| Cámara o smartphone para foto grupal | 1 | Para recuerdo y redes sociales |

---

## 3. Detalle de cada bloque

### Bloque 1 – Bienvenida & Ice‑breaker  
- **Duración:** 10 min  
- **Objetivo:** Romper el hielo, crear un ambiente de confianza y alinear expectativas.  
- **Dinámica:**  
  1. Facilitador se presenta (30 seg).  
  2. Cada participante dice su nombre, startup (o idea) y **una palabra** que describa su mayor reto hoy (ej. “tiempo”, “clientes”, “tecnología”).  
  3. Se anotan las palabras en un flipchart para visualizar temas comunes.  
- **Key takeaway:** “Todos estamos aquí para resolver un problema concreto con IA, no para teoría.”  

### Bloque 2 – ¿Por qué un Asistente de IA?  
- **Duración:** 15 min  
- **Objetivo:** Conectar la IA con necesidades reales de una startup early‑stage (ahorro de tiempo, atención al cliente, validación de ideas).  
- **Dinámica:** Mini‑charla (5 min) + encuesta en vivo (Mentimeter) donde los participantes votan cuál de 3 beneficios les parece más valioso.  
- **Key takeaway:** “Un asistente de IA puede liberar hasta 10 h/semana de tareas repetitivas en una startup de menos de 5 personas.”  

### Bloque 3 – Casos de uso reales para startups  
- **Duración:** 20 min  
- **Objetivo:** Inspirar con ejemplos concretos que los participantes puedan replicar.  
- **Dinámica:**  
  - 3‑4 casos (FAQ bot, lead qualifier, agenda inteligente, análisis de feedback).  
  - Cada caso se muestra en pantalla (2 min) seguido de 1 min de Preguntas‑Respuestas rápidas.  
- **Key takeaway:** “No necesitas ser desarrollador para que tu startup tenga un asistente que hable con clientes, califique leads o organice tu calendario.”  

### Bloque 4 – Herramientas No‑Code + IA (panorama rápido)  
- **Duración:** 20 min  
- **Objetivo:** Dar una visión clara de las opciones disponibles y cuál elegir según el caso de uso.  
- **Dinámica:** Demo en vivo (10 min) donde se construye un “mini‑flujo” en **Make.com** que llama a la API de OpenAI y devuelve una respuesta. Después, se muestra una tabla comparativa (precio, curva de aprendizaje, tipo de salida).  
- **Key takeaway:** “Make.com, Zapier y Voiceflow son las puertas de entrada más rápidas; elige según si necesitas flujo de datos, automatización de marketing o conversación por voz/chat.”  

### Bloque 5 – Mini‑break  
- **Duración:** 5 min  
- **Objetivo:** Recargar energía y permitir preguntas informales.  

### Bloque 6 – ¡Manos a la obra! Construye tu asistente paso a paso  
- **Duración:** 60 min (núcleo del workshop)  
- **Objetivo:** Cada participante (o pareja) tenga un asistente funcional al final del bloque.  
- **Dinámica:**  
  1. **Introducción al flujo (5 min):** Explicar el escenario – “Asistente de FAQ para la página de tu startup”.  
  2. **Setup de cuenta (5 min):** Crear cuenta en Make.com, conectar a OpenAI (sandbox).  
  3. **Construcción del escenario (30 min):** Paso a paso guiado por el facilitador:  
     - Trigger: Webhook (simula un mensaje desde un formulario de contacto).  
     - Acción 1: Recibir texto del usuario.  
     - Acción 2: Llamada a OpenAI (prompt: “Responde como un experto en [industria] y mantén un tono amigable”).  
     - Acción 3: Enviar respuesta por email o Slack (simulación).  
     - Acción 4: Guardar log en Google Sheets (para métricas).  
  4. **Personalización (15 min):** Cada pareja modifica el prompt, agrega una variable (ej. nombre del usuario) o cambia el canal de salida (WhatsApp vía Twilio sandbox).  
  5. **Check‑list rápido:** Facilitador recorre las mesas, verifica que cada escenario tenga al menos un test exitoso.  
- **Key takeaway:** “En menos de una hora tienes un prototipo de asistente de IA que puedes conectar a tu sitio web o a tu WhatsApp Business.”  

### Bloque 7 – Testeo, iteración y métricas simples  
- **Duración:** 20 min  
- **Objetivo:** Aprender a validar que el asistente responde bien y a mejorar el prompt con datos reales.  
- **Dinámica:**  
  - Demo de testing: enviar 3‑5 preguntas de muestra y observar respuestas (5 min).  
  - Ejercicio rápido: cada pareja anota en un post‑it “¿Qué mejorarías?” (prompt, tono, longitud) y lo pega en una pared de “Mejoras”.  
  - Facilitador sintetiza los patrones más comunes (2 min).  
- **Key takeaway:** “Un buen prompt es un proceso de iteración: prueba, mide, ajusta.”  

### Bloque 8 – Pitch relámpago & feedback grupal  
- **Duración:** 15 min  
- **Objetivo:** Practicar la comunicación del valor del asistente y recibir retroalimentación concreta.  
- **Dinámica:**  
  - Cada pareja tiene **60 seg** para mostrar su asistente (demo en vivo o video de 15 seg) y explicar el problema que resuelve.  
  - El resto del grupo da **una** mejora y **una** fortaleza (formato “+1 / Δ”).  
- **Key takeaway:** “Explicar tu solución en menos de un minuto es la habilidad más valiosa para conseguir primeros usuarios o inversores.”  

### Bloque 9 – Próximos pasos & recursos  
- **Duración:** 10 min  
- **Objetivo:** Dejar claro cómo continuar después del workshop y qué materiales llevar.  
- **Dinámica:**  
  - Resumen de los 3 pasos siguientes (1) crear cuenta de pago si se necesita escala, 2) integrar con tu sitio/web, 3) medir KPI (tiempo de respuesta, satisfacción).  
  - Entrega del handout y acceso a carpeta de Google Drive con plantillas, videos tutoriales y lista de comunidades.  
- **Key takeaway:** “Tu asistente no termina hoy; empieza ahora y mejora cada semana.”  

### Bloque 10 – Cierre & foto grupal  
- **Duración:** 5 min  
- **Objetivo:** Finalizar con energía y dejar recuerdo del evento.  
- **Dinámica:** Agradecimientos, recordatorio de redes sociales del organizador y foto grupal.  
- **Key takeaway:** “Llevate la energía, el prototipo y la red de compañeros que también están construyendo su futuro con IA.”  

---

## 4. Ejercicio principal del workshop (que todos puedan hacer)

**“Construye tu Asistente de FAQ para tu Startup”**  

- **Escenario:** Un visitante llega a la landing page de tu startup y tiene una pregunta (precio, funcionamiento, horario de soporte). En lugar de esperar un email, el asistente le responde al instante.  
- **Herramientas:** Make.com (o Zapier) + OpenAI API (sandbox) + Google Sheets (log).  
- **Pasos resumidos (para que el facilitador los siga en pantalla):**  
  1. Crear un **Webhook** que reciba un JSON `{ "pregunta": "...", "nombre": "Ana", "email": "ana@ejemplo.com" }`.  
  2. Añadir módulo **OpenAI – Completion** con prompt:  
     ```
     Eres un asistente amigable y experto en [INDUSTRIA]. Responde la siguiente pregunta de forma clara y breve, usando un tono cercano: 
     {{pregunta}}
     ```  
  3. (Opcional) Añadir filtro para limitar longitud de respuesta (≤ 150 caracteres).  
  4. Enviar respuesta por **Email** (o Slack) al usuario usando el campo `email`.  
  5. Guardar en **Google Sheets**: timestamp, nombre, pregunta, respuesta, rating (dejar vacío para que el usuario lo llene después).  
  6. Probar enviando un test desde **Postman** o desde un formulario HTML sencillo (el facilitador provee un link).  

- **Resultado esperado:** Cada pareja tiene un flujo que, al dispararlo, devuelve una respuesta generada por IA y registra la interacción.  
- **Tiempo de ejecución:** 30‑35 min de construcción + 10‑15 min de prueba y ajuste.  

---

## 5. Recursos para llevar a casa

| Recurso | Formato | Descripción |
|---------|---------|-------------|
| **Cheat sheet de prompts y herramientas No‑Code** | PDF 1 página (impreso) | Lista de 10 prompts útiles (FAQ, lead qualifier, résumé de reuniones), enlaces a cuentas gratuitas de Make.com, Zapier, Voiceflow, y guía rápida de precios. |
| **Plantilla de escenario Make.com** | JSON exportable (link de descarga) | El flujo construido en el taller listo para importar y modificar. |
| **Video tutorial de 5 min** | YouTube (privado, link en handout) | Recapitulación paso a paso del ejercicio principal. |
| **Lista de comunidades y foros** | Documento Google | Slack/Discord de “No‑Code IA Latinoamérica”, grupos de Facebook, newsletters (Ben’s Bites, AI Tangent). |
| **Descuento o crédito** | Código promocional | Ej. $10 de crédito en OpenAI (para los primeros 30 días) o 1 mes gratis en Make.com Plan Pro (si el organizador tiene convenio). |
| **Próximos pasos checklist** | Hoja de acción personal | 3 tareas: 1) crear cuenta de pago si se necesita escala, 2) integrar webhook en landing page, 3) definir KPI (tiempo de respuesta, CSAT). |

---

## 6. Slide count estimado por sección

| Sección | Slides aproximados | Comentario |
|---------|-------------------|------------|
| Bienvenida & Ice‑breaker | 3 | Título, agenda, regla de oro (“learn by doing”). |
| ¿Por qué un Asistente de IA? | 5 | Estadísticas, beneficios, encuesta en vivo. |
| Casos de uso reales | 6 | 4 casos + 1 slide de resumen + 1 de preguntas. |
| Herramientas No‑Code + IA (panorama) | 8 | Visión de mercado, tabla comparativa, demo paso a paso (3 slides), decisión rápida. |
| Manos a la obra (construcción) | 12 | Guía paso a paso (10 slides) + slide de tips de depuración + slide de “qué hacer si falla”. |
| Testeo, iteración y métricas simples | 5 | Métricas básicas, ciclo de mejora, ejemplo de A/B de prompts. |
| Pitch relámpago & feedback | 3 | Instrucciones, temporizador, formato de feedback. |
| Próximos pasos & recursos | 4 | Checklist, enlaces, comunidad, llamado a acción. |
| Cierre | 2 | Gracias, foto grupal, redes. |
| **Total estimado** | **48 slides** | Un promedio de ~16 slides por hora – suficiente para mantener ritmo rápido sin sobrecargar. |

> **Tip de facilidad:** Usa diseños muy visuales (iconos, screenshots grandes, mínimo texto). Cada slide debe ser explicable en ≤ 45 seg para mantener la energía alta.

---

### Cierre final (tono)

> “¡Listos! En apenas tres horas han pasado de la idea a un prototipo que habla con sus clientes. No se trata de ser el mejor programador; se trata de probar, aprender y seguir iterando. Llevense su asistente, su hoja de acción y, sobre todo, la confianza de que la IA ya está al alcance de su startup. Ahora, ¡a construir!”  

--- 

**Listado rápido para el facilitador (check‑list de día‑of):**

- [ ] Sala reservada, proyector y sonido verificados.  
- [ ] Laptop de facilitador cargada, cuentas de prueba creadas y accesibles.  
- [ ] Handouts impresos (cheat sheet) y sobre mesa.  
- [ ] Post‑its, marcadores, flipchart listos.  
- [ ] Formularios de ice‑breaker y feedback (Google Forms) con link corto y QR.  
- [ ] Agua y snack en mesa lateral.  
- [ ] Música de fondo baja (opcional) para los momentos de trabajo individual.  
- [ ] Cronómetro o app de tiempo visible para cada bloque.  

¡Éxitos con el workshop! 🚀