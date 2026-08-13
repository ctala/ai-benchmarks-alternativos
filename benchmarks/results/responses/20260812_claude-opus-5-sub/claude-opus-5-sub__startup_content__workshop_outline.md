# Claude Opus 5 (suscripción) — startup_content/workshop_outline

- model_id: `claude-opus-5`
- success: True  | final: 7.74 | quality: 10.0
- latency_total: 211.167s | tokens_per_second: 64.6
- input_tokens: 2 | output_tokens: 13640
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el taller.

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

# Construye tu Asistente de IA para tu Startup
### Workshop presencial · 3 horas · 20-30 emprendedores early-stage no técnicos

---

## La promesa (dila así al abrir y repítela al cerrar)

> "Nadie se va de acá con un PDF de teoría. Te vas con **un asistente funcionando** que hace **una tarea real** de tu negocio, y con un plan de 7 días para que la siga haciendo sin ti."

**Regla de diseño de todo el workshop:** cada minuto de charla tiene que pagar un minuto de construcción. Ratio objetivo: **35% exposición / 55% manos a la obra / 10% logística**.

---

## 1. Agenda detallada (180 minutos)

| # | Bloque | Min | Acumulado | Formato dominante |
|---|---|---|---|---|
| B0 | Bienvenida y el costo real de tu tiempo | 10 | 0:10 | Charla + shock |
| B1 | Inventario: dónde se te va la semana | 15 | 0:25 | Ejercicio individual + parejas |
| B2 | Qué es (y qué NO es) un asistente de IA | 20 | 0:45 | Charla + demo en vivo |
| B3 | El filtro: elegir la tarea correcta | 20 | 1:05 | Marco + ejercicio de puntaje |
| — | **PAUSA** | 10 | 1:15 | Café, baño, networking |
| B4 | **Construcción 1: las instrucciones** | 40 | 1:55 | Hands-on guiado |
| B5 | **Construcción 2: contexto, prueba, iteración** | 30 | 2:25 | Hands-on + testing |
| B6 | Que trabaje sin ti (y dónde se rompe) | 12 | 2:37 | Demo del facilitador |
| B7 | Vitrina: 5 asistentes en vivo | 15 | 2:52 | Presentaciones relámpago |
| B8 | Cierre, compromiso de 7 días y recursos | 8 | 3:00 | Charla + entrega |

**Total: 180 minutos.** Los bloques B4 y B5 son intocables: si algo se atrasa, se recorta B2 y B6, nunca la construcción.

---

## 2. Materiales necesarios (qué preparar antes)

### 2.1 Con 7 días de anticipación

**Email de pre-requisitos a los inscritos** (asunto: "Lo que necesitas traer el jueves — 4 minutos de preparación")

1. **Notebook cargado.** Celular no sirve para construir, solo para probar. Sin notebook no se puede participar del ejercicio principal.
2. **Cuenta creada y con sesión iniciada** en la herramienta elegida (ver 2.4). Que la creen desde la casa, no en la sala.
3. **Tres archivos de su negocio** en una carpeta: puede ser su lista de precios, sus preguntas frecuentes, un documento de propuesta, su tono de comunicación, ejemplos de respuestas que ya dieron a clientes. Formato libre (PDF, Doc, texto pegado).
4. **Tres ejemplos reales** de la tarea que quieren automatizar: tres correos reales que respondieron, tres cotizaciones que hicieron, tres publicaciones que escribieron.

> El punto 4 es el que más gente olvida y el que más determina si su asistente sirve. Insiste con recordatorio a las 24 horas.

### 2.2 Sala y logística

| Ítem | Detalle | Por qué |
|---|---|---|
| Distribución | Mesas de 4-5 personas, no filas de auditorio | El ejercicio principal se apoya en el vecino |
| Enchufes | 1 tomacorriente por cada 2 personas + 4 zapatillas de repuesto | 3 horas agotan baterías de notebooks viejos |
| WiFi | Red probada con 30 dispositivos simultáneos. Clave impresa en cada mesa | El WiFi caído mata el workshop entero |
| Plan B de conectividad | Hotspot 4G del facilitador + 2 asistentes | Cubre a 6-8 personas si la red del lugar falla |
| Proyector | Probado con el notebook del facilitador 30 min antes | Adaptadores HDMI/USB-C propios, nunca los del lugar |
| Timer visible | Cronómetro proyectado o reloj grande durante los ejercicios | Presión sana, evita que se estiren |
| Café y agua | Disponible desde el inicio, no solo en la pausa | 3 horas de tarde son largas |

### 2.3 Materiales impresos (1 por persona)

1. **Hoja de Inventario de Tareas** (B1) — tabla de 6 filas: tarea / frecuencia semanal / minutos por vez / cuánto me molesta (1-5).
2. **Tarjeta del Filtro de Tarea** (B3) — la matriz de 4 criterios en tamaño tarjeta, plastificada si el presupuesto lo permite.
3. **Plantilla de Instrucciones** (B4) — la estructura de 7 campos en una plana, con espacio para escribir a mano antes de tipear.
4. **Checklist de Prueba** (B5) — el protocolo de semáforo con espacio para 3 casos.
5. **Hoja de Compromiso de 7 Días** (B8) — se llena y se fotografía en la sala.

Total: **5 hojas por persona.** Imprime 35 sets para 25 inscritos.

### 2.4 Decisión de herramienta (resuélvela 48 horas antes)

El error clásico: el facilitador usa una herramienta de pago y la mitad de la sala choca con un muro de suscripción a los 20 minutos de construir.

**Criterio:** la herramienta principal tiene que permitir **crear un asistente con instrucciones y archivos de contexto en el plan gratuito**.

- **Opción principal recomendada:** un creador de asistentes personalizados con capa gratuita (tipo Gemini Gems), porque casi todos ya tienen cuenta de Google y no requiere tarjeta.
- **Alternativas para quien ya paga:** Proyectos de ChatGPT o Proyectos de Claude. Funcionan igual de bien y la plantilla de instrucciones es idéntica.

**Acción obligatoria del facilitador:** verifica los límites del plan gratuito **48 horas antes del evento**. Los planes de estas herramientas cambian cada pocos meses y una guía desactualizada te quema la sala en vivo. Ten un plan B: si la herramienta principal muere, el ejercicio se hace igual pegando las instrucciones en una conversación normal — el aprendizaje es el mismo, solo pierdes la persistencia.

### 2.5 Kit del facilitador

- **Asistentes de sala: 1 por cada 10 participantes.** Con 25 personas necesitas 2 ayudantes, mínimo. Durante B4 y B5 la mano levantada tiene que atenderse en menos de 60 segundos o la persona se desconecta.
- **Un asistente de ejemplo ya construido** para tu propio negocio, listo para demostrar en 90 segundos.
- **Un asistente MAL construido**, a propósito, para la demo comparativa de B2.
- **Tres casos de prueba universales** para quien llegue sin sus ejemplos.
- **Un negocio ficticio de respaldo** ("Panadería con delivery, 4 empleados, vende por WhatsApp") para quien no tenga claro su propio caso.
- **Automatización lista para demo** en B6: un flujo simple donde llega un mensaje y el asistente responde solo.

---

## 3. Detalle bloque por bloque

---

### B0 · Bienvenida y el costo real de tu tiempo
**10 minutos · 4 slides**

**Objetivo:** que cada persona ponga un número en pesos a las horas que pierde por semana, y que ese número duela lo suficiente para sostener 3 horas de atención.

**Dinámica:** charla corta con una cuenta hecha en vivo.

Abre sin presentarte. Primera pregunta a la sala: *"Levanta la mano si esta semana hiciste algo por tercera vez que ya sabías cómo hacer."* Casi todos levantan la mano.

Haz la cuenta en el pizarrón con un voluntario: horas repetitivas por semana × 4 semanas × lo que vale su hora. El número típico de un fundador early-stage está entre 30 y 60 horas al mes. Escríbelo grande.

Después, las reglas de la sala en 30 segundos:
- Notebook abierto solo cuando yo lo diga. En los bloques de charla, cerrado.
- Si te trabas más de 2 minutos, levantas la mano. No sufras en silencio.
- Nadie se va sin algo que funcione.

**Key takeaway:** *"No estás acá para aprender IA. Estás acá para recuperar entre 20 y 40 horas al mes."*

---

### B1 · Inventario: dónde se te va la semana
**15 minutos · 3 slides**

**Objetivo:** generar la materia prima del workshop. Sin este bloque, la gente construye asistentes genéricos e inútiles.

**Dinámica:**
- **Minutos 0-7 — individual, en silencio.** Cada uno llena la Hoja de Inventario: 6 tareas que hizo esta semana y que va a volver a hacer la próxima. Con frecuencia, minutos y nivel de molestia. Silencio real, música de fondo si ayuda.
- **Minutos 7-13 — en parejas.** Cada uno le explica su lista al vecino en 3 minutos. La instrucción es específica: *"Tu trabajo no es opinar. Tu trabajo es preguntar '¿por qué eso lo tienes que hacer tú?' hasta que se quede sin respuesta."*
- **Minutos 13-15 — plenario relámpago.** Tres personas dicen su tarea más pesada en voz alta. Anótalas en el pizarrón: van a servir de ejemplo el resto del taller.

**Nota de facilitación:** siempre hay 2-3 personas que escriben "vender" o "conseguir clientes". Redirígelas: no es una tarea, es un objetivo. Pídeles que desglosen los pasos concretos de esta semana.

**Key takeaway:** *"Lo que no puedes describir en una frase, no lo puedes delegar — ni a una persona ni a una máquina."*

---

### B2 · Qué es (y qué NO es) un asistente de IA
**20 minutos · 8 slides**

**Objetivo:** desarmar el misticismo y dejar un modelo mental de 4 piezas que van a usar el resto de la tarde.

**Dinámica:** 8 minutos de charla + 8 minutos de demo comparativa en vivo + 4 minutos de preguntas.

**Charla (8 min).** Un asistente de IA no es un chat. Un chat es un empleado nuevo al que le explicas todo desde cero cada mañana. Un asistente es ese mismo empleado, pero con el manual ya leído.

Las 4 piezas, y ninguna más:

| Pieza | En lenguaje de negocio | Ejemplo |
|---|---|---|
| **Instrucciones** | La descripción del cargo | "Eres quien responde cotizaciones de mi taller" |
| **Contexto** | El manual y los archivos de la empresa | Lista de precios, tiempos de entrega, garantías |
| **Formato de salida** | Cómo tiene que entregar el trabajo | "Correo de máximo 120 palabras, con precio y plazo" |
| **Reglas duras** | Lo que nunca debe hacer | "Nunca inventes un precio. Si no está en la lista, avisa" |

**Demo comparativa (8 min).** Esta es la parte que hace clic. Proyecta y ejecuta en vivo, misma pregunta a dos asistentes:

- **El malo:** instrucción "eres un asistente útil para mi negocio". Resultado genérico, cordial, inservible, con datos inventados.
- **El bueno:** el mismo pedido, con las 4 piezas completas. Resultado usable tal cual.

Pausa después de mostrar los dos resultados lado a lado. Pregunta a la sala: *"¿Cuál es la diferencia entre estos dos? Porque el modelo de IA es exactamente el mismo."* Deja que ellos lo digan.

**Key takeaway:** *"La IA no es mágica ni tonta. Es literal. La calidad de la salida es la calidad de tus instrucciones."*

---

### B3 · El filtro: elegir la tarea correcta
**20 minutos · 5 slides**

**Objetivo:** que cada persona salga con **una sola tarea elegida** — no tres, no "varias ideas". Una.

**Dinámica:** 7 minutos de marco + 8 minutos de ejercicio individual + 5 minutos de validación en mesa.

**El marco (7 min).** Una tarea es buena candidata cuando cumple los 4 criterios:

1. **Se repite.** Mínimo 3 veces por semana. Automatizar algo mensual no te devuelve tiempo, te consume un sábado.
2. **Es de texto.** Escribir, resumir, clasificar, responder, traducir, estructurar. Si la tarea es negociar por teléfono o firmar, no es esto.
3. **Tú ya sabes cómo hacerla bien.** Si no puedes explicar el criterio, la IA tampoco lo va a adivinar. No delegues lo que no dominas.
4. **Un error no te hunde.** Un correo mal redactado se corrige. Un contrato mal revisado o un diagnóstico médico, no. Empieza donde el error es barato.

Muestra la lista de anti-ejemplos: "que me consiga clientes", "que maneje mis redes completas", "que decida mis precios". Son proyectos, no tareas.

**Ejercicio (8 min).** Con la Tarjeta del Filtro, cada uno puntúa sus 6 tareas del inventario de 1 a 5 en cada criterio. La de mayor puntaje total gana. Se escribe en grande arriba de la hoja: **MI TAREA ES: ______**.

**Validación (5 min).** En la mesa, cada uno lee su tarea elegida en voz alta y el resto responde una sola cosa: *"¿Eso es una tarea o es un deseo?"* La mesa tiene derecho a veto.

**Key takeaway:** *"El asistente que hace una cosa bien te sirve el lunes. El que hace diez cosas más o menos no lo vas a usar nunca."*

---

### PAUSA · 10 minutos

Mantén la sala abierta y quédate adentro: los mejores diagnósticos individuales pasan acá. Aprovecha para detectar quién todavía no tiene tarea elegida y asígnale un ayudante para el arranque de B4.

---

### B4 · Construcción 1: las instrucciones
**40 minutos · 6 slides · EJERCICIO PRINCIPAL, PARTE A**

**Objetivo:** que cada persona tenga escritas las instrucciones completas de su asistente y lo tenga creado en la herramienta.

**Dinámica:** hands-on guiado, campo por campo, con el facilitador construyendo su propio ejemplo en paralelo en la pantalla.

**Formato:** proyecta la plantilla, llena TU campo en vivo mientras ellos llenan el suyo, cronómetro visible por campo. Nunca avanzas al siguiente campo sin decir *"levanten la mano los que todavía están en el anterior"*.

| Min | Campo de la plantilla | Consigna en pantalla |
|---|---|---|
| 0-3 | Setup | Todos crean el asistente vacío y le ponen nombre |
| 3-8 | **1. Rol** | "Eres quien [tarea] para [tipo de negocio]" — una frase |
| 8-14 | **2. Contexto del negocio** | Qué vendes, a quién, qué te diferencia — 4 líneas |
| 14-20 | **3. La tarea exacta** | El paso a paso que TÚ haces hoy, numerado |
| 20-26 | **4. Formato de salida** | Extensión, estructura, tono, idioma |
| 26-32 | **5. Reglas duras** | 3 a 5 "nunca". Al menos una sobre inventar datos |
| 32-36 | **6. Qué hacer si falta información** | "Pregúntame en vez de asumir" |
| 36-40 | **7. Un ejemplo bueno** | Pegar UN caso real bien resuelto |

**El campo 7 es el de mayor retorno y el que más gente salta.** Insiste: un solo ejemplo real de una respuesta bien hecha mejora el resultado más que párrafos de instrucciones.

**Trabajo de los ayudantes:** circular permanentemente. Señales de alerta: alguien escribiendo párrafos larguísimos (redirigir a concreto), alguien con la pantalla en blanco a los 10 minutos (bloqueo, intervenir), alguien construyendo tres asistentes a la vez (frenar).

**Key takeaway:** *"Escribir las instrucciones es el trabajo. Lo demás es pegar y probar."*

---

### B5 · Construcción 2: contexto, prueba e iteración
**30 minutos · 4 slides · EJERCICIO PRINCIPAL, PARTE B**

**Objetivo:** que el asistente pase de "existe" a "sirve". Acá es donde el workshop se gana o se pierde.

**Dinámica:** tres rondas cronometradas.

**Ronda 1 — Cargar contexto (8 min).** Suben sus archivos del negocio al asistente. Máximo 3 archivos: más documentos no lo hacen más inteligente, lo hacen más confuso. Si alguien no trajo archivos, que escriba a mano los 10 datos clave de su negocio.

**Ronda 2 — Prueba con casos reales (12 min).** Acá se usan los tres ejemplos reales que trajeron. Protocolo del semáforo, con la Checklist de Prueba en mano:

| Color | Qué significa | Qué haces |
|---|---|---|
| **Verde** | Lo mando tal cual | Guarda ese resultado como ejemplo nuevo |
| **Amarillo** | Sirve pero lo tengo que editar | Anota QUÉ editaste. Eso es una regla que falta |
| **Rojo** | Inservible o inventó datos | Falta contexto o falta una regla dura |

La consigna clave: *"No arregles el resultado. Arregla la instrucción."* La gente tiende a corregir el texto de salida a mano, que es exactamente el trabajo que vinieron a eliminar.

**Ronda 3 — Iterar (10 min).** Cada amarillo y cada rojo se convierte en una línea nueva en las instrucciones. Vuelven a correr el mismo caso. **Meta mínima del workshop: 2 de 3 casos en verde.**

Al cierre del bloque, pide señal con la mano: *"Verde arriba si tu asistente pasó 2 de 3."* Cuenta en voz alta cuántas manos hay. Ese número es tu métrica de éxito del taller.

**Key takeaway:** *"Un asistente no se escribe, se entrena. Cada corrección que le haces hoy es una corrección que no haces mañana."*

---

### B6 · Que trabaje sin ti (y dónde se rompe)
**12 minutos · 6 slides**

**Objetivo:** mostrar el siguiente escalón sin que nadie intente subirlo hoy. Esto abre el apetito y define el camino de los próximos meses.

**Dinámica:** demo del facilitador, notebooks CERRADOS. Dilo explícitamente: *"Cierren los notebooks. Esto es para mirar, no para hacer."*

- **6 min — La demo.** Muestra tu asistente conectado a un disparador real: llega un mensaje o un formulario, el asistente procesa, la respuesta sale sola. Nombra las piezas en lenguaje simple: **disparador → asistente → acción**. No entres a la configuración técnica.
- **3 min — Los tres niveles.** Nivel 1: lo abro y le pido (donde están hoy). Nivel 2: se dispara solo y me pide aprobación. Nivel 3: se dispara solo y actúa. Casi ningún negocio early-stage debería estar en nivel 3 todavía.
- **3 min — Dónde se rompe.** Esta parte no se salta nunca:
  - **Inventa con seguridad.** Nunca lo dejes solo con precios, plazos legales o compromisos con clientes.
  - **No sabe lo que no le dijiste.** Cambiaste tus precios y no actualizaste el contexto: sigue cotizando con los viejos.
  - **Aprobación humana antes de publicar.** Todo lo que sale con tu nombre lo revisas tú, hasta que tengas 50 casos verdes seguidos.
  - **Datos sensibles.** No subas datos de clientes que no puedes subir.

**Key takeaway:** *"Primero que funcione contigo apretando el botón. Recién después le sueltas el botón."*

---

### B7 · Vitrina: 5 asistentes en vivo
**15 minutos · 1 slide**

**Objetivo:** consolidar por prueba social y mostrar variedad de casos. Es el bloque que la gente recuerda y comenta después.

**Dinámica:** 5 personas, 2 minutos cada una, con el notebook conectado al proyector. Formato estricto:
1. Qué hago y qué tarea odiaba (30 s)
2. Correr el asistente EN VIVO con un caso real (60 s)
3. Cuánto tiempo me ahorra por semana (30 s)

**Selección:** los eliges tú durante B5, no por voluntarios. Busca variedad deliberada: un servicio, un producto físico, alguien de mesa distinta, alguien que llegó escéptico, y —muy importante— **alguien cuyo asistente todavía no funciona bien**. Ese último es el más valioso: la sala ve que la iteración es normal y no se van con la idea de que a todos les salió a la primera.

**Key takeaway:** *"Ninguno de estos cinco escribió una línea de código. Escribieron instrucciones claras."*

---

### B8 · Cierre, compromiso de 7 días y recursos
**8 minutos · 4 slides**

**Objetivo:** convertir el entusiasmo de la sala en una acción concreta con fecha. Sin esto, el 80% no vuelve a abrir su asistente.

**Dinámica:**
- **4 min — Hoja de Compromiso de 7 Días.** Cada uno la llena y **le toma una foto con el celular ahí mismo**, antes de pararse. Tres campos:
  1. Voy a usar mi asistente en **[N] casos reales** antes del **[fecha exacta, 7 días]**
  2. La regla que sé que le falta y voy a agregar es: ______
  3. La segunda tarea que voy a delegarle cuando la primera funcione es: ______
- **2 min — Entrega de recursos.** QR proyectado y también impreso en cada mesa.
- **2 min — Cierre.** Vuelve al número del pizarrón de B0. *"Empezamos con [X] horas al mes perdidas. Te vas con una tarea menos. Repite esto cuatro veces y recuperaste tu mes."*

**Key takeaway final:** *"El asistente que construiste hoy vale cero si el lunes no lo abres. Ábrelo el lunes."*

---

## 4. El ejercicio principal: "El Asistente de Una Sola Tarea"

Es un ejercicio único partido en dos bloques (B4 + B5), con 70 minutos totales de construcción.

**Entregable concreto:** un asistente de IA creado, con nombre propio, instrucciones completas de 7 campos, contexto de negocio cargado y probado contra 3 casos reales, con al menos 2 en verde.

**Por qué funciona con audiencia no técnica:**
- No hay instalaciones, ni cuentas de pago obligatorias, ni una sola línea de código.
- El insumo es el propio negocio del participante, no un caso de estudio ajeno.
- El resultado se ve y se usa en la misma sesión.
- El criterio de éxito es binario y verificable: pasó 2 de 3 o no pasó.

**Criterios de calidad que anuncias al empezar B4** (proyéctalos y déjalos fijos):

1. Un asistente. Una tarea. Si tienes dos ideas, la segunda va a la Hoja de Compromiso.
2. Instrucciones concretas: nada de "profesional", "de calidad", "atractivo". Números, ejemplos, límites.
3. Mínimo 3 reglas duras, y una de ellas contra inventar datos.
4. Un ejemplo real pegado en el campo 7. No negociable.
5. Probado con casos reales tuyos, no inventados en el momento.

**Diferenciación para los que van rápido** (siempre hay 3-4): no los dejes ociosos y no los dejes empezar un segundo asistente. Dales el reto extra: *"Prueba con el caso más raro y difícil que hayas tenido este año. Ese que te tomó una hora resolver. Ahí se ve si tus reglas aguantan."*

**Rescate para los que van lento:** el ayudante les entrega el negocio ficticio de respaldo y las instrucciones semi-llenas. Objetivo mínimo: que terminen con algo que corre, aunque el caso no sea 100% suyo. Nadie se va con la pantalla vacía.

---

## 5. Recursos para llevar a casa

Todo en un enlace único con QR, entregado en B8 y enviado por correo esa misma noche. Sin registro adicional, sin fricción.

**Kit descargable:**

1. **Plantilla de Instrucciones en 7 campos** — versión editable, lista para copiar y pegar.
2. **Cuatro asistentes pre-armados** para los casos más comunes de la sala: responder consultas de clientes, redactar cotizaciones, convertir notas de reunión en tareas, y escribir publicaciones a partir de un hecho del negocio. Se copian y se les cambia el contexto.
3. **Tarjeta del Filtro de Tarea** — para elegir la tarea #2, #3 y #4 sin volver al workshop.
4. **Checklist de Prueba del Semáforo** — el protocolo de las 3 rondas.
5. **Guía de las 8 fallas más comunes** — inventar datos, contexto desactualizado, instrucciones vagas, demasiados archivos, resultado corregido a mano en vez de instrucción corregida, delegar lo que no dominas, automatizar antes de validar, publicar sin revisar.
6. **Plan de 30 días** — semana 1: usar el asistente actual todos los días. Semana 2: agregar las reglas que descubriste. Semana 3: construir el segundo asistente. Semana 4: evaluar cuál conectar a un disparador automático.
7. **Grabación de la demo de automatización** de B6, con las piezas nombradas.
8. **Comparativa de herramientas** con qué permite cada plan gratuito, con fecha de última verificación visible.

**Seguimiento vivo (esto multiplica el impacto del taller):**

- **Correo día 3:** una sola pregunta, *"¿Lo usaste?"*, con enlace para responder en un clic.
- **Correo día 7:** los 3 mejores asistentes de la sala, publicados con nombre y negocio. La prueba social es lo que reactiva a los que abandonaron.
- **Sesión de dudas en línea a los 14 días,** 45 minutos, opcional. La asistencia es baja pero la calidad de las preguntas es altísima: ahí aparecen los casos reales de producción.

---

## 6. Conteo de slides estimado

| Bloque | Slides | Detalle |
|---|---|---|
| B0 · Bienvenida | 4 | Título, la pregunta, la cuenta en vivo, reglas de la sala |
| B1 · Inventario | 3 | Consigna, cronómetro, instrucción de parejas |
| B2 · Qué es un asistente | 8 | Analogía del empleado, las 4 piezas (4 slides), demo malo, demo bueno |
| B3 · El filtro | 5 | Los 4 criterios, anti-ejemplos, consigna, validación de mesa |
| Pausa | 1 | Cronómetro de 10 min proyectado |
| B4 · Construcción 1 | 6 | Plantilla completa + 1 slide por bloque de campos con la consigna |
| B5 · Construcción 2 | 4 | Ronda 1, semáforo, ronda 3, meta 2 de 3 |
| B6 · Sin ti | 6 | Disparador-asistente-acción, 3 niveles, 4 riesgos (2 slides) |
| B7 · Vitrina | 1 | Formato de los 2 minutos |
| B8 · Cierre | 4 | Compromiso, QR de recursos, seguimiento, cierre con el número |
| **TOTAL** | **42** | ~14 slides por hora |

**Regla de la presentación:** 42 slides en 180 minutos es correcto solo porque **más de la mitad son de consigna y quedan proyectadas fijas** durante los ejercicios. Slides de contenido real: unas 20. Si te pasas de 50, estás dando una clase, no un taller.

**Formato:** máximo 8 palabras por slide en los bloques de charla. Los slides de consigna sí llevan texto completo porque la gente los lee mientras trabaja.

---

## 7. Métricas de éxito del workshop

Mídelas, no las asumas.

| Métrica | Cómo se mide | Meta |
|---|---|---|
| Asistentes construidos | Manos arriba al cierre de B5 | ≥ 85% de los presentes |
| Calidad mínima | Manos verdes en "2 de 3 casos" | ≥ 70% de los presentes |
| Compromiso firmado | Fotos de la Hoja de 7 Días | ≥ 90% |
| **Uso real al día 7** | Respuesta al correo de seguimiento | **≥ 40%** |
| Segundo asistente al día 30 | Encuesta corta | ≥ 20% |

La única métrica que importa de verdad es la cuarta. Las tres primeras se consiguen con buena facilitación; la cuarta te dice si el workshop cambió algo.

---

## 8. Riesgos y plan B

| Riesgo | Probabilidad | Respuesta |
|---|---|---|
| WiFi cae en pleno B4 | Media | Hotspots de respaldo + el ejercicio se completa en papel y se digita después. Las instrucciones escritas a mano son el activo, no la herramienta |
| Un tercio llega sin ejemplos reales | Alta | Casos universales y negocio ficticio en el kit del facilitador |
| La herramienta cambió su plan gratuito | Media | Verificación 48 h antes + plan B de conversación normal |
| Un participante monopoliza con preguntas técnicas | Alta | "Excelente pregunta, la respondo en la pausa" y sigues. No negocies |
| B4 se atrasa 10 minutos | Muy alta | Recortas B6 a 6 minutos y B7 a 3 presentaciones. Nunca recortes B5 |
| Alguien quiere construir el asistente que reemplaza a su equipo | Media | Redirígelo a la tarea repetitiva. Este taller no es sobre reemplazar gente, es sobre recuperar tus horas |