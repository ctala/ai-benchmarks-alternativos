# GPT-OSS 20B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.21 | quality: 10.0
- latency_total: 24.494s | tokens_per_second: 113.3
- input_tokens: 237 | output_tokens: 2776
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y materiales necesarios para un workshop práctico.

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

**Workshop presencial**  
*“Construye tu Asistente de IA para tu Startup – Workshop Práctico”*  
**Duración:** 3 h (180 min)  
**Audiencia:** 20‑30 emprendedores early‑stage, sin experiencia técnica.  
**Tono:** Energético, hands‑on, sin tecnicismos académicos.

---

## 1️⃣ Agenda Detallada (3 h)

| Hora | Bloque | Duración | Dinámica | Key Takeaway |
|------|--------|----------|----------|--------------|
| 0:00–0:10 | **Apertura & Expectativas** | 10 min | Charla rápida + ice‑breaker (“¿Qué es la IA para ti?”) | Todos alineados con objetivos y reglas del día. |
| 0:10–0:25 | **¿Qué es un Asistente de IA?** | 15 min | Mini‑demo + storytelling con ejemplos reales (ChatGPT, Alexa, Google Assistant). | Comprender la gama de posibilidades y el impacto en startups. |
| 0:25–0:45 | **Identifica tu Oportunidad** | 20 min | Ejercicio en grupos: “Mapa de procesos” + “Problema‑valor‑IA”. | Cada equipo define un caso de uso concreto (FAQ, soporte, lead‑qual). |
| 0:45–1:15 | **Herramientas sin Código** | 30 min | Demo paso‑a‑paso: OpenAI API, Zapier, Make, Typebot, Notion + AI. | Saber qué stack usar sin escribir código. |
| 1:15–1:30 | **Break & Networking** | 15 min | Café, refrescos, posteos en redes. | Recarregar energías y conectar con otros emprendedores. |
| 1:30–2:15 | **Taller Práctico: Construye tu Asistente** | 45 min | Ejercicio principal: “Crea un asistente FAQ” con ChatGPT + Zapier. | Producto mínimo viable que responde preguntas en tiempo real. |
| 2:15–2:35 | **Integración en tu Startup** | 20 min | Discusión guiada: canales (WhatsApp, Slack, web) + métricas. | Plan de despliegue y métricas de éxito. |
| 2:35–2:50 | **Roadmap & Próximos Pasos** | 15 min | Visualización de “Next 30/60/90 days” con checklist. | Cada emprendedor tiene un plan de acción concreto. |
| 2:50–3:00 | **Cierre & Recursos** | 10 min | Feedback rápido + entrega de material de apoyo. | Acceso a recursos y comunidad post‑workshop. |

---

## 2️⃣ Materiales Necesarios (para preparar antes)

| Ítem | Descripción | Cómo prepararlo |
|------|-------------|-----------------|
| **Equipos** | Laptop/PC con conexión a internet | Cada participante trae su propio portátil. |
| **Cuentas** | OpenAI (API key), Zapier, Make, Typebot, Slack/WhatsApp Business | Se invita a crear cuentas gratuitas antes del día. Los enlaces se comparten 48 h antes. |
| **Documentación** | PDF de “Guía rápida de IA sin código” + “Plantilla de caso de uso” | Se envían por email con 1 semana de anticipación. |
| **Material de la sala** | Proyector, pantalla, pizarras digitales, marcadores | Se coordina con el lugar de alquiler. |
| **Snacks & Bebidas** | Café, té, agua, snacks ligeros | Se reserva un kit de “refrescos energéticos”. |

---

## 3️⃣ Bloques Detallados

| Bloque | Duración | Objetivo | Dinámica | Key Takeaway |
|--------|----------|----------|----------|--------------|
| **Apertura & Expectativas** | 10 min | Establecer el objetivo y crear un ambiente colaborativo. | Charla + ice‑breaker (“IA y tu startup”) | Todos saben qué se busca y la dinámica del día. |
| **¿Qué es un Asistente de IA?** | 15 min | Entender el concepto y el ecosistema de asistentes. | Mini‑demo + ejemplos (ChatGPT, Alexa, Chatbot de Shopify). | IA puede ser un asistente interno y externo sin código. |
| **Identifica tu Oportunidad** | 20 min | Definir un caso de uso que aporte valor a la startup. | Brainstorm “Mapa de procesos” + “Problema‑valor‑IA” en grupos pequeños. | Cada equipo tiene un “pain point” que la IA puede resolver. |
| **Herramientas sin Código** | 30 min | Conocer stack práctico y barato. | Demo de Zapier + OpenAI + Typebot, con ejemplos de flujo. | Se aprende a conectar APIs sin escribir líneas de código. |
| **Break & Networking** | 15 min | Recarregar energías y crear comunidad. | Café + actividades de “speed networking” 2‑minutos. | Los participantes comparten ideas y potenciales partners. |
| **Taller Práctico: Construye tu Asistente** | 45 min | Crear un asistente FAQ funcional. | Paso a paso: <br>1. Define preguntas frecuentes. <br>2. Configura Zapier → OpenAI. <br>3. Prueba en Slack/WhatsApp. | Al final, cada equipo tiene un asistente que funciona. |
| **Integración en tu Startup** | 20 min | Mapear cómo el asistente se inserta en el flujo de negocio. | Discusión guiada + checklist de canales, métricas, soporte. | Se genera un plan de despliegue y seguimiento. |
| **Roadmap & Próximos Pasos** | 15 min | Convertir aprendizaje en acción. | Visualizar “Next 30/60/90 days” con hitos y métricas. | Cada participante sale con un roadmap accionable. |
| **Cierre & Recursos** | 10 min | Consolidar aprendizajes y ofrecer soporte continuo. | Feedback rápido + entrega de material de apoyo. | Acceso a repositorios, foros, y comunidad de usuarios. |

---

## 4️⃣ Ejercicio Principal

**“Crea tu Asistente FAQ”**  
Cada equipo construirá un asistente que responda automáticamente a las preguntas frecuentes de su producto o servicio. Se usará:

1. **OpenAI ChatGPT** (modelo LLM)  
2. **Zapier** (conexión a Slack, WhatsApp, o sitio web)  
3. **Plantilla de Preguntas** (proporcionada en el material)

**Pasos**:

1. **Define** 5‑10 preguntas frecuentes.  
2. **Crea** un Zap: Evento (mensaje en Slack/WhatsApp) → Acción (ChatGPT → respuesta).  
3. **Prueba** el flujo con usuarios internos.  
4. **Itera**: ajusta prompts, añade lógica de fallback.  
5. **Entrega**: cada equipo presenta su asistente funcional y comparte la URL/ejemplo de chat.

---

## 5️⃣ Recursos para Llevar a Casa

| Tipo | Enlace | Descripción |
|------|--------|-------------|
| **Plantilla de Caso de Uso** | `link` | Hoja de cálculo para mapear procesos y oportunidades IA. |
| **Guía rápida de IA sin código** | `link` | PDF con pasos y tips para Zapier + OpenAI. |
| **Cheat Sheet Prompt** | `link` | Lista de prompts efectivos para ChatGPT. |
| **Repositorios de Ejemplos** | `link` | GitHub con scripts de Zapier y Typebot. |
| **Comunidad** | `link` | Grupos de Slack/Discord para usuarios de IA sin código. |
| **Checklist de Despliegue** | `link` | PDF con pasos de integración y métricas. |
| **Curso gratuito** | `link` | Mini‑curso en línea de 2 h sobre IA sin código. |

---

## 6️⃣ Slide Count Estimado por Sección

| Sección | Slides |
|---------|--------|
| Apertura & Expectativas | 4 |
| ¿Qué es un Asistente de IA? | 5 |
| Identifica tu Oportunidad | 6 |
| Herramientas sin Código | 7 |
| Break & Networking | 2 |
| Taller Práctico: Construye tu Asistente | 8 |
| Integración en tu Startup | 5 |
| Roadmap & Próximos Pasos | 4 |
| Cierre & Recursos | 3 |
| **Total** | **44 slides** |

> *Los slides son “visuales + bullets” para evitar lecturas largas; cada slide tiene 1‑2 ideas clave.*

---

### 🎉 ¡Listo!  
Con este outline, tu workshop de 3 h será dinámico, práctico y entregará a los emprendedores una herramienta tangible que pueden implementar inmediatamente en sus startups. ¡Éxitos en la facilitación!