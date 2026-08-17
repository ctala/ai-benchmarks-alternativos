# MiniMax M2.7 (directo) — startup_content/workshop_outline

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.95 | quality: 8.94
- latency_total: 38.587s | tokens_per_second: 53.1
- input_tokens: 185 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

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

# Workshop: Construye tu Asistente de IA para tu Startup

## Guía Completa para el Facilitador

---

# 1. AGENDA DETALLADA (3 Horas)

| Bloque | Duración | Horario | Tipo |
|--------|----------|---------|------|
| **Apertura + Icebreaker** | 15 min | 0:00 - 0:15 | Dinámica grupal |
| **Conceptos Base** | 20 min | 0:15 - 0:35 | Charla interactiva |
| **Demo en Vivo** | 15 min | 0:35 - 0:50 | Demo |
| **Ejercicio: Mapeo de Oportunidades** | 20 min | 0:50 - 1:10 | Ejercicio individual |
| **Herramientas Sin Código** | 25 min | 1:10 - 1:35 | Charla + Demo |
| ☕ **Coffee Break** | 10 min | 1:35 - 1:45 | Networking |
| **EJERCICIO PRINCIPAL: Construye tu Prompt** | 30 min | 1:45 - 2:15 | Workshop hands-on |
| **Casos de Éxito LATAM** | 15 min | 2:15 - 2:30 | Charla |
| **Integración y Workflows** | 15 min | 2:30 - 2:45 | Charla + Demo |
| **Cierre + Recursos + Q&A** | 15 min | 2:45 - 3:00 | Grupal |

---

# 2. MATERIALES NECESARIOS (Preparar Antes)

## Materiales Físicos

- [ ] Proyector y pantalla o TV grande (compatible con HDMI)
- [ ] Micrófono inalámbrico (para workshops grandes)
- [ ] WiFi robusto (mínimo 50 Mbps dedicado, mejor 100 Mbps)
- [ ] Extensiones eléctricas y adaptadores (USB-C, HDMI)
- [ ] Papeletas post-it de 3 colores (rosa, amarillo, verde)
- [ ] Marcadores gruesos (1 por mesa, 8-10 mesas)
- [ ] Lonas/papeles grandes para grupos (8-10)
- [ ] Stickers o badges con nombres
- [ ] Botellas de agua para participantes
- [ ] Coffee break: café, agua, snacks ligeros

## Materiales Digitales (Enviar 1 día antes)

- [ ] Link a presentación en Google Slides/Canva (modo presentación)
- [ ] Carpeta compartida en Google Drive con:
  - Plantilla de ejercicio principal (ver sección 4)
  - Cheat sheet de prompts (1 página)
  - Lista de herramientas con comparativa
  - Guía de integración básica
  - Encuesta de feedback (Google Forms)

## Cuentas Preparadas (para Demo)

- [ ] ChatGPT Plus (o cuenta Pro) -睁开
- [ ] Claude.ai -睁开
- [ ] Notion AI (con workspace de demo)
- [ ] Zapier (cuenta gratuita con Zaps pre-hechos)
- [ ] Make.com (cuenta gratuita con escenarios de ejemplo)

## Setup del Espacio

- [ ] Mesas en formato "isla" (grupos de 3-4 personas)
- [ ] Sillas suficientes para 25-30 personas
- [ ] Nombre del workshop en entrada/pizarra
- [ ] Timer visible (proyectar cuenta regresiva en breaks)

---

# 3. BLOQUES DETALLADOS

---

## BLOQUE 1: Apertura + Icebreaker

**⏱️ Duración:** 15 minutos  
**🎯 Tipo:** Dinámica grupal

### Objetivo del Bloque

Crear energía inicial, romper el hielo entre participantes y establecer expectativas claras. Los emprendedores deben sentirse cómodos para participar, hacer preguntas y colaborar.

### Estructura de Tiempo

| Minuto | Actividad |
|--------|-----------|
| 0-2 | Bienvenida energética +自我介绍 rápido |
| 2-5 | **Dinámica "Dos verdades y una meta"** |
| 5-10 | Compartir en parejas + selección de 3-4 voluntarios |
| 10-15 | Presentación de la agenda + regla del taller |

### Dinámica: "Dos verdades y una meta"

**Instrucciones (léelas en voz alta):**

> *"Turnen con la persona al lado. Tienen 3 minutos. Cada uno comparte:*
>
> - *Dos verdades sobre tu startup (ej: 'Estamos en validación' + 'Ya tenemos 10 clientes pagados')*
> - *Una meta específica para hoy (ej: 'Quiero automatizar mi atención al cliente')*
>
> *Después de 3 minutos, voy a pedir que 3-4 compartan su meta en voz alta."*

### Key Takeaway

> *"En 3 horas vas a construir algo funcional. No necesitas saber programar. Solo necesitas saber qué problema quieres resolver."*

### Slides: 5-7 slides

| # | Contenido | Notas |
|---|-----------|-------|
| 1 | Portada: Logo + Nombre del workshop | Energía alta, colores brillantes |
| 2 | "¿Quién está aquí?" - Foto de la audiencia (opcional: collage de logos de startups) |  |
| 3 | "En 3 horas vas a..." (emoji bullets) |  |
| 4 | La regla #1: No hay preguntas tontas | Icono de manos levantadas |
| 5 | La regla #2: El teléfono es para practicar |  |
| 6 | Agenda visual (timeline horizontal) |  |
| 7 | "¿Listos? manos arriba →" |  |

---

## BLOQUE 2: Conceptos Base - ¿Qué es un Asistente de IA?

**⏱️ Duración:** 20 minutos  
**🎯 Tipo:** Charla interactiva

### Objetivo del Bloque

Demolición de mitos comunes ("la IA es mágica", "solo para tech"), explicación clara de qué es un LLM y cómo funciona en términos que un emprendedor entienda (como un empleado muy brillante pero sin contexto de tu negocio).

### Estructura de Tiempo

| Minuto | Actividad |
|--------|-----------|
| 0-5 | Pregunta: "¿Quién ha usado ChatGPT? ¿Qué pasó?" → Recopilar respuestas |
| 5-12 | Explicación: El modelo mental del "empleado brillante sin manual" |
| 12-18 | Demostración rápida: Mismo prompt → diferentes resultados |
| 18-20 | Resumen + anticipación del próximo bloque |

### Contenido Clave (Explicar con Analogías)

**El Modelo Mental del "Empleado Brillante Sin Manual":**

> *"Piénsalo así: La IA es como contratar a alguien超级 inteligente, que leyó TODO internet, pero que nunca ha trabajado en tu empresa. Si no le explicas cómo trabaja tu negocio, va a tomar decisiones basadas en su 'sentido común' de internet... y eso no siempre es tu sentido común."*

**Conceptos Clave:**

| Concepto | Analogía | Ejemplo |
|----------|----------|---------|
| **Prompt** | La instrucción que le das | "Escribe un email a mi cliente" |
| **Contexto** | El briefing completo | "Somos un SaaS de facturación para freelancers, el cliente se llama..." |
| **Fine-tuning** |