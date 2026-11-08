# Ling 3.0 Flash — startup_content/workshop_outline

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.69 | quality: 9.72
- latency_total: 221.257s | tokens_per_second: 30.7
- input_tokens: 235 | output_tokens: 6794
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

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
### Workshop Práctico — 3 Horas | 20-30 Participantes | Emprendedores Early-Stage No-Técnicos

---

## 📋 1. AGENDA DETALLADA CON TIEMPOS

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 – 0:15 | 🔥 Bienvenida y Rompehielo | 15 min |
| 0:15 – 0:35 | 🧠 Bloque 1: ¿Qué es un Asistente de IA y para qué te sirve? | 20 min |
| 0:35 – 0:50 | 🎯 Bloque 2: Definir el caso de uso perfecto | 15 min |
| 0:50 – 1:15 | 🛠️ Bloque 3: Construyamos el prompt (Ejercicio Principal) | 25 min |
| 1:15 – 1:35 | 🤖 Bloque 4: Herramientas sin código — Demo en vivo | 20 min |
| 1:35 – 1:45 | ☕ Pausa | 10 min |
| 1:45 – 2:10 | 🚀 Bloque 5: Arma tu MVP con no-code (Ejercicio Práctico) | 25 min |
| 2:10 – 2:30 | 🎤 Bloque 6: Testeo rápido y retroalimentación entre pares | 20 min |
| 2:30 – 2:45 | 💡 Bloque 7: Cómo escalar, medir y mejorar | 15 min |
| 2:45 – 3:00 | 🎉 Cierre, next steps y networking | 15 min |

**Total: 180 minutos**

---

## 🎒 2. MATERIALES NECESARIOS (PREPARAR ANTES)

### Para el facilitador:
- [ ] Laptop con internet estable y cuenta registrada en ChatGPT, Make (Integromat) y/o Voiceflow
- [ ] Proyector o pantalla compartida
- [ ] Altavoz Bluetooth (para dinámicas en grupo)
- [ ] Plantillas impresas: Ficha de Caso de Uso (1 por persona), Tarjetas de Rol (para icebreaker), Checklist MVP
- [ ] Marcadores de colores, pizarra blanca o papelógrafos
- [ ] Post-its de colores (mínimo 3 colores por persona)
- [ ] Cronómetro visible para gestionar tiempos
- [ ] Playlist de música de fondo energética (para ejercicios y pausa)

### Para cada participante:
- [ ] Laptop o tablet con internet (pedir que vengan preparados; tener 3-4 laptops de respaldo)
- [ ] Acceso a una cuenta gratuita de ChatGPT (o similar) — enviar link de registro en confirmación previa
- [ ] Acceso a una cuenta gratuita de Make (Integromat) o Zapier
- [ ] Cuenta gratuita en Voiceflow o Botpress (enviar link previo)
- [ ] Ficha impresa: "Mi Caso de Uso Ideal" (plantilla con campos)
- [ ] Tarjeta personal con nombre y empresa

### Logística del sala:
- [ ] Mesas agrupadas en clusters de 4-5 personas
- [ ] WiFi de alta velocidad (confirmar ancho de banda para 30 personas)
- [ ] Cartel de bienvenida con hashtag del workshop
- [ ] Snacks y bebidas (café, agua, fruta) — mantener energía alta

---

## 📚 3. DESGLOSE POR BLOQUES

---

### 🔥 BLOQUE 0: BIENVENIDA Y ROMPEHIELO
**⏱ Duración:** 15 minutos

**🎯 Objetivo:**
Crear ambiente de confianza, establecer la energía del workshop y que todos se conozcan con el contexto correcto.

**📊 Dinámica:**
- **(3 min)** Facilitador saluda con energía, presenta el objetivo del workshop: *"En las próximas 3 horas van a tener un asistente de IA funcional para su startup. Sí, en serio."*
- **(7 min)** **Icebreaker "¿Qué haría tu startup con un asistente mágico?"**
  - Cada persona en su mesa tiene 1 minuto para escribir en un post-it: *"Si tuviera un asistente de IA que pudiera hacer UNA cosa por mí, sería..."*
  - Pegan los post-its en una pared/mesa grande. Facilitador agrupa por temas visualmente (ventas, atención al cliente, operaciones, marketing, etc.)
  - Breve lectura en voz alta de 3-4 post-its destacados.
- **(5 min)** Presentación de la agenda y reglas del juego: *"Aquí no hay preguntas tontas, todos aprendemos juntos."*

**💡 Key Takeaway:**
> Hoy vas a construir algo real. No es teoría — es hacer. Trae tu energía y tu caso de uso real.

**🟦 Slide count:** 4 slides

---

### 🧠 BLOQUE 1: ¿QUÉ ES UN ASISTENTE DE IA Y PARA QUÉ TE SERVE?
**⏱ Duración:** 20 minutos

**🎯 Objetivo:**
Demoler mitos, entender conceptos clave de forma simple y mostrar casos reales de startups que ya usan asistentes de IA.

**📊 Dinámica:**
- **(8 min)** **Mini-charla energética con demos visuales:**
  - ¿Qué es realmente un asistente de IA? (No es robot — es una herramienta que entiende texto y responde con inteligencia)
  - Conceptos clave en lenguaje simple:
    - **Prompt** = la instrucción que le das (ej: "Actúa como un agente de ventas de mi startup y responde estas preguntas")
    - **Contexto** = la información que le das para que entienda tu mundo
    - **Flujo** = el camino que sigue el asistente según lo que el usuario diga
  - Mostrar 3 ejemplos reales:
    1. Startup de e-commerce → asistente que responde preguntas de productos (ahorro de 60% en tiempo de atención)
    2. Startup de servicios → asistente que hace seguimiento de leads automático
    3. Startup SaaS → asistente que onboardea nuevos usuarios
  - Mostrar screenshot/demo rápida de un chatbot real funcionando
- **(5 min)** **Discusión rápida en parejas:** *"¿Cuál de estos 3 ejemplos se parece más a lo que hace tu startup?"* (2 min de conversación + 3 min de compartir en plenario)
- **(7 min)** **Mini-demo en vivo:** Facilitador abre ChatGPT y construye un prompt básico en tiempo real frente a la pantalla. Mostrar cómo 30 segundos de instrucción clara generan un resultado útil. *"¿Ven? Esto es lo que van a crear."*

**💡 Key Takeaway:**
> Un asistente de IA es como un empleado nuevo muy rápido — pero necesitas darle instrucciones claras y contexto para que haga bien su trabajo.

**🟦 Slide count:** 12 slides

---

### 🎯 BLOQUE 2: DEFINIR EL CASO DE USO PERFECTO
**⏱ Duración:** 15 minutos

**🎯 Objetivo:**
Que cada participante defina con claridad qué quiere que su asistente de IA haga, enfocándose en UN caso de uso específico y realista.

**📊 Dinámica:**
- **(3 min)** **Charla rápida:** *"El error #1 es querer que el asistente haga todo. El secreto: empieza con UN caso de uso. Puedes escalar después."*
  - Mostrar el framework **"¿Para quién? ¿Hace qué? ¿Cuál es el resultado?"**
  - Ejemplo llenado: *"Para: clientes potenciales que visitan mi landing page. Hace: responde preguntas sobre precios y agenda demo. Resultado: más ventas sin que yo responda cada mensaje."*
- **(7 min)** **Ejercicio individual con plantilla "Mi Caso de Uso Ideal":**
  - Cada persona llena la ficha impresa con:
    - 🎯 Mi startup/idea es: ___
    - 👤 A quién quiero ayudar con IA: ___
    - 📝 La tarea principal que quiero que haga: ___
    - 📊 El resultado que busco: ___
    - ❓ Ejemplo de pregunta que le haría al asistente: ___
  - Facilitador circula entre mesas ayudando a enfocar (restringir, simplificar)
- **(5 min)** **Compartir en mesa:** Cada mesa elige el caso de uso más interesante de sus miembros y lo comparte brevemente con el grupo (1 minuto por mesa).

**💡 Key Takeaway:**
> Tu asistente de IA NO es para todo. Elige UN problema real, resuélvelo bien, y luego escala.

**🟦 Slide count:** 6 slides

---

### 🛠️ BLOQUE 3: CONSTRUYAMOS EL PROMPT (EJERCICIO PRINCIPAL — PARTE 1)
**⏱ Duración:** 25 minutos

**🎯 Objetivo:**
Que todos los participantes escriban un prompt funcional y bien estructurado para su asistente de IA, usando una plantilla guiada.

**📊 Dinámica:**
- **(5 min)** **Charla + demo:** *"El prompt es tu mejor arma. No es programación — es redacción inteligente."*
  - Mostrar la **Plantilla de Prompt Magico** con 6 componentes:
    1. 🎭 **Rol:** "Actúa como un experto en [área]..."
    2. 🎯 **Misión:** "Tu trabajo es [tarea específica]..."
    3. 👥 **Audiencia:** "La persona que te va a hablar es [perfil]..."
    4. 📦 **Contexto:** "Aquí tienes información sobre [tu startup/producto]..."
    5. 📐 **Formato:** "Responde en [formato: lista, párrafo, tabla, etc.]..."
    6. ⚡ **Restricciones:** "NO hagas [X]. Si no sabes, di [Y]..."
  - Ejemplo completo llenado frente al proyector
- **(15 min)** **Ejercicio individual/grupal:**
  - Cada persona usa la plantilla impresa para escribir su prompt completo
  - Luego lo prueba en ChatGPT (o similar) directamente en su laptop
  - Iterar: ajustar, mejorar, volver a probar
  - Facilitador y asistentes circulan ayudando activamente
  - Música de fondo energética para mantener ritmo
- **(5 min)** **Pausa rápida de mostrar:** Facilitador pide que 2-3 personas compartan pantalla o lean en voz alta sus mejores resultados. Celebración pública: *"¡Miren lo que acaba de crear esta persona en 10 minutos!"*

**💡 Key Takeaway:**
> Un buen prompt = Rol + Misión + Audiencia + Contexto + Formato + Restricciones. Con esta fórmula, cualquiera puede obtener resultados profesionales de una IA.

**🟦 Slide count:** 8 slides

---

### 🤖 BLOQUE 4: HERRAMIENTAS SIN CÓDIGO — DEMO EN VIVO
**⏱ Duración:** 20 minutos

**🎯 Objetivo:**
Mostrar las principales plataformas no-code para crear asistentes de IA con interfaz visual, y que los participantes vean que NO necesitan programar.

**📊 Dinámica:**
- **(3 min)** **Charla rápida de panorámica:**
  - Mostrar mapa visual de herramientas (en pantalla):
    - **ChatGPT Custom GPTs** → más fácil, todo en ChatGPT
    - **Voiceflow** → visual, drag & drop, para bots conversacionales
    - **Make (Integromat)** → para conectar tu asistente con otras herramientas (Google Sheets, CRM, email)
    - **Botpress, Flowise, BotPenguin** → alternativas gratuitas
  - *"Vamos a construir en la que menos código necesiten."*
- **(12 min)** **Demo en vivo paso a paso — Construir un asistente en Voiceflow (o Custom GPT):**
  - Crear un nuevo "assistant" / "chatbot"
  - Agregar el prompt que ya construyeron en Bloque 3
  - Configurar el flujo básico: bienvenida → pregunta del usuario → respuesta del asistente → cierre
  - Probarlo en tiempo real frente al proyector
  - Mostrar cómo agregar una "Knowledge Base" (subir un PDF con info de su startup)
  - Mostrar el resultado final: un link compartible o un chat embebido
- **(5 min)** **Q&A rápida:** *"¿Alguna duda sobre cómo funciona? Levanten la mano."*

**💡 Key Takeaway:**
> No necesitas saber programar. Existen herramientas visuales donde solo arrastras, conectas y publicas. Tu asistente puede estar online en menos de 30 minutos.

**🟦 Slide count:** 10 slides

---

### ☕ PAUSA
**⏱ Duración:** 10 minutos

- Snacks, café, música
- Facilitador aprovecha para revisar que todas las laptops funcionan, resolver problemas técnicos individuales

---

### 🚀 BLOQUE 5: ARMA TU MVP — EJERCICIO PRÁCTICO (PARTE 2)
**⏱ Duración:** 25 minutos

**🎯 Objetivo:**
Que cada participante tenga un asistente de IA funcional y publicable para su startup, usando la herramienta no-code que se mostró.

**📊 Dinámica:**
- **(3 min)** **Charla motivacional + instrucciones:**
  - *"Ya tienen su prompt, ya vieron la herramienta. Ahora toca armar el producto. Es como armar LEGO — la pieza ya está, solo hay que conectarla."*
  - Checklist en pantalla:
    1. ✅ Entrar a la plataforma (Custom GPT / Voiceflow / alternativa)
    2. ✅ Crear nuevo asistente
    3. ✅ Copiar/pegar el prompt del Bloque 3
    4. ✅ Agregar contexto (nombre de startup, producto, tono)
    5. ✅ Probar al menos 3 interacciones
    6. ✅ Ajustar según resultados
    7. ✅ Obtener link de compartir o código embebido
- **(18 min)** **Trabajo independiente con asistencia intensiva:**
  - Facilitador y co-facilitador(s) recorren mesas constantemente
  - Resolver problemas técnicos, guiar en la integración del prompt, ayudar con la plataforma
  - Música de fondo motivacional
  - Pantalla secundaria con tutoriales paso a paso por si alguien se atrasa
  - **Bonus para los que terminan rápido:** "¿Quieres conectar tu asistente a WhatsApp o Telegram? Aquí te mostramos cómo..."
- **(4 min)** **Mini-celebración:**
  - *"Si tienes un asistente funcionando en tu laptop, ¡levántate y agita la mano!"*
  - Reconocer públicamente a quienes ya lo lograron

**💡 Key Takeaway:**
> Ya tienes un MVP real de tu asistente de IA. No es perfecto — y no necesita serlo. Está listo para probarlo con usuarios reales.

**🟦 Slide count:** 5 slides

---

### 🎤 BLOQUE 6: TESTEO RÁPIDO Y RETROALIMENTACIÓN ENTRE PARES
**⏱ Duración:** 20 minutos

**🎯 Objetivo:**
Que los participantes prueben los asistentes de otros compañeros, den feedback constructivo y mejoren sus propios asistentes con insights externos.

**📊 Dinámica:**
- **(3 min)** **Charla breve:** *"La IA mejora con uso. Tu primer asistente NO será tu último. Vamos a hacer que otros lo prueben y te den feedback."*
  - Explicar el protocolo de feedback:
    - 🟢 **Lo que funciona** (al menos 1 cosa)
    - 🔴 **Lo que se puede mejorar** (al menos 1 cosa)
    - 💡 **Una idea extra** (algo que no habías pensado)
- **(12 min)** **Dinámica "Testeo Rápido":**
  - Cada persona se empareja con alguien de otra mesa
  - Se intercambian laptops / comparten el link del asistente
  - Cada uno interactúa con el asistente del otro durante 3 minutos
  - Comparten feedback usando el protocolo (3 minutos)
  - Rotan: cada persona prueba 2 asistentes diferentes (6 min por ronda x 2 rondas = 12 min total)
- **(5 min)** **Plenario rápido:**
  - *"¿Qué sorpresas tuvieron? ¿Qué descubrieron?"*
  - 2-3 personas comparten insights. Facilitador anota en pizarra patrones comunes de mejora.

**💡 Key Takeaway:**
> Tu asistente mejora con feedback real. No lo pruebes solo — haz que otros lo usen y escucha lo que descubren.

**🟦 Slide count:** 6 slides

---

### 💡 BLOQUE 7: CÓMO ESCALAR, MEDIR Y MEJORAR
**⏱ Duración:** 15 minutos

**🎯 Objetivo:**
Dar una hoja de ruta clara para que los participantes lleven su asistente de IA del MVP a una herramienta real de valor para su startup.

**📊 Dinámica:**
- **(5 min)** **Mini-charla "De MVP a Producto":**
  - **Siguientes pasos concretos:**
    - Semana 1: Probar con 5-10 usuarios reales
    - Semana 2: Medir qué preguntas hacen, dónde falla, qué confunde
    - Semana 3: Mejorar el prompt y agregar más contexto
    - Mes 2: Conectar con herramientas reales (CRM, email, WhatsApp)
    - Mes 3: Medir tiempo ahorrado, leads generados, satisfacción
  - **Métricas simples que importan:**
    - ⏱ Tiempo que ahorra (vs. hacerlo tú)
    - 💰 Leads o ventas que genera
    - 😊 Satisfacción del usuario (¿vuelve a preguntar?)
  - **Errores comunes a evitar:**
    - Que el asistente responda cosas fuera de su rol
    - No tener un plan cuando no sabe algo (ej: "Pásame a un humano")
    - No actualizar la Knowledge Base con información nueva
- **(5 min)** **Demo rápido:** Mostrar cómo agregar una Knowledge Base en ChatGPT Custom GPT (subir un PDF de su startup) — esto es el "secreto" para que el asistente conozca tu mundo.
- **(5 min)** **Charla de cierre motivacional:**
  - *"Los asistentes de IA no reemplazan emprendedores — los potencian. El que domine esta herramienta hoy, tiene ventaja competitiva mañana."*
  - Mostrar quote o dato de impacto (ej: "Startups que usan IA en atención reducen costos operativos en 40% promedio")

**💡 Key Takeaway:**
> Tu asistente de IA es un proyecto vivo. Mejora con datos, mide resultados, y conéctalo con tu operación real. No es un experimento — es una herramienta de negocio.

**🟦 Slide count:** 10 slides

---

### 🎉 BLOQUE 8: CIERRE, NEXT STEPS Y NETWORKING
**⏱ Duración:** 15 minutos

**📊 Dinámica:**
- **(3 min)** **Entrega de certificados simples** (opcional: imprimir "Certificado de Construcción de Asistente de IA" con el nombre de cada participante y el nombre de su startup)
- **(5 min)** **Recursos para llevar a casa** (mostrar en pantalla y entregar impreso/USB):
  - Lista de herramientas con links
  - Plantilla de Prompt (versión digital)
  - Checklist de implementación
  - Recomendaciones de comunidades y aprendizaje
- **(4 min)** **Compromiso público rápido:**
  - Cada persona escribe en un post-it: *"En las próximas 7 días, voy a hacer ___ con mi asistente de IA"*
  - Lo pegan en una "Pared de Compromisos"
  - Facilitador toma foto para compartir con el grupo después
- **(3 min)** **Networking con música de fondo:**
  - Facilitador se queda disponible para consultas individuales
  - Se comparte grupo de WhatsApp/Telegram del workshop
  - *"¡Gracias por construir hoy! Tu asistente ya está vivo. Cuídalo, aliméntalo y obsérvalo crecer."*

**💡 Key Takeaway:**
> Esto no es el final — es el inicio. Tu asistente de IA ya existe. El reto ahora es hacerlo crecer.

**🟦 Slide count:** 4 slides

---

## 🎯 4. EJERCICIO PRINCIPAL DEL WORKSHOP

### **"Construye tu Asistente de IA Funcional en 30 Minutos"**

**Descripción:** Un ejercicio guiado que todos realizan, combinando el Bloque 3 (construir el prompt) y el Bloque 5 (implementar en herramienta no-code).

**Pasos:**
1. **Definir** (5 min): Usando la plantilla del Bloque 2, cada persona tiene su caso de uso claro
2. **Escribir el prompt** (10 min): Usando la Plantilla de Prompt Mágico (Rol + Misión + Audiencia + Contexto + Formato + Restricciones), escriben un prompt completo
3. **Probar el prompt** (5 min): Lo pegan en ChatGPT y verifican que el resultado sea útil. Ajustan si es necesario.
4. **Implementar en herramienta no-code** (10 min): Entran a Voiceflow (o Custom GPTs de ChatGPT) y construyen su asistente con el prompt listo. Configuran el flujo básico.
5. **Probar y compartir** (5 min): Prueban su asistente 2-3 interacciones. Si tienen tiempo, comparten el link con su mesa.

**Resultado esperado:** Cada participante sale con un asistente de IA funcional que puede abrir en su navegador y probar.

---

## 📦 5. RECURSOS PARA LLEVAR A CASA

### Digitales (enviar por email/Grupo WhatsApp al finalizar):
- [ ] 📄 **Plantilla "Prompt Mágico"** — PDF editable con los 6 componentes y ejemplo lleno
- [ ] 📄 **Checklist "De MVP a Producto"** — Hoja de ruta de 90 días para escalar el asistente
- [ ] 📄 **Guía de Herramientas No-Code** — Comparativa de plataformas con pros, contras, precios y links
- [ ] 📄 **Grabación del workshop** (si se graba) — enlace a video
- [ ] 📄 **Slides del workshop** — PDF con todas las presentaciones
- [ ] 🔗 **Lista de comunidades** — Grupos de Telegram/Discord de emprendedores + IA en LatAm
- [ ] 📚 **Reading list** — 5 artículos/videos recomendados para seguir aprendiendo
- [ ] 🎓 **Curso gratuito recomendado** — Link a curso gratuito de IA para emprendedores (ej: curso de Make, o Google AI Skills)

### Físicos (entregados en el evento):
- [ ] 📋 Ficha "Mi Caso de Uso Ideal" (impresa)
- [ ] 📋 Plantilla de Prompt (impresa, formato bolsillo)
- [ ] 🏅 Certificado de participación (personalizado)
- [ ] 📌 Tarjeta de recursos con links en QR (para escanear desde celular)

---

## 📊 6. SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides | Justificación |
|---------|--------|---------------|
| Bienvenida y Rompehielo | 4 | Intro, agenda, reglas, objetivo |
| Bloque 1: ¿Qué es un Asistente de IA? | 12 | Explicación de conceptos, ejemplos, capturas de pantalla, demo |
| Bloque 2: Definir Caso de Uso | 6 | Framework, ejemplo, instrucciones de ejercicio |
| Bloque 3: Construir el Prompt | 8 | Plantilla, componentes, ejemplo, instrucciones |
| Bloque 4: Herramientas No-Code | 10 | Mapa de herramientas, demo paso a paso, screenshots |
| Bloque 5: Arma tu MVP | 5 | Checklist, instrucciones, motivación |
| Bloque 6: Testeo entre Pares | 6 | Protocolo de feedback, instrucciones, dinámica |
| Bloque 7: Escalar y Mejorar | 10 | Hoja de ruta, métricas, errores comunes, demo |
| Bloque 8: Cierre | 4 | Certificados, recursos, compromiso, agradecimiento |
| **TOTAL** | **~65 slides** | Para 3 horas, esto da un ritmo dinámico con mucha interacción |

---

## ⚡ BONUS: TIPS DEL FACILITADOR

1. **Mantén la energía alta** — Cambia de dinámica cada 10-15 min máximo. Alterna: charla → ejercicio → demo → discusión.
2. **Circula constantemente** — No te quedes en el frente. El 60% del tiempo debes estar entre las mesas.
3. **Normaliza el error** — *"Si tu asistente responde algo absurdo, ¡perfecto! Eso significa que aprendiste. Ajusta y vuelve a intentar."*
4. **Ten un co-facilitador técnico** — Idealmente alguien que pueda resolver problemas de plataforma sin detener el grupo.
5. **Prepara "planes B"** — Si WiFi falla, tener screenshots y videos pregrabados de los demos. Si una herramienta cae, tener alternativa lista.
6. **Usa la competencia sana** — *"¿Quién tiene el asistente más chistoso? ¿El más útil? ¿El más creativo?"* — Motiva a los que van rezagados.
7. **Cierra con claridad** — Que cada persona se vaya con UNA acción concreta para las próximas 48 horas.

---

> *"El mejor momento para construir tu asistente de IA fue ayer. El segundo mejor momento es ahora."* 🚀