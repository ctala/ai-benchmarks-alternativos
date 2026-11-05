# Nemotron 3 Super — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.41 | quality: 9.52
- latency_total: 47.836s | tokens_per_second: 98.8
- input_tokens: 206 | output_tokens: 4728
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

¡Claro! Aquí tienes el **outline completo** para tu workshop presencial de **3 horas**, diseñado específicamente para **emprendedores early-stage no técnicos** (20-30 personas), con un tono **energético, práctico y sin jerga académica**. El enfoque es: **“Hazlo tú mismo, hoy, sin código”**.

---

## 🚀 **WORKSHOP: “Construye tu Asistente de IA para tu Startup – Workshop Práctico”**  
*Duración total: 3 horas | Audiencia: Emprendedores early-stage no técnicos (20-30 personas)*  
*Objetivo general: Al final del taller, cada participante tendrá un asistente de IA funcional (sin código) que puede responder preguntas básicas sobre su startup, y sabrá cómo mejorarlo y escalarlo.*

---

### ✅ **1. AGENDA DETALLADA CON TIEMPOS (3 HORAS)**

| Hora | Bloque | Actividad |
|------|--------|-----------|
| 0:00 – 0:15 | **Bienvenida y Calentamiento** | Icebreaker + contexto + por qué esto importa AHORA |
| 0:15 – 0:45 | **Bloque 1: ¿Qué es un asistente de IA (y qué NO es)?** | Charla interactiva + ejemplos reales |
| 0:45 – 1:25 | **Bloque 2: Herramientas sin código para construir tu asistente** | Demo en vivo + comparación rápida |
| 1:25 – 1:40 | **Pausa activa** | Agua, estiramiento, networking relámpago |
| 1:40 – 2:30 | **Bloque 3: ¡Construye tu asistente PASO A PASO!** | Ejercicio principal guiado (todos construyen el suyo) |
| 2:30 – 2:50 | **Bloque 4: Prueba, mejora y escala** | Demo de mejoras + discusión en grupos pequeños |
| 2:50 – 3:00 | **Cierre y llamado a la acción** | Compartir resultados, recursos para llevar, próximos pasos |

> ⏱️ *Nota: Los tiempos incluyen transición y preguntas espontáneas. Se asume un ritmo dinámico, no pausado.*

---

### ✅ **2. MATERIALES NECESARIOS (QUE PREPARAR ANTES)**

**Para el facilitador:**
- Laptop con conexión a internet (proyector o pantalla grande)
- Clicker para avanzar slides
- Micrófono (si el espacio es grande)
- Timer visible (puede ser en el teléfono o proyector)
- Marcadores y pizarrón blanco o paperboard (para anotar ideas espontáneas)
- Pegatinas de colores (para votaciones rápidas)
- Copias impresas de la “Hoja de Trabajo del Asistente de IA” (ver sección 4)
- Botellas de agua y snacks ligeros (frutas, nueces) — *mantiene la energía alta*

**Para cada participante (entregar al llegar):**
- Hoja de trabajo impresa (1 página, doble cara) — incluye:
  - Espacio para definir su startup (nombre, problema, cliente ideal)
  - Lista de 5 preguntas clave que su asistente debe responder
  - Espacio para anotar el “prompt base” y los ajustes
  - Checklist de “¿Está listo para probar?”
- Acceso a una cuenta gratuita pre-creada en **Voiceflow** (o alternativa: Landbot o Tidio) — *pre-registrar 30 cuentas con email temporal tipo `startup1@talleria.com`*
- Tarjeta con QR code que lleva a:
  - Guía paso a paso en PDF (para llevar a casa)
  - Lista de 5 herramientas gratuitas (sin código) para asistentes de IA
  - Video tutorial de 5 min (revisar después)
- Bolígrafo

> 💡 *Tip: Pre-crear las cuentas en Voiceflow evita que pierdan tiempo registrándose. Usa emails temporales y elimínalos después del workshop si es necesario.*

---

### ✅ **3. BLOQUES DETALLADOS**

#### **Bloque 0: Bienvenida y Calentamiento (15 min)**  
- **Título:** “¿Tu startup ya tiene un empleado que nunca duerme?”  
- **Objetivo:** Romper el hielo, generar curiosidad y conectar el tema con su dolor diario (responder las mismas preguntas una y otra vez).  
- **Dinámica:**  
  - Icebreaker: “Levántate si hoy respondiste la misma pregunta de un cliente/inversor más de 3 veces.” (La mayoría se levanta → risas y conexión).  
  - Breve historia: “Yo también fui emprendedor no técnico… y perdí 10 horas/semana respondiendo FAQs. Hasta que construí mi primer asistente de IA… sin saber programar.”  
  - Muestra un video de 30 seg de un asistente de IA respondiendo preguntas reales de una startup latinoamericana (ej: “¿Cuánto cuesta tu plan?”, “¿Dónde están ubicados?”).  
- **Key takeaway:** *“Tu tiempo es tu recurso más escaso. Un asistente de IA no te reemplaza… te libera para hacer lo que solo tú puedes hacer.”*  
- **Slide count estimado:** 3 slides (title, icebreaker result, antes/después)

---

#### **Bloque 1: ¿Qué es un asistente de IA (y qué NO es)? (30 min)**  
- **Título:** “IA no es magia… es un empleado muy bien entrenado”  
- **Objetivo:** Desmitificar la IA, eliminar el miedo a lo técnico y enfocarse en lo útil para su startup.  
- **Dinámica:**  
  - Charla interactiva con analogías cotidianas:  
    - “Es como entrenar a un nuevo pasante… pero le das instrucciones por escrito, y nunca se olvida.”  
    - Muestra 3 ejemplos reales:  
      1. Un asistente que responde preguntas de precios y horarios (e-commerce)  
      2. Uno que ayuda a founders a explicar su pitch en 30 seg (edtech)  
      3. Uno que recopila feedback de usuarios tras una demo (saas B2B)  
  - Mini-enquête con pegatinas: “¿Cuál de estas tareas te quita más tiempo?” (Opciones: responder emails, explicar tu producto, seguir leads, hacer facturas, otras) → se pega en un cartel.  
  - Clarifica qué NO es:  
    - ❌ No reemplaza tu visión ni tu ventas  
    - ❌ No necesita código ni PhD  
    - ❌ No es caro (muchas opciones gratis)  
- **Key takeaway:** *“Un asistente de IA no es un robot complejo… es un documento de instrucciones muy bien seguido por una máquina que nunca se cansa.”*  
- **Slide count estimado:** 6 slides (definición, mitos vs realidad, 3 ejemplos, encuesta en vivo, qué NO es, tu turno)

---

#### **Bloque 2: Herramientas sin código para construir tu asistente (40 min)**  
- **Título:** “3 herramientas gratis que usan founders como tú (y no necesitan ingeniero)”  
- **Objetivo:** Mostrar opciones accesibles, compararlas en 2 minutos cada una y elegir una para el ejercicio práctico.  
- **Dinámica:**  
  - Demo en vivo (10 min por herramienta):  
    1. **Voiceflow** → mejor para flujos conversacionales (voz y texto), ideal si quieren integrarlo en WhatsApp o web.  
    2. **Landbot** → súper visual, perfecto para landing pages y captura de leads.  
    3. **Tidio** → fácil de instalar en WordPress/Shopify, buen soporte en español.  
  - En cada demo:  
    - Muestro cómo crear un “saludo” y una respuesta a una pregunta simple (ej: “¿Cuál es tu precio?”).  
    - Resalto: “¿Cuánto tardé? 4 minutos. ¿Necesité código? No.”  
  - Luego, votación rápida con pegatinas: “¿Cuál te parece más fácil de empezar?” → se revela el ganador (usualmente Voiceflow por su equilibrio poder/simplicidad).  
  - Explico por qué elegimos Voiceflow para el ejercicio: gratis hasta 1000 mensajes/mes, interfaz en español, buena comunidad latinoamericana.  
- **Key takeaway:** *“No necesitas la herramienta más potente… necesitas la que puedes usar HOY sin pedir ayuda.”*  
- **Slide count estimado:** 5 slides (intro, 3 herramientas con screenshots, comparación rápida, por qué elegimos Voiceflow)

---

#### **Bloque 3: ¡Construye tu asistente PASO A PASO! (50 min)** → **EJERCICIO PRINCIPAL**  
- **Título:** “Tu asistente en 25 minutos: manos a la obra”  
- **Objetivo:** Que cada participante construya un asistente de IA funcional que responda al menos 3 preguntas clave de su startup.  
- **Dinámica:**  
  - **Paso 1 (5 min):** Completa la hoja de trabajo:  
    - Nombre de tu startup  
    - Problema que resuelves  
    - Cliente ideal  
    - **Escribe 5 preguntas que te hacen constantemente** (ej: “¿Cómo funciona?”, “¿Cuánto cuesta?”, “¿Dónde están?”, “¿Cómo empiezo?”, “¿Qué tan seguro es?”)  
    - Elige las **TOP 3** que más te quitan tiempo.  
  - **Paso 2 (5 min):** Te guío a crear tu cuenta en Voiceflow (usando el email pre-asignado).  
  - **Paso 3 (30 min):** Construimos juntos, paso a paso, en pantalla:  
    1. Crear un nuevo agente → nombrearlo (ej: “Asistente de [Tu Startup]”)  
    2. Añadir un “Start” node (saludo: “¡Hola! Soy el asistente de [Startup]. ¿En qué puedo ayudarte?”)  
    3. Añadir 3 “Intent” nodes (uno por cada pregunta top):  
       - Ej: Intent “Precio” → responde: “Nuestro plan básico cuesta $19/mes y el profesional $49/mes. ¿Quieres ver un comparativo?”  
       - Ej: Intent “Ubicación” → respondemos: “Estamos en Medellín, pero atendemos a toda LATAM remotamente.”  
       - Ej: Intent “Cómo empezar” → respondemos: “¡Genial! Solo necesitas registrarte en [link] y te guiamos en 5 minutos.”  
    4. Añadir un “Fallback” node (cuando no entiende): “Lo siento, aún no aprendí eso. ¿Puedes reformular tu pregunta? O puedes escribir ‘ayuda’ para ver qué puedo hacer.”  
    5. Probarlo en el simulador de Voiceflow (¡en vivo!): yo pruebo uno, luego ellos prueban el suyo.  
  - **Paso 4 (10 min):** Tiempo libre para ajustar, probar y pedir ayuda a los vecinos (fomento el networking activo).  
  - Yo recorro la sala, doy tips personalizados: “¿Notaste que si escribes ‘cuánto sale’ no lo entiende? Añádelo como variación del intent ‘Precio’.”  
- **Key takeaway:** *“No necesitas perfección… necesitas un primer versión que funcione. La mejora viene después.”*  
- **Slide count estimado:** 8 slides (paso a paso con screenshots grandes, 1 slide por paso + 1 de “¡Tú puedes!” + 1 de errores comunes a evitar)

---

#### **Bloque 4: Prueba, mejora y escala (20 min)**  
- **Título:** “Tu asistente no es estático: hazlo más inteligente cada semana”  
- **Objetivo:** Mostrar cómo mejorarlo con datos reales y pensar en escalarlo (WhatsApp, sitio web, etc.).  
- **Dinámica:**  
  - Demo rápida de 3 mejoras fáciles (5 min):  
    1. Añadir una pregunta que surgió en las pruebas de otros (ej: “¿Ofrecen prueba gratis?”) → mostrar cómo agregarla en 2 min.  
    2. Ver el historial de conversaciones (Voiceflow lo guarda gratis) → “Así ves qué preguntas te están haciendo en realidad.”  
    3. Conectarlo a WhatsApp usando la integración gratuita de Voiceflow (mostrar el enlace de configuración — no entrar en detalle, solo decir: “Está aquí, lo haces en 10 min después del taller”).  
  - Discusión en grupos de 3-4 personas (7 min):  
    - Pregunta guía: *“¿Cuál es UNA pregunta que tu asistente NO respondió bien hoy… y cómo la agregarías mañana?”*  
    - Cada grupo comparte 1 idea en voz alta (se anotan en un paperboard).  
  - Cierre del bloque: Muestro un caso real de una startup colombiana que redujo un 70% sus emails de soporte en 3 semanas con su asistente.  
- **Key takeaway:** *“Tu asistente mejora cuando tú escuchas a tus clientes… no cuando aprendes a programar.”*  
- **Slide count estimado:** 4 slides (mejoras fáciles, cómo ver historial, integración WhatsApp, caso de éxito)

---

#### **Bloque 5: Cierre y llamado a la acción (10 min)**  
- **Título:** “Tu turno: lleva esto a tu startup esta semana”  
- **Objetivo:** Consolidar el aprendizaje, inspirar acción inmediata y entregar recursos para seguir.  
- **Dinámica:**  
  - Invito a 2-3 voluntarios a compartir:  
    - “¿Cuál fue tu ‘aha moment’?”  
    - “¿Cuál es la primera pregunta que le vas a poner a tu asistente mañana?”  
  - Entrego:  
    - La hoja de trabajo (ya la tienen)  
    - El QR code con recursos para llevar a casa (ver sección 5)  
    - Un sticker que dice: “Mi asistente de IA está en construcción 🚀” (para poner en su laptop)  
  - Última frase:  
    > “No esperes a tener un equipo de tech. Tu primera versión de IA no necesita ser perfecta… solo necesita estar *activa*. Hazla hoy. Mañana ya estarás adelante del 90% de los founders que aún están pensando en ello.”  
  - Aplausos, fotos grupales, networking libre.  
- **Key takeaway:** *“La IA no es para el futuro… es para tu lunes por la mañana. Empieza ahora.”*  
- **Slide count estimado:** 3 slides (llamado a la acción, QR + recursos, foto de equipo inspiradora)

---

### ✅ **4. EJERCICIO PRINCIPAL DEL WORKSHOP**

> **“Construye tu asistente de IA en Voiceflow que responda las 3 preguntas más frecuentes de tu startup — en menos de 30 minutos.”**

- **Por qué funciona:**  
  - Es concreto, acotado y medible (3 preguntas).  
  - Usa su propio contexto (su startup) → alta relevancia y motivación.  
  - No requiere conocimiento previo → accesible para no técnicos.  
  - Genera un entregable tangible que pueden probar inmediatamente.  
  - Fomenta la autonomía: al salir, saben cómo modificarlo y escalarlo.  
- **Resultado esperado:** Cada participante tiene un asistente funcional en su cuenta de Voiceflow, probado en el simulador, listo para conectar a su sitio web o WhatsApp en las próximas 24-48 horas.

---

### ✅ **5. RECURSOS PARA LLEVAR A CASA (ENTREGADOS AL FINAL)**

Todos los recursos están accesibles por **QR code** (impreso en una tarjeta de crédito tamaño) y también enviados por email al día siguiente (para quienes no escanearon):

- 📄 **Guía paso a paso en PDF** (8 páginas):  
  - “Cómo construir tu primer asistente de IA en Voiceflow (sin código)”  
  - Con screenshots en español, tips de redacción de prompts, y lista de errores comunes.  
- 🔗 **Lista de 5 herramientas gratuitas (sin código) para asistentes de IA** (con enlaces directos y pros/contras):  
  1. Voiceflow  
  2. Landbot  
  3. Tidio  
  4. Chatbase (para entrenar con tu sitio web)  
  5. ManyChat (si enfocan en WhatsApp/Instagram)  
- ▶️ **Video tutorial de 5 min** (YouTube, privado, solo para asistentes):  
  - Recapitulación del ejercicio principal (construir las 3 intents).  
- 📋 **Plantilla de “Lista de Preguntas para tu Asistente”** (editable en Google Docs):  
  - Para que cada semana añadan nuevas preguntas basadas en lo que escuchan de clientes.  
- 💬 **Acceso a una comunidad privada de WhatsApp/Telegram** (opcional):  
  - “Founders de IA sin código LATAM” — para compartir dudas, éxitos y plantillas.  
- 🎁 **Bonus:** Cupón de 20% de descuento en el plan pagado de Voiceflow (por 3 meses) — gestionado previamente con el equipo de Voiceflow para el evento.

---

### ✅ **6. SLIDE COUNT ESTIMADO POR SECCIÓN**

| Sección | Slides estimados | Comentario |
|--------|------------------|------------|
| Bienvenida y Calentamiento | 3 | Muy visual, mínimo texto |
| Bloque 1: ¿Qué es un asistente de IA? | 6 | Enfocado en ejemplos y mitos |
| Bloque 2: Herramientas sin código | 5 | Comparativa clara, demo en vivo |
| Bloque 3: Ejercicio principal (construir) | 8 | Paso a paso con screenshots grandes |
| Bloque 4: Prueba, mejora y escala | 4 | Enfocado en acciones simples y casos reales |
| Cierre y llamado a la acción | 3 | Inspirador, bajo en texto, alto en emoción |
| **TOTAL** | **29 slides** | *Nota: Muchos slides son de 1 imagen + 1 frase. Evitar bloques de texto. Usar iconos, fotos de founders reales, y colores de la marca del workshop (ej: naranja + azul eléctrico).* |

---

### 💡 **NOTAS FINALES PARA EL FACILITADOR**

- **Energía es clave:** Usa tu voz, movimiento, humor. Pregunta: “¿Quién aquí se siente abrumado por responder lo mismo una y otra vez?” → levántate tú primero.  
- **Evita el tecnicismo:** Nunca digas “NLP”, “intent classification”, “token”. Di: “le enseñas qué significa cuando alguien dice X”.  
- **Sé el primer usuario:** Prueba tu propio asistente en voz alta durante el demo. Muestra fallos y cómo los arreglas — eso genera confianza.  
- **Fomenta el “imperfecto action”: ** El objetivo no es un asistente de nivel enterprise… es uno que *funciona hoy* y les ahorra 1 hora esta semana.  
- **Después del workshop:** Envía el email con recursos a las 24h. Haz un follow-up a los 7 días: “¿Ya probaste tu asistente? ¿Cuánto tiempo te ahorró?” — esto genera testimonio y lealtad.

---

Este workshop no enseña IA… **enseña a recuperar tu tiempo**.  
Y para un fundador early-stage, eso es más valioso que cualquier ronda de financiación.

¡Éxito con tu taller! 🚀  
Si quieres, puedo ayudarte a crear los slides o la hoja de trabajo en formato listo para imprimir. Solo dime.