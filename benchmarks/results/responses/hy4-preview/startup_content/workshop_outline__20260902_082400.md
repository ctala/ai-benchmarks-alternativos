# Tencent Hy4 preview — startup_content/workshop_outline

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.18 | quality: 9.72
- latency_total: 89.927s | tokens_per_second: 56.8
- input_tokens: 220 | output_tokens: 5106
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

¡Hola! Como facilitador con experiencia en LATAM, sé exactamente qué necesita este público: **acción, cero humo teórico y herramientas que puedan usar hoy mismo**. Los emprendedores early-stage quieren ver cómo la IA les va a ahorrar "chamba" operativa o ayudarles a vender más. 

Aquí tienes el diseño de la experiencia (el "outline") para que te luzcas. El tono de esta guía es enérgico, directo y enfocado en la ejecución.

---

### 🛠️ 1. Materiales Necesarios (Preparación Previa)

**Infraestructura (El "Kit de Supervivencia"):**
*   **Sala:** Mesas o superficies planas (todos usarán laptop).
*   **Conectividad:** Wi-Fi de alta velocidad (¡Vital! Lleva un Hotspot 4G/5G de respaldo por si falla la sala).
*   **Energía:** Extensores de corriente / zapatillas para TODAS las mesas (3 horas de laptops agotan las baterías).
*   **Visuales:** Proyector, pantalla grande y adaptadores HDMI/USB-C.

**Material de Apoyo:**
*   Plantillas impresas del **"Canvas de Asistente IA"** (1 por participante).
*   Post-its y marcadores.

**Pre-Work (Enviar por correo 2 días antes):**
*   Pedirles que traigan laptop y que se creen una cuenta gratuita en **Claude.ai, ChatGPT o Google Gemini**.
*   Pedirles que lleven en una carpeta digital (o en un Word/Notion) un **documento base** de su negocio: puede ser un PDF de preguntas frecuentes, su catálogo de servicios, o el guion de ventas que usan en WhatsApp. (Esto será el "cerebro" de su asistente).

---

### ⏱️ 2. Agenda Detallada y Estructura de Bloques (180 Minutos)

#### Bloque 1: Romper el Hielo y el "Para Qué" (15 mins)
*   **Título:** ¡Tu nuevo co-fundador digital!
*   **Objetivo:** Romper el hielo, bajar la ansiedad tecnológica y alinear expectativas.
*   **Dinámica:** *Charla express + Dinámica de presentación.* Todos se presentan en 15 segundos: Nombre, Startup y **¿Qué tarea de su día a día odian hacer o les quita más tiempo?**
*   **Key Takeaway:** La IA no viene a reemplazarte, viene a hacerse cargo de esa tarea que odias para que tú te enfoques en hacer crecer el negocio.
*   **Slides:** 3 (Título, Reglas del juego, La dinámica).

#### Bloque 2: El Cerebro de la Operación (30 mins)
*   **Título:** Diseñando tu Asistente (Cero Código, Pura Estrategia)
*   **Objetivo:** Aprender a estructurar el "cerebro" de la IA. Entender que el Prompt es el nuevo código.
*   **Dinámica:** *Charla interactiva + Ejercicio en parejas.* Usarán el "Canvas de Asistente IA" en papel para definir: **R**ol, **O**bjetivo, **T**ono de voz y **L**ímites (qué *no* debe hacer).
*   **Key Takeaway:** *Garbage in, garbage out* (Si le das basura, te da basura). El 80% del éxito de un asistente está en el contexto y las instrucciones claras, no en la herramienta mágica.
*   **Slides:** 6 (Qué es un LLM a nivel usuario, Anatomía de un buen Prompt, Ejemplos buenos vs. malos).

#### Bloque 3: ¡Manos a la Obra! (60 mins) - **EJERCICIO PRINCIPAL**
*   **Título:** Construyendo tu Asistente en Vivo
*   **Objetivo:** Que cada participante salga con un asistente funcional y probado.
*   **Dinámica:** *Demo paso a paso + Follow along (Seguimiento).* Tú proyectas tu pantalla y construyes un asistente en vivo (usaremos **Custom GPTs de OpenAI, Gemini Gems o Claude Projects**, según lo que tengan disponible). Ellos replican el proceso en sus laptops. Tú y un co-facilitador (si hay presupuesto) circulan por la sala resolviendo dudas.
*   **Key Takeaway:** Cualquier emprendedor, sin saber programar, puede tener un prototipo de IA funcional en menos de 60 minutos.
*   **Slides:** 8 (Paso a paso visual con flechas y capturas de pantalla de la herramienta).

#### Pausa Activa / Networking (15 mins)
*   **Título:** Recarga de Energía ☕
*   **Objetivo:** Estirar las piernas y despejar la mente.
*   **Slides:** 1 (Cronómetro en pantalla con música de fondo).

#### Bloque 4: Pruebas, Ajustes y "Hackeo" Mental (30 mins)
*   **Título:** Pon a Prueba a tu Nuevo Empleado
*   **Objetivo:** Testear el asistente, refinar respuestas y aprender a iterar.
*   **Dinámica:** *Roleplaying.* Los participantes deben "entrevistar" o "atacar" a su propio asistente. Intentarán que la IA se equivoque o invente información (alucine). Después, aprenderán a corregir eso ajustando el prompt base.
*   **Key Takeaway:** La IA alucina y se equivoca. Tu trabajo como "jefe" es ponerle límites estrictos (guardrails) y decirle qué hacer cuando no sabe la respuesta.
*   **Slides:** 5 (Ejemplos de alucinaciones, Cómo corregir un prompt, Matriz de pruebas).

#### Bloque 5: Despliegue y Cierre (30 mins)
*   **Título:** Conecta tu Asistente al Mundo Real
*   **Objetivo:** Mostrar cómo integrarlo en canales reales y generar el compromiso de acción.
*   **Dinámica:** *Charla rápida + Ronda de compromisos.* Mostrar un video de 2 minutos de cómo conectar esto a WhatsApp (Twilio, Zapier, ManyChat) o a la web. Cierre con la dinámica: **"¿Cuál es la única acción que vas a tomar mañana a las 9 AM con este asistente?"** (Lo dicen en voz alta a su compañero de mesa).
*   **Key Takeaway:** El mejor asistente de IA no es el más complejo, es el que ya está hablando con tus clientes hoy mismo.
*   **Slides:** 6 (Integraciones, Costos estimados, Próximos pasos, Cierre).

---

### 💻 4. El Ejercicio Principal del Workshop (Detalle)

**El Reto:** *Crear un "Asistente de Soporte y Ventas" o un "Generador de Contenido" en 60 minutos.*

**Herramienta:** Para no técnicos, la interfaz más amigable es crear un **Custom GPT (OpenAI)** o un **Gem/Project (Google/Anthropic)**.
**Paso a paso del ejercicio:**
1.  **Instrucción Base (System Prompt):** Usar la plantilla en papel del Bloque 2 y pegarla en la configuración de la herramienta. (Ej: "Eres el asistente virtual de [Startup]. Tu objetivo es responder dudas sobre nuestros precios y agendar reuniones. Tu tono es amigable pero profesional. Si no sabes algo, pide el contacto para que un humano escriba").
2.  **Carga de Conocimiento:** Subir el PDF o documento de texto que trajeron en el Pre-Work (el catálogo o las FAQs).
3.  **Configuración:** Ponerle nombre, foto y guardarlo.
4.  **El Test:** Hacerle 3 preguntas trampa (ej. una pregunta que no esté en el PDF) para ver cómo responde y ajustar en el momento.

---

### 🎁 5. Recursos para Llevar a Casa (El "Goody Bag" Digital)

Crea un enlace (usando Notion, Google Drive o una web sencilla) y ponlo en un código QR en la última diapositiva. Debe incluir:

1.  **La "Chuleta" del Prompt Perfecto:** Un PDF de 1 página con la estructura exacta para crear instrucciones para IA (Rol + Contexto + Tarea + Formato + Restricciones).
2.  **Biblioteca de Prompts para Startups:** 10 prompts listos para copiar y pegar (Redacción de copies para Instagram, Email de seguimiento a clientes fríos, Análisis de competencia, etc.).
3.  **Mapa de Herramientas No-Code:** Un directorio visual con las mejores herramientas de IA para conectar a WhatsApp, automatizar emails y crear flujos de ventas (con sus precios).
4.  **Certificado Digital:** Un diploma de "Implementador de IA Nivel 1" (en LATAM a los emprendedores les encanta compartir esto en LinkedIn).
5.  **Acceso a Comunidad:** Un grupo de WhatsApp o Discord exclusivo para los asistentes del workshop para que sigan compartiendo sus avances y dudas.

**Consejo de Facilitador:** Durante el Bloque 3 (el ejercicio), pon un cronómetro gigante en la pantalla. La presión de tiempo sana hace que la gente se enfoque y evita que se pierdan en detalles irrelevantes. ¡Mucha energía y a romperla!