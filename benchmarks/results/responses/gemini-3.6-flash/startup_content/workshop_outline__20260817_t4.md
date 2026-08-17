# Gemini 3.6 Flash — startup_content/workshop_outline

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.29 | quality: 9.72
- latency_total: 26.948s | tokens_per_second: 157.9
- input_tokens: 190 | output_tokens: 4255
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

¡Hola! Qué excelente iniciativa. Para founders *early-stage* no técnicos, el secreto de este workshop es **quitarle el miedo a la tecnología** y mostrarles que "programar" un asistente hoy en día es saber estructurar el pensamiento y dar buenas instrucciones en español.

Aquí tienes el outline completo, diseñado con una metodología *hands-on* (70% práctica, 30% teoría), alto nivel de energía y formato visual para mantener a 20-30 personas conectadas durante las 3 horas.

---

# 🚀 OUTLINE DEL WORKSHOP
**Título:** Construye tu Asistente de IA para tu Startup (Sin escribir una sola línea de código)
**Duración Total:** 3 Horas (180 minutos)
**Audiencia:** 20-30 Emprendedores No-Técnicos (Early-Stage)

---

## 🛠️ MATERIALES Y PREPARACIÓN PREVIA

### Para el Facilitador / Organizador:
*   Proyector/Pantalla grande y cable HDMI/Adaptadores.
*   Conexión a Wi-Fi de alta velocidad (¡Crucial! Probarla antes con 30 conexiones simultáneas).
*   Multitomas / Extensiones eléctricas en las mesas.
*   Post-its de colores (2 bloques) y plumones gruesos (uno por participante).
*   Un temporizador visible en pantalla (ej. ilovemt.com o un video de YouTube).

### Para los Participantes (Enviar por email 48h antes):
1.  **Laptop obligatoria** con cargador (No tablets, no celulares para el taller).
2.  **Cuenta activa** en OpenAI (ChatGPT) o Anthropic (Claude). *Nota: Se puede hacer el 100% del workshop con cuentas gratuitas usando Custom Instructions / System Prompts, o con ChatGPT Plus / Claude Pro si quieren crear "Custom GPTs/Projects".*
3.  Tener a la mano en digital: La propuesta de valor de su startup, preguntas frecuentes de sus clientes y un texto breve sobre su producto/servicio.

---

## ⏰ AGENDA DETALLADA (180 MINUTOS)

```
[00:00 - 00:15] Bloque 0: Rompehielos y El Nuevo Rol del Founder
[00:15 - 00:45] Bloque 1: Prompt Engineering para Ejecutivos (El Framework R-C-T-F)
[00:45 - 01:10] Bloque 2: Diseñando el "Cerebro" de tu Asistente (Prompt Canvas)
[01:10 - 02:10] Bloque 3: ¡MANOS A LA OBRA! Construcción en Vivo + Break
[02:10 - 02:45] Bloque 4: Stress Test en Parejas (Peer Review) & Optimización
[02:45 - 03:00] Bloque 5: Demos Relámpago, Stack Futuro y Cierre
```

---

## 📑 DESGLOSE POR BLOQUES

### BLOQUE 0: Rompehielos y El Nuevo Rol del Founder
*   **Duración:** 15 min
*   **Slide Count Estimado:** 4 slides
*   **Objetivo:** Elevar la energía, nivelar expectativas y cambiar la mentalidad de "usuario de chat" a "jefe de un empleado digital".
*   **Dinámica:**
    *   *Charla relámpago (5 min):* "¿Por qué hoy un founder no-técnico puede construir software usando lenguaje natural?".
    *   *Ejercicio de calibración (10 min):* En parejas, responder: *"Si pudieras contratar a un pasante gratis hoy que trabaje 24/7, ¿cuál es la tarea más aburrida que le darías?"*. 3 personas comparten en voz alta.
*   **Key Takeaway:** Un asistente de IA no es un buscador elegante; es un empleado junior infinitamente paciente al que debes saber delegar.

---

### BLOQUE 1: Prompt Engineering para Ejecutivos (Sin Jargón)
*   **Duración:** 30 min
*   **Slide Count Estimado:** 8 slides
*   **Objetivo:** Enseñar la estructura lógica para comunicarse con LLMs de forma efectiva y consistente.
*   **Dinámica:**
    *   *Demo en vivo (10 min):* Facilitador muestra la diferencia entre un "Bad Prompt" (ej: *"Escríbeme respuestas para atención al cliente"*) vs. "Master Prompt" usando el Framework **R-C-T-F** (Rol, Contexto, Tarea, Formato/Límites).
    *   *Ejercicio en caliente (15 min):* El facilitador muestra un prompt defectuoso en pantalla y la audiencia debe corregirlo a mano alzada.
*   **Key Takeaway:** Si la IA te da una respuesta mediocre, el 90% de las veces es porque tu instrucción fue ambigua.

---

### BLOQUE 2: Diseñando el "Cerebro" de tu Asistente
*   **Duración:** 25 min
*   **Slide Count Estimado:** 5 slides
*   **Objetivo:** Aterrizar el caso de uso específico antes de tocar la computadora.
*   **Dinámica:**
    *   *Ejercicio Análogo con "Prompt Canvas" impreso o en Post-its (20 min):*
        Cada emprendedor elegirá **UN** uso de uso para su startup (ej: Calificador de Leads, Generador de Propuestas, Onboarding de Clientes, Soporte Nivel 1).
        Llenarán su lienzo respondiendo:
        1. **Rol:** ¿Quién es el bot?
        2. **Contexto/Knowledge:** ¿Qué datos de la empresa debe saber?
        3. **Reglas de Oro:** ¿Qué tiene ESTRICTAMENTE PROHIBIDO decir o hacer?
        4. **Output Esperado:** ¿Cómo debe responder? (Listas, JSON, tono cercano, profesional, etc.).
*   **Key Takeaway:** Primero piensa la estrategia en papel; la pantalla es solo el canal de ejecución.

---

### BLOQUE 3: ¡MANOS A LA OBRA! Construcción en Vivo
*   **Duración:** 60 min *(Incluye 10 min de receso/break activo)*
*   **Slide Count Estimado:** 8 slides (Screenshots de guía paso a paso)
*   **Objetivo:** Configurar y entrenar el asistente funcionalmente en la plataforma elegida.
*   **Dinámica:**
    *   *Live Demo / Follow-me (15 min):* El facilitador proyecta su pantalla y crea un Custom GPT (o configura las Custom Instructions de ChatGPT/Claude Projects) paso a paso, cargando un archivo de contexto (PDF/TXT) y probándolo.
    *   *Trabajo Individual Guiado (35 min):* Todos abren sus laptops. Tienen 35 minutos para traducir su "Prompt Canvas" al sistema y cargar el conocimiento de su startup. El facilitador y un co-facilitador/staff van mesa por mesa resolviendo traba técnica.
    *   *Bio-Break Integrado (10 min):* Pueden ir por café sin desconectarse de la dinámica.
*   **Key Takeaway:** ¡Felicidades, acabas de desplegar tu primer producto con Inteligencia Artificial!

---

### BLOQUE 4: Stress Test en Parejas & Optimización
*   **Duración:** 35 min
*   **Slide Count Estimado:** 3 slides
*   **Objetivo:** Probar el asistente en condiciones reales, encontrar fallos ("alucinaciones") e iterar el prompt.
*   **Dinámica:**
    *   *Peer Testing (20 min):* Se cambian las laptops con el compañero de al lado. El compañero interpreta a un cliente "difícil", "confundido" o un "lead calificado". Intentará "romper" el asistente o sacarle información incorrecta.
    *   *Ajuste e Iteración (15 min):* Cada founder recupera su laptop, analiza en qué falló su bot y ajusta las "Reglas de Oro" en el prompt para corregir el comportamiento.
*   **Key Takeaway:** La IA no se programa a la primera; se itera a través del testeo constante.

---

### BLOQUE 5: Demos Relámpago, Stack Futuro y Cierre
*   **Duración:** 15 min
*   **Slide Count Estimado:** 5 slides
*   **Objetivo:** Celebrar los logros, mostrar los siguientes pasos para automatizar y cerrar con alta energía.
*   **Dinámica:**
    *   *Demos Relámpago (6 min):* 3 emprendedores voluntarios presentan en 2 minutos su asistente proyectado en pantalla funcionando.
    *   *Visión del Stack Futuro (5 min):* Breve explicación de cómo conectar este asistente con WhatsApp/CRM en el futuro usando herramientas No-Code (Zapier, Make, Voiceflow, ManyChat) sin saturar de técnica.
    *   *Cierre y Foto Grupal (4 min).*
*   **Key Takeaway:** La ventaja competitiva no es la tecnología, es la velocidad con la que implementas la IA en tus procesos cotidianos.

---

## 🎯 EL EJERCICIO PRINCIPAL EN DETALLE
**(Para el Bloque 2 y 3)**

El ejercicio se llama **"El Asistente MVP"**.
Para garantizar que todos terminen, los participantes eligen **1 de 3 Plantillas de Caso de Uso**:

1.  **Opción A: El Vendedor Nocturno (SDR Bot):** Lee una consulta de un cliente entrante, le hace 3 preguntas clave para calificar si tiene presupuesto/interés y redacta un correo para agendar una llamada.
2.  **Opción B: El Soporte Implacable (Customer Support):** Responde preguntas frecuentes usando el sitio web o un PDF de precios/servicios de la startup, manteniendo siempre la calma y el tono de marca.
3.  **Opción C: El Copywriter de Founder (Content Bot):** Toma una idea en audio o texto sucio del founder y la convierte en un post de LinkedIn con la voz del emprendedor y una propuesta de valor clara.

**Entregable al final de las 3 horas:**
Cada participante tendrá una URL ejecutable o un System Prompt guardado en su cuenta personal que puede usar a partir de mañana en su empresa.

---

## 📦 RECURSOS PARA LLEVAR A CASA (Digital Kit)

Al finalizar, se envía un correo o código QR con un repositorio (Notion o Drive) que contiene:

1.  **Prompt Engineering Cheatsheet (PDF 1 página):** Estructura del Framework R-C-T-F y verbos de comando recomendados.
2.  **El "Prompt Canvas" Editable:** Plantilla en Google Docs / Notion.
3.  **5 Prompts Maestros de Regalo:**
    *   Prompt para análisis de competencia.
    *   Prompt para crear customer personas.
    *   Prompt para resumir feedback de clientes.
    *   Prompt para estructurar un pitch deck.
    *   Prompt para negociación de proveedores.
4.  **Mapa de Herramientas No-Code AI:** Diagrama simple recomendando herramientas según el canal (WhatsApp = ManyChat + OpenAI; Web = Voiceflow/Chatbase; Interno = Custom GPTs / Claude Projects).

---

## 📊 RESUMEN DE SLIDES ESTIMADO

| Sección | No. de Slides | Enfoque |
| :--- | :--- | :--- |
| **Intro & Rompehielos** | 4 | Visuales, preguntas cortas, agenda. |
| **Prompt Engineering (R-C-T-F)** | 8 | Ejemplos comparativos Antes/Después. |
| **Explicación del Canvas** | 5 | Gráfico interactivo del lienzo. |
| **Tutorial Paso a Paso (Demo)** | 8 | Capturas de pantalla gigantes con flechas claras. |
| **Instrucciones del Testing** | 3 | Reglas del juego en parejas y temporizador. |
| **Stack Futuro & Cierre** | 5 | Mapa visual no-code, QR de recursos y redes. |
| **TOTAL ESTIMADO** | **33 Slides** | *(Pocas palabras, imágenes grandes y tipografía legible)* |

---

### 💡 Consejos de Facilitación para Latinoamérica:
*   **Lenguaje:** Evita anglicismos innecesarios; en lugar de "embeddings" o "fine-tuning", habla de "darle contexto" o "entrenar con tus propios datos".
*   **Manejo del Ritmo:** En el Bloque 3, algunos irán muy rápido y otros se trabarán con la contraseña de OpenAI. Ten un asistente de apoyo en la sala para no detener el ritmo del grupo.
*   **Pausas de Reconocimiento:** Haz que aplaudan a los valientes que presentan en la Demo Relámpago. Romper la timidez inicial genera una atmósfera de comunidad indispensable en ecosistemas de emprendimiento locales.