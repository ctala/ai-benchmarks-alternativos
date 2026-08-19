# MiMo V2.5-Pro (Xiaomi) — startup_content/workshop_outline

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.93 | quality: 9.52
- latency_total: 40.579s | tokens_per_second: 50.5
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🔥 WORKSHOP: "Construye tu Asistente de IA para tu Startup"
## Outline Completo — 3 Horas Presenciales

---

## 📋 1. AGENDA DETALLADA (180 minutos)

| Hora | Bloque | Duración | Tipo |
|------|--------|----------|------|
| 0:00-0:15 | Apertura + Icebreaker | 15 min | Interactivo |
| 0:15-0:35 | "¿Por qué tu startup NECESITA un asistente de IA?" | 20 min | Charla + Demo |
| 0:35-1:05 | El Framework C.R.E.A.: Define tu asistente | 30 min | Ejercicio individual |
| 1:05-1:15 | ☕ Break | 10 min | — |
| 1:15-1:35 | Herramientas sin código: El menú del día | 20 min | Demo en vivo |
| 1:35-2:25 | 🚀 EJERCICIO PRINCIPAL: Construye tu asistente | 50 min | Hands-on |
| 2:25-2:40 | Showcase: Muestra tu asistente | 15 min | Presentaciones |
| 2:40-2:55 | Escalando tu asistente + Errores comunes | 15 min | Charla + Discusión |
| 2:55-3:00 | Cierre + Recursos | 5 min | Wrap-up |

---

## 📦 2. MATERIALES NECESARIOS (Preparación Pre-Workshop)

### Para el facilitador:
- [ ] Proyector + pantalla
- [ ] Micrófono (si el espacio es grande)
- [ ] Laptop con acceso a ChatGPT, Poe, Botpress/Chatbase abiertos
- [ ] Cuenta demo/premium en una de las plataformas (para hacer demos sin límites)
- [ ] Conexión a internet estable (WiFi + hotspot de respaldo)
- [ ] Pizarra o rotafolio grande + marcadores de colores
- [ ] Timer visible (proyectado o físico)
- [ ] Playlist de música energética (para los ejercicios prácticos)

### Para cada participante:
- [ ] Laptop o tablet (confirmar con anticipación — tener 5 laptops de respaldo)
- [ ] Acceso a WiFi con credenciales impresas en tarjetas en cada mesa
- [ ] Workbook impreso (PDF que se envía 48h antes + copia física)
- [ ] Lápiz/bolígrafo
- [ ] Sticker para nombre (con su nombre + nombre de su startup)

### Kit de bienvenida en cada silla:
- [ ] Workbook de 8 páginas (diseñado con espacios para escribir)
- [ ] Tarjeta con links y contraseñas de WiFi
- [ ] Post-its de colores (3 colores)
- [ ] QR code → carpeta de Google Drive con todos los recursos

### Preparación digital:
- [ ] Template de "System Prompt" en Google Doc compartido
- [ ] Carpeta de Google Drive con: prompts de ejemplo, checklist, guía de herramientas
- [ ] Formulario de feedback (Google Forms) con QR
- [ ] Grupo de WhatsApp o Telegram para seguimiento post-workshop

---

## 📚 3. BLOQUES DETALLADOS

---

### BLOQUE 1: APERTURA + ICEBREAKER
**⏱ Duración:** 15 minutos
**🎯 Objetivo:** Crear energía, generar confianza y activar el cerebro de "hacer" en vez de "escuchar"

**🔧 Dinámica:** Interactiva grupal

**Contenido:**

**Minuto 0-3 — Bienvenida con impacto**
- El facilitador abre con una demo en vivo: le pregunta algo a un asistente de IA creado específicamente para el workshop y obtiene una respuesta sorprendente
- *"Esto que acaban de ver, en 3 horas ustedes van a saber cómo construirlo para SU startup"*

**Minuto 3-10 — Icebreaker: "El Pitch de 15 segundos"**
- Cada participante tiene 15 segundos para decir:
  1. Su nombre
  2. Su startup en una frase
  3. Una tarea odiosa de su día a día que desearían que alguien hiciera por ellos
- Dinámica tipo "fuego rápido" — el facilitador marca el ritmo con aplausos
- El facilitador va anotando en la pizarra las tareas que se repiten (servicio al cliente, emails, investigación de mercado, etc.)

**Minuto 10-15 — Encuadre**
- Reglas del workshop: "Hoy no hay preguntas tontas, todo se construye, nada se queda en teoría"
- Mencionar que al final tendrán algo FUNCIONANDO en sus manos
- Encuesta rápida con mano arriba: ¿quién ha usado ChatGPT? ¿quién ha intentado automatizar algo?

**📌 Key Takeaway:** *"La IA no es para empresas de Silicon Valley. Es para resolver los problemas que tú acabas de mencionar."*

**🖼 Slides estimadas:** 5 slides (portada, agenda visual, reglas, dato impactante, transición)

---

### BLOQUE 2: "¿POR QUÉ TU STARTUP NECESITA UN ASISTENTE DE IA?"
**⏱ Duración:** 20 minutos
**🎯 Objetivo:** Conectar la IA con problemas reales de startups early-stage y romper el mito de que "es muy técnico"

**🔧 Dinámica:** Charla interactiva + 2 demos en vivo

**Contenido:**

**Minuto 0-5 — El mito que necesitas romper**
- *"La gente piensa que IA = robots, millones de dólares y un equipo de ingenieros"*
- Realidad: un asistente de IA es un "empleado" que trabaja 24/7, no se enferma y cuesta $20/mes
- Datos concretos: startups en LATAM que están usando IA para escalar con equipo mínimo

**Minuto 5-12 — 3 Casos reales de startups LATAM**
- **Caso 1 — E-commerce:** Asistente de WhatsApp que responde preguntas de productos, hace recomendaciones y procesa pedidos → redujo 70% de tiempo del fundador en atención
- **Caso 2 — Servicios B2B:** Asistente que califica leads automáticamente y agenda demos → el fundador solo habla con clientes calificados
- **Caso 3 — Educación:** Tutor de IA que responde dudas de estudiantes 24/7 → escalaron de 50 a 500 estudiantes sin contratar más tutores
- Para cada caso: mostrar screenshot real o demo rápida

**Minuto 12-17 — Demo en vivo: "Mira lo que puedes construir"**
- El facilitador muestra un asistente de IA completo (pre-construido) para una startup ficticia
- Le hace preguntas reales frente al público
- Muestra el "backend" por 30 segundos: *"Miren, esto es todo. No hay código."*

**Minuto 17-20 — Framework mental**
- Dibujar en la pizarra: **TÚ → PROBLEMA → ASISTENTE DE IA → CLIENTE FELIZ**
- *"Un asistente de IA es un EMPLEADO con un manual de instrucciones. Hoy vamos a escribir ese manual."*

**📌 Key Takeaway:** *"Tu startup no necesita un equipo de IA. Necesita un asistente bien entrenado para UNA tarea específica."*

**🖼 Slides estimadas:** 8 slides (mitos vs realidad, 3 casos con fotos, framework, dato de cierre)

---

### BLOQUE 3: EL FRAMEWORK C.R.E.A. — DEFINE TU ASISTENTE
**⏱ Duración:** 30 minutos
**🎯 Objetivo:** Que cada participante defina con precisión QUÉ asistente necesita y CÓMO debe comportarse

**🔧 Dinámica:** Mini-charla (10 min) + Ejercicio individual guiado (20 min)

**Contenido:**

**Minuto 0-10 — Presentación del Framework C.R.E.A.**

El facilitador explica el framework en la pizarra/proyector:

```
C — CONTEXTO: ¿Quién