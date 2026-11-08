# Qwen 3.5 35B — startup_content/workshop_outline

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.62 | quality: 9.72
- latency_total: 15.178s | tokens_per_second: 151.1
- input_tokens: 204 | output_tokens: 2293
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

¡Hola! Qué genial iniciativa. Como facilitador con experiencia en el ecosistema de startups latinoamericanas, sé que la clave para este grupo (emprendedores early-stage no-técnicos) es **desmitificar la IA**, eliminar el miedo a lo "complejo" y demostrar valor inmediato. No queremos hablar de algoritmos, queremos hablar de *ahorrar tiempo* y *vender más*.

Aquí tienes el outline completo para tu workshop de 3 horas, diseñado para ser una montaña rusa de energía y productividad.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup
**Duración:** 3 Horas | **Audiencia:** Emprendedores Early-Stage (No Técnicos)
**Tono:** Energético, Práctico, "Hands-on", Directo al grano.

---

## 1. Agenda Detallada (Cronograma)

| Tiempo | Sección | Actividad Principal |
| :--- | :--- | :--- |
| **00:00 - 00:20** | **Kick-off & Desmitificación** | Rompehielos, realidad vs. mito y mentalidad. |
| **00:20 - 00:50** | **Bloque 1: El Cerebro (Prompting)** | Taller intensivo de ingeniería de prompts básica. |
| **00:50 - 01:00** | ☕ *Coffee Break (Networking)* | |
| **01:00 - 01:45** | **Bloque 2: La Arquitectura (Sin Código)** | Introducción a herramientas "No-Code" para conectar la IA. |
| **01:45 - 02:30** | **🔥 BLOQUE PRINCIPAL: Hands-On** | **Construcción del MVP del Asistente.** |
| **02:30 - 02:50** | **Demo & Pitch Rápido** | Los participantes muestran su creación en 60 seg. |
| **02:50 - 03:00** | **Cierre & Siguientes Pasos** | Recursos, Q&A y motivación final. |

---

## 2. Materiales Necesarios (Preparación Previa)

**Para el Facilitador:**
*   Proyector y audio potente.
*   Pizarra o Flipchart con marcadores de colores.
*   Plantilla de "Mapa de Procesos" impresa (una hoja por persona).
*   Lista de acceso rápido a las herramientas seleccionadas (Google Sites, Zapier/Make, ChatGPT Plus/Claude).
*   Ejemplos pre-construidos de asistentes (ej: un bot de soporte para e-commerce, un generador de posts para LinkedIn).

**Para los Participantes (Requisito previo):**
*   Laptop propia (obligatorio).
*   Cuentas creadas y logueadas en:
    *   Un modelo de lenguaje (ChatGPT, Claude o Gemini).
    *   Una herramienta de automatización (Zapier o Make tienen versiones gratuitas).
    *   Google Sheets o Airtable (cualquiera sirva como base de datos).
*   Correo electrónico corporativo o personal activo.

---

## 3. Estructura Detallada por Bloques

### Bloque 1: El Cerebro (Prompting Estratégico)
*   **Título:** De "Hola Bot" a "Empleado Ideal": Domina el Lenguaje.
*   **Duración:** 30 min (+ 10 min ejercicio).
*   **Objetivo:** Que entiendan que la calidad de la respuesta depende de la calidad de la instrucción.
*   **Dinámica:**
    *   *Charla Interactiva (10 min):* Demostración en vivo de un prompt "malo" vs. un prompt "excelente". Usar ejemplos reales de LatAm (ventas, atención al cliente, redacción de emails).
    *   *Ejercicio Rápido (15 min):* "El Desafío del Rol". Cada emprendedor debe definir qué rol juega la IA en su negocio (¿Vendedor? ¿Analista?) y escribir un prompt inicial.
    *   *Discusión (5 min):* Compartir en parejas sus prompts.
*   **Key Takeaway:** "La IA no es magia, es un empleado muy listo que necesita un manual de instrucciones claro".
*   **Slide Count:** 8 diapositivas (Mitos, Framework de Prompts, Ejemplo Antes/Después).

### Bloque 2: La Arquitectura (Conectando Puntos sin Código)
*   **Título:** Tu Stack Tecnológico de $0: Sin saber programar.
*   **Duración:** 45 min.
*   **Objetivo:** Entender cómo mover datos entre apps (ej: de WhatsApp a Email, de Formulario a Base de Datos) usando la IA.
*   **Dinámica:**
    *   *Demo Visual (15 min):* Mostrar un flujo simple: "Cuando llega un lead en Facebook -> La IA analiza si es serio -> Si lo es, le envía un email personalizado automáticamente".
    *   *Explicación de Herramientas (10 min):* Presentar el "Santo Grial" No-Code: Zapier/Make + AI. Explicar que no necesitan contratar un dev.
    *   *Q&A Técnico Básico (20 min):* Resolver dudas sobre seguridad de datos y privacidad (crucial en LatAm).
*   **Key Takeaway:** "Puedes automatizar procesos complejos conectando tus apps favoritas con un solo clic".
*   **Slide Count:** 10 diapositivas (Diagramas de flujo, Screenshots de interfaces, Casos de éxito locales).

---

## 4. El Ejercicio Principal: "Construye tu MVP en 45 Minutos"

Este es el corazón del taller. Todos saldrán con algo funcional.

*   **Nombre del Ejercicio:** "Mi Primer Asistente Operativo".
*   **El Reto:** Crear un asistente que resuelva **un solo dolor** específico de su startup hoy mismo.
*   **Guía Paso a Paso (Facilitador guía el ritmo):**
    1.  **Definir el Caso (5 min):** Elegir uno de tres escenarios pre-definidos para acelerar:
        *   *Opción A (Ventas):* Clasificar leads entrantes por WhatsApp y enviar propuesta.
        *   *Opción B (Marketing):* Tomar un artículo de blog y generar 5 tweets y 1 post de LinkedIn.
        *   *Opción C (Soporte):* Responder preguntas frecuentes de clientes basándose en un PDF de ayuda.
    2.  **Configurar la IA (10 min):** Escribir el "System Prompt" en la herramienta de chat para que actúe como ese especialista.
    3.  **Conectar la Acción (20 min):** Usar una herramienta No-Code (ej: usar Zapier para recibir un email y que la IA genere una respuesta, o usar un formulario web simple conectado a la IA). *Nota: Si el tiempo es corto, hacer el prototipo "semi-manual" donde ellos simulan el paso de entrada/salida pero prueban el flujo lógico.*
    4.  **Probar y Ajustar (10 min):** Probar con datos falsos y corregir el prompt.
*   **Resultado:** Un prototipo funcional (o un diagrama de flujo validado) que pueden implementar esa misma tarde.

---

## 5. Recursos para Llevar a Casa (Kit de Supervivencia)

Entregarás un PDF descargable o un enlace a Notion con:

1.  **Biblioteca de Prompts Maestros:** 10 plantillas listas para copiar y pegar para Ventas, Marketing, Soporte y RRHH.
2.  **Checklist de Seguridad de Datos:** Qué información NUNCA subir a una IA pública.
3.  **Lista de Herramientas No-Code:** Comparativa de Zapier vs. Make vs. n8n (con enlaces de prueba gratis).
4.  **Plantilla de "Job Description" para tu IA:** Un documento para que definen roles, tono y límites de su asistente antes de construirlo.
5.  **Video Tutorial Grabado:** Un link a una grabación de 5 min mostrando el ejercicio principal paso a paso para repasar en casa.
6.  **Comunidad:** Enlace a un grupo de Telegram/WhatsApp exclusivo de los asistentes del workshop para compartir avances.

---

## 6. Slide Count Estimado Total

*   **Total Diapositivas:** ~35 slides.
*   **Distribución:**
    *   Intro/Kick-off: 5 slides.
    *   Bloque 1 (Prompting): 8 slides.
    *   Bloque 2 (Arquitectura): 10 slides.
    *   Guía del Ejercicio Principal (Visual): 7 slides (muy visuales, poco texto).
    *   Cierre/Recursos: 5 slides.

---

## 💡 Consejos de Facilitador para el Éxito en LatAm

1.  **Usa Contexto Local:** Cuando hagas ejemplos, usa monedas locales (Pesos, Reales), nombres de ciudades conocidas y problemas típicos (ej: "cómo manejar el caos de WhatsApp Business").
2.  **Rompe la barrera técnica:** Insiste mucho en que **"No necesitas saber código"**. Repite esta frase cada hora. El miedo principal es creer que esto requiere un equipo de ingenieros.
3.  **Energía Alta:** No te quedes leyendo las diapositivas. Camina, toca las pantallas de los alumnos, celebra cuando logren que la IA haga algo bien.
4.  **Manejo del Tiempo:** El bloque principal suele alargarse. Ten un "Plan B" simplificado por si alguien se atasca con la configuración técnica; enfócalos en la lógica del prompt primero y la automatización después.

¡Listo para lanzar! Con este outline, tendrás un ambiente de alto impacto donde los emprendedores sentirán que ganaron un superpoder en 3 horas. ¿Te gustaría que desarrolle el guion de alguna sección específica?