# Nemotron 3 Ultra 550B — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 59.804s | tokens_per_second: 102.7
- input_tokens: 206 | output_tokens: 6140
- judge_score: 5.0 | justificación: 

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

# 🚀 OUTLINE COMPLETO: "Construye tu Asistente de IA para tu Startup"
## Workshop Presencial · 3 Horas · 20-30 Emprendedores No-Técnicos

---

## 📋 AGENDA GENERAL (3 HORAS)

| Bloque | Tiempo | Duración | Tipo |
|--------|--------|----------|------|
| **0. Check-in & Café** | 0:00 - 0:15 | 15 min | Networking |
| **1. Mentalidad: IA como Co-founder, no Herramienta** | 0:15 - 0:45 | 30 min | Charla + Demo vivo |
| **2. Anatomía de un Asistente que Sirve (Prompt Engineering Real)** | 0:45 - 1:30 | 45 min | Ejercicio guiado |
| **3. ☕ BREAK + Preguntas rápidas** | 1:30 - 1:40 | 10 min | — |
| **4. MANOS A LA OBRA: Construye tu Asistente (Ejercicio Principal)** | 1:40 - 2:40 | 60 min | Workshop hands-on |
| **5. Stress-test & Iteración: "Rómpelo antes que tu cliente"** | 2:40 - 2:55 | 15 min | Ejercicio en parejas |
| **6. Despliegue Express: De notebook a producción en 5 min** | 2:55 - 3:00 | 5 min | Demo relámpago |
| **7. Cierre: Próximos pasos + Foto grupal + QR recursos** | 3:00 - 3:10 | 10 min | Cierre energético |

---

## 🎒 MATERIALES NECESARIOS (PREPARAR ANTES)

### **Facilitador (tú)**
- [ ] Laptop + cargador + **adaptador HDMI/USB-C**
- [ ] Clicker presentación
- [ ] **Cuenta Pro verificada** en: ChatGPT, Claude, y (opcional) Poe/Perplexity
- [ ] **Proyecto demo listo** en Replit / Streamlit / Gradio (ver Sección 6)
- [ ] Hotspot móvil (backup WiFi)
- [ ] Timer visible (teléfono en modo avión + cronómetro grande)

### **Por Participante (comunicar en email previo)**
- [ ] **Laptop cargada** (no tablet, no celular)
- [ ] Cuenta creada en **ChatGPT (gratis ok)** y **Claude (gratis ok)**
- [ ] Navegador Chrome/Edge actualizado
- [ ] **1 problema real de su startup** escrito en 3 líneas máx (ver template pre-work)

### **Físicos en Sala**
- [ ] **Post-its** (3 colores: problema / solución / métrica)
- [ ] **Rotuladores gruesos** (negro, rojo, verde) × 30
- [ ] **Hojas A3** impresas con "Canvas del Asistente" (ver Anexo A) × 35
- [ ] **Checklist de testing** impreso (Anexo B) × 35
- [ ] Stickers divertidos ("Lo rompí", "Funciona", "MVP listo") × 50
- [ ] Agua + café + galletas (energía = engagement)

### **Digitales (compartir por QR al inicio)**
- [ ] Deck en Notion/Google Slides (link corto: `bit.ly/ia-startup-ws`)
- [ ] Canvas digital (Miro/FigJam duplicable)
- [ ] Prompt library starter (Notion page)
- [ ] Repo GitHub con template deploy (ver Sección 6)

---

## 🧱 BLOQUES DETALLADOS

---

### **BLOQUE 0: CHECK-IN & CAFÉ** (15 min)
| | |
|---|---|
| **Objetivo** | Romper hielo, detectar nivel real, crear energía de "tribu" |
| **Dinámica** | **Speed-networking 2×2**: "Nombre, startup en 5 palabras, 1 tarea que odias hacer hoy" |
| **Key Takeaway** | *"Todos estamos ahogados en lo mismo. La IA no es magia, es palanca."* |
| **Slides** | 2 (Welcome + Instrucciones speed-networking) |

> 💡 **Tip facilitador**: Camina, escucha, anota dolores reales en post-it gigante visible. Úsalos después como ejemplos.

---

### **BLOQUE 1: MENTALIDAD — IA COMO CO-FOUNDER** (30 min)
| | |
|---|---|
| **Título** | *"Deja de hacer prompts. Empieza a delegar."* |
| **Objetivo** | Cambiar mindset: prompt ≠ asistente. Asistente = contexto + instrucciones + herramientas + memoria |
| **Dinámica** | **Charla 12 min + Demo vivo 15 min + Q&A 3 min** |
| **Demo Vivo** | Muestra **dos versiones** del mismo request:<br>1. Prompt suelto: *"Escribe email venta"* → resultado genérico<br>2. Asistente configurado: *"Eres VP Sales SaaS B2B, tono consultivo, conoce mi ICP, usa framework PAS..."* → resultado usable |
| **Key Takeaway** | **Un asistente = System Prompt + Contexto fijo + Instrucciones de estilo + Ejemplos (few-shot) + Acceso a tools.** No es un chat. Es un empleado digital. |
| **Slides** | 8 (Concepto → Comparativa → Anatomía 5 partes → Casos reales LATAM → "Tu turno") |

> 🎯 **Frase ancla**: *"Si no le darías este brief a un pasante, no se lo des a la IA."*

---

### **BLOQUE 2: ANATOMÍA DE UN ASISTENTE QUE SIRVE** (45 min)
| | |
|---|---|
| **Título** | *"Prompt Engineering para no-técnicos: El Framework CO-STAR"* |
| **Objetivo** | Dar estructura repetible para escribir system prompts que funcionan |
| **Dinámica** | **Ejercicio guiado paso a paso** (todos abren ChatGPT/Claude en vivo) |
| **Framework CO-STAR** (adaptado de Sheila Teo) | **C**ontexto (quién eres, startup, stage)<br>**O**bjetivo (qué debe lograr el asistente)<br>**S**tyle (tono, formato, restricciones)<br>**T**ools (qué puede usar: web, code, files, APIs)<br>**A**ctions (flujos: "si usuario pide X, haz Y")<br>**R**esponse format (JSON, markdown, bullets, email listo para enviar) |
| **Ejercicio Guiado** (35 min) | 1. **Min 0-5**: Cada uno escribe su **Contexto** en Canvas A3 (5 min)<br>2. **Min 5-15**: Definen **Objetivo único** del asistente (ej: "Redactar emails fríos que abran >40%")<br>3. **Min 15-30**: Rellenan Style + Tools + Actions + Response format<br>4. **Min 30-40**: Copian system prompt → pegan en **Custom Instructions** (ChatGPT) o **Projects** (Claude)<br>5. **Min 40-45**: **Prueba de fuego**: piden 1 output real. Ajustan en vivo. |
| **Key Takeaway** | **CO-STAR = checklist mental.** Si falta una pieza, el asistente alucina. Completalo y tendrás consistencia. |
| **Slides** | 12 (Framework → Ejemplo real paso a paso → Errores comunes → "Tu Canvas") |

> ⚡ **Truco facilitador**: Ten listo un **system prompt ejemplo completo** en slide para copiar/pegar. Ahorra 10 min de tipeo.

---

### **BLOQUE 3: BREAK** (10 min)
- Música suave, post-its en pared: *"¿Qué parte te cuesta más?"* → agrupar para abordar en Bloque 4.

---

### **BLOQUE 4: MANOS A LA OBRA — EJERCICIO PRINCIPAL** (60 min) ⭐
| | |
|---|---|
| **Título** | **Construye TU Asistente: El que usarás mañana en tu startup** |
| **Objetivo** | Cada participante sale con **un asistente funcional, probado y desplegable** para un caso real propio |
| **Dinámica** | **Workshop hands-on** (tú facilitas, ellos construyen, mentores/asistentes rotan ayudando) |

#### **ESTRUCTURA DEL EJERCICIO PRINCIPAL**

| Fase | Tiempo | Qué Hace el Participante | Qué Haces Tú |
|------|--------|--------------------------|--------------|
| **4.1 Elección del Caso** | 5 min | Elige **UNO** de su pre-work (ver abajo). Lo escribe en Canvas A3. | Proyectas 4 arquetipos comunes para inspirar (ver abajo). |
| **4.2 System Prompt Completo** | 20 min | Rellena CO-STAR completo en Canvas → copia a Custom Instructions / Project. | Recorres mesas. Preguntas: *"¿Este asistente sabe tu ICP? ¿Sabe qué NO hacer?"* |
| **4.3 Few-Shot: 3 Ejemplos Reales** | 15 min | Pega 3 pares **Input → Output ideal** (emails reales, posts reales, respuestas reales). | Demuestra en pantalla: *"Así enseño a mi asistente de contenido"* |
| **4.4 Test & Ajuste** | 15 min | Lanza 5 prompts de prueba variados. Anota fallos en Checklist (Anexo B). Itera system prompt. | Anuncia: *"Quedan 10 min. Objetivo: 3/5 outputs usables sin editar."* |
| **4.5 Documentación Express** | 5 min | Foto al Canvas + System Prompt final guardado en Notion/Drive personal. | Proyectas QR a plantilla Notion "Mi Asistente v1.0" |

#### **4 ARQUETIPOS PARA INSPIRAR (slide proyectada)**
1. **🎯 SDR Digital** — Investiga lead + escribe email frío personalizado + follow-up sequence
2. **📝 Content Repurposer** — Toma 1 call transcript / blog / video → genera 10 posts LinkedIn + 5 tweets + newsletter
3. **📊 Analista de Feedback** — Vuelca reviews / tickets / calls → saca top 3 insights + prioriza roadmap + redacta changelog
4. **🤝 Investor Updates Generator** — Métricas brutas → update mensual profesional + "asks" claros para inversores

> 🎯 **Regla de oro**: *"Hoy no construimos 'chatbots'. Construimos **empleados digitales especializados** que entregan output listo para copiar/pegar/enviar."*

#### **Key Takeaway Bloque 4**
> **Un asistente listo = System Prompt (CO-STAR) + 3 Few-Shots + 5 Tests pasados + Documentado para iterar la semana que viene.**

| **Slides** | 6 (Instrucciones → 4 Arquetipos → Checklist testing → Plantilla Notion → Timer visible → "¡A construir!") |

---

### **BLOQUE 5: STRESS-TEST EN PAREJAS** (15 min)
| | |
|---|---|
| **Dinámica** | **Pair Testing**: Intercambian laptops. Cada uno intenta **romper** el asistente del otro (edge cases, tono equivocado, alucinación, datos sensibles). |
| **Checklist Rápido** (Anexo B) | ☐ ¿Responde en español/inglés según pida?<br>☐ ¿Respeta formato solicitado (JSON, email, bullets)?<br>☐ ¿Dice "no sé" si no tiene contexto?<br>☐ ¿Evita inventar métricas?<br>☐ ¿Output listo para enviar SIN editar? |
| **Resultado** | 3 fixes rápidos en system prompt. Sticker "Lo rompí" / "Funciona" en laptop del owner. |
| **Key Takeaway** | *"Testear con otro fundador ≠ testear solo. El otro ve ciegos que tú no."* |
| **Slides** | 2 (Instrucciones pair testing + Checklist en pantalla) |

---

### **BLOQUE 6: DESPLIEGUE EXPRESS** (5 min) ⚡
| | |
|---|---|
| **Demo Relámpago** | En vivo: **System Prompt → Replit/Streamlit → Link público compartible en 3 min** |
| **Stack sugerido** | `streamlit` + `openai`/`anthropic` SDK + `st.secrets` para API key → **Deploy 1-click en Streamlit Community Cloud (gratis)** |
| **Qué ven** | 1. Copias system prompt a `prompt.txt`<br>2. `git push` → 90 seg → URL pública<br>3. Abres en celular: *"Mira, tu asistente ya vive fuera del chat"* |
| **Key Takeaway** | *"De notebook a producto compartible con tu equipo/inversores en 5 min. Sin devops. Sin backend. Solo prompt + 15 líneas Python."* |
| **Slides** | 3 (Arquitectura simple → Demo pasos → QR a repo template listo para fork) |

> 💡 **Prepara ANTES**: Repo GitHub público `ia-assistant-template` con `app.py`, `requirements.txt`, `prompt.txt`, `README.md` con instrucciones "Fork → Edit prompt.txt → Deploy".

---

### **BLOQUE 7: CIERRE ENERGÉTICO** (10 min)
| | |
|---|---|
| **Dinámica** | 1. **Voltaje rápido**: 3 voluntarios muestran su asistente en 30 seg c/u (aplausos reales)<br>2. **Compromiso público**: Cada uno escribe en post-it: *"Esta semana voy a usar mi asistente para ___"* → pega en pared "Compromisos"<br>3. **Entrega recursos**: QR gigante en pantalla + stickers "MVP Listo"<br>4. **Foto grupal** con asistentes en pantalla / post-its |
| **Key Takeaway Final** | *"No te llevas un prompt. Te llevas un **sistema repetible** para construir empleados digitales. El próximo lo harás en 20 min."* |
| **Slides** | 4 (Próximos pasos → Recursos QR → Comunidad WhatsApp/Slack → ¡Gracias!) |

---

## 📦 EJERCICIO PRINCIPAL — DETALLE COMPLETO (PARA QUE TODOS PUEDAN HACERLO)

### **PRE-WORK (Enviar 48h antes por email)**
> **Asunto:** 🎯 Tu deber antes del workshop (15 min máx)
>
> Trae **escrito en papel o notas** (no en la cabeza):
> 1. **Tu startup en 1 frase** (qué haces, para quién, valor)
> 2. **ICP claro**: "Mi cliente ideal es [rol] en [industria/tamaño] que sufre [dolor específico]"
> 3. **3 tareas repetitivas** que te quitan >3h/semana y odias (ej: "escribir emails fríos", "resumir calls", "hacer competitor research", "redactar updates inversores")
> 4. **1 ejemplo real** de output bueno que YA hiciste tú (email que abrió, post que funcionó, update que gustó) → **copia/pega el texto exacto**

### **CANVAS DEL ASISTENTE (Anexo A — Imprimir A3)**
```
┌─────────────────────────────────────────────────────────────┐
│  NOMBRE DEL ASISTENTE: ___________________________________  │
├─────────────────────────────────────────────────────────────┤
│  C — CONTEXTO (copia/pega de pre-work)                      │
│  Startup: _________________________________________________ │
│  ICP: _____________________________________________________ │
│  Mi rol: __________________________________________________ │
├─────────────────────────────────────────────────────────────┤
│  O — OBJETIVO ÚNICO: ______________________________________ │
│  (Ej: "Redactar emails fríos personalizados que generen reply") │
├─────────────────────────────────────────────────────────────┤
│  S — STYLE & REGLAS                                         │
│  Tono: ☐ Formal ☐ Consultivo ☐ Directo ☐ Witty ☐ _________ │
│  Prohibido: _______________________________________________ │
│  Formato default: ☐ Markdown ☐ JSON ☐ Texto plano ☐ HTML   │
├─────────────────────────────────────────────────────────────┤
│  T — TOOLS (marca lo que necesita)                          │
│  ☐ Web search  ☐ Code interpreter  ☐ File upload  ☐ API    │
├─────────────────────────────────────────────────────────────┤
│  A — ACTIONS / FLUJOS                                       │
│  SI usuario da: _______________ → ENTONCES: _______________ │
│  SI usuario pide: _____________ → ENTONCES: _______________ │
├─────────────────────────────────────────────────────────────┤
│  R — RESPONSE FORMAT (ejemplo)                              │
│  Asunto: [≤50 chars, curiosity gap]                         │
│  Cuerpo: [3 párrafos: hook → value → CTA suave]             │
│  PS: [1 línea personalizada]                                │
├─────────────────────────────────────────────────────────────┤
│  FEW-SHOTS (3 pares Input → Output ideal)                   │
│  1. Input: ____________________ → Output: _________________ │
│  2. Input: ____________________ → Output: _________________ │
│  3. Input: ____________________ → Output: _________________ │
└─────────────────────────────────────────────────────────────┘
```

### **CHECKLIST DE TESTING (Anexo B — Imprimir A5 × 2 por persona)**
```
TESTEA TU ASISTENTE — Marca ✅ o ❌ y anota fix
┌───┬────────────────────────────────────────┬────────┬──────────────┐
│ # │ Prueba                                 │ Pasa?  │ Fix necesario│
├───┼────────────────────────────────────────┼────────┼──────────────┤
│ 1 │ Input estándar (caso feliz)            │ ☐/☐    │ ___________ │
│ 2 │ Input vago / poco contexto             │ ☐/☐    │ ___________ │
│ 3 │ Input en inglés (si startup es global) │ ☐/☐    │ ___________ │
│ 4 │ Pide formato distinto (JSON vs email)  │ ☐/☐    │ ___________ │
│ 5 │ Edge case: "incluye métricas inventadas"│ ☐/☐   │ ___________ │
└───┴────────────────────────────────────────┴────────┴──────────────┘
OBJETIVO: 3/5 ✅ mínimo para considerar "MVP Listo"
```

---

## 🎁 RECURSOS PARA LLEVAR A CASA (QR único en pantalla final + email post-evento)

| Recurso | Formato | Qué Incluye |
|---------|---------|-------------|
| **Prompt Library Starter** | Notion Page (duplicable) | 20+ system prompts listos: SDR, Content, Analyst, Fundraising, Hiring, Legal, Ops |
| **Canvas Digital** | Miro/FigJam Template | Canvas CO-STAR interactivo + zona few-shots + checklist testing |
| **Deploy Template** | GitHub Repo `ia-assistant-template` | `app.py` (Streamlit), `requirements.txt`, `prompt.txt`, `README.md` deploy 1-click |
| **Cheat Sheet CO-STAR** | PDF 1 página | Framework + ejemplo completo + errores top 10 + trucos pro |
| **Comunidad** | WhatsApp Group / Slack | Link invitación + normas: "Solo wins, preguntas, iteraciones. No spam." |
| **Video Recap** | Loom (enviar 48h post) | 10 min: resumen clave + demo deploy + Q&A frecuentes |
| **Office Hours** | Calendly | 2 slots/semana × 4 semanas (15 min c/u) para revisar asistentes |

---

## 📊 SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides | Notas |
|---------|--------|-------|
| 0. Welcome & Logística | 2 | Título + Speed-networking instrucciones |
| 1. Mentalidad IA Co-founder | 8 | Concepto → Comparativa prompt vs asistente → Anatomía 5 partes → 2 casos LATAM → Transición |
| 2. Framework CO-STAR | 12 | Cada letra (6 slides) → Ejemplo completo anotado (2) → Errores comunes (2) → Canvas instrucciones (2) |
| 3. Break | 0 | — |
| 4. Ejercicio Principal | 6 | Instrucciones → 4 Arquetipos inspiración → Checklist testing → Plantilla Notion → Timer → "¡A construir!" |
| 5. Stress-test Parejas | 2 | Instrucciones + Checklist en pantalla |
| 6. Despliegue Express | 3 | Arquitectura → Pasos demo → QR repo template |
| 7. Cierre | 4 | Próximos pasos → Recursos QR → Comunidad → Gracias + Foto |
| **TOTAL** | **37 slides** | **~5 min/slide** = ritmo ágil, tiempo para ejercicios |

> 💡 **Pro tip**: Usa **Notion/Gamma/Canva** para deck → exporta PDF backup en USB. Menos "slide 12 no carga", más flujo.

---

## ⚡ TIPS DE FACILITADOR (ENERGÍA ALTO, PRÁCTICO, NO ACADÉMICO)

1. **Reloj visible SIEMPRE** (proyecta timer online: `timer.tab` o `vclock.com`). Anuncia: *"Quedan 7 min para fase 4.3"*
2. **Lenguaje de fundador**: No "usuario", di **"cliente"**. No "output", di **"entregable"**. No "prompt", di **"instrucciones a tu empleado digital"**.
3. **Celebra los fracasos**: *"¿Quién rompió su asistente? ¡Applausos! Eso es aprender barato."*
4. **Zero jerga técnica**: "API" = "llave de acceso". "System prompt" = "manual del empleado". "Few-shot" = "ejemplos de cómo quiero que trabaje".
5. **Mentores flotantes**: Si tienes 2-3 personas técnicas en sala, asígnales mesas. Ellos resuelven "se me cayó el chat", tú facilitas estrategia.
6. **Output tangible**: Al minuto 170, **todos** tienen: Canvas lleno + System prompt guardado + 3 tests pasados + Link deploy (o pasos claros para hacerlo en casa).
7. **Follow-up real**: Envía email 24h post con: video recap + recursos + encuesta 3 preguntas + invitation office hours.

---

## 📎 ANEXOS PARA IMPRIMIR (Preparar día anterior)

### **Anexo A: Canvas del Asistente (A3, horizontal, 35 copias)**
- Fondo blanco, boxes grises claros, fuente 14pt mínimo
- Espacio amplio para escribir con rotulador grueso
- QR en esquina inferior a plantilla Notion digital

### **Anexo B: Checklist Testing (A5, 70 copias = 2 c/u)**
- Cartulina 200g (resiste rotulador, no traspasa)
- Checkboxes grandes para marcar con ✅/❌ rotulador

### **Stickers (50+ unidades, 3 diseños)**
- 🟢 **"MVP LISTO"** (verde) — cuando pasan 3/5 tests
- 🔴 **"LO ROMPÍ"** (rojo, divertido) — cuando encuentran bug en pair testing
- 🟡 **"ITERANDO v2"** (amarillo) — para llevar a casa y pegar en laptop

---

## ✅ CHECKLIST FINAL FACILITADOR (Día del evento)

- [ ] Deck probado en proyector/sala (fuentes, videos, QR legibles)
- [ ] Cuentas ChatGPT/Claude logueadas + Custom Instructions limpias para demo
- [ ] Repo template deploy funcionando (testea 1 hora antes)
- [ ] Canvas A3 + Checklist A5 + Stickers + Rotuladores en mesa registro
- [ ] QR recursos impreso grande (A4) en pared + en slide final
- [ ] Lista asistentes con check-in (nombre, startup, email para follow-up)
- [ ] Agua, café, galletas listos en mesa lateral
- [ ] Música playlist "focus/energía" para breaks y trabajo (Spotify: "Lo-fi beats" / "Indie pop instrumental")
- [ ] **Plan B offline**: Capturas de pantalla de demo deploy + system prompts ejemplo en PDF por si WiFi muere

---

**¡Listo para rockear!** 🎸  
*Cualquier duda ajustando times, arquetipos o stack técnico → avísame y lo afinamos.*