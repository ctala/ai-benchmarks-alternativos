# Claude Fable 5 — startup_content/workshop_outline

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.83 | quality: 9.8
- latency_total: 32.589s | tokens_per_second: 62.8
- input_tokens: 314 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que se ajusta perfectamente a las necesidades de los emprendedores no técnicos, proporcionando un plan de taller práctico y útil.

## Respuesta completa

# 🚀 Construye tu Asistente de IA para tu Startup
## Workshop Práctico — Outline Completo del Facilitador

**Duración:** 3 horas (180 min)
**Audiencia:** 20-30 emprendedores early-stage, no-técnicos
**Formato:** Presencial, hands-on (laptop obligatoria)
**Promesa del workshop:** *"Sales de aquí con un asistente de IA funcionando para TU startup. No teoría. No humo. Algo que uses mañana."*

---

## 📋 1. AGENDA GENERAL (vista rápida)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 – 0:15 | Bienvenida + Icebreaker "El dolor de tu semana" | 15 min |
| 0:15 – 0:35 | Bloque 1: IA sin humo — Qué es y qué NO es | 20 min |
| 0:35 – 1:00 | Bloque 2: Anatomía de un buen prompt (demo en vivo) | 25 min |
| 1:00 – 1:15 | Bloque 3: Elige tu caso de uso (mini-ejercicio) | 15 min |
| 1:15 – 1:25 | ☕ BREAK | 10 min |
| 1:25 – 2:25 | Bloque 4: EJERCICIO PRINCIPAL — Construye tu asistente | 60 min |
| 2:25 – 2:45 | Bloque 5: Demo Day relámpago | 20 min |
| 2:45 – 3:00 | Cierre: Roadmap de 30 días + recursos | 15 min |

---

## 🎒 2. MATERIALES NECESARIOS (preparar ANTES)

### Logística del espacio
- [ ] Mesas en formato "islas" de 4-5 personas (facilita peer support)
- [ ] WiFi confiable + contraseña visible en pantalla y en cada mesa
- [ ] Proyector/pantalla grande + adaptadores HDMI/USB-C
- [ ] Extensiones eléctricas en cada mesa (laptops = baterías que mueren)
- [ ] Música de entrada (energía alta al llegar)

### Materiales impresos (1 por participante)
- [ ] **"Plantilla de Asistente"** — hoja de trabajo con los 6 componentes del prompt (el corazón del workshop)
- [ ] **Cheat sheet de prompting** — 1 página, laminada si el presupuesto da
- [ ] Post-its (3 colores) + marcadores por mesa
- [ ] Sticker/badge divertido para el Demo Day ("Founder + AI 🤖")

### Preparación digital
- [ ] Verificar que ChatGPT / Claude / Gemini funcionen en la red del venue
- [ ] Email pre-workshop: "Trae laptop + crea cuenta gratuita en [herramienta] ANTES de llegar" (esto salva 20 minutos de caos)
- [ ] Cuentas de respaldo listas por si alguien llega sin cuenta
- [ ] QR code gigante con link a recursos descargables
- [ ] 3 asistentes de ejemplo pre-construidos para la demo (uno de e-commerce, uno de servicios, uno B2B — que resuenen con el ecosistema local)
- [ ] Timer visible en pantalla para los ejercicios

### Equipo humano
- [ ] Ideal: 1-2 co-facilitadores o voluntarios "flotantes" para apoyar mesas durante el ejercicio (ratio 1:15)

---

## 🎯 3. BLOQUES DETALLADOS

---

### 🎬 BLOQUE 0: Bienvenida + Icebreaker "El dolor de tu semana" (15 min)

**Objetivo:** Romper el hielo, bajar la ansiedad de los no-técnicos y conectar la IA con dolores REALES de sus negocios desde el minuto uno.

**Dinámica:**
- (5 min) Bienvenida energética. Regla de oro del workshop: *"Aquí no hay preguntas tontas, hay founders que quieren aprender."*
- (7 min) Icebreaker en mesas: cada persona escribe en un post-it **la tarea más repetitiva y molesta de su semana como founder** (responder mensajes, escribir posts, cotizar, hacer follow-up...). Los pegan en la pared de "Dolores".
- (3 min) Facilitador lee 4-5 en voz alta: *"Todo esto que está en la pared... hoy le vamos a meter IA."*

**Key takeaway:** Este workshop no es sobre tecnología. Es sobre recuperar tus horas.

**Slides:** 4

---

### 🧠 BLOQUE 1: IA sin humo — Qué es y qué NO es (20 min)

**Objetivo:** Nivelar conceptos básicos sin tecnicismos. Destruir mitos ("me va a reemplazar", "necesito saber programar", "es solo para techies").

**Dinámica:**
- Charla dinámica con analogías locales y humor. Ejemplo: *"Un LLM es como el mejor practicante del mundo: sabe de todo, trabaja 24/7, pero necesita instrucciones CLARAS o hace cualquier cosa."*
- Mini-quiz interactivo a mano alzada: "¿Verdadero o falso?" (3 preguntas sobre mitos de IA)
- Mapa simple: qué herramienta sirve para qué (ChatGPT, Claude, Gemini — sin guerra de marcas, todas sirven para hoy