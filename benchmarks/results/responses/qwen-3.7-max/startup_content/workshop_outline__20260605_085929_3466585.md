# Qwen 3.7 Max — startup_content/workshop_outline

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.28 | quality: 9.44
- latency_total: 77.57s | tokens_per_second: 50.4
- input_tokens: 202 | output_tokens: 3912
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Qué onda! Como facilitador que ha recorrido el ecosistema startupero desde México hasta Argentina, te digo algo: **a los founders early-stage de LatAm no les sirve la teoría de la IA, les sirve sobrevivir y escalar con pocos recursos.** 

Este workshop está diseñado para que se ensucien las manos. Cero código, 100% tracción. Vamos a usar **Custom GPTs (de OpenAI)** porque la curva de aprendizaje es mínima y el "efecto wow" es inmediato, y les mostraremos cómo la magia real en LatAm es conectar eso a **WhatsApp**.

Aquí tienes el blueprint completo para romperla en tu próximo workshop.

---

### 🛠️ 2. Materiales Necesarios (Preparación Pre-Workshop)

**Logística y Físicos:**
*   **Wi-Fi de alta densidad:** (Crítico. Si el internet falla, el workshop muere. Ten un router 4G/5G de respaldo).
*   **Extensiones y regletas:** 1 enchufe por asistente.
*   **Post-its de 3 colores diferentes y marcadores Sharpie.**
*   **"El Kit de Supervivencia" (Impreso o QR):** Un PDF con 3 prompts maestros, links a las herramientas y un dataset "dummy" (PDF con info de una startup ficticia para los que no trajeron su propia info).

**Digitales (Para el Facilitador):**
*   Cuenta Premium de ChatGPT (Plus/Team) para demostrar.
*   Cuenta en **Make.com** o **Zapier** (para la demo de WhatsApp).
*   Cuenta en **Interakt** o **Wati** (API oficial de WhatsApp Business) para mostrar el bot en vivo.
*   Grupo de WhatsApp temporal para que los asistentes se unan y prueben el bot del facilitador en tiempo real.

---

### ⏱️ 1. Agenda Detallada (3 Horas)

#### **Bloque 1: El Mindset - Tu Primer Empleado No Humano (20 min)**
*   **Objetivo:** Romper el miedo a la tecnología y enfocar la IA como una herramienta de *bootstrapping* (hacer más con menos).
*   **Dinámica:** Charla energética + Demo en vivo ("El Efecto Wow").
*   **Acción:** El facilitador muestra un bot en el grupo de WhatsApp del salón que responde dudas de la logística del evento en tiempo real usando voz y texto.
*   **Key Takeaway:** "La IA no te va a reemplazar, pero el founder que use IA te va a destruir si no la usas. Hoy contratas a tu primer empleado".
*   **Slides:** ~5 slides (Memés de founders estresados, estadísticas de LatAm sobre WhatsApp, video del bot).

#### **Bloque 2: El Cerebro - De la Idea al Prompt Maestro (30 min)**
*   **Objetivo:** Enseñar a estructurar el conocimiento de su startup para que la IA no alucine.
*   **Dinámica:** Ejercicio rápido con Post-its (Pair-sharing).
*   **Acción:** En parejas, definen el "Rol", el "Tono" y las "Reglas Inquebrantables" de su asistente (ej. *Nunca des descuentos mayores al 10%, siempre cierra con una pregunta*).
*   **Key Takeaway:** "Garbage in, garbage out. Tu IA es tan buena como el manual de operaciones que le escribas".
*   **Slides:** ~8 slides (Anatomía de un System Prompt, ejemplos de buenos vs malos prompts).

#### **Bloque 3: Manos a la Obra - Construyendo el Asistente (60 min) 🏆 EJERCICIO PRINCIPAL**
*   **Objetivo:** Que cada founder salga con un prototipo funcional de su asistente de IA.
*   **Dinámica:** Hackathon guiado (Sprint de construcción).
*   **Acción:** (Ver detalle del ejercicio abajo).
*   **Key Takeaway:** "Construir un MVP de IA ya no toma 3 meses y $10,000 USD. Toma 45 minutos y $20 USD al mes".
*   **Slides:** ~4 slides (Solo capturas de pantalla de los pasos a seguir en la UI de ChatGPT).

#### **☕ Break / Networking (10 min)**
*   *Música Lo-Fi de fondo. El facilitador camina por las mesas resolviendo dudas 1 a 1.*

#### **Bloque 4: La Magia LatAm - Conectando a WhatsApp y CRM (40 min)**
*   **Objetivo:** Sacar al bot de la web y ponerlo donde están los clientes latinos: WhatsApp.
*   **Dinámica:** Demo en pantalla grande + Discusión de casos de uso.
*   **Acción:** El facilitador muestra en vivo (usando Make.com/Zapier) cómo conectar el Custom GPT a un número de WhatsApp Business y cómo guardar los leads en un Google Sheet/Notion.
*   **Key Takeaway:** "Un bot en la web es un juguete. Un bot en WhatsApp que califica leads y los manda a tu CRM es una máquina de ventas".
*   **Slides:** ~10 slides (Diagramas de flujo visuales de Zapier/Make, costos de APIs).

#### **Bloque 5: Show & Tell + Plan de Acción (20 min)**
*   **Objetivo:** Validación social y compromiso de implementación.
*   **Dinámica:** Pitch relámpago (2 founders pasan al frente a mostrar su bot en la pantalla grande).
*   **Acción:** Cada fundador escribe en un post-it su "Next Step" para el lunes a las 9 AM y se lo lleva pegado en su laptop.
*   **Key Takeaway:** "La velocidad de implementación es tu única ventaja competitiva".
*   **Slides:** ~3 slides (Resumen de herramientas, QR para recursos, foto grupal).

---

### 🏆 4. Ejercicio Principal: "El SDR (Sales Dev Rep) Infatigable"

**El Reto:** Crear un asistente de IA que califique leads, responda objeciones de pricing y agende reuniones, usando la base de conocimiento de su propia startup.

**Paso a Paso para los Asistentes:**
1.  **Preparación de Datos (10 min):** Suben a su drive un PDF de 2-3 páginas con su Pitch Deck, Pricing, y Top 5 FAQs (o usan el PDF "Dummy" que provees).
2.  **Creación en Custom GPTs (20 min):**
    *   Van a *Create a GPT*.
    *   **Instructions:** Usan la fórmula que enseñaste en el Bloque 2 (Rol + Contexto + Tono + Restricciones). *Ej: "Eres el SDR de [Startup]. Tu tono es amigable pero profesional. Nunca inventes features. Si preguntan por precio, dales el plan Básico y pregunta por su presupuesto".*
    *   **Knowledge:** Suben su PDF.
3.  **Entrenamiento y Testeo (20 min):**
    *   En la ventana de *Preview*, simulan ser el cliente más difícil y tóxico posible. Intentan hacer que el bot "alucine" o rompa las reglas.
    *   Ajustan las instrucciones en tiempo real hasta que el bot se comporte perfecto.
4.  **Publicación (10 min):** Lo configuran como "Anyone with the link" y comparten el link en el grupo de WhatsApp del workshop para que otros founders intenten "romper" sus bots.

---

### 🎒 5. Recursos para Llevar a Casa (El "Take-Home Stack")

Al terminar, les envías un correo/Notion con:
1.  **La "Biblia" de Prompts para Startups (Notion Template):** 15 prompts listos para copiar/pegar (Generador de Cold Emails, Analizador de Feedback de Usuarios, Resumen de Llamadas de Ventas).
2.  **El Blueprint de Make.com (PDF):** Diagrama visual de cómo conectar OpenAI -> WhatsApp -> Google Sheets, con links a los módulos exactos.
3.  **Calculadora de ROI de IA (Excel):** Una hoja simple donde calculan cuántas horas de soporte/ventas les ahorra el bot y a cuánto equivale en salario mínimo de su país.
4.  **Directorio de Herramientas No-Code:** Links a Voiceflow, Botpress, Make, Zapier, y Chatbase con notas sobre cuándo usar cada una.

---

### 📊 6. Slide Count Estimado por Sección (Total: ~30 Slides)

*La regla de oro: Cero paredes de texto. Usa capturas de pantalla, memes de startups, y diagramas de flujo.*

*   **Intro & Mindset:** 5 slides (Enfocado en dolor del founder y la oportunidad).
*   **El Cerebro (Prompts):** 8 slides (Fórmulas visuales, ejemplos de "Lo que dijiste vs Lo que la IA entendió").
*   **Manos a la Obra:** 4 slides (Solo QR codes a los datasets dummy y los 4 pasos críticos en la UI).
*   **Conexión WhatsApp/CRM:** 10 slides (Capturas de Make/Zapier, costos reales de Twilio/Meta, diagramas de arquitectura simples).
*   **Cierre:** 3 slides (Llamado a la acción, QR de feedback, redes sociales).

---

### 💡 Tips de Facilitador (El "Sabor" LatAm)

*   **Habla de plata y tiempo:** En LatAm el runway es corto. No hables de "Transformación Digital", habla de "Cómo atender 500 mensajes de WhatsApp el fin de semana sin contratar a un Community Manager".
*   **El "Parked Lot" (Estacionamiento):** Si alguien hace una pregunta súper técnica o de nicho (ej. "¿Cómo hago fine-tuning con Llama 3 en AWS?"), córtalo con buena onda: *"Esa es una pregunta de nivel Senior, la anoto en el 'Parked Lot' y te la respondo por LinkedIn al terminar, hoy estamos en modo supervivencia y tracción"*.
*   **Maneja la frustración:** Las APIs a veces fallan o ChatGPT se satura. Ten siempre un plan B (un video grabado de ti haciendo el proceso) por si el internet del venue decide sabotear el workshop.

¡Con esta estructura te aseguro que los founders salen con la adrenalina a tope, un bot funcionando en su celular y recomendando tu workshop a toda su cofounder network! ¿Quieres que profundicemos en el PDF "Dummy" o en el diagrama de Make.com?