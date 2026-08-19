# Seed 2.0 Code — startup_content/workshop_outline

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.65 | quality: 8.76
- latency_total: 37.657s | tokens_per_second: 54.4
- input_tokens: 238 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

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


El usuario pide un outline completo de workshop presencial de 3 horas para emprendedores early-stage NO TÉCNICOS, sobre construir asistente de IA para startup. Primero, tengo que adaptarme a la audiencia: no saben código, son early-stage, así que necesitan HERRAMIENTAS SIN CÓDIGO, ejemplos relevantes para startups (captación de leads, soporte, onboarding), no jerga.

Primero, la agenda detallada con tiempos: 3 horas, ¿con pausa? Sí, porque 3 horas seguidas es mucho, pero no muy larga: 10 min de pausa a la 1h30, por ejemplo. Tiene que ser estructurado: bienvenida, contexto, herramientas sin código, ejercicio práctico (el principal), aplicación a su startup, cierre.

Luego, materiales necesarios: tanto para el facilitador como para los participantes. Los participantes necesitan laptop o celular (porque no son técnicos, tal vez algunos traen celular, pero mejor especificar laptop preferido, pero compatible con celular), cuenta gratuita en herramientas SIN CÓDIGO: ¿cuáles? No ChatGPT solo, sino herramientas que hagan ASISTENTES CON INTERFAZ, porque es para STARTUP: Typeform? No, mejor herramientas específicas de asistentes sin código: Tars (pero tiene prueba gratuita), Chatbase (sí, Chatbase es genial porque sube documentos de la startup (pitch, FAQs, catálogo) y crea un asistente con enlace o widget, GRATIS para plan básico), tal vez también ManyChat pero Chatbase es más versátil para cualquier startup (no solo redes). También, materiales impresos: hoja de ruta para su asistente, ejemplos de startups latinas con asistentes, tarjetas de ayuda con pasos de Chatbase.

Para cada bloque: título, duración, objetivo, dinámica, key takeaway. También slide count estimado: importante, no exceder, porque es práctico.

El ejercicio principal: tiene que ser que TODOS puedan hacerlo en el tiempo, sin código. ¿Qué? Que cada emprendedor cree un ASISTENTE DE IA BÁSICO PARA SU STARTUP en 45 min, usando Chatbase (plan gratuito), subiendo 1-2 documentos propios (si no traen, usar un modelo de FAQs de startup genérico que el facilitador prepare), personalizar el nombre, tono, y generar el enlace para probarlo. También, que definan el CASO DE USO ESPECÍFICO para su startup (no genérico: por ejemplo, "asistente para captar leads de clientes de cafetería gourmet que preguntan por menús de catering" vs "asistente general").

Recursos para llevar a casa: lista de herramientas sin código (Chatbase, Tars, ManyChat, Botpress Community Edition), plantilla de FAQs para asistente, hoja de medición de resultados (qué métricas mirar: tasa de respuesta, leads captados, tiempo de soporte reducido), acceso a un grupo de WhatsApp/Telegram para dudas post-workshop, grabación de la demo (si se permite), ejemplos de asistentes de startups latinas.

Slide count: por sección, por ejemplo, bienvenida 3 slides, contexto 5, herramientas 4, ejercicio 2, aplicación 3, cierre 2: total alrededor de 20 slides, lo cual es poco, ideal para práctico.

Ahora, estructurar la agenda con tiempos exactos:

Total: 3 horas = 180 min. Vamos a dividir:

1. Bienvenida + "Check de Realidad" (15 min): Porque los emprendedores no técnicos piensan "necesito código para IA", así que desmentir eso rápidamente. Dinámica: charla interactiva + encuesta rápida (levantar la mano: ¿cuántos creen que necesitan programar para hacer un asistente de IA? ¿cuántos tienen FAQs en su startup? ¿cuántos pierden tiempo respondiendo las mismas preguntas?). Key takeaway: "La IA para startups no necesita código, se enfoca en SOLUCIONAR PROBLEMAS CONCRETOS".

2. Bloque 1: ¿Por qué un Asistente de IA VALE LA PENA para TU Startup Early-Stage? (25 min): Objetivo: que entiendan casos de uso REALES de startups latinas early-stage, no de Google. Dinámica: charla con demos rápidos (ejemplo: asistente de una startup de alquiler de bicicletas en CDMX que responde sobre precios, ubicaciones, y capta leads; asistente de una startup de cuidado de mascotas en Bogotá que hace onboarding de clientes). También discusión grupal: ¿cuál es el problema que más te quita tiempo en tu startup? (levantar la mano: soporte, captación de leads, onboarding, administración). Slide count: 5 slides. Key takeaway: "Tu asistente de IA debe resolver UN SOLO PROBLEMA CONCRETO, no ser un 'todo terreno'".

3. Pausa Corta (10 min): Importante para estirar, ir al baño, tomar agua. El facilitador puede estar disponible para preguntas rápidas.

4. Bloque 2: Herramientas SIN CÓDIGO para Crear tu Asistente (20 min): Objetivo: que conozcan herramientas accesibles (gratis o prueba gratuita) para su perfil no técnico. Dinámica: DEMO EN VIVO de Chatbase (porque es el más fácil para no técnicos): 1) Crear cuenta gratuita con Google, 2) Subir un documento (FAQs de startup genérica que el facilitador preparó), 3) Personalizar nombre, tono (amigable, profesional, juvenil), 4) Generar enlace de prueba. También mencionar otras herramientas por caso de uso: ManyChat para redes sociales, Tars para landing pages, Botpress Community para más personalización (pero solo mencionar, no demo). Slide count: 4 slides. Key takeaway: "Chatbase es la herramienta ideal para empezar: GRATIS, SIN CÓDIGO, y se integra con tu sitio web o redes en 5 min".

5. Bloque 3: EJERCICIO PRINCIPAL (45 min): ESTE ES EL CORAZÓN. Objetivo: que CADA EMPRENDEDOR CREE SU PROPIO ASISTENTE DE IA FUNCIONAL para su startup, sin código. Dinámica: Guiado paso a paso por el facilitador, con ayudantes (si hay, pero si no, tarjetas de ayuda). Pasos del ejercicio:
   a. Paso 1 (5 min): Definir el PROBLEMA CONCRETO que resolverá tu asistente (ej: "Asistente para responder preguntas de clientes de mi tienda de ropa sostenible sobre tallas y envíos, y captar su correo para descuentos"). Usar la hoja de ruta impresa.
   b. Paso 2 (10 min): Crear cuenta gratuita en Chatbase (con Google, no necesidad de tarjeta).
   c. Paso 3 (15 min): Preparar el contenido: si traen sus propios documentos (FAQs, pitch, catálogo), subirlos; si no, usar la PLANTILLA DE FAQs GRATUITA que el facilitador compartió por QR o enlace (plantilla adaptada a startups: preguntas sobre qué es el producto, precios, formas de pago, envíos, garantía). También pueden escribir 5 preguntas y respuestas directamente en Chatbase si no tienen documentos.
   d. Paso 4 (10 min): Personalizar el asistente: nombre (ej: "Asistente Sostenible de TiendaVerde"), tono (amigable, juvenil), agregar un llamado a la acción (ej: "Si quieres un descuento del 10%, déjanos tu correo aquí").
   e. Paso 5 (5 min): Probar el asistente y compartir el enlace en el chat del grupo (si se creó un grupo temporal de WhatsApp para el workshop).
   El facilitador camina por las mesas para ayudar a quienes tienen problemas (ej: no pueden subir el documento, no saben personalizar el tono). También hay tarjetas de ayuda con pasos ilustrados.
   Key takeaway: "Ya tienes un asistente de IA FUNCIONAL para tu startup, en menos de 45 min, sin código".
   Slide count: 2 slides (solo con los pasos del ejercicio, para que lo vean en pantalla).

6. Bloque 4: De Asistente Básico a Herramienta de Ingresos (20 min): Objetivo: que sepan cómo usar su asistente para generar valor real (no solo un juguete). Dinámica: discusión grupal + demo rápida de integración: 1) Cómo poner el widget de Chatbase en su sitio web (si lo tienen), 2) Có