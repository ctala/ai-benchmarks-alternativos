# Gemma 4 31B — startup_content/workshop_outline

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 67.359s | tokens_per_second: 26.6
- input_tokens: 206 | output_tokens: 1794
- judge_score: 5.0 | justificación: 

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

¡Hola! Como facilitador, sé que con emprendedores *early-stage* el tiempo es el recurso más escaso. No quieren teoría sobre redes neuronales; quieren saber **cómo esto les ahorra 10 horas a la semana o cómo les ayuda a cerrar más ventas**.

Aquí tienes el diseño del workshop. El enfoque es **"No-Code IA"**: vamos a construir soluciones reales sin escribir una sola línea de código.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup
**Slogan:** *Deja de usar ChatGPT como un buscador y empieza a usarlo como un empleado.*

## 🎯 Objetivo General
Que cada emprendedor salga con un **prototipo funcional de un Asistente de IA personalizado** (Custom GPT o similar) configurado para una tarea crítica de su negocio (Ventas, Soporte, Operaciones o Marketing).

---

## 🛠️ 1. Materiales y Preparación (Pre-Workshop)

**Para el Facilitador:**
*   Proyector y sonido.
*   Conexión Wi-Fi robusta (crítico).
*   Cuentas de ChatGPT Plus (o acceso a herramientas No-Code como Poe o MindStudio) para demos.
*   Post-its y marcadores.

**Para los Asistentes (Enviar por email 3 días antes):**
*   **Cuenta de ChatGPT Plus** (Indispensable para crear GPTs personalizados). *Alternativa: Si no tienen, indicar que usen Poe.com o herramientas gratuitas similares.*
*   **Laptop** (No tablets, no celulares).
*   **"El Kit de Conocimiento":** Pedirles que traigan en un PDF o Doc: su propuesta de valor, FAQ de clientes, manual de marca o ejemplos de correos que ya funcionan.

---

## 🕒 2. Agenda Detallada (180 Minutos)

| Bloque | Título | Duración | Formato |
| :--- | :--- | :--- | :--- |
| 0 | **Bienvenida y Energía** | 10 min | Charla rápida |
| 1 | **El Mindset: De "Chat" a "Asistente"** | 20 min | Demo + Conceptos |
| 2 | **Ingeniería de Prompts para No-Técnicos** | 30 min | Ejercicio guiado |
| 3 | **Construcción: El "Cerebro" de tu Asistente** | 60 min | Workshop Práctico |
| 4 | **Testeo, Ajuste y Pitch** | 40 min | Dinámica de grupo |
| 5 | **Cierre y Próximos Pasos** | 20 min | Q&A + Recursos |

---

## 📦 3. Desglose de Bloques

### Bloque 0: Bienvenida y Energía (10 min)
*   **Objetivo:** Romper el hielo y alinear expectativas.
*   **Dinámica:** Presentación flash. "Nombre + Startup + El proceso más aburrido de tu día".
*   **Key Takeaway:** La IA no reemplaza al emprendedor, reemplaza las tareas repetitivas.
*   **Slides:** 2 slides.

### Bloque 1: El Mindset: De "Chat" a "Asistente" (20 min)
*   **Objetivo:** Entender la diferencia entre un prompt suelto y un agente con contexto.
*   **Dinámica:** **Demo "Antes vs. Después"**. Muestro un prompt genérico ("Escribe un mail de ventas") vs. un Asistente configurado con el tono de marca y el ICP (Ideal Customer Profile).
*   **Key Takeaway:** Un asistente es: **Rol + Contexto + Conocimiento + Formato de Salida.**
*   **Slides:** 5 slides.

### Bloque 2: Prompting Estratégico (30 min)
*   **Objetivo:** Dominar el framework de prompts profesionales.
*   **Dinámica:** **"El Juego del Teléfono Descompuesto"**. Les doy un prompt malo y, entre todos, lo optimizamos usando la técnica **R-C-I (Rol, Contexto, Instrucción)**.
*   **Key Takeaway:** Si el resultado es malo, el problema suele ser la falta de contexto, no la IA.
*   **Slides:** 6 slides.

### Bloque 3: Construcción: El "Cerebro" de tu Asistente (60 min)
*   **Objetivo:** Crear el GPT personalizado.
*   **Dinámica:** **Hands-on (Manos a la obra)**.
    1.  **Definición:** Eligen una tarea (ej. "Calificador de Leads" o "Redactor de LinkedIn").
    2.  **Configuración:** Llenan las *Instructions* del GPT usando el framework aprendido.
    3.  **Knowledge Base:** Suben sus archivos (PDFs, Docs) para que la IA no alucine y use datos reales de la startup.
    4.  **Iteración:** Prueban el bot y ajustan las instrucciones.
*   **Key Takeaway:** La magia no está en la herramienta, sino en la calidad de la información que le das.
*   **Slides:** 4 slides (guía paso a paso).

### Bloque 4: Testeo y Pitch (40 min)
*   **Objetivo:** Validar la utilidad y recibir feedback.
*   **Dinámica:** **"Speed Dating de Asistentes"**. Se agrupan en parejas. El emprendedor A intenta "romper" el asistente del emprendedor B haciéndole preguntas difíciles. Luego rotan.
*   **Key Takeaway:** La iteración basada en errores es la forma más rápida de mejorar un producto de IA.
*   **Slides:** 3 slides.

### Bloque 5: Cierre y Próximos Pasos (20 min)
*   **Objetivo:** Dar ruta de crecimiento y cerrar con energía.
*   **Dinámica:** Q&A abierto y entrega de recursos digitales.
*   **Key Takeaway:** Esto es solo el inicio; el siguiente paso es la automatización (Zapier/Make).
*   **Slides:** 3 slides.

---

## 🛠️ 4. Ejercicio Principal: "El Empleado Digital"

El ejercicio central es la creación de un **Custom GPT (o Agente)**. Para que no se pierdan, les doy 3 "Plantillas de Misión" a elegir:

1.  **El Growth Hacker:** Un asistente que analiza el perfil de LinkedIn de un prospecto y redacta un mensaje de apertura hiper-personalizado basado en la propuesta de valor de la startup.
2.  **El Especialista en Soporte:** Un asistente que lee el manual de producto y responde dudas de clientes en el tono de marca, escalando a un humano solo si es necesario.
3.  **El Estratega de Contenido:** Un asistente que convierte un video de YouTube o un artículo largo en 5 posts de Twitter, 1 hilo y un copy de Instagram.

---

## 🏠 5. Recursos para llevar a casa (The Toolkit)

Al finalizar, les envío un Notion/PDF con:
*   **Cheat Sheet de Prompting:** Una hoja con fórmulas (Rol + Tarea + Restricciones + Ejemplo).
*   **Directorio de Herramientas:** Lista de herramientas No-Code (Make.com, Zapier, Perplexity, Claude, Poe).
*   **Template de "Instrucciones Maestras":** Un documento donde solo tengan que rellenar espacios en blanco para configurar nuevos asistentes.
*   **Guía de Seguridad:** Qué datos NO subir nunca a una IA abierta.

---

## 📊 Resumen de Slides (Total estimado: 23-25 slides)
*   **Intro:** 2
*   **Conceptos/Mindset:** 5
*   **Prompting:** 6
*   **Guía de Construcción:** 4
*   **Dinámica de Testeo:** 3
*   **Cierre/Recursos:** 3