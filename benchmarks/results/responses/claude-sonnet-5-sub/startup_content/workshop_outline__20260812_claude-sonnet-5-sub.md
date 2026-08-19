# Claude Sonnet 5 (suscripción) — startup_content/workshop_outline

- model_id: `claude-sonnet-5`
- success: True  | final: 7.88 | quality: 9.8
- latency_total: 100.011s | tokens_per_second: 80.6
- input_tokens: 2 | output_tokens: 8058
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que facilita la comprensión. Ofrece información práctica y útil para emprendedores no técnicos, aunque podría profundizar un poco más en ciertos aspectos técnicos.

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

# Workshop: "Construye tu Asistente de IA para tu Startup"
### Outline completo — 3 horas presencial · 20-30 emprendedores early-stage no-técnicos

---

## 1. Agenda detallada (180 min)

| Hora | Bloque | Duración |
|---|---|---|
| 0:00 – 0:15 | Bienvenida + Rompehielo + Expectativas | 15 min |
| 0:15 – 0:35 | Bloque 1 — Por qué un asistente de IA (no un chatbot más) | 20 min |
| 0:35 – 1:00 | Bloque 2 — Anatomía de un asistente (demo en vivo) | 25 min |
| 1:00 – 1:15 | Bloque 3 — Define tu caso de uso | 15 min |
| 1:15 – 1:25 | **Break** (café + red) | 10 min |
| 1:25 – 2:15 | Bloque 4 — EJERCICIO PRINCIPAL: construye tu asistente | 50 min |
| 2:15 – 2:35 | Bloque 5 — Prueba y refina en pares | 20 min |
| 2:35 – 2:50 | Bloque 6 — Show & Tell (voluntarios) | 15 min |
| 2:50 – 3:00 | Cierre + próximos pasos + recursos | 10 min |

**Regla de oro de timing:** el bloque 4 (ejercicio principal) NUNCA se recorta. Si algo se atrasa, se quita tiempo del Bloque 1 o 2, no del ejercicio — la gente vino a construir, no a escuchar.

---

## 2. Materiales necesarios (preparar antes)

### Del facilitador
- Laptop + adaptadores HDMI/USB-C + proyector probado el día anterior
- Slides con backup en USB (por si falla el laptop)
- **WiFi confirmado con capacidad para 30 dispositivos simultáneos** — punto crítico, avisar al venue con 48h de anticipación. Contraseña en slide grande, letra gigante, toda la sesión
- 1-2 cuentas demo pre-armadas (ChatGPT Plus o equivalente) para el demo en vivo del Bloque 2 — nunca improvisar el demo con cuenta nueva
- Link corto (bit.ly o QR) a: el Canvas del Asistente, la lista de herramientas, y el formulario de registro
- Cronómetro visible (proyectado o físico) para el ejercicio principal
- Plan B sin internet: versión impresa del Canvas del Asistente en papel, para que nadie se quede sin avanzar si el WiFi falla
- Música de fondo suave para el bloque hands-on (energiza sin distraer)
- 3-5 incentivos pequeños (merch, mes gratis de algo, lo que tengas a mano) para quienes compartan en el Show & Tell

### De los participantes (comunicar por email 3-4 días antes)
- Traer laptop cargado + cargador (obligatorio, no hay excepción)
- Crear cuenta gratuita en ChatGPT ANTES de llegar (el registro se hace en casa, no en el workshop — cada minuto configurando cuenta es un minuto menos construyendo)
- Si ya tienen ChatGPT Plus/Team, mejor — pueden crear GPTs personalizados en vivo
- **Tarea previa de 2 minutos:** llegar con una frase escrita respondiendo "¿Qué tarea repetitiva de mi startup me quita más tiempo?" — esto acelera el Bloque 3 enormemente

---

## 3. Detalle por bloque

### Bienvenida + Rompehielo (15 min)
- **Objetivo:** bajar la ansiedad de "esto es técnico y no voy a entender nada" y activar el grupo
- **Dinámica:** charla corta de encuadre + rompehielo en parejas ("cuéntale a tu vecino qué tarea de tu día odias hacer") + 1-2 respuestas en voz alta al grupo
- **Key takeaway:** *"Nadie acá va a programar. Si sabes explicarle una tarea a un empleado nuevo, ya sabes lo suficiente para construir esto."*

### Bloque 1 — Por qué un asistente de IA (20 min)
- **Objetivo:** que entiendan la diferencia entre "usar ChatGPT" y "tener un asistente configurado para SU negocio"
- **Dinámica:** charla con 3-4 ejemplos reales y concretos (atención al cliente 24/7, calificación de leads, onboarding de usuarios, respuestas a objeciones de venta) — cifras concretas de tiempo ahorrado, no promesas vagas
- **Key takeaway:** *"Un asistente configurado no es más inteligente que ChatGPT — sabe exactamente lo que tú le enseñaste sobre tu negocio, y responde igual todas las veces."*

### Bloque 2 — Anatomía de un asistente (demo en vivo) (25 min)
- **Objetivo:** desmitificar la "caja negra" mostrando que un asistente son solo 4 piezas
- **Dinámica:** demo en vivo construyendo un asistente desde cero delante del grupo (ej: "Asistente de soporte para una cafetería") — nombran las 4 piezas mientras las escriben: **Rol** (quién es) → **Tarea** (qué resuelve) → **Contexto** (qué sabe de ti) → **Tono** (cómo habla). Cierran probándolo con una pregunta real del público
- **Key takeaway:** *"Cuatro piezas. Nada más. Si puedes llenar esas cuatro, puedes construir un asistente."*

### Bloque 3 — Define tu caso de uso (15 min)
- **Objetivo:** que cada persona elija UN caso de uso concreto y realista (no "quiero automatizar todo mi negocio")
- **Dinámica:** ejercicio individual con el Canvas del Asistente — completan solo la primera mitad (Rol, Tarea, Para quién). Filtro clave: la tarea debe ser algo que hoy hacen manualmente, seguido y de forma repetitiva
- **Key takeaway:** *"El mejor primer asistente no es el más ambicioso, es el que resuelve algo que haces todos los días."*

### **Break (10 min)**
Café, agua, red entre participantes. No acortar — la gente necesita procesar antes del bloque intenso.

### Bloque 4 — EJERCICIO PRINCIPAL: construye tu asistente (50 min)
Ver detalle completo en sección 4.

### Bloque 5 — Prueba y refina en pares (20 min)
- **Objetivo:** que cada asistente se pruebe con ojos externos — el creador siempre tiene puntos ciegos
- **Dinámica:** se emparejan (con quien no hablaron aún), cada uno le hace 3 preguntas difíciles al asistente del otro, dan feedback de 1 minuto: "esto respondió bien / esto se sintió raro"
- **Key takeaway:** *"Tu asistente nunca está terminado en la primera versión — se afina probándolo con gente real, igual que un empleado nuevo."*

### Bloque 6 — Show & Tell (15 min)
- **Objetivo:** generar contagio de energía y mostrar variedad de casos de uso reales
- **Dinámica:** 3-4 voluntarios muestran su asistente en pantalla (60-90 seg cada uno) — el facilitador hace UNA pregunta en vivo al asistente de cada voluntario
- **Key takeaway:** *"Miren cuántos problemas distintos se resolvieron con el mismo método en la misma hora."*

### Cierre + próximos pasos (10 min)
- **Objetivo:** convertir el impulso del workshop en acción concreta las próximas 48h
- **Dinámica:** charla de cierre + entrega de recursos + compromiso público ("¿quién se compromete a mostrarle su asistente a un cliente real esta semana?" — levantan la mano)
- **Key takeaway:** *"Lo que construiste hoy es una versión 1. Úsalo esta semana con gente real — ahí es donde realmente aprende tu negocio."*

---

## 4. Ejercicio principal (Bloque 4, 50 min)

### "De la idea al asistente en producción"

**Formato:** trabajo individual con el Canvas del Asistente, en 3 tramos cronometrados y proyectados en pantalla.

| Tramo | Tiempo | Qué hacen |
|---|---|---|
| **Tramo 1 — Completar el Canvas** | 15 min | Terminan las 5 casillas: Rol · Tarea principal · Contexto (qué necesita saber sobre tu negocio) · Tono · 3 preguntas de prueba |
| **Tramo 2 — Escribir las instrucciones** | 20 min | Traducen el Canvas a instrucciones de texto plano (el "system prompt") usando la plantilla de frases guía proyectada. No hay código, solo redacción estructurada |
| **Tramo 3 — Montarlo y probarlo** | 15 min | Lo pegan en un GPT personalizado (o Proyecto de Claude) y le hacen las 3 preguntas que escribieron en el Canvas |

**Dos rutas según herramienta disponible** (anunciar al inicio del bloque):
- **Ruta A (con ChatGPT Plus/Team o Claude Pro):** crean el asistente real, en vivo, funcional al terminar el bloque
- **Ruta B (sin plan pago):** arman el mismo asistente como documento — "Blueprint" listo para pegar en cualquier chat de IA gratuita esa misma tarde. Nadie se queda sin construir algo funcional

**El facilitador circula todo el bloque** — este es el momento de mayor valor 1:1: resolver bloqueos, sugerir mejor redacción de tono, señalar cuando el caso de uso es demasiado ambicioso para una V1.

---

## 5. Recursos para llevar a casa

- **PDF/Google Doc — "Canvas del Asistente de IA"** (plantilla en blanco, reutilizable para el próximo asistente)
- **"10 instrucciones maestras" —** ejemplos ya redactados por función: ventas, soporte, onboarding, calificación de leads, contenido, cobranza
- **Lista curada de herramientas no-code** (5-7, con nivel de dificultad y costo): GPTs de ChatGPT, Proyectos de Claude, Voiceflow, Chatbase, Landbot, Botpress
- **Checklist "7 días: de la idea al asistente en producción"** — pasos concretos post-workshop (probar con 5 clientes reales, ajustar tono, medir tiempo ahorrado)
- Slides en PDF + grabación del workshop (si se grabó)
- Link a canal de comunidad (WhatsApp/Skool) para preguntas post-workshop y compartir resultados

---

## 6. Slide count estimado

| Sección | Slides |
|---|---|
| Bienvenida | 3-4 |
| Bloque 1 (contexto/charla) | 6-8 |
| Bloque 2 (demo en vivo — mínimas, la demo es la protagonista) | 4-5 |
| Bloque 3 (instrucciones ejercicio corto) | 2-3 |
| Break | 1 |
| Bloque 4 (instrucciones + plantilla de frases guía, proyectadas todo el bloque) | 4-6 |
| Bloque 5 (instrucciones pares) | 1-2 |
| Bloque 6 (transición, sin slides de contenido) | 1 |
| Cierre + recursos | 4-5 |
| **Total estimado** | **~28-35 slides** |

**Nota de diseño:** en los bloques hands-on (4, 5, 6) las slides son mínimas a propósito — la sala debe mirar sus laptops y al facilitador circulando, no una pantalla. El deck existe para dar estructura, no para leerse.