# Claude Opus 4.8 — startup_content/workshop_outline

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 7.19 | quality: 9.8
- latency_total: 29.482s | tokens_per_second: 69.5
- input_tokens: 314 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando una agenda detallada y materiales necesarios para un workshop de emprendimiento no técnico, con ejercicios prácticos e insights aplicables.

## Respuesta completa

# 🚀 Construye tu Asistente de IA para tu Startup
## Workshop Práctico - 3 Horas

> **Audiencia:** Emprendedores early-stage NO técnicos (20-30 personas)
> **Promesa:** Sales con un asistente de IA funcionando para tu startup. Hoy. Sin escribir código.

---

## 📋 MATERIALES NECESARIOS (Preparar ANTES)

### Para el facilitador
- [ ] Slides (ver conteo por sección abajo, ~45 slides total)
- [ ] Cuentas demo pre-creadas en ChatGPT, Claude y una plataforma no-code (ej. Botpress / Chatbase / Voiceflow)
- [ ] Proyector + audio + buen WiFi (¡crítico! confírmalo 2 veces)
- [ ] Extensión/multitoma para que la gente cargue laptops
- [ ] Timer visible en pantalla
- [ ] Plantilla del "Brief de Asistente" (impresa + digital)
- [ ] Casos de ejemplo locales (3 startups LATAM que usen IA)

### Para los participantes (comunicar 48h antes)
- [ ] **Laptop cargada** (no tablet, no celular como único equipo)
- [ ] Cuenta gratis de ChatGPT o Claude ya creada
- [ ] Su startup definida en 1 frase
- [ ] 3 preguntas que sus clientes hacen TODO el tiempo

### Pre-workshop (kit digital)
- [ ] Grupo de WhatsApp/Discord para el cohort
- [ ] Carpeta compartida con plantillas y links

---

## ⏱️ AGENDA DETALLADA (180 min)

| Hora | Bloque | Min |
|------|--------|-----|
| 0:00 | Bienvenida + Romper hielo | 15 |
| 0:15 | IA sin humo: qué sí y qué no | 25 |
| 0:40 | Demo en vivo: De cero a asistente | 20 |
| 1:00 | **EJERCICIO: Diseña tu asistente** | 30 |
| 1:30 | ☕ BREAK | 10 |
| 1:40 | Manos a la obra: Construcción guiada | 50 |
| 2:30 | Pruébalo y rómpelo | 20 |
| 2:50 | Show & Tell + cierre | 10 |

---

## 🧱 BLOQUES DETALLADOS

### BLOQUE 1 — Bienvenida + Romper hielo (15 min)
- **Objetivo:** Bajar la ansiedad ("yo no soy técnico") y crear energía de cohort.
- **Dinámica:** Charla corta + dinámica express. Cada quien dice en 10 seg: nombre, startup en 1 frase, y "la tarea aburrida que ojalá desaparezca".
- **Key takeaway:** *No necesitas ser ingeniero. Necesitas saber qué problema resolver.*
- **Slides:** 4

---

### BLOQUE 2 — IA sin humo: qué sí y qué no (25 min)
- **Objetivo:** Dar el modelo mental correcto sin tecnicismos.
- **Dinámica:** Charla energética con ejemplos reales LATAM + 2 mini-preguntas a mano alzada.
- **Contenido clave:**
  - Qué es un LLM (analogía: "becario brillante con amnesia")
  - 3 casos donde la IA brilla en una startup: soporte, ventas, operaciones
  - 3 casos donde NO la uses (decisiones legales, datos sensibles sin control, "que invente cifras")
  - Costo real: gratis vs pago (expectativas honestas)
- **Key takeaway:** *La IA no reemplaza tu criterio; multiplica tu tiempo en lo repetitivo.*
- **Slides:** 10

---

### BLOQUE 3 — Demo en vivo: De cero a asistente (20 min)
- **Objetivo:** Mostrar que es alcanzable HOY, en vivo, con errores incluidos.
- **Dinámica:** Demo en pantalla. El facilitador construye un asistente real frente a todos (ej. "Asistente de soporte para una cafetería de especialidad").
- **Qué mostrar:**
  - Escribir un buen prompt de sistema
  - Cargar info de la startup (FAQ, precios)
  - Probarlo en vivo y ajustarlo
- **Key takeaway:** *Un asistente útil = buenas instrucciones + buena información. Ya.*
- **Slides:** 3 (la demo manda)

---

### BLOQUE 4 — 🎯 EJERCICIO PRINCIPAL: Diseña tu asistente (30 min)
- **Objetivo:** Cada participante define QUÉ va a construir antes de tocar la herramienta.
- **Dinámica:** Trabajo individual (15 min) + parejas para feedback (15 min).
- **Herramienta:** "Brief de Asistente" (1 página). *Ver plantilla abajo.*
- **Key takeaway:** *El 80% del éxito está en el diseño, no en la herramienta.*
- **Slides:** 3

---

### ☕ BREAK (10 min)
*Música, networking, café. El facilitador circula resolviendo dudas 1:1.*

---

### BLOQUE 5 — Manos a la obra: Construcción guiada (50 min)
- **Objetivo:** Que CADA persona tenga un asistente funcionando.
- **Dinámica:** Construcción paso a paso en pantalla + cada quien replica. Facilitador + 2-3 asistentes circulando (asignar "buddies" técnicos si hay).
- **Pasos en pantalla:**
  1. Abrir herramienta (Custom GPT / Claude Project / Chatbase)
  