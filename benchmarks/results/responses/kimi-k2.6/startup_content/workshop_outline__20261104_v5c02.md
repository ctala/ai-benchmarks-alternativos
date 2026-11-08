# Kimi K2.6 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.05 | quality: 9.72
- latency_total: 107.95s | tokens_per_second: 56.1
- input_tokens: 219 | output_tokens: 6056
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

 # 🤖 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico | Outline Completo

---

## 📋 1. AGENDA DETALLADA (3 HORAS)

| Tiempo | Bloque | Duración |
|--------|--------|----------|
| 0:00 - 0:20 | 🔥 Apertura y calentamiento | 20 min |
| 0:20 - 0:55 | 🧠 Fundamentos sin código | 35 min |
| 0:55 - 1:10 | ☕ Break + networking | 15 min |
| 1:10 - 1:50 | 🛠️ Construcción en vivo | 40 min |
| 1:50 - 2:30 | ⚡ Ejercicio principal: Tu asistente funcional | 40 min |
| 2:30 - 2:45 | ☕ Break rápido | 15 min |
| 2:45 - 3:15 | 🚀 Casos de Latinoamérica y escalamiento | 30 min |
| 3:15 - 3:30 | 🎯 Cierre, recursos y próximos pasos | 15 min |

---

## 🎒 2. MATERIALES NECESARIOS (Pre-workshop)

### **Que prepara el facilitador:**
| Item | Detalle | Cantidad |
|------|---------|----------|
| Proyector + adaptadores | HDMI, USB-C, Lightning | 2 de cada |
| WiFi de respaldo | Hotlist con 20GB mínimo | 2 routers |
| Extensiones eléctricas | 6 tomas cada una | 5 unidades |
| Stickers/post-its | Para votación y agrupar ideas | 3 bloques |
| Marcadores gruesos | Para pizarras/papeles | 10 |
| Hojas A3 | Para mapas de flujo | 30 |
| Cuentas de demo pre-creadas | En cada plataforma (5 por plataforma) | 15 totales |
| Laptop de backup | Con todo instalado y logueado | 1 |
| Agua + snacks energéticos | Maní, barras de cereal | Suficiente |

### **Que traen los participantes (enviar por mail 3 días antes):**
```
📧 MAIL DE PREPARACIÓN:

"Hola, futuro constructor de IA 👋

PARA ESTE WORKSHOP NECESITÁS:
✅ Laptop con carga completa
✅ Celular con WhatsApp activo
✅ Cuenta de Gmail (para loguearse en todo)
✅ Una idea de qué hace tu startup (aunque sea vaga)

OPCIONAL PERO RECOMENDADO:
💳 Tarjeta de crédito (muchas herramientas tienen free tier 
   pero piden verificación; NO vamos a gastar, es solo por si 
   alguien quiere probar features de pago)

NO NECESITÁS:
❌ Saber programar
❌ Saber de IA
❌ Traer ideas terminadas

Pre-tarea de 5 min (hacela en el bondi):
📝 Escribí: "Mi startup ayuda a [QUIÉN] a [QUÉ PROBLEMA RESUELVE]"
   Ejemplo real: "Mi startup ayuda a veterinarios a recordar 
   cuándo vacunar a las mascotas"
```

### **Plataformas con cuentas enterprise/demo preparadas:**
- **Chatbase.co** (chatbots para web)
- **Voiceflow.com** (asistentes conversacionales)
- **Make.com** (automatizaciones, ex-Integromat)
- **Google AI Studio** (probar prompts gratis)
- **Typeform + ChatGPT integration** (para demo rápida)

---

## 🧩 3. BLOQUES DETALLADOS

---

### **BLOQUE 1: 🔥 APERTURA Y CALENTAMIENTO**
**Duración:** 20 min | **Slides:** 8

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Romper hielo, alinear expectativas, mostrar que "no ser técnico" no es excusa |
| **Dinámica** | Charla rápida (10 min) + ejercicio grupal (10 min) |

**Actividad: "El peor chatbot del mundo" (10 min)**

> *"Antes de construir bien, vamos a construir MAL. En 3 minutos, diseñen el chatbot más inútil posible para una pizzería. Que sea frustrante de propósito."*

- Grupos de 3 personas
- Dibujan en A3 el flujo del chatbot
- Presentan en 30 segundos al grupo
- **Risa garantizada, tensiones bajan**

**Key takeaway:** *"Entender qué hace MAL un asistente te da superpoderes para diseñar uno bueno. Vos ya sabés de experiencia de cliente porque SOS cliente todos los días."*

**Slides (8):**
1. Título grande con animación
2. Foto de un chatbot fail real (ej: el de algún banco argentino)
3. "Quién soy" (facilitador, 30 segundos)
4. Reglas del workshop: "No hay preguntas tontas, sí hay chatbots tontos"
5. Agenda visual con íconos
6. Ejercicio: "El peor chatbot" - instrucciones
7. Tiempo de grupos (fondo con timer)
8. Compartimos: "¿Qué hizo que fuera terrible?"

---

### **BLOQUE 2: 🧠 FUNDAMENTOS SIN CÓDIGO**
**Duración:** 35 min | **Slides:** 14

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Entender componentes de un asistente de IA y mapearlos a herramientas reales |
| **Dinámica** | Demo en vivo + ejercicio individual corto |

**Estructura (35 min):**

| Tiempo | Actividad |
|--------|-----------|
| 0-8 min | "Anatomía de un asistente" - charla con metáforas |
| 8-18 min | Demo en vivo: construyo uno en 10 minutos |
| 18-28 min | Ejercicio individual: "Mapeá TU asistente" |
| 28-35 min | Compartimos 3 ejemplos al azar |

**Metáfora central (repetir durante todo el workshop):**
> *"Un asistente de IA es como un mozo en un restaurante: ESCUCHA (entradas), PIENSA (procesa con el 'chef'/IA), HACE (acciones), y APRENDE (se acuerda si te gustó picante)."*

**Demo en vivo (10 min):**
- Entro a Chatbase.co
- Subo un PDF de FAQ de ejemplo (tengo 3 preparados: fintech, edtech, health)
- Configuro en 5 clics
- Pruebo en mi celular, proyectando la pantalla
- **"Listo. Diez minutos. Cero código."**

**Ejercicio: "Tu asistente en una servilleta" (10 min)**
```
En tu hoja A3, completá:

MI STARTUP: _______________________

MI ASISTENTE ATIENDE A: [ ] Clientes  [ ] Equipo interno  [ ] Proveedores

CUANDO LE ESCRIBEN, ÉL/ELLA TIENE QUE:
1. _________________________________
2. _________________________________
3. _________________________________

INFO QUE NECESITA SABER (¿dónde está?):
□ PDF  □ Web  □ Excel  □ En mi cabeza  □ Base de datos

ACCIONES QUE DEBE HACER:
□ Responder solo  □ Agendar  □ Cobrar  □ Enviar mail  □ Alertar a alguien
```

**Key takeaway:** *"No empezás por la herramienta. Empezás por el trabajo: ¿qué conversación quiero automatizar? La herramienta es el último paso."*

**Slides (14):**
1. "¿Qué es realmente un asistente de IA?" (anatomía visual)
2. Metáfora del mozo (ilustración)
3-5. Los 3 componentes: INPUT → PROCESAMIENTO → OUTPUT (uno por slide, con ejemplos visuales)
6. "El ecosistema no-code 2024" (mapa mental de herramientas)
7. Demo en vivo: pantalla de login
8. Demo: subiendo documento
9. Demo: configurando respuestas
10. Demo: ¡probando en mi celular!
11. Instrucciones ejercicio "servilleta"
12. Template visual del ejercicio
13. Ejemplo completado (salud/fitness)
14. "¿Preguntas antes del break?"

---

### **BLOQUE 3: ☕ BREAK + NETWORKING**
**Duración:** 15 min

**Dinámica activa:** "Speed dating de problemas"
> *"En estos 15 min, encontrá a alguien que tenga un problema parecido al tuyo, o totalmente opuesto. Intercambiá contacto. El networking es el mejor break."*

- Música energética de fondo
- Facilitador circula y escucha (recoge 2-3 ideas para mencionar después)

---

### **BLOQUE 4: 🛠️ CONSTRUCCIÓN EN VIVO**
**Duración:** 40 min | **Slides:** 12

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Que cada uno tenga un asistente configurado al 70% |
| **Dinámica** | "Sigan al líder" - yo construyo, ellos replican en paralelo |

**Setup previo al workshop:**
- 5 facilitadores/voluntarios (1 cada 6 participantes) que ya hicieron el ejercicio
- Cada voluntario domina una plataforma diferente

**Flujo (40 min):**

| Tiempo | Qué hacemos |
|--------|-------------|
| 0-5 min | Elegí tu plataforma según TU caso (guía de decisión) |
| 5-25 min | Construcción guiada paso a paso |
| 25-35 min | Prueba con tu celular, iterá |
| 35-40 min | "Showcase rápido" - 3 voluntarios muestran |

**Guía de decisión (proyectada en pantalla grande):**

| Si tu caso es... | Usá... | Porque... |
|------------------|--------|-----------|
| Responder FAQs de tu web | **Chatbase** | 5 min de setup, se embebe fácil |
| WhatsApp con lógica compleja | **Voiceflow** + WhatsApp API | Flujos visuales potentes |
| Conectar con 3+ herramientas | **Make** + cualquier IA | El rey de las integraciones |
| Prototipo rápido para validar | **Google AI Studio** | Gratis, sin tarjeta, instantáneo |

**Construcción guiada (20 min):**
- Yo construyo en Chatbase (el más accesible)
- Los que eligieron lo mismo, siguen paso a paso
- Los que eligieron otra, sus voluntarios los guían
- **Paso crítico:** todos deben subir SU información (FAQ, web, o texto que prepararon)

**Momento "Oh shit" preparado:**
> *"Si te sale error, NO levantes la mano todavía. Primero: ¿refrescaste? ¿estás en el navegador correcto? ¿probaste en incógnito? El 80% de los errores se resuelven así. Después sí, levanta la mano."*

**Key takeaway:** *"En 20 minutos tenés algo que funciona. No perfecto, FUNCIONAL. El perfeccionismo mata más startups que la falta de recursos."*

**Slides (12):**
1. "Manos al código... digo, al no-código" (título chiste)
2. Guía de decisión de plataformas (tabla visual)
3. Paso 1: Crear cuenta (screenshot con flechas)
4. Paso 2: Elegir tipo de asistente
5. Paso 3: Subir tu conocimiento (¡este es el secreto!)
6. "Truco: si no tenés documentos, copiá y pegá de tu web"
7. Paso 4: Configurar personalidad ("hacelo hablar como vos")
8. Paso 5: Probar, fallar, ajustar
9. Paso 6: Publicar (o al menos, obtener link de prueba)
10. "¿Atorado? Checklist de supervivencia"
11. Showcase: "¿Quién se anima a mostrar?"
12. "No es perfecto, ¡pero existe!" (celebración)

---

### **BLOQUE 5: ⚡ EJERCICIO PRINCIPAL**
**Duración:** 40 min | **Slides:** 6

---

## 🎯 4. EJERCICIO PRINCIPAL DEL WORKSHOP

### **"Tu Asistente MVP en 30 Minutos"**

**Objetivo:** Cada participante sale con un asistente funcional que puede probar con clientes reales esta misma semana.

---

**FASE 1: DEFINIR EL CASO DE USO (5 min)**
```
Completá esta frase en voz alta con tu vecino:

"Mi asistente se llama _______ y cuando alguien le escribe 
por _______, él/ella responde _______ y luego hace _______."

Ejemplo real de último workshop:
"Mi asistente se llama Turi y cuando alguien le escribe por 
Instagram, él responde cuánto cuesta el tour y luego envía 
un calendly para agendar."
```

---

**FASE 2: CONSTRUCCIÓN LIBRE CON GUARDA-RAILS (20 min)**

**Guarda-rails (reglas para no atascarse):**

| No hagas esto | Hacé esto en cambio |
|---------------|---------------------|
| Querer que haga 10 cosas | Que haga 1 cosa MUY bien |
| Escribir 500 líneas de "base de conocimiento" | Copiar y pegar 5 conversaciones reales que ya tuviste |
| Preocuparte por el logo/color | Preocuparte por que entienda bien la pregunta |
| Intentar conectar con tu sistema de pagos | Que te avise por email cuando alguien quiere pagar |

**Checklist de éxito (proyectado en pantalla durante los 20 min):**
```
□ Responde coherente a 3 preguntas que le haría tu cliente típico
□ Tiene un "límite honesto": sabe decir "no sé, te paso con un humano"
□ Tiene TU voz (no suena a robot de call center)
□ Funciona en el canal que elegiste (web, WhatsApp, o al menos por link)
```

---

**FASE 3: PRUEBA DE FUEGO (10 min)**

**"El test del suegro/a"**
> *"Prestale tu celular a tu vecino. Que le escriba como si fuera tu cliente más difícil. Si tu asistente no lo manda a la mierda, estás bien."*

- Intercambio de celulares con el vecino
- 3 minutos de "ataque" con preguntas difíciles
- Feedback rápido: "¿Qué funcionó? ¿Qué lo hizo sonar robótico?"

---

**FASE 4: COMPROMISO PÚBLICO (5 min)**

Cada uno completa en voz alta:
> *"Esta semana, mi asistente va a atender a [NÚMERO] personas reales. Si funciona bien, voy a [SIGUIENTE PASO]. Si funciona mal, voy a [AJUSTE CONCRETO]."*

Ejemplo: *"Esta semana, mi asistente va a atender a 10 consultas de Instagram. Si funciona bien, voy a conectarlo con mi calendario de reservas. Si funciona mal, voy a agregar más respuestas sobre precios porque ahí se trabó."*

---

**Slides del ejercicio (6):**
1. "Ejercicio principal: Tu MVP en 30 min" (timer grande)
2. Fase 1: Plantilla de definición
3. Fase 2: Guarda-rails + checklist
4. Fase 3: "El test del suegro/a" - instrucciones
5. Timer de 10 min con música de tensión (opcional)
6. Fase 4: Compromiso público - template

---

### **BLOQUE 6: 🚀 CASOS DE LATINOAMÉRICA Y ESCALAMIENTO**
**Duración:** 30 min | **Slides:** 10

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Inspirar con casos reales de la región y dar hoja de ruta post-workshop |
| **Dinámica** | Charla con 2 demos rápidas + discusión grupal |

**Casos presentados (reales o realistas):**

| Startup | País | Qué hace el asistente | Herramienta | Resultado |
|---------|------|----------------------|-------------|-----------|
| **Kriptón** (crypto) | Argentina | Onboarding de usuarios primerizos, explica sin jerga | Voiceflow + WhatsApp | 40% menos tickets de soporte |
| **Luuna** (colchones) | México | Recomienda colchón según datos de sueño | Chatbase + quiz | 15% más conversión en web |
| **Ualá** (fintech) | Argentina | Resuelve "no me llegó la tarjeta" | Intercom Fin (híbrido) | Tiempo de respuesta: 2 horas → 2 min |
| **Tu empresa de X** | Tu país | Tu caso | Tu elección | Tu métrica |

**Demo rápida 1 (3 min):** Muestro un asistente que ya tiene 3 meses de datos, cómo se ve la mejora

**Demo rápida 2 (3 min):** Muestro un "antes y después" de prompts (cómo mejorar la calidad de respuestas)

**Discusión: "¿Qué te frena?" (10 min)**
- Post-its anónimos: cada uno escribe su mayor obstáculo
- Agrupo en pizarra: "No tengo datos", "Me da miedo que diga algo mal", "No sé si mis clientes lo usarían", etc.
- Resuelvo los 3 más comunes en 5 min cada uno

**Hoja de ruta post-workshop:**

| Semana | Hacer | No hacer |
|--------|-------|----------|
| 1 | Probar con 10 clientes reales, tomar notas | Intentar automatizar todo |
| 2 | Refinar las 5 preguntas más frecuentes | Agregar features nuevos |
| 3 | Medir: ¿cuántos resolvió solo? ¿cuántos escaló? | Cambiar de plataforma |
| 4 | Decidir: ¿escalo esto, o pruebo otro caso de uso? | Abandonar si hay un bug |

**Key takeaway:** *"Los mejores asistentes de IA en LatAm no son los más técnicos. Son los que más iteraron con clientes reales. Tu ventaja: estás acá, entendés el contexto, sabés que 'haceme una transferencia' en Argentina implica 7 pasos diferentes según el banco."*

**Slides (10):**
1. "¿Esto funciona en LATAM?" (título provocador)
2-5. Casos de éxito (uno por slide, con logo, foto de fundador si es público)
6. Demo: evolución de un asistente en 3 meses
7. Demo: antes/después de prompts
8. Actividad post-its: "¿Qué te frena?"
9. Hoja de ruta 4 semanas
10. "Tu superpoder: contexto local"

---

### **BLOQUE 7: 🎯 CIERRE, RECURSOS Y PRÓXIMOS PASOS**
**Duración:** 15 min | **Slides:** 5

| Aspecto | Detalle |
|---------|---------|
| **Objetivo** | Cerrar con energía, dar recursos concretos, crear comunidad |
| **Dinámica** | Charla + entrega física/virtual + foto grupal |

---

## 📦 5. RECURSOS PARA LLEVAR A CASA

### **Kit físico (entregar al final):**
```
📦 CAJA/ENVELOPE "MI ASISTENTE DE IA"

Contenido:
□ Tarjeta con QR al drive de recursos
□ Sticker del workshop (branding, recordatorio)
□ Checklist laminado: "¿Mi asistente está listo para salir?"
□ Template impreso: "Prompt perfecto para tu asistente"
□ 2 post-its: "Feature que quiero agregar" / "Bug que descubrí"
```

### **Drive digital (estructura):**

```
📁 CONSTRUYE TU ASISTENTE DE IA - RECURSOS
│
├── 📁 01-Plantillas listas para usar
│   ├── Plantilla-Chatbase-inicio.xlsx
│   ├── Plantilla-prompts-sistema.docx
│   ├── 10-ejemplos-de-instructions-para-IA.pdf
│   └── Comparativa-plataformas-2024.pdf
│
├── 📁 02-Video-guiados del workshop
│   ├── Bloque-2-fundamentos.mp4 (15 min)
│   ├── Bloque-4-construccion-paso-a-paso.mp4 (25 min)
│   └── Ejercicio-principal-completo.mp4 (20 min)
│
├── 📁 03-Casos-LatAm-extendidos
│   ├── Entrevista-founder-Kripton.mp3
│   ├── Entrevista-founder-Luuna.mp3
│   └── 15-casos-mas-sin-nombres.pdf (anónimos)
│
├── 📁 04-Comunidad
│   ├── Link-grupo-WhatsApp-workshop
│   ├── Calendario-office-hours-semanales
│   └── Formulario-para-1-a-1-con-facilitador
│
└── 📄 README-primeros-pasos.pdf
    (literally: "Abrí esto primero, tiene links a todo")
```

### **Acceso a comunidad:**
- Grupo de WhatsApp con nombre del workshop ("IA Startups - Marzo 2024")
- Reglas: solo recursos, no spam. Una pregunta técnica por día resuelta por facilitador.
- Office hours virtuales: martes 7pm (hora Buenos Aires/México), 30 min, sin agenda previa

---

## 📊 RESUMEN DE SLIDES

| Bloque | Slides | Acumulado |
|--------|--------|-----------|
| 1. Apertura | 8 | 8 |
| 2. Fundamentos | 14 | 22 |
| 3. Break | 0 | 22 |
| 4. Construcción | 12 | 34 |
| 5. Ejercicio principal | 6 | 40 |
| 6. Casos y escalamiento | 10 | 50 |
| 7. Cierre | 5 | **55** |

**Total estimado: 55 slides** (manejable, con muchas pantallas de demo que son básicamente screenshots con flechas)

---

## 💡 NOTAS DEL FACILITADOR (tips de ejecución)

| Situación | Qué hacer |
|-----------|-----------|
| **Se cae el WiFi** | Laptop de backup con todo offline + hotspot. Seguir con ejercicios en papel si es necesario. |
| **Alguien no tiene laptop** | Pareja con alguien que sí tenga, o uso mi laptop de demo para que configuren su cuenta. |
| **"Esto es muy básico"** | Ofrecer track avanzado: conectar con API real, o que ayude a otro participante (enseñar es aprender). |
| **"Esto es muy difícil"** | Voluntario va a su lado. Recordar: "El objetivo no es que sea perfecto, es que exista." |
| **Se acaba el tiempo** | Ejercicio principal NUNCA se recorta. Si hay que recortar, reducir casos de LatAm a 2 en vez de 4. |
| **Nadie quiere mostrar al final** | Yo muestro el mío, luego "¿alguien hizo algo similar pero diferente?" (pregunta más fácil). |

---

## 🎤 FRASES PARA REPETIR (branding del facilitador)

> *"En LatAm no tenemos el presupuesto de Silicon Valley. Tenemos algo mejor: la necesidad de resolver con lo que hay."*

> *"Tu primer asistente va a ser feo. El segundo, usable. El tercero, brillante. Empezá."*

> *"La IA no reemplaza al emprendedor. El emprendedor que usa IA reemplaza al que no."*

> *"Si tu abuela no entiende qué hace tu asistente, tu cliente tampoco."*

---

**¿Necesitás que desarrolle alguna sección con más profundidad?** Por ejemplo: los scripts exactos de la demo en vivo, el contenido del README, o variantes para audiencia más técnica. 🚀