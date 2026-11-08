# DeepSeek V4 Flash 0731 — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.99 | quality: 9.72
- latency_total: 15.923s | tokens_per_second: 226.6
- input_tokens: 199 | output_tokens: 3609
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

# 🚀 Construye tu Asistente de IA para tu Startup - Workshop Práctico

## Outline Completo (3 horas)

---

## 📋 MATERIALES NECESARIOS (PREPARACIÓN PREVIA)

### Para el facilitador:
- [ ] Laptop con adaptador HDMI + backup USB
- [ ] Presentación PPT/Canva (60 slides aprox.)
- [ ] WiFi robusto (testear velocidad antes)
- [ ] Cuenta demo de ChatGPT Plus, Claude, y una herramienta no-code (Zapier/Make)
- [ ] Playlist de música energética para breaks
- [ ] Stickers o premios pequeños para participación
- [ ] QR code impreso para recursos digitales

### Para participantes:
- [ ] Laptop (o tablets con teclado) - *avisar con 1 semana de anticipación*
- [ ] Cuenta gratuita de ChatGPT (crear antes del workshop)
- [ ] Cuenta gratuita de Zapier o Make (crear antes)
- [ ] Block de notas + plumas (backup si falla tecnología)
- [ ] **Impresos:** Template de "Mapa de Tareas" (1 por persona)

### Setup del espacio:
- [ ] Mesas en grupos de 4-5 personas
- [ ] Flipchart + marcadores
- [ ] Post-its de colores
- [ ] Proyector + parlantes
- [ ] Agua y snacks en mesa lateral

---

## 🗓️ AGENDA DETALLADA

---

### BLOQUE 1: DESPERTANDO AL CURIOSO (0:00 - 0:30)
**Título:** "Tu Startup + IA = Superpoderes" 
**Duración:** 30 minutos

**Objetivo:** Romper el hielo, desmitificar la IA y crear expectativa sobre lo que van a construir.

**Dinámica:**
- **Ice-breaker (10 min):** "Dos verdades y una mentira sobre IA" - Cada participante escribe 2 verdades y 1 mentira sobre IA en post-its. Los leen al grupo y votan cuál es la mentira. Premio con stickers.
- **Charla corta (15 min):** Presentación energética con ejemplos reales de startups LATAM usando IA:
  - *Ejemplo:* Una tienda de ropa en CDMX que usa IA para responder WhatsApp
  - *Ejemplo:* Un food truck en Bogotá que automatiza pedidos por Instagram
  - *Ejemplo:* Una consultora en Buenos Aires que genera propuestas comerciales en 5 minutos
- **Demo rápida (5 min):** Mostrar en vivo cómo un asistente de IA responde preguntas de clientes para un negocio ficticio de ejemplo ("Café con Causa").

**Key Takeaway:** "La IA no es magia, es una herramienta que cualquier emprendedor puede usar HOY para ahorrar horas semanales. No necesitas saber programar."

**Slide count:** 10 slides

---

### BLOQUE 2: EL MAPA DE TAREAS (0:30 - 1:00)
**Título:** "¿Qué tareas puedes delegar a tu Asistente IA?"
**Duración:** 30 minutos

**Objetivo:** Que cada participante identifique 3-5 tareas repetitivas en su negocio que puede automatizar con IA.

**Dinámica:**
- **Mini-charla (10 min):** Marco simple de las 4 categorías de tareas delegables:
  1. 📞 Atención al cliente (FAQ, respuestas, seguimiento)
  2. 📝 Contenido (posts, emails, propuestas)
  3. 📊 Datos (resúmenes, reportes, análisis)
  4. 🔄 Procesos (recordatorios, agendamiento, facturación)
  
  *Ejemplos concretos para cada una.*

- **Ejercicio individual (15 min):** Cada participante usa el **Template de "Mapa de Tareas"** (impreso):
  - Columna 1: Tarea que odian hacer
  - Columna 2: Tiempo semanal que le dedican
  - Columna 3: ¿Podría una IA hacerla? (Sí/No/Parcial)
  - Columna 4: Nivel de impacto (1-5)
  
- **Compartir en parejas (5 min):** Cada persona comparte su tarea #1 con su compañero de mesa. El compañero da feedback rápido.

**Key Takeaway:** "Tu asistente IA no reemplaza tu trabajo - reemplaza las tareas que te roban tiempo. Empieza por las que más te frustran."

**Slide count:** 8 slides

---

### 🍩 BREAK (1:00 - 1:15) - 15 minutos
*Música energética + snacks*

---

### BLOQUE 3: CONSTRUYENDO TU ASISTENTE (1:15 - 2:15)
**Título:** "El Ejercicio Principal: Tu Primer Asistente de IA"
**Duración:** 60 minutos (el corazón del workshop)

**Objetivo:** Que cada participante construya un prototipo funcional de asistente IA para su startup.

**Dinámica:**
- **Demo guiada (10 min):** El facilitador muestra paso a paso cómo crear un asistente de atención al cliente para el negocio ficticio "Café con Causa":
  1. Definir el "personaje" del asistente (tono, estilo, límites)
  2. Crear el prompt base con instrucciones específicas
  3. Probar con 3 preguntas de ejemplo
  4. Ajustar según respuestas

- **Ejercicio individual guiado (40 min):** Cada participante construye SU asistente:
  
  **PASO 1 (5 min):** Definir el rol y personalidad de su asistente
  - *Template:* "Eres [nombre], el asistente virtual de [negocio]. Tu tono es [amigable/profesional/divertido]. Conoces todos los detalles sobre [producto/servicio]."
  
  **PASO 2 (10 min):** Agregar conocimiento del negocio
  - Escribir: qué venden, precios, horario, políticas, FAQ
  - *Tip:* "Pega tu info real - el asistente es tan bueno como la información que le des"
  
  **PASO 3 (10 min):** Definir límites y escalamiento
  - Qué puede responder solo vs. cuándo debe derivar a humano
  - *Template:* "Si el cliente pregunta sobre [tema complejo], responde: 'Un asesor te contactará'"
  
  **PASO 4 (15 min):** Probar y refinar
  - Probar 5 preguntas difíciles que les han hecho clientes reales
  - Iterar: ajustar prompt según respuestas débiles

- **Circulación del facilitador (durante todo el ejercicio):** El facilitador y co-facilitador circulan ayudando individualmente.

**Key Takeaway:** "En 40 minutos puedes crear un asistente que responde como tú. El secreto está en el prompt: sé específico, dale contexto y define límites claros."

**Slide count:** 15 slides (más template de trabajo)

---

### BLOQUE 4: CONECTANDO CON EL MUNDO REAL (2:15 - 2:40)
**Título:** "De Chat a Canal: Conectando tu Asistente con tus Clientes"
**Duración:** 25 minutos

**Objetivo:** Mostrar cómo llevar el asistente del laboratorio a WhatsApp, Instagram o tu web.

**Dinámica:**
- **Demo rápida (10 min):** El facilitador muestra 3 opciones de conexión:
  1. **Opción Simple (5 min):** Compartir link de ChatGPT personalizado
  2. **Opción No-Code (10 min):** Conectar con Zapier/Make para responder en Google Sheets o email automáticamente
  3. **Opción Avanzada (mencionar):** Herramientas como Chatbase, Voiceflow o ManyChat para WhatsApp

- **Discusión grupal (10 min):** 
  - ¿Qué canal usa más tu startup? (WhatsApp, Instagram, web, email)
  - ¿Cuál sería el flujo ideal? (cliente → canal → asistente → respuesta)
  - Escribir en flipchart los 3 canales más populares del grupo

- **Mini-ejercicio (5 min):** Cada participante escribe en un post-it:
  - "Mi asistente estará en [canal]"
  - "Para resolver [tarea principal]"
  - Pegan en flipchart para compartir

**Key Takeaway:** "Un asistente en un documento no sirve. Conectado a tu canal de comunicación, es tu empleado 24/7."

**Slide count:** 10 slides

---

### BLOQUE 5: PLAN DE ACCIÓN Y CIERRE (2:40 - 3:00)
**Título:** "De Workshop a Realidad: Tu Plan de 7 Días"
**Duración:** 20 minutos

**Objetivo:** Convertir el aprendizaje en acciones concretas para la próxima semana.

**Dinámica:**
- **Charla corta (7 min):** "El Plan de 7 Días" para implementar su asistente:
  - Día 1-2: Refinar el prompt con feedback de 2 amigos
  - Día 3-4: Probar con 5 clientes reales (preguntar feedback)
  - Día 5: Iterar según feedback
  - Día 6-7: Conectar al canal principal (o planificar cómo)

- **Ejercicio de compromiso (5 min):** Cada participante escribe en un post-it:
  - "Esta semana voy a: ________"
  - "Mi asistente se llamará: ________"
  - Pegan en la "Pared de Compromisos" (flipchart)

- **Recursos y cierre (5 min):** 
  - QR para descargar recursos (ver sección 6)
  - Invitación a comunidad/WhatsApp group
  - Foto grupal + cierre energético
  - "Si solo recuerdas una cosa de hoy: tu asistente IA no es un lujo, es tu primer empleado 24/7."

- **Feedback rápido (3 min):** Post-it verde (me gustó), amarillo (mejoraría), rosa (me llevo)

**Key Takeaway:** "El workshop termina hoy, pero tu asistente empieza a trabajar esta semana. La diferencia entre tener una idea y tener un resultado es la ejecución."

**Slide count:** 8 slides

---

## 🎯 EJERCICIO PRINCIPAL: "Mi Primer Asistente IA" (Detalle)

**Tiempo:** 40 minutos
**Formato:** Individual (con apoyo del facilitador)

### Instrucciones paso a paso:

**PASO 1: Define tu asistente (5 min)**
Escribe en tu template:
```
Nombre del asistente: ______
Negocio: ______
Tono de voz: ( ) Amigable ( ) Profesional ( ) Divertido ( ) Formal
Rol principal: ( ) Atención al cliente ( ) Ventas ( ) Soporte ( ) Otro
```

**PASO 2: Alimenta el conocimiento (10 min)**
Escribe la información clave que tu asistente necesita:
- ¿Qué vendes/ofreces?
- ¿Cuáles son tus precios?
- ¿Cuál es tu horario?
- ¿Cuál es tu política de entregas/devoluciones?
- 3 preguntas frecuentes de tus clientes

**PASO 3: Define límites (10 min)**
- ¿Qué puede responder solo? 
- ¿Qué necesita derivar a humano?
- Escribe 2 respuestas de "derivación" que usaría

**PASO 4: Construye el prompt (10 min)**
Usando esta plantilla:

```
ERES [nombre], el asistente virtual de [negocio].
TU TONO es [tono].
CONOCES esta información sobre el negocio:
[pegar info del paso 2]

REGLAS:
1. Responde amablemente siempre
2. Si te preguntan sobre [tema límite], responde: "[respuesta derivación]"
3. Si no sabes, di: "Déjame verificar y te confirmo"
4. Nunca inventes información que no esté en tus datos

COMENZAR: Saluda y pregunta cómo puedes ayudar.
```

**PASO 5: Prueba y refina (5 min)**
- Copia el prompt en ChatGPT
- Prueba con 3 preguntas que te hagan clientes reales
- Ajusta el prompt según respuestas débiles

**ENTREGABLE:** Cada participante se va con su prompt guardado y probado.

---

## 📦 RECURSOS PARA LLEVAR A CASA (QR Code)

### Digitales:
1. **Template del "Mapa de Tareas"** (Google Sheets editable)
2. **Template del Prompt** (Google Doc editable)
3. **Guía de prompts avanzados** (PDF con 20 ejemplos por industria)
4. **Video tutorial:** "Cómo conectar tu asistente a WhatsApp" (10 min)
5. **Lista de herramientas** con precios y pros/contras:
   - ChatGPT Plus ($20/mes)
   - Claude Pro ($20/mes)
   - Chatbase (desde $15/mes)
   - Voiceflow (freemium)
   - ManyChat (freemium)
   - Zapier/Make (freemium)
6. **Checklist de implementación en 7 días** (PDF imprimible)
7. **Plantilla de email** para anunciar tu asistente a clientes
8. **Comunidad privada** (WhatsApp/Telegram) para seguimiento

### Físicos:
- Template "Mapa de Tareas" impreso
- Stickers de "IA Builder" para los que completaron el ejercicio
- Tarjeta con QR code para recursos

---

## 📊 RESUMEN DE SLIDES

| Sección | Slides | Tiempo |
|---------|--------|--------|
| Bloque 1: Despertando al curioso | 10 | 30 min |
| Bloque 2: Mapa de tareas | 8 | 30 min |
| Bloque 3: Construyendo tu asistente | 15 | 60 min |
| Bloque 4: Conectando con el mundo real | 10 | 25 min |
| Bloque 5: Plan de acción | 8 | 20 min |
| **Total** | **~51 slides** | **3 horas** |

---

## ⚡ TIPS PARA EL FACILITADOR

1. **Energía:** Cambia de posición cada 10 minutos, usa historias personales de emprendedores LATAM, celebra cada pequeña victoria con aplausos.

2. **Manejo de tiempos:** Pon alarmas visibles. Si el ejercicio principal se pasa, recorta el bloque 4 (la demo puede ser más corta).

3. **Audiencia no-técnica:** Evita jerga. Cada término técnico (API, prompt, automatización) se explica con analogía del mundo emprendedor.

4. **Fallos técnicos:** Ten plan B: si el WiFi falla, el ejercicio principal se hace en papel (escriben el prompt a mano) y se prueban en casa.

5. **Niveles diferentes:** Ten "retos extra" para los que avanzan rápido (ej. agregar 3 variaciones de tono al asistente).

6. **Cierre memorable:** Termina con una historia inspiradora de un emprendedor LATAM que transformó su negocio con IA.

---

*"La mejor inversión de 3 horas que harás esta semana es construir tu ventaja competitiva."*

¡Éxito con tu workshop! 🚀