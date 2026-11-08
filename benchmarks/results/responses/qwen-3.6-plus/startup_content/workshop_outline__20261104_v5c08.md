# Qwen 3.6 Plus — startup_content/workshop_outline

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.36 | quality: 9.72
- latency_total: 46.256s | tokens_per_second: 57.1
- input_tokens: 204 | output_tokens: 2639
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

¡Hola! Qué gran iniciativa. Como facilitador con experiencia en la región, sé que el mayor bloqueo para los emprendedores no técnicos no es la falta de ideas, sino el miedo a que la tecnología sea "demasiado compleja" o "cara".

Este workshop está diseñado para romper ese mito en 180 minutos. El objetivo no es que salgan siendo ingenieros de prompt, sino que salgan con una herramienta funcional que les ahorre tiempo *mañana mismo*.

Aquí tienes el outline completo, optimizado para energía alta y resultados tangibles.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup
**Duración:** 3 Horas (Presencial)
**Audiencia:** 20-30 Emprendedores Early-stage (No técnicos)
**Tono:** Energético, "Hands-on", Sin jerga técnica innecesaria.

---

## 1. Materiales Necesarios (Preparación Previa)

**Para el Facilitador:**
*   **Proyector/Pantalla grande:** Para demos en vivo.
*   **Cuentas Demo:** Tener listas 3 cuentas gratuitas en plataformas No-Code (recomendación: **Voiceflow** o **Botpress** por su facilidad visual, o **Zapier Interfaces** si prefieren algo más simple). *Nota: Voiceflow es ideal porque permite ver el flujo lógico visualmente.*
*   **Plantilla de "Persona":** Un PDF o Notion template listo para compartir.
*   **Wi-Fi Robusto:** Crucial. Ten un hotspot de respaldo.
*   **Timer visible:** Proyectado en pantalla para mantener el ritmo.

**Para los Participantes:**
*   Laptop (indispensable).
*   Cuenta gratuita creada previamente en la plataforma elegida (enviar email 24h antes con instrucciones simples: "Regístrate aquí, es gratis").
*   Cuaderno y bolígrafo (para brainstorming analógico rápido).

---

## 2. Agenda Detallada & Estructura de Bloques

### ⏱️ 0:00 - 0:20 | Bloque 1: Rompiendo el Hielo & Desmitificando la IA
*   **Duración:** 20 min
*   **Objetivo:** Bajar la ansiedad tecnológica y alinear expectativas. Entender que la IA es una herramienta de palanca, no de reemplazo.
*   **Dinámica:**
    *   *Charla relámpago (5 min):* "La IA no viene por tu trabajo, viene por tu aburrimiento". Ejemplos reales de startups latinas usando IA simple.
    *   *Icebreaker rápido (10 min):* En parejas, compartir: "¿Qué tarea repetitiva odias hacer cada semana?".
    *   *Demo Magia (5 min):* El facilitador muestra un asistente básico respondiendo preguntas complejas en segundos.
*   **Key Takeaway:** La IA es accesible, barata y ya está aquí. No necesitas saber código para usarla.
*   **Slides Estimados:** 3-4 slides (Impacto visual, poco texto).

### ⏱️ 0:20 - 0:50 | Bloque 2: El Cerebro del Asistente (Prompting Estratégico)
*   **Duración:** 30 min
*   **Objetivo:** Aprender a darle identidad y reglas claras a la IA. Sin un buen "prompt base", el asistente será inútil.
*   **Dinámica:**
    *   *Charla Interactiva (10 min):* La fórmula secreta: **Rol + Contexto + Tarea + Restricciones + Formato**.
    *   *Ejercicio Individual (15 min):** Llenar la "Plantilla de Persona". Definir quién es su asistente (ej: "Experto en Ventas B2B", "Soporte Técnico empático").
    *   *Prueba Rápida (5 min):* Pegar ese prompt en un chat simple (ChatGPT/Claude) para ver si "suena" como quieren.
*   **Key Takeaway:** Garbage in, garbage out. La calidad de tu asistente depende de qué tan bien definas su personalidad y límites.
*   **Slides Estimados:** 5 slides (La fórmula, ejemplos buenos vs. malos).

### ⏱️ 0:50 - 1:00 | ☕ Break Energético (10 min)
*   *Música alta, movimiento. Nada de pantallas.*

### ⏱️ 1:00 - 2:15 | Bloque 3: MANOS A LA OBRA - Construyendo el MVP del Asistente
*   **Duración:** 75 min (El núcleo del workshop)
*   **Objetivo:** Construir un prototipo funcional conectado a una base de conocimiento básica.
*   **Dinámica:**
    *   *Demo Guiada Paso a Paso (15 min):* El facilitador comparte pantalla y construye un flujo básico en la plataforma No-Code (ej: Voiceflow/Botpress).
        1. Crear el proyecto.
        2. Configurar el "System Prompt" (lo hecho en el Bloque 2).
        3. Subir un documento PDF (ej: FAQ de la startup o lista de precios) como base de conocimiento (RAG básico).
        4. Conectar la respuesta.
    *   *Build Session (45 min):* Los participantes construyen el suyo.
        *   *Facilitador y 1-2 ayudantes circulan por la sala resolviendo dudas técnicas específicas.*
        *   *Regla:* "Si te trabas más de 3 minutos, levanta la mano".
    *   *Testeo entre pares (15 min):* Intercambian laptops o URLs de prueba. El compañero hace 3 preguntas "difíciles" al bot.
*   **Key Takeaway:** Puedes tener un asistente entrenado con TU información en menos de 1 hora sin escribir una línea de código.
*   **Slides Estimados:** 8-10 slides (Capturas de pantalla grandes, flechas rojas indicando dónde clicar).

### ⏱️ 2:15 - 2:40 | Bloque 4: Integración y Siguientes Pasos (La realidad)
*   **Duración:** 25 min
*   **Objetivo:** Entender cómo sacar el bot de la plataforma de prueba y ponerlo donde están los clientes.
*   **Dinámica:**
    *   *Charla Demo (15 min):* Cómo incrustar el widget en una web (WordPress, Webflow, Shopify) o conectarlo a WhatsApp (mención de herramientas como ManyChat o Waha si hay tiempo, sino mantenerlo en Web Widget para simplificar).
    *   *Discusión de Errores Comunes (10 min):* ¿Qué pasa si la IA inventa datos? (Importancia de las fuentes y restricciones).
*   **Key Takeaway:** La integración es fácil (copiar y pegar un script). La mantenimiento es clave (revisar logs semanalmente).
*   **Slides Estimados:** 4 slides (Diagrama de integración, checklist de lanzamiento).

### ⏱️ 2:40 - 3:00 | Bloque 5: Cierre, Demo Day Relámpago & Recursos
*   **Duración:** 20 min
*   **Objetivo:** Celebrar logros, compartir recursos y crear comunidad.
*   **Dinámica:**
    *   *Showcase (10 min):* 3 voluntarios muestran su bot en pantalla grande y hacen una pregunta en vivo. Aplausos garantizados.
    *   *Entrega de Recursos (5 min):* QR code gigante en pantalla con todos los links.
    *   *Cierre Inspiracional (5 min):* "Lo que construyeron hoy es solo el comienzo. La iteración es la clave."
*   **Key Takeaway:** Ya eres un creador de IA. Sigue iterando.
*   **Slides Estimados:** 2 slides (QR de recursos, foto grupal/final).

---

## 3. El Ejercicio Principal: "El Experto de Nicho"

**Descripción:**
Cada emprendedor creará un Chatbot Web Embeddable que actúe como un experto específico de su negocio.

**Pasos concretos para el participante:**
1.  **Definir el Rol:** Usar la plantilla para escribir: *"Eres un asesor de ventas para [Nombre Startup], especializado en [Producto]. Tu tono es [Adjetivo]. Tu objetivo es [Meta]."*
2.  **Alimentar la Base de Conocimiento:** Subir un archivo PDF simple (puede ser una hoja de cálculo guardada como PDF con sus precios, o un texto plano con las 5 preguntas frecuentes de sus clientes).
3.  **Configurar la Lógica:** En la herramienta No-Code, crear un flujo simple:
    *   Input del usuario -> Busca en Base de Conocimiento -> Genera respuesta basada SOLO en esa información -> Si no sabe, dice "No tengo esa información, contacta a soporte".
4.  **Publicar:** Obtener el link de prueba o el código de inserción.

**Por qué funciona:** Es tangible. Ven su propia información siendo procesada. Resuelve un dolor real (responder las mismas preguntas una y otra vez).

---

## 4. Recursos para Llevar a Casa (Digital Pack)

Entregar vía Email automático o Link QR al final:

1.  **La "Cheat Sheet" de Prompting:** Un PDF de una página con la fórmula Rol+Contexto+Tarea y 5 ejemplos copy-pasteables.
2.  **Lista de Herramientas No-Code Recomendadas:**
    *   Para Chatbots: Voiceflow, Botpress, Flowise (open source).
    *   Para Automatización: Zapier, Make.
    *   Para Contenido: Gamma.app (presentaciones), Canva Magic.
3.  **Template de "Base de Conocimiento":** Un archivo de Word/Notion estructurado idealmente para ser leído por IAs (títulos claros, bullet points).
4.  **Grabación del Workshop:** (Si se graba) o al menos los slides.
5.  **Acceso a Comunidad Slack/WhatsApp:** Para seguir preguntando dudas post-workshop.

---

## 5. Consejos Pro para el Facilitador (Latam Context)

*   **Manejo del Tiempo:** En Latam somos flexibles con el tiempo, pero en un workshop técnico esto es mortal. Sé estricto con el timer. Si se atrasan en el Bloque 2, recorta la discusión del Bloque 4. Lo importante es que *construyan*.
*   **Nivel Técnico Disparejo:** Siempre habrá uno que sabe programar y se aburre, y otro que le tiene miedo al mouse.
    *   *Para el avanzado:* Retarlo a añadir una condición lógica extra (ej: "Si el cliente menciona 'precio', ofrece un descuento del 10%").
    *   *Para el principiante:* Tener un "template clonable" listo. Si se traba, dale el link para duplicar tu estructura base y que solo cambie el texto.
*   **Conectividad:** Ten descargados los PDFs de ejemplo en local. No dependas de que ellos tengan sus archivos listos si falla el internet. Ten "archivos de rescate" para enviarles por chat si no traen nada.
*   **Energía:** Usa música durante los ejercicios de construcción (Lo-fi beats o electrónica suave). Mantiene el foco y reduce la ansiedad del silencio.

¡Éxito con el workshop! Este formato suele tener un NPS (Net Promoter Score) muy alto porque la gente se va con algo *hecho*, no solo con teoría.