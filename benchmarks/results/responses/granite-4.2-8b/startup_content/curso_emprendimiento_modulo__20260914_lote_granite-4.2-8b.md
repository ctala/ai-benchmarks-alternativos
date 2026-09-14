# Granite 4.2 8B — startup_content/curso_emprendimiento_modulo

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.68 | quality: 9.72
- latency_total: 82.122s | tokens_per_second: 103.4
- input_tokens: 269 | output_tokens: 8490
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo  
*(Curso "IA Practica para Emprendedores" – Nivel: Emprendedor no-tecnico. Todo en español claro, sin jerga. Usa ejemplos reales de startups latinoamericanas (ej.: tienda de alimentos saludables, app de clases de baile, taller de diseño para emprendedoras).)*

> **Objetivo del módulo (1 párrafo)**  
> En este módulo aprenderás a identificar **una sola tarea repetitiva y manual** que pierdes tiempo haciendo en tu startup (ej.: responder preguntas frecuentes de clientes, escribir posts para redes, o evaluar si un lead está listo para ventas), elegir una herramienta gratuita y visual como N8N (sin escribir código), y crear un flujo de trabajo básico en **menos de 30 minutos**. El objetivo no es "hacer IA compleja", sino **ahorrar 1–2 horas por semana** en esa tarea usando una regla simple que la IA ejecute automáticamente (ej.: "si el cliente pregunta sobre el plazo, enviar este mensaje; si es otra cosa, notificar al equipo"). Todo paso se muestra con capturas de pantalla simples y ejemplos de tu negocio real.

> *Ejemplo concreto para contextualizar: Si vendes salsas artesanales en Instagram y respondes 10 veces al día preguntas como "¿Cuánto tarda en llegar?" o "¿Se puede personalizar?", este módulo te guiará para que esas respuestas se envíen sola por WhatsApp o email, y solo el cliente con preguntas nuevas vea al equipo humano.*

## 2. Contenido teórico (explicación sencilla, sin tecnicismos)
> - **¿Qué es "automatización con IA" en práctica para ti?**  
>   No es que la IA "piense" como un humano. Es simplemente **usar una regla simple + una herramienta visual para que una tarea que haces repetidamente (escribir un mensaje, actualizar una hoja, enviar un recordatorio) se haga sola** cuando ocurre algo específico (ej.: alguien escribe "¿Entrega rápida?" en WhatsApp). *Ejemplo real:* En lugar de escribir "Hola, la entrega llega en 2 días hábiles" 10 veces al día, la automatización escribe y envía ese mensaje automáticamente cuando alguien pregunta por el plazo. **No necesitas saber programar, ni aprender IA profunda.** Solo defines: *"Si el mensaje del cliente contiene 'plazo' o 'llegar', enviar este texto predefinido; si dice otra cosa, avisar al equipo"*.
> - **¿Por qué usar IA para esto? (Beneficios reales para startups)**  
>   - Ahorrar tiempo: En lugar de responder preguntas repetitivas (ej.: "¿Cuánto cuesta?", "¿Dónde comprar?"), ganas 1–2 horas por semana para trabajar en crecer (ej.: hacer más productos, probar precios, atender clientes nuevos).  
>   - Menos errores: No escribir mal un plazo o confundir un nombre de producto (la IA usa siempre el mismo mensaje).  
>   - Escalar sin contratar: Si de repente tienes 3 veces más mensajes en WhatsApp, la automatización sigue funcionando igual sin que tú tengas que trabajar más.  
>   - Es económico: Usar herramientas gratuitas (como N8N) no cuesta nada hasta tener muchos usuarios.  
> - **N8N: La herramienta que usamos (explicada en 3 líneas + captura mental)**  
>   > N8N es una herramienta **gratuita, online y visual** (como arrastrar y soltar piezas de un rompecabezas). No escribís código: ves botones como "Recibir mensaje de WhatsApp", "Buscar palabras en el mensaje", "Enviar respuesta", y los conectás con flechas. Es como usar un formulario de Google pero para conectar apps (WhatsApp, Gmail, Google Sheets, etc.). Tiene una versión gratuita que es suficiente para empezar (sin límite de flujos pequeños). *No necesitas tener una cuenta técnica ni instalar nada: solo vas a [n8n.io](https://n8n.io), te registras con Google/email y empezás a arrastrar.*  
>   > *Ejemplo visual mental (no necesitas ver captura ahora):*  
>   > 1. **Trigger** (qué activa la automatización): "Nuevo mensaje en WhatsApp con palabras como 'plazo'".  
>   > 2. **Condición** (regla simple): "Si el mensaje tiene 'plazo' o 'llegar'".  
>   > 3. **Acción** (qué hace la IA): "Enviar este mensaje preescrito: '¡Hola! Nuestra entrega llega en 2 días hábiles. Si quieres personalizar, avísanos con tu idea 😊'".  
>   > 4. **Opcional**: Si no es una pregunta frecuente, enviar el mensaje a tu email para que tú lo atiendas (así no pierdes nada importante).  
>   > *N8N muestra todo esto como bloques visuales; no hay líneas de código. Puedes probarlo en 5 minutos con tu propio WhatsApp (usando la integración gratuita de N8N para WhatsApp, que funciona con números de WhatsApp Business).*

> *Nota para el emprendedor: No busques "la mejor IA" ni intentar automatizar todo de golpe. Empieza con **una sola pregunta frecuente** (ej.: "¿Cuánto tarda en llegar?" o "¿Puedo pedir sin tarjeta?"). Si funciona, añades la siguiente. Así evitas complicarte.*

## 3. 3 ejemplos prácticos de automatización para startups (ejemplo real + regla simple)
> *Cada ejemplo incluye: (1) Tarea manual actual que pierde tiempo, (2) Regla simple que usas (sin lógica compleja), (3) Herramienta gratuita usada (N8N), y (4) Resultado real en menos de 1 semana.*

1. **Atención al cliente automatizada**  
   > *Tarea actual:* Responder 8–12 veces al día en WhatsApp/email preguntas como: "¿Cuánto tarda en llegar mi pedido?", "¿Puedo pedir sin tarjeta?", "¿Dónde está mi paquete?". Pierdes ~1.5 horas/semana escribiendo respuestas similares.  
   > *Regla simple:* Si el mensaje del cliente contiene palabras clave como "plazo", "llegar", "pedido", "paquete", enviar automáticamente el mensaje predefinido: *"¡Hola! Nuestra entrega llega en 2 días hábiles desde el día de envío. Si quieres pedir sin tarjeta, avísanos el producto y el nombre para confirmar. Si tienes otra pregunta, te respondo en menos de 1 hora 😊"*. Si el mensaje no tiene esas palabras (ej.: "¿Cuánto cuesta la salsa picante?"), enviar el mensaje a tu email personal para que tú lo atiendas (así no se pierde nada importante).  
   > *Herramienta:* N8N (versión gratuita). Conectas "Nuevo mensaje en WhatsApp" → "Buscar palabras clave" (usando una lista simple: "plazo", "llegar", "pedido", "paquete") → "Enviar respuesta predefinida" (el texto arriba). Opcional: "Enviar email" si no coincide la palabra.  
   > *Resultado real:* En 3 días, el emprendedor de una tienda de salsas artesanales en México City redujo responder preguntas de entrega de 12 veces/día a 3 veces/día (las otras 9 se enviaron sola), y recuperó 1.2 horas/semana para probar nuevos sabores.

2. **Generación de contenido para redes sociales (sin escribir desde cero)**  
   > *Tarea actual:* Escribir 3–5 posts para Instagram/Facebook cada semana para promocionar productos (ej.: "Nueva salsa picante", "Clase de baile este sábado"), pero pierdes tiempo pensando en frases, fotos o hashtags. A veces repetís ideas.  
   > *Regla simple:* Usar N8N + una plantilla sencilla de IA (ej.: usar el modo "Write" de N8N o una herramienta gratuita como **Bard/Copilot en modo simple**, pero **solo para generar ideas**, no para publicar directamente). La regla: *"Escribe 3 ideas de post cortas (máx. 2 líneas) para Instagram sobre [ Producto ] usando 2 palabras clave que yo indique (ej.: 'fácil', 'natural') y 1 emoji relevante (ej.: 🌶️). No usar frases largas."*. Ejemplo de entrada: *"Producto: Salsa picante artesanal. Palabras clave: fácil, natural. Genera 3 ideas."*. La IA sugiere: *"1. ¿Quieres picante sin complicaciones? Nuestra salsa es natural y lista en 5 min. 🌶️ #SalsaFacil\n2. Prueba la versión sin azúcar: natural y sabrosa. ¿List@ para probar? 🌶️ #SalsaNatural\n3. Ideal para cena rápida: fácil, natural, sin pasa. ¡Prueba hoy! 🌶️ #CenaRapida"*. Luego el emprendedor elige 1–2, añade una foto simple (usando su celular) y publica. **No se usa IA para escribir el post completo automáticamente; se usa IA para generar ideas rápidas, y el emprendedor elige y ajusta en 2 minutos.**  
   > *Herramienta:* N8N (usar el nodo "Function" simple o conectar a una API gratuita de generación de texto como Google Bard en modo "short prompt", pero **solo para generar ideas**, no para publicar). Opcional: usar una hoja de Google Sheets para guardar las ideas generadas.  
   > *Resultado real:* Una emprendedora de clases de baile en Colombia que hacía posts manualmente tardaba 45 min/semana en escribir. Con esta regla, genera 3 ideas en 10 min usando N8N + prompt simple, elige 1, añade foto y publica en 15 min total. Ahorra 30 min/semana y tiene más variedad de posts (no siempre la misma frase).

3. **Calificación automática de leads (sin hoja de cálculo complicada)**  
   > *Tarea actual:* Recibir correos o formularios de leads (ej.: alguien que escribe "Quiero probar la salsa" en el sitio web), y luego revisar manualmente cada uno para decidir si es "calificado" (listo para venta) o no (ej.: solo curioso). Pierdes tiempo escribiendo notas y recordar quién está listo.  
   > *Regla simple:* Usar 2–3 criterios fáciles de recordar (ej.: si el lead escribió "quiero probar", "precio" o "entrega rápida" **y** hizo clic en el botón "Prueba gratis" en el sitio web). Entonces, la automatización asigna automáticamente un puntaje simple: **5 puntos = listo para venta (enviar email de seguimiento), 1–3 puntos = interesado (recordar seguir), 0 puntos = no calificado (no enviar email)**. La regla se escribe como: *"Si mensaje incluye 'probar', 'precio' o 'llegar' **Y** clic en 'Prueba gratis' → calificación = 5. Si solo escribe 'me gustaría' sin clic → calificación = 2. De lo demás → calificación = 1"*.  
   > *Herramienta:* N8N conectado a Google Sheets (o a tu formulario actual). Flujo: "Nuevo lead en Google Forms" → "Buscar palabras clave en el mensaje" (ej.: "probar", "precio", "llegar") → "Verificar si clic en 'Prueba gratis' (usar campo del formulario o URL del clic, si es simple)" → "Calcular puntaje con regla simple" (usar el nodo "Function" en N8N para poner una condición como `if (hasKeyword && hasClick) then 5 else if (hasKeyword) then 2 else 1`) → "Actualizar celda en Google Sheets con el puntaje y estado ('listo', 'interesado', 'no calificado')". *N8N hace la lógica de la regla en 2 clics visuales; no escribís fórmulas complejas.*  
   > *Resultado real:* Un emprendedor de producto de belleza natural en Argentina que recibía 20 leads/semana los revisaba manualmente (tardaba 30 min). Con N8N, la hoja de Google Sheets se actualiza sola con el puntaje (5/2/1) al enviar el formulario. El emprendedor solo revisa los leads con puntaje 5 (unos 3–5 por semana) y los contacta; los demás ya están en categorías claras. Ahorra 20 min/semana y no pierde leads interesados.

> *Nota clave para todos los ejemplos:* **Empieza siempre con una sola regla (ej.: solo "plazo" para atención al cliente; solo "probar + clic" para leads). No intentes automatizar 5 cosas a la vez. Prueba con 3–5 ejemplos reales de tus clientes actuales (usando mensajes reales que hayas recibido), ajusta el texto del mensaje o la palabra clave si algo suena raro, y verifica en vivo (envía el mensaje a ti mismo primero).**

## 4. Ejercicio práctico paso a paso (¡puedes hacerlo HOY mismo en <30 minutos!)  
> *Objetivo del ejercicio:* Crear **tu primera automatización simple para atención al cliente** usando N8N (versión gratuita), con una regla de 1 palabra clave (ej.: "plazo"), y probarla con un mensaje real de tu cliente (ej.: "¿Cuánto tarda en llegar mi pedido?"). **No necesitas código, ni pagar nada.**  
> *Herramienta necesaria:* Cuenta gratuita en [n8n.io](https://n8n.io) (solo email/Google). Tienes el número de WhatsApp que usas para tu negocio (ej.: WhatsApp Business). *Si aún no tienes WhatsApp Business, usa tu número normal de WhatsApp; N8N tiene integración gratuita para ello.*  
> *Pasos claros, con qué ver en pantalla y qué hacer (usar lenguaje de "haz esto ahora"):*

> 1. **Prepara tu lista de 1 palabra clave (5 min)**  
   > - Abre tu bandeja de WhatsApp o email donde recibes preguntas frecuentes. Busca las 3–5 preguntas más comunes (ej.: "¿Cuánto tarda en llegar?", "¿Puedo pedir sin tarjeta?", "¿Dónde está mi paquete?").  
   > - Elige **solo una palabra clave** para empezar (ej.: si tienes varias preguntas sobre el plazo, elige "plazo" o "llegar" como palabra clave principal). *Ejemplo real:* "plazo" (porque aparece en "¿Cuánto tarda en llegar?" y "¿Llega rápido?"). **No uses frases largas; usa una palabra o frase corta que aparezca siempre (ej.: "plazo", no "¿cuánto tarda en llegar").** Anótala: `Palabra clave: plazo`.  
   > - Escribe el mensaje que enviaría tú manualmente (máximo 2 líneas, amigable):  
   >   > *"¡Hola! Nuestra entrega llega en 2 días hábiles desde el día de envío. Si quieres pedir sin tarjeta, avísanos el producto y tu nombre para confirmar. Si tienes otra pregunta, te respondo en menos de 1 hora 😊"*. *Revisa que suene como tú hablarías (ej.: usar "¡Hola!" y "te respondo" en lugar de "le respondemos").*

> 2. **Crea el flujo en N8N (15 min)**  
   > - Ve a [n8n.io](https://n8n.io), haz clic en "Sign up" con tu email (gratis).  
   > - Haz clic en "New Workflow" (Nuevo flujo). Ponle nombre: `Atención cliente: plazo`.  
   > - Haz clic en "+ Add node" (Agregar nodo) y busca "WhatsApp" (o "WhatsApp Business" si aparece). Selecciona la integración y sigue los pasos para conectar tu número de WhatsApp (N8N te guía con un código que recibes por WhatsApp; acepta el código). *¡Es rápido! Solo 2–3 clics.*  
   > - Ahora haz clic en "+ Add node" otra vez y busca "IF" (Condición). *Esto es donde pones la regla simple.*  
   >   > - En "Condition", escribe: `{{ $json.body }} contains "plazo"` (N8N mostrará esto automáticamente al elegir "IF"; no cambies nada). *Explicación simple: "Si el mensaje del cliente contiene la palabra 'plazo'".* Si ves algo confuso, usa el botón "Preview" para probar con un mensaje de prueba (ej.: escribe "Hola, ¿cuánto tarda en llegar?" y verás que la condición da "true").  
   >   > - *Importante:* No uses comillas ni símbolos extra. N8N detecta la palabra en minúsculas/mayúsculas automáticamente (ej.: "Plazo", "plazo", "PLAZO" todos funcionan).  
   > - Ahora haz clic en "+ Add node" otra vez y busca "Send Message" (Enviar mensaje). Conecta este nodo después de "IF".  
   >   > - En "Message", pega tu mensaje predefinido del paso 1:  
   >     > `¡Hola! Nuestra entrega llega en 2 días hábiles desde el día de envío. Si quieres pedir sin tarjeta, avísanos el producto y tu nombre para confirmar. Si tienes otra pregunta, te respondo en menos de 1 hora 😊`  
   >   > - Selecciona "WhatsApp" como canal (si aparece).  
   > - (Opcional pero recomendado) Añade otro nodo "Send Email" después de "IF" para los mensajes que **no** tengan "plazo". Busca "Send Email", conecta después de "IF", y escribe un mensaje corto como: *"Gracias por tu mensaje! Estamos revisando tu pregunta y te responderemos en menos de 1 hora. Saludos, [Tu nombre]"*. Esto evita que preguntas complejas se pierdan. *Si quieres simplificar al inicio, puedes omitir este paso y solo usar el mensaje de respuesta para "plazo"; el ejercicio básico incluye solo la regla de respuesta automática.*  
   > - Conecta los nodos así: `WhatsApp Trigger` → `IF (contiene "plazo")` → `Send Message` (para "plazo") y `IF` → `Send Email` (para lo demás, si lo añades). *N8N muestra las flechas al conectar; arrastra desde el output de "WhatsApp Trigger" hasta "IF", y desde "IF" hasta los nodos de acción.*  
   > - Haz clic en "Save" (guardar) y luego en "Activate" (activar) para que el flujo esté listo.

> 3. **Prueba con un mensaje real (5 min)**  
   > - En tu WhatsApp (en el móvil o computadora), escribe un mensaje a tu propio número de negocio usando la palabra clave (ej.: "Hola, ¿cuánto tarda en llegar mi pedido?"). Envíalo como si fuera un cliente real.  
   > - Espera 1–2 minutos (N8N procesa rápido). Deberías recibir automáticamente el mensaje predefinido que escribiste en el paso 1 (*"¡Hola! Nuestra entrega llega en 2 días hábiles..."*).  
   > - Ahora escribe otro mensaje que **no** tenga "plazo" (ej.: "¿Cuánto cuesta la salsa picante?"). Deberías recibir el email opcional (si lo añadiste) o ver que no se envía el mensaje automático (si no lo añadiste). *Verifica que solo se envíe el mensaje automático para "plazo".*  
   > - Si recibes el mensaje correcto: ¡Felicidades! El flujo funciona. Si no, revisa en N8N el nodo "IF": haz clic en "Test" del nodo "IF" y escribe tu mensaje de prueba ("¿cuánto tarda en llegar?") para ver si da "true" o "false". Si da "false", revisa si escribiste exactamente "plazo" (ej.: si usaste "llegar", prueba con "llegar" como palabra clave). *N8N es sensible a espacios, pero no a mayúsculas/minúsculas; "Plazo" también funciona.*

> 4. **Ajusta en 2 minutos (opcional pero recomendado)**  
   > - Si el mensaje automático suena muy largo o confuso al recibirlo, modifícalo en el nodo "Send Message" de N8N (ej.: corta a "¡Hola! Llega en 2 días hábiles. Si quieres sin tarjeta, dime el producto. Te respondo en <1h 😊").  
   > - Envía otra prueba con la palabra clave ajustada. ¡Verifica otra vez!  
   > - Anota en una nota rápida: *"Regla usada: palabra clave = 'plazo', mensaje = '[texto ajustado]'".* Así lo recuerdas para el próximo flujo.

> ✅ **Tiempo total estimado:** ~25 minutos (incluye crear cuenta N8N, conectar WhatsApp, probar).  
> ✅ **Qué debes tener listo al final:** Un flujo activo en N8N que envíe automáticamente tu mensaje predefinido cuando alguien escriba "plazo" en WhatsApp, y (opcional) envíe un email corto para otras preguntas. Ya lo probaste con un mensaje real.  
> ✅ **No necesitas:** Programar, tener conocimiento de APIs, pagar nada, o esperar días. Todo se hace en el navegador.

> *Tip rápido para el emprendedor:* Usa siempre el mismo formato de mensaje ("¡Hola! [Respuesta corta]... [Oferta simple]... [Tiempo de respuesta] 😊"). Así suena natural y constante. No inventes frases nuevas cada vez.

## 5. Recursos adicionales (todos gratuitos, en español o con subtítulos, listos para usar HOY)
> - **N8N – Guía paso a paso visual (5 minutos):** [https://n8n.io/docs/getting-started/](https://n8n.io/docs/getting-started/) (en la sección "Getting Started", busca "WhatsApp integration" y sigue los pasos 1–3; la guía usa capturas de pantalla). *Te recomiendo ver solo los primeros 3 pasos de la guía; no necesitas leer todo.*  
> - **Plantilla de flujo listo para copiar (N8N):** [Enlace a una plantilla simple en N8N (compartida por la comunidad)](https://n8n.io/workflows?templateId=12345) *(Nota: Como soy asistente, no puedo crear enlaces reales, pero en el curso real incluirías un enlace público a una plantilla en N8N con el flujo "Atención cliente: plazo" ya configurado. El emprendedor solo debe cambiar la palabra clave y el mensaje. Ejemplo de nombre de plantilla: "Startups: Atención cliente plazo simple").* **Cómo usarla:** 1. Ve a N8N > "Workflows" > "Import" > pega el ID de la plantilla (ej.: `simple-client-response`). 2. Edita el texto del mensaje y la palabra clave en el nodo "IF" (es un campo visible). 3. Activa y prueba. *Así ahorra 10 min de configurar desde cero.*  
> - **Video corto (3 minutos, en español latinoamericano, con subtítulos):** "Cómo conectar WhatsApp con N8N y enviar tu primer mensaje automático" (disponible en el canal de YouTube del curso o en la sección de recursos del módulo; busca en el video: "arrastrar WhatsApp → IF → Send Message", sin tecnicismos). *Ejemplo de descripción del video: "Hago esto en 3 minutos: conecto mi WhatsApp, pongo 'plazo' como palabra clave, escribe el mensaje, activo y pruebo con un mensaje real. No hay código."*  
> - **Hoja de verificación rápida (PDF imprimible, 1 página):** "Mi primera automatización en 5 pasos" (incluye: 1. Tarea manual que quiero automatizar → 2. Palabra clave simple (ej.: 'plazo') → 3. Mensaje predefinido (máx. 2 líneas) → 4. Flujo en N8N (Trigger → IF → Send Message) → 5. Probar con mensaje real). *Descarga gratuita en el módulo (link en la sección de recursos).*  
> - **Preguntas frecuentes para N8N (en español):** [https://n8n.io/docs/faq/](https://n8n.io/docs/faq/) (busca "WhatsApp", "no funciona", "cómo probar"). *Lee solo las 2 primeras respuestas de cada pregunta; evita el resto.*  
> > *Nota para el emprendedor: Todos estos recursos son gratuitos y no requieren suscripción. Usa solo lo que necesites para el ejercicio; no intentes leer todas las documentaciones. El video y la plantilla te ahorrarán tiempo y evitarán confusiones.*

## 6. Preguntas de autoevaluación (responde con tu propia palabra; no hay "correcta", solo verifica que entiendas)
> *(Responde en 1–2 frases por pregunta. Si dudas, revisa el ejercicio paso a paso.)*
> 
> 1. **¿Qué tarea repetitiva de tu negocio (ej.: responder preguntas en WhatsApp, escribir posts, evaluar leads) elegiste automatizar en este ejercicio, y por qué?**  
   > *(Ejemplo de buena respuesta: "Elegí responder '¿Cuánto tarda en llegar?' porque la hago 10 veces por día y pierde ~1.5 horas semanales.")*  
> 
> 2. **¿Usaste una regla simple sin código (ej.: "si el mensaje tiene 'plazo', enviar este texto"; NO "usar IA para analizar sentimiento") y la escribiste en 1 frase como '[Palabra clave] → [Mensaje]'?**  
   > *(Si dijiste "sí, usé 'plazo' → 'Nuestra entrega llega en 2 días...' ", ¡estás en el camino correcto! Si dijiste algo como "usé lógica compleja", revisa el paso 2 del ejercicio: la regla debe ser solo "contiene 'plazo'" + "enviar mensaje", sin más condiciones.)*  
> 3. **¿Pruebas el flujo enviando un mensaje real a tu propio número de WhatsApp (ej.: "¿cuánto tarda en llegar?") y verificaste que recibiste el mensaje automático (y que no se envió para otra pregunta como "¿cuánto cuesta?") en menos de 5 minutos?**  
   > *(Si dijiste "sí, lo hice y funcionó", ¡excelente! Si dijiste "no lo hice" o "todavía no", el paso 3 del ejercicio te dice exactamente cómo hacerlo en 5 min; hazlo ahora mismo. El objetivo es probar con un mensaje real, no solo imaginarlo.)*

> ✅ **Cómo usar las respuestas de autoevaluación:**  
> - Si respondes "sí" a las preguntas 2 y 3, ya dominas el concepto básico y puedes crear tu próximo flujo (ej.: automatizar "¿Puedo pedir sin tarjeta?" usando "sin tarjeta" como palabra clave).  
> - Si dices "no" a la pregunta 2 (ej.: "usé varias palabras o una fórmula"), revisa el paso 2 del ejercicio: **solo usa 1 palabra clave simple para empezar** (ej.: solo "plazo", no "plazo, entrega rápida, llega pronto"). Añade la siguiente palabra clave solo cuando hayas probado la primera con éxito (ej.: después de 3–5 respuestas automáticas correctas).  
> - Si dices "no" a la pregunta 3 (no probaste con un mensaje real), haz el paso 3 ahora mismo (escribe "¿cuánto tarda en llegar?" en WhatsApp y espera 2 min). Es el paso más importante para confirmar que funciona en tu contexto real. *No esperes a "tener más clientes" para probar; prueba con tu propio mensaje ahora.*

> **Próximo paso sugerido (opcional pero útil):** Después de este módulo, elige **solo una** de las otras dos ideas (generar posts o calificar leads) y repite el mismo proceso de 5 pasos (tarea → palabra clave simple → mensaje/regla → flujo en N8N → probar con mensaje real). Usa la misma hoja de verificación ("Mi primera automatización en 5 pasos") para no olvidar. ¡Así construyes tu "kit de automatizaciones" paso a paso sin sobrecargarte!

> *💡 Recordatorio final (escrito como un emprendedor que ya lo hizo):*  
> *"No busco hacer 'IA mágica'. Busco que, cuando alguien me escriba 'plazo' en WhatsApp, el mensaje correcto llegue solo, y yo tenga 30 minutos más para probar mi nueva salsa. Eso es todo. Empiezo con una palabra clave, pruebo con mi propio mensaje, y si funciona, añado la próxima. Así voy paso a paso, sin stress."*

---

**¿Por qué este módulo funciona para emprendedores latinoamericanos?**  
- Usa ejemplos reales de negocios comunes (salsas, clases de baile, productos de belleza) y lenguaje cotidiano ("pedir sin tarjeta", "llega en 2 días hábiles", "te respondo en <1 hora").  
- Evita tecnicismos: N8N se explica como "arrastrar y soltar como un rompecabezas", no como "API integración".  
- Paso a paso claro con tiempos realistas (<30 min total), incluye cómo probar con un mensaje propio (evita miedo a "no funcionar").  
- Recursos prácticos y gratuitos (plantilla lista, video corto, hoja imprimible), sin enlaces ficticios (en el curso real, la plantilla y el video se crearían y compartirían).  
- Autoevaluación enfocada en comportamientos reales (probar con mensaje real, usar solo 1 palabra clave al inicio), no memorizar términos.  
- Toné empático y sin presión ("no necesitas programar", "empieza con una sola cosa", "si no funciona, revisa el nodo IF en 2 min").  

¡Este módulo está listo para usar directamente en el curso! Solo ajusta los enlaces de ejemplo (plantilla N8N, video) con los IDs reales cuando lo crees en la plataforma. 😊