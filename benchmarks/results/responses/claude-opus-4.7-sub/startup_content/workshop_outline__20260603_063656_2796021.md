# Claude Opus 4.7 (suscripción) — startup_content/workshop_outline

- model_id: `claude-opus-4-7`
- success: True  | final: 7.03 | quality: 10.0
- latency_total: 95.307s | tokens_per_second: 60.6
- input_tokens: 6 | output_tokens: 5779
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, cubriendo todos los aspectos solicitados con detalles prácticos y organización.

## Respuesta completa

# Workshop: Construye tu Asistente de IA para tu Startup
### Workshop Práctico Presencial · 3 horas · 20-30 emprendedores

---

## Filosofía del workshop

> **"Salen con un asistente funcionando o no salen."**

Cero teoría innecesaria. Cero "el futuro de la IA". Cada minuto debe acercar al participante a tener un asistente real corriendo en su celular o laptop antes de irse.

---

## 1. Materiales necesarios (preparar 48h antes)

### Para el facilitador
- [ ] Laptop con proyector + cable HDMI/USB-C + adaptador de respaldo
- [ ] Pizarra blanca o papelógrafo + 4 marcadores
- [ ] Timer visible para todos (app proyectada o reloj físico grande)
- [ ] **Cuenta demo gratuita pre-creada** en la plataforma que se va a usar (sugerido: ChatGPT free + Claude.ai free + un agente N8N pre-armado de respaldo)
- [ ] Plan B offline: PDF con screenshots de cada paso por si cae el WiFi
- [ ] 3-5 ejemplos reales de asistentes funcionando (uno comercial, uno operativo, uno de soporte)

### Para los participantes (enviar 72h antes por email)
- [ ] Traer laptop **cargada** + cargador
- [ ] Crear cuenta gratuita en **ChatGPT** y **Claude.ai** antes del workshop (link directo + tutorial de 2 min en video)
- [ ] Llegar con **1 dolor operativo concreto** de su startup escrito en una hoja (ej: "respondo 30 emails iguales por semana")
- [ ] Tarjeta de crédito **opcional** (solo si quieren probar versión paga el mismo día)

### Logística sala
- [ ] Mesas en grupos de 4-5 personas (NO filas tipo aula)
- [ ] WiFi probado con 30 dispositivos simultáneos (clave: hacer test real previo)
- [ ] Café + agua + snacks disponibles todo el tiempo (no parar el flow para "coffee break")
- [ ] Cartel en la entrada: *"Hoy sales con tu asistente funcionando"*

### Material impreso (1 por persona)
- [ ] **Worksheet "Mi Asistente de IA"** (1 hoja, doble cara) — guía paso a paso del ejercicio principal
- [ ] **Cheat sheet de prompts** (1 hoja) — 10 plantillas listas para copiar-pegar
- [ ] **Sticker o tarjeta** con QR al grupo de WhatsApp/Skool de seguimiento

---

## 2. Agenda Detallada (180 minutos)

| Bloque | Tiempo | Duración | Tipo |
|---|---|---|---|
| 0. Bienvenida y energía | 0:00 - 0:10 | 10 min | Icebreaker |
| 1. El problema real | 0:10 - 0:25 | 15 min | Charla + discusión |
| 2. Demo: 3 asistentes reales | 0:25 - 0:45 | 20 min | Demo en vivo |
| 3. Anatomía de un asistente | 0:45 - 1:05 | 20 min | Charla práctica |
| **Stretch break** | 1:05 - 1:10 | 5 min | Pausa activa |
| 4. **EJERCICIO PRINCIPAL: Construye el tuyo** | 1:10 - 2:25 | 75 min | Hands-on |
| 5. Showcase + feedback peer | 2:25 - 2:45 | 20 min | Demos grupales |
| 6. Próximos pasos + comunidad | 2:45 - 3:00 | 15 min | Cierre |

---

## 3. Detalle por Bloque

### Bloque 0 · Bienvenida y energía (10 min)

**Slides estimados:** 3

- **Objetivo:** Romper la formalidad y alinear expectativas. Que entiendan que esto NO es una charla.
- **Dinámica:**
  - (3 min) Saludo + regla única: *"Si no entendiste algo, levanta la mano AHORA, no después."*
  - (5 min) Icebreaker rápido: cada persona en su mesa de 4 dice en **30 segundos** su startup + el dolor operativo que trajo escrito
  - (2 min) Mostrar el cartel: *"A las 3 horas, sales con un asistente funcionando."*
- **Key takeaway:** Esto es un taller, no una charla. Vas a construir, no escuchar.

---

### Bloque 1 · El problema real (15 min)

**Slides estimados:** 5

- **Objetivo:** Conectar emocionalmente con el problema que la IA resuelve (NO vender IA).
- **Dinámica:**
  - (5 min) Charla corta: *"¿Cuántas horas a la semana hacés tareas que cualquiera podría hacer?"* — usar datos reales de founders LATAM
  - (5 min) Discusión en mesa: cada uno responde 3 preguntas en su worksheet:
    1. ¿Qué tarea repetitiva te roba más tiempo?
    2. ¿Qué pregunta te hacen tus clientes 10 veces por semana?
    3. ¿Qué proceso te frena para escalar?
  - (5 min) Compartir 3-4 respuestas con toda la sala (mano alzada)
- **Key takeaway:** Un asistente de IA no es magia futurista. Es un empleado virtual que responde lo repetitivo para que vos hagas lo estratégico.

---

### Bloque 2 · Demo: 3 asistentes reales (20 min)

**Slides estimados:** 4 (mayormente pantalla compartida en vivo)

- **Objetivo:** Que vean asistentes REALES funcionando con resultados medibles, no slides teóricos.
- **Dinámica:** Demo en vivo de 3 casos (6 min cada uno + 2 min Q&A total):
  1. **Asistente comercial**: responde leads por WhatsApp 24/7 (mostrar caso real con números: X leads, Y conversiones)
  2. **Asistente operativo**: clasifica emails y los responde con plantillas personalizadas
  3. **Asistente de contenido**: genera posts para LinkedIn desde una idea cruda
- Mostrar siempre: **input → asistente → output → cuánto tiempo ahorra a la semana**
- **Key takeaway:** No necesitás ser técnico. Necesitás claridad sobre QUÉ querés que haga tu asistente.

---

### Bloque 3 · Anatomía de un asistente (20 min)

**Slides estimados:** 8

- **Objetivo:** Dar el framework mental simple para diseñar CUALQUIER asistente.
- **Dinámica:** Charla práctica con la fórmula:

  > **ROL + CONOCIMIENTO + INSTRUCCIONES + EJEMPLOS = Asistente**

  - **ROL** → ¿quién es? (ej: "Sos el agente comercial de una marca de café especialidad")
  - **CONOCIMIENTO** → ¿qué sabe? (productos, precios, FAQs)
  - **INSTRUCCIONES** → ¿cómo se comporta? (tono, qué hacer si no sabe, cuándo escalar a humano)
  - **EJEMPLOS** → 2-3 conversaciones ideales

- Mostrar en pantalla un asistente mal hecho vs uno bien hecho con la fórmula
- **Key takeaway:** Si tu asistente no funciona, no es culpa de la IA. Es que le faltó uno de los 4 ingredientes.

---

### Stretch break (5 min)

Música, parar de mirar pantalla, ir al baño, recargar café. **No es opcional**, es para que vengan frescos al bloque más importante.

---

### Bloque 4 · EJERCICIO PRINCIPAL: Construye tu asistente (75 min)

**Slides estimados:** 6 (instrucciones paso a paso visibles todo el tiempo)

- **Objetivo:** Que CADA participante salga con UN asistente funcional probado.
- **Dinámica:** Hands-on guiado con facilitador caminando entre mesas.

#### Fase 1 — Define tu asistente (15 min)
Cada participante completa la fórmula en su worksheet usando el dolor que trajo:
- ¿Cuál es el ROL?
- ¿Qué necesita SABER?
- ¿Cómo se debe COMPORTAR?
- Escribir 2 ejemplos de conversación ideal

#### Fase 2 — Construye (30 min)
- Abrir **ChatGPT** (free funciona) → crear un **GPT personalizado** o usar Claude.ai con **Projects**
- Pegar el ROL en las instrucciones
- Subir 1-3 documentos como CONOCIMIENTO (catálogo, FAQ, manual)
- Configurar el comportamiento

> 🚨 **Regla de oro del bloque:** "Funcional > Perfecto". Versión 1 hoy, versión 2 mañana.

#### Fase 3 — Prueba y rompe (20 min)
- Cada persona prueba SU asistente con 5 preguntas reales
- Intercambia laptops con el compañero de mesa: **rómpele el asistente** (preguntas raras, fuera de tema, edge cases)
- Anota qué falló y ajusta instrucciones

#### Fase 4 — Documenta el ROI (10 min)
En el worksheet:
- ¿Cuántas horas a la semana te ahorra esto?
- ¿Cuánto vale tu hora?
- ROI mensual estimado

- **Key takeaway:** Pasaste de "quiero usar IA" a "tengo un asistente probado con ROI calculado" en 75 minutos.

---

### Bloque 5 · Showcase + feedback peer (20 min)

**Slides estimados:** 2

- **Objetivo:** Cerrar con energía, aprender de otros casos, generar comunidad.
- **Dinámica:**
  - (12 min) **6 voluntarios** demuestran su asistente en pantalla grande (90 seg cada uno + 30 seg de feedback de la sala)
  - (8 min) Discusión abierta: *"¿Qué patrón ven en los asistentes que funcionaron mejor?"* — facilitador anota en pizarra
- **Key takeaway:** Ver 6 asistentes distintos resueltos te da 6 ideas más para tu propia startup.

---

### Bloque 6 · Próximos pasos + comunidad (15 min)

**Slides estimados:** 4

- **Objetivo:** Que NO se vayan al vacío post-workshop. Convertir entusiasmo en hábito.
- **Dinámica:**
  - (5 min) Mostrar **roadmap de evolución** del asistente:
    - Hoy: ChatGPT/Claude personalizado
    - Semana 2: conectarlo a WhatsApp Business (mostrar herramientas no-code)
    - Mes 1: automatización con N8N o Make
    - Mes 3: asistente propio embebido en su web
  - (5 min) Compartir recursos para llevar a casa (siguiente sección)
  - (5 min) **Compromiso público**: cada uno dice en voz alta UNA acción específica que va a hacer en las próximas 48h
- **Key takeaway:** El workshop no termina hoy. Empieza hoy.

---

## 4. Ejercicio Principal (resumen visual)

```
┌─────────────────────────────────────────────────┐
│  🛠  CONSTRUYE TU ASISTENTE - 75 MINUTOS          │
├─────────────────────────────────────────────────┤
│                                                  │
│  15 min · DEFINIR    → Worksheet ROL/SABER/...   │
│  30 min · CONSTRUIR  → GPT personalizado/Project │
│  20 min · PROBAR     → Tu compañero lo rompe     │
│  10 min · ROI        → Calcular ahorro mensual   │
│                                                  │
│  ✅ Sales con: 1 asistente funcional + ROI       │
└─────────────────────────────────────────────────┘
```

**Output garantizado por participante:**
- ✅ Asistente personalizado funcionando en su cuenta (queda guardado)
- ✅ Worksheet completa con su caso documentado
- ✅ ROI mensual calculado para presentar a su socio/equipo
- ✅ Lista de 3 mejoras para implementar en la semana

---

## 5. Recursos para llevar a casa

Enviar por email **el mismo día** del workshop (no dejar para "después"):

### Kit digital (Notion/Drive compartido)
- 📄 **Cheat sheet de 10 prompts** para asistentes (comercial, soporte, contenido, operativo)
- 🎥 **Video de 5 min**: cómo conectar tu asistente a WhatsApp Business
- 📋 **Plantilla Notion**: "Backlog de mi asistente" (qué mejorar semana a semana)
- 🔗 **Lista curada de herramientas** con tier gratuito: ChatGPT, Claude, N8N, Make, Manychat
- 📊 **Calculadora ROI** (Google Sheets) para justificar el costo a su equipo
- 📚 **Glosario sin tecnicismos**: 15 términos que van a escuchar (LLM, RAG, agente, tool calling)

### Comunidad de seguimiento
- 💬 **Grupo de WhatsApp o comunidad Skool** del workshop
  - Compromiso: el facilitador responde dudas durante 30 días
  - Reto semanal: compartir mejora del asistente cada lunes
- 📅 **Sesión de Q&A gratuita** a los 14 días (asegurar que sigan iterando)

### Próximo nivel (opcional, soft pitch al final)
- Workshop avanzado: "Automatiza tu startup con N8N + IA"
- Mentorías 1:1
- Comunidad premium

---

## 6. Resumen Slide Count

| Bloque | Slides estimados |
|---|---|
| 0. Bienvenida | 3 |
| 1. Problema real | 5 |
| 2. Demo asistentes | 4 |
| 3. Anatomía | 8 |
| 4. Ejercicio (instrucciones) | 6 |
| 5. Showcase | 2 |
| 6. Cierre + recursos | 4 |
| **Total** | **~32 slides** |

> 💡 **Regla**: Promedio 1 slide cada ~5 min. Si necesitás más, sobra contenido. Si necesitás menos, hay que sumar imágenes/visual.

---

## Checklist de éxito del facilitador

Al final del workshop, **mide estas 4 cosas**:

1. ✅ **¿Cuántos participantes tienen un asistente funcionando antes de irse?** → meta: 90%+
2. ✅ **¿Cuántos pueden explicar la fórmula ROL+CONOCIMIENTO+INSTRUCCIONES+EJEMPLOS?** → meta: 100%
3. ✅ **¿Cuántos se unen al grupo de WhatsApp/Skool?** → meta: 80%+
4. ✅ **NPS del workshop (1 pregunta al salir):** *"¿Lo recomendarías a otro emprendedor?"* → meta: 9+

---

## Tips finales para el facilitador

- 🔥 **Energía alta primeros 10 min** define el resto del workshop
- 🚫 **Cero jerga técnica innecesaria** — si decís "LLM" sin explicar, perdés al 60% de la sala
- 👂 **Caminar entre mesas durante el ejercicio** — no quedarse atrás del proyector
- 🆘 **Tener 2 ayudantes** si la sala tiene 25+ personas (técnico imposible solo)
- ⏰ **Cumplir el tiempo religiosamente** — emprendedores valoran que respetes su agenda
- 📸 **Foto grupal al final** con todos mostrando su asistente en pantalla → contenido orgánico para redes

---

**Recordá:** El éxito del workshop no se mide en cuánto aprendieron, sino en **cuántos asistentes siguen vivos a los 30 días**. Diseñá todo el material apuntando a esa métrica.