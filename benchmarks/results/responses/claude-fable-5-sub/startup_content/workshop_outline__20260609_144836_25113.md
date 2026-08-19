# Claude Fable 5 (suscripción) — startup_content/workshop_outline

- model_id: `claude-fable-5`
- success: True  | final: 7.18 | quality: 10.0
- latency_total: 73.56s | tokens_per_second: 63.0
- input_tokens: 2 | output_tokens: 4632

## Respuesta completa

# Construye tu Asistente de IA para tu Startup
## Workshop Práctico — 3 horas | 20-30 emprendedores early-stage no técnicos

**Premisa del workshop:** todos salen con un asistente de IA funcionando en su teléfono/laptop, configurado para SU startup. No teoría. No slides infinitos. Construir.

---

## 1. Agenda resumen (180 minutos)

| Hora | Bloque | Duración |
|---|---|---|
| 0:00 – 0:15 | Apertura: "Tu primer empleado cuesta $0" | 15 min |
| 0:15 – 0:35 | Demo en vivo: de cero a asistente en 10 minutos | 20 min |
| 0:35 – 0:55 | Los 4 ingredientes de un buen asistente | 20 min |
| 0:55 – 1:05 | **Break** | 10 min |
| 1:05 – 2:05 | **EJERCICIO PRINCIPAL: construye el tuyo** | 60 min |
| 2:05 – 2:30 | Show & Tell: 5 asistentes al escenario | 25 min |
| 2:30 – 2:50 | Qué sigue: de asistente a sistema | 20 min |
| 2:50 – 3:00 | Cierre + recursos + foto grupal | 10 min |

---

## 2. Materiales necesarios (preparar ANTES)

**Logística:**
- WiFi confiable y contraseña visible en pantalla y en cada mesa (esto mata más workshops que cualquier otra cosa — testear con 30 dispositivos simultáneos si es posible)
- Proyector + HDMI + adaptadores (USB-C y mini)
- Mesas en grupos de 4-5 personas, no auditorio
- Extensiones eléctricas por mesa

**Digital:**
- Cuenta de demo en la herramienta elegida (ChatGPT / Claude / Gemini — recomendación: usar la que tenga tier gratuito robusto y funcione bien en español)
- Link corto + QR a una página con todos los recursos (probarlo desde un celular el día anterior)
- Plantilla de prompt imprimible: 1 hoja por persona (sí, papel — los no técnicos escriben primero en papel y funciona)
- 3 ejemplos de asistentes ya configurados para mostrar (uno de e-commerce, uno de servicios, uno B2B)
- Formulario de feedback (QR al final)

**Plan B:**
- Hotspot móvil de respaldo
- Capturas de pantalla de la demo completa por si la herramienta se cae en vivo (pasa, y pasa siempre el día del workshop)

**Pre-workshop (enviar 48h antes):**
- Email: "Trae laptop o celular con batería, crea cuenta gratuita en [herramienta], piensa en la tarea que más odias hacer cada semana"

---

## 3. Bloques en detalle

### Bloque 1 — Apertura: "Tu primer empleado cuesta $0" (15 min)

- **Objetivo:** romper el miedo. Que entiendan que esto no requiere saber programar, y que en 3 horas se van con algo funcionando.
- **Dinámica:** charla + pregunta a la sala. Abrir con: "Levanten la mano los que pierden más de 5 horas a la semana en tareas repetitivas". Anotar en pizarra las 5 tareas más mencionadas (responder correos, cotizaciones, redes sociales, atención a clientes, propuestas). Esa lista se usa todo el workshop.
- **Key takeaway:** "La IA no reemplaza al fundador. Reemplaza las 10 horas semanales que el fundador gasta en tareas que odia."
- **Slides:** 5

### Bloque 2 — Demo en vivo: de cero a asistente en 10 minutos (20 min)

- **Objetivo:** que VEAN que es posible antes de explicarles cómo. La demo vende el ejercicio.
- **Dinámica:** demo en vivo, sin red de seguridad. Tomar UNA de las tareas que la sala mencionó en el bloque 1 y construir un asistente frente a ellos: instrucciones, contexto del negocio, primer prompt, iteración cuando la respuesta sale mal (importante mostrar el error — humaniza el proceso). Cerrar mostrando el asistente respondiendo desde el celular.
- **Key takeaway:** "Si lo viste en 10 minutos, lo puedes hacer en 60. La barrera no es técnica, es sentarse a hacerlo."
- **Slides:** 2 (la demo ES el contenido)

### Bloque 3 — Los 4 ingredientes de un buen asistente (20 min)

- **Objetivo:** darles el framework mínimo para que el ejercicio no sea prueba y error a ciegas.
- **Dinámica:** charla interactiva con ejemplos malos vs buenos en pantalla. Los 4 ingredientes:
  1. **Rol** — quién es el asistente ("eres el encargado de cotizaciones de una agencia de diseño")
  2. **Contexto** — qué sabe de tu negocio (productos, precios, tono, clientes)
  3. **Tarea** — qué hace exactamente, con ejemplos de input y output esperado
  4. **Reglas** — qué NUNCA debe hacer (inventar precios, prometer plazos, dar descuentos)
  
  Mostrar el mismo prompt sin ingredientes vs con los 4. La diferencia en la respuesta hace el punto solo.
- **Key takeaway:** "Un asistente genérico da respuestas genéricas. La calidad del asistente = la calidad del contexto que le diste."
- **Slides:** 8

### Break (10 min)
Música, café, y en pantalla: "Al volver, construyes el tuyo. Ve pensando: ¿cuál es la tarea que más odias?"

### Bloque 4 — EJERCICIO PRINCIPAL: construye tu asistente (60 min)

Ver sección 4 abajo en detalle.

- **Slides:** 3 (instrucciones del ejercicio + timer en pantalla)

### Bloque 5 — Show & Tell: 5 asistentes al escenario (25 min)

- **Objetivo:** validación social + aprendizaje cruzado. Ver lo que construyó alguien de otra industria genera más ideas que cualquier slide.
- **Dinámica:** 5 voluntarios pasan al frente, 4 minutos cada uno: muestran su asistente respondiendo en vivo, cuentan qué tarea resuelve y cuántas horas semanales les ahorra. El facilitador da 1 mejora concreta a cada uno (no 3 — una que puedan aplicar hoy).
- **Key takeaway:** "Hay 25 asistentes funcionando en esta sala que no existían hace una hora."
- **Slides:** 1

### Bloque 6 — Qué sigue: de asistente a sistema (20 min)

- **Objetivo:** mostrar el camino sin abrumar. Un asistente es el primer paso; el siguiente nivel es conectarlo a tus herramientas reales.
- **Dinámica:** charla + mini-demo rápida de un flujo automatizado (ej.: correo entra → asistente lo clasifica → respuesta en borrador). Mostrar, no construir. Mapa de madurez en 3 niveles:
  - **Nivel 1 (hoy):** asistente con contexto — $0
  - **Nivel 2 (próximo mes):** asistente conectado a tus datos reales — $0-20/mes
  - **Nivel 3 (cuando duela):** automatizaciones que corren solas, sin que tú estés — $20-50/mes
- **Key takeaway:** "No necesitas el nivel 3 hoy. Necesitas usar el nivel 1 todos los días durante 30 días."
- **Slides:** 7

### Bloque 7 — Cierre + recursos (10 min)

- **Objetivo:** compromiso concreto + canal para seguir.
- **Dinámica:** cada persona escribe en su hoja: "Esta semana mi asistente va a hacer ___ por mí". QR a recursos. Foto grupal.
- **Key takeaway:** "El asistente que construiste hoy vale $0 si no lo abres mañana. El reto: úsalo 5 días seguidos."
- **Slides:** 3

---

## 4. Ejercicio principal (60 min): "Tu Primer Empleado de IA"

**Consigna:** construye un asistente que resuelva LA tarea repetitiva que más tiempo te quita cada semana.

**Estructura del bloque:**

| Min | Fase |
|---|---|
| 0-10 | **Papel primero.** Cada uno llena la plantilla impresa: Rol / Contexto / Tarea / Reglas. Escribir antes de teclear evita la parálisis frente a la pantalla en blanco. |
| 10-15 | **Validación en mesa.** Le lees tu plantilla al de al lado. Si no entiende qué hace tu asistente en 30 segundos, la IA tampoco lo va a entender. |
| 15-40 | **Construcción.** Pasar la plantilla a la herramienta. Crear el asistente. Probarlo con un caso real de su negocio (un correo real, una consulta real de cliente). |
| 40-55 | **Iteración.** Regla de oro en pantalla: "Si la respuesta salió mal, no es que la IA sea tonta — le faltó contexto. Agrega un ejemplo de cómo SÍ quieres la respuesta y vuelve a probar." Mínimo 3 iteraciones. |
| 55-60 | **Prueba final.** Pedirle al compañero de mesa que le haga una pregunta difícil al asistente, como si fuera un cliente real. |

**Rol del facilitador:** circular entre mesas TODO el tiempo. Los no técnicos no levantan la mano — hay que ir a buscarlos. Tener 1 asistente de sala por cada 10-15 personas si es posible.

**Casos de respaldo** (para quien se bloquee): 3 plantillas pre-armadas — (a) asistente de respuestas a clientes, (b) generador de cotizaciones, (c) creador de posts para redes con la voz de tu marca.

---

## 5. Recursos para llevar a casa (página con QR)

1. **La plantilla de los 4 ingredientes** — versión digital editable, lista para copiar y pegar
2. **5 plantillas de asistentes pre-armadas** por tipo de negocio (e-commerce, servicios, B2B, restaurante/local, freelancer)
3. **Cheatsheet de iteración:** "10 frases para mejorar cualquier respuesta de la IA" (ej.: "hazlo más corto", "usa este ejemplo como referencia", "responde como le hablarías a un cliente molesto")
4. **El reto de 5 días:** un mini-plan diario para que el asistente se vuelva hábito (día 1: úsalo en un correo real; día 2: una cotización; etc.)
5. **Grabación de la demo del workshop** (grabar la pantalla durante el bloque 2)
6. **Lista de herramientas con precios reales** — qué es gratis, qué cuesta, y cuándo vale la pena pagar
7. **Canal de seguimiento** (comunidad/grupo) para compartir avances del reto de 5 días — aquí es donde el workshop genera relación de largo plazo

---

## 6. Slide count estimado

| Sección | Slides |
|---|---|
| Apertura | 5 |
| Demo en vivo | 2 |
| Los 4 ingredientes | 8 |
| Ejercicio (instrucciones + timer) | 3 |
| Show & Tell | 1 |
| De asistente a sistema | 7 |
| Cierre + recursos | 3 |
| **Total** | **29** |

29 slides para 3 horas. Correcto: la mayor parte del tiempo la pantalla muestra demos en vivo, el timer del ejercicio o los asistentes de los participantes. Si tu deck pasa de 40 slides para un workshop práctico, es una charla disfrazada de workshop.

---

## Notas finales para el facilitador

- **Métrica de éxito del workshop:** % de participantes que salen con un asistente funcionando y probado con un caso real. Meta: 90%+. No "satisfacción", no aplausos — asistentes funcionando.
- **El momento crítico es el minuto 15-40 del ejercicio.** Ahí se decide si el workshop fue transformador o entretenido. Toda tu energía de facilitación va ahí.
- **Trampa a evitar:** explicar cómo funciona la IA por dentro. A esta audiencia no le importa y los pierde. Funciona, úsala, punto.