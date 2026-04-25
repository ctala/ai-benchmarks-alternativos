# Claude Opus 4.6 — startup_content/workshop_outline

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.13 | quality: 9.24
- latency_total: 46.832s | tokens_per_second: 43.7
- input_tokens: 237 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa



# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico — Outline Completo (3 horas)

---

## 📋 1. FICHA TÉCNICA DEL WORKSHOP

| Campo | Detalle |
|-------|---------|
| **Duración** | 3 horas (180 minutos) |
| **Audiencia** | 20-30 emprendedores early-stage, no-técnicos |
| **Nivel** | Principiante (cero código) |
| **Formato** | Presencial, mesas de 5-6 personas |
| **Resultado prometido** | Cada participante sale con un asistente de IA funcional, configurado y listo para usar en su startup |

---

## 📦 2. MATERIALES NECESARIOS

### Lo que prepara el facilitador ANTES del workshop:

**Tecnología y espacio:**
- [ ] Wi-Fi estable y testeado (publicar nombre y clave en cada mesa)
- [ ] Proyector/pantalla grande + adaptadores
- [ ] Parlantes (para los videos/demos)
- [ ] Extensiones eléctricas en cada mesa (mínimo 2 por mesa)
- [ ] Laptop del facilitador con las demos pre-cargadas
- [ ] Cuenta de ChatGPT Plus activa para demo en vivo
- [ ] Cuentas de respaldo en Claude, Gemini (por si falla algo)

**Materiales físicos:**
- [ ] Hojas de trabajo impresas — "Canvas del Asistente IA" (1 por persona)
- [ ] Hojas de trabajo impresas — "Biblioteca de Prompts" (1 por persona)
- [ ] Hojas de trabajo impresas — "Checklist de Implementación" (1 por persona)
- [ ] Post-its de 3 colores (amarillo, verde, rosa) — 1 block por mesa
- [ ] Marcadores gruesos (2-3 por mesa)
- [ ] Stickers/pegatinas para votación (5 por persona)
- [ ] Timer visible (pantalla secundaria o reloj grande)

**Lo que traen los participantes:**
- [ ] Laptop con carga completa
- [ ] Cuenta gratuita creada en ChatGPT (enviar instrucciones 48h antes)
- [ ] Cuenta gratuita creada en Claude (enviar instrucciones 48h antes)
- [ ] Una descripción breve de su startup (enviar template 48h antes)

**Comunicación previa (48 horas antes):**
- Email con: instrucciones de cuentas, qué traer, template "Describe tu startup en 5 líneas", expectativas del workshop

---

## 🗓️ 3. AGENDA DETALLADA

```
MINUTO    BLOQUE                                    TIPO
─────────────────────────────────────────────────────────────
0:00      Apertura y Rompe-hielo                    Dinámica
0:15      Bloque 1: La IA como Co-Founder           Charla + Demo
0:40      Bloque 2: Anatomía de un Gran Prompt      Charla + Ejercicio
1:10      Bloque 3: Diseña tu Asistente (Canvas)    Ejercicio grupal
1:40      ☕ BREAK                                   Descanso
1:50      Bloque 4: Construye tu Asistente EN VIVO  Ejercicio principal
2:35      Bloque 5: Showcase & Feedback             Presentaciones
2:50      Cierre: Tu Plan de Acción de 7 días       Reflexión + Cierre
3:00      FIN
```

---

## 🔬 4. DESGLOSE POR BLOQUE

---

### 🎬 APERTURA Y ROMPE-HIELO
**⏱️ Duración: 15 minutos (0:00 - 0:15)**
**📊 Slides: 5**

**Objetivo:**
Crear energía, romper el hielo, nivelar expectativas y detectar el nivel real del grupo.

**Dinámica:**

| Min | Actividad | Detalle |
|-----|-----------|---------|
| 0-3 | **Bienvenida energética** | Facilitador se presenta en 60 segundos. Reglas del workshop: "Esto NO es una clase. Es un taller. Van a ensuciarse las manos." |
| 3-8 | **Rompe-hielo: "La IA y yo"** | Cada persona se pone de pie. El facilitador lee afirmaciones y los participantes se mueven a zonas del salón: **"Ya usé ChatGPT" → izquierda / "Nunca lo abrí" → derecha / "Lo uso todos los días" → centro.** Se hacen 4 rondas rápidas. Genera risas, movimiento y el facilitador mapea al grupo. |
| 8-12 | **Encuadre de expectativas** | "Hoy NO van a aprender a programar. Van a aprender a PENSAR con IA y van a salir con algo funcionando." Mostrar el ANTES/DESPUÉS del workshop. |
| 12-15 | **Presentación relámpago en mesas** | Cada persona en su mesa dice: nombre, startup, y "la tarea que más odio hacer en mi negocio". 30 segundos cada uno. Anotan la tarea odiada en un post-it amarillo y lo pegan en la mesa. |

**Key Takeaway:**
> *"Esa tarea que odian hacer... hoy le van a crear un asistente para que la haga por ustedes."*

**Notas para el facilitador:**
- La energía de los primeros 5 minutos define todo el workshop. Arranca de pie, con música, con volumen.
- El rompe-hielo físico (moverse por el salón) es intencional: rompe la inercia de "me siento y escucho".

---

### 📘 BLOQUE 1: LA IA COMO CO-FOUNDER INVISIBLE
**⏱️ Duración: 25 minutos (0:15 - 0:40)**
**📊 Slides: 12**

**Objetivo:**
Que entiendan QUÉ puede hacer la IA hoy (y qué no), y que vean ejemplos reales de startups latinoamericanas usándola. Eliminar el miedo y el hype simultáneamente.

**Dinámica:**

| Min | Actividad | Tipo | Detalle |
|-----|-----------|------|---------|
| 15-22 | **Mini-charla: "Qué es realmente un LLM"** | Charla con slides | Explicación con analogía: *"Es como un pasante super inteligente que leyó todo internet, pero que necesita instrucciones MUY claras porque no conoce TU negocio."* Cubrir: qué hace bien (texto, análisis, ideas, código), qué hace mal (datos en tiempo real, matemáticas exactas, decisiones críticas). Sin jerga técnica. |
| 22-28 | **3 Casos reales LATAM** | Storytelling con capturas | **Caso 1:** Startup de delivery en Colombia que usa IA para responder WhatsApp de clientes (ahorra 4h/día). **Caso 2:** Emprendedora en México que usa Claude para crear todo su contenido de redes (de 8h/semana a 2h). **Caso 3:** SaaS en Argentina que usa GPT para onboarding automatizado de usuarios. Mostrar capturas reales, números reales. |
| 28-35 | **Demo en vivo: "De cero a asistente en 3 minutos"** | Demo live | El facilitador abre ChatGPT, crea un asistente de atención al cliente para una tienda ficticia EN VIVO. Muestra el prompt, la respuesta, itera una vez. El público ve la magia en tiempo